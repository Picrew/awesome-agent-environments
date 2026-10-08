#!/usr/bin/env python3
"""Read public primary sources into an ignored local cache; never executes source code."""
import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
from pathlib import Path
import urllib.request
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.cache' / 'sources'

def fetch(url):
    CACHE.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha256(url.encode()).hexdigest()[:20]
    meta_path = CACHE / (key + '.json')
    if meta_path.exists():
        return json.loads(meta_path.read_text())
    record = {'url': url, 'checked_at': dt.datetime.now(dt.timezone.utc).isoformat()}
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (research catalog; public read-only)'})
        with urllib.request.urlopen(req, timeout=30) as response:
            raw = response.read().decode('utf-8', errors='replace')
            record.update(status=response.status, final_url=response.url)
        soup = BeautifulSoup(raw, 'html.parser')
        record['title'] = soup.title.get_text(' ', strip=True) if soup.title else ''
        record['links'] = sorted(set(a['href'] for a in soup.find_all('a', href=True)))
        record['meta'] = {m.get('name', m.get('property', '')): m.get('content') for m in soup.find_all('meta') if m.get('content')}
        for el in soup(['script', 'style', 'nav', 'footer', 'header']):
            el.decompose()
        body = soup.select_one('article') or soup.select_one('main') or soup
        record['text'] = body.get_text('\n', strip=True)
        (CACHE / (key + '.html')).write_text(raw)
        (CACHE / (key + '.txt')).write_text(record['text'])
    except Exception as exc:
        record.update(status='error', error=str(exc))
    meta_path.write_text(json.dumps(record, ensure_ascii=False, indent=2))
    return record

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('urls', nargs='+')
    ap.add_argument('--abstract', action='store_true')
    ap.add_argument('--limit', type=int, default=1600)
    args = ap.parse_args()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for r in pool.map(fetch, args.urls):
            text = r.get('text', '')
            if args.abstract and 'Abstract:' in text:
                text = text.split('Abstract:', 1)[1].split('Comments:', 1)[0].split('Subjects:', 1)[0]
            print(json.dumps({'url':r['url'],'status':r['status'],'title':r.get('title'),'date':r.get('meta',{}).get('citation_date'), 'text':text[:args.limit], 'links':[x for x in r.get('links',[]) if any(k in x for k in ('github.com','huggingface.co','github.io'))]},ensure_ascii=False))

if __name__ == '__main__':
    main()
