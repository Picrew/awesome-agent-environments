#!/usr/bin/env python3
"""Generate both languages, bibliographic export and a flat machine-readable export."""
import argparse
from collections import Counter
import datetime as dt
import json
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/projects.yaml'
LEVELS = {
    'imitation': ('Imitation learning', '模仿学习'),
    'rl': ('RL experiments', 'RL 实验'), 'sft': ('SFT / trajectory training', 'SFT／轨迹训练'),
    'rl+sft': ('RL and SFT experiments', 'RL 与 SFT 实验'),
    'rl+harness': ('RL and harness learning', 'RL 与 harness 学习'),
    'rl-ready': ('Trainable interface', '可训练接口'),
    'generation': ('Environment / task generation', '环境／任务生成'),
    'evaluation': ('Evaluation substrate', '评测环境'),
    'methodology': ('Quality / failure study', '质量／失败研究'), 'survey': ('Survey', '综述'),
    'framework': ('Environment infrastructure', '环境基础设施'),
    'technical-account': ('Technical account', '技术报告'),
}
CODE = {'author-linked': ('Code', '代码'), 'partial-or-associated': ('Partial / associated code', '部分／关联代码'),
        'empty-repository': ('Empty repository', '空仓库'), 'not-confirmed': ('Not confirmed', '未确认'),
        'not-applicable': ('—', '—')}

def load():
    return yaml.safe_load(DATA.read_text())

def activity(github, as_of, days=60):
    if not github:
        return 'unknown'
    if github.get('archived'):
        return 'archived'
    if github.get('size_kb') == 0:
        return 'empty'
    pushed = github.get('pushed_at')
    if not pushed:
        return 'unknown'
    age = (dt.date.fromisoformat(as_of) - dt.date.fromisoformat(pushed[:10])).days
    if age < 0:
        return 'future'
    return 'active' if age <= days else 'reference'

def table_cell(s):
    return str(s).replace('|', '\\|').replace('\n', ' ')

def slug(text):
    return re.sub(r'[^\w\- ]', '', text.lower()).replace(' ', '-')

def detail_heading(e):
    return e['name']+' — '+e['id']

def detail_path(lang):
    return 'docs/catalog_details'+('_zh' if lang=='zh' else '')+'.md'

def report_path(lang):
    return 'docs/technical_report_sections'+('_zh' if lang=='zh' else '')+'.md'

def detail_link(e,lang):
    return '['+('详情' if lang=='zh' else 'Details')+']('+detail_path(lang)+'#'+slug(detail_heading(e))+')'

def table(headers, rows):
    return ['| '+' | '.join(headers)+' |','| '+' | '.join('---' for _ in headers)+' |']+[
        '| '+' | '.join(table_cell(cell) for cell in row)+' |' for row in rows]+['']

def resource_links(e,lang,details=True):
    zh=lang=='zh'; links=[]
    if e['kind']=='project':links.append(f"[GitHub]({e['url']})")
    if e.get('homepage_url'):links.append(f"[{'主页' if zh else 'Home'}]({e['homepage_url']})")
    if e.get('code_url'):links.append(f"[{CODE[e['code_status']][int(zh)]}]({e['code_url']})")
    for a in e.get('artifacts',[]):links.append(f"[{a['name_'+lang]}]({a['url']})")
    if details:links.append(detail_link(e,lang))
    return ' · '.join(links) or '—'

