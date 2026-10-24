#!/usr/bin/env python3
"""
Merge all 8 SNL quiz batches into tools/staging/snl_clean.json and check for cross-batch duplicates.
"""

import json
import os
import sys

def merge():
    staging_dir = os.path.join(os.path.dirname(__file__), "..", "staging")
    all_questions = []
    seen_q = {}

    for b in range(1, 9):
        batch_file = os.path.join(staging_dir, f"snl_batch{b}.json")
        if not os.path.exists(batch_file):
            print(f"Error: {batch_file} does not exist!")
            sys.exit(1)
        with open(batch_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"Loaded Batch {b}: {len(data)} questions")
            for idx, item in enumerate(data):
                q_text = item["q"].strip().lower()
                if q_text in seen_q:
                    prev_batch, prev_idx = seen_q[q_text]
                    print(f"ERROR: Duplicate question across batches!")
                    print(f"  Batch {prev_batch} Q{prev_idx+1} and Batch {b} Q{idx+1}")
                    print(f"  Question: {item['q']}")
                    sys.exit(1)
                seen_q[q_text] = (b, idx)
                all_questions.append(item)

    print(f"Total merged questions: {len(all_questions)}")
    if len(all_questions) != 800:
        print(f"ERROR: Expected 800 questions, got {len(all_questions)}")
        sys.exit(1)

    out_file = os.path.join(staging_dir, "snl_clean.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(all_questions)} questions to {out_file}")

if __name__ == "__main__":
    merge()
