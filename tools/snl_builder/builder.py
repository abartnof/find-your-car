#!/usr/bin/env python3
"""
SNL Quiz Batch Builder & Validator Utility
"""

import json
import random
import re
import sys

def build_batch(raw_questions, output_path, batch_num=1):
    if len(raw_questions) != 100:
        raise ValueError(f"Batch {batch_num} must contain exactly 100 questions, got {len(raw_questions)}")

    # Deterministic seed per batch for reproducible shuffling
    seed = 5000 + batch_num
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
            raise ValueError(f"Batch {batch_num} Q{i+1}: empty question text")
        q_norm = q.lower()
        if q_norm in seen_q:
            raise ValueError(f"Batch {batch_num} Q{i+1}: duplicate question text in batch: {q}")
        seen_q.add(q_norm)

        if len(distractors) != 3:
            raise ValueError(f"Batch {batch_num} Q{i+1}: does not have exactly 3 distractors: {distractors}")

        all_opts = [correct] + distractors
        for opt in all_opts:
            if not opt:
                raise ValueError(f"Batch {batch_num} Q{i+1}: empty option in {all_opts}")
            if re.match(r"^[A-D][\.\)]\s*", opt):
                raise ValueError(f"Batch {batch_num} Q{i+1}: option starts with letter prefix: {opt}")

        if len(set(opt.lower() for opt in all_opts)) != 4:
            raise ValueError(f"Batch {batch_num} Q{i+1}: duplicate options: {all_opts}")

        ans_idx = target_indices[i]
        options = [None, None, None, None]
        options[ans_idx] = correct

        other_slots = [j for j in range(4) if j != ans_idx]
        for slot, dist in zip(other_slots, distractors):
            options[slot] = dist

        formatted.append({
            "show": "SNL",
            "q": q,
            "options": options,
            "answer": ans_idx,
            "d": d
        })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(formatted, f, indent=2, ensure_ascii=False)

    print(f"Successfully wrote {len(formatted)} questions to {output_path}")
    return formatted
