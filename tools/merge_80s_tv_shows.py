import json
import os
import sys

def merge_batches():
    merged = []
    seen_questions = set()
    errors = []

    for i in range(1, 11):
        batch_path = f"tools/staging/80s_tv_shows_batch{i}.json"
        if not os.path.exists(batch_path):
            print(f"ERROR: {batch_path} not found!")
            sys.exit(1)

        with open(batch_path, "r", encoding="utf-8") as f:
            batch_data = json.load(f)

        print(f"Batch {i}: {len(batch_data)} questions")
        for q_obj in batch_data:
            q_text = q_obj["q"].strip().lower()
            if q_text in seen_questions:
                errors.append(f"Duplicate question across batches: '{q_obj['q']}'")
            seen_questions.add(q_text)
            merged.append(q_obj)

    print(f"Total merged questions: {len(merged)}")
    if errors:
        print(f"Found {len(errors)} cross-batch error(s):")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    clean_path = "tools/staging/80s_tv_shows_clean.json"
    with open(clean_path, "w", encoding="utf-8") as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)

    print(f"Successfully wrote {clean_path}")

if __name__ == "__main__":
    merge_batches()
