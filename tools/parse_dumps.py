#!/usr/bin/env python3 -I
"""Parse raw trivia dumps into staging clean JSON."""
import json
import re
import sys
from pathlib import Path

def parse_movie_taglines(src_path: Path) -> list[dict]:
    text = src_path.read_text(encoding="utf-8")
    chunks = re.split(r'\n(?=\d+\.\s*)', text)[1:]
    questions = []
    
    for i, c in enumerate(chunks, 1):
        lines = [l.strip() for l in c.strip().splitlines() if l.strip()]
        num_match = re.match(r'^(\d+)\.\s*(.+)$', lines[0])
        if not num_match:
            raise ValueError(f"Movie taglines chunk {i}: invalid title header line: {lines[0]}")
        
        num = int(num_match.group(1))
        title = num_match.group(2).strip()
        
        opts = []
        ans_idx = None
        for l in lines[1:]:
            opt_match = re.match(r'^([A-D])\)\s*(.+)$', l)
            if opt_match:
                opts.append(opt_match.group(2).strip())
                continue
            ans_match = re.match(r'^Answer:\s*([A-D])\b', l)
            if ans_match:
                ans_idx = "ABCD".index(ans_match.group(1))
                continue
        
        if len(opts) != 4:
            raise ValueError(f"Movie taglines #{num} ({title}): expected 4 options, found {len(opts)}")
        if len(set(opts)) != 4:
            raise ValueError(f"Movie taglines #{num} ({title}): duplicate options: {opts}")
        if ans_idx is None or not (0 <= ans_idx <= 3):
            raise ValueError(f"Movie taglines #{num} ({title}): invalid answer index {ans_idx}")
            
        questions.append({
            "show": "Movie Taglines",
            "q": f"What was the official tagline for {title}?",
            "options": opts,
            "answer": ans_idx,
            "d": 1
        })
        
    return questions

def parse_texas_history(src_path: Path) -> list[dict]:
    text = src_path.read_text(encoding="utf-8")
    chunks = re.split(r'\n(?=\d+\.\s*)', text)[1:]
    questions = []
    
    for i, c in enumerate(chunks, 1):
        lines = [l.strip() for l in c.strip().splitlines() if l.strip()]
        q_lines = []
        opts = []
        ans_idx = None
        mode = "q"
        
        for l in lines:
            opt_match = re.match(r'^([A-D])\.\s*(.+)$', l)
            ans_match = re.match(r'^Answer:\s*([A-D])\b', l)
            if opt_match:
                mode = "opt"
                opts.append(opt_match.group(2).strip())
            elif ans_match:
                mode = "ans"
                ans_idx = "ABCD".index(ans_match.group(1))
            elif mode == "q":
                q_lines.append(l)
                
        q_text = re.sub(r'^\d+\.\s*', '', " ".join(q_lines)).strip()
        if not q_text:
            raise ValueError(f"Texas history chunk {i}: empty question text")
        if len(opts) != 4:
            raise ValueError(f"Texas history #{i}: expected 4 options, found {len(opts)}")
        if len(set(opts)) != 4:
            raise ValueError(f"Texas history #{i}: duplicate options: {opts}")
        if ans_idx is None or not (0 <= ans_idx <= 3):
            raise ValueError(f"Texas history #{i}: invalid answer index {ans_idx}")
            
        questions.append({
            "show": "Texas History",
            "q": q_text,
            "options": opts,
            "answer": ans_idx,
            "d": 1
        })
        
    return questions

