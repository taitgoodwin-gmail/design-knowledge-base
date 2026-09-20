const sourcePage=await figma.getNodeByIdAsync('34:8');
await figma.setCurrentPageAsync(sourcePage);
const source=await figma.getNodeByIdAsync('35:8');
for(const t of source.findAllWithCriteria({types:['TEXT']})){
 for(const s of t.getStyledTextSegments(['fontName'])) await figma.loadFontAsync(s.fontName);
}
const page=figma.createPage(); page.name='LAB / Prototype behavior / 2026-09-20';
const card=source.clone(); page.appendChild(card); card.name='E08 / Closed';card.x=160;card.y=160;
card.resize(390,640);card.primaryAxisSizingMode='FIXED';card.counterAxisSizingMode='FIXED';
const byName=name=>card.children.find(n=>n.name===name);
byName('Question').characters='What supports this answer?';
byName('Answer').characters='A citation is a starting point. Open the original source and check its date and context.';
byName('Source button').children[0].characters='Show source';
byName('Disclosure').visible=false;
byName('Following content').characters='Next: compare the evidence.';
return {pageId:page.id,createdNodeIds:[page.id,card.id,...card.findAll(()=>true).map(n=>n.id)],cardId:card.id,children:card.children.map(n=>({id:n.id,name:n.name,width:n.width,height:n.height,y:n.y,visible:n.visible})),fontFamilies:card.findAllWithCriteria({types:['TEXT']}).map(t=>t.fontName)};
