#!/usr/bin/env python3
"""Validate the catalog and generated artifacts; optionally check public links.

No third-party environment or model code is executed. Network failures remain
visible and produce a non-zero exit status instead of silently passing.
"""
import argparse
from collections import Counter
import concurrent.futures
import datetime as dt
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlparse, urldefrag

from render_readme import ROOT, LEVELS, CODE, activity, load, outputs

KINDS = {'blog', 'paper', 'project', 'report'}
ENV_TYPES = {'executable', 'procedural', 'neural', 'desktop', 'browser', 'mobile', 'game', 'mixed'}
LINK_RE = re.compile(r'(?<!!)\[[^\]\n]*\]\(([^\s)]+)\)')

def valid_date(value):
    try:
        return isinstance(value, str) and dt.date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False

def valid_url(value):
    return isinstance(value, str) and urlparse(value).scheme in {'http', 'https'} and bool(urlparse(value).netloc)

def validate_data(data):
    errors, warnings = [], []
    meta = data.get('catalog', {})
    as_of = meta.get('as_of', '')
    if not valid_date(as_of):
        return ['catalog.as_of must be an ISO date'], warnings
    categories = [c['id'] for c in data.get('categories', [])]
    if len(categories) != len(set(categories)):
        errors.append('Duplicate category IDs')
    for c in data.get('categories', []):
        if not c.get('name_en') or not c.get('name_zh'):
            errors.append(f"Category {c['id']} missing bilingual names")
    groups = [g['id'] for g in data.get('groups', [])]
    if not groups or len(groups) != len(set(groups)):
        errors.append('Missing or duplicate major groups')
    for g in data.get('groups', []):
        if not g.get('name_en') or not g.get('name_zh'):
            errors.append('Major group missing bilingual names')
    for c in data.get('categories', []):
        if c.get('parent') not in groups:
            errors.append(f"Category {c['id']}: invalid parent group")
    assignments = {}
    for e in data.get('entries', []):
        assignments.setdefault(e.get('work_id'), set()).add(e.get('category'))
    for work, placements in assignments.items():
        if len(placements) != 1:
            errors.append(f'{work}: work has inconsistent category placement')
    ids, urls = set(), set()
    required = ['id', 'work_id', 'kind', 'name', 'title', 'url', 'category', 'environment_type',
                'evidence_type', 'summary_en', 'summary_zh', 'limitation_en', 'limitation_zh',
                'reviewed_at', 'evidence']
    for e in data.get('entries', []):
        eid = e.get('id', '<missing>')
        for field in required:
            if not e.get(field):
                errors.append(f'{eid}: missing {field}')
        if eid in ids:
            errors.append(f'{eid}: duplicate ID')
        ids.add(eid)
        if e.get('catalog_scope')=='background':
            if e.get('featured_blog') or e.get('kind')!='blog':
                errors.append(f'{eid}: background article cannot be featured or non-blog')
            if not all(e.get('scope_reason_'+lang) for lang in ['en','zh']):
                errors.append(f'{eid}: background article needs bilingual scope reasons')
        if e.get('featured_blog'):
            if e.get('blog_theme') not in {t['id'] for t in data.get('company_blog_themes',[])}:
                errors.append(f'{eid}: missing/invalid core blog theme')
            if not all(e.get('research_question_'+lang) and e.get('core_contents_'+lang) for lang in ['en','zh']):
                errors.append(f'{eid}: core blog needs a question and concrete contents in both languages')
        key = (e.get('kind'), str(e.get('url', '')).lower().rstrip('/'))
        if key in urls:
            errors.append(f'{eid}: duplicate resource URL within kind')
        urls.add(key)
        if e.get('kind') not in KINDS:
            errors.append(f'{eid}: invalid kind')
        if e.get('category') not in categories:
            errors.append(f'{eid}: invalid category')
        if e.get('environment_type') not in ENV_TYPES:
            errors.append(f'{eid}: invalid environment_type')
        if e.get('evidence_type') not in LEVELS:
            errors.append(f'{eid}: invalid evidence type')
        if not valid_url(e.get('url')):
            errors.append(f'{eid}: invalid URL')
        for artifact in e.get('artifacts', []):
            if not artifact.get('name_en') or not artifact.get('name_zh') or not valid_url(artifact.get('url')):
                errors.append(f'{eid}: incomplete companion artifact')
        if e.get('homepage_url') and not valid_url(e['homepage_url']):
            errors.append(f'{eid}: invalid homepage URL')
        if e.get('kind') == 'report' and not e.get('report_sections'):
            errors.append(f'{eid}: model report needs section locations')
        if e.get('report_sections'):
            if not e.get('report_version') or not valid_url(e.get('pdf_url')):
                errors.append(f'{eid}: report needs version and PDF URL')
            section_ids = set()
            for section in e['report_sections']:
                pages = section.get('pdf_pages', [])
                if not section.get('section') or not section.get('title') or not valid_url(section.get('url')) or not urlparse(section['url']).fragment:
                    errors.append(f'{eid}: incomplete report section locator')
                if not pages or any(not isinstance(p, int) or p < 1 for p in pages) or pages != sorted(set(pages)):
                    errors.append(f'{eid}: invalid PDF page range')
                if not section.get('summary_en') or not section.get('summary_zh'):
                    errors.append(f'{eid}: missing bilingual section content')
                if section.get('section') in section_ids:
                    errors.append(f'{eid}: duplicate report section')
                section_ids.add(section.get('section'))
        for field in ['published', 'reviewed_at']:
            value = e.get(field)
            if value is not None and (not valid_date(value) or value > as_of):
                errors.append(f'{eid}: invalid/future {field}: {value}')
        for ev in e.get('evidence', []):
            if not valid_url(ev.get('url')) or not ev.get('excerpt') or not ev.get('method'):
                errors.append(f'{eid}: incomplete evidence')
            if not valid_date(ev.get('reviewed_at')) or ev['reviewed_at'] > as_of:
                errors.append(f'{eid}: invalid evidence review date')
            if len(ev.get('excerpt', '').split()) > 25:
                errors.append(f'{eid}: evidence excerpt exceeds 25 words')
        if e.get('kind') in {'paper', 'report'}:
            if not e.get('authors') or (e['kind'] == 'paper' and not e.get('published')):
                errors.append(f'{eid}: paper needs authors and first submission date')
            if e['kind'] == 'report' and not e.get('published'):
                warnings.append(f'{eid}: first publication date unconfirmed')
            status = e.get('code_status')
            if status not in CODE:
                errors.append(f'{eid}: invalid code status')
            has_code = bool(e.get('code_url'))
            if has_code != (status in {'author-linked', 'partial-or-associated', 'empty-repository'}):
                errors.append(f'{eid}: code URL/status mismatch')
            if has_code and not valid_url(e.get('code_evidence_url')):
                errors.append(f'{eid}: code needs ownership evidence')
            if status in {'not-confirmed', 'partial-or-associated', 'empty-repository'}:
                warnings.append(f'{eid}: {status}')
            if status == 'empty-repository' and e.get('code_github', {}).get('size_kb') != 0:
                errors.append(f'{eid}: empty status does not match repository size')
        if e.get('kind') == 'blog':
            if not e.get('publisher'):
                errors.append(f'{eid}: missing publisher')
            if e.get('published') is None:
                warnings.append(f'{eid}: publication date unconfirmed')
        for field in ['github', 'code_github']:
            if field not in e:
                continue
            g = e[field]
            if g.get('private') is not False:
                errors.append(f'{eid}: repository not confirmed public')
            if not isinstance(g.get('stars'), int) or g['stars'] < 0:
                errors.append(f'{eid}: invalid star count')
            if not g.get('fetched_at') or not g.get('source'):
                errors.append(f'{eid}: missing metadata provenance')
            if not valid_date(str(g.get('pushed_at', ''))[:10]):
                errors.append(f'{eid}: invalid pushed_at')
            elif activity(g, as_of, meta.get('activity_days', 60)) == 'future':
                errors.append(f'{eid}: future push date')
            target = e['url'] if field == 'github' else e.get('code_url')
            if g.get('url') != target:
                errors.append(f'{eid}: canonical repository URL mismatch')
        if e.get('kind') == 'project':
            g = e.get('github')
            if not g:
                errors.append(f'{eid}: project missing GitHub metadata')
            elif g.get('size_kb', 0) <= 0:
                errors.append(f'{eid}: empty repository cannot be an implementation entry')
            elif activity(g, as_of, meta.get('activity_days', 60)) != 'active':
                warnings.append(f'{eid}: {activity(g, as_of, meta.get("activity_days", 60))}')
    return errors, warnings

