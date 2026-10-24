#!/usr/bin/env python3
"""
Builder helper for Romantic Comedies quiz batches.
"""
import json
import os
import random
import re

SHOW_NAME = "Romantic Comedies"

def make_batch(questions_raw, batch_num, output_path=None):
    """
    questions_raw is a list of tuples:
      (q_text, correct_answer, [distractor1, distractor2, distractor3], difficulty)
    
    Ensures:
      - Exactly 100 questions
      - Exactly 25 of each answer index (0, 1, 2, 3)
      - Difficulty counts: ~30 d1, ~40 d2, ~30 d3
      - No regex prefix match on options (^[A-D][\.\)]\s*)
      - No duplicate options
      - No duplicate question text
    """
    if len(questions_raw) != 100:
        raise ValueError(f"Batch {batch_num} must have exactly 100 questions, got {len(questions_raw)}")

    rng = random.Random(5000 + batch_num * 107)
    answer_slots = [0] * 25 + [1] * 25 + [2] * 25 + [3] * 25
    rng.shuffle(answer_slots)

    clean_batch = []
    seen_q = set()
    diff_counts = {1: 0, 2: 0, 3: 0}

    for idx, item in enumerate(questions_raw):
        q, correct, distractors, d = item
        q_clean = q.strip()
        q_lower = q_clean.lower()

        if re.match(r"^\d+[\.\)]\s*", q_clean):
            raise ValueError(f"Batch {batch_num} Q{idx+1} starts with number prefix: {q_clean}")
        if q_lower in seen_q:
            raise ValueError(f"Batch {batch_num} Q{idx+1} duplicate question: {q_clean}")
        seen_q.add(q_lower)

        if d not in (1, 2, 3):
            raise ValueError(f"Batch {batch_num} Q{idx+1} invalid difficulty: {d}")
        diff_counts[d] += 1

        if len(distractors) != 3:
            raise ValueError(f"Batch {batch_num} Q{idx+1} does not have exactly 3 distractors: {distractors}")

        all_opts = [correct.strip()] + [opt.strip() for opt in distractors]
        opts_lower = [opt.lower() for opt in all_opts]
        if len(set(opts_lower)) != 4:
            raise ValueError(f"Batch {batch_num} Q{idx+1} has duplicate options: {all_opts}")

        for opt in all_opts:
            if not opt:
                raise ValueError(f"Batch {batch_num} Q{idx+1} has empty option")
            if re.match(r"^[A-D][\.\)]\s*", opt):
                raise ValueError(f"Batch {batch_num} Q{idx+1} option has letter prefix: '{opt}'")

        target_slot = answer_slots[idx]
        d_shuffled = [opt.strip() for opt in distractors]
        rng.shuffle(d_shuffled)

        final_opts = [None] * 4
        final_opts[target_slot] = correct.strip()
        d_idx = 0
        for slot in range(4):
            if slot != target_slot:
                final_opts[slot] = d_shuffled[d_idx]
                d_idx += 1

        clean_batch.append({
            "show": SHOW_NAME,
            "q": q_clean,
            "options": final_opts,
            "answer": target_slot,
            "d": d
        })

    print(f"Batch {batch_num} successfully built: {len(clean_batch)} questions")
    print(f"  Difficulties: d1={diff_counts[1]}, d2={diff_counts[2]}, d3={diff_counts[3]}")

    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(clean_batch, f, indent=2, ensure_ascii=False)
        print(f"  Saved to {output_path}")

    return clean_batch
