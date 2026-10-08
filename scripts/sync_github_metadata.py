#!/usr/bin/env python3
"""Refresh public GitHub metadata without credentials or running third-party code.

All requests must succeed before the catalog is replaced. Human evidence dates
are never advanced by metadata refreshes. Public GitHub rate limits apply.
"""
import concurrent.futures
import datetime as dt
import json
from pathlib import Path
import urllib.request
from urllib.parse import urlparse
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/projects.yaml'

def slug(url):
    p = urlparse(url)
    parts = p.path.strip('/').split('/')
    if p.scheme != 'https' or p.hostname != 'github.com' or len(parts) != 2:
        raise ValueError(f'Expected repository root: {url}')
    return '/'.join(parts)

def fetch_repo(name):
    url = 'https://api.github.com/repos/' + name
    req = urllib.request.Request(url, headers={'User-Agent': 'awesome-agent-environments',
                                               'Accept': 'application/vnd.github+json'})
    with urllib.request.urlopen(req, timeout=30) as response:
        data = json.load(response)
    for key in ['html_url', 'full_name', 'pushed_at', 'archived', 'private', 'stargazers_count', 'size']:
        if key not in data:
            raise ValueError(f'{name}: missing {key}')
    if data['private']:
        raise ValueError(f'{name}: expected a public repository')
    return dict(url=data['html_url'], full_name=data['full_name'],
                stars=data['stargazers_count'], pushed_at=data['pushed_at'],
                updated_at=data.get('updated_at'), archived=data['archived'],
                private=data['private'], size_kb=data['size'],
                license=(data.get('license') or {}).get('spdx_id') or 'none',
                default_branch=data.get('default_branch'), source=url,
                fetched_at=dt.datetime.now(dt.timezone.utc).isoformat())

def main():
    catalog = yaml.safe_load(DATA.read_text())
    refs = {}
    for e in catalog['entries']:
        url = e['url'] if e['kind'] == 'project' else e.get('code_url')
        if url:
            refs.setdefault(slug(url).lower(), []).append(e)
    results, errors = {}, []
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        jobs = {pool.submit(fetch_repo, name): name for name in refs}
        for job in concurrent.futures.as_completed(jobs):
            name = jobs[job]
            try:
                results[name] = job.result()
            except Exception as exc:
                errors.append(f'{name}: {exc}')
    report = ROOT / 'reports/verification/github-metadata.json'
    report.write_text(json.dumps({'repositories': results, 'errors': errors}, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit('Catalog unchanged. Metadata errors:\n' + '\n'.join(errors))
    for name, linked in refs.items():
        for e in linked:
            e['github' if e['kind'] == 'project' else 'code_github'] = results[name]
            e['url' if e['kind'] == 'project' else 'code_url'] = results[name]['url']
    catalog['catalog']['metadata_refreshed_at'] = dt.datetime.now(dt.timezone.utc).isoformat()
    temporary = DATA.with_suffix('.yaml.tmp')
    temporary.write_text(yaml.safe_dump(catalog, allow_unicode=True, sort_keys=False, width=110))
    temporary.replace(DATA)
    canonical_count = len({r['url'].lower() for r in results.values()})
    print(f'Refreshed {canonical_count} canonical public repositories through {len(results)} lookup URLs; human review dates unchanged.')

if __name__ == '__main__':
    main()
