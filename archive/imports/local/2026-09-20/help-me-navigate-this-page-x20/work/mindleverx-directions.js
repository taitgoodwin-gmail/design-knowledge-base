
(() => {
 const root=document.getElementById('mlx-directions');
 const site=root.querySelector('.mlx-site');
 const state={direction:'signal',atmosphere:true,accent:'#dafe77'};
 const titles={signal:'Your next<br>customer<br>is asking AI.',human:'Be part of<br>the answer.',proof:'Make your<br>evidence<br>stand out.'};
 const questions={signal:'Will it mention you?',human:'Visibility begins with understanding.',proof:'Make the next move count.'};
 function render(){site.dataset.look=state.direction;site.classList.toggle('no-atmosphere',!state.atmosphere);root.style.setProperty('--mlx-accent',state.accent);root.querySelector('h1').innerHTML=titles[state.direction];root.querySelector('.mlx-question').textContent=questions[state.direction];root.querySelectorAll('[data-direction]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.direction===state.direction)));}
 function restore(saved){const v=saved?.modelContent;if(v&&titles[v.direction])state.direction=v.direction;render();}
 function save(){if(window.openai?.setWidgetState)window.openai.setWidgetState({modelContent:{direction:state.direction},privateContent:{atmosphere:state.atmosphere}}).catch(()=>{});}
 root.querySelectorAll('[data-direction]').forEach(b=>b.addEventListener('click',()=>{state.direction=b.dataset.direction;render();save();}));
 const citation=root.querySelector('.mlx-citation');citation.addEventListener('click',()=>{const source=root.querySelector('.mlx-source');source.hidden=!source.hidden;citation.setAttribute('aria-expanded',String(!source.hidden));});
 restore(window.openai?.widgetState);window.addEventListener('openai:set_globals',e=>{if(e.detail?.globals?.widgetState)restore(e.detail.globals.widgetState);});
 if(globalThis.Tweak){const tweak=new Tweak({container:site,onChange:render});tweak.addToggle(state,'atmosphere',{label:'Atmospheric graphic'});tweak.addColorPicker(state,'accent',{label:'Signal accent',reference:'--mlx-accent'});}
})();
