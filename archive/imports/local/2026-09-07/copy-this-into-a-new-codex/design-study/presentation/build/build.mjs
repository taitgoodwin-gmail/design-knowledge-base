import fs from 'node:fs/promises';import path from 'node:path';import {Presentation,PresentationFile} from '@oai/artifact-tool';import sharp from 'sharp';
import {finalizePresentation} from '/Users/tag/.codex/plugins/cache/openai-primary-runtime/presentations/26.905.11957/skills/presentations/container_tools/artifact_tool_utils.mjs';
const W=path.resolve('design-study/presentation'),B=path.join(W,'build'),O=path.join(W,'output');
const data=JSON.parse(await fs.readFile(path.join(B,'content.json'),'utf8'));const p=Presentation.create({slideSize:{width:1280,height:720}});
const C={paper:'#F5F2EA',ink:'#182B32',accent:'#B24837',muted:'#52676B',dark:'#16333A',pale:'#B4CDC9'};
function text(s,content,x,y,w,h,size=28,color=C.ink,bold=false){const t=s.shapes.add({geometry:'textbox',name:content.slice(0,40),position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});t.text=content;t.text.style={fontSize:size,typeface:'Arial',color,bold,autoFit:'none',wrap:'square',verticalAlignment:'top',insets:{top:0,bottom:0,left:0,right:0}};return t;}
async function img(s,file,x,y,w,h){const actual=path.resolve(W,file);let bytes=await fs.readFile(actual);let meta=await sharp(bytes).metadata();let k=Math.min(w/meta.width,h/meta.height);s.images.add({blob:new Uint8Array(bytes),contentType:meta.format==='png'?'image/png':'image/jpeg',alt:path.basename(file),position:{left:x+(w-meta.width*k)/2,top:y+(h-meta.height*k)/2,width:meta.width*k,height:meta.height*k},fit:'contain'});}
function links(s,urls,dark=false,prefix='Source: '){urls.slice(0,2).forEach((u,i)=>{let host=new URL(u).hostname.replace(/^www\./,'');let t=text(s,(i?'Related source: ':prefix)+host,64,644+i*23,1060,21,15,dark?C.pale:C.muted);t.text.getRange(0,10000).link={uri:u,isExternal:true};});}
function box(s,x,y,w,h,fill,line='none'){s.shapes.add({geometry:'rect',position:{left:x,top:y,width:w,height:h},fill,line:{fill:line,width:1}});}
function diagram(s,d){
 text(s,d.title,64,48,1130,112,47,C.ink,true);
 if(d.diagram==='spacing'){
  for(let i=0;i<2;i++){let x=64+i*610;text(s,i?'Related items closer':'Even spacing',x,183,530,38,24,C.accent,true);
   text(s,'Material study',x,260,520,42,34,C.ink,true);text(s,'Light and texture',x,i?307:340,520,42,27);
   text(s,'Color study',x,420,520,42,34,C.ink,true);text(s,'Hue and contrast',x,i?467:500,520,42,27);
  }text(s,'Same words, type and width. Only the description’s vertical position changes.',64,575,1120,54,24,C.muted);
 }else if(d.diagram==='contrast'){
  text(s,'Variable reading surface',64,179,540,38,24,C.accent,true);text(s,'Solid reading surface',674,179,540,38,24,C.accent,true);
  for(let i=0;i<2;i++){let x=64+i*610;box(s,x,240,540,240,C.pale);if(!i)box(s,x+260,240,160,240,C.ink);text(s,'Make the message\neasy to read.',x+38,305,460,120,42,C.ink,true);}
  text(s,'Check the background beneath each letter. A palette alone is insufficient.',64,520,1130,67,30);
  text(s,'AA minimums: 4.5:1 ordinary text; 3:1 qualifying large text. Exceptions apply.',64,589,1130,38,22,C.muted);
 }else if(d.diagram==='motion'){
  text(s,'Proposed motion sequence',64,182,540,40,25,C.accent,true);
  for(let i=0;i<3;i++){let x=64+i*230;box(s,x,250,200,200,'none',C.pale);box(s,x+22+i*48,320,45,45,C.accent);text(s,'Frame '+(i+1),x,469,200,35,22,C.muted);}
  text(s,'Still alternative',824,182,360,40,25,C.accent,true);box(s,824,250,350,200,'none',C.pale);box(s,976,320,45,45,C.accent);text(s,'Meaning remains available',824,469,370,65,24,C.muted);
  text(s,'Keep meaning in the still state. Provide controls and reduced-motion support.',64,556,1120,70,29);
 }else if(d.diagram==='reflow'){
  text(s,'Wide composition',64,173,650,35,24,C.accent,true);text(s,'Narrow composition',844,173,360,35,24,C.accent,true);
  box(s,64,225,680,299,'none',C.pale);box(s,488,261,216,218,C.pale);text(s,'A material\npoint of view',95,270,370,100,38,C.ink,true);text(s,'Light, texture and color.',95,385,360,42,24);box(s,95,447,175,43,C.ink);text(s,'Explore',115,455,135,30,22,C.paper,true);
  box(s,844,225,360,326,'none',C.pale);text(s,'A material\npoint of view',865,245,315,88,33,C.ink,true);text(s,'Light, texture and color.',865,335,315,56,22);box(s,865,391,315,77,C.pale);box(s,865,487,175,43,C.ink);text(s,'Explore',885,495,135,30,22,C.paper,true);
  text(s,'Preserve hierarchy. Recompose the same text, image and action.',64,580,1120,45,29);
 }
 links(s,d.source_urls||[]);
}
for(let i=0;i<data.length;i++){
 const d=data[i],s=p.slides.add();const dark=d.kind==='divider'||d.kind==='cover';s.background.fill=dark?C.dark:C.paper;
 const number=String(i+1).padStart(2,'0'); text(s,number,1170,663,52,26,17,dark?C.pale:C.muted);
 if(d.kind==='cover'){text(s,'A field guide\nto expressive design',72,122,1100,230,74,C.paper,true);text(s,'Visual styles, logo craft and brand systems',76,430,1100,70,30,C.pale);text(s,'Living study edition 1.0 / 8 September 2026',76,592,1060,45,22,C.pale);}
 else if(d.kind==='divider'){text(s,d.title,72,160,1040,250,72,C.paper,true);text(s,d.body.join('\n'),76,455,1020,125,32,C.pale);}
 else if(d.kind==='portrait'){
  text(s,d.title,64,48,800,102,47,C.ink,true);
  for(let j=0;j<d.body.length;j++)text(s,d.body[j],64,202+j*112,710,105,30,C.ink,j===0);
  await img(s,d.image,845,104,345,509);text(s,'Visual: supplied reference screenshot',845,620,345,20,13,C.muted);links(s,d.source_urls||[],false,'Related research: ');
 }
 else if(d.kind==='landscape'){
  text(s,d.title,64,42,1130,103,44,C.ink,true);
  await img(s,d.image,64,177,660,415);
  for(let j=0;j<d.body.length;j++)text(s,d.body[j],784,181+j*102,420,95,26,C.ink,j===0);
  links(s,d.source_urls||[]);
 }
 else if(d.kind==='diagram'){diagram(s,d);}
 else if(d.kind==='sources'){
  text(s,d.title,64,48,1100,70,44,C.ink,true);
  for(let j=0;j<d.body.length;j++){let u=d.body[j];let t=text(s,u,64,155+j*65,1140,60,20,C.muted);t.text.getRange(0,u.length).link={uri:u,isExternal:true};}
 }
 else {
  text(s,d.title,64,48,1130,125,47,C.ink,true);
  let ys=d.body.length===4?[210,308,406,504]:d.body.length===3?[211,342,473]:[231,395];
  d.body.forEach((b,j)=>{text(s,String(j+1).padStart(2,'0'),66,ys[j]+3,58,40,22,C.accent,true);text(s,b,151,ys[j],1040,92,31,C.ink,j===0);});links(s,d.source_urls||[]);
 }
 let notes=(d.notes||'')+'\n\nLesson ID: '+d.id+'\nSection: '+d.section+'\n\nSources:\n'+(d.source_urls||[]).join('\n')+'\n\nStudy date: 8 September 2026.';
 if(d.image)notes+='\nVisual: '+(d.image.startsWith('../references/')?'Original user-supplied reference screenshot. Artwork attribution remains qualified in the lesson.':'Source visual from the credited case study or captured page.');
 s.speakerNotes.textFrame.setText(notes);
}
await fs.writeFile(path.join(B,'deck.proto.json'),JSON.stringify(p.toProto()));
await(await PresentationFile.exportPptx(p)).save(path.join(B,'candidate.pptx'));
console.log('Exported '+data.length+' slides');
const skill='/Users/tag/.codex/plugins/cache/openai-primary-runtime/presentations/26.905.11957/skills/presentations';
const result=await finalizePresentation({workspaceDir:W,candidatePath:path.join(B,'candidate.pptx'),finalPath:path.join(O,'Design-Field-Guide-v2.pptx'),pythonExecutable:'/Users/tag/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3',integrityValidatorPath:skill+'/container_tools/inspect_presentation_package_integrity.py',layoutValidatorPath:skill+'/container_tools/inspect_presentation_layout_geometry.py',layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit'],fontPolicy:{basis:'design',families:['Arial']},verifyArtifactToolImport:true,receiptPath:path.join(B,'validation-v2.json')});console.log(JSON.stringify(result));