def parse_streaming_tv(src_path: Path) -> list[dict]:
    text = src_path.read_text(encoding="utf-8")
    parts = text.split("ANSWER KEY")
    if len(parts) != 2:
        raise ValueError(f"Streaming TV: expected exactly one ANSWER KEY section, found {len(parts) - 1}")
    q_part, ans_part = parts

    answers = {}
    for line in ans_part.splitlines():
        line = line.strip()
        if not line or set(line) <= set("="):
            continue
        m = re.match(r"^(\d+)\.\s*([A-D])\)", line)
        if not m:
            raise ValueError(f"Streaming TV: invalid answer key line: {line}")
        num = int(m.group(1))
        ans_letter = m.group(2)
        answers[num] = "ABCD".index(ans_letter)

    q_part = re.sub(r"^=+\s*STREAMING TV SHOWS TRIVIA QUIZ.*?\n=+\s*", "", q_part, flags=re.DOTALL)
    chunks = re.split(r"\n(?=\d+\.\s*)", q_part.strip())
    questions = []

    for i, c in enumerate(chunks, 1):
        lines = [l.strip() for l in c.strip().splitlines() if l.strip() and not set(l.strip()) <= set("=")]
        num_match = re.match(r"^(\d+)\.\s*(.+)$", lines[0])
        if not num_match:
            raise ValueError(f"Streaming TV chunk {i}: invalid question header: {lines[0]}")
        num = int(num_match.group(1))
        q_text = num_match.group(2).strip()

        opts = []
        for l in lines[1:]:
            opt_match = re.match(r"^([A-D])\)\s*(.+)$", l)
            if opt_match:
                opts.append(opt_match.group(2).strip())
            else:
                raise ValueError(f"Streaming TV #{num}: unrecognized line: {l}")

        if len(opts) != 4:
            raise ValueError(f"Streaming TV #{num}: expected 4 options, found {len(opts)}")
        if len(set(opts)) != 4:
            raise ValueError(f"Streaming TV #{num}: duplicate options: {opts}")
        if num not in answers:
            raise ValueError(f"Streaming TV #{num}: missing from answer key")

        ans_idx = answers[num]
        questions.append({
            "show": "Streaming TV Shows",
            "q": q_text,
            "options": opts,
            "answer": ans_idx,
            "d": 1
        })

    return questions

def parse_famous_canadians(src_path: Path) -> list[dict]:
    text = src_path.read_text(encoding="utf-8")
    text = re.sub(r"^=+\s*FAMOUS CANADIANS.*?\n=+\s*", "", text, flags=re.DOTALL)
    chunks = re.split(r"\n(?=\d+\.\s*)", text.strip())
    questions = []

    for i, c in enumerate(chunks, 1):
        lines = [l.strip() for l in c.strip().splitlines() if l.strip() and not set(l.strip()) <= set("=")]
        num_match = re.match(r"^(\d+)\.\s*(.+)$", lines[0])
        if not num_match:
            raise ValueError(f"Famous Canadians chunk {i}: invalid question header: {lines[0]}")
        num = int(num_match.group(1))
        q_text = num_match.group(2).strip()

        opts = []
        ans_idx = None
        for l in lines[1:]:
            opt_match = re.match(r"^([A-D])\)\s*(.+)$", l)
            ans_match = re.match(r"^Answer:\s*([A-D])\b", l)
            if opt_match:
                opts.append(opt_match.group(2).strip())
            elif ans_match:
                ans_idx = "ABCD".index(ans_match.group(1))
            else:
                raise ValueError(f"Famous Canadians #{num}: unrecognized line: {l}")

        if len(opts) != 4:
            raise ValueError(f"Famous Canadians #{num}: expected 4 options, found {len(opts)}")
        if len(set(opts)) != 4:
            raise ValueError(f"Famous Canadians #{num}: duplicate options: {opts}")
        if ans_idx is None or not (0 <= ans_idx <= 3):
            raise ValueError(f"Famous Canadians #{num}: invalid answer index {ans_idx}")

        questions.append({
            "show": "Famous Canadians",
            "q": q_text,
            "options": opts,
            "answer": ans_idx,
            "d": 1
        })

    return questions

