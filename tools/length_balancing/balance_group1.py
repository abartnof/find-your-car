#!/usr/bin/env python3
"""
Length-Bias Balancer for Group 1 (Sitcoms & Comedies).
Processes tools/length_balancing/group1.json and outputs tools/length_balancing/group1_balanced.json.
Targets ~21.5% longest-answer-is-correct rate for all shows.
"""

import json
import os
import sys
from natural_enricher import natural_elongate

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(BASE_DIR, "group1.json")
OUTPUT_PATH = os.path.join(BASE_DIR, "group1_balanced.json")

def balance_group1():
    print(f"Loading {INPUT_PATH}...")
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"Loaded {len(data)} questions from group 1.")

    # Group by show
    shows = sorted(list(set(q['show'] for q in data)))
    
    # We will identify candidate questions to modify by their index in the original list
    modified_indices = {}

    for show in shows:
        show_qs = [(idx, q) for idx, q in enumerate(data) if q['show'] == show]
        total_show = len(show_qs)

        # Questions where correct is currently longest or tied for longest
        long_qs = []
        for idx, q in show_qs:
            ans = q['answer']
            lens = [len(o) for o in q['options']]
            if lens[ans] == max(lens):
                wrongs = [len(o) for i, o in enumerate(q['options']) if i != ans]
                diff = lens[ans] - max(wrongs)
                long_qs.append((diff, idx, q))

        # Target ~21.5%
        target_longest = int(total_show * 0.215)
        needed_fix = len(long_qs) - target_longest

        if needed_fix <= 0:
            print(f"[{show}] Already at {len(long_qs)}/{total_show} ({len(long_qs)/total_show*100:.1f}%), no fix needed.")
            continue

        # Sort by length diff ascending (ties first, then smallest diffs)
        long_qs.sort(key=lambda x: x[0])
        candidates = long_qs[:needed_fix]

        print(f"[{show}] Total: {total_show}, Longest: {len(long_qs)} -> Target: {target_longest} (modifying {len(candidates)} questions)")

        for diff, idx, q in candidates:
            ans = q['answer']
            c_text = q['options'][ans]
            c_len = len(c_text)
            wrongs = [(i, o) for i, o in enumerate(q['options']) if i != ans]
            wrongs.sort(key=lambda x: len(x[1]), reverse=True)
            best_idx, best_w = wrongs[0]

            new_w = natural_elongate(best_w, q['q'], c_text)
            
            # Ensure new_w is strictly longer than c_text
            if len(new_w) <= c_len:
                print(f"WARNING: Q{idx} elongation did not exceed correct answer length: {len(new_w)} <= {c_len}")
                new_w = f"{new_w} (verified by complete series broadcast records)"

            new_opts = list(q['options'])
            new_opts[best_idx] = new_w

            # Verify uniqueness
            if len(set(new_opts)) != 4:
                print(f"ERROR: Q{idx} options not unique: {new_opts}")
                sys.exit(1)

            modified_indices[idx] = new_opts

    # Construct balanced questions list
    balanced_data = []
    for idx, q in enumerate(data):
        new_q = dict(q)
        if idx in modified_indices:
            new_q['options'] = modified_indices[idx]
        balanced_data.append(new_q)

    print(f"Saving balanced dataset to {OUTPUT_PATH}...")
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(balanced_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully wrote {len(balanced_data)} questions to {OUTPUT_PATH}.")
    return True

if __name__ == "__main__":
    balance_group1()
