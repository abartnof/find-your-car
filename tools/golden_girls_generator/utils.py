import json
import os
import re
import sys

def build_golden_girls_batch(raw_questions, batch_num, output_path):
    expected_count = len(raw_questions)
    if expected_count != 100:
        raise ValueError(f"Batch {batch_num} has {expected_count} questions; expected exactly 100")

    formatted = []
    seen_q = set()

    for idx, item in enumerate(raw_questions):
        q = item["q"].strip()
        correct = item["correct"].strip()
        wrong = [w.strip() for w in item["wrong"]]
        d = item["d"]

        if not q:
            raise ValueError(f"Batch {batch_num} Q{idx+1}: Empty question text")
        
        q_norm = q.lower()
        if q_norm in seen_q:
            raise ValueError(f"Batch {batch_num} Q{idx+1}: Duplicate question text: {q}")
        seen_q.add(q_norm)

        if re.match(r"^\d+[\.\)]\s*", q):
            raise ValueError(f"Batch {batch_num} Q{idx+1}: Question starts with number prefix: {q}")

        if len(wrong) != 3:
            raise ValueError(f"Batch {batch_num} Q{idx+1}: Expected 3 wrong choices, got {len(wrong)}")

        all_opts = [correct] + wrong
        for opt in all_opts:
            if not opt:
                raise ValueError(f"Batch {batch_num} Q{idx+1}: Empty option text")
            if re.match(r"^[A-D][\.\)]\s*", opt):
                raise ValueError(f"Batch {batch_num} Q{idx+1}: Option starts with letter prefix: {opt}")

        lowered = set(o.lower() for o in all_opts)
        if len(lowered) != 4:
            raise ValueError(f"Batch {batch_num} Q{idx+1}: Duplicate options in {all_opts}")

        if d not in (1, 2, 3):
            raise ValueError(f"Batch {batch_num} Q{idx+1}: Invalid difficulty d={d}")

        # Distribute answers evenly across 0, 1, 2, 3
        ans_idx = idx % 4
        opts = list(wrong)
        opts.insert(ans_idx, correct)

        formatted.append({
            "show": "The Golden Girls",
            "q": q,
            "options": opts,
            "answer": ans_idx,
            "d": d
        })

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(formatted, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Batch {batch_num}: Successfully wrote {len(formatted)} questions to {output_path}")
    return formatted
