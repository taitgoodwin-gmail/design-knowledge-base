await figma.loadFontAsync({family:'Inter',style:'Bold'});await figma.loadFontAsync({family:'Inter',style:'Regular'});
const board=figma.createSection();board.name='';board.x=160;board.y=160;board.resize(2200,1620);board.fills=[{type:'SOLID',color:{r:1,g:1,b:1}}];
function text(name,copy,size,style,x,y,width){const n=figma.createText();board.appendChild(n);n.name=name;n.fontName={family:'Inter',style};n.fontSize=size;n.fills=[{type:'SOLID',color:{r:0x1e/255,g:0x1e/255,b:0x1e/255}}];n.characters=copy;n.textAutoResize='HEIGHT';n.resize(width,n.height);n.x=x;n.y=y;return n;}
const title=text('Board title','Decisions you can trace',64,'Bold',80,64,2000);
const subtitle=text('Board instructions','E17 / Evidence-led UI decisions\nRead observation → assumption → decision. Challenge the assumption below; keep the source and the test result attached.',28,'Regular',80,168,1800);
return {createdNodeIds:[board.id,title.id,subtitle.id],boardId:board.id,editorType:figma.editorType,children:board.children.map(n=>({id:n.id,name:n.name,x:n.x,y:n.y,width:n.width,height:n.height}))};
