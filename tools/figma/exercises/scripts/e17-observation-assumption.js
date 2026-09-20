const data=[{"kind":"observation","title":"01 / Observation","x":80,"y":360,"tint":[245,251,255],"body":"OBSERVED · 20 SEP 2026\nIn the six-second Figma test, disclosure text faded in while other text moved. Temporary overlap was visible; settled states were readable.\nScope: one lab fixture, not user research.","linkText":"Open the recorded experiment","url":"https://github.com/taitgoodwin-gmail/design-knowledge-base/blob/dd81a55a646080b0a3c60b497601dbbfd61685b6/tools/figma/evidence/lab/prototype-and-handoff.md"},{"kind":"assumption","title":"02 / Assumption","x":800,"y":360,"tint":[248,245,255],"body":"HYPOTHESIS · NOT VALIDATED\nMoving reading text may distract someone checking evidence. A source trail could improve confidence only if the source is useful and relevant.\nNo conversion or GEO lift is established.","linkText":"Read the distinction in our practice","url":"https://github.com/taitgoodwin-gmail/design-knowledge-base/blob/dd81a55a646080b0a3c60b497601dbbfd61685b6/governance/official-source-build-practice.md"}];
await figma.loadFontAsync({family:'Inter',style:'Bold'});await figma.loadFontAsync({family:'Inter',style:'Regular'});
const board=await figma.getNodeByIdAsync('2:2');const ids=[];const results=[];
const black={r:0x1e/255,g:0x1e/255,b:0x1e/255};
function tx(parent,name,copy,size,style,x,y,w){const n=figma.createText();parent.appendChild(n);n.name=name;n.fontName={family:'Inter',style};n.fontSize=size;n.lineHeight={unit:'PERCENT',value:150};n.fills=[{type:'SOLID',color:black}];n.characters=copy;n.textAutoResize='HEIGHT';n.resize(w,n.height);n.x=x;n.y=y;ids.push(n.id);return n;}
for(const d of data){
 const zone=figma.createSection();board.appendChild(zone);zone.name='';zone.x=d.x;zone.y=d.y;zone.resize(520,480);zone.fills=[{type:'SOLID',color:{r:d.tint[0]/255,g:d.tint[1]/255,b:d.tint[2]/255}}];ids.push(zone.id);
 const heading=tx(zone,d.kind+' heading',d.title,32,'Bold',24,20,472);
 const card=figma.createSection();zone.appendChild(card);card.name='';card.x=24;card.y=92;card.resize(472,340);card.fills=[{type:'SOLID',color:{r:1,g:1,b:1}}];ids.push(card.id);
 const body=tx(card,d.kind+' body',d.body,24,'Regular',24,24,424);
 const link=tx(card,d.kind+' source',d.linkText,20,'Regular',24,body.y+body.height+24,424);link.setRangeHyperlink(0,link.characters.length,{type:'URL',value:d.url});link.textDecoration='UNDERLINE';
 card.resize(472,link.y+link.height+24);zone.resize(520,Math.max(480,card.y+card.height+24));
 results.push({kind:d.kind,zoneId:zone.id,bodyId:body.id,linkId:link.id,height:zone.height,link:link.getRangeHyperlink(0,link.characters.length)});
}
return {createdNodeIds:ids,cards:results};
