const page=await figma.getNodeByIdAsync('34:8');await figma.setCurrentPageAsync(page);
await figma.loadFontAsync({family:'Inter',style:'Regular'});await figma.loadFontAsync({family:'Inter',style:'Bold'});
const ids=[];const card=figma.createAutoLayout('VERTICAL');ids.push(card.id);card.name='E02 / Responsive evidence card';card.x=160;card.y=160;card.resize(320,100);card.primaryAxisSizingMode='AUTO';card.counterAxisSizingMode='FIXED';card.paddingTop=24;card.paddingBottom=24;card.paddingLeft=24;card.paddingRight=24;card.itemSpacing=16;card.cornerRadius=16;card.fills=[figma.util.solidPaint('#F6F8FF')];card.clipsContent=false;
function text(name,characters,size,bold,parent){const t=figma.createText();ids.push(t.id);t.name=name;t.fontName={family:'Inter',style:bold?'Bold':'Regular'};t.fontSize=size;t.lineHeight={unit:'PERCENT',value:150};t.characters=characters;t.fills=[figma.util.solidPaint('#16223D')];parent.appendChild(t);t.textAutoResize='HEIGHT';t.layoutSizingHorizontal='FILL';return t;}
text('Question','Where does this answer come from?',24,true,card);
text('Answer','Inspect the source behind an AI answer.',16,false,card);
const button=figma.createAutoLayout('HORIZONTAL');ids.push(button.id);button.name='Source button';card.appendChild(button);button.paddingLeft=16;button.paddingRight=16;button.paddingTop=12;button.paddingBottom=12;button.minHeight=48;button.layoutSizingHorizontal='FILL';button.fills=[figma.util.solidPaint('#274BDD')];button.cornerRadius=8;const label=text('Source label','Read source',16,true,button);label.fills=[figma.util.solidPaint('#FFFFFF')];
const disclosure=text('Disclosure','This is an illustrative lab fixture. It is not a live AI answer or evidence of search performance.',14,false,card);disclosure.visible=false;
text('Following content','Next: compare the evidence.',14,false,card);
return {createdNodeIds:ids,cardId:card.id,children:card.children.map(n=>({id:n.id,name:n.name,type:n.type}))};
