#!/usr/bin/env python3
import os
import json
from collections import Counter

from tools.frasier_generator.batch1 import RAW_QUESTIONS as B1
from tools.frasier_generator.batch2 import RAW_QUESTIONS as B2
from tools.frasier_generator.batch3 import RAW_QUESTIONS as B3
from tools.frasier_generator.batch4 import RAW_QUESTIONS as B4
from tools.frasier_generator.batch5 import RAW_QUESTIONS as B5
from tools.frasier_generator.batch6 import RAW_QUESTIONS as B6
from tools.frasier_generator.batch7 import RAW_QUESTIONS as B7
from tools.frasier_generator.batch8 import RAW_QUESTIONS as B8
from tools.frasier_generator.calibrate import calibrate_batch
from tools.frasier_generator.utils import assemble_batch, save_json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGING_DIR = os.path.join(ROOT, "staging")
os.makedirs(STAGING_DIR, exist_ok=True)

batches_raw = [B1, B2, B3, B4, B5, B6, B7, B8]
all_clean_questions = []

seen_questions = set()
duplicates = []

for b_idx, raw_b in enumerate(batches_raw, 1):
    calibrated = calibrate_batch(raw_b)
    assembled = assemble_batch(calibrated, b_idx, "Frasier")
    batch_file = os.path.join(STAGING_DIR, f"frasier_batch{b_idx}.json")
    save_json(assembled, batch_file)
    print(f"Saved {len(assembled)} questions to {batch_file}")

    for item in assembled:
        q_norm = item["q"].strip().lower()
        if q_norm in seen_questions:
            duplicates.append((b_idx, item["q"]))
        seen_questions.add(q_norm)
        all_clean_questions.append(item)

if duplicates:
    print(f"CRITICAL ERROR: Found {len(duplicates)} duplicate questions:")
    for b_idx, q in duplicates:
        print(f"  Batch {b_idx}: {q}")
    raise ValueError("Duplicate questions found!")

clean_file = os.path.join(STAGING_DIR, "frasier_clean.json")
save_json(all_clean_questions, clean_file)
print(f"\nSuccessfully merged {len(all_clean_questions)} questions to {clean_file}")

ans_counts = Counter(q["answer"] for q in all_clean_questions)
diff_counts = Counter(q["d"] for q in all_clean_questions)
print("Answer distribution:", ans_counts)
print("Difficulty distribution:", diff_counts)
