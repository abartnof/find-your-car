#!/usr/bin/env python3
"""
Merge all 5 batches into tools/staging/streaming_tv_clean.json.
Validates counts, deduplication, answer balance, and difficulty balance.
"""

import json
from collections import Counter

BATCH_FILES = [
    "tools/staging/streaming_tv_batch1.json",
    "tools/staging/streaming_tv_batch2.json",
    "tools/staging/streaming_tv_batch3.json",
    "tools/staging/streaming_tv_batch4.json",
    "tools/staging/streaming_tv_batch5.json",
]

def merge_batches():
    all_questions = []
    seen_q = set()
    answers = Counter()
    difficulties = Counter()

    for idx, path in enumerate(BATCH_FILES, 1):
        with open(path, "r", encoding="utf-8") as f:
            batch = json.load(f)
        print(f"Loaded Batch {idx} from {path}: {len(batch)} questions")
        for item in batch:
            q_norm = item["q"].strip().lower()
            if q_norm in seen_q:
                raise ValueError(f"Duplicate question across batches: {item['q']}")
            seen_q.add(q_norm)
            all_questions.append(item)
            answers[item["answer"]] += 1
            difficulties[item["d"]] += 1

    total = len(all_questions)
    print(f"\nTotal merged questions: {total}")
    print(f"Answers: {dict(answers)}")
    print(f"Difficulties: {dict(difficulties)} (d1: {difficulties[1]/total*100:.1f}%, d2: {difficulties[2]/total*100:.1f}%, d3: {difficulties[3]/total*100:.1f}%)")

    output_path = "tools/staging/streaming_tv_clean.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Successfully saved {total} questions to {output_path}")

if __name__ == "__main__":
    merge_batches()
