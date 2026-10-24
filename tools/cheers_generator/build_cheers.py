import json
import os
import sys

def merge_batches():
    batch_files = [
        "tools/staging/cheers_batch1.json",
        "tools/staging/cheers_batch2.json",
        "tools/staging/cheers_batch3.json",
        "tools/staging/cheers_batch4.json",
        "tools/staging/cheers_batch5.json"
    ]

    all_questions = []
    seen_q = set()

    for idx, b_path in enumerate(batch_files, 1):
        if not os.path.exists(b_path):
            raise FileNotFoundError(f"Missing batch file: {b_path}")
        with open(b_path, "r", encoding="utf-8") as f:
            b_data = json.load(f)
        if len(b_data) != 100:
            raise ValueError(f"Batch {idx} at {b_path} has {len(b_data)} questions, expected 100")
        
        for q_idx, item in enumerate(b_data):
            q_clean = item["q"].strip().lower()
            if q_clean in seen_q:
                raise ValueError(f"Duplicate question detected in Batch {idx} item {q_idx}: {item['q']}")
            seen_q.add(q_clean)
            all_questions.append(item)

    assert len(all_questions) == 500, f"Expected 500 questions, got {len(all_questions)}"

    # Validate global distributions
    ans_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    d_counts = {1: 0, 2: 0, 3: 0}

    for item in all_questions:
        ans_counts[item["answer"]] += 1
        d_counts[item["d"]] += 1

    print("Global stats for 500 questions:")
    print(f"  Answer distribution: {ans_counts}")
    print(f"  Difficulty distribution: {d_counts}")

    assert ans_counts[0] == 125, f"Expected 125 answer 0, got {ans_counts[0]}"
    assert ans_counts[1] == 125, f"Expected 125 answer 1, got {ans_counts[1]}"
    assert ans_counts[2] == 125, f"Expected 125 answer 2, got {ans_counts[2]}"
    assert ans_counts[3] == 125, f"Expected 125 answer 3, got {ans_counts[3]}"

    assert d_counts[1] == 150, f"Expected 150 d1 (30%), got {d_counts[1]}"
    assert d_counts[2] == 200, f"Expected 200 d2 (40%), got {d_counts[2]}"
    assert d_counts[3] == 150, f"Expected 150 d3 (30%), got {d_counts[3]}"

    out_path = "tools/staging/cheers_clean.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated and wrote 500 clean questions to {out_path}!")

if __name__ == "__main__":
    merge_batches()
