#!/usr/bin/env python3
"""
Parser for sitcom trivia dumps:
- 30 Rock (300 questions)
- Brooklyn Nine-Nine (300 questions)
- Arrested Development (300 questions)
- Parks and Recreation (300 questions)

Parses dumps in tools/dumps/ and outputs clean JSON in tools/staging/.
"""

import json
import os
import re
from typing import Dict, List, Any

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUMPS_DIR = os.path.join(ROOT, "tools", "dumps")
STAGING_DIR = os.path.join(ROOT, "tools", "staging")

LETTER_TO_INDEX = {"A": 0, "B": 1, "C": 2, "D": 3}


def clean_text(text: str) -> str:
    """Clean whitespace and common artifact chars."""
    return re.sub(r"[ \t]+", " ", text).strip()


def parse_dump(path: str, show_name: str, inline_answers: bool = False) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    ans_dict: Dict[int, int] = {}
    if not inline_answers:
        ans_idx = text.rfind("ANSWER KEY")
        if ans_idx == -1:
            raise ValueError(f"Could not find ANSWER KEY in {path}")
        q_text = text[:ans_idx]
        ans_text = text[ans_idx:]
        matches = re.findall(r"(\d+)\.\s*([A-D])\b", ans_text)
        for k, v in matches:
            ans_dict[int(k)] = LETTER_TO_INDEX[v.upper()]
        if len(ans_dict) != 300:
            raise ValueError(f"Expected 300 answers in {path}, found {len(ans_dict)}")
    else:
        q_text = text

    lines = q_text.splitlines()
    questions: List[Dict[str, Any]] = []
    curr_q_num = None
    curr_q_str = None
    curr_opts: Dict[str, str] = {}
    curr_ans = None

    def commit():
        nonlocal curr_q_num, curr_q_str, curr_opts, curr_ans
        if curr_q_num is None:
            return

        if len(curr_opts) != 4 or set(curr_opts.keys()) != {"A", "B", "C", "D"}:
            raise ValueError(f"[{show_name}] Q{curr_q_num} does not have exactly 4 options: {curr_opts}")

        opts = [curr_opts[k] for k in ["A", "B", "C", "D"]]
        if len(set(opts)) != 4:
            raise ValueError(f"[{show_name}] Q{curr_q_num} has duplicate options: {opts}")

        ans = curr_ans if inline_answers else ans_dict.get(curr_q_num)
        if ans is None or ans not in (0, 1, 2, 3):
            raise ValueError(f"[{show_name}] Q{curr_q_num} invalid or missing answer: {ans}")

        # Check stripping of question number & option letters
        if re.match(r"^\d+[\.\)]\s*", curr_q_str):
            raise ValueError(f"[{show_name}] Q{curr_q_num} has unstripped number prefix: {curr_q_str}")
        for opt in opts:
            if re.match(r"^\*{0,2}[A-D][\)\.]\s+", opt):
                raise ValueError(f"[{show_name}] Q{curr_q_num} option has unstripped option label: {opt}")

        item: Dict[str, Any] = {
            "show": show_name,
            "q": curr_q_str,
            "options": opts,
            "answer": ans,
            "d": 1,
        }
        questions.append(item)

    for line in lines:
        ls = clean_text(line)
        if not ls or ls.startswith("="):
            continue

        # Check for question line: e.g., '1. Question...' or '**1.** Question...'
        qm = re.match(r"^\*{0,2}(\d+)[\.\)]\*{0,2}\s*(.*)", ls)
        if qm:
            commit()
            curr_q_num = int(qm.group(1))
            curr_q_str = clean_text(qm.group(2))
            curr_opts = {}
            curr_ans = None
            continue

        # Check for option line: e.g., 'A. Option' or 'A) Option' or '**A)** Option'
        om = re.match(r"^\*{0,2}([A-D])[\)\.:]\*{0,2}\s*(.*)", ls)
        if om and curr_q_num is not None:
            curr_opts[om.group(1).upper()] = clean_text(om.group(2))
            continue

        # Check for inline answer line: e.g., 'Answer: B'
        if inline_answers:
            am = re.match(r"^Answer:\s*([A-D])\b", ls, re.IGNORECASE)
            if am and curr_q_num is not None:
                curr_ans = LETTER_TO_INDEX[am.group(1).upper()]
                continue

    commit()

    if len(questions) != 300:
        raise ValueError(f"[{show_name}] Expected 300 questions, but parsed {len(questions)}")

    return questions


def validate_questions(questions: List[Dict[str, Any]], expected_show: str, expected_count: int = 300):
    assert len(questions) == expected_count, f"Expected {expected_count} questions for {expected_show}, got {len(questions)}"
    for idx, q in enumerate(questions):
        q_num = idx + 1
        assert q["show"] == expected_show, f"Q{q_num} show mismatch: {q.get('show')} != {expected_show}"
        assert isinstance(q["q"], str) and len(q["q"].strip()) > 0, f"Q{q_num} empty question text"
        assert not re.match(r"^\d+[\.\)]\s*", q["q"]), f"Q{q_num} contains question number: {q['q']}"
        assert isinstance(q["options"], list) and len(q["options"]) == 4, f"Q{q_num} does not have 4 options"
        assert len(set(q["options"])) == 4, f"Q{q_num} options are not unique: {q['options']}"
        for opt in q["options"]:
            assert isinstance(opt, str) and len(opt.strip()) > 0, f"Q{q_num} empty option text"
            assert not re.match(r"^\*{0,2}[A-D][\)\.]\s+", opt), f"Q{q_num} option has label prefix: {opt}"
        assert isinstance(q["answer"], int) and 0 <= q["answer"] <= 3, f"Q{q_num} answer not between 0 and 3: {q['answer']}"
        assert q["d"] == 1, f"Q{q_num} difficulty is not 1: {q.get('d')}"


CONFIGS = [
    {
        "dump_file": "30_rock_ultimate_trivia_300_multiple_choice_questions.txt",
        "output_file": "30_rock_clean.json",
        "show": "30 Rock",
        "inline_answers": False,
    },
    {
        "dump_file": "brooklyn_nine_nine_300_question_trivia_quiz.txt",
        "output_file": "brooklyn_nine_nine_clean.json",
        "show": "Brooklyn Nine-Nine",
        "inline_answers": True,
    },
    {
        "dump_file": "arrested_development_300_trivia_questions.txt",
        "output_file": "arrested_development_clean.json",
        "show": "Arrested Development",
        "inline_answers": False,
    },
    {
        "dump_file": "parks_and_recreation_300_trivia_questions.txt",
        "output_file": "parks_and_recreation_clean.json",
        "show": "Parks and Recreation",
        "inline_answers": True,
    },
]


def main():
    os.makedirs(STAGING_DIR, exist_ok=True)
    summary = {}

    for cfg in CONFIGS:
        dump_path = os.path.join(DUMPS_DIR, cfg["dump_file"])
        out_path = os.path.join(STAGING_DIR, cfg["output_file"])

        print(f"Parsing {cfg['show']} from {dump_path}...")
        questions = parse_dump(dump_path, cfg["show"], inline_answers=cfg["inline_answers"])
        validate_questions(questions, cfg["show"], expected_count=300)

        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(questions, f, indent=2, ensure_ascii=False)

        summary[cfg["show"]] = len(questions)
        print(f"  -> Wrote {len(questions)} verified questions to {out_path}")

    print("\n--- Summary of Parsed Quizzes ---")
    for show, count in summary.items():
        print(f"  {show}: {count} questions")
    print("All quizzes parsed and validated successfully!")


if __name__ == "__main__":
    main()