def render(catalog, lang):
    zh=lang=='zh';idx=int(zh);pick=lambda en,cn:cn if zh else en
    es=[e for e in catalog['entries'] if e.get('catalog_scope')!='background'];meta=catalog['catalog'];counts=Counter(e['kind'] for e in es)
    background=[e for e in catalog['entries'] if e.get('catalog_scope')=='background']
    lines=['# '+meta['title'],'',meta['description_'+lang],'','[English](README.md) | [中文](README_zh.md)','',
        pick(f"**{len(set(e['work_id'] for e in es))} work families · {counts['paper']} papers · {counts['report']} model reports · {counts['blog']} blogs · {counts['project']} GitHub projects**",f"**{len(set(e['work_id'] for e in es))} 组工作 · {counts['paper']} 篇论文 · {counts['report']} 篇模型报告 · {counts['blog']} 篇博客 · {counts['project']} 个 GitHub 项目**"),'',
        pick(f"Snapshot: **{meta['as_of']}**. Covers environment construction, task synthesis, interaction data, training and evaluation. Report sections and companion links are not counted as independent resources.",f"快照：**{meta['as_of']}**。覆盖环境构建、任务合成、交互数据、训练与评测。报告章节和配套链接不作为独立资源累计。"),'',
        pick(f'{len(background)} adjacent background articles are kept separately and excluded from these counts.',f'另有 {len(background)} 篇相邻背景文章单独保留，不计入上述入选数量。'),'',
        '## '+pick('Two Research Tracks','两条核心研究主线'),'']
    lines += table([pick('Theme','主题'),pick('Question to answer','必须回答的问题')],[[t['name_'+lang],t['question_'+lang]] for t in catalog['company_blog_themes']])
    lines += [catalog['research_focus']['scope_note_'+lang],'',
              pick('Working hypothesis: content / skills / repositories → environment and task generation → quality checks → interaction sampling and filtering → SFT or RL → independent evaluation → revise generation. The final feedback step is a research proposal, not a demonstrated result of this catalog.',
                   '拟研究的链路：内容／技能／仓库 → 环境与任务生成 → 质量验收 → 交互采样与筛选 → SFT 或 RL → 独立评测 → 反馈修正生成。最后的反馈机制属于待验证的研究设想。'),'',
              pick('SFT uses selected demonstrations; online RL additionally needs sampleable task distributions, executable environments and reliable rewards. More generated artifacts do not by themselves establish better learning.',
                   'SFT 主要使用筛选后的示范轨迹；在线 RL 还需要可采样任务分布、可执行环境和可靠奖励。生成得更多、验证通过更多，都不能直接等同训练得更好。'),'',
              '[研究主张、指标与实验设想 / Research focus](docs/research_focus_zh.md)','']
    lines += ['## '+pick('Model Company Articles — By Environment Contribution','模型公司文章：按环境贡献归类'),'',
        pick('Only articles directly addressing environment production at scale or training-data production are featured here. Interfaces, general evaluation and runtime facilities remain supporting references in the subject catalog.',
             '这里只前置直接讨论规模化环境生产或训练数据生产的文章。环境接口、一般评测和运行设施回到下方分类作支撑；每项列出具体机制与披露边界。'),'',
        pick('[Scope decisions and background articles](docs/north_american_company_blogs.md)','[逐篇相关性判断与背景资料](docs/north_american_company_blogs.md)'), '']
    for theme in catalog['company_blog_themes']:
        lines += ['### '+pick('Blog theme: ','博客主题：')+theme['name_'+lang],'',theme['question_'+lang],'']
        rows=[]
        for e in sorted(es,key=lambda e:e.get('published') or '',reverse=True):
            if e.get('featured_blog') and e.get('blog_theme')==theme['id']:
                contents='；'.join(e['core_contents_'+lang]) if zh else '; '.join(e['core_contents_'+lang])
                rows.append([f"[{e['title']}]({e['url']}) · {e['publisher']}",e['research_question_'+lang],contents,e.get('published') or e.get('published_label') or pick('Unconfirmed','未确认'),e['limitation_'+lang]+' '+detail_link(e,lang)])
        lines += table([pick('Article / publisher','文章／机构'),pick('Core question','核心问题'),pick('Concrete content / outputs','具体内容／产物'),pick('Date','日期'),pick('Boundary / source passages','边界／正文定位')],rows)
    lines += ['## '+pick('Selected Research for the Two Tracks','两条主线的重点研究'),'']
    by_id={e['id']:e for e in es}
    for track in catalog['research_focus']['tracks']:
        lines += ['### '+pick('Papers: ','论文重点：')+track['name_'+lang],'']
        rows=[]
        for selected in track['entries']:
            e=by_id[selected['id']]
            rows.append([f"[{e['name']}]({e['url']})",selected['angle_'+lang],e['summary_'+lang],LEVELS[e['evidence_type']][idx],e['limitation_'+lang]+' '+detail_link(e,lang)])
        lines += table([pick('Work','工作'),pick('Focus','重点切入点'),pick('Mechanism / output','机制／产物'),pick('Reported evidence','作者报告的证据'),pick('Limits / details','限制／详情')],rows)
    lines += [pick('These are editorial selections from the existing catalog, not a performance ranking. SFT, RL and construction-only evidence are kept distinct; no experiments were reproduced here.',
                   '以上是从既有目录筛出的研究重点，不是性能排名。SFT、RL 与仅构造证据分开记录；本调研没有复现训练结果。'),'']
    lines+=['## '+pick('Environment Sections in Technical Reports','技术报告中的环境章节'),'',
        pick('Section locations are pinned to the versions below. PDF links open at the first relevant page; the section index explains each passage separately. Model weights or an agent client do not establish release of the training environments.',
             '以下位置对应指定报告版本。PDF 链接定位到首个相关页；章节索引逐节说明内容。模型权重或 Agent 客户端开放，不代表训练环境开放。'),'']
    rows=[]
    for e in es:
        if not e.get('report_sections'):continue
        secs=e['report_sections'];pp=sorted({p for s in secs for p in s['pdf_pages']})
        rows.append([f"[{e['name']}]({e['url']})",e['report_version'],', '.join('§'+s['section'] for s in secs),
            f"[PDF pp. {', '.join(map(str,pp))}]({e['pdf_url']}#page={pp[0]}) · ["+pick('Section index','逐节内容')+']('+report_path(lang)+'#'+slug(e['name'])+')',e['summary_'+lang]])
    lines+=table([pick('Report / paper','报告／论文'),pick('Version','版本'),pick('Relevant sections','相关章节'),pick('Location','定位'),pick('Content','内容')],rows)
    lines+=['## '+pick('Catalog','分类目录'),'',
        pick('Major groups organize contributions; subcategories identify construction methods or infrastructure roles. Papers and repositories use separate tables. Stars are recorded snapshots, not a quality ranking. Full titles, feedback, release boundaries and evidence are in the linked details.',
             '保留原有 6 个大类、20 个小类以及论文／仓库分表结构，便于查资料。上方两条主线决定本次研究重点；下方接口、运行时、领域基准与审计材料提供支撑，不再全部作为并列研究方向。Stars 为快照，不代表质量排名。'),'',
        '[覆盖审计 / Coverage](docs/coverage_audit.md) · [技能与需求合成](docs/skills_to_environments.md) · [中文综述](docs/research_landscape_zh.md) · [收录标准 / Policy](docs/curation_policy.md)','']
    for group in catalog['groups']:
        lines.append(f"- [{group['name_'+lang]}](#{slug(group['name_'+lang])})")
        for c in catalog['categories']:
            if c['parent']==group['id']:lines.append(f"  - [{c['name_'+lang]}](#{slug(c['name_'+lang])})")
    lines+=['']
    for group in catalog['groups']:
        lines+=['## '+group['name_'+lang],'']
        for c in catalog['categories']:
            if c['parent']!=group['id']:continue
            subset=[e for e in es if e['category']==c['id'] and e['kind']!='report' and not e.get('featured_blog')]
            subset.sort(key=lambda e:e.get('published') or '',reverse=True)
            lines+=['### '+c['name_'+lang],'']
            papers=[e for e in subset if e['kind']=='paper']
            if papers:
                lines+=['**'+pick('Papers','论文')+'**','']
                rows=[]
                for e in papers:
                    rows.append([f"[{e['name']}]({e['url']})",e['published'],resource_links(e,lang),e['summary_'+lang],LEVELS[e['evidence_type']][idx]+': '+e.get('feedback_'+lang,pick('See source and details.','见原文与详情。')),e['limitation_'+lang]])
                lines+=table([pick('Paper','论文'),pick('Date','日期'),pick('Resources','资源'),pick('Environment / task contribution','环境／任务贡献'),pick('Feedback / evidence','反馈／证据'),pick('Release boundary','开放边界')],rows)
            projects=[e for e in subset if e['kind']=='project']
            if projects:
                lines+=['**'+pick('Repositories','仓库')+'**','']
                projects.sort(key=lambda e:e['github']['stars'],reverse=True)
                rows=[[e['name'],resource_links(e,lang),f"★ {e['github']['stars']:,}",', '.join(e['tags']),e['summary_'+lang]] for e in projects]
                lines+=table([pick('Project','项目'),pick('Links','链接'),'Stars',pick('Tags','标签'),pick('Summary','摘要')],rows)
            blogs=[e for e in subset if e['kind']=='blog']
            if blogs:
                lines+=['**'+pick('Blogs','博客')+'**','']
                rows=[[f"[{e['name']}]({e['url']})",e['publisher'],e.get('published') or pick('Unconfirmed','未确认'),e['summary_'+lang],detail_link(e,lang)] for e in blogs]
                lines+=table([pick('Article','文章'),pick('Publisher','发布方'),pick('Date','日期'),pick('Summary','摘要'),pick('Evidence','证据')],rows)
    lines+=['## '+pick('Maintenance','维护方式'),'',
        pick('Edit `data/projects.yaml`, then regenerate and validate. Automated metadata refreshes never renew human review dates. Tests and link checks do not reproduce research results.',
             '编辑 `data/projects.yaml` 后重新生成与核验。自动元数据更新不会刷新人工复核日期；测试和链接检查不代表复现研究结果。'),'',
        '```bash','.venv/bin/python scripts/render_readme.py','.venv/bin/python scripts/verify_catalog.py','.venv/bin/python -m unittest discover -s tests','.venv/bin/python scripts/verify_catalog.py --links','```','',
        '- [YAML](data/projects.yaml) · [JSON](data/catalog.json) · [BibTeX](references.bib)',
        '- [Verification / 核验报告](reports/verification/2026-10-08.md)',
        '- [Sources / 来源核验](docs/sources_and_verification.md) · [Contributing](CONTRIBUTING.md)','']
    return '\n'.join(lines)

