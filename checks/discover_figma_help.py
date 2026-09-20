#!/usr/bin/env python3
"""Inventory public English Figma Help categories; retrieval is not review."""
import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import urllib.parse
import urllib.request
from discover_figma_docs import Headings

ROOT = pathlib.Path(__file__).resolve().parents[1]
CACHE = ROOT / '.research-cache' / 'figma-help'
START = 'https://help.figma.com/api/v2/help_center/en-us/categories.json?per_page=100'

def pages(start, cache_dir, key):
    url, seen = start, set()
    while url:
        p = urllib.parse.urlsplit(url)
        if p.scheme != 'https' or p.netloc != 'help.figma.com' or url in seen:
            raise RuntimeError('Unexpected or repeated pagination URL')
        seen.add(url)
        with urllib.request.urlopen(url, timeout=45) as response:
            raw, status = response.read(), response.status
        data = json.loads(raw)
        cache_dir.mkdir(parents=True, exist_ok=True)
        (cache_dir / f'page-{len(seen):03}.json').write_bytes(raw)
        yield data[key], {'url': url, 'status': status, 'sha256': hashlib.sha256(raw).hexdigest(), 'count': len(data[key]), 'reported_count': data.get('count')}
        url = data.get('next_page')

def inventory(category):
    cid = category['id']
    start = f'https://help.figma.com/api/v2/help_center/en-us/categories/{cid}/articles.json?per_page=100'
    articles, receipts = {}, []
    try:
        for rows, receipt in pages(start, CACHE / str(cid), 'articles'):
            receipts.append(receipt)
            for article in rows:
                body = article.get('body') or ''
                headings = Headings()
                headings.feed(body)
                articles[article['id']] = {
                    'id': article['id'], 'title': article['title'], 'url': article['html_url'],
                    'section_id': article['section_id'], 'updated_at': article['updated_at'],
                    'locale': article['locale'], 'draft': article['draft'],
                    'body_sha256': hashlib.sha256(body.encode()).hexdigest(),
                    'body_characters': len(body), 'headings': headings.items,
                    'retrieval_status': 'body-retrieved',
                    'review_status': 'not-established-by-retrieval'
                }
        result = {'id': cid, 'name': category['name'], 'url': category['html_url'],
                  'pagination_exhausted': True, 'pages': receipts,
                  'article_count': len(articles), 'articles': list(articles.values())}
    except Exception as exc:
        result = {'id': cid, 'name': category['name'], 'url': category['html_url'],
                  'pagination_exhausted': False, 'error': str(exc), 'pages': receipts,
                  'article_count': len(articles), 'articles': list(articles.values())}
    print(json.dumps({'category': category['name'], 'articles': len(articles), 'pagination_exhausted': result['pagination_exhausted']}), flush=True)
    return result

def main():
    categories, receipts = [], []
    for rows, receipt in pages(START, CACHE / 'categories', 'categories'):
        categories.extend(rows)
        receipts.append(receipt)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(inventory, categories))
    ids = {a['id'] for c in records for a in c['articles']}
    result = {
        'schema_version': 1, 'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope': 'Public en-us categories and their returned articles on help.figma.com. Not Weave external docs, videos, Figma marketing/developer sites, private articles or every UI context.',
        'category_discovery': {'start_url': START, 'pagination_exhausted': True, 'pages': receipts},
        'category_count': len(records), 'unique_article_count': len(ids), 'categories': records,
        'all_category_pagination_exhausted': all(c['pagination_exhausted'] for c in records),
        'review_register': 'tools/figma/records/sources.json',
        'limitations': ['Retrieved bodies are not all substantively reviewed.', 'Local full-response cache is ignored by Git; metadata, headings and hashes are committed.', 'No claim of every capability or every site scraped.']
    }
    (ROOT / 'sources/figma-help-article-inventory.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'categories': len(records), 'unique_articles': len(ids), 'complete_pagination': result['all_category_pagination_exhausted']}))

if __name__ == '__main__':
    main()
