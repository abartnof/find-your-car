#!/usr/bin/env python3
"""
Parser for Anglophone Slang Trivia Quizzes (300 questions).
Processes:
- tools/dumps/anglophone_slang_quiz_100_questions.txt
- tools/dumps/anglophone_slang_quiz_questions_101_200.txt
- tools/dumps/anglophone_slang_quiz_questions_201_300.txt
Outputs:
- tools/staging/anglophone_slang_clean.json
"""

import json
import re
from pathlib import Path

FILES = [
    "tools/dumps/anglophone_slang_quiz_100_questions.txt",
    "tools/dumps/anglophone_slang_quiz_questions_101_200.txt",
    "tools/dumps/anglophone_slang_quiz_questions_201_300.txt",
]

OUTPUT_PATH = Path("tools/staging/anglophone_slang_clean.json")

LETTER_TO_INDEX = {"A": 0, "B": 1, "C": 2, "D": 3}


def parse_quiz_file(file_path: str):
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    lines = path.read_text(encoding="utf-8").splitlines()

    # Split between questions section and ANSWER KEY section
    ak_idx = None
    for idx, line in enumerate(lines):
        if "ANSWER KEY" in line:
            ak_idx = idx
            break

    if ak_idx is None:
        raise ValueError(f"Could not find ANSWER KEY in {file_path}")

    q_lines = lines[:ak_idx]
    ak_lines = lines[ak_idx + 1:]

    # Parse answer key
    answers = {}
    for line in ak_lines:
        line = line.strip()
        if not line or line.startswith("="):
            continue
        m = re.match(r"^(\d+)\.\s*([A-D])\s*(.*)$", line)
        if m:
            num = int(m.group(1))
            letter = m.group(2)
            fact = m.group(3).strip()
            answers[num] = (letter, fact)

    # Parse questions and options
    questions = []
    curr_num = None
    curr_qtext = None
    curr_opts = []

    def commit_question():
        if curr_num is not None:
            if curr_num not in answers:
                raise ValueError(f"Missing answer for question {curr_num}")
            ans_letter, fact = answers[curr_num]
            ans_idx = LETTER_TO_INDEX[ans_letter]
            if len(curr_opts) != 4:
                raise ValueError(f"Question {curr_num} does not have exactly 4 options: {curr_opts}")
            if len(set(curr_opts)) != 4:
                raise ValueError(f"Question {curr_num} has duplicate options: {curr_opts}")
            questions.append({
                "num": curr_num,
                "show": "Anglophone Slang",
                "q": curr_qtext,
                "options": list(curr_opts),
                "answer": ans_idx,
                "d": 1,
                "fact": fact
            })

    for line in q_lines:
        line_s = line.strip()
        if not line_s or line_s.startswith("==="):
            continue
        if line_s.startswith("Instructions:") or line_s.startswith("Answer key") or "GLOBAL ANGLOPHONE" in line_s:
            continue

        m_q = re.match(r"^(\d+)\.\s+(.*)$", line_s)
        m_opt = re.match(r"^([A-D])\)\s+(.*)$", line_s)

        if m_q:
            commit_question()
            curr_num = int(m_q.group(1))
            curr_qtext = m_q.group(2).strip()
            curr_opts = []
        elif m_opt:
            curr_opts.append(m_opt.group(2).strip())
        else:
            raise ValueError(f"Unexpected line format in {file_path}: {line_s}")

    commit_question()
    return questions


def main():
    all_questions = []
    for file_path in FILES:
        batch = parse_quiz_file(file_path)
        print(f"Parsed {len(batch)} questions from {file_path}")
        all_questions.extend(batch)

    # Sort and verify question sequence
    all_questions.sort(key=lambda x: x["num"])
    assert len(all_questions) == 300, f"Expected 300 questions, got {len(all_questions)}"
    for idx, item in enumerate(all_questions, 1):
        assert item["num"] == idx, f"Question number mismatch at index {idx}: got {item['num']}"

    # Strip the temporary "num" field to strictly adhere to the required schema
    cleaned_output = []
    for item in all_questions:
        cleaned_output.append({
            "show": item["show"],
            "q": item["q"],
            "options": item["options"],
            "answer": item["answer"],
            "d": item["d"],
            "fact": item["fact"]
        })

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(cleaned_output, f, indent=2, ensure_ascii=False)

    print(f"Successfully wrote {len(cleaned_output)} questions to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
