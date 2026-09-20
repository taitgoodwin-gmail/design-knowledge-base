const fs=require('fs'),vm=require('vm'),path=require('path');
const root=path.resolve(__dirname,'..');
const files=['index.html','what-is-geo.html','research-hub.html','answer-engine-index-q3-2026.html'];
async function test(file,mode){
 let source=fs.readFileSync(path.join(root,'reference-build/site-v3.1/dist',file),'utf8');
 let code=source.slice(source.indexOf('var AUDIT_ENDPOINT ='));
 code=code.split('</script>')[0].split('// motion: opt-in')[0];
 let nodes={},now=100000,requests=[];
 function node(id){return nodes[id]??=( {id,value:'',hidden:id==='domrow',textContent:id==='auditbtn'?'Submit':'',disabled:false,attrs:{},listeners:{},classList:{remove(){},add(){}},checkValidity(){return this.value.includes('@')},setAttribute(k,v){this.attrs[k]=v},removeAttribute(k){delete this.attrs[k]},addEventListener(k,f){this.listeners[k]=f}})}
 const context={window:{MLX_AUDIT_ENDPOINT:mode==='absent'?null:'/test-only'},document:{getElementById:node},Date:{now:()=>now},fetch:async(url,init)=>{requests.push(JSON.parse(init.body));if(mode==='network')throw Error('offline');return{ok:mode==='accepted'||mode==='false-body',status:mode==='rate'?429:mode==='server'?500:202,json:async()=>({ok:mode!=='false-body',lead_id:'mock'})}},console};
 vm.runInNewContext(code,context);
 now+=3000;node('auditemail').value='audit@example.com';
 node('auditform').listeners.submit({preventDefault(){}});
 await new Promise(resolve=>setImmediate(resolve));
 return {file,mode,requests:requests.length,note:node('fnote').textContent,busy:node('auditform').attrs['aria-busy']||false,buttonDisabled:node('auditbtn').disabled};
}
(async()=>{let rows=[];for(const f of files)for(const m of ['absent','accepted','false-body','rate','server','network'])rows.push(await test(f,m));fs.writeFileSync(path.join(root,'docs/form-audit.json'),JSON.stringify(rows,null,2));console.log(JSON.stringify(rows,null,2));})();
