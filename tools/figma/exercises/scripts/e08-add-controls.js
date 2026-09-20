const page=await figma.getNodeByIdAsync('63:8');await figma.setCurrentPageAsync(page);
const card=await figma.getNodeByIdAsync('63:9'),button=await figma.getNodeByIdAsync('63:12');
for(const t of card.findAllWithCriteria({types:['TEXT']})) for(const s of t.getStyledTextSegments(['fontName'])) await figma.loadFontAsync(s.fontName);
const created=[];
for(const [name,label] of [['Error button','Simulate source error'],['Back button','Back'],['Restart button','Restart flow']]){
 const b=button.clone();card.appendChild(b);b.name=name;b.layoutSizingHorizontal='FILL';b.children[0].characters=label;created.push(b.id,...b.children.map(n=>n.id));
}
return {createdNodeIds:created,mutatedNodeIds:[card.id],children:card.children.map(n=>({id:n.id,name:n.name,y:n.y,width:n.width,height:n.height,visible:n.visible}))};
