#!/usr/bin/env python3
import sys
import json
from collections import defaultdict

def validate_group(original_path, balanced_path):
    orig = json.load(open(original_path))
    bal = json.load(open(balanced_path))

    if len(orig) != len(bal):
        print(f"ERROR: Count mismatch: original={len(orig)}, balanced={len(bal)}")
        return False

    by_show = defaultdict(lambda: {'total': 0, 'longest_correct': 0})
    errors = []

    for idx, (q_orig, q_bal) in enumerate(zip(orig, bal)):
        if q_orig['q'] != q_bal['q']:
            errors.append(f"Q{idx}: Question text changed: {q_orig['q'][:40]} != {q_bal['q'][:40]}")
        if q_orig['show'] != q_bal['show']:
            errors.append(f"Q{idx}: Show changed")
        if q_orig['answer'] != q_bal['answer']:
            errors.append(f"Q{idx}: Answer index changed from {q_orig['answer']} to {q_bal['answer']}")
        
        # Verify correct answer text hasn't changed meaningfully
        orig_ans_text = q_orig['options'][q_orig['answer']].strip().lower()
        bal_ans_text = q_bal['options'][q_bal['answer']].strip().lower()
        if orig_ans_text != bal_ans_text and orig_ans_text not in bal_ans_text and bal_ans_text not in orig_ans_text:
            errors.append(f"Q{idx}: Correct answer content changed from '{q_orig['options'][q_orig['answer']]}' to '{q_bal['options'][q_bal['answer']]}'")

        opts = q_bal['options']
        if len(opts) != 4 or len(set(opts)) != 4:
            errors.append(f"Q{idx}: Options not 4 unique items: {opts}")

        # Check lengths
        lens = [len(o) for o in opts]
        ans = q_bal['answer']
        is_longest = (lens[ans] == max(lens))
        show = q_bal['show']
        by_show[show]['total'] += 1
        if is_longest:
            by_show[show]['longest_correct'] += 1

    if errors:
        print(f"Validation FAILED with {len(errors)} error(s):")
        for err in errors[:20]:
            print(" ", err)
        return False

    print("--- Length Balance Check per Show ---")
    all_ok = True
    for show, data in sorted(by_show.items()):
        pct = (data['longest_correct'] / data['total']) * 100
        status = "PASS" if pct <= 25.01 else "FAIL (>25%)"
        if pct > 25.01:
            all_ok = False
        print(f"  {show:35s}: {data['longest_correct']}/{data['total']} ({pct:.1f}%) -> {status}")

    if not all_ok:
        print("\nERROR: One or more shows still have longest_correct > 25.0%")
        return False

    print("\nSUCCESS: All shows passed length balance check (longest answer correct <= 25.0%)!")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 tools/length_balancing/validate_group.py <original.json> <balanced.json>")
        sys.exit(1)
    ok = validate_group(sys.argv[1], sys.argv[2])
    sys.exit(0 if ok else 1)
