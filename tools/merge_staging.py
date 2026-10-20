#!/usr/bin/env python3 -I
"""Append reviewed staging files (tools/staging/*_clean.json) to src/questions.json (deduped by question text)."""
import json, sys, glob
qs = json.load(open('src/questions.json'))
have = {q['q'] for q in qs}
for f in sorted(sys.argv[1:] or glob.glob('tools/staging/*_clean.json')):
    n = 0
    for c in json.load(open(f)):
        assert len(set(c['options'])) == 4 and 0 <= c['answer'] < 4, c
        if c['q'] in have: continue
        have.add(c['q']); n += 1
        q = {k: c[k] for k in ('show', 'q', 'options', 'answer', 'd') if k in c}
        if c.get('fact'): q['fact'] = c['fact']
        if c.get('section'): q['section'] = c['section']
        qs.append(q)
    print(f, 'added', n)
json.dump(qs, open('src/questions.json', 'w'), ensure_ascii=False, indent=0)
print('total', len(qs))
