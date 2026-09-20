#!/usr/bin/env python3
"""Validate preserved imports, maintained links, and source records; no network calls."""
from pathlib import Path
import hashlib, json, re, sys
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[1]
errors=[]
def require(condition,message):
 if not condition:errors.append(message)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
local=json.loads((ROOT/'archive/imports/local-manifest.json').read_text())
for r in local['files']:
 p=ROOT/r['stored_path']
 require(p.is_file(),f"Missing archived file: {r['stored_path']}")
 if p.is_file():require(digest(p)==r['sha256'],f"Changed archive: {r['stored_path']}")
notion=json.loads((ROOT/'sources/notion-import-manifest.json').read_text())
require(len({r['markdown_path'] for r in notion})==len(notion),'Notion readable path collision')
for r in notion:
 p=ROOT/r['snapshot_path']
 require(p.is_file(),f"Missing Notion response: {r['id']}")
 if p.is_file():require(digest(p)==r['snapshot_sha256'],f"Changed Notion response: {r['id']}")
 require((ROOT/r['markdown_path']).is_file(),f"Missing readable Notion page: {r['id']}")
json_count=0
for p in ROOT.rglob('*.json'):
 if '.git' in p.parts:continue
 try:json.loads(p.read_text());json_count+=1
 except Exception as e:errors.append(f'Invalid JSON: {p.relative_to(ROOT)}: {e}')
sources=json.loads((ROOT/'sources/catalog.json').read_text())['sources']
require(len({r['id'] for r in sources})==len(sources),'Duplicate source IDs')
require(len({r['url'] for r in sources})==len(sources),'Duplicate exact source URLs')
for r in sources:
 require(bool(r['records']),f"No provenance: {r['id']}")
 for obs in r['records']:
  require((ROOT/obs['evidence']).is_file(),f"Missing source evidence: {obs['evidence']}")
figma_sources=json.loads((ROOT/'tools/figma/records/sources.json').read_text())
figma_ids={r['id'] for r in figma_sources}
for r in json.loads((ROOT/'tools/figma/records/controls.json').read_text()):
 require(set(r['source_ids'])<=figma_ids,f"Unknown Figma source: {r['id']}")
 require((ROOT/'tools/figma'/r['evidence']).is_file(),f"Missing control evidence: {r['id']}")
for r in json.loads((ROOT/'tools/figma/records/exercises.json').read_text()):
 if r.get('evidence'):require((ROOT/'tools/figma'/r['evidence']).is_file(),f"Missing exercise evidence: {r['id']}")
links=0
for p in ROOT.rglob('*.md'):
 if '.git' in p.parts or 'archive' in p.relative_to(ROOT).parts:continue
 text=re.sub(r'```.*?```','',p.read_text(),flags=re.S)
 for target in re.findall(r'\]\(([^)]+)\)',text):
  target=target.strip().split(' "')[0].strip('<>')
  if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target) or target.startswith('#'):continue
  target=unquote(target.split('#')[0])
  if not target:continue
  links+=1
  require((p.parent/target).exists(),f'Broken maintained link: {p.relative_to(ROOT)} -> {target}')
sizes=[(p.stat().st_size,str(p.relative_to(ROOT))) for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts]
require(all(n<100*1024*1024 for n,_ in sizes),'File exceeds GitHub ordinary Git limit')
summary={'local_archives':len(local['files']),'notion_snapshots':len(notion),'source_urls':len(sources),'valid_json_files':json_count,'maintained_links_checked':links,'largest_file_bytes':max(sizes)[0],'errors':errors}
print(json.dumps(summary,indent=2))
sys.exit(bool(errors))
