#!/usr/bin/env python3
"""
Parse 4 quiz dump files into clean staging JSON files:
1. tools/dumps/king_of_the_hill_400_quiz_questions.txt -> tools/staging/king_of_the_hill_clean.json ("King of the Hill", 400 questions)
2. tools/dumps/taskmaster_uk_300_multiple_choice_questions.txt -> tools/staging/taskmaster_uk_clean.json ("Taskmaster UK", 300 questions)
3. tools/dumps/ben_folds_300_question_trivia_quiz.txt -> tools/staging/ben_folds_clean.json ("Ben Folds", 300 questions)
4. tools/dumps/celebrity_anecdotes_quiz-3.txt -> tools/staging/celebrity_anecdotes_clean.json ("Celebrity Anecdotes", 400 questions)
"""

import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUMPS_DIR = os.path.join(ROOT, "tools", "dumps")
STAGING_DIR = os.path.join(ROOT, "tools", "staging")

LETTER_TO_INDEX = {"A": 0, "B": 1, "C": 2, "D": 3}


def clean_option(opt_str: str) -> str:
    """Strip markdown artifacts and option prefix (e.g. 'A) ', '**A)** ')."""
    s = opt_str.strip()
    s = re.sub(r"^\*+([A-D][\)\.])\*+\s*", "", s)
    s = re.sub(r"^([A-D][\)\.])\s*", "", s)
    return s.strip()


def clean_question(q_str: str) -> str:
    """Strip question numbers (e.g. '1. ') and markdown artifacts."""
    s = q_str.strip()
    s = re.sub(r"^\d+\.\s*", "", s)
    if s.startswith("**") and s.endswith("**"):
        s = s[2:-2].strip()
    return s.strip()


def clean_fact(fact_str: str) -> str:
    """Strip 'Fact:' prefix and whitespace."""
    s = fact_str.strip()
    s = re.sub(r"^Fact:\s*", "", s, flags=re.IGNORECASE)
    return s.strip()


def validate_questions(questions: list, expected_count: int, show_name: str):
    """Validate question list against project requirements."""
    assert len(questions) == expected_count, (
        f"Expected {expected_count} questions for '{show_name}', found {len(questions)}"
    )
    for idx, q in enumerate(questions, 1):
        assert q.get("show") == show_name, f"Item {idx}: invalid show {q.get('show')}"
        assert q.get("q"), f"Item {idx}: missing question text"
        assert not re.match(r"^\d+\.", q["q"]), f"Item {idx}: question text has leading number: {q['q']}"
        opts = q.get("options")
        assert isinstance(opts, list) and len(opts) == 4, f"Item {idx}: must have exactly 4 options"
        assert len(set(opts)) == 4, f"Item {idx}: options not unique: {opts}"
        for opt in opts:
            assert opt, f"Item {idx}: empty option in {opts}"
            assert not re.match(r"^[A-D]\)", opt), f"Item {idx}: option has letter prefix: {opt}"
        ans = q.get("answer")
        assert ans in (0, 1, 2, 3), f"Item {idx}: invalid answer index: {ans}"
        assert q.get("d") == 1, f"Item {idx}: invalid difficulty 'd': {q.get('d')}"


