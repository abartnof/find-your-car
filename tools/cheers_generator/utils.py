import json

def assemble_batch(raw_questions, batch_num, show_name="Cheers"):
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
    d_counts = {1: 0, 2: 0, 3: 0}

    for idx, item in enumerate(raw_questions):
        q = item["q"].strip()
        correct = item["correct"].strip()
        wrong = [w.strip() for w in item["wrong"]]
        d = item["d"]

        if d not in (1, 2, 3):
            raise ValueError(f"Batch {batch_num} Q{idx+1}: invalid difficulty {d}")
        d_counts[d] += 1

        if not q:
            raise ValueError(f"Batch {batch_num} Q{idx+1}: empty question text")

        if len(wrong) != 3:
            raise ValueError(f"Batch {batch_num} Q{idx+1}: wrong options count is {len(wrong)}, expected 3")

        all_opts = [correct] + wrong
        for opt in all_opts:
            if not opt:
                raise ValueError(f"Batch {batch_num} Q{idx+1}: empty option text in {all_opts}")

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

    print(f"Batch {batch_num} validated: 100 questions. Difficulties: d1={d_counts[1]}, d2={d_counts[2]}, d3={d_counts[3]}")
    return formatted

def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
