from pathlib import Path
import base64, html, json, re

ROOT = Path(__file__).resolve().parent

def inline(text):
    text = html.escape(text)
    links=[]
    def save_link(m):
        links.append('<a href="'+m[2]+'" target="_blank" rel="noreferrer">'+m[1]+'</a>')
        return 'LINKPLACEHOLDER'+str(len(links)-1)+'END'
    text = re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)', save_link, text)
    text = re.sub(r'https?://[^\s<]+', lambda m:'<a href="'+m[0].rstrip('.,;)')+'" target="_blank" rel="noreferrer">'+m[0].rstrip('.,;)')+'</a>'+m[0][len(m[0].rstrip('.,;)')):], text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    for i,link in enumerate(links): text=text.replace('LINKPLACEHOLDER'+str(i)+'END',link)
    return text

def markdown(text):
    result=[]; para=[]; list_type=None
    def flush():
        if para: result.append('<p>'+inline(' '.join(para))+'</p>'); para.clear()
    def close_list():
        nonlocal list_type
        if list_type: result.append('</'+list_type+'>'); list_type=None
    for line in text.splitlines():
        if not line.strip(): flush(); close_list(); continue
        heading=re.match(r'^(#{1,6}) (.*)',line)
        item=re.match(r'^(?:[-*]|\d+\.) (.*)',line)
        if heading:
            flush(); close_list(); n=min(len(heading[1])+1,6)
            result.append(f'<h{n}>'+inline(heading[2])+f'</h{n}>')
        elif item:
            flush(); typ='ol' if line[0].isdigit() else 'ul'
            if list_type!=typ: close_list(); result.append('<'+typ+'>'); list_type=typ
            result.append('<li>'+inline(item[1])+'</li>')
        else: close_list(); para.append(line)
    flush(); close_list(); return '\n'.join(result)

entries=[
 ('Risograph','01-risograph.jpeg','Printing process / visual analogy','Look for separated color layers, large lettering and intersections that create another color. The screenshot suggests overprinting; it cannot prove how the poster was physically printed.','Try describing the composition with no reference to grain. Does the overlap explain anything?'),
 ('Claymorphism','02-claymorphism.jpeg','Informal material/form label','Observe the blue fins, green folds, coral cylinders and glossy rounded forms. Their lighting and edge treatment make them look dimensional. The original Simplicity21 portfolio ties five objects to conference themes.','Which cues make one object seem soft and another hard? Compare the edge and highlight, not just the color.'),
 ('Organic Tech','03-organic-tech.jpeg','Descriptive aesthetic label','Intricate porous and tufted forms surround a very plain information card. Their contrast creates the visual tension. Authorship of this crop is unverified.','Cover the organic imagery, then cover the white card. What does each contribute?'),
 ('Holographic Iridescence','09-overview.jpeg','Material effect; overview only','The small fourth tile suggests shifting reflective color. Its maker and physical process are unknown. Real angle-dependent color effects differ from a static rainbow gradient.','Separate color variation, highlights and geometric form. Which one is supplying the metallic impression?'),
 ('Dirty Gradients','04-dirty-gradients.jpeg','Descriptive surface label','The color fields move through muted warm/cool transitions. Their broad horizontal structure and restrained information matter. Exact grain and production methods are unverified.','Compare the transition width and the quiet region behind text. Where does color carry atmosphere?'),
 ('Austurbane','05-austurbane.jpeg','Attributed contemporary classification','CARI credits Alex Edwards with the label. This screenshot shows overlapping pastel packages, fine serif titles and restrained marks. Its exact artist credit is unresolved.','How much of the character comes from color, and how much from spacing, angles and photography?'),
 ('Asian Chic','09-overview.jpeg','Broad label; overview only','The seventh tile shows a dense frame, portrait and saturated colors. That is not enough to identify cultural lineage, script or maker. The phrase has separate documented use in fashion scholarship.','Describe only visible structure first. What would a maker, place and date add to your interpretation?'),
 ('Clean Girl Brutalism','06-clean-girl-brutalism.jpeg','Compound label; origin unverified','AGNI concentrates visual weight in a large heading and a small pink block, with a very quiet field between. Related brutalist labels do not establish this compound as a formal movement.','What attracts you first, second and third? Notice how emptiness creates hierarchy.'),
 ('Spray','07-spray.jpeg','Gestural technique / visual vocabulary','Blue freehand marks dominate a white package while small black information remains separately typeset. Spray-stencil work in other contexts can communicate a very different attitude.','Which marks carry personality and which text carries facts? Could one survive without the other?'),
 ('Gzhel','08-gzhel.jpeg','Ceramic tradition; screenshot attribution unresolved','The supplied LOEWE bag shows blue birds and foliage in a repeated grid. It has not been authenticated as Gzhel. A De Morgan collaboration is a possible lead, not a confirmed match.','Study repetition, tonal range and empty space while keeping the provenance question open.')
]
data=[]
for name,file,kind,obs,question in entries:
    data.append(dict(name=name,kind=kind,observation=obs,question=question,image='data:image/jpeg;base64,'+base64.b64encode((ROOT/'references'/file).read_bytes()).decode()))
buttons=''.join(f'<button type="button" data-reference="{i}" aria-pressed="{str(i==0).lower()}">{html.escape(e[0])}</button>' for i,e in enumerate(entries))
research=''
for path in ['history-and-print.md','contemporary-materials.md','perception-and-motion.md','tiktok-discovery.md','lucy-eden-source-notes.md','zach-heffner-aisthetes.md']:
    p=ROOT/'research'/path
    text=p.read_text()
    research+='<details class="chapter"><summary>'+html.escape(text.splitlines()[0].lstrip('# '))+'</summary><article>'+markdown(text)+'</article></details>'
guide=markdown((ROOT/'START-HERE.md').read_text())
material=(ROOT/'material-study.html').read_text()
page='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Visual Design Study — A Learning Library</title>
<style>
:root{color-scheme:light;--background:#f5f2eb;--foreground:#1c2428;--blue:#4669c4;--red:#e26a79;--purple:#9b65bb;--green:#83bba9;--border:#c4c3bc;--primary:#213e46;--primary-foreground:#fff;--font-size-base:16px}
*{box-sizing:border-box}body{margin:0;background:var(--background);color:var(--foreground);font:17px/1.65 system-ui,sans-serif}main{max-width:1080px;margin:auto;padding:48px 28px 80px}h1{font-family:Georgia,serif;font-size:clamp(38px,7vw,74px);font-weight:400;line-height:1.07;letter-spacing:-.045em;max-width:840px;margin:20px 0}h2{font-size:28px;line-height:1.2;margin-top:36px}h3{font-size:22px;line-height:1.3}h4{font-size:19px}p,li{max-width:78ch}a{color:#244f85;text-underline-offset:3px;overflow-wrap:anywhere}button,input,select{font:inherit}button{cursor:pointer;background:transparent;color:inherit;border:1px solid var(--border);border-radius:5px;padding:9px 13px;min-height:44px}button[aria-pressed=true]{background:var(--primary);color:var(--primary-foreground);border-color:var(--primary)}button:focus-visible,a:focus-visible,input:focus-visible,summary:focus-visible{outline:3px solid #7966b7;outline-offset:3px}.eyebrow{font-size:13px;letter-spacing:.13em;text-transform:uppercase}.intro{font-size:20px;max-width:720px}nav{display:flex;gap:24px;flex-wrap:wrap;border-block:1px solid var(--border);padding:16px 0;margin:35px 0}section{scroll-margin-top:20px}.ref-buttons,.viz-controls{display:flex;flex-wrap:wrap;gap:8px}.reference{display:grid;grid-template-columns:minmax(160px,282px) 1fr;gap:36px;align-items:start;margin:28px 0 50px}.reference img{width:100%;height:auto;max-height:560px;object-fit:contain;object-position:left top}.reference h3{margin-top:0}.reference .kind{font-size:13px;text-transform:uppercase;letter-spacing:.08em}.question{border-left:3px solid #b3a488;padding-left:18px}.lab{border-top:1px solid var(--border);margin-top:35px;padding-top:15px}.lab-note{font-size:15px}.experiment{margin:20px 0;padding:28px;max-width:740px;background:#fff;border:1px solid var(--border)}.pairs{display:grid;grid-template-columns:1fr 1fr;gap:35px}.pairs div{min-width:0}.pairs h4{margin:0}.pairs p{margin:var(--spacing,12px) 0 0}.controls{display:flex;gap:20px;align-items:center;flex-wrap:wrap}.controls label{display:flex;align-items:center;gap:12px}.controls input{max-width:180px}.texture-demo{position:relative;min-height:220px;background:linear-gradient(130deg,#a5bfd1,#ede4ce 55%,#cc8774);overflow:hidden;padding:32px}.texture-demo h4,.texture-demo p{position:relative;margin:0 0 10px;color:#16282e}.grain-svg{position:absolute;inset:0;width:100%;height:100%;opacity:.12;pointer-events:none}.chapter{border-top:1px solid var(--border);padding:18px 0}.chapter summary{cursor:pointer;font-size:20px;font-weight:600;padding:5px 0}.chapter article{max-width:850px;padding:0 8px}.chapter p,.chapter li{overflow-wrap:anywhere}.text-small{font-size:14px}.material-demo{max-height:340px}footer{margin-top:45px;border-top:1px solid var(--border);padding-top:20px;font-size:14px}@media(max-width:600px){main{padding:28px 18px 50px}.reference{grid-template-columns:1fr;gap:20px}.reference img{max-width:240px;margin:auto}.pairs{gap:18px}.experiment{padding:20px}.texture-demo{padding:24px}nav{gap:15px}h2{font-size:25px}.controls label{flex-wrap:wrap}}@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important;animation:none!important;transition:none!important}}
</style></head><body><main>
<div class="eyebrow">A saved study · 7–8 September 2026 · First edition</div>
<h1>Learn to see<br>what makes it work.</h1>
<p class="intro">Nine original references. Ten visual labels. Three research perspectives. Explore structure, material, color and detail before choosing a design direction.</p>
<nav aria-label="Study sections"><a href="#references">Look at the references</a><a href="#experiments">Try the experiments</a><a href="#reading">Read the research</a><a href="#course">Learning guide</a></nav>
<section id="references"><h2>The reference collection</h2><p>Select a label to inspect the original screenshot and separate visible evidence from interpretation. The two overview-only styles use the supplied overview at its original resolution.</p>
<div class="ref-buttons">__BUTTONS__</div>
<div class="reference"><img id="reference-image" src="__FIRST_IMAGE__" alt="Original user-supplied Risograph reference screenshot"><div aria-live="polite"><p class="kind" id="reference-kind">__FIRST_KIND__</p><h3 id="reference-name">Risograph</h3><p id="reference-observation">__FIRST_OBS__</p><p class="question" id="reference-question">__FIRST_QUESTION__</p></div></div></section>
<section id="experiments"><h2>Three ways to train your eye</h2><p>These original demonstrations isolate a few variables. They are visual analogies and preference exercises, not physical simulations or tests of commercial effectiveness.</p>
<div class="lab"><h3>1. Same composition, different material</h3><p class="lab-note">Switch the treatment while the shapes and their positions stay fixed.</p>__MATERIAL__</div>
<div class="lab"><h3>2. Spacing changes the relationship</h3><div class="controls"><label for="spacing">Title-to-description gap <output id="spacing-value">12 px</output><input id="spacing" type="range" min="0" max="64" value="12"></label></div><div class="experiment pairs" id="spacing-scene"><div><h4>Shape</h4><p>What does the silhouette suggest?</p></div><div><h4>Surface</h4><p>What makes the material convincing?</p></div></div><p class="lab-note">Only the internal gap changes. Notice when each description starts to feel detached from its title.</p></div>
<div class="lab"><h3>3. Texture changes the reading surface</h3><div class="controls"><label for="grain">Grain opacity <output id="grain-value">12%</output><input id="grain" type="range" min="0" max="60" value="12"></label></div><div class="experiment texture-demo"><svg class="grain-svg" id="grain-layer" aria-hidden="true"><filter id="texture-noise"><feTurbulence type="fractalNoise" baseFrequency=".7" numOctaves="3" seed="19"/></filter><rect width="100%" height="100%" filter="url(#texture-noise)"/></svg><h4>A clear idea, a textured field.</h4><p>The words, layout and base gradient stay fixed. Change only the strength of the grain.</p></div><p class="lab-note">Describe the tradeoff you see. This exercise does not produce an accessibility score.</p></div></section>
<section id="reading"><h2>Research, with the sources exposed</h2><p>Each contributor distinguishes observed screenshots, documented claims, interpretations and unresolved questions. Source failures are retained in the notes rather than treated as completed reading.</p>__RESEARCH__</section>
<section id="course"><details class="chapter" open><summary>Learning guide and how to use this library</summary><article>__GUIDE__</article></details></section>
<footer>Original screenshots preserved unmodified. Demonstrations authored for this study. No logo or website direction selected. External source links open only when you choose them; the study itself works offline.</footer>
</main><script>
const references=__DATA__;
document.querySelectorAll('[data-reference]').forEach(button=>button.addEventListener('click',()=>{
 const item=references[Number(button.dataset.reference)];
 document.querySelectorAll('[data-reference]').forEach(peer=>peer.setAttribute('aria-pressed',String(peer===button)));
 document.getElementById('reference-image').src=item.image;
 document.getElementById('reference-image').alt='Original user-supplied '+item.name+' reference screenshot';
 document.getElementById('reference-name').textContent=item.name;
 document.getElementById('reference-kind').textContent=item.kind;
 document.getElementById('reference-observation').textContent=item.observation;
 document.getElementById('reference-question').textContent=item.question;
}));
document.getElementById('spacing').addEventListener('input',e=>{document.getElementById('spacing-scene').style.setProperty('--spacing',e.target.value+'px');document.getElementById('spacing-value').textContent=e.target.value+' px';});
document.getElementById('grain').addEventListener('input',e=>{document.getElementById('grain-layer').style.opacity=Number(e.target.value)/100;document.getElementById('grain-value').textContent=e.target.value+'%';});
</script></body></html>'''
replace={'__BUTTONS__':buttons,'__FIRST_IMAGE__':data[0]['image'],'__FIRST_KIND__':data[0]['kind'],'__FIRST_OBS__':data[0]['observation'],'__FIRST_QUESTION__':data[0]['question'],'__MATERIAL__':material,'__RESEARCH__':research,'__GUIDE__':guide,'__DATA__':json.dumps(data).replace('</','<\/')}
for k,v in replace.items():page=page.replace(k,v)
(ROOT/'study-book.html').write_text(page)
print(json.dumps({'output':str(ROOT/'study-book.html'),'bytes':len(page.encode()),'references':len(data),'chapters':6}))
