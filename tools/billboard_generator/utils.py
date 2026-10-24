import json
import os
import re

SHOW_NAME = "Billboard Hits"

def assemble_batch(raw_questions, batch_num):
    """
    raw_questions is a list of dicts:
    {
        "q": str,
        "correct": str,
        "wrong": [str, str, str],
        "d": int (1, 2, or 3)
    }
    """
    if len(raw_questions) != 100:
        raise ValueError(f"Batch {batch_num} has {len(raw_questions)} questions; expected exactly 100")

    formatted = []
    seen_q = set()

    for idx, item in enumerate(raw_questions):
        q = item["q"].strip()
        correct = item["correct"].strip()
        wrong = [w.strip() for w in item["wrong"]]
        d = item["d"]

        if not q:
            raise ValueError(f"Batch {batch_num} Q{idx+1}: question text is empty")

        q_lower = q.lower()
        if q_lower in seen_q:
            raise ValueError(f"Batch {batch_num} Q{idx+1}: duplicate question in batch: {q}")
        seen_q.add(q_lower)

        if re.match(r"^\d+[\.\)]\s*", q):
            raise ValueError(f"Batch {batch_num} Q{idx+1}: starts with number prefix: {q}")

        if len(wrong) != 3:
            raise ValueError(f"Batch {batch_num} Q{idx+1}: wrong options count is {len(wrong)}, expected 3")

        all_opts = [correct] + wrong
        lowered = set(o.lower() for o in all_opts)
        if len(lowered) != 4:
            raise ValueError(f"Batch {batch_num} Q{idx+1}: duplicate options in {all_opts}")

        for opt in all_opts:
            if re.match(r"^[A-D][\.\)]\s*", opt):
                raise ValueError(f"Batch {batch_num} Q{idx+1}: option starts with letter prefix: {opt}")

        target_idx = idx % 4
        opts = list(wrong)
        opts.insert(target_idx, correct)

        formatted.append({
            "show": SHOW_NAME,
            "q": q,
            "options": opts,
            "answer": target_idx,
            "d": d
        })

    return formatted

def save_batch(batch_data, batch_num):
    out_dir = os.path.join(os.path.dirname(__file__), "..", "staging")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"billboard_batch_{batch_num}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(batch_data, f, indent=2, ensure_ascii=False)
    print(f"Saved Batch {batch_num} ({len(batch_data)} questions) to {out_path}")
