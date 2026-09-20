from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re,hashlib
root=Path(__file__).resolve().parents[1] / 'reference-build/site-v3.1/dist'
class P(HTMLParser):
 def __init__(self): super().__init__(); self.tags=[];self.text=[];self.skip=0
 def handle_starttag(self,t,a):
  self.tags.append((t,dict(a),self.getpos()[0]))
  if t in ('script','style'):self.skip+=1
 def handle_endtag(self,t):
  if t in ('script','style'):self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if not self.skip and d.strip():self.text.append(d.strip())
pages={}
for f in sorted(root.glob('*.html')):
 p=P();s=f.read_text();p.feed(s);pages[f.name]=(p,s)
report={}
for name,(p,s) in pages.items():
 broken=[];external=[]
 for t,a,line in p.tags:
  for att in ('href','src'):
   u=a.get(att)
   if not u:continue
   part=urlsplit(u)
   if part.scheme or part.netloc: external.append(u);continue
   target=unquote(part.path).lstrip('/') or name
   if not (root/target).exists():broken.append([line,u,'file missing'])
   elif part.fragment and target in pages and part.fragment not in {a.get('id') for _,a,_ in pages[target][0].tags}:broken.append([line,u,'anchor missing'])
 schemas=[]
 for m in re.finditer(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):
  try:schemas.append(json.loads(m.group(1)))
  except Exception as e:schemas.append({'parse_error':str(e)})
 report[name]={'sha256':hashlib.sha256(s.encode()).hexdigest(),'lines':len(s.splitlines()),'h1':sum(t=='h1' for t,_,_ in p.tags),'forms':[(a,line) for t,a,line in p.tags if t=='form'],'canonical':[(a.get('href'),line) for t,a,line in p.tags if t=='link' and a.get('rel')=='canonical'],'broken_local_links':broken,'external_assets_links':sorted(set(external)),'schemas':schemas,'internal_sentinel_count':s.count('INTERNAL:'),'placeholder_href_count':s.count('href="#"'),'sample_label_count':s.count('SAMPLE'),'fields':[(a,line) for t,a,line in p.tags if t=='input'],'title':re.findall(r'<title>(.*?)</title>',s,re.S),'meta':[(a,line) for t,a,line in p.tags if t=='meta']}
 # Visible text is inspected in memory; no extra files are emitted.
(Path(__file__).resolve().parents[1] / 'docs/static-audit.json').write_text(json.dumps(report,indent=2))
for n,r in report.items():print(n, 'h1',r['h1'],'forms',len(r['forms']),'canonical',len(r['canonical']),'broken',r['broken_local_links'],'internal',r['internal_sentinel_count'],'samples',r['sample_label_count'])