def render_details(catalog,lang):
    zh=lang=='zh';idx=int(zh);pick=lambda en,cn:cn if zh else en
    main='../README_zh.md' if zh else '../README.md'
    lines=['# '+pick('Catalog Details & Evidence','目录详情与证据'),'',f"[← {pick('Catalog','主目录')}]({main})",'',pick('Each resource retains its own release boundary. Companion links are not counted as separate projects.','每项资源保留独立开放边界，配套链接不额外算作项目。'),'']
    for e in catalog['entries']:
        lines+=['## '+detail_heading(e),'',f"**[{e['title']}]({e['url']})**",'',
            f"`{e['kind']}` · `{e['work_id']}` · {e.get('published') or e.get('published_label') or pick('Date unconfirmed','日期未确认')} · {LEVELS[e['evidence_type']][idx]}",'',e['summary_'+lang],'']
        if e.get('feedback_'+lang):lines += ['**'+pick('Feedback / validation','反馈／验收')+'：** '+e['feedback_'+lang],'']
        if e.get('catalog_scope')=='background':lines += ['**'+pick('Background only — excluded from the selected catalog','仅作背景，不计入入选目录')+'：** '+e['scope_reason_'+lang],'']
        if e.get('catalog_scope')=='supporting':lines += ['**'+pick('Supporting reference','支撑资料')+'：** '+e['scope_reason_'+lang],'']
        if e.get('research_question_'+lang):
            lines += ['**'+pick('Article research question','文章研究问题')+'：** '+e['research_question_'+lang],'','**'+pick('Concrete content','具体内容')+'**','']
            lines += ['- '+item for item in e['core_contents_'+lang]]+['']
        if e.get('source_section'):lines += ['**'+pick('Relevant passages (original headings / locator notes)','相关段落（原文标题／定位说明）')+'：** '+(e['source_section'] if zh else e.get('source_section_en',e['source_section'])),'']
        lines+=['**'+pick('Release boundary','开放边界')+'：** '+e['limitation_'+lang],'']
        if e.get('code_status'):lines+=['**'+pick('Implementation status','实现状态')+'：** '+CODE[e['code_status']][idx],'']
        if e.get('github'):
            g=e['github'];lines+=[f"GitHub: ★ {g['stars']:,} · push {g['pushed_at'][:10]} · `{g['license']}` · {activity(g,catalog['catalog']['as_of'])}",'']
        links=resource_links(e,lang,False)
        if links!='—':lines += [links,'']
        others=[o for o in catalog['entries'] if o['work_id']==e['work_id'] and o['id']!=e['id']]
        if others:lines += [pick('Same work: ','同组资源：')+' · '.join(f"[{o['name']} ({o['kind']})](#{slug(detail_heading(o))})" for o in others),'']
        if e.get('report_sections'):lines += ['['+pick('Report section index','报告章节索引')+']('+Path(report_path(lang)).name+'#'+slug(e['name'])+')','']
        lines += ['**'+pick('Evidence','来源证据')+'**','']
        for ev in e['evidence']:lines.append(f"- [{ev['method']}]({ev['url']}) · {ev['reviewed_at']} · “{ev['excerpt']}”")
        lines+=['']
    return '\n'.join(lines)

