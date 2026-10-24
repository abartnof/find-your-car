#!/usr/bin/env python3
"""
Helper module to build, balance, and validate 90s Sitcoms batches.
"""
import json
import os
import random

SHOW_NAME = "90s Sitcoms"

def make_batch(questions_raw, batch_num, output_path=None):
    """
    questions_raw: list of dicts with:
      - 'q': question text
      - 'correct': correct answer string
      - 'distractors': list of 3 distractor strings
      - 'd': difficulty (1, 2, or 3)
    
    Balances answer positions evenly (0, 1, 2, 3: 25 each per 100 questions).
    """
    if len(questions_raw) != 100:
        raise ValueError(f"Batch {batch_num} must have exactly 100 questions, got {len(questions_raw)}")

    # Deterministic seed based on batch_num
    rng = random.Random(42 + batch_num)
    
    # Target 25 of each answer index: 0, 1, 2, 3
    answer_slots = [0]*25 + [1]*25 + [2]*25 + [3]*25
    rng.shuffle(answer_slots)

    clean_batch = []
    seen_q = set()

    for idx, item in enumerate(questions_raw):
        q = item["q"].strip()
        q_lower = q.lower()
        if q_lower in seen_q:
            raise ValueError(f"Duplicate question in batch {batch_num} index {idx}: {q}")
        seen_q.add(q_lower)

        correct = item["correct"].strip()
        distractors = [d.strip() for d in item["distractors"]]
        if len(distractors) != 3:
            raise ValueError(f"Batch {batch_num} Q{idx+1} does not have 3 distractors: {distractors}")

        all_opts = [correct] + distractors
        if len(set(opt.lower() for opt in all_opts)) != 4:
            raise ValueError(f"Batch {batch_num} Q{idx+1} has duplicate options: {all_opts}")

        target_slot = answer_slots[idx]
        # Place correct option at target_slot, and shuffle distractors into the remaining slots
        d_shuffled = distractors.copy()
        rng.shuffle(d_shuffled)

        final_opts = [None]*4
        final_opts[target_slot] = correct
        d_idx = 0
        for i in range(4):
            if i != target_slot:
                final_opts[i] = d_shuffled[d_idx]
                d_idx += 1

        d = item.get("d", 2)
        if d not in (1, 2, 3):
            raise ValueError(f"Invalid difficulty {d} in Batch {batch_num} Q{idx+1}")

        clean_batch.append({
            "show": SHOW_NAME,
            "q": q,
            "options": final_opts,
            "answer": target_slot,
            "d": d
        })

    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(clean_batch, f, indent=2, ensure_ascii=False)
        print(f"Batch {batch_num} written to {output_path} (100 questions)")

    return clean_batch
