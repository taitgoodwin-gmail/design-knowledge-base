#!/usr/bin/env python3
"""Check saved lab measurements; does not claim a live Figma rerun."""
import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / 'tools/figma/evidence/lab'

def result(name):
    raw = json.loads((LAB / name).read_text())
    assert raw.get('isError') is False, name
    return json.loads(next(c['text'] for c in raw['content'] if c['type'] == 'text'))

def close(a, b):
    return abs(a - b) < 0.1

card_count = 0
for width in (320, 390, 768, 1440):
    cases = result(f'02-e02-{width}.json')['cases']
    assert {(c['length'], c['open']) for c in cases} == {(n, o) for n in ('short', 'long') for o in (False, True)}
    for c in cases:
        assert c['width'] == width and not c['violations']
        assert len(c['children']) == (5 if c['open'] else 4)
        for i, child in enumerate(c['children']):
            assert child['x'] >= 24 and child['x'] + child['width'] <= width - 24 + .1
            assert child['y'] + child['height'] <= c['card']['height'] - 24 + .1
            if i:
                prev = c['children'][i-1]
                assert child['y'] >= prev['y'] + prev['height'] + 16 - .1
        assert next(n for n in c['children'] if n['name'] == 'Source button')['height'] >= 48
        card_count += 1
    for length in ('short', 'long'):
        closed = next(c for c in cases if c['length'] == length and not c['open'])
        opened = next(c for c in cases if c['length'] == length and c['open'])
        disclosure = next(n for n in opened['children'] if n['name'] == 'Disclosure')
        assert close(opened['children'][-1]['y'] - closed['children'][-1]['y'], disclosure['height'] + 16)

grids = result('06-e03-resize.json')['results']
assert len(grids) == 9
for width, first_row in ((390, 2), (600, 3), (840, 4)):
    wrap = next(c for c in grids if c['mode'] == 'HORIZONTAL' and c['width'] == width)
    assert sum(close(c['y'], 24) for c in wrap['children']) == first_row
    grid = next(c for c in grids if c['mode'] == 'GRID' and c['width'] == width)
    assert len(grid['tracks']) == 3
    for c in grid['children']:
        assert close(c['width'], (width - 48 - 32) / 3)
span = result('07-e03-span.json')
assert span['tracks'][0] == {'type': 'FIXED', 'value': 120}
assert span['children'][0]['columnSpan'] == 2 and close(span['children'][0]['width'], 336)

fonts = result('09-e07-width-fonts.json')['cases']
assert {(c['family'], c['width']) for c in fonts} == {(f, w) for f in ('Inter', 'Noto Sans') for w in (320, 390, 768)}
for c in fonts:
    assert not c['violations'] and len(c['children']) == 4
    for t in c['children']:
        assert not t['hasMissingFont'] and t['textAutoResize'] == 'HEIGHT'
        assert t['characters']
states = {s['mode']: s for s in result('10-e07-resizing-modes.json')['states']}
assert states['auto-width']['width'] > states['auto-width']['containerWidth']
assert states['restored-auto-height']['height'] > states['fixed-small-box']['height']

control = result('12-e18-guide-control.json')['runs']
assert control[0]['guide'] == 'NONE' and control[1]['guide'] == 'STRETCH'
assert [n['x'] for n in control[0]['after'][:3]] == [24, 200, 376]
assert [n['x'] for n in control[1]['after'][:3]] == [24, 130, 306]
failure = json.loads((LAB / '11-e18-guide-refresh.json').read_text())
assert failure['isError'] and 'sectionSize' in failure['content'][0]['text']
linear = result('22-e09-linear.json')['tracks']['OPACITY']
eased = result('23-e09-ease-out.json')['tracks']['OPACITY']
assert linear['id'] == eased['id']
assert [k['id'] for k in linear['keyframes']] == [k['id'] for k in eased['keyframes']]
assert linear['keyframes'][-1]['easing']['type'] == 'LINEAR'
assert eased['keyframes'][-1]['easing']['type'] == 'EASE_OUT'
assert [(k['timelinePosition'], k['value']['value']) for k in eased['keyframes']] == [(0, 0), (.6, 1)]
static = result('24-e09-static.json')['children']
assert len(static) == 6 and all(not n['tracks'] and not n['styles'] and n['opacity'] == 1 for n in static)
vector = result('19-e10-export.json')
assert len(vector['sourceVectors']) == 3 and all(n['paths'] for n in vector['sourceVectors'])
assert '<filter' in vector['svg'] and '<svg' in vector['svg']
assert close(vector['sourceVectors'][1]['rotation'], 8)
for item in vector['bounds']:
    b = item['bounds']
    assert b['x'] >= 600 and b['y'] >= 1700 and b['x'] + b['width'] <= 1100 and b['y'] + b['height'] <= 2000
video = (LAB / 'e09-native-reveal.mp4').read_bytes()
assert len(video) > 1000 and b'ftyp' in video[:40]
observed = json.loads((LAB / '26-e09-browser-observation.json').read_text())
assert [s['seconds'] for s in observed['samples']] == [0, .2, .6, 1.8]
before = result('43-e04-before-main-update.json')['instances']
after = result('44-e04-after-main-update.json')['after']
assert after[0]['properties']['Question#57:10']['value'] == before[0]['properties']['Question#57:10']['value']
assert after[1]['properties']['Question#57:10']['value'] != before[1]['properties']['Question#57:10']['value']
assert after[0]['properties']['Show source#57:11']['value'] is False
for instance in after:
    assert next(n['text'] for n in instance['children'] if n['name'] == 'Explanation').startswith('Updated guidance:')
