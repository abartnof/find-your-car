import json
import os
import sys

def build_seinfeld():
    batches = [
        "tools/staging/seinfeld_batch1.json",
        "tools/staging/seinfeld_batch2.json",
        "tools/staging/seinfeld_batch3.json",
        "tools/staging/seinfeld_batch4.json",
        "tools/staging/seinfeld_batch5.json",
        "tools/staging/seinfeld_batch6.json"
    ]

    all_questions = []
    seen_q = set()
    longest_correct_count = 0
    ans_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    d_counts = {1: 0, 2: 0, 3: 0}

    for b_idx, b_path in enumerate(batches, 1):
        if not os.path.exists(b_path):
            raise FileNotFoundError(f"Missing batch file: {b_path}")
        with open(b_path, "r", encoding="utf-8") as f:
            b_data = json.load(f)
        if len(b_data) != 100:
            raise ValueError(f"Batch {b_idx} has {len(b_data)} questions; expected exactly 100")

        for q_idx, item in enumerate(b_data):
            q_clean = item["q"].strip().lower()
            if q_clean in seen_q:
                raise ValueError(f"Duplicate question detected in Batch {b_idx} Q{q_idx+1}: {item['q']}")
            seen_q.add(q_clean)

            ans = item["answer"]
            d = item["d"]
            ans_counts[ans] += 1
            d_counts[d] += 1

            lens = [len(o) for o in item["options"]]
            if lens[ans] == max(lens):
                longest_correct_count += 1

            all_questions.append(item)

    total = len(all_questions)
    if total != 600:
        raise ValueError(f"Expected 600 questions, got {total}")

    print(f"Total questions assembled: {total}")
    print(f"Answer counts: {ans_counts}")
    print(f"Difficulty counts: {d_counts}")
    longest_pct = (longest_correct_count / total) * 100
    print(f"Longest correct option: {longest_correct_count}/{total} ({longest_pct:.2f}%)")

    assert ans_counts[0] == 150, f"Expected 150 of answer 0, got {ans_counts[0]}"
    assert ans_counts[1] == 150, f"Expected 150 of answer 1, got {ans_counts[1]}"
    assert ans_counts[2] == 150, f"Expected 150 of answer 2, got {ans_counts[2]}"
    assert ans_counts[3] == 150, f"Expected 150 of answer 3, got {ans_counts[3]}"

    assert d_counts[1] == 180, f"Expected 180 d1, got {d_counts[1]}"
    assert d_counts[2] == 240, f"Expected 240 d2, got {d_counts[2]}"
    assert d_counts[3] == 180, f"Expected 180 d3, got {d_counts[3]}"

    assert longest_pct <= 25.0, f"Longest correct percentage {longest_pct:.2f}% exceeds 25.0%!"

    out_path = "tools/staging/seinfeld_clean.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Successfully generated {out_path} with {total} questions!")
    return out_path

if __name__ == "__main__":
    build_seinfeld()
