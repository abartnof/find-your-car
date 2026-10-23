#!/usr/bin/env python3 -I
"""Parse and validate Batch C trivia dumps into staging JSON files.

Dumps processed:
1. tools/dumps/don_t_tell_comedy_youtube_transcript_deep_cuts.txt
   -> tools/staging/dont_tell_comedy_deep_cuts_clean.json (Category: "Don't Tell Comedy")
2. tools/dumps/rupaul_s_drag_race_200_question_trivia_quiz.txt
   -> tools/staging/rupaul_clean.json (Category: "RuPaul's Drag Race")
3. tools/dumps/rom_com_trivia_master_quiz.txt
   -> tools/staging/rom_com_clean.json (Category: "Romantic Comedies")
"""
import json
import re
import sys
from pathlib import Path


def parse_dont_tell_comedy_deep_cuts(src_path: Path) -> list[dict]:
    """Parse DTC deep cuts bonus dump (Q301 - Q335) with answer key & notes."""
    text = src_path.read_text(encoding="utf-8")
    parts = re.split(r"-+\s*\n\s*ANSWER KEY[^\n]*\n\s*-+", text, flags=re.IGNORECASE)
    if len(parts) < 2:
        raise ValueError(f"DTC Deep Cuts: expected ANSWER KEY section in {src_path.name}")
    q_part, ans_part = parts[0], parts[1]

    ans_key: dict[int, tuple[int, str]] = {}
    for line in ans_part.splitlines():
        line = line.strip()
        if not line or set(line) <= set("="):
            continue
        m = re.match(r"^(\d+)\.\s*([A-D])\s*(?:[—–\-:]\s*(.*))?$", line)
        if not m:
            continue
        num = int(m.group(1))
        letter = m.group(2).upper()
        note = m.group(3).strip() if m.group(3) else ""
        ans_key[num] = ("ABCD".index(letter), note)

    chunks = re.split(r"\n(?=\d+\.\s*)", q_part)
    questions: list[dict] = []

    for c in chunks:
        lines = [
            l.strip()
            for l in c.strip().splitlines()
            if l.strip() and not set(l.strip()) <= set("=-")
        ]
        if not lines:
            continue
        num_match = re.match(r"^(\d+)\.\s*(.+)$", lines[0])
        if not num_match:
            continue
        num = int(num_match.group(1))

        q_lines = [num_match.group(2).strip()]
        opts: list[str] = []
        for l in lines[1:]:
            opt_match = re.match(r"^([A-D])\)\s*(.+)$", l)
            if opt_match:
                opts.append(opt_match.group(2).strip())
            elif opts:
                opts[-1] += " " + l
            else:
                q_lines.append(l)

        q_text = " ".join(q_lines).strip()
        if len(opts) != 4:
            raise ValueError(f"DTC Deep Cuts #{num}: expected 4 options, found {len(opts)}")
        if len(set(opts)) != 4:
            raise ValueError(f"DTC Deep Cuts #{num}: duplicate options: {opts}")
        if num not in ans_key:
            raise ValueError(f"DTC Deep Cuts #{num}: missing from answer key")

        ans_idx, note = ans_key[num]
        q_obj = {
            "show": "Don't Tell Comedy",
            "q": q_text,
            "options": opts,
            "answer": ans_idx,
            "d": 1,
        }
        if note:
            q_obj["fact"] = note

        questions.append(q_obj)

    return questions


