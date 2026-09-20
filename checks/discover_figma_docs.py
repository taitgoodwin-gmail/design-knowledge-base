#!/usr/bin/env python3
"""Inventory public Figma Design articles; retrieval is not substantive review."""
import datetime
import hashlib
import json
import pathlib
import urllib.parse
import urllib.request
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parents[1]
CACHE = ROOT / '.research-cache' / 'figma-design'
OUT = ROOT / 'sources' / 'figma-design-article-inventory.json'
START = 'https://help.figma.com/api/v2/help_center/en-us/categories/360002042553/articles.json?per_page=100'

class Headings(HTMLParser):
    def __init__(self):
        super().__init__()
        self.level = None
        self.buffer = []
        self.items = []
    def handle_starttag(self, tag, attrs):
        if tag in ('h1', 'h2', 'h3', 'h4'):
            self.level = tag
            self.buffer = []
    def handle_data(self, data):
        if self.level:
            self.buffer.append(data)
    def handle_endtag(self, tag):
        if tag == self.level:
            self.items.append({'level': tag, 'text': ' '.join(''.join(self.buffer).split())})
            self.level = None

def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    url, seen, articles, pages = START, set(), {}, []
    while url:
        parsed = urllib.parse.urlsplit(url)
        if parsed.scheme != 'https' or parsed.netloc != 'help.figma.com' or url in seen:
            raise RuntimeError('Unexpected or repeated pagination URL')
        seen.add(url)
        with urllib.request.urlopen(url, timeout=40) as response:
            raw = response.read()
            status = response.status
        data = json.loads(raw)
        number = len(pages) + 1
        (CACHE / f'page-{number:03}.json').write_bytes(raw)
        pages.append({'url': url, 'http_status': status, 'sha256': hashlib.sha256(raw).hexdigest(), 'article_count': len(data['articles']), 'reported_count': data.get('count')})
        for article in data['articles']:
            parser = Headings()
            body = article.get('body') or ''
            parser.feed(body)
            articles[article['id']] = {'id': article['id'], 'title': article['title'], 'url': article['html_url'], 'section_id': article['section_id'], 'updated_at': article['updated_at'], 'locale': article['locale'], 'draft': article['draft'], 'body_sha256': hashlib.sha256(body.encode()).hexdigest(), 'body_characters': len(body), 'headings': parser.items, 'status': 'body-retrieved-not-reviewed'}
        url = data.get('next_page')
        print(json.dumps({'page': number, 'unique_articles': len(articles), 'has_next': bool(url)}), flush=True)
    result = {'schema_version': 1, 'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'scope': 'Public en-us articles returned by the Figma Design category API; excludes other categories, videos, plan-restricted UI and unpublished changes.', 'start_url': START, 'pagination_exhausted': url is None, 'pages': pages, 'article_count': len(articles), 'articles': list(articles.values()), 'limitation': 'Body retrieval and heading extraction are discovery evidence, not expert review, feature testing, or completeness of all Figma capabilities. Full response cache is local and ignored by Git.'}
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')

if __name__ == '__main__':
    main()