def render_reports(catalog,lang):
    zh=lang=='zh';pick=lambda en,cn:cn if zh else en
    lines=['# '+pick('Environment Sections in Technical Reports','技术报告中的环境章节'),'',
        '[← '+pick('Catalog','主目录')+'](../README'+('_zh' if zh else '')+'.md)','',
        pick('Locations refer to the explicitly named versions. PDF page numbers are one-based viewer pages, checked against PDF text; Kimi K3, DSec and MiMo page layouts were also inspected. These are curated passages, not a claim that every relevant report is covered.',
             '位置对应下列固定版本。页码为 PDF 阅读器从 1 开始的页序，已对照 PDF 文本；另检查了 Kimi K3、DSec 与 MiMo 的页面版式。本页是已核验的章节索引，不声称穷尽所有报告。'),'']
    for e in catalog['entries']:
        if not e.get('report_sections'):continue
        lines+=['## '+e['name'],'',f"[{e['title']}]({e['url']}) · **{e['report_version']}**",'',e['limitation_'+lang],'']
        rows=[]
        for s in e['report_sections']:
            pages=s['pdf_pages'];label=str(pages[0]) if len(pages)==1 else str(pages[0])+'–'+str(pages[-1])
            rows.append([f"[§{s['section']}]({s['url']})",s['title'],f"[pp. {label}]({e['pdf_url']}#page={pages[0]})",s['summary_'+lang]])
        lines+=table([pick('Section','章节'),pick('Original heading','原文章节标题'),'PDF',pick('Environment content','环境相关内容')],rows)
        if e.get('artifacts'):lines += [' · '.join(f"[{a['name_'+lang]}]({a['url']})" for a in e['artifacts']),'']
    return '\n'.join(lines)

