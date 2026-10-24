import json
import random
import re

def build_batch(questions_data, batch_num, output_path):
    """
    questions_data is a list of tuples:
    (q_text, correct_answer, [distractor1, distractor2, distractor3], difficulty)
    """
    if len(questions_data) != 100:
        raise ValueError(f"Batch {batch_num} has {len(questions_data)} questions, expected 100")

    # Fixed seed per batch for reproducible balanced answer indices
    rng = random.Random(batch_num * 1000 + 42)
    ans_list = [0] * 25 + [1] * 25 + [2] * 25 + [3] * 25
    rng.shuffle(ans_list)

    batch_output = []
    seen_q = set()
    diff_counts = {1: 0, 2: 0, 3: 0}

    for idx, (q, correct, distractors, d) in enumerate(questions_data):
        q_clean = q.strip()
        if re.match(r"^\d+[\.\)]\s*", q_clean):
            raise ValueError(f"Q{idx+1} starts with a number prefix: {q_clean}")
        if q_clean.lower() in seen_q:
            raise ValueError(f"Q{idx+1} is duplicate question text: {q_clean}")
        seen_q.add(q_clean.lower())

        if d not in (1, 2, 3):
            raise ValueError(f"Q{idx+1} has invalid difficulty: {d}")
        diff_counts[d] += 1

        if len(distractors) != 3:
            raise ValueError(f"Q{idx+1} does not have exactly 3 distractors: {distractors}")

        target_ans = ans_list[idx]
        options = [None, None, None, None]
        options[target_ans] = correct.strip()

        # Shuffle distractors deterministically
        shuffled_distractors = list(distractors)
        rng.shuffle(shuffled_distractors)

        w_idx = 0
        for slot in range(4):
            if slot != target_ans:
                options[slot] = shuffled_distractors[w_idx].strip()
                w_idx += 1

        # Check unique options
        opts_lower = [opt.lower() for opt in options]
        if len(set(opts_lower)) != 4:
            raise ValueError(f"Q{idx+1} has duplicate options: {options}")

        # Check no option has letter prefix
        for opt in options:
            if re.match(r"^[A-D][\.\)]\s*", opt):
                raise ValueError(f"Q{idx+1} option has letter prefix: {opt}")

        batch_output.append({
            "show": "80s TV Shows",
            "q": q_clean,
            "options": options,
            "answer": target_ans,
            "d": d
        })

    print(f"Batch {batch_num} generated successfully:")
    print(f"  Difficulties: d1={diff_counts[1]}, d2={diff_counts[2]}, d3={diff_counts[3]}")
    print(f"  Writing to: {output_path}")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(batch_output, f, indent=2, ensure_ascii=False)

    return batch_output
