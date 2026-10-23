#!/usr/bin/env python3 -I
"""Parse raw podcast quiz dumps into valid staging JSON files.

Quizzes processed:
1. tools/dumps/why_wont_you_date_me_quiz.txt
   -> tools/staging/why_wont_you_date_me_clean.json (Show: "Why Won't You Date Me?")
2. tools/dumps/hdtgm_200_question_multiple_choice_quiz.txt
   -> tools/staging/hdtgm_clean.json (Show: "How Did This Get Made?")
3. tools/dumps/comedy_bang_bang_200_question_trivia_quiz.txt
   -> tools/staging/comedy_bang_bang_clean.json (Show: "Comedy Bang! Bang!")
"""

import json
import re
import sys
from pathlib import Path


def clean_text(text: str) -> str:
    """Clean markdown artifacts, collapse extra whitespace."""
    # Remove leading option labels if mistakenly attached
    text = re.sub(r"^\*{0,2}[A-D]\s*[\)\.\-:]\s*\*{0,2}", "", text)
    # Collapse multiple spaces
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def parse_why_wont_you_date_me(src_path: Path) -> list[dict]:
    """Parse 'Why Won't You Date Me?' 200-question quiz."""
    text = src_path.read_text(encoding="utf-8")

    # Extract answers from [ANSWERS Q...: 1-A, 2-B, ...] blocks
    ans_key: dict[int, int] = {}
    for block in re.findall(r"\[ANSWERS[^\]]*\]", text):
        for m in re.finditer(r"(\d+)\s*[-:]\s*([A-D])", block):
            ans_key[int(m.group(1))] = "ABCD".index(m.group(2).upper())

    if len(ans_key) != 200:
        raise ValueError(f"WYWDM: expected 200 answers, found {len(ans_key)}")

    # Split by PART headers
    part_chunks = re.split(r"={5,}\s*\n\s*(PART\s+\d+:[^\n]+)\n\s*={5,}", text)
    questions: list[dict] = []

    for i in range(1, len(part_chunks), 2):
        sec_header = part_chunks[i].strip()
        sec_m = re.match(r"PART\s+\d+:\s*(.*?)(?:\s*\([^\)]*\))?$", sec_header)
        section = sec_m.group(1).strip().title() if sec_m else sec_header.title()
        content = part_chunks[i + 1]

        # Strip [ANSWERS...] from content
        content = re.sub(r"\[ANSWERS[^\]]*\]", "", content)

        chunks = re.split(r"\n(?=\d+\.\s+)", content)
        for c in chunks:
            c = c.strip()
            if not c:
                continue
            lines = [
                l.strip()
                for l in c.splitlines()
                if l.strip() and not set(l.strip()) <= set("=-_")
            ]
            if not lines:
                continue
            m = re.match(r"^(\d+)\.\s+(.*)", lines[0])
            if not m:
                continue
            qnum = int(m.group(1))
            qlines = [m.group(2).strip()]
            opts: list[str] = []
            for l in lines[1:]:
                opt_m = re.match(r"^\*{0,2}([A-D])\s*[\)\.\-:]\s*\*{0,2}(.*)", l)
                if opt_m:
                    opts.append(clean_text(opt_m.group(2)))
                elif opts:
                    opts[-1] = clean_text(opts[-1] + " " + l)
                else:
                    qlines.append(l)

            q_text = clean_text(" ".join(qlines))
            if len(opts) != 4:
                raise ValueError(f"WYWDM Q{qnum}: expected 4 options, got {len(opts)}")
            if len(set(opts)) != 4:
                raise ValueError(f"WYWDM Q{qnum}: duplicate options: {opts}")
            if qnum not in ans_key:
                raise ValueError(f"WYWDM Q{qnum}: missing answer")

            questions.append({
                "show": "Why Won't You Date Me?",
                "section": section,
                "q": q_text,
                "options": opts,
                "answer": ans_key[qnum],
                "d": 1,
            })

    if len(questions) != 200:
        raise ValueError(f"WYWDM: expected 200 questions, got {len(questions)}")
    return questions


