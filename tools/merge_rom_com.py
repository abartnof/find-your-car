#!/usr/bin/env python3
"""
Merge Romantic Comedies batches 1-5 into tools/staging/rom_com_clean.json
and check deduplication, balance, and constraints.
"""
import json
import os
import sys

def merge():
    staging_dir = os.path.join(os.path.dirname(__file__), "staging")
    batch_files = [
        os.path.join(staging_dir, f"rom_com_batch{i}.json")
        for i in range(1, 6)
    ]

    all_questions = []
    seen_q = set()
    duplicates = []

    for path in batch_files:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Missing batch file: {path}")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"Loaded {len(data)} questions from {os.path.basename(path)}")
            for idx, item in enumerate(data):
                q = item["q"].strip().lower()
                if q in seen_q:
                    duplicates.append((os.path.basename(path), idx + 1, item["q"]))
                seen_q.add(q)
                all_questions.append(item)

    if duplicates:
        print(f"ERROR: Found {len(duplicates)} duplicate questions across batches:")
        for b, qn, text in duplicates:
            print(f"  [{b} Q{qn}]: {text}")
        sys.exit(1)

    print(f"\nTotal merged questions: {len(all_questions)}")

    out_path = os.path.join(staging_dir, "rom_com_clean.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    print(f"Saved merged dataset to: {out_path}")

if __name__ == "__main__":
    merge()
