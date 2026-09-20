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
manifest = json.loads((LAB / 'export-manifest.json').read_text())
for name, expected in manifest['files'].items():
    blob = (LAB / name).read_bytes()
    assert len(blob) == expected['bytes'] and hashlib.sha256(blob).hexdigest() == expected['sha256'], name
print(json.dumps({'scope': 'saved observations only; no live Figma or browser rerun', 'card_cases': card_count, 'layout_cases': len(grids), 'font_width_cases': len(fonts), 'guide_control_cases': len(control), 'expected_tool_rejection_preserved': True, 'motion_track_edit_verified': True, 'static_alternative_children': len(static), 'editable_vector_nodes': len(vector['sourceVectors']), 'native_video_bytes': len(video), 'browser_sample_observations': len(observed['samples']), 'passed': True}, indent=2))
