const p=await figma.getNodeByIdAsync('63:8');await figma.setCurrentPageAsync(p);
const following=await figma.getNodeByIdAsync('63:28');following.name='Following content';
const ids=['63:12','63:16','63:25','63:29','63:38','63:42'];
for(const id of ids){const n=await figma.getNodeByIdAsync(id);const reactions=n.reactions.map(r=>({trigger:r.trigger,actions:r.actions.map(a=>({...a,transition:{type:'SMART_ANIMATE',easing:{type:'EASE_OUT'},duration:.2}}))}));await n.setReactionsAsync(reactions);}
return {mutatedNodeIds:[following.id,...ids],durationSeconds:.2,easing:'EASE_OUT',nameRestored:following.name};