def parse_chuck_norris(src_path: Path) -> list[dict]:
    text = src_path.read_text(encoding="utf-8")
    chunks = re.split(r'\n(?=\d+\.\s*)', text)[1:]
    questions = []

    for i, c in enumerate(chunks, 1):
        lines = [l.strip() for l in c.strip().splitlines() if l.strip() and not l.startswith("=") and "END OF QUIZ" not in l]
        if not lines:
            continue
        num_match = re.match(r'^(\d+)\.\s*(.+)$', lines[0])
        if not num_match:
            raise ValueError(f"Chuck Norris chunk {i}: invalid question header: {lines[0]}")
        num = int(num_match.group(1))

        q_lines = [num_match.group(2).strip()]
        opts = []
        ans_idx = None
        mode = "q"

        for l in lines[1:]:
            opt_match = re.match(r'^([A-D])\)\s*(.+)$', l)
            ans_match = re.match(r'^(?:Correct Answer|Answer):\s*([A-D])\b', l, re.IGNORECASE)
            if opt_match:
                mode = "opt"
                opts.append(opt_match.group(2).strip())
            elif ans_match:
                mode = "ans"
                ans_idx = "ABCD".index(ans_match.group(1).upper())
            elif mode == "q":
                q_lines.append(l)
            else:
                raise ValueError(f"Chuck Norris #{num}: unexpected line: {l}")

        q_text = " ".join(q_lines).strip()
        if len(opts) != 4:
            raise ValueError(f"Chuck Norris #{num}: expected 4 options, found {len(opts)}")
        if len(set(opts)) != 4:
            raise ValueError(f"Chuck Norris #{num}: duplicate options: {opts}")
        if ans_idx is None or not (0 <= ans_idx <= 3):
            raise ValueError(f"Chuck Norris #{num}: invalid answer index: {ans_idx}")

        questions.append({
            "show": "Chuck Norris Jokes",
            "q": q_text,
            "options": opts,
            "answer": ans_idx,
            "d": 1
        })

    return questions

def parse_dont_tell_comedy(batch_paths: list[Path]) -> list[dict]:
    all_questions = []

    for src_path in batch_paths:
        text = src_path.read_text(encoding="utf-8")
        parts = re.split(r'-+\s*\n\s*ANSWER KEY[^\n]*\n\s*-+', text, flags=re.IGNORECASE)
        if len(parts) < 2:
            raise ValueError(f"Don't Tell Comedy: expected ANSWER KEY section in {src_path.name}")
        q_part, ans_part = parts[0], parts[1]

        ans_key = {}
        for line in ans_part.splitlines():
            line = line.strip()
            if not line or set(line) <= set("="):
                continue
            m = re.match(r'^(\d+)\.\s*([A-D])\s*(?:[—–\-:]\s*(.*))?$', line)
            if not m:
                continue
            num = int(m.group(1))
            letter = m.group(2).upper()
            note = m.group(3).strip() if m.group(3) else ""
            ans_key[num] = ("ABCD".index(letter), note)

        chunks = re.split(r'\n(?=\d+\.\s*)', q_part)
        for c in chunks:
            lines = [l.strip() for l in c.strip().splitlines() if l.strip() and not set(l.strip()) <= set("=")]
            if not lines:
                continue
            num_match = re.match(r'^(\d+)\.\s*(.+)$', lines[0])
            if not num_match:
                continue
            num = int(num_match.group(1))

            q_lines = [num_match.group(2).strip()]
            opts = []
            mode = "q"
            for l in lines[1:]:
                opt_match = re.match(r'^([A-D])\)\s*(.+)$', l)
                if opt_match:
                    mode = "opt"
                    opts.append(opt_match.group(2).strip())
                elif mode == "q":
                    q_lines.append(l)
                else:
                    raise ValueError(f"Don't Tell Comedy #{num} in {src_path.name}: unexpected line: {l}")

            q_text = " ".join(q_lines).strip()
            if len(opts) != 4:
                raise ValueError(f"Don't Tell Comedy #{num} in {src_path.name}: expected 4 options, found {len(opts)}")
            if len(set(opts)) != 4:
                raise ValueError(f"Don't Tell Comedy #{num} in {src_path.name}: duplicate options: {opts}")
            if num not in ans_key:
                raise ValueError(f"Don't Tell Comedy #{num} in {src_path.name}: missing from answer key")

            ans_idx, note = ans_key[num]

            fact = None
            if note:
                n_clean = note.strip('"\' ').strip()
                o_clean = opts[ans_idx].strip('"\' ').strip()
                if n_clean.lower() != o_clean.lower():
                    if not (o_clean.lower().startswith(n_clean.lower()) and len(n_clean) < len(o_clean) and '(' not in note and '|' not in note):
                        fact = note

            q_obj = {
                "show": "Don't Tell Comedy",
                "q": q_text,
                "options": opts,
                "answer": ans_idx,
                "d": 1
            }
            if fact:
                q_obj["fact"] = fact
            all_questions.append(q_obj)

    return all_questions

