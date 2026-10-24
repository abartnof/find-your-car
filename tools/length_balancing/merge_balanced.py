#!/usr/bin/env python3
"""
Merge the 4 length-balanced groups back into src/questions.json and verify all metrics.
"""

import json
import os
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
QUESTIONS_PATH = os.path.join(BASE_DIR, "src", "questions.json")
BAL_DIR = os.path.join(BASE_DIR, "tools", "length_balancing")

GROUP_FILES = [
    os.path.join(BAL_DIR, "group1_balanced.json"),
    os.path.join(BAL_DIR, "group2_balanced.json"),
    os.path.join(BAL_DIR, "group3_balanced.json"),
    os.path.join(BAL_DIR, "group4_balanced.json"),
]

def merge_and_verify():
    all_qs = []
    for g_path in GROUP_FILES:
        if not os.path.exists(g_path):
            print(f"WAIT: {g_path} does not exist yet!")
            return False
        qs = json.load(open(g_path))
        print(f"Loaded {len(qs)} questions from {os.path.basename(g_path)}")
        all_qs.extend(qs)

    if len(all_qs) != 16759:
        print(f"ERROR: Expected 16759 questions, got {len(all_qs)}")
        return False

    by_show = defaultdict(lambda: {'total': 0, 'longest_correct': 0})
    total_longest = 0
    errors = []

    for idx, q in enumerate(all_qs):
        opts = q['options']
        if len(opts) != 4 or len(set(opts)) != 4:
            errors.append(f"Q{idx}: invalid options {opts}")
        if q['answer'] not in (0, 1, 2, 3):
            errors.append(f"Q{idx}: invalid answer {q['answer']}")
        if q.get('d') not in (1, 2, 3):
            errors.append(f"Q{idx}: invalid difficulty {q.get('d')}")

        lens = [len(o) for o in opts]
        ans = q['answer']
        show = q['show']
        is_longest = (lens[ans] == max(lens))
        by_show[show]['total'] += 1
        if is_longest:
            by_show[show]['longest_correct'] += 1
            total_longest += 1

    if errors:
        print(f"Validation FAILED with {len(errors)} error(s):")
        for err in errors[:10]:
            print(" ", err)
        return False

    print("\n================== LENGTH BALANCE SUMMARY ==================")
    all_passed = True
    for show, data in sorted(by_show.items()):
        pct = (data['longest_correct'] / data['total']) * 100
        ok = pct <= 25.01
        if not ok:
            all_passed = False
        status = "PASS" if ok else "FAIL (>25%)"
        print(f"  {show:35s}: {data['longest_correct']:4d}/{data['total']:4d} ({pct:5.1f}%) -> {status}")

    global_pct = (total_longest / len(all_qs)) * 100
    print(f"\nGLOBAL LONGEST-IS-CORRECT RATE: {total_longest}/{len(all_qs)} ({global_pct:.1f}%)")

    if not all_passed:
        print("ERROR: Not all shows are <= 25.0%!")
        return False

    with open(QUESTIONS_PATH, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, ensure_ascii=False, indent=0)

    print(f"\nSUCCESS: Saved all {len(all_qs)} length-balanced questions to {QUESTIONS_PATH}")
    return True

if __name__ == "__main__":
    ok = merge_and_verify()
    exit(0 if ok else 1)
