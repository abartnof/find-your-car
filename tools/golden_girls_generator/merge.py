import json
import os
import re
import subprocess
import sys
from collections import Counter

def merge_batches():
    batch_files = [
        "tools/staging/golden_girls_batch1.json",
        "tools/staging/golden_girls_batch2.json",
        "tools/staging/golden_girls_batch3.json",
        "tools/staging/golden_girls_batch4.json",
        "tools/staging/golden_girls_batch5.json"
    ]

    all_questions = []
    seen_q = set()
    duplicates = []

    for b_idx, b_path in enumerate(batch_files, 1):
        if not os.path.exists(b_path):
            raise FileNotFoundError(f"Missing batch file: {b_path}")
        with open(b_path, "r", encoding="utf-8") as f:
            batch_data = json.load(f)
        print(f"Batch {b_idx} loaded: {len(batch_data)} questions.")

        for q_idx, item in enumerate(batch_data):
            q_clean = item["q"].strip().lower()
            if q_clean in seen_q:
                duplicates.append((b_idx, q_idx + 1, item["q"]))
            else:
                seen_q.add(q_clean)
            all_questions.append(item)

    if duplicates:
        print(f"ERROR: Found {len(duplicates)} duplicate question(s) across batches:")
        for b, qn, text in duplicates:
            print(f"  Batch {b} Q{qn}: {text}")
        sys.exit(1)

    total_count = len(all_questions)
    print(f"Total questions merged: {total_count}")

    output_path = "tools/staging/golden_girls_clean.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Wrote merged questions to {output_path}")

    # Validate using validate_quiz.py
    cmd = ["python3", "tools/validate_quiz.py", output_path, "The Golden Girls", "500"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("--- VALIDATION OUTPUT ---")
    print(res.stdout)
    if res.stderr:
        print(res.stderr)

    if res.returncode != 0:
        print("Validation failed!")
        sys.exit(res.returncode)

    # Detailed statistics
    answers = Counter(item["answer"] for item in all_questions)
    diffs = Counter(item["d"] for item in all_questions)

    print("--- DETAILED SUMMARY ---")
    print(f"Total Questions: {total_count}")
    print(f"Answer Distribution:")
    for a in range(4):
        pct = (answers[a] / total_count) * 100
        print(f"  Choice {a}: {answers[a]} ({pct:.1f}%)")
    print(f"Difficulty Distribution:")
    for d in (1, 2, 3):
        pct = (diffs[d] / total_count) * 100
        print(f"  Difficulty {d}: {diffs[d]} ({pct:.1f}%)")

if __name__ == "__main__":
    merge_batches()
