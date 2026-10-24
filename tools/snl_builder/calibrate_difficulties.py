#!/usr/bin/env python3
"""
Calibrate difficulty distribution to exactly:
d1: 240 (30.0%)
d2: 320 (40.0%)
d3: 240 (30.0%)
"""

import json
import re

with open("tools/staging/snl_clean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Criteria for hardest questions (d3):
# - Mentions specific years/dates
# - Mentions specific obscure characters/writers/directors/crew
# - Specific lyric or line citations
# - Historical network/backstage trivia

# Criteria for easiest questions (d1):
# - Major iconic catchphrases ("Live from New York", "More cowbell", "Van down by the river")
# - High-profile recurring characters (Stefon, Church Lady, Wayne & Garth, Coneheads)
# - Well-known cast names (Chevy Chase, Will Ferrell, Eddie Murphy, Tina Fey, Kenan Thompson)

# First pass: sort candidates for d3 from d2
d2_indices = [i for i, item in enumerate(data) if item["d"] == 2]

# Score d2 items by specificity/complexity to find the best 91 to promote to d3
def complexity_score(item):
    text = item["q"] + " " + " ".join(item["options"])
    score = 0
    # specific years or dates
    if re.search(r'\b(19\d\d|20\d\d)\b', text):
        score += 3
    # specific backstage / producer / director / writer names
    if any(k in text for k in ["Ebersol", "Doumanian", "Olmeyer", "Schlosser", "McCarthy", "Pickett", "Downey", "Zakarian", "Feresten", "O'Donoghue", "Broecker", "Villines", "Rodriguez", "Diva", "McKinney"]):
        score += 4
    # longer questions usually have more specific situational context
    score += len(item["q"]) / 50.0
    return score

d2_sorted = sorted(d2_indices, key=lambda idx: complexity_score(data[idx]), reverse=True)

# Promote top 91 to d3
promote_to_d3 = set(d2_sorted[:91])
for idx in promote_to_d3:
    data[idx]["d"] = 3

# Now adjust d1 from 254 to 240 by moving 14 of the least obvious d1 questions to d2
d1_indices = [i for i, item in enumerate(data) if item["d"] == 1]
# Score d1 items: highest score means more specific/less obvious -> move to d2
d1_sorted = sorted(d1_indices, key=lambda idx: complexity_score(data[idx]), reverse=True)
demote_to_d2 = set(d1_sorted[:14])
for idx in demote_to_d2:
    data[idx]["d"] = 2

# Verify counts
counts = {1: 0, 2: 0, 3: 0}
for item in data:
    counts[item["d"]] += 1

print(f"Calibrated difficulty counts: d1={counts[1]} ({counts[1]/len(data)*100:.1f}%), d2={counts[2]} ({counts[2]/len(data)*100:.1f}%), d3={counts[3]} ({counts[3]/len(data)*100:.1f}%)")

with open("tools/staging/snl_clean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