def render_company_scope(catalog):
    es=catalog['entries'];core=[e for e in es if e.get('featured_blog')];background=[e for e in es if e.get('catalog_scope')=='background']
    supporting=[e for e in es if e.get('catalog_scope')=='supporting']
    selected=[e for e in es if e.get('catalog_scope')!='background']
    lines=['# 公司文章：主题相关性与取舍','', '[返回目录](../README_zh.md) · [完整来源证据](catalog_details_zh.md)','',
           '公司是检索线索。当前前置主线收敛为大规模构建高质量环境，以及从环境和内容生产有效训练数据；执行、一般评测、泛模拟等作为支撑。以下分层是本目录的编辑判断，不是对文章本身质量的评价。','',
           f'此前 38 篇公司文章分为：{len(core)} 篇主线文章、{len(supporting)} 篇分类支撑、{len(background)} 篇背景资料。当前主目录 {len(selected)} 条入选资源；完整证据库保留 {len(es)} 条记录，背景资料不计入主目录。','',
           '[研究主张与实验设想](research_focus_zh.md)','',
           '## 核心主题与具体内容','']
    for theme in catalog['company_blog_themes']:
        lines += ['### '+theme['name_zh'],'',theme['question_zh'],'']
        rows=[]
        for e in core:
            if e['blog_theme']!=theme['id']:continue
            rows.append([f"[{e['title']}]({e['url']}) · {e['publisher']}",e['research_question_zh'],'；'.join(e['core_contents_zh']),e.get('source_section') or '按正文中的上述机制段落定位；详见来源证据'])
        lines += table(['文章／机构','核心问题','具体内容','原文位置'],rows)
    lines += ['## 分类支撑材料','',
              '保留在原有分类表中，可按实现或评测需要查阅；不再与两条生产主线并列。','']
    lines += table(['文章','机构','定位'],[[f"[{e['title']}]({e['url']})",e['publisher'],e['scope_reason_zh']] for e in supporting])
    lines += ['## 相邻背景资料','',
              '这些页面保留来源、摘要与核验记录，但从主目录及公司核心表移出。模型报告中有独立环境机制的章节仍按原位置保留，例如 Kimi K3。','']
    rows=[[f"[{e['title']}]({e['url']})",e['publisher'],e['scope_reason_zh']] for e in background]
    lines += table(['文章','机构','未进入核心表的原因'],rows)
    lines += ['## 判定规则','',
              '主线文章需要直接回答规模化环境生产或训练数据生产中的具体问题。环境质量研究若与生产、筛选、修复和迭代直接相连，可以进入主线；仅解释通用评测、接口或隔离机制的文章保留为支撑。只列使用领域、模型能力、环境数量或通用服务架构，不足以进入主线。','',
              '只使用现成环境训练也可以相关，但必须讲清环境中的执行、反馈或数据生产过程，并明确“使用环境”与“构造环境”的区别。运行基础设施可以入选，但需要直接解释任务／rollout 的状态、隔离、反馈或批量执行，而非泛泛讨论 agent 服务。','',
              '文章是否开源与主题相关性是两条独立判断：私有环境的具体构造机制可以研究；开放模型或运行客户端也不能自动算作开放环境。日期、版本、章节和发布边界保留在各条详情。','']
    return '\n'.join(lines)

