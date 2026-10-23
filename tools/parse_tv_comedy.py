#!/usr/bin/env python3
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUMPS_DIR = os.path.join(ROOT, "tools", "dumps")
STAGING_DIR = os.path.join(ROOT, "tools", "staging")

LETTER_TO_INDEX = {"A": 0, "B": 1, "C": 2, "D": 3}


def parse_bobs_burgers():
    path = os.path.join(DUMPS_DIR, "bob_s_burgers_300_question_trivia_quiz.txt")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    ans_idx = text.rfind("ANSWER KEY")
    if ans_idx == -1:
        raise ValueError("Could not find ANSWER KEY in Bob's Burgers")
    q_text = text[:ans_idx]
    ans_text = text[ans_idx:]

    ans_dict = {
        int(k): LETTER_TO_INDEX[v]
        for k, v in re.findall(r"(\d+)\.\s*([A-D])\b", ans_text)
    }
    if len(ans_dict) != 300:
        raise ValueError(f"Expected 300 answers for Bob's Burgers, found {len(ans_dict)}")

    lines = q_text.splitlines()
    questions = []
    current_sec = None
    current_q_num = None
    current_q_str = None
    current_opts = {}

    def commit_q():
        if current_q_num is None:
            return
        if len(current_opts) != 4 or set(current_opts.keys()) != {"A", "B", "C", "D"}:
            raise ValueError(f"Q{current_q_num} does not have exactly 4 options: {current_opts}")
        opts = [current_opts[k] for k in ["A", "B", "C", "D"]]
        if len(set(opts)) != 4:
            raise ValueError(f"Q{current_q_num} has duplicate options: {opts}")
        if current_q_num not in ans_dict:
            raise ValueError(f"Q{current_q_num} not found in answer key")

        item = {
            "show": "Bob's Burgers",
            "section": current_sec,
            "q": current_q_str,
            "options": opts,
            "answer": ans_dict[current_q_num],
            "d": 1,
        }
        questions.append(item)

    for line in lines:
        ls = line.strip()
        if not ls:
            continue
        sm = re.match(r"^---\s*(SECTION\s*\d+:?\s*[^-\n\r]+?)\s*---", ls)
        if sm:
            # Clean section name
            sec_name = re.sub(r"^SECTION\s*\d+:\s*", "", sm.group(1)).strip()
            current_sec = sec_name.title()
            continue

        qm = re.match(r"^(\d+)\.\s*(.*)", ls)
        if qm:
            commit_q()
            current_q_num = int(qm.group(1))
            current_q_str = qm.group(2).strip()
            current_opts = {}
            continue

        om = re.match(r"^([A-D])[\)\.]\s*(.*)", ls)
        if om and current_q_num is not None:
            current_opts[om.group(1)] = om.group(2).strip()
            continue

    commit_q()

    if len(questions) != 300:
        raise ValueError(f"Expected 300 questions for Bob's Burgers, parsed {len(questions)}")

    out_path = os.path.join(STAGING_DIR, "bobs_burgers_clean.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=1, ensure_ascii=False)
    print(f"Successfully wrote {len(questions)} Bob's Burgers questions to {out_path}")
    return questions


def parse_90s_nickelodeon():
    path = os.path.join(DUMPS_DIR, "90s_nickelodeon_trivia_bank_300_questions.txt")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    ans_idx = text.find("PART II: ANSWER KEY")
    if ans_idx == -1:
        raise ValueError("Could not find PART II: ANSWER KEY in 90s Nickelodeon")
    q_text = text[:ans_idx]
    ans_text = text[ans_idx:]

    ans_raw = re.findall(r"(?m)^(\d+)\.\s*([A-D])\s*-\s*(.*)", ans_text)
    if len(ans_raw) != 300:
        raise ValueError(f"Expected 300 answers for 90s Nickelodeon, found {len(ans_raw)}")

    ans_dict = {}
    for q_num_s, letter, fact in ans_raw:
        ans_dict[int(q_num_s)] = (LETTER_TO_INDEX[letter], fact.strip())

    lines = q_text.splitlines()
    questions = []
    current_q_num = None
    current_q_str = None
    current_opts = {}

    def commit_q():
        if current_q_num is None:
            return
        if len(current_opts) != 4 or set(current_opts.keys()) != {"A", "B", "C", "D"}:
            raise ValueError(f"Q{current_q_num} does not have exactly 4 options: {current_opts}")
        opts = [current_opts[k] for k in ["A", "B", "C", "D"]]
        if len(set(opts)) != 4:
            raise ValueError(f"Q{current_q_num} has duplicate options: {opts}")
        if current_q_num not in ans_dict:
            raise ValueError(f"Q{current_q_num} not found in answer key")

        ans_idx_val, fact_text = ans_dict[current_q_num]
        item = {
            "show": "90s Nickelodeon",
            "q": current_q_str,
            "options": opts,
            "answer": ans_idx_val,
            "d": 1,
            "fact": fact_text,
        }
        questions.append(item)

    for line in lines:
        ls = line.strip()
        if not ls:
            continue
        qm = re.match(r"^(\d+)\.\s*(.*)", ls)
        if qm:
            commit_q()
            current_q_num = int(qm.group(1))
            current_q_str = qm.group(2).strip()
            current_opts = {}
            continue

        om = re.match(r"^([A-D])[\)\.]\s*(.*)", ls)
        if om and current_q_num is not None:
            current_opts[om.group(1)] = om.group(2).strip()
            continue

    commit_q()

    if len(questions) != 300:
        raise ValueError(f"Expected 300 questions for 90s Nickelodeon, parsed {len(questions)}")

    out_path = os.path.join(STAGING_DIR, "nickelodeon_90s_clean.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=1, ensure_ascii=False)
    print(f"Successfully wrote {len(questions)} 90s Nickelodeon questions to {out_path}")
    return questions


def parse_knock_knock():
    path = os.path.join(DUMPS_DIR, "knock_knock_joke_quiz.txt")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    ans_idx = text.rfind("ANSWER KEY")
    if ans_idx == -1:
        raise ValueError("Could not find ANSWER KEY in Knock Knock Jokes")
    q_text = text[:ans_idx]
    ans_text = text[ans_idx:]

    ans_dict = {
        int(k): LETTER_TO_INDEX[v]
        for k, v in re.findall(r"(\d+)\.\s*([A-D])\b", ans_text)
    }
    if len(ans_dict) != 300:
        raise ValueError(f"Expected 300 answers for Knock Knock Jokes, found {len(ans_dict)}")

    lines = q_text.splitlines()
    questions = []
    current_q_num = None
    current_q_str = None
    current_opts = {}

    def commit_q():
        if current_q_num is None:
            return
        if len(current_opts) != 4 or set(current_opts.keys()) != {"A", "B", "C", "D"}:
            raise ValueError(f"Q{current_q_num} does not have exactly 4 options: {current_opts}")
        opts = [current_opts[k] for k in ["A", "B", "C", "D"]]
        if len(set(opts)) != 4:
            raise ValueError(f"Q{current_q_num} has duplicate options: {opts}")
        if current_q_num not in ans_dict:
            raise ValueError(f"Q{current_q_num} not found in answer key")

        item = {
            "show": "Knock-Knock Jokes",
            "q": current_q_str,
            "options": opts,
            "answer": ans_dict[current_q_num],
            "d": 1,
        }
        questions.append(item)

    for line in lines:
        ls = line.strip()
        if not ls:
            continue
        qm = re.match(r"^(\d+)\.\s*(.*)", ls)
        if qm:
            commit_q()
            current_q_num = int(qm.group(1))
            current_q_str = qm.group(2).strip()
            current_opts = {}
            continue

        om = re.match(r"^([A-D])[\)\.]\s*(.*)", ls)
        if om and current_q_num is not None:
            current_opts[om.group(1)] = om.group(2).strip()
            continue

    commit_q()

    if len(questions) != 300:
        raise ValueError(f"Expected 300 questions for Knock Knock Jokes, parsed {len(questions)}")

    out_path = os.path.join(STAGING_DIR, "knock_knock_clean.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=1, ensure_ascii=False)
    print(f"Successfully wrote {len(questions)} Knock Knock questions to {out_path}")
    return questions


def main():
    os.makedirs(STAGING_DIR, exist_ok=True)
    parse_bobs_burgers()
    parse_90s_nickelodeon()
    parse_knock_knock()
    print("All quizzes parsed successfully!")


if __name__ == "__main__":
    main()
