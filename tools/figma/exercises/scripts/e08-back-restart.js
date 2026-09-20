const page=await figma.getNodeByIdAsync('63:8');await figma.setCurrentPageAsync(page);
const frames=await Promise.all(['63:9','63:22','63:35'].map(id=>figma.getNodeByIdAsync(id)));
const changed=[];
for(const f of frames){
 f.resize(390,640);f.primaryAxisSizingMode='FIXED';f.counterAxisSizingMode='FIXED';changed.push(f.id);
 const back=f.children.find(n=>n.name==='Back button');await back.setReactionsAsync([{trigger:{type:'ON_CLICK'},actions:[{type:'BACK'}]}]);changed.push(back.id);
 if(f.id!=='63:9'){
  const restart=f.children.find(n=>n.name==='Restart button');await restart.setReactionsAsync([{trigger:{type:'ON_CLICK'},actions:[{type:'NODE',destinationId:'63:9',navigation:'NAVIGATE',transition:null,resetScrollPosition:true,resetInteractiveComponents:true}]}]);changed.push(restart.id);
 }
}
for(const [id,label] of [['63:21','At start'],['63:43','Return to closed']]){
 const n=await figma.getNodeByIdAsync(id);for(const s of n.getStyledTextSegments(['fontName']))await figma.loadFontAsync(s.fontName);n.characters=label;changed.push(n.id);
}
return {mutatedNodeIds:changed,frames:frames.map(f=>({id:f.id,width:f.width,height:f.height,layoutMode:f.layoutMode,sizing:f.primaryAxisSizingMode,children:f.children.map(n=>({id:n.id,name:n.name,y:n.y,height:n.height,reactions:'reactions'in n?n.reactions:undefined}))}))};