def parse_quiz_with_inline_answers(src_path: Path, show_name: str) -> list[dict]:
    """Parse quiz dump where each question ends with an inline Answer: X line."""
    text = src_path.read_text(encoding="utf-8")
    chunks = re.split(r"\n(?=\d+\.\s*)", text)[1:]
    questions: list[dict] = []

    for i, c in enumerate(chunks, 1):
        lines = [
            l.strip()
            for l in c.strip().splitlines()
            if l.strip() and not set(l.strip()) <= set("=-")
        ]
        if not lines:
            continue
        num_match = re.match(r"^(\d+)\.\s*(.+)$", lines[0])
        if not num_match:
            raise ValueError(f"{show_name} chunk {i}: invalid question header: {lines[0]}")
        num = int(num_match.group(1))

        q_lines = [num_match.group(2).strip()]
        opts: list[str] = []
        ans_idx = None

        for l in lines[1:]:
            opt_match = re.match(r"^([A-D])\)\s*(.+)$", l)
            ans_match = re.match(r"^Answer:\s*([A-D])\b", l, re.IGNORECASE)
            if opt_match:
                opts.append(opt_match.group(2).strip())
            elif ans_match:
                ans_idx = "ABCD".index(ans_match.group(1).upper())
            elif opts:
                opts[-1] += " " + l
            else:
                q_lines.append(l)

        q_text = " ".join(q_lines).strip()
        if len(opts) != 4:
            raise ValueError(f"{show_name} #{num}: expected 4 options, found {len(opts)}")
        if len(set(opts)) != 4:
            raise ValueError(f"{show_name} #{num}: duplicate options: {opts}")
        if ans_idx is None or not (0 <= ans_idx <= 3):
            raise ValueError(f"{show_name} #{num}: invalid answer index: {ans_idx}")

        questions.append({
            "show": show_name,
            "q": q_text,
            "options": opts,
            "answer": ans_idx,
            "d": 1,
        })

    return questions


def validate_dataset(name: str, questions: list[dict]) -> None:
    """Validate question formatting, options, answer bounds, and internal duplicates."""
    seen_qs: set[str] = set()
    for idx, q_obj in enumerate(questions, 1):
        # Required fields
        for field in ("show", "q", "options", "answer", "d"):
            if field not in q_obj:
                raise ValueError(f"{name} item {idx}: missing required field '{field}'")

        if not q_obj["q"].strip():
            raise ValueError(f"{name} item {idx}: empty question string")

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

        # Fact validation
        if "fact" in q_obj:
            if not isinstance(q_obj["fact"], str) or not q_obj["fact"].strip():
                raise ValueError(f"{name} item {idx}: empty or non-string fact: {q_obj['fact']}")


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    dumps_dir = root / "tools" / "dumps"
    staging_dir = root / "tools" / "staging"
    staging_dir.mkdir(parents=True, exist_ok=True)

    # 1. Don't Tell Comedy Deep Cuts
    dtc_in = dumps_dir / "don_t_tell_comedy_youtube_transcript_deep_cuts.txt"
    dtc_out = staging_dir / "dont_tell_comedy_deep_cuts_clean.json"
    dtc_qs = parse_dont_tell_comedy_deep_cuts(dtc_in)
    validate_dataset("Don't Tell Comedy Deep Cuts", dtc_qs)
    with open(dtc_out, "w", encoding="utf-8") as f:
        json.dump(dtc_qs, f, ensure_ascii=False, indent=1)
    print(f"Saved {len(dtc_qs)} questions to {dtc_out}")

    # 2. RuPaul's Drag Race
    rupaul_in = dumps_dir / "rupaul_s_drag_race_200_question_trivia_quiz.txt"
    rupaul_out = staging_dir / "rupaul_clean.json"
    rupaul_qs = parse_quiz_with_inline_answers(rupaul_in, "RuPaul's Drag Race")
    validate_dataset("RuPaul's Drag Race", rupaul_qs)
    with open(rupaul_out, "w", encoding="utf-8") as f:
        json.dump(rupaul_qs, f, ensure_ascii=False, indent=1)
    print(f"Saved {len(rupaul_qs)} questions to {rupaul_out}")

    # 3. Romantic Comedies
    romcom_in = dumps_dir / "rom_com_trivia_master_quiz.txt"
    romcom_out = staging_dir / "rom_com_clean.json"
    romcom_qs = parse_quiz_with_inline_answers(romcom_in, "Romantic Comedies")
    validate_dataset("Romantic Comedies", romcom_qs)
    with open(romcom_out, "w", encoding="utf-8") as f:
        json.dump(romcom_qs, f, ensure_ascii=False, indent=1)
    print(f"Saved {len(romcom_qs)} questions to {romcom_out}")

    print("\n--- Summary Verification ---")
    print(f"1. Don't Tell Comedy Deep Cuts: {len(dtc_qs)} questions (all 35 with 'fact' context notes)")
    print(f"2. RuPaul's Drag Race:         {len(rupaul_qs)} questions")
    print(f"3. Romantic Comedies:          {len(romcom_qs)} questions")
    print(f"Total new staging questions:   {len(dtc_qs) + len(rupaul_qs) + len(romcom_qs)}")


if __name__ == "__main__":
    main()