def main():
    root = Path(__file__).resolve().parent.parent
    dumps_dir = root / "tools" / "dumps"
    staging_dir = root / "tools" / "staging"
    staging_dir.mkdir(parents=True, exist_ok=True)
    
    movie_in = dumps_dir / "movie_taglines.txt"
    movie_out = staging_dir / "movie_taglines_clean.json"
    movie_qs = parse_movie_taglines(movie_in)
    with open(movie_out, "w", encoding="utf-8") as f:
        json.dump(movie_qs, f, ensure_ascii=False, indent=1)
    print(f"Saved {len(movie_qs)} questions to {movie_out}")
    
    texas_in = dumps_dir / "texas_history.txt"
    texas_out = staging_dir / "texas_history_clean.json"
    texas_qs = parse_texas_history(texas_in)
    with open(texas_out, "w", encoding="utf-8") as f:
        json.dump(texas_qs, f, ensure_ascii=False, indent=1)
    print(f"Saved {len(texas_qs)} questions to {texas_out}")

    streaming_in = dumps_dir / "streaming_tv_shows_trivia_quiz.txt"
    streaming_out = staging_dir / "streaming_tv_clean.json"
    streaming_qs = parse_streaming_tv(streaming_in)
    with open(streaming_out, "w", encoding="utf-8") as f:
        json.dump(streaming_qs, f, ensure_ascii=False, indent=1)
    print(f"Saved {len(streaming_qs)} questions to {streaming_out}")

    canadians_in = dumps_dir / "famous_canadians_quiz.txt"
    canadians_out = staging_dir / "famous_canadians_clean.json"
    canadians_qs = parse_famous_canadians(canadians_in)
    with open(canadians_out, "w", encoding="utf-8") as f:
        json.dump(canadians_qs, f, ensure_ascii=False, indent=1)
    print(f"Saved {len(canadians_qs)} questions to {canadians_out}")

    chuck_in = dumps_dir / "chuck_norris_jokes_multiple_choice_quiz.txt"
    chuck_out = staging_dir / "chuck_norris_clean.json"
    chuck_qs = parse_chuck_norris(chuck_in)
    with open(chuck_out, "w", encoding="utf-8") as f:
        json.dump(chuck_qs, f, ensure_ascii=False, indent=1)
    print(f"Saved {len(chuck_qs)} questions to {chuck_out}")

    dtc_batches = [
        dumps_dir / "don_t_tell_comedy_youtube_metadata_quiz.txt",
        dumps_dir / "don_t_tell_comedy_youtube_metadata_quiz_batch_2.txt",
        dumps_dir / "don_t_tell_comedy_youtube_metadata_quiz_batch_3.txt",
        dumps_dir / "don_t_tell_comedy_youtube_metadata_quiz_batch_4.txt",
        dumps_dir / "don_t_tell_comedy_youtube_metadata_quiz_batch_5.txt",
        dumps_dir / "don_t_tell_comedy_youtube_metadata_quiz_batch_6.txt",
        dumps_dir / "don_t_tell_comedy_youtube_metadata_quiz_batch_7.txt",
    ]
    dtc_out = staging_dir / "dont_tell_comedy_clean.json"
    dtc_qs = parse_dont_tell_comedy(dtc_batches)
    with open(dtc_out, "w", encoding="utf-8") as f:
        json.dump(dtc_qs, f, ensure_ascii=False, indent=1)
    print(f"Saved {len(dtc_qs)} questions to {dtc_out}")

if __name__ == "__main__":
    main()