def parse_king_of_the_hill() -> list:
    path = os.path.join(DUMPS_DIR, "king_of_the_hill_400_quiz_questions.txt")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    blocks = re.split(r"(?m)(?=^\d+\.\s+)", text)
    blocks = [b for b in blocks if re.match(r"^\d+\.", b.strip())]

    questions = []
    for b in blocks:
        lines = [l.strip() for l in b.strip().splitlines() if l.strip() and not l.startswith("=")]
        q_line = lines[0]
        qm = re.match(r"^(\d+)\.\s*(.*)", q_line)
        if not qm:
            continue
        q_num = int(qm.group(1))
        q_str = clean_question(qm.group(2))

        ans_idx = None
        opts = []
        for l in lines[1:]:
            if l.startswith("Answer:"):
                letter = l.split(":", 1)[1].strip()
                ans_idx = LETTER_TO_INDEX[letter]
            elif l.startswith("=") or l == "END OF QUIZ":
                continue
            else:
                opts.append(clean_option(l))

        # Handle formatting edge cases in dump
        if q_num == 5:
            # Peggy Hill's official profession when not writing columns or substitute teaching:
            # Dump had duplicate 'B)' markers: 'B) Real estate agent', 'B) Substitute Spanish teacher'.
            # Set option B to 'Real estate agent' matching Answer: B.
            opts = [
                "Substitute Spanish teacher",
                "Real estate agent",
                "Hairdresser",
                "Boggle referee",
            ]
            ans_idx = 1
        elif q_num == 235:
            # Yes/No question in dump -> expand to 4 options
            opts = ["Yes", "No", "Only his singing voice", "No, voiced by an impersonator"]
            ans_idx = 0

        questions.append({
            "show": "King of the Hill",
            "q": q_str,
            "options": opts,
            "answer": ans_idx,
            "d": 1,
        })

    validate_questions(questions, 400, "King of the Hill")
    out_path = os.path.join(STAGING_DIR, "king_of_the_hill_clean.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=1, ensure_ascii=False)
    print(f"Successfully wrote {len(questions)} King of the Hill questions to {out_path}")
    return questions


def parse_taskmaster_uk() -> list:
    path = os.path.join(DUMPS_DIR, "taskmaster_uk_300_multiple_choice_questions.txt")
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    def clean_section(s: str) -> str:
        words = s.split()
        lower_words = {"of", "and", "the", "in", "on", "at", "to", "for"}
        res = []
        for i, w in enumerate(words):
            if w in {"II", "III", "IV", "VR", "UK"}:
                res.append(w)
            elif w == "&":
                res.append("&")
            elif i > 0 and w.lower() in lower_words:
                res.append(w.lower())
            else:
                res.append(w.capitalize())
        return " ".join(res)

    questions = []
    current_sec = None
    current_q_num = None
    current_q_str = None
    current_opts = {}

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("------"):
            if i + 1 < len(lines):
                cand = lines[i + 1].strip()
                if cand and not cand.startswith("------") and not cand.startswith("==="):
                    current_sec = clean_section(cand)
                    i += 2
                    continue
        qm = re.match(r"^(\d+)\.\s*(.*)", line)
        if qm:
            current_q_num = int(qm.group(1))
            current_q_str = clean_question(qm.group(2))
            current_opts = {}
            i += 1
            continue

        om = re.match(r"^([A-D])\)\s*(.*)", line)
        if om and current_q_num is not None:
            current_opts[om.group(1)] = clean_option(om.group(2))
            i += 1
            continue

        am = re.match(r"^Answer:\s*([A-D])", line)
        if am and current_q_num is not None:
            ans_idx = LETTER_TO_INDEX[am.group(1)]
            opts = [current_opts[k] for k in ["A", "B", "C", "D"]]
            item = {
                "show": "Taskmaster UK",
                "section": current_sec,
                "q": current_q_str,
                "options": opts,
                "answer": ans_idx,
                "d": 1,
            }
            questions.append(item)
            current_q_num = None
            current_q_str = None
            current_opts = {}
            i += 1
            continue
        i += 1

    validate_questions(questions, 300, "Taskmaster UK")
    out_path = os.path.join(STAGING_DIR, "taskmaster_uk_clean.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=1, ensure_ascii=False)
    print(f"Successfully wrote {len(questions)} Taskmaster UK questions to {out_path}")
    return questions


def parse_ben_folds() -> list:
    path = os.path.join(DUMPS_DIR, "ben_folds_300_question_trivia_quiz.txt")
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    questions = []
    current_sec = None
    current_q_num = None
    current_q_str = None
    current_opts = {}

    for line in lines:
        ls = line.strip()
        if not ls:
            continue
        sm = re.match(r"^---\s*SECTION\s*\d+:\s*(.*?)\s*---$", ls)
        if sm:
            current_sec = sm.group(1).title()
            continue
        qm = re.match(r"^(\d+)\.\s*(.*)", ls)
        if qm:
            current_q_num = int(qm.group(1))
            current_q_str = clean_question(qm.group(2))
            current_opts = {}
            continue
        om = re.match(r"^([A-D])\)\s*(.*)", ls)
        if om and current_q_num is not None:
            current_opts[om.group(1)] = clean_option(om.group(2))
            continue
        am = re.match(r"^Answer:\s*([A-D])", ls)
        if am and current_q_num is not None:
            ans_idx = LETTER_TO_INDEX[am.group(1)]
            opts = [current_opts[k] for k in ["A", "B", "C", "D"]]
            item = {
                "show": "Ben Folds",
                "section": current_sec,
                "q": current_q_str,
                "options": opts,
                "answer": ans_idx,
                "d": 1,
            }
            questions.append(item)
            current_q_num = None
            current_q_str = None
            current_opts = {}

    validate_questions(questions, 300, "Ben Folds")
    out_path = os.path.join(STAGING_DIR, "ben_folds_clean.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=1, ensure_ascii=False)
    print(f"Successfully wrote {len(questions)} Ben Folds questions to {out_path}")
    return questions


def parse_celebrity_anecdotes() -> list:
    path = os.path.join(DUMPS_DIR, "celebrity_anecdotes_quiz-3.txt")
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    questions = []
    current_sec = None
    current_q_num = None
    current_q_str = None
    current_opts = {}
    current_ans = None

    for line in lines:
        ls = line.strip()
        if not ls:
            continue
        sm = re.search(r"BATCH\s*\d+:\s*\d+[–-]\d+", ls)
        if sm:
            current_sec = sm.group(0).title()
            continue
        qm = re.match(r"^(\d+)\.\s*(.*)", ls)
        if qm:
            current_q_num = int(qm.group(1))
            current_q_str = clean_question(qm.group(2))
            current_opts = {}
            current_ans = None
            continue
        om = re.match(r"^([A-D])\)\s*(.*)", ls)
        if om and current_q_num is not None:
            current_opts[om.group(1)] = clean_option(om.group(2))
            continue
        am = re.match(r"^Answer:\s*([A-D])", ls)
        if am and current_q_num is not None:
            current_ans = LETTER_TO_INDEX[am.group(1)]
            continue
        fm = re.match(r"^Fact:\s*(.*)", ls, flags=re.IGNORECASE)
        if fm and current_q_num is not None and current_ans is not None:
            fact_str = clean_fact(fm.group(1))
            opts = [current_opts[k] for k in ["A", "B", "C", "D"]]
            item = {
                "show": "Celebrity Anecdotes",
                "section": current_sec,
                "q": current_q_str,
                "options": opts,
                "answer": current_ans,
                "d": 1,
                "fact": fact_str,
            }
            questions.append(item)
            current_q_num = None
            current_q_str = None
            current_opts = {}
            current_ans = None

    validate_questions(questions, 400, "Celebrity Anecdotes")
    out_path = os.path.join(STAGING_DIR, "celebrity_anecdotes_clean.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=1, ensure_ascii=False)
    print(f"Successfully wrote {len(questions)} Celebrity Anecdotes questions to {out_path}")
    return questions


def main():
    os.makedirs(STAGING_DIR, exist_ok=True)
    koth = parse_king_of_the_hill()
    tm = parse_taskmaster_uk()
    bf = parse_ben_folds()
    ca = parse_celebrity_anecdotes()

    total = len(koth) + len(tm) + len(bf) + len(ca)
    print(f"\nAll 4 quiz dumps parsed successfully! Total questions: {total}")
    print(f"- King of the Hill: {len(koth)}")
    print(f"- Taskmaster UK: {len(tm)}")
    print(f"- Ben Folds: {len(bf)}")
    print(f"- Celebrity Anecdotes: {len(ca)}")


if __name__ == "__main__":
    main()
