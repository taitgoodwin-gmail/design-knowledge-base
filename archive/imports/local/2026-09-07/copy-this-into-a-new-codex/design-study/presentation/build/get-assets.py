from pathlib import Path
import json,urllib.request,concurrent.futures
out=Path('design-study/presentation/assets')
data=json.loads((out/'geist-provenance.json').read_text())
print(data.keys())
items=data.get('failures',[])
def get(a):
 try:
  req=urllib.request.Request(a['url'],headers={'User-Agent':'Mozilla/5.0'})
  b=urllib.request.urlopen(req,timeout=20).read();p=out/a['name'];p.write_bytes(b);return {'name':a['name'],'bytes':len(b)}
 except Exception as e:return {'name':a['name'],'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: print(list(ex.map(get,items)))
