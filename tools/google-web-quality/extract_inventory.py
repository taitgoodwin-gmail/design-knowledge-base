import argparse
import json
import re
from collections import Counter
from pathlib import Path

parser = argparse.ArgumentParser(description='Extract the pinned Lighthouse 13.5.0 default audit inventory')
parser.add_argument('--source', type=Path, required=True, help='Local checkout of Lighthouse 13.5.0')
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
repo = args.source.resolve()
out = args.output.resolve()
out.mkdir(parents=True, exist_ok=True)
config_path = 'core/config/default-config.js'
config = (repo / config_path).read_text()
commit = 'cb853a38a6410617518b363590c967b3fe211949'
base = f'https://github.com/GoogleChrome/lighthouse/blob/{commit}/'
categories_text = config.split('  categories: {', 1)[1]
markers = list(re.finditer(r"^    '([^']+)': \{", categories_text, re.M))
source_files = list((repo / 'core/audits').rglob('*.js'))
rows = []
for i, marker in enumerate(markers):
    category = marker.group(1)
    block = categories_text[marker.end():markers[i + 1].start() if i + 1 < len(markers) else len(categories_text)]
    for match in re.finditer(r"\{id: '([^']+)', weight: ([^,}]+)([^}]*)\}", block):
        audit_id, weight_expr, rest = match.groups()
        candidates = [p for p in source_files if p.stem == audit_id]
        if not candidates:
            candidates = [p for p in source_files if re.search(r"\bid:\s*'" + re.escape(audit_id) + "'", p.read_text())]
        assert len(candidates) == 1, (audit_id, candidates)
        source = candidates[0].relative_to(repo).as_posix()
        group = re.search(r"group: '([^']+)'", rest)
        weight_parts = [float(x.strip()) for x in weight_expr.split('/')]
        weight = weight_parts[0] if len(weight_parts) == 1 else weight_parts[0] / weight_parts[1]
        manual = '/manual/' in source
        rows.append(dict(category=category, audit_id=audit_id, configured_weight_expression=weight_expr.strip(), configured_weight=weight,
                         group=group.group(1) if group else None,
                         role='manual review' if manual else ('weighted reference' if weight > 0 else 'unscored reference'),
                         source_path=source, source_url=base + source))

counts = Counter(r['category'] for r in rows)
unique_count = len({r['audit_id'] for r in rows})
inventory = dict(checked_date='2026-09-23', lighthouse_version='13.5.0', source_commit=commit,
    method='Static extraction of every auditRef in default-config.js; each ID resolved to an existing audit source file. Not runtime audit results.',
    scope_note='References can be shared by categories and include manual, hidden, informative and mode-dependent checks. Counts do not represent independent failures or checks run on a page. Configured weights are not normalized runtime weights.',
    source_url=base+config_path, category_reference_counts=dict(counts), reference_count=len(rows), unique_audit_id_count=unique_count, references=rows)
(out / 'lighthouse-audit-inventory.json').write_text(json.dumps(inventory, indent=2) + '\n')
lines = ['# Lighthouse 13.5.0 audit inventory', '', 'Checked: 23 September 2026.', '',
    f'Extracted **{len(rows)} category references covering {unique_count} unique audit IDs** from the [pinned default configuration]({base}{config_path}). Each audit ID was resolved to a source file. This is a source inventory, not website test results.', '',
    'Weights below are configured inputs, not final percentages. Runtime mode, applicability and errors affect inclusion and scoring. Zero weight does not mean unimportant. Shared checks must not be counted twice as customer issues. Experimental agentic checks require separate interpretation.', '',
    '| Category | References |', '| --- | ---: |']
lines += [f'| {cat} | {n} |' for cat,n in counts.items()]
for category in counts:
    lines += ['', f'## {category}', '', '| Audit ID and implementation | Configured weight | Group | Role |', '| --- | ---: | --- | --- |']
    for r in rows:
        if r['category'] == category:
            lines.append(f"| [{r['audit_id']}]({r['source_url']}) | {r['configured_weight_expression']} | {r['group'] or '—'} | {r['role']} |")
lines += ['', '## Verification', '', f"Source commit: `{commit}`. Extraction asserted that every reference maps to exactly one audit source file. JSON contains the same records for future import. Titles, availability and results should be taken from each actual Lighthouse report; this inventory must be regenerated after version upgrades.", '']
(out / 'lighthouse-audit-inventory.md').write_text('\n'.join(lines))
print(json.dumps({k: inventory[k] for k in ['category_reference_counts', 'reference_count', 'unique_audit_id_count']}, indent=2))
