from pathlib import Path
import json
p=Path('design-study/presentation/build/content.json');d=json.loads(p.read_text());ico=json.loads(Path('design-study/slides-content-iconic.json').read_text())
for x in ico:
 x.update(kind='text',section='Logo craft')
 if x.get('image_url'):x.update(image='assets/'+x['id']+('.svg.png' if '.svg' in x['image_url'] else '.jpg'),kind='landscape')
pos=next(i for i,x in enumerate(d) if x['id']=='brand-01');d[pos:pos]=ico
for x in d:
 if (x.get('image') or '').endswith('.svg'):x['image']+='.png'
 if x['id']=='brand-02':x.update(image='assets/lucy-bluey-full.png',kind='landscape')
 if x['id'] in ['brand-03','brand-04','brand-05']:x['notes']+=' Source text was available in the saved research. A fresh screenshot attempt for Splatter returned Page Not Found on 8 September 2026. The original logo assets are not reproduced on this slide. Recheck the current portfolio before relying on the link.'
 x['title']=x['title'].replace('—',' / ').replace('not the same as already familiar','and familiarity')
 x['body']=[s.replace(' → ',' informs ').replace('—not',' rather than').replace('—',' / ').replace(' • ',' / ') for s in x['body']]
urls=[]
for x in d:
 for u in x.get('source_urls',[]):
  if u not in urls:urls.append(u)
for i in range(0,len(urls),7):
 batch=urls[i:i+7];d.append(dict(id='sources-'+str(i//7+1),title='Source directory '+str(i//7+1),body=batch,notes='Sources are linked on the teaching slides as well as in this directory. Access dates and qualification details appear in the corresponding speaker notes. Original artworks remain the property of their creators. Inclusion supports private study and does not provide a reuse license.',source_urls=batch,kind='sources',section='Source directory'))
p.write_text(json.dumps(d,ensure_ascii=False,indent=2));print(len(d), 'slides',len(urls),'unique URLs')
