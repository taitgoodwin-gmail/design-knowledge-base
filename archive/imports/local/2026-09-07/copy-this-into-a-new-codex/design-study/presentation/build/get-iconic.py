from pathlib import Path
import json,urllib.request
out=Path('design-study/presentation/assets')
for s in json.loads(Path('design-study/slides-content-iconic.json').read_text()):
 if s.get('image_url'):
  ext='svg' if '.svg' in s['image_url'] else 'jpg'
  try:
   b=urllib.request.urlopen(urllib.request.Request(s['image_url'],headers={'User-Agent':'Mozilla/5.0'}),timeout=20).read(); (out/(s['id']+'.'+ext)).write_bytes(b);print(s['id'],len(b))
  except Exception as e:print(s['id'],e)
