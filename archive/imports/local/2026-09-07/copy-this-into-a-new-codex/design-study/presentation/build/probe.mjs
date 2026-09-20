import {Presentation,PresentationFile} from '@oai/artifact-tool';
import {resolvePresentationFont} from '/Users/tag/.codex/plugins/cache/openai-primary-runtime/presentations/26.905.11957/skills/presentations/container_tools/artifact_tool_utils.mjs';
console.log(resolvePresentationFont({fontFamily:'Arial'}));
const p=Presentation.create({slideSize:{width:1280,height:720}}); const s=p.slides.add(); const t=s.shapes.add({geometry:'textbox',position:{left:50,top:50,width:1100,height:150},fill:'none',line:{fill:'none',width:0}});t.text='Design field guide';t.text.style={fontSize:60,typeface:'Arial',color:'#142735'};await(await PresentationFile.exportPptx(p)).save('design-study/presentation/build/probe.pptx');console.log('exported');
