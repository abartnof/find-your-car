#!/usr/bin/env python3
"""
Merge script to replace/add trivia topics into src/questions.json.
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTIONS_PATH = os.path.join(BASE_DIR, "src", "questions.json")
STAGING_DIR = os.path.join(BASE_DIR, "tools", "staging")

OLD_90S_SITCOM_SHOWS = {
    'The Fresh Prince of Bel-Air', 'Seinfeld', 'Full House',
    'Home Improvement', 'The Nanny', 'The Drew Carey Show', '3rd Rock from the Sun',
    'NewsRadio', 'Boy Meets World', 'Married... with Children', 'Family Matters',
    'Mad About You', 'Living Single', 'A Different World', 'Spin City',
    'Roseanne', 'Coach', 'Just Shoot Me!', 'Step by Step', '90s Sitcoms'
}

TOPIC_FILES = [
    ("friends_clean.json", "Friends", 800),
    ("90s_sitcoms_clean.json", "90s Sitcoms", 1000),
    ("frasier_clean.json", "Frasier", 800),
    ("will_and_grace_clean.json", "Will & Grace", 800),
    ("80s_tv_shows_clean.json", "80s TV Shows", 1000),
    ("simpsons_clean.json", "The Simpsons", 500),
    ("snl_clean.json", "SNL", 800),
    ("produce_clean.json", "Fruits & Veggies", 500),
    ("rom_com_clean.json", "Romantic Comedies", 500),
    ("streaming_tv_clean.json", "Streaming TV Shows", 500),
    ("billboard_hits_clean.json", "Billboard Hits", 1000),
    ("cheers_clean.json", "Cheers", 500),
    ("ingredients_clean.json", "Ingredients", 800),
    ("golden_girls_clean.json", "The Golden Girls", 500),
]

def merge():
    with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
        existing_qs = json.load(f)

    print(f"Original total questions in {QUESTIONS_PATH}: {len(existing_qs)}")

    # Filter out topics being replaced wholesale
    filtered_qs = []
    removed_counts = {}
    for q in existing_qs:
        show = q.get("show", "")
        if show == "Friends":
            removed_counts["Friends"] = removed_counts.get("Friends", 0) + 1
        elif show == "Frasier":
            removed_counts["Frasier"] = removed_counts.get("Frasier", 0) + 1
        elif show in ("Will & Grace", "Will and Grace"):
            removed_counts["Will & Grace"] = removed_counts.get("Will & Grace", 0) + 1
        elif show in OLD_90S_SITCOM_SHOWS:
            removed_counts["Old 90s Sitcoms"] = removed_counts.get("Old 90s Sitcoms", 0) + 1
        elif show == "The Simpsons":
            removed_counts["The Simpsons"] = removed_counts.get("The Simpsons", 0) + 1
        elif show == "80s TV Shows":
            removed_counts["80s TV Shows"] = removed_counts.get("80s TV Shows", 0) + 1
        elif show.startswith("Comedy · ") or show == "Comedy Classics":
            removed_counts["Comedy Classics"] = removed_counts.get("Comedy Classics", 0) + 1
        elif show == "SNL":
            removed_counts["SNL"] = removed_counts.get("SNL", 0) + 1
        elif show == "Fruits & Veggies":
            removed_counts["Fruits & Veggies"] = removed_counts.get("Fruits & Veggies", 0) + 1
        elif show == "Romantic Comedies":
            removed_counts["Romantic Comedies"] = removed_counts.get("Romantic Comedies", 0) + 1
        elif show == "Streaming TV Shows":
            removed_counts["Streaming TV Shows"] = removed_counts.get("Streaming TV Shows", 0) + 1
        elif show == "Billboard Hits":
            removed_counts["Billboard Hits"] = removed_counts.get("Billboard Hits", 0) + 1
        elif show == "Cheers":
            removed_counts["Cheers"] = removed_counts.get("Cheers", 0) + 1
        elif show == "Ingredients":
            removed_counts["Ingredients"] = removed_counts.get("Ingredients", 0) + 1
        elif show in ("The Golden Girls", "Golden Girls"):
            removed_counts["The Golden Girls"] = removed_counts.get("The Golden Girls", 0) + 1
        else:
            filtered_qs.append(q)

    print("Removed old questions:")
    for k, v in removed_counts.items():
        print(f"  - {k}: {v}")
    print(f"Remaining baseline questions: {len(filtered_qs)}")

    all_qs = list(filtered_qs)

    missing = []
    ready = []
    for filename, expected_show, expected_count in TOPIC_FILES:
        filepath = os.path.join(STAGING_DIR, filename)
        if not os.path.exists(filepath):
            missing.append((filename, expected_show, expected_count))
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            topic_data = json.load(f)

        print(f"Adding {len(topic_data)} questions from {filename} for '{expected_show}' (target: {expected_count})...")
        ready.append((expected_show, len(topic_data)))
        for item in topic_data:
            q_clean = {
                "show": expected_show,
                "q": item["q"].strip(),
                "options": item["options"],
                "answer": item["answer"],
                "d": item.get("d", 1),
            }
            if "fact" in item and item["fact"]:
                q_clean["fact"] = item["fact"]
            all_qs.append(q_clean)

    if missing:
        print(f"\nNote: {len(missing)} topic files still generating:")
        for fn, show, cnt in missing:
            print(f"  - {show} ({cnt}): {fn}")

    print(f"\nTotal questions combined: {len(all_qs)}")
    with open(QUESTIONS_PATH, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, ensure_ascii=False, indent=0)
    print(f"Successfully saved to {QUESTIONS_PATH}")

if __name__ == "__main__":
    merge()
