#!/usr/bin/env python3
"""
Merge all 5 produce batches into tools/staging/produce_clean.json
and verify uniqueness and schema compliance.
"""

import json
import os
import sys

def merge():
    batches = []
    for i in range(1, 6):
        batch_path = f"tools/staging/produce_batch{i}.json"
        if not os.path.exists(batch_path):
            raise FileNotFoundError(f"Missing batch file: {batch_path}")
        with open(batch_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"Loaded {len(data)} questions from {batch_path}")
            batches.append(data)

    all_questions = []
    seen_q = set()

    for batch_idx, batch in enumerate(batches, 1):
        for q_idx, item in enumerate(batch, 1):
            q_clean = item["q"].strip().lower()
            if q_clean in seen_q:
                raise ValueError(f"Duplicate question detected in batch {batch_idx}, Q{q_idx}: {item['q']}")
            seen_q.add(q_clean)
            all_questions.append({
                "show": "Fruits & Veggies",
                "q": item["q"].strip(),
                "options": item["options"],
                "answer": item["answer"],
                "d": item["d"]
            })

    output_path = "tools/staging/produce_clean.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\nSuccessfully wrote {len(all_questions)} merged questions to {output_path}")

if __name__ == "__main__":
    merge()
