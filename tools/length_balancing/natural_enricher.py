import re

CITIES = {
    'Savannah': 'Savannah, Georgia',
    'Macon': 'Macon, Georgia',
    'Athens': 'Athens, Georgia',
    'Paris': 'Paris, France',
    'Florence': 'Florence, Italy',
    'Bermuda': 'Bermuda in the Caribbean',
    'Vermont': 'The rural state of Vermont',
    'Maine': 'The coastal state of Maine',
    'Seattle': 'Seattle, Washington',
    'Boston': 'Boston, Massachusetts',
    'Miami': 'Miami, Florida',
    'Chicago': 'Chicago, Illinois',
    'New York': 'New York City, New York',
    'London': 'London, England',
    'Rome': 'Rome, Italy',
    'Virginia': 'The Commonwealth of Virginia',
    'Bloomer': 'Bloomer, Wisconsin',
    'Fond du Lac': 'Fond du Lac, Wisconsin',
    'Oshkosh': 'Oshkosh, Wisconsin',
    'Eau Claire': 'Eau Claire, Wisconsin'
}

NETWORKS = {
    'CBS': 'CBS Television Network',
    'NBC': 'NBC Universal Television Network',
    'ABC': 'ABC Television Network',
    'UPN': 'UPN Broadcast Network',
    'FOX': 'Fox Broadcasting Company',
    'HBO': 'HBO Premium Cable Network',
    'PBS': 'PBS Public Broadcasting Service',
    'The WB': 'The WB Television Network',
    'Showtime': 'Showtime Premium Cable Network'
}

UNIVERSITIES = {
    'Harvard University': 'Harvard University in Cambridge',
    'Yale University': 'Yale University campus in New Haven',
    'New York University': 'New York University (NYU) in Manhattan',
    'Columbia University': 'Columbia University campus in New York',
    'Princeton University': 'Princeton University campus in New Jersey',
    'Cornell University': 'Cornell University in upstate New York',
    'Dartmouth College': 'Dartmouth College campus in New Hampshire'
}

