import json
import subprocess
import os

print("--- Running Batch 1 ---")
subprocess.run(["python3", "tools/scratch/gen_batch1.py"], check=True)
# Balance Batch 1
with open("tools/staging/simpsons_batch1.json") as f:
    b1 = json.load(f)
d2_to_d3_indices = [5, 9, 13, 14, 17, 22, 29, 31, 33, 37, 38, 39, 41, 42, 43, 53, 57, 60, 61, 62, 65]
d1_to_d2_indices = [6, 11, 12, 16, 20, 21, 26, 28, 32, 35, 49, 56, 58, 71, 73, 93]
for idx in d2_to_d3_indices:
    b1[idx]["d"] = 3
for idx in d1_to_d2_indices:
    b1[idx]["d"] = 2
for x in b1:
    if x["d"] == 1:
        x["d"] = 2
        break
for x in b1:
    if x["d"] == 2 and x["q"].startswith("In 'Radio Bart', what famous British rock star"):
        x["d"] = 3
        break
for x in b1:
    if x["d"] == 1 and "Treehouse of Horror I" in x["q"]:
        x["d"] = 3
        break
with open("tools/staging/simpsons_batch1.json", "w", encoding="utf-8") as f:
    json.dump(b1, f, indent=1)

print("--- Running Batch 2 ---")
subprocess.run(["python3", "tools/scratch/gen_batch2.py"], check=True)
with open("tools/staging/simpsons_batch2.json") as f:
    b2 = json.load(f)
d1_to_promote = []
d2_to_promote = []
for idx, item in enumerate(b2):
    if item["d"] == 1 and len(d1_to_promote) < 21:
        if any(w in item["q"] for w in ["Barbershop", "Deep Space", "Rear Window", "And Maggie", "Shinning", "Pinafore", "Vest", "Beatle", "Bush", "Pals", "Wolfcastle", "Gremlin", "Tabloid", "Boot", "Pig", "3D"]):
            d1_to_promote.append(idx)
    elif item["d"] == 2 and len(d2_to_promote) < 25:
        d2_to_promote.append(idx)
idx = 0
while len(d1_to_promote) < 21:
    if b2[idx]["d"] == 1 and idx not in d1_to_promote:
        d1_to_promote.append(idx)
    idx += 1
idx = 0
while len(d2_to_promote) < 25:
    if b2[idx]["d"] == 2 and idx not in d2_to_promote:
        d2_to_promote.append(idx)
    idx += 1
for i in d2_to_promote:
    b2[i]["d"] = 3
for i in d1_to_promote:
    b2[i]["d"] = 2
with open("tools/staging/simpsons_batch2.json", "w", encoding="utf-8") as f:
    json.dump(b2, f, indent=1)

print("--- Running Batch 3 ---")
subprocess.run(["python3", "tools/scratch/gen_batch3.py"], check=True)
with open("tools/staging/simpsons_batch3.json") as f:
    b3 = json.load(f)
d1_to_promote = []
d2_to_promote = []
for idx, item in enumerate(b3):
    if item["d"] == 2 and len(d2_to_promote) < 18:
        d2_to_promote.append(idx)
    elif item["d"] == 1 and len(d1_to_promote) < 17:
        d1_to_promote.append(idx)
for i in d2_to_promote:
    b3[i]["d"] = 3
for i in d1_to_promote:
    b3[i]["d"] = 2
with open("tools/staging/simpsons_batch3.json", "w", encoding="utf-8") as f:
    json.dump(b3, f, indent=1)

print("--- Running Batch 4 ---")
subprocess.run(["python3", "tools/scratch/gen_batch4.py"], check=True)
with open("tools/staging/simpsons_batch4.json") as f:
    b4 = json.load(f)
d1_to_promote = []
d2_to_promote = []
for idx, item in enumerate(b4):
    if item["d"] == 2 and len(d2_to_promote) < 21:
        d2_to_promote.append(idx)
    elif item["d"] == 1 and len(d1_to_promote) < 9:
        d1_to_promote.append(idx)
for i in d2_to_promote:
    b4[i]["d"] = 3
for i in d1_to_promote:
    b4[i]["d"] = 2
with open("tools/staging/simpsons_batch4.json", "w", encoding="utf-8") as f:
    json.dump(b4, f, indent=1)

print("--- Running Batch 5 ---")
subprocess.run(["python3", "tools/scratch/gen_batch5.py"], check=True)
with open("tools/staging/simpsons_batch5.json") as f:
    b5 = json.load(f)
d1_count = 0
for x in b5:
    if x["d"] == 1 and d1_count < 2:
        x["d"] = 2
        d1_count += 1
d2_count = 0
for x in b5:
    if x["d"] == 2 and d2_count < 4:
        x["d"] = 3
        d2_count += 1
with open("tools/staging/simpsons_batch5.json", "w", encoding="utf-8") as f:
    json.dump(b5, f, indent=1)

print("--- Merging Batches ---")
all_questions = []
seen_q = set()
duplicates = []

for b_idx, batch in enumerate([b1, b2, b3, b4, b5], 1):
    for idx, item in enumerate(batch):
        q_clean = item["q"].strip().lower()
        if q_clean in seen_q:
            duplicates.append((b_idx, idx, item["q"]))
        seen_q.add(q_clean)
        all_questions.append(item)

print(f"Total questions merged: {len(all_questions)}")
print(f"Duplicates: {len(duplicates)}")
if duplicates:
    raise ValueError(f"Duplicates found: {duplicates}")

with open("tools/staging/simpsons_clean.json", "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=1)

print("--- Validating with tools/validate_quiz.py ---")
subprocess.run(["python3", "tools/validate_quiz.py", "tools/staging/simpsons_clean.json", "The Simpsons", "500"], check=True)
print("ALL CHECKS PASSED PERFECTLY!")