def bibtex(catalog):
    blocks=[]
    escape=lambda s:s.replace('&','\\&').replace('%','\\%').replace('_','\\_')
    for e in catalog['entries']:
        if e['kind'] not in {'paper','report'}:continue
        year=e['published'][:4] if e.get('published') else None
        fields=[('title',escape(e['title'].replace('$',''))),('author',' and '.join(escape(a) for a in e['authors']))]
        if year:fields.append(('year',year))
        if e['url'].startswith('https://arxiv.org/abs/'):
            fields += [('eprint',e['url'].rsplit('/',1)[-1]),('archivePrefix','arXiv')]
        if e.get('report_version'):fields.append(('note',escape(e['report_version']+(' ; first publication date unconfirmed' if not year else ''))))
        fields.append(('url',e['url']))
        key=e['work_id'].replace('-','_')+'_'+(year or 'undated')
        blocks.append('@misc{'+key+',\n'+',\n'.join('  '+k+' = {'+v+'}' for k,v in fields)+'\n}')
    return '\n\n'.join(blocks)+'\n'

def outputs(catalog):
    return {'README.md':render(catalog,'en'), 'README_zh.md':render(catalog,'zh'),
            'docs/north_american_company_blogs.md':render_company_scope(catalog),
            'references.bib':bibtex(catalog),
            detail_path('en'):render_details(catalog,'en'), detail_path('zh'):render_details(catalog,'zh'),
            report_path('en'):render_reports(catalog,'en'), report_path('zh'):render_reports(catalog,'zh'),
            'data/catalog.json':json.dumps(catalog,ensure_ascii=False,indent=2)+'\n'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args()
    mismatches=[]
    for path,content in outputs(load()).items():
        p=ROOT/path
        if args.check:
            if not p.exists() or p.read_text()!=content:
                mismatches.append(path)
        else:
            p.write_text(content)
    if mismatches:
        raise SystemExit('Generated files differ: '+', '.join(mismatches))
    print('Generated outputs match.' if args.check else 'Rendered bilingual catalog, BibTeX and JSON.')

if __name__=='__main__':
    main()