slot_cases = result('46-e05-state-switches.json')['cases']
assert [c['state'] for c in slot_cases] == ['Error', 'Default', 'Open']
for case in slot_cases:
    assert case['type'] == 'INSTANCE' and not case['slot']['limits']
    assert [n['name'] for n in case['slot']['children']] == ['Source 3', 'Source 1', 'Source 2']
    assert case['slot']['visible'] == (case['state'] == 'Open')
for path in ['47-e06-boolean-binding.json', '52-e06-variant-binding.json']:
    binding = result(path)
    assert binding['events'][0]['accepted']
    assert [(c['mode'], c['resolved']['value'], c['source']['visible']) for c in binding['cases']] == [('Light', True, True), ('Dark', False, False)]
audit = result('54-component-final-compact.json')
assert len(audit['records']) == 9 and not audit['issues']
for root in audit['records']:
    assert not root['missingFonts'] and not root['unboundTextFills']
    assert {'fills','paddingLeft','paddingRight','paddingTop','paddingBottom','itemSpacing','topLeftRadius','topRightRadius','bottomLeftRadius','bottomRightRadius'} <= set(root['bindings'])
contrast = json.loads((LAB / '56-component-contrast.json').read_text())
assert len(contrast['pairs']) == 6 and all(p['ratio'] >= 4.5 for p in contrast['pairs'])
original = result('17-original-page-check.json')['children']
preserved = result('70-original-after-prototype.json')['topLevel']
keys = ('id', 'name', 'x', 'y', 'width', 'height')
assert [{k: n[k] for k in keys} for n in original] == [{k: n[k] for k in keys} for n in preserved]
prototype = result('66-prototype-final-audit.json')
assert len(prototype['records']) == 3 and not prototype['issues']
assert prototype['flows'] == [{'nodeId': '63:9', 'name': 'E08 / Source disclosure'}]
assert all(not f['missingFonts'] and f['width'] == 390 and f['height'] == 640 for f in prototype['records'])
assert all(n['name'] not in ('Back button', 'Restart button') for n in prototype['records'][0]['visibleChildren'])
for f in prototype['records']:
    for n in f['reactions']:
        for reaction in n['reactions']:
            for action in reaction['actions']:
                if action['type'] == 'NODE':
                    assert action['destinationId'] != f['id']
                    if action['transition']:
                        assert close(action['transition']['duration'], .2)
                        assert action['transition']['easing']['type'] == 'EASE_OUT'
rejected = json.loads((LAB / '60-prototype-navigation.json').read_text())
assert rejected['isError'] and 'different top-level frame' in rejected['content'][0]['text']
handoff = json.loads((LAB / 'e12-browser-observations.json').read_text())
assert (handoff['reference']['width'], handoff['reference']['height']) == (360, 204)
assert handoff['reference']['font_loaded'] and handoff['interactive_default']['height'] == 224
assert [(k['key'], k['expanded'], k['focus']) for k in handoff['keyboard']] == [('Enter', True, 'source-toggle'), ('Space', False, 'source-toggle')]
assert [c['viewport'] for c in handoff['width_cases']] == [320, 390, 768, 1440]
for c in handoff['width_cases']:
    assert not c['violations'] and c['page_width'] == c['viewport']
    assert c['source_width'] == c['source_scroll_width']
    assert c['source_order'] == ['[3]', '[1]', '[2]'] and c['button_height'] >= 44
    assert close(c['following_top'] - c['card_bottom'], 16)
assert handoff['reset']['state'] == 'Default' and not handoff['reset']['expanded']
font_dir = ROOT / 'tools/figma/exercises/handoff/assets'
font_record = json.loads((font_dir / 'provenance.json').read_text())
font_bytes = (font_dir / 'Inter-Regular.woff2').read_bytes()
assert len(font_bytes) == font_record['bytes'] and hashlib.sha256(font_bytes).hexdigest() == font_record['font_sha256']
manifest = json.loads((LAB / 'export-manifest.json').read_text())
for name, expected in manifest['files'].items():
    blob = (LAB / name).read_bytes()
    assert len(blob) == expected['bytes'] and hashlib.sha256(blob).hexdigest() == expected['sha256'], name
print(json.dumps({'scope': 'saved observations only; no live Figma or browser rerun', 'card_cases': card_count, 'layout_cases': len(grids), 'font_width_cases': len(fonts), 'guide_control_cases': len(control), 'expected_tool_rejection_preserved': True, 'motion_track_edit_verified': True, 'static_alternative_children': len(static), 'editable_vector_nodes': len(vector['sourceVectors']), 'native_video_bytes': len(video), 'browser_sample_observations': len(observed['samples']), 'component_roots_checked': len(audit['records']), 'slot_state_switches': len(slot_cases), 'boolean_binding_routes': 2, 'contrast_pairs': len(contrast['pairs']), 'prototype_frames': len(prototype['records']), 'handoff_width_cases': len(handoff['width_cases']), 'handoff_keyboard_cases': len(handoff['keyboard']), 'original_top_level_nodes_preserved': len(original), 'passed': True}, indent=2))
