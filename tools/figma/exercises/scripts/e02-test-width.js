const page=await figma.getNodeByIdAsync('34:8');await figma.setCurrentPageAsync(page);const card=await figma.getNodeByIdAsync('35:8');const question=await figma.getNodeByIdAsync('35:9');const answer=await figma.getNodeByIdAsync('35:10');const disclosure=await figma.getNodeByIdAsync('35:13');await figma.loadFontAsync({family:'Inter',style:'Regular'});await figma.loadFontAsync({family:'Inter',style:'Bold'});
const cases=[];const width=320;
card.resize(width,card.height);card.primaryAxisSizingMode='AUTO';
for(const length of ['short','long']){
question.characters=length==='short'?'Where does this answer come from?':'How can a team tell whether a generated answer is supported by a reliable, relevant and current source?';
answer.characters=length==='short'?'Inspect the source behind an AI answer.':'A citation is a starting point, not a guarantee. Open the original material, check the publication date, compare the quoted claim with its context, and record what the evidence supports. A useful answer should also disclose uncertainty and distinguish an observation from an interpretation.';
for(const open of [false,true]){disclosure.visible=open;
const children=card.children.filter(n=>n.visible).map(n=>({id:n.id,name:n.name,x:n.x,y:n.y,width:n.width,height:n.height}));
const violations=[];for(let i=0;i<children.length;i++){const n=children[i];if(n.x<card.paddingLeft-0.1||n.x+n.width>card.width-card.paddingRight+0.1||n.y+n.height>card.height-card.paddingBottom+0.1)violations.push('bounds:'+n.name);if(i&&n.y<children[i-1].y+children[i-1].height-0.1)violations.push('overlap:'+n.name);}
cases.push({width,length,open,card:{width:card.width,height:card.height},children,violations});}}
return {mutatedNodeIds:[card.id,question.id,answer.id,disclosure.id],cases};
