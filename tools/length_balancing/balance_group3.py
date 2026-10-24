#!/usr/bin/env python3
"""
Length Balancer for Group 3 (Animation, Movies, Jokes & Pop Culture).

Ensures that the longest option is correct no more than 25.0% of the time
(targeting ~20.5% to 22.0%) for every show in Group 3:
- The Simpsons
- King of the Hill
- Bob's Burgers
- 90s Nickelodeon
- Romantic Comedies
- Movie Taglines
- RuPaul's Drag Race
- Celebrity Anecdotes
- Chuck Norris Jokes
- Knock-Knock Jokes
"""

import json
import os
import re
import copy
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(BASE_DIR, "group3.json")
OUTPUT_PATH = os.path.join(BASE_DIR, "group3_balanced.json")

def get_smart_elongation(show, q_text, opt, min_target_len, seed_idx=0):
    """
    Elongate a false option by adding plausible details, full names,
    realistic qualifiers, or relevant context so that len(result) >= min_target_len.
    """
    q_lower = q_text.lower()
    cleaned = opt.strip()
    
    # Check for quotes if present
    quote_char = None
    if (cleaned.startswith('"') and cleaned.endswith('"')) or (cleaned.startswith("'") and cleaned.endswith("'")):
        quote_char = cleaned[0]
        inner_text = cleaned[1:-1].strip()
    else:
        inner_text = cleaned

    # 1. Pure 4-digit years (e.g. 1999)
    if re.match(r'^\d{4}$', inner_text):
        year = inner_text
        year_templates = [
            f"{year} (inaugural television broadcast season)",
            f"{year} (premiering on prime-time television)",
            f"{year} (celebrated fall television premiere)",
            f"{year} (official network syndication release year)"
        ]
        choice = year_templates[seed_idx % len(year_templates)]
        if len(choice) >= min_target_len:
            return choice
        return f"{year} (officially debuted during prime-time broadcast television programming)"

    # 2. Currency (e.g. $4.95)
    if re.match(r'^\$\d+(\.\d+)?$', inner_text):
        price = inner_text
        price_templates = [
            f"{price} (special chalkboard lunch combo with fries and a soda)",
            f"{price} (regular chalkboard special price with local sales tax)",
            f"{price} (value meal promotion served with hand-cut fries)",
            f"{price} (everyday discount chalkboard special price)"
        ]
        choice = price_templates[seed_idx % len(price_templates)]
        if len(choice) >= min_target_len:
            return choice
        return f"{price} (special chalkboard lunch combo with seasoned fries and beverage included)"

    # 3. Phone numbers (e.g. KL5-4796)
    if re.match(r'^[A-Z0-9]{3}-\d{4}$', inner_text):
        phone_templates = [
            f"{inner_text} (Springfield commercial toll-free dispatch line)",
            f"{inner_text} (direct telephone customer support hotline)",
            f"{inner_text} (emergency dispatch switchboard number)",
            f"{inner_text} (official twenty-four-hour broadcast hotline)"
        ]
        choice = phone_templates[seed_idx % len(phone_templates)]
        if len(choice) >= min_target_len:
            return choice
        return f"{inner_text} (Springfield commercial dispatch line with twenty-four-hour answering service)"

    # 4. Pure small integers
    if re.match(r'^\d+$', inner_text):
        val = inner_text
        if 'room' in q_lower or 'temple' in q_lower:
            return f"{val} interconnected stone obstacle chambers"
        if 'point' in q_lower or 'score' in q_lower:
            return f"{val} total verified points awarded by the judging panel"
        if any(w in q_lower for w in ['win', 'maxi', 'challenge', 'season']):
            return f"{val} consecutive maxi challenge victories on the main stage"
        if any(w in q_lower for w in ['letter', 'envelope', 'page']):
            return f"{val} handwritten, sealed love letters discovered in the attic"
        int_templates = [
            f"{val} separate consecutive recorded victories",
            f"{val} verified independent recorded instances",
            f"{val} officially documented occurrences",
            f"{val} total recognized standard competitions"
        ]
        choice = int_templates[seed_idx % len(int_templates)]
        if len(choice) >= min_target_len:
            return choice
        return f"{val} officially recorded and verified consecutive tournament victories"

    # 5. Shoe size (Peggy Hill)
    if re.match(r'^\d+(\s*1/2)?$', inner_text):
        koth_size_templates = [
            f"Size {inner_text} extra-wide steel-toe comfort fit work boot",
            f"Size {inner_text} orthopedic high-top leather walking shoe",
            f"Size {inner_text} double-wide Texas athletic running shoe",
            f"Size {inner_text} reinforced heavy-duty cowboy work boot"
        ]
        choice = koth_size_templates[seed_idx % len(koth_size_templates)]
        if len(choice) >= min_target_len:
            return choice
        return f"Size {inner_text} reinforced extra-wide steel-toe work boot from Arlen Shoe Outlet"

    # ================= SHOW SPECIFIC LOGIC =================

    if show == 'Chuck Norris Jokes':
        cn_action_templates = [
            f"{inner_text} while roundhouse kicking through solid granite",
            f"{inner_text} without breaking a single drop of sweat",
            f"{inner_text} across three different international time zones",
            f"{inner_text} and staring down a charging mother grizzly bear",
            f"{inner_text} in negative five seconds flat without blinking",
            f"{inner_text} while blindfolded in deep interstellar space",
            f"{inner_text} using only his devastating left eyebrow",
            f"{inner_text} and forcing modern quantum physics to apologize"
        ]
        if inner_text.endswith(('.', '!')):
            base = inner_text[:-1]
            cn_punct_templates = [
                f"{base} while roundhouse kicking through solid granite.",
                f"{base} without breaking a single drop of sweat.",
                f"{base} across three different international time zones.",
                f"{base} and staring down a charging mother grizzly bear.",
                f"{base} in negative five seconds flat without blinking.",
                f"{base} while blindfolded in deep interstellar space."
            ]
            for t in cn_punct_templates[seed_idx % len(cn_punct_templates):] + cn_punct_templates[:seed_idx % len(cn_punct_templates)]:
                if len(t) >= min_target_len:
                    return t
        for t in cn_action_templates[seed_idx % len(cn_action_templates):] + cn_action_templates[:seed_idx % len(cn_action_templates)]:
            if len(t) >= min_target_len:
                return t
        return f"{inner_text} while simultaneously executing a double roundhouse kick through solid granite"

    elif show == 'Knock-Knock Jokes':
        if inner_text.endswith('!'):
            base = inner_text[:-1]
            kk_templates = [
                f"{base} before the bright morning sun comes up!",
                f"{base} and enjoy the wonderful sunny afternoon!",
                f"{base} while everyone in the room is watching!",
                f"{base} down by the cheerful front entrance!",
                f"{base} at the lively neighborhood celebration!",
                f"{base} with all our favorite lifelong friends!"
            ]
        elif inner_text.endswith('?'):
            base = inner_text[:-1]
            kk_templates = [
                f"{base} before it gets completely dark outside?",
                f"{base} across the sunny open backyard garden?",
                f"{base} while we still have plenty of free time?",
                f"{base} with a great big cheerful smile on your face?",
                f"{base} down by the sparkling blue lakeside?"
            ]
        else:
            kk_templates = [
                f"{inner_text} before anyone else even notices",
                f"{inner_text} across the sunny open courtyard patio",
                f"{inner_text} with all of our cheerful favorite neighbors",
                f"{inner_text} right in the middle of the bright afternoon"
            ]
        for t in kk_templates[seed_idx % len(kk_templates):] + kk_templates[:seed_idx % len(kk_templates)]:
            if len(t) >= min_target_len:
                return t
        return f"{inner_text.rstrip('.!?')} and celebrate together with the entire friendly neighborhood!"

    elif show == 'Movie Taglines':
        base = inner_text.rstrip('.')
        tag_templates = [
            f"{base}... in a perilous world where survival is everything.",
            f"{base}... before the shocking truth is revealed to everyone.",
            f"{base}... where fear runs deeper than the darkest ocean waters.",
            f"{base}... and only the bravest heroes will survive the night.",
            f"{base}... when an unspeakable terror awakens from the shadows.",
            f"{base}... because some deadly secrets were never meant to be discovered.",
            f"{base}... in the ultimate high-stakes battle for human survival.",
            f"{base}... where every shadow hides a terrifying new nightmare."
        ]
        for t in tag_templates[seed_idx % len(tag_templates):] + tag_templates[:seed_idx % len(tag_templates)]:
            if len(t) >= min_target_len:
                return t
        return f"{base}... in the ultimate high-stakes cinematic battle for mankind's survival."

    elif show == "RuPaul's Drag Race":
        if 'train' in q_lower:
            return f"{inner_text} (runaway luxury transcontinental bullet train)"
        if any(w in q_lower for w in ['judge', 'guest']):
            return f"{inner_text} (distinguished celebrity guest judge on the main stage)"
        if any(w in q_lower for w in ['queen', 'who won', 'who', 'contestant', 'puppet', 'impersonate']):
            rp_templates = [
                f"{inner_text} (season runner-up and Miss Congeniality recipient)",
                f"{inner_text} (celebrated All Stars finalist and lip sync assassin)",
                f"{inner_text} (legendary Werk Room comedy and fashion superstar)",
                f"{inner_text} (distinguished pageant icon and design challenge victor)",
                f"{inner_text} (beloved international fan favorite and tour headliner)",
                f"{inner_text} (famed runway maven and World of Wonder series host)"
            ]
            for t in rp_templates[seed_idx % len(rp_templates):] + rp_templates[:seed_idx % len(rp_templates)]:
                if len(t) >= min_target_len:
                    return t
            return f"{inner_text} (distinguished Drag Race superstar, All Stars finalist, and lip sync assassin)"
        if any(w in q_lower for w in ['outfit', 'runway', 'dress', 'costume']):
            return f"{inner_text} (elaborate handcrafted couture runway look with sudden reveal)"
        rp_templates = [
            f"{inner_text} (season runner-up and Miss Congeniality recipient)",
            f"{inner_text} (celebrated All Stars finalist and lip sync assassin)",
            f"{inner_text} (legendary Werk Room comedy and fashion superstar)",
            f"{inner_text} (distinguished pageant icon and design challenge victor)",
            f"{inner_text} (beloved international fan favorite and tour headliner)",
            f"{inner_text} (famed runway maven and World of Wonder series host)"
        ]
        for t in rp_templates[seed_idx % len(rp_templates):] + rp_templates[:seed_idx % len(rp_templates)]:
            if len(t) >= min_target_len:
                return t
        return f"{inner_text} (distinguished Drag Race superstar, All Stars finalist, and lip sync assassin)"

    elif show == 'Celebrity Anecdotes':
        if any(w in q_lower for w in ['store', 'shop', 'boutique', 'hotel', 'restaurant', 'venue']):
            celeb_venue_templates = [
                f"{inner_text} flagship luxury boutique on Rodeo Drive in Beverly Hills",
                f"{inner_text} historic high-end department store location in Manhattan",
                f"{inner_text} exclusive luxury flagship department store"
            ]
            for t in celeb_venue_templates[seed_idx % len(celeb_venue_templates):] + celeb_venue_templates[:seed_idx % len(celeb_venue_templates)]:
                if len(t) >= min_target_len:
                    return t
        if len(inner_text.split()) > 3:
            celeb_action_templates = [
                f"{inner_text} while hotel security and eyewitnesses watched in utter disbelief",
                f"{inner_text} during a chaotic live television broadcast recording session",
                f"{inner_text} before making an escape in an unmarked limousine through traffic",
                f"{inner_text} after an intense backstage confrontation with the show producers",
                f"{inner_text} causing thousands of dollars in property damage to the luxury suite"
            ]
            for t in celeb_action_templates[seed_idx % len(celeb_action_templates):] + celeb_action_templates[:seed_idx % len(celeb_action_templates)]:
                if len(t) >= min_target_len:
                    return t
        celeb_templates = [
            f"{inner_text} (Academy Award-winning Hollywood film icon)",
            f"{inner_text} (prolific movie star and veteran character performer)",
            f"{inner_text} (celebrated multi-platinum recording legend and producer)",
            f"{inner_text} (famed Hollywood leading performer and activist)",
            f"{inner_text} (veteran comedy star and frequent late-night television guest)"
        ]
        for t in celeb_templates[seed_idx % len(celeb_templates):] + celeb_templates[:seed_idx % len(celeb_templates)]:
            if len(t) >= min_target_len:
                return t
        return f"{inner_text} (distinguished Academy Award-winning Hollywood star and veteran performer)"

    elif show == 'The Simpsons':
        if any(w in q_lower for w in ['dog', 'cat', 'pet', 'animal', 'adopt']):
            simp_pet_templates = [
                f"{inner_text} (champion pedigree racing greyhound)",
                f"{inner_text} (local Springfield animal shelter rescue)",
                f"{inner_text} (purebred prize-winning show dog)"
            ]
            for t in simp_pet_templates[seed_idx % len(simp_pet_templates):] + simp_pet_templates[:seed_idx % len(simp_pet_templates)]:
                if len(t) >= min_target_len:
                    return t
        if any(w in q_lower for w in ['ingredient', 'drink', 'beer', 'beverage', 'cocktail', 'recipe']):
            simp_drink_templates = [
                f"{inner_text} (secret formula ingredient from Moe's Tavern)",
                f"{inner_text} (popular beverage sold cold at the Kwik-E-Mart)",
                f"{inner_text} (industrial chemical additive from the nuclear plant)"
            ]
            for t in simp_drink_templates[seed_idx % len(simp_drink_templates):] + simp_drink_templates[:seed_idx % len(simp_drink_templates)]:
                if len(t) >= min_target_len:
                    return t
        if any(w in q_lower for w in ['statue', 'monument', 'head', 'sculpture']):
            return f"{inner_text} (historic town square bronze memorial monument)"
        if len(inner_text.split()) > 3:
            simp_action_templates = [
                f"{inner_text} during the annual Springfield Whacking Day festival",
                f"{inner_text} at the Springfield Nuclear Power Plant annual company picnic",
                f"{inner_text} according to an investigative report in the Springfield Shopper",
                f"{inner_text} while Homer was napping peacefully on the living room couch"
            ]
            for t in simp_action_templates[seed_idx % len(simp_action_templates):] + simp_action_templates[:seed_idx % len(simp_action_templates)]:
                if len(t) >= min_target_len:
                    return t
        simpsons_templates = [
            f"{inner_text} (eccentric Springfield Elementary School staff member)",
            f"{inner_text} (frequent longtime customer sitting at Moe's Tavern)",
            f"{inner_text} (Springfield Nuclear Power Plant safety department employee)",
            f"{inner_text} (eccentric lifelong citizen of greater Springfield)",
            f"{inner_text} (veteran Krustylu Studios television cast performer)",
            f"{inner_text} (popular local novelty item purchased at the Kwik-E-Mart)"
        ]
        for t in simpsons_templates[seed_idx % len(simpsons_templates):] + simpsons_templates[:seed_idx % len(simpsons_templates)]:
            if len(t) >= min_target_len:
                return t
        return f"{inner_text} (eccentric longtime resident and beloved citizen of greater Springfield)"

    elif show == 'King of the Hill':
        if len(inner_text.split()) > 3:
            koth_action_templates = [
                f"{inner_text} with clean-burning propane and propane accessories",
                f"{inner_text} while standing in the Rainey Street alley holding an Alamo Beer",
                f"{inner_text} during the annual Heimlich County fair lawnmower races",
                f"{inner_text} as officially certified by the Texas Propane Gas Association"
            ]
            for t in koth_action_templates[seed_idx % len(koth_action_templates):] + koth_action_templates[:seed_idx % len(koth_action_templates)]:
                if len(t) >= min_target_len:
                    return t
        koth_templates = [
            f"{inner_text} (dedicated senior employee at Strickland Propane)",
            f"{inner_text} (lifelong resident of Rainey Street in Arlen, Texas)",
            f"{inner_text} (Hank's longtime varsity high school football teammate)",
            f"{inner_text} (veteran Arlen High School athletic booster club member)",
            f"{inner_text} (prominent Heimlich County civic board member)",
            f"{inner_text} (certified clean-burning propane system specialist)"
        ]
        for t in koth_templates[seed_idx % len(koth_templates):] + koth_templates[:seed_idx % len(koth_templates)]:
            if len(t) >= min_target_len:
                return t
        return f"{inner_text} (dedicated employee at Strickland Propane and longtime Rainey Street resident)"

    elif show == "Bob's Burgers":
        if any(w in q_lower for w in ['address', 'street', 'avenue', 'location']):
            bb_addr_templates = [
                f"{inner_text} (historic seaside storefront located near Wonder Wharf)",
                f"{inner_text} (located directly across the street from Jimmy Pesto's Pizzeria)",
                f"{inner_text} (situated next door to Mort's funeral home on Ocean Avenue)"
            ]
            for t in bb_addr_templates[seed_idx % len(bb_addr_templates):] + bb_addr_templates[:seed_idx % len(bb_addr_templates)]:
                if len(t) >= min_target_len:
                    return t
        if any(w in q_lower for w in ['cat', 'pet', 'animal']):
            return f"{inner_text} (rescued outdoor neighborhood alley cat)"
        if any(w in q_lower for w in ['burger', 'chalkboard', 'menu']):
            return f"{inner_text} served with a side of freshly seasoned hand-cut french fries"
        if len(inner_text.split()) > 3:
            bb_action_templates = [
                f"{inner_text} served with a side of freshly seasoned hand-cut french fries",
                f"{inner_text} performed live on the Wagstaff School auditorium stage",
                f"{inner_text} during the chaotic annual Ocean Avenue lobster festival parade",
                f"{inner_text} while Linda enthusiastically harmonizes in the background"
            ]
            for t in bb_action_templates[seed_idx % len(bb_action_templates):] + bb_action_templates[:seed_idx % len(bb_action_templates)]:
                if len(t) >= min_target_len:
                    return t
        bb_templates = [
            f"{inner_text} (eccentric Ocean Avenue seaside neighborhood resident)",
            f"{inner_text} (staff faculty member at Wagstaff Middle School)",
            f"{inner_text} (veteran employee at the Wonder Wharf family boardwalk)",
            f"{inner_text} (frequent longtime patron dining at Bob's counter)",
            f"{inner_text} (member of the Seymour Bay downtown business council)"
        ]
        for t in bb_templates[seed_idx % len(bb_templates):] + bb_templates[:seed_idx % len(bb_templates)]:
            if len(t) >= min_target_len:
                return t
        return f"{inner_text} (eccentric Ocean Avenue resident and frequent patron at Bob's Burgers)"

    elif show == '90s Nickelodeon':
        if 'rugrats' in q_lower and any(w in q_lower for w in ['who', 'character', 'baby', 'toddler', 'doll', 'name']):
            return f"{inner_text} (curious adventurous toddler from the playpen gang)"
        if 'hey arnold' in q_lower and any(w in q_lower for w in ['who', 'character', 'student', 'girl', 'boy', 'bully', 'name']):
            return f"{inner_text} (regular 4th-grade student at P.S. 118 in Brooklyn)"
        if any(w in q_lower for w in ['doll', 'toy']):
            return f"{inner_text} (vintage collectible fashion doll with accessories)"
        if any(w in q_lower for w in ['guts', 'crag', 'mountain']):
            return f"{inner_text} (artificial rock climbing mountain obstacle in the final round)"
        if 'salute your shorts' in q_lower:
            return f"{inner_text} (camper in Bunk 13 at Camp Anawanna)"
        if 'legends of the hidden temple' in q_lower:
            return f"{inner_text} (ancient stone chamber guarded by Temple Guards)"
        if len(inner_text.split()) > 3:
            nick_action_templates = [
                f"{inner_text} broadcast live from Nickelodeon Studios at Universal Studios",
                f"{inner_text} featured during the Saturday evening SNICK programming lineup",
                f"{inner_text} while getting drenched in gallons of green Nickelodeon slime",
                f"{inner_text} inside the mysterious hidden chambers of Olmec's ancient Temple"
            ]
            for t in nick_action_templates[seed_idx % len(nick_action_templates):] + nick_action_templates[:seed_idx % len(nick_action_templates)]:
                if len(t) >= min_target_len:
                    return t
        nick_templates = [
            f"{inner_text} (classic 90s animated Nicktoon fan-favorite character)",
            f"{inner_text} (regular 4th-grade student at P.S. 118 in Brooklyn)",
            f"{inner_text} (counselor at Camp Anawanna in Salute Your Shorts)",
            f"{inner_text} (recurring ensemble performer on the Nickelodeon sketch stage)",
            f"{inner_text} (eccentric citizen of O-Town in Rocko's Modern Life)"
        ]
        for t in nick_templates[seed_idx % len(nick_templates):] + nick_templates[:seed_idx % len(nick_templates)]:
            if len(t) >= min_target_len:
                return t
        return f"{inner_text} (classic 90s animated Nicktoon fan-favorite character from the golden era)"

    elif show == 'Romantic Comedies':
        if any(w in q_lower for w in ['magazine', 'publication', 'paper', 'article', 'book', 'novel']):
            romcom_pub_templates = [
                f"{inner_text} Magazine (Manhattan editorial office)",
                f"{inner_text} (monthly glossy fashion publication)",
                f"{inner_text} Weekly (lifestyle and culture magazine)"
            ]
            for t in romcom_pub_templates[seed_idx % len(romcom_pub_templates):] + romcom_pub_templates[:seed_idx % len(romcom_pub_templates)]:
                if len(t) >= min_target_len:
                    return t
        if any(w in q_lower for w in ['song', 'sing', 'sung', 'serenade', 'ballad', 'track', 'music']):
            romcom_song_templates = [
                f"{inner_text} (original certified platinum studio track)",
                f"{inner_text} (live acoustic serenade on the bleachers)",
                f"{inner_text} (romantic pop ballad from the film soundtrack)"
            ]
            for t in romcom_song_templates[seed_idx % len(romcom_song_templates):] + romcom_song_templates[:seed_idx % len(romcom_song_templates)]:
                if len(t) >= min_target_len:
                    return t
        if any(w in q_lower for w in ['delicatessen', 'deli', 'restaurant', 'store', 'shop', 'hotel', 'city', 'avenue', 'location', 'live', 'where']):
            romcom_venue_templates = [
                f"{inner_text} (historic Manhattan dining establishment)",
                f"{inner_text} on 7th Avenue in Midtown Manhattan",
                f"{inner_text} near Central Park South in New York City",
                f"{inner_text} (famous Greenwich Village eatery)"
            ]
            for t in romcom_venue_templates[seed_idx % len(romcom_venue_templates):] + romcom_venue_templates[:seed_idx % len(romcom_venue_templates)]:
                if len(t) >= min_target_len:
                    return t
        if len(inner_text.split()) > 3:
            romcom_action_templates = [
                f"{inner_text} right before sprinting through airport gate security in the rain",
                f"{inner_text} during a disastrous, high-society rehearsal dinner meltdown",
                f"{inner_text} culminating in an emotional romantic confession in front of everyone",
                f"{inner_text} while slow dancing beneath the twinkling lights of the Empire State Building"
            ]
            for t in romcom_action_templates[seed_idx % len(romcom_action_templates):] + romcom_action_templates[:seed_idx % len(romcom_action_templates)]:
                if len(t) >= min_target_len:
                    return t
        romcom_templates = [
            f"{inner_text} (acclaimed romantic comedy film starring Meg Ryan)",
            f"{inner_text} (charming eccentric best friend and romantic confidant)",
            f"{inner_text} (wealthy, polished fiancé who turns out to be wrong for her)",
            f"{inner_text} (beloved golden-age classic Hollywood romantic comedy lead)",
            f"{inner_text} (career-focused professional living in a Manhattan brownstone)"
        ]
        for t in romcom_templates[seed_idx % len(romcom_templates):] + romcom_templates[:seed_idx % len(romcom_templates)]:
            if len(t) >= min_target_len:
                return t
        return f"{inner_text} (beloved romantic comedy classic featured across Hollywood film history)"

    # Fallback
    fallback_templates = [
        f"{inner_text} (distinguished pop culture reference and fan favorite)",
        f"{inner_text} (officially recognized across broadcast entertainment history)",
        f"{inner_text} (celebrated benchmark in television and film comedy)"
    ]
    for t in fallback_templates[seed_idx % len(fallback_templates):] + fallback_templates[:seed_idx % len(fallback_templates)]:
        if len(t) >= min_target_len:
            return t
    return f"{inner_text} (distinguished cultural benchmark recognized across entertainment history)"

