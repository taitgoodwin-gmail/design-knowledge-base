const p=await figma.getNodeByIdAsync('63:8');await figma.setCurrentPageAsync(p);
const ids=['63:34','63:47'];for(const id of ids){const n=await figma.getNodeByIdAsync(id);for(const s of n.getStyledTextSegments(['fontName']))await figma.loadFontAsync(s.fontName);n.characters='Reset to closed';}
const closedBack=await figma.getNodeByIdAsync('63:18');closedBack.visible=false;await closedBack.setReactionsAsync([]);
const inactive=await figma.getNodeByIdAsync('63:20');inactive.visible=false;
return {mutatedNodeIds:[...ids,closedBack.id,inactive.id],resetMeaning:'Navigation to closed; does not erase history',startControls:'Hidden Back and inactive pseudo-button; no empty-history action offered'};
