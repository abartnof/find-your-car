import json
import os
import glob
from collections import Counter

def merge():
    staging_dir = os.path.join(os.path.dirname(__file__), "..", "staging")
    all_questions = []
    seen_q = set()
    duplicates = []

    for b in range(1, 11):
        batch_path = os.path.join(staging_dir, f"billboard_batch_{b}.json")
        if not os.path.exists(batch_path):
            raise FileNotFoundError(f"Batch file not found: {batch_path}")
        with open(batch_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"Loaded batch {b}: {len(data)} questions")
            for item in data:
                q_text = item["q"].strip().lower()
                if q_text in seen_q:
                    duplicates.append((b, item["q"]))
                seen_q.add(q_text)
                all_questions.append(item)

    print(f"\nTotal loaded questions: {len(all_questions)}")
    if duplicates:
        print(f"ERROR: Found {len(duplicates)} duplicate question(s) across batches:")
        for b, q in duplicates:
            print(f"  Batch {b}: {q}")
        return False

    out_file = os.path.join(staging_dir, "billboard_hits_clean.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(all_questions)} questions to {out_file}")

    # Summary
    d_counts = Counter(q["d"] for q in all_questions)
    ans_counts = Counter(q["answer"] for q in all_questions)
    print("\n--- Summary ---")
    print(f"Total: {len(all_questions)}")
    print(f"Answer distribution: 0: {ans_counts[0]}, 1: {ans_counts[1]}, 2: {ans_counts[2]}, 3: {ans_counts[3]}")
    print(f"Difficulty distribution: d1: {d_counts[1]}, d2: {d_counts[2]}, d3: {d_counts[3]}")
    return True

if __name__ == "__main__":
    merge()
