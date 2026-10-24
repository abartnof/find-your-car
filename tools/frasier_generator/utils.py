import json
import re

def assemble_batch(raw_questions, batch_num, show_name="Frasier"):
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
    for idx, item in enumerate(raw_questions):
        q = item["q"].strip()
        correct = item["correct"].strip()
        wrong = [w.strip() for w in item["wrong"]]
        d = item["d"]

        if len(wrong) != 3:
            raise ValueError(f"Batch {batch_num} Q{idx+1}: wrong options count is {len(wrong)}, expected 3")

        all_opts = [correct] + wrong
        lowered = set(o.lower() for o in all_opts)
        if len(lowered) != 4:
            raise ValueError(f"Batch {batch_num} Q{idx+1}: duplicate options in {all_opts}")

        target_idx = idx % 4
        opts = list(wrong)
        opts.insert(target_idx, correct)

        formatted.append({
            "show": show_name,
            "q": q,
            "options": opts,
            "answer": target_idx,
            "d": d
        })

    return formatted

def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
