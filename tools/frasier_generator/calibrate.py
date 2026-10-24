import re

def calibrate_batch(raw_questions):
    """
    Ensure exactly 30 d1, 40 d2, 30 d3 per batch of 100 questions.
    Score questions by 'hardness' factors:
    - contains specific dates, years, numbers, obscure names, quotes, technical details.
    """
    scores = []
    hard_words = [
        "which year", "in what year", "how many", "approximately how much",
        "specific", "technique", "autobiography", "peabody", "wga", "dga",
        "emmy", "tony", "golden globe", "quote", "latin", "german", "klingon",
        "château", "bordeaux", "mercedes", "steinway", "wassily", "chihuly",
        "director", "composer", "lyricist", "guest-starred", "guest star",
        "steppenwolf", "juilliard", "yale", "flight 11", "trainer", "moose",
        "enzo", "angell", "keenan", "burrows", "soundstage", "syndication",
        "derek", "manu", "clint", "esteban", "tewksbury", "blaine", "alastair", "alistair"
    ]
    easy_words = [
        "catchphrase", "what is the name of", "who serves as", "what dog breed",
        "what brand of beer", "what city", "what is frasier's", "niles crane",
        "daphne moon", "martin crane", "eddie", "kacl", "space needle", "sherry",
        "cheers", "brother", "father", "ex-wife", "psychiatrist"
    ]

    for idx, q in enumerate(raw_questions):
        text = (q["q"] + " " + q["correct"]).lower()
        score = 0
        for w in hard_words:
            if w in text:
                score += 2
        for w in easy_words:
            if w in text:
                score -= 1
        # preserve current hint
        curr_d = q.get("d", 2)
        score += (curr_d - 2) * 2
        scores.append((score, idx))

    scores.sort(key=lambda x: x[0])
    # lowest 30 -> d=1
    # middle 40 -> d=2
    # top 30 -> d=3
    for rank, (score, idx) in enumerate(scores):
        if rank < 30:
            raw_questions[idx]["d"] = 1
        elif rank < 70:
            raw_questions[idx]["d"] = 2
        else:
            raw_questions[idx]["d"] = 3

    return raw_questions