def parse_hdtgm(src_path: Path) -> list[dict]:
    """Parse 'How Did This Get Made?' 200-question quiz."""
    text = src_path.read_text(encoding="utf-8")
    parts = re.split(r"={5,}\s*\n\s*ANSWER KEY\s*\n\s*={5,}", text)
    if len(parts) < 2:
        raise ValueError("HDTGM: missing ANSWER KEY section")
    body, ans_part = parts[0], parts[1]

    # Parse answer key
    ans_key: dict[int, int] = {}
    for m in re.finditer(r"(\d+)\.\s*([A-D])", ans_part):
        ans_key[int(m.group(1))] = "ABCD".index(m.group(2).upper())

    if len(ans_key) != 200:
        raise ValueError(f"HDTGM: expected 200 answers, got {len(ans_key)}")

    # Split body by PART headers
    part_chunks = re.split(r"-{5,}\s*\n\s*(PART\s+\d+:[^\n]+)\n\s*-{5,}", body)
    questions: list[dict] = []

    for i in range(1, len(part_chunks), 2):
        sec_header = part_chunks[i].strip()
        sec_m = re.match(r"PART\s+\d+:\s*(.*?)(?:\s*\([^\)]*\))?$", sec_header)
        section = sec_m.group(1).strip().title() if sec_m else sec_header.title()
        content = part_chunks[i + 1]

        chunks = re.split(r"\n(?=\d+\.\s+)", content)
        for c in chunks:
            c = c.strip()
            if not c:
                continue
            lines = [
                l.strip()
                for l in c.splitlines()
                if l.strip() and not set(l.strip()) <= set("=-_")
            ]
            if not lines:
                continue
            m = re.match(r"^(\d+)\.\s+(.*)", lines[0])
            if not m:
                continue
            qnum = int(m.group(1))
            qlines = [m.group(2).strip()]
            opts: list[str] = []
            for l in lines[1:]:
                opt_m = re.match(r"^\*{0,2}([A-D])\s*[\)\.\-:]\s*\*{0,2}(.*)", l)
                if opt_m:
                    opts.append(clean_text(opt_m.group(2)))
                elif opts:
                    opts[-1] = clean_text(opts[-1] + " " + l)
                else:
                    qlines.append(l)

            q_text = clean_text(" ".join(qlines))
            if len(opts) != 4:
                raise ValueError(f"HDTGM Q{qnum}: expected 4 options, got {len(opts)}")
            if len(set(opts)) != 4:
                raise ValueError(f"HDTGM Q{qnum}: duplicate options: {opts}")
            if qnum not in ans_key:
                raise ValueError(f"HDTGM Q{qnum}: missing answer")

            questions.append({
                "show": "How Did This Get Made?",
                "section": section,
                "q": q_text,
                "options": opts,
                "answer": ans_key[qnum],
                "d": 1,
            })

    if len(questions) != 200:
        raise ValueError(f"HDTGM: expected 200 questions, got {len(questions)}")
    return questions