def markdown_files():
    return sorted([*ROOT.glob('*.md'), *ROOT.glob('docs/*.md'), *ROOT.glob('reports/**/*.md')])

def local_links(files):
    errors = []
    for path in files:
        text = path.read_text()
        for target in LINK_RE.findall(text):
            if urlparse(target).scheme or target.startswith('//'):
                continue
            base, fragment = urldefrag(unquote(target))
            dest = (path.parent / base).resolve() if base else path
            if not dest.exists():
                errors.append(f'{path.relative_to(ROOT)}: missing local target {target}')
                continue
            if fragment and dest.suffix == '.md':
                body = dest.read_text()
                anchors = set(re.findall(r'<a\s+id="([^"]+)"', body))
                for heading in re.findall(r'^#+\s+(.+)$', body, re.M):
                    anchors.add(re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-'))
                if fragment not in anchors:
                    errors.append(f'{path.relative_to(ROOT)}: missing anchor {target}')
    return errors

def collect_urls(data, files):
    urls = set()
    def walk(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key in {'url', 'code_url', 'code_evidence_url', 'paper_url', 'code_path', 'homepage_url', 'pdf_url'} and valid_url(value):
                    urls.add(urldefrag(value)[0])
                elif isinstance(value, (dict, list)):
                    walk(value)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)
    walk(data)
    for p in files:
        for url in LINK_RE.findall(p.read_text()):
            if valid_url(url):
                urls.add(urldefrag(url)[0])
    return sorted(urls)

def check_url(url):
    """Bound each public request; retry HTTP failures, not a failed connection."""
    record = {'url': url, 'checked_at': dt.datetime.now(dt.timezone.utc).isoformat()}
    for method in ['HEAD', 'GET']:
        cmd = ['curl', '--location', '--silent', '--show-error', '--connect-timeout', '3',
               '--max-time', '8', '--output', '/dev/null', '--write-out',
               '%{http_code}\n%{url_effective}', '--user-agent',
               'Mozilla/5.0 (public research link check)']
        if method == 'HEAD':
            cmd.append('--head')
        cmd.append(url)
        try:
            response = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        except subprocess.TimeoutExpired:
            record.update(status=None, result='failed', method=method, error='Request exceeded total time limit; connectivity unconfirmed')
            return record
        parts = response.stdout.strip().split('\n', 1)
        status = int(parts[0]) if parts and parts[0].isdigit() else 0
        record.update(status=status or None, method=method, final_url=parts[1] if len(parts)>1 else url)
        if response.returncode:
            record.update(result='failed', error=response.stderr.strip() or f'curl exit {response.returncode}')
            return record
        if 200 <= status < 400:
            record.update(result='ok')
            return record
        record.update(result='blocked' if status in {401,403,429} else 'failed', error=f'HTTP {status}')
    return record

def write_report(data, errors, warnings, link_report):
    meta = data['catalog']; entries = [e for e in data['entries'] if e.get('catalog_scope')!='background']; count = Counter(e['kind'] for e in entries)
    status = Counter(activity(e.get('github'), meta['as_of'], meta['activity_days']) for e in entries if e['kind'] == 'project')
    lines = [f'# 核验报告：{meta["as_of"]}', '',
             f'- 资源：{len(entries)} 条；论文 {count["paper"]}、模型报告 {count["report"]}、博客 {count["blog"]}、项目 {count["project"]}。',
             f'- 另存背景资料：{len(data["entries"])-len(entries)} 条，不计入上述入选数量；完整证据库 {len(data["entries"])} 条。',
             f'- 工作组：{len(set(e["work_id"] for e in entries))}；论文与配套资源不按独立成果累计。',
             f'- 项目活跃度：{dict(status)}。',
             f'- 离线核验错误：{len(errors)}；需保留的状态提示：{len(warnings)}。',
             f'- GitHub 最近完整批次时间：{meta.get("metadata_refreshed_at", "unknown")}；增量批次时间：{meta.get("metadata_incremental_refreshed_at", "none")}；单仓库查询时间保存在数据源。', '',
             '## 核验内容', '',
             '字段与双语内容完整性、分类和日期、资源去重、代码状态和归属证据、GitHub 元数据、两份 README／JSON／BibTeX 的生成一致性、本地文件与锚点。论文内容由策展过程人工阅读；脚本不裁决研究结论。', '',
             '## 外链检查', '']
    if link_report:
        counts = Counter(r['result'] for r in link_report['links'])
        lines += [f'检查时间：{link_report["checked_at"]}。共 {len(link_report["links"])} 个唯一 URL：成功 {counts["ok"]}，受阻 {counts["blocked"]}，失败 {counts["failed"]}。', '',
                  '逐项 HTTP 状态、重定向目标与时间见 [link-checks.json](link-checks.json)。HEAD 收到 HTTP 错误时回退 GET；连接超时不重复请求。连接限时 3 秒、单次总限时 8 秒，失败不等于网站不存在。不验证外部网页锚点或网页内容含义。', '']
        connection_failures = [r for r in link_report['links'] if r['result'] != 'ok' and r.get('status') is None]
        if connection_failures:
            lines += [f'其中 {len(connection_failures)} 项没有取得 HTTP 状态，属于连接未确认，不能判定为死链。各项连接错误保存在 JSON 中。', '']
        baseline = ROOT / 'reports/verification/link-checks-before-expansion.json'
        if baseline.exists():
            lines += ['扩展前的成功检查单独保存在 [历史快照](link-checks-before-expansion.json)，仅供时间对照，不用于替代本次结果。', '']
        for r in link_report['links']:
            if r['result'] != 'ok' and r.get('status') is not None:
                lines.append(f'- `{r["result"]}` [{r["url"]}]({r["url"]}) — {r.get("status")} / {r.get("error")}')
    else:
        lines += ['本次没有外链报告；运行 `scripts/verify_catalog.py --links` 生成。', '']
    lines += ['## 错误', ''] + (['- '+e for e in errors] or ['无。'])
    lines += ['', '## 需要保留的边界', ''] + ['- '+w for w in warnings]
    lines += ['', '## 未验证事项', '', '未安装或运行第三方环境；未复现模型训练或性能；未审计数据与软件许可组合；未验证云服务账户、资源额度、外部 API 或私有数据。HTTP 成功与公开仓库元数据不能替代这些检查。', '']
    out = ROOT / 'reports/verification' / (meta['as_of']+'.md')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text('\n'.join(lines))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--links', action='store_true'); args = ap.parse_args()
    data = load(); errors, warnings = validate_data(data)
    for path, expected in outputs(data).items():
        file = ROOT / path
        if not file.exists() or file.read_text() != expected:
            errors.append(f'Generated artifact differs: {path}')
    link_path = ROOT / 'reports/verification/link-checks.json'
    previous = json.loads(link_path.read_text()) if link_path.exists() else None
    write_report(data, errors, warnings, previous)
    errors += local_links(markdown_files())
    if args.links:
        urls = collect_urls(data, markdown_files())
        links = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            jobs = {pool.submit(check_url, url): url for url in urls}
            for job in concurrent.futures.as_completed(jobs):
                links.append(job.result())
                if len(links) % 25 == 0:
                    print(f'Checked {len(links)}/{len(urls)} URLs', flush=True)
        links.sort(key=lambda row: row['url'])
        previous = {'checked_at': dt.datetime.now(dt.timezone.utc).isoformat(), 'links': links}
        link_path.write_text(json.dumps(previous, ensure_ascii=False, indent=2)+'\n')
    write_report(data, errors, warnings, previous)
    network_errors = [r for r in previous['links'] if r['result'] != 'ok'] if args.links and previous else []
    print(f'Offline errors: {len(errors)}; retained caveats: {len(warnings)}.')
    for error in errors:
        print('ERROR:', error)
    if args.links:
        print('Link results:', dict(Counter(r['result'] for r in previous['links'])))
    raise SystemExit(bool(errors or network_errors))

if __name__ == '__main__':
    main()