def balance_group():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)

    print(f"Loaded {len(questions)} questions from {INPUT_PATH}")

    # Group by show
    shows = defaultdict(list)
    for idx, q in enumerate(questions):
        shows[q['show']].append((idx, q))

    # Target percentage: ~21.0%
    TARGET_PCT = 0.210

    balanced_questions = copy.deepcopy(questions)
    total_elongated = 0

    print("\n--- Balancing Shows in Group 3 ---")
    for show_name, show_items in sorted(shows.items()):
        total_q = len(show_items)
        
        # Find which items currently have longest answer correct
        longest_items = []
        for orig_idx, q in show_items:
            opts = q['options']
            ans = q['answer']
            lens = [len(o) for o in opts]
            if lens[ans] == max(lens):
                diff = lens[ans] - max(len(o) for j, o in enumerate(opts) if j != ans)
                longest_items.append((diff, orig_idx, q))

        # Sort by diff ascending so we balance the closest ones first
        longest_items.sort(key=lambda x: x[0])

        current_longest_count = len(longest_items)
        current_pct = (current_longest_count / total_q) * 100
        target_count = int(total_q * TARGET_PCT)
        needed_reductions = max(0, current_longest_count - target_count)

        print(f"Show '{show_name}': {current_longest_count}/{total_q} ({current_pct:.1f}%) -> Target: {target_count} ({TARGET_PCT*100:.1f}%), Needed reductions: {needed_reductions}")

        if needed_reductions <= 0:
            continue

        items_to_modify = longest_items[:needed_reductions]

        modified_count = 0
        for seed, (diff, orig_idx, q) in enumerate(items_to_modify):
            target_q = balanced_questions[orig_idx]
            ans_idx = target_q['answer']
            orig_opts = target_q['options']
            max_len = max(len(o) for o in orig_opts)
            min_target_len = max_len + 6  # strictly exceed by at least 6 chars

            # Pick a false option to elongate: choose the one closest in length
            false_indices = [i for i in range(4) if i != ans_idx]
            false_indices.sort(key=lambda i: len(orig_opts[i]), reverse=True)
            chosen_false_idx = false_indices[seed % min(2, len(false_indices))]
            false_opt = orig_opts[chosen_false_idx]

            # Generate elongated option
            new_opt = get_smart_elongation(show_name, target_q['q'], false_opt, min_target_len, seed_idx=seed)
            
            # Ensure unique and strictly longer
            retry_count = 0
            while (len(new_opt) <= max_len or new_opt in target_q['options']) and retry_count < 25:
                retry_count += 1
                new_opt = get_smart_elongation(show_name, target_q['q'], false_opt, min_target_len + retry_count * 5, seed_idx=seed + retry_count)

            if len(new_opt) <= max_len:
                new_opt = f"{new_opt} (additional verified distinctive detail)"

            # Apply replacement
            target_q['options'][chosen_false_idx] = new_opt

            # Verify
            new_lens = [len(o) for o in target_q['options']]
            assert new_lens[ans_idx] < max(new_lens), f"Failed to elongate: {target_q['options']}"
            assert len(set(target_q['options'])) == 4, f"Options not unique: {target_q['options']}"
            modified_count += 1
            total_elongated += 1

        print(f"  Successfully modified {modified_count} questions for '{show_name}'")

    print(f"\nTotal questions modified across all shows: {total_elongated}")

    # Write output file
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(balanced_questions, f, ensure_ascii=False, indent=0)

    print(f"Saved balanced questions to {OUTPUT_PATH}")

if __name__ == "__main__":
    balance_group()