def parse_comedy_bang_bang(src_path: Path) -> list[dict]:
    """Parse 'Comedy Bang! Bang!' 200-question quiz."""
    text = src_path.read_text(encoding="utf-8")
    parts = re.split(r"={5,}\s*\n\s*ANSWER KEY\s*\n\s*={5,}", text)
    if len(parts) < 2:
        raise ValueError("CBB: missing ANSWER KEY section")
    body, ans_part = parts[0], parts[1]

    # Parse answer key
    ans_key: dict[int, int] = {}
    for m in re.finditer(r"(\d+)\.\s*([A-D])", ans_part):
        ans_key[int(m.group(1))] = "ABCD".index(m.group(2).upper())

    if len(ans_key) != 200:
        raise ValueError(f"CBB: expected 200 answers, got {len(ans_key)}")

    # Split body by SECTION headers
    part_chunks = re.split(r"-{5,}\s*\n\s*(SECTION\s+\d+:[^\n]+)\n\s*-{5,}", body)
    questions: list[dict] = []

    for i in range(1, len(part_chunks), 2):
        sec_header = part_chunks[i].strip()
        sec_m = re.match(r"SECTION\s+\d+:\s*(.*?)(?:\s*\([^\)]*\))?$", sec_header)
        section = sec_m.group(1).strip().title() if sec_m else sec_header.title()
        content = part_chunks[i + 1]

        chunks = re.split(r"\n(?=\d+\.\s+)", content)
        for c in chunks:
            c = c.strip()
            if not c:
                continue
            lines = [
                l.strip()
                for l in c.splitlines()
                if l.strip() and not set(l.strip()) <= set("=-_")
            ]
            if not lines:
                continue
            m = re.match(r"^(\d+)\.\s+(.*)", lines[0])
            if not m:
                continue
            qnum = int(m.group(1))
            qlines = [m.group(2).strip()]
            opts: list[str] = []
            for l in lines[1:]:
                opt_m = re.match(r"^\*{0,2}([A-D])\s*[\)\.\-:]\s*\*{0,2}(.*)", l)
                if opt_m:
                    opts.append(clean_text(opt_m.group(2)))
                elif opts:
                    opts[-1] = clean_text(opts[-1] + " " + l)
                else:
                    qlines.append(l)

            q_text = clean_text(" ".join(qlines))
            if len(opts) != 4:
                raise ValueError(f"CBB Q{qnum}: expected 4 options, got {len(opts)}")
            if len(set(opts)) != 4:
                raise ValueError(f"CBB Q{qnum}: duplicate options: {opts}")
            if qnum not in ans_key:
                raise ValueError(f"CBB Q{qnum}: missing answer")

            questions.append({
                "show": "Comedy Bang! Bang!",
                "section": section,
                "q": q_text,
                "options": opts,
                "answer": ans_key[qnum],
                "d": 1,
            })

    if len(questions) != 200:
        raise ValueError(f"CBB: expected 200 questions, got {len(questions)}")
    return questions


def validate_and_save(questions: list[dict], out_path: Path, expected_show: str):
    """Validate question schema and uniqueness, then write formatted JSON."""
    assert len(questions) == 200, f"Expected 200 questions, found {len(questions)}"
    for idx, q in enumerate(questions, 1):
        assert q["show"] == expected_show, f"Item {idx}: unexpected show {q['show']}"
        assert isinstance(q["q"], str) and q["q"], f"Item {idx}: missing q text"
        assert len(q["options"]) == 4, f"Item {idx}: opts len != 4"
        assert len(set(q["options"])) == 4, f"Item {idx}: duplicate options: {q['options']}"
        assert isinstance(q["answer"], int) and 0 <= q["answer"] < 4, f"Item {idx}: invalid answer index {q['answer']}"
        assert q["d"] == 1, f"Item {idx}: d != 1"
        for opt in q["options"]:
            assert not opt.startswith(("A)", "B)", "C)", "D)")), f"Item {idx}: raw prefix in opt: {opt}"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(questions)} questions to {out_path}")


def main():
    root = Path(__file__).resolve().parent
    dumps_dir = root / "dumps"
    staging_dir = root / "staging"

    targets = [
        (
            dumps_dir / "why_wont_you_date_me_quiz.txt",
            staging_dir / "why_wont_you_date_me_clean.json",
            "Why Won't You Date Me?",
            parse_why_wont_you_date_me,
        ),
        (
            dumps_dir / "hdtgm_200_question_multiple_choice_quiz.txt",
            staging_dir / "hdtgm_clean.json",
            "How Did This Get Made?",
            parse_hdtgm,
        ),
        (
            dumps_dir / "comedy_bang_bang_200_question_trivia_quiz.txt",
            staging_dir / "comedy_bang_bang_clean.json",
            "Comedy Bang! Bang!",
            parse_comedy_bang_bang,
        ),
    ]

    for src, dst, show, parse_fn in targets:
        print(f"\nProcessing {src.name} -> {dst.name} ({show})...")
        qs = parse_fn(src)
        validate_and_save(qs, dst, show)

    print("\nAll podcast trivia dumps parsed and validated successfully!")


if __name__ == "__main__":
    main()
