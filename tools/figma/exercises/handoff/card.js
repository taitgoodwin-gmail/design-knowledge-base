const card = document.querySelector('#evidence-card');
const question = document.querySelector('#card-question');
const explanation = document.querySelector('#card-explanation');
const stateLabel = document.querySelector('#card-state');
const toggle = document.querySelector('#source-toggle');
const sources = document.querySelector('#source-list');
const longCopy = document.querySelector('#long-copy');
const showSource = document.querySelector('#show-source');
const appearance = document.querySelector('#appearance');
let state = 'Default';
const copy = {
  Default: 'Updated guidance: open the original source and check its date.',
  Open: 'Review the source before making a visibility claim.',
  Error: 'Simulated source error. Retry to show the example.'
};
function render() {
  card.dataset.state = state;
  stateLabel.textContent = state;
  question.textContent = longCopy.checked
    ? 'Which facts support this recommendation, how recently were they checked, and what uncertainty remains for a team deciding whether to act?'
    : 'What evidence supports this answer?';
  explanation.textContent = copy[state];
  toggle.hidden = !showSource.checked;
  const open = state === 'Open' && showSource.checked;
  toggle.setAttribute('aria-expanded', String(open));
  toggle.textContent = state === 'Error' ? 'Retry source' : open ? 'Hide source' : 'Source [1] available — show source';
  sources.hidden = !open;
  const items = longCopy.checked ? [
    '[3] Another illustrative source.',
    '[1] Example source — inspect the original.',
    '[2] A deliberately long fictional source description that wraps, with collection context and an identifier: EXAMPLE_SOURCE_WITHOUT_SPACES_20260920.'
  ] : ['[1] Example source — inspect the original.'];
  sources.replaceChildren(...items.map(text => {
    const p = document.createElement('p'); p.textContent = text; return p;
  }));
}
toggle.addEventListener('click', () => { state = state === 'Open' ? 'Default' : 'Open'; render(); });
longCopy.addEventListener('change', render);
showSource.addEventListener('change', () => { state = 'Default'; render(); });
appearance.addEventListener('change', () => { document.documentElement.dataset.appearance = appearance.value; });
document.querySelector('#simulate-error').addEventListener('click', () => { state = 'Error'; render(); });
document.querySelector('#reset').addEventListener('click', () => {
  state = 'Default'; longCopy.checked = false; showSource.checked = true;
  appearance.value = 'light'; document.documentElement.dataset.appearance = 'light'; render();
});
render();
