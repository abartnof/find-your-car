#!/usr/bin/env python3
"""
Calibrate difficulty ratings to ~30% d1 (easy), ~40% d2 (medium), ~30% d3 (hard)
across the 1000 questions and update both the batch files and clean file.
"""
import json
import os
import re

STAGING_DIR = os.path.join(os.path.dirname(__file__), "staging")

def score_difficulty(q_text, correct_ans):
    """
    Heuristic score to rank difficulty of questions:
    Higher score = harder question.
    """
    text = (q_text + " " + correct_ans).lower()
    score = 0

    # Hard markers (industry execs, unaired pilots, ratings numbers, legal/contract figures, obscure names)
    hard_keywords = [
        "executive", "president", "pilot", "unaired", "recast", "originally cast",
        "contract", "nielsen", "rating", "million per episode", "garnished", "lawsuit",
        "showrunner", "creator", "peabody", "syndication", "billboard", "airplay",
        "substance", "boycott", "standards and practices", "terry rakolta", "warren littlefield",
        "brandon tartikoff", "rick ludwin", "quincy jones", "fbi", "d.b. cooper", "1502",
        "consecutive", "nomination", "stephen tobolowsky", "frances fisher", "john posey",
        "lee garlington", "melissa joan hart", "dan quayle", "vice president", "al gore",
        "joe biden", "frank sinatra", "larry david", "matt williams", "carsey-werner",
        "miller-boyett", "peter engel", "don reo", "yvette lee bowser", "barry kemp",
        "chuck lorre", "michael jacobs", "daniel davis", "brenda cooper", "ann hampton",
        "dr. john", "jesse frederick", "bennett salvay", "the rembrandts", "jonathan wolff",
        "kelsey grammer", "moose", "alanis morissette", "dave coulier", "jon lovitz",
        "brynn", "phil hartman", "brett butler", "jaimee foxworth", "marques houston"
    ]
    for kw in hard_keywords:
        if kw in text:
            score += 2

    # Easy markers (catchphrases, famous lead characters, iconic food/props)
    easy_keywords = [
        "catchphrase", "what is the name of", "who played", "what was the name",
        "did i do that", "have mercy", "cut it out", "how rude", "you got it, dude",
        "whoa", "hey now", "holy crap", "not the mama", "no soup for you",
        "yada", "serenity now", "master of your domain", "puffy shirt", "junior mint",
        "art vandelay", "festivus", "carlton dance", "uncle phil", "steve urkel",
        "tool time", "binford", "al borland", "bayside high", "danny tanner",
        "full house", "saved by the bell", "fresh prince", "bel-air", "frasier crane"
    ]
    for kw in easy_keywords:
        if kw in text:
            score -= 2

    # Length of question often correlates with complex background setup
    if len(q_text) > 130:
        score += 1
    elif len(q_text) < 70:
        score -= 1

    return score

def main():
    batches = []
    for b in range(1, 11):
        b_path = os.path.join(STAGING_DIR, f"90s_sitcoms_batch{b}.json")
        with open(b_path, "r", encoding="utf-8") as f:
            batches.append(json.load(f))

    # Score each question in each batch
    # In each batch of 100 questions, assign exactly:
    # 30 d1 (easy), 40 d2 (medium), 30 d3 (hard)
    for b_idx, batch in enumerate(batches, 1):
        scored = []
        for q_idx, q in enumerate(batch):
            sc = score_difficulty(q["q"], q["options"][q["answer"]])
            scored.append((sc, q_idx))
        
        # Sort by score ascending (lowest score = easiest = d1)
        scored.sort(key=lambda x: x[0])
        
        # Lowest 30 -> d1
        for sc, q_idx in scored[:30]:
            batch[q_idx]["d"] = 1
        # Middle 40 -> d2
        for sc, q_idx in scored[30:70]:
            batch[q_idx]["d"] = 2
        # Highest 30 -> d3
        for sc, q_idx in scored[70:]:
            batch[q_idx]["d"] = 3

        # Save calibrated batch
        b_path = os.path.join(STAGING_DIR, f"90s_sitcoms_batch{b_idx}.json")
        with open(b_path, "w", encoding="utf-8") as f:
            json.dump(batch, f, indent=2, ensure_ascii=False)
        print(f"Batch {b_idx} calibrated: 30 d1, 40 d2, 30 d3")

    # Merge into clean file
    all_q = []
    for b in batches:
        all_q.extend(b)

    clean_path = os.path.join(STAGING_DIR, "90s_sitcoms_clean.json")
    with open(clean_path, "w", encoding="utf-8") as f:
        json.dump(all_q, f, indent=2, ensure_ascii=False)

    print(f"Merged 1000 questions into {clean_path}")

if __name__ == "__main__":
    main()
