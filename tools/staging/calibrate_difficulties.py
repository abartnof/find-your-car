#!/usr/bin/env python3
import json
import re

# We can categorize questions into d=1, 2, 3 based on query keywords, depth, or ranking
# For each batch of 100 questions, we want exactly 30 d=1, 40 d=2, 30 d=3.

def score_question_depth(q_text):
    text = q_text.lower()
    score = 0
    # Easy indicators (famous leads, broad fundamentals)
    easy_words = ["profession", "middle name", "signature beverage", "catchphrase", 
                  "what kind of pills", "ice cream", "water-filled", "emmy", "cher", "biden",
                  "best friends", "roommates", "who played", "what is the name of", "columbia",
                  "apartments", "bartender", "maid", "lawyer", "interior designer"]
    
    # Hard indicators (specific episode titles, numbers, behind the scenes, obscure side characters)
    hard_words = ["episode '", "in what year", "how many", "nielsen", "viewers", "puck building",
                  "smithsonian", "barrowman", "jonathan wolff", "kinnally", "marchinko", "emerson",
                  "stage 17", "contract", "lawsuit", "peabody", "golden globe record", "alts",
                  "monitors", "warm-up", "multi-camera", "cloris leachman", "bobby cannavale",
                  "gavin hatch", "fannie lieber", "scott woolley", "amber-louise", "estefan",
                  "quinceañera", "curmudgeon", "tracheostomy", "baby glenn", "klaus", "delaney",
                  "940 park", "400,000", "syndication", "30-second"]
    
    for w in hard_words:
        if w in text:
            score += 2
    for w in easy_words:
        if w in text:
            score -= 1
    return score

for b in range(1, 9):
    batch_file = f"tools/staging/will_and_grace_batch{b}.json"
    with open(batch_file, "r", encoding="utf-8") as f:
        questions = json.load(f)
    assert len(questions) == 100
    
    # Sort indexed by depth score
    scored = []
    for idx, q in enumerate(questions):
        scored.append((score_question_depth(q["q"]), idx))
    
    scored.sort(key=lambda x: x[0])
    
    # Lowest 30 -> d=1
    # Middle 40 -> d=2
    # Highest 30 -> d=3
    for rank, (score, idx) in enumerate(scored):
        if rank < 30:
            questions[idx]["d"] = 1
        elif rank < 70:
            questions[idx]["d"] = 2
        else:
            questions[idx]["d"] = 3
            
    with open(batch_file, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2)

print("Calibrated difficulties in all 8 batches.")
