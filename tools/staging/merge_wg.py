#!/usr/bin/env python3
import json
import re
from collections import Counter

batches = []
all_questions = []
seen_q = set()
duplicates = []

for b in range(1, 9):
    batch_file = f"tools/staging/will_and_grace_batch{b}.json"
    with open(batch_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"Batch {b}: {len(data)} questions")
    for idx, item in enumerate(data):
        q = item["q"].strip().lower()
        if q in seen_q:
            duplicates.append((b, idx, item["q"]))
        seen_q.add(q)
        all_questions.append(item)

print(f"Total merged questions: {len(all_questions)}")
print(f"Duplicates across batches: {len(duplicates)}")
if duplicates:
    for dup in duplicates:
        print(f"  Duplicate in Batch {dup[0]}, Q{dup[1]}: {dup[2]}")

# Balance difficulty if needed:
# Target: d1 ~ 30% (240), d2 ~ 40% (320), d3 ~ 30% (240)
diff_counts = Counter(q["d"] for q in all_questions)
print(f"Current difficulty distribution: {diff_counts}")

with open("tools/staging/will_and_grace_clean.json", "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2)

print("Saved to tools/staging/will_and_grace_clean.json")
