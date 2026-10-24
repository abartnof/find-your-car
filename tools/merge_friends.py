#!/usr/bin/env python3
"""
Merge tools/staging/friends_batch1.json through friends_batch8.json
into tools/staging/friends_clean.json and check for cross-batch duplicates.
"""

import json
import os
import sys

STAGING_DIR = os.path.join(os.path.dirname(__file__), "staging")
OUTPUT_PATH = os.path.join(STAGING_DIR, "friends_clean.json")

all_questions = []
seen_q = set()
duplicates = []

for b in range(1, 9):
    batch_file = os.path.join(STAGING_DIR, f"friends_batch{b}.json")
    if not os.path.exists(batch_file):
        print(f"ERROR: {batch_file} does not exist!")
        sys.exit(1)

    with open(batch_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if len(data) != 100:
        print(f"ERROR: {batch_file} has {len(data)} questions, expected 100")
        sys.exit(1)

    for idx, item in enumerate(data):
        q_norm = item["q"].strip().lower()
        if q_norm in seen_q:
            duplicates.append((b, idx + 1, item["q"]))
        seen_q.add(q_norm)
        all_questions.append(item)

print(f"Total merged questions: {len(all_questions)}")

if duplicates:
    print(f"Found {len(duplicates)} duplicate questions across batches:")
    for b, qnum, q in duplicates:
        print(f"  Batch {b} Q{qnum}: {q}")
    sys.exit(1)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"Saved merged clean file to {OUTPUT_PATH}")
