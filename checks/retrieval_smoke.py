#!/usr/bin/env python3
"""Bounded navigation check, not a general retrieval-quality benchmark."""
import json,sys
from query import search
cases=[
 ('element rationale','templates/element-rationale.md'),
 ('code connect','integrations/code-connect.md'),
 ('notion research imports','reference-library/notion/README.md'),
 ('reduced motion','workflows/ai-and-motion.md'),
 ('Figma knowledge practice','tools/figma/README.md')
]
results=[]
for query,expected in cases:
 hits=search(query)
 results.append({'query':query,'expected':expected,'found_in_first_eight':expected in [r['path'] for r in hits],'paths':[r['path'] for r in hits]})
print(json.dumps(results,indent=2))
sys.exit(not all(r['found_in_first_eight'] for r in results))
