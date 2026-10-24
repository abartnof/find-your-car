#!/usr/bin/env python3
"""
Helper to build and validate Friends quiz batches.
Each batch has exactly 100 questions, balanced 25 of each answer index (0, 1, 2, 3),
and validated against tools/validate_quiz.py.
"""

import json
import os
import random
import re
import sys

def build_batch(raw_questions, output_path, batch_num=None):
    if len(raw_questions) != 100:
        raise ValueError(f"Batch must contain exactly 100 questions, got {len(raw_questions)}")

    # Deterministic seed per batch for reproducibility
    seed = 1000 + (batch_num if batch_num is not None else 1)
    rng = random.Random(seed)

    # 25 of each answer index: 0, 1, 2, 3
    target_indices = [0]*25 + [1]*25 + [2]*25 + [3]*25
    rng.shuffle(target_indices)

    seen_q = set()
    formatted = []

    for i, item in enumerate(raw_questions):
        q = item["q"].strip()
        correct = item["correct"].strip()
        distractors = [d.strip() for d in item["distractors"]]
        d = item.get("d", 2)

        if not q:
            raise ValueError(f"Question {i+1} has empty text")
        q_norm = q.lower()
        if q_norm in seen_q:
            raise ValueError(f"Duplicate question text at index {i+1}: {q}")
        seen_q.add(q_norm)

        if len(distractors) != 3:
            raise ValueError(f"Question {i+1} does not have exactly 3 distractors: {distractors}")

        all_opts_check = [correct] + distractors
        for opt in all_opts_check:
            if not opt:
                raise ValueError(f"Question {i+1} has empty option: {all_opts_check}")
            if re.match(r"^[A-D][\.\)]\s*", opt):
                raise ValueError(f"Question {i+1} option has letter prefix: {opt}")

        if len(set(opt.lower() for opt in all_opts_check)) != 4:
            raise ValueError(f"Question {i+1} has duplicate options: {all_opts_check}")

        ans_idx = target_indices[i]
        options = [None, None, None, None]
        options[ans_idx] = correct

        # Place the 3 distractors in the remaining slots
        distractor_slots = [j for j in range(4) if j != ans_idx]
        for slot, dist in zip(distractor_slots, distractors):
            options[slot] = dist

        formatted.append({
            "show": "Friends",
            "q": q,
            "options": options,
            "answer": ans_idx,
            "d": d
        })

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(formatted, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Successfully generated {output_path} with {len(formatted)} questions.")
    return formatted

if __name__ == "__main__":
    print("build_friends_batch module loaded.")
