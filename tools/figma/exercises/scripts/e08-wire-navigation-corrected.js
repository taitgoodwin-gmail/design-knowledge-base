const page=await figma.getNodeByIdAsync('63:8');await figma.setCurrentPageAsync(page);
const frames=await Promise.all(['63:9','63:22','63:35'].map(id=>figma.getNodeByIdAsync(id)));
const nav=to=>({type:'NODE',destinationId:to,navigation:'NAVIGATE',transition:{type:'SMART_ANIMATE',easing:{type:'LINEAR'},duration:6},resetScrollPosition:true});
const changed=[];
for(let i=0;i<frames.length;i++){
 const f=frames[i],source=f.children.find(n=>n.name==='Source button'),error=f.children.find(n=>n.name==='Error button');
 await source.setReactionsAsync([{trigger:{type:'ON_CLICK'},actions:[nav(i===1?'63:9':'63:22')]}]);
 await error.setReactionsAsync([{trigger:{type:'ON_CLICK'},actions:[nav(i===2?'63:9':'63:35')]}]);changed.push(source.id,error.id);
}
page.flowStartingPoints=[{nodeId:'63:9',name:'E08 / Source disclosure'}];
return {mutatedNodeIds:[page.id,...changed],flows:page.flowStartingPoints,reactions:frames.flatMap(f=>f.children.filter(n=>changed.includes(n.id)).map(n=>({id:n.id,name:n.name,reactions:n.reactions})))};