def natural_elongate(w, q_text, c_text):
    needed_len = len(c_text) + 2
    q_low = q_text.lower()

    # Exact overrides
    if w in NETWORKS:
        res = NETWORKS[w]
        if len(res) >= needed_len:
            return res
        return f"{res} broadcast affiliate"
    if w in CITIES:
        res = CITIES[w]
        if len(res) >= needed_len:
            return res
        return f"{res} metropolitan area"
    if w in UNIVERSITIES:
        res = UNIVERSITIES[w]
        if len(res) >= needed_len:
            return res
        return f"{res} academic campus"

    # Numbers / percentages / money
    if re.match(r'^\$[\d,]+(\.\d+)?$', w):
        res = f"{w} in crisp cash bills"
        if len(res) >= needed_len: return res
        return f"{w} in unmarked twenty-dollar cash bills"

    if re.match(r'^\d+%$', w):
        res = f"{w} of surveyed respondents"
        if len(res) >= needed_len: return res
        return f"{w} of all surveyed television viewers"

    if re.match(r'^\d+$', w):
        if 'jersey' in q_low or 'number' in q_low:
            res = f"Uniform jersey number {w}"
            if len(res) >= needed_len: return res
            return f"Official uniform jersey number #{w}"
        elif 'season' in q_low:
            res = f"Season {w} (original broadcast)"
            if len(res) >= needed_len: return res
            return f"Season {w} (full syndicated broadcast run)"
        elif 'episode' in q_low:
            res = f"Episode {w} (primetime cut)"
            if len(res) >= needed_len: return res
            return f"Episode {w} (extended primetime broadcast)"
        elif 'year' in q_low or 'when' in q_low:
            res = f"The calendar year {w}"
            if len(res) >= needed_len: return res
            return f"The {w} television broadcast season"
        elif 'age' in q_low or 'old' in q_low:
            res = f"{w} years old at the time"
            if len(res) >= needed_len: return res
            return f"Exactly {w} years of age at the time"
        else:
            res = f"A verified total of {w}"
            if len(res) >= needed_len: return res
            return f"A verified documented total of {w}"

    # Year / Season / Dates
    m_season = re.match(r'^(Fall|Spring|Summer|Winter)\s+(\d{4})$', w)
    if m_season:
        res = f"{m_season.group(1)} {m_season.group(2)} broadcast season"
        if len(res) >= needed_len: return res
        return f"{m_season.group(1)} {m_season.group(2)} primetime television season"

    if re.match(r'^(19\d\d|20\d\d)$', w):
        res = f"The {w} broadcast year"
        if len(res) >= needed_len: return res
        return f"The {w} primetime television season"

    if re.match(r'^(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d+(st|nd|rd|th)?$', w):
        res = f"{w} (holiday celebration)"
        if len(res) >= needed_len: return res
        return f"{w} (annual holiday celebration)"

    # 'X years' / 'X episodes' / 'X nominations' / 'X months' / 'X years old'
    if re.match(r'^\d+\s+years\s+old$', w, re.I):
        res = f"{w} at the time of filming"
        if len(res) >= needed_len: return res
        return f"Approximately {w} at the time of filming"

    m_num_unit = re.match(r'^(\d+)\s+([a-zA-Z]+)$', w)
    if m_num_unit:
        res = f"A total of {w} overall"
        if len(res) >= needed_len: return res
        return f"A verified total of {w} overall"

    # Quotes
    if (w.startswith('"') and w.endswith('"')) or (w.startswith("'") and w.endswith("'")):
        quote = w[0]
        inner = w[1:-1].strip()
        if inner.startswith('...'):
            res = f"{quote}{inner} and never look back.{quote}"
            if len(res) >= needed_len: return res
            return f"{quote}{inner} and never look back for even a single second.{quote}"
        elif inner.endswith('!'):
            res = f"{quote}{inner[:-1]} with pure conviction!{quote}"
            if len(res) >= needed_len: return res
            return f"{quote}{inner[:-1]} with complete and pure conviction!{quote}"
        elif inner.endswith('?'):
            res = f"{quote}{inner[:-1]} right at this moment?{quote}"
            if len(res) >= needed_len: return res
            return f"{quote}{inner[:-1]} right now at this exact moment in time?{quote}"
        elif inner.endswith('.'):
            res = f"{quote}{inner[:-1]} without a doubt.{quote}"
            if len(res) >= needed_len: return res
            return f"{quote}{inner[:-1]} with absolute and complete certainty.{quote}"
        else:
            res = f"{quote}{inner} (full version){quote}"
            if len(res) >= needed_len: return res
            return f"{quote}{inner} (complete uncut extended broadcast version){quote}"

    # Asterisks
    if w.startswith('*') and w.endswith('*'):
        inner = w[1:-1]
        res = f"*{inner}: Extended Cut*"
        if len(res) >= needed_len: return res
        return f"*{inner}: The Complete Extended Television Cut*"

    # Parenthetical in w
    m_paren = re.match(r'^(.*?)\s*\((.*?)\)$', w)
    if m_paren:
        base, inside = m_paren.group(1), m_paren.group(2)
        res = f"{base} ({inside}, full cut)"
        if len(res) >= needed_len: return res
        res = f"{base} ({inside}, extended broadcast television cut)"
        if len(res) >= needed_len: return res
        return f"{base} ({inside}, complete uncut extended broadcast edition)"

    # If c_text has parenthetical and w doesn't
    if '(' in c_text and c_text.endswith(')') and not ('(' in w and ')' in w):
        m_c = re.search(r'\((.*?)\)$', c_text)
        c_inside = m_c.group(1) if m_c else ""
        if re.search(r'\b(19\d\d|20\d\d)\b', c_inside):
            paren = "(original broadcast run)"
        elif re.search(r'\b(played by|star of|as |guest)\b', c_inside, re.I):
            paren = "(in a guest starring appearance)"
        elif any(k in q_low for k in ['actress', 'actor', 'played', 'who']):
            paren = "(recurring guest performer)"
        else:
            paren = "(extended broadcast detail)"
            
        res = f"{w} {paren}"
        if len(res) >= needed_len: return res
        res = f"{w} (featured extended broadcast appearance)"
        if len(res) >= needed_len: return res
        return f"{w} (fully verified by series production archives)"

    # Animals / Pets
    if any(k in q_low for k in ['dog', 'corgi', 'cat', 'pet', 'primate', 'animal', 'monkey']):
        if re.match(r'^[A-Z][a-z]+$', w): # e.g. 'Biscuit', 'Gouda'
            res = f"{w} the beloved pet dog"
            if len(res) >= needed_len: return res
            return f"{w} the prize-winning purebred show dog"
        else:
            res = f"{w} with full pedigree papers"
            if len(res) >= needed_len: return res
            return f"A purebred {w.lower()} with certified pedigree papers"

    # Actions: 'To ...'
    if w.startswith('To '):
        res = f"{w} once and for all"
        if len(res) >= needed_len: return res
        res = f"{w} and settle the score once and for all"
        if len(res) >= needed_len: return res
        return f"{w} and definitively avoid any further complications"

    # Verb-ing
    if re.match(r'^[A-Z][a-z]+ing\b', w):
        res = f"Constantly {w[0].lower() + w[1:]}"
        if len(res) >= needed_len: return res
        res = f"Secretly {w[0].lower() + w[1:]} behind closed doors"
        if len(res) >= needed_len: return res
        return f"Repeatedly {w[0].lower() + w[1:]} without anyone in the building knowing"

    # Articles: 'A ', 'An ', 'The '
    if w.startswith('A '):
        rest = w[2:]
        res = f"A brand new {rest}"
        if len(res) >= needed_len: return res
        res = f"A vintage collectible {rest}"
        if len(res) >= needed_len: return res
        return f"A rare, authentic, and certified vintage {rest}"

    if w.startswith('An '):
        rest = w[3:]
        res = f"An expensive {rest}"
        if len(res) >= needed_len: return res
        res = f"An authentic vintage {rest}"
        if len(res) >= needed_len: return res
        return f"An authentic, certified, and documented vintage {rest}"

    if w.startswith('The '):
        rest = w[4:]
        res = f"The prestigious {rest}"
        if len(res) >= needed_len: return res
        res = f"The renowned {rest} of the city"
        if len(res) >= needed_len: return res
        return f"The celebrated and historic {rest} of the city"

    # Proper names: First + Last (e.g. 'Stephen Baldwin', 'Billy Porter', 'Craig Dixon')
    if re.match(r'^[A-Z][a-zA-Z\.\'\-]+ [A-Z][a-zA-Z\.\'\-]+$', w):
        if any(k in q_low for k in ['actor', 'actress', 'played', 'star', 'who', 'guest', 'performer']):
            res = f"Actor {w}"
            if len(res) >= needed_len: return res
            res = f"Veteran performer {w}"
            if len(res) >= needed_len: return res
            return f"Acclaimed veteran actor {w} (credited guest appearance)"
        elif any(k in q_low for k in ['author', 'writer', 'creator', 'director']):
            res = f"Noted author {w}"
            if len(res) >= needed_len: return res
            return f"Prominent screenwriter {w} (credited writer)"
        elif any(re.search(rf'\b{k}\b', q_low) for k in ['character', 'friend', 'brother', 'boyfriend', 'husband', 'wife', 'girlfriend']):
            res = f"{w} (close acquaintance)"
            if len(res) >= needed_len: return res
            return f"{w} (frequent family acquaintance)"
        else:
            res = f"{w} (senior associate)"
            if len(res) >= needed_len: return res
            return f"{w} (notable recurring figure)"

    # Single capitalized word (name or item)
    if re.match(r'^[A-Z][a-zA-Z\.\'\-]+$', w):
        if any(re.search(rf'\b{k}\b', q_low) for k in ['brother', 'boyfriend', 'husband', 'son', 'father', 'guy', 'man']):
            res = f"{w} (longtime friend)"
            if len(res) >= needed_len: return res
            return f"{w} (longtime family acquaintance)"
        elif any(re.search(rf'\b{k}\b', q_low) for k in ['sister', 'girlfriend', 'wife', 'daughter', 'mother', 'woman']):
            res = f"{w} (close confidante)"
            if len(res) >= needed_len: return res
            return f"{w} (trusted close confidante)"
        elif any(k in q_low for k in ['instrument', 'play', 'music']):
            res = f"Classical {w.lower()} music"
            if len(res) >= needed_len: return res
            return f"Classical orchestral {w.lower()}"
        elif any(k in q_low for k in ['health', 'ailment', 'condition', 'disease', 'illness', 'syndrome']):
            res = f"Acute {w.lower()} condition"
            if len(res) >= needed_len: return res
            res = f"A severe case of acute {w.lower()}"
            if len(res) >= needed_len: return res
            return f"A severe diagnosed case of acute {w.lower()}"
        else:
            res = f"{w} (official selection)"
            if len(res) >= needed_len: return res
            return f"{w} (official commemorative broadcast edition)"

    # General phrase fallback
    clean_w = w.rstrip('.,;:')
    res = f"{clean_w} in every detail"
    if len(res) >= needed_len: return res
    res = f"{clean_w} according to official records"
    if len(res) >= needed_len: return res
    res = f"{clean_w} according to documented production records"
    if len(res) >= needed_len: return res
    return f"{clean_w} (verified by official network television archives)"

print("Natural enricher v2 loaded")
