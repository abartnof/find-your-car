#!/usr/bin/env python3
"""
Validator for quiz question json files.
Usage: python3 tools/validate_quiz.py <path_to_json> <expected_show> <expected_count>
"""

import sys
import json
import re
from collections import Counter

def validate(path, expected_show, expected_count):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, list):
        print(f"ERROR: Root is not a list in {path}")
        return False

    actual_count = len(data)
    print(f"Validating {path}: found {actual_count} questions (expected {expected_count})...")

    errors = []
    seen_q = set()
    answers = Counter()
    difficulties = Counter()

    for idx, item in enumerate(data):
        q_num = idx + 1
        if not isinstance(item, dict):
            errors.append(f"Q{q_num}: Not a dict")
            continue

        show = item.get("show")
        if show != expected_show:
            errors.append(f"Q{q_num}: show '{show}' does not match expected '{expected_show}'")

        q = item.get("q")
        if not isinstance(q, str) or not q.strip():
            errors.append(f"Q{q_num}: empty question text")
        else:
            q_clean = q.strip().lower()
            if q_clean in seen_q:
                errors.append(f"Q{q_num}: duplicate question text: {q[:60]}...")
            seen_q.add(q_clean)
            if re.match(r"^\d+[\.\)]\s*", q.strip()):
                errors.append(f"Q{q_num}: question text starts with number prefix: {q[:30]}")

        opts = item.get("options")
        if not isinstance(opts, list) or len(opts) != 4:
            errors.append(f"Q{q_num}: does not have exactly 4 options: {opts}")
        else:
            for opt_idx, opt in enumerate(opts):
                if not isinstance(opt, str) or not opt.strip():
                    errors.append(f"Q{q_num} opt{opt_idx}: empty option text")
                elif re.match(r"^[A-D][\.\)]\s*", opt.strip()):
                    errors.append(f"Q{q_num} opt{opt_idx}: option starts with letter prefix: {opt}")
            if len(set(opt.strip().lower() for opt in opts if isinstance(opt, str))) != 4:
                errors.append(f"Q{q_num}: duplicate options in {opts}")

        ans = item.get("answer")
        if not isinstance(ans, int) or ans not in (0, 1, 2, 3):
            errors.append(f"Q{q_num}: invalid answer index: {ans}")
        else:
            answers[ans] += 1

        d = item.get("d")
        if not isinstance(d, int) or d not in (1, 2, 3):
            errors.append(f"Q{q_num}: invalid difficulty d: {d}")
        else:
            difficulties[d] += 1

        if len(errors) >= 30:
            errors.append("Too many errors, stopping check early.")
            break

    if actual_count < expected_count:
        errors.append(f"Question count {actual_count} is less than target {expected_count}")

    if errors:
        print(f"FAILED validation with {len(errors)} error(s):")
        for err in errors[:25]:
            print(f"  - {err}")
        return False

    print("SUCCESS: File validated successfully!")
    print(f"  Total questions: {actual_count}")
    print(f"  Answer distribution: 0: {answers[0]} ({answers[0]/actual_count*100:.1f}%), 1: {answers[1]} ({answers[1]/actual_count*100:.1f}%), 2: {answers[2]} ({answers[2]/actual_count*100:.1f}%), 3: {answers[3]} ({answers[3]/actual_count*100:.1f}%)")
    print(f"  Difficulty distribution: d1: {difficulties[1]}, d2: {difficulties[2]}, d3: {difficulties[3]}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 tools/validate_quiz.py <path> <expected_show> <expected_count>")
        sys.exit(1)
    ok = validate(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    sys.exit(0 if ok else 1)
