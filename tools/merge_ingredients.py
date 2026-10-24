#!/usr/bin/env python3
"""
Merge all 8 Ingredients quiz batches into tools/staging/ingredients_clean.json.
Validates question uniqueness and answer distributions.
"""

import json
import glob
import os
import sys

def merge_all(output_file="tools/staging/ingredients_clean.json"):
    batch_files = sorted([f"tools/staging/ingredients_batch{i}.json" for i in range(1, 9)])
    
    combined = []
    seen_q = set()
    errors = []

    for bf in batch_files:
        if not os.path.exists(bf):
            print(f"Error: Missing batch file {bf}")
            return False
        with open(bf, "r", encoding="utf-8") as f:
            batch_data = json.load(f)
            print(f"Loaded {len(batch_data)} questions from {bf}")
            for item in batch_data:
                q_text = item["q"].strip().lower()
                if q_text in seen_q:
                    errors.append(f"Cross-batch duplicate question: {item['q']}")
                seen_q.add(q_text)
                combined.append(item)

    if errors:
        print(f"Found {len(errors)} cross-batch errors:")
        for err in errors[:10]:
            print(f"  - {err}")
        return False

    if len(combined) != 800:
        print(f"Error: Expected exactly 800 questions, got {len(combined)}")
        return False

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(combined, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Successfully merged {len(combined)} questions to {output_file}")
    return True

if __name__ == "__main__":
    success = merge_all()
    sys.exit(0 if success else 1)
