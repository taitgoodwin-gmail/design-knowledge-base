#!/usr/bin/env python3
"""Small local topic search. Results are leads; read evidence status before reuse."""
from pathlib import Path
import re,json,sys

ROOT=Path(__file__).resolve().parents[1]
def search(query,limit=8):
 terms=re.findall(r'[a-z0-9]+',query.lower());out=[]
 for p in ROOT.rglob('*.md'):
  rel=str(p.relative_to(ROOT))
  if rel.startswith(('archive/','evidence/')) or '.git' in p.parts:continue
  text=p.read_text();low=text.lower();title=text.splitlines()[0].lstrip('# ')
  found=[t for t in terms if t in low]
  if len(found)!=len(terms):continue
  score=sum(3+min(low.count(t),10)+8*(t in title.lower())+10*(t in rel.lower()) for t in found)
  score+=15*(query.lower() in title.lower())
  score-=40*rel.startswith('tools/figma/reference-index/')
  matching=[l.strip() for l in text.splitlines() if any(t in l.lower() for t in terms) and l.strip()]
  out.append({'path':rel,'title':title,'score':score,'excerpt':' '.join(matching[:3])[:500]})
 return sorted(out,key=lambda r:(-r['score'],r['path']))[:limit]
if __name__=='__main__':
 query=' '.join(sys.argv[1:]).strip()
 if not query:raise SystemExit('Usage: python3 checks/query.py "topic"')
 print(json.dumps({'query':query,'results':search(query)},indent=2))
