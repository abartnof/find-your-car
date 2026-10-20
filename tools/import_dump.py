#!/usr/bin/env python3 -I
"""Merge a pasted trivia dump (see tools/dumps/*.txt) into src/questions.json.
Format: '==== LABEL' section headers, 'N. question' + 'A) ..' lines, then '==== KEY' with 'N. X' pairs.
usage: import_dump.py dump.txt "Show prefix" [--skip 44,45] [--easy 3,4] [--hard 1,5]"""
import json, re, sys, random
a = sys.argv[1:]
path, prefix = a[0], a[1]
def lst(flag):
    return {int(x) for x in a[a.index(flag) + 1].split(',')} if flag in a else set()
skip, easy, hard = lst('--skip'), lst('--easy'), lst('--hard')
text = open(path).read()
body, key = text.split('==== KEY')
ans = {int(n): 'ABCD'.index(l) for n, l in re.findall(r'(\d+)\.\s*([A-D])', key)}
out, label, cur = [], '', None
for line in body.splitlines():
    m = re.match(r'==== (.+)', line)
    if m: label = m.group(1).title().replace('S', 's') if False else m.group(1).lower(); continue
    m = re.match(r'(\d+)\. (.+)', line)
    if m: cur = {'n': int(m.group(1)), 'q': m.group(2).strip(), 'o': [], 'era': label}; out.append(cur); continue
    m = re.match(r'\s+([A-D])\) (.+)', line)
    if m and cur: cur['o'].append(m.group(2).strip())
random.seed(5)
qs = json.load(open('src/questions.json'))
have = {q['q'] for q in qs}
added = 0
for c in out:
    if c['n'] in skip or c['q'] in have: continue
    assert len(c['o']) == 4 and c['n'] in ans, c
    opts = c['o']; right = opts[ans[c['n']]]
    random.shuffle(opts)
    qs.append({'show': f"{prefix} · {c['era']}", 'q': c['q'], 'options': opts, 'answer': opts.index(right),
               'd': 1 if c['n'] in easy else 3 if c['n'] in hard else 2})
    added += 1
json.dump(qs, open('src/questions.json', 'w'), ensure_ascii=False, indent=0)
print('added', added, 'total', len(qs))
