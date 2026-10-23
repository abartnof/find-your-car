#!/usr/bin/env python3 -I
"""Parse and validate Ann Zimmerman journalism trivia dump into staging clean JSON."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


SHOW_NAME = "A. Zimmerman, Reporter-at-Large!"


def parse_ann_zimmerman_quiz(src_path: Path) -> list[dict]:
    text = src_path.read_text(encoding="utf-8")
    chunks = re.split(r"\n(?=\d+\.\s*)", text)[1:]
    questions: list[dict] = []

    for i, c in enumerate(chunks, 1):
        lines = [
            l.strip()
            for l in c.strip().splitlines()
            if l.strip() and not set(l.strip()) <= set("=-") and l.strip() != "END OF QUIZ"
        ]
        if not lines:
            continue

        num_match = re.match(r"^(\d+)\.\s*(.+)$", lines[0])
        if not num_match:
            raise ValueError(f"Chunk {i}: invalid question header: {lines[0]}")
        num = int(num_match.group(1))

        q_lines = [num_match.group(2).strip()]
        opts: list[str] = []
        ans_idx = None
        fact = None

        for l in lines[1:]:
            opt_match = re.match(r"^([A-D])\)\s*(.+)$", l)
            ans_match = re.match(r"^Answer:\s*([A-D])\b", l, re.IGNORECASE)
            fact_match = re.match(r"^(?:Note|Fact|Context):\s*(.+)$", l, re.IGNORECASE)

            if opt_match:
                opts.append(opt_match.group(2).strip())
            elif ans_match:
                ans_idx = "ABCD".index(ans_match.group(1).upper())
            elif fact_match:
                fact = fact_match.group(1).strip()
            elif ans_idx is not None:
                # Text following the answer line if any
                if fact:
                    fact += " " + l
                else:
                    fact = l
            elif opts:
                opts[-1] += " " + l
            else:
                q_lines.append(l)

        q_text = " ".join(q_lines).strip()

        if len(opts) != 4:
            raise ValueError(f"Q#{num}: expected 4 options, found {len(opts)}: {opts}")
        if len(set(opts)) != 4:
            raise ValueError(f"Q#{num}: duplicate options: {opts}")
        if ans_idx is None or not (0 <= ans_idx <= 3):
            raise ValueError(f"Q#{num}: invalid answer index: {ans_idx}")

        q_obj = {
            "show": SHOW_NAME,
            "q": q_text,
            "options": opts,
            "answer": ans_idx,
            "d": 1,
        }
        if fact:
            q_obj["fact"] = fact

        questions.append(q_obj)

    return questions


def validate_dataset(name: str, questions: list[dict], expected_count: int = 100) -> None:
    """Validate question formatting, options, answer bounds, uniqueness, and count."""
    if len(questions) != expected_count:
        raise ValueError(f"{name}: expected {expected_count} questions, found {len(questions)}")

    seen_qs: set[str] = set()
    for idx, q_obj in enumerate(questions, 1):
        # Required fields
        for field in ("show", "q", "options", "answer", "d"):
            if field not in q_obj:
                raise ValueError(f"{name} item {idx}: missing required field '{field}'")

        if q_obj["show"] != SHOW_NAME:
            raise ValueError(f"{name} item {idx}: invalid show name: {q_obj['show']}")

        if not isinstance(q_obj["q"], str) or not q_obj["q"].strip():
            raise ValueError(f"{name} item {idx}: empty or non-string question")

        # Ensure question has no leading numbering
        if re.match(r"^\d+\.\s*", q_obj["q"]):
            raise ValueError(f"{name} item {idx}: question text still has number prefix: {q_obj['q']}")

        norm_q = re.sub(r"[^a-z0-9]", "", q_obj["q"].lower())
        if norm_q in seen_qs:
            raise ValueError(f"{name} item {idx}: duplicate question text: {q_obj['q']}")
        seen_qs.add(norm_q)

        # Options validation
        opts = q_obj["options"]
        if not isinstance(opts, list) or len(opts) != 4:
            raise ValueError(f"{name} item {idx}: expected 4 options, found {opts}")
        if len(set(opts)) != 4:
            raise ValueError(f"{name} item {idx}: duplicate options detected: {opts}")
        for opt in opts:
            if not isinstance(opt, str) or not opt.strip():
                raise ValueError(f"{name} item {idx}: invalid/empty option string: {repr(opt)}")
            if re.match(r"^[A-D]\)\s*", opt):
                raise ValueError(f"{name} item {idx}: option still contains prefix: {opt}")

        # Answer validation
        ans = q_obj["answer"]
        if not isinstance(ans, int) or not (0 <= ans <= 3):
            raise ValueError(f"{name} item {idx}: invalid answer index {ans}")

        # Difficulty validation
        if q_obj["d"] != 1:
            raise ValueError(f"{name} item {idx}: expected d=1, found {q_obj['d']}")

        # Fact validation if present
        if "fact" in q_obj:
            if not isinstance(q_obj["fact"], str) or not q_obj["fact"].strip():
                raise ValueError(f"{name} item {idx}: empty or non-string fact: {q_obj['fact']}")


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    src_path = root / "tools" / "dumps" / "ann_zimmerman_journalism_quiz.txt"
    dest_path = root / "tools" / "staging" / "ann_zimmerman_clean.json"

    print(f"Parsing {src_path} ...")
    questions = parse_ann_zimmerman_quiz(src_path)

    print("Validating dataset ...")
    validate_dataset("Ann Zimmerman Journalism Quiz", questions, expected_count=100)

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=1)

    print(f"Successfully saved {len(questions)} validated questions to {dest_path}")


if __name__ == "__main__":
    main()
