#!/usr/bin/env python3 -I
"""Parse raw trivia dumps into a staging JSON for review (not merged into the game yet).
usage: stage_dump.py out.json "Show" dump1.txt [dump2.txt ...]
Handles '==== SECTION' headers, 'N. question', 'A) option' lines; answers from either an inline
'ANSWER: X) ...' line (+ optional 'DID YOU KNOW? ...' -> fact) or an '==== KEY' block ('N-X' or 'N. X')."""
import json, re, sys
out, show, files = sys.argv[1], sys.argv[2], sys.argv[3:]
qs = []
for f in files:
    text = open(f).read()
    body, _, key = text.partition('==== KEY')
    ans = {int(n): 'ABCD'.index(l) for n, l in re.findall(r'(\d+)\s*[-.]\s*([A-D])\b', key)}
    section, cur = '', None
    for line in body.splitlines():
        if m := re.match(r'==== (.+)', line): section = m.group(1).strip(); continue
        if m := re.match(r'(\d+)\. (.+)', line):
            cur = {'show': show, 'section': section, 'n': int(m.group(1)), 'q': m.group(2).strip(), 'options': []}; qs.append(cur); continue
        if not cur: continue
        if m := re.match(r'\s+([A-D])\) (.+)', line): cur['options'].append(m.group(2).strip())
        elif m := re.match(r'\s+ANSWER: ([A-D])\)', line): cur['answer'] = 'ABCD'.index(m.group(1))
        elif m := re.match(r'\s+DID YOU KNOW\? (.+)', line): cur['fact'] = m.group(1).strip()
    for c in qs:
        if 'answer' not in c and c['n'] in ans and c['section'] is not None and c.get('_f') is None: pass
    # key-based answers (per file, numbers restart in each file)
    if ans:
        for c in qs:
            if c.get('_file') is None and 'answer' not in c: c['answer'] = ans.get(c['n'], None)
    for c in qs: c.setdefault('_file', f)
for c in qs:
    c.pop('_file', None); c.pop('_f', None)
    assert len(c['options']) == 4 and c.get('answer') is not None, c
json.dump(qs, open(out, 'w'), ensure_ascii=False, indent=1)
print(out, len(qs))
