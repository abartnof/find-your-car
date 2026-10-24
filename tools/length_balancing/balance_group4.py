#!/usr/bin/env python3
"""
Length Balancer for Group 4 (History, Food, Places & Music).

Ensures that the longest option is correct no more than 25.0% of the time
(targeting ~21.0% to 22.5%) for every show in Group 4:
- Billboard Hits
- Ingredients
- Fruits & Veggies
- Texas History
- Dallas
- UT Austin
- Famous Canadians
- Anglophone Slang
- A. Zimmerman, Reporter-at-Large!
- Ben Folds
"""

import json
import os
import re
import copy
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(BASE_DIR, "group4.json")
OUTPUT_PATH = os.path.join(BASE_DIR, "group4_balanced.json")

def get_contextual_elongation(show, q_text, opt, min_target_len, seed_idx=0):
    """
    Produce a context-aware, factually sound, and grammatically natural elongation of false option `opt`
    so that len(result) >= min_target_len.
    """
    cleaned = opt.strip()
    q_lower = q_text.lower()
    
    # Preserve quotes if title in quotes
    quote_char = None
    if (cleaned.startswith('"') and cleaned.endswith('"')) or (cleaned.startswith("'") and cleaned.endswith("'")):
        quote_char = cleaned[0]
        inner = cleaned[1:-1].strip()
    else:
        inner = cleaned

    # 1. 4-digit years (e.g. 1901, 1871, 1886)
    if re.match(r'^\d{4}$', inner):
        year = inner
        if 'open' in q_lower or 'door' in q_lower or 'found' in q_lower or 'charter' in q_lower:
            y_opts = [
                f"{year} (inaugural legislative charter session)",
                f"{year} (fall administrative opening)",
                f"{year} (statewide constitutional convention)",
                f"{year} (interim municipal governance charter)"
            ]
        elif 'fire' in q_lower or 'burn' in q_lower or 'destroy' in q_lower:
            y_opts = [
                f"{year} (major municipal downtown fire)",
                f"{year} (severe commercial district blaze)",
                f"{year} (great town square fire disaster)"
            ]
        elif 'fair' in q_lower or 'expo' in q_lower:
            y_opts = [
                f"{year} (inaugural North Texas agricultural exposition)",
                f"{year} (first regional industrial exhibition)",
                f"{year} (grand opening celebration fair)"
            ]
        elif 'sec' in q_lower or 'conference' in q_lower or 'league' in q_lower:
            y_opts = [
                f"{year} (initial conference realignment vote)",
                f"{year} (formal membership announcement session)",
                f"{year} (preliminary athletic conference agreement)"
            ]
        elif 'network' in q_lower or 'espn' in q_lower or 'launch' in q_lower:
            y_opts = [
                f"{year} (initial television network development)",
                f"{year} (early broadcast programming negotiations)",
                f"{year} (regional telecast launch announcement)"
            ]
        elif 'hand sign' in q_lower or 'hook' in q_lower:
            y_opts = [
                f"{year} (student rally introduction)",
                f"{year} (varsity football game tradition)",
                f"{year} (campus spirit organization adoption)"
            ]
        else:
            y_opts = [
                f"{year} (inaugural legislative charter session)",
                f"{year} (fall administrative reorganization)",
                f"{year} (regional constitutional convention)",
                f"{year} (interim municipal governance)",
                f"{year} (official statewide proclamation)"
            ]
        choice = y_opts[seed_idx % len(y_opts)]
        if len(choice) >= min_target_len:
            return choice
        return f"{choice} (ratified during the regular legislative assembly)"

    # 2. Pure integers (e.g. 2, 4, 6)
    if re.match(r'^\d+$', inner):
        num = inner
        if 'musician' in q_lower or 'band' in q_lower or 'member' in q_lower:
            return f"{num} musicians (performing as a full ensemble)"
        elif 'championship' in q_lower or 'title' in q_lower or 'national' in q_lower:
            return f"{num} consensus varsity national championships"
        elif 'storey' in q_lower or 'floor' in q_lower:
            return f"{num} continuous above-ground architectural storeys"
        else:
            return f"{num} verified separate historical instances"

    # 3. Heights / Distances (e.g. 357 feet)
    if re.match(r'^\d+\s*feet$', inner, re.IGNORECASE):
        ft_opts = [
            f"Approximately {inner} from plaza pavement to the highest decorative spire",
            f"Measuring {inner} in total architectural height from plaza level to spire",
            f"Roughly {inner} from the foundation base to the upper observation deck"
        ]
        choice = ft_opts[seed_idx % len(ft_opts)]
        if len(choice) >= min_target_len:
            return choice
        return f"Approximately {inner} in total structural height from ground plaza to tower summit"

    # 4. Animal mascots
    if inner in ('A Bison', 'A Mustang', 'An Armadillo') or ('mascot' in q_lower and 'animal' in q_lower):
        animal_map = {
            'A Bison': 'A wild North American plains bison (buffalo)',
            'A Mustang': 'A free-roaming North American wild Mustang',
            'An Armadillo': 'A native Texas nine-banded armadillo'
        }
        if inner in animal_map:
            res = animal_map[inner]
            if len(res) >= min_target_len:
                return res
            return f"{res} native to the region"

    # 5. Cities / Towns
    if inner in ('Raleigh', 'Charlotte', 'Durham') or ('town' in q_lower and 'formed' in q_lower):
        city_map = {
            'Raleigh': 'Raleigh (capital city of North Carolina)',
            'Charlotte': 'Charlotte (Queen City of North Carolina)',
            'Durham': 'Durham (home of Duke University and the Bulls)'
        }
        if inner in city_map:
            res = city_map[inner]
            if len(res) >= min_target_len:
                return res
            return f"{res} in the Piedmont region"

    # 6. Colors (UT Austin)
    if 'color' in q_lower and show == 'UT Austin':
        color_map = {
            'Crimson and gray': 'Deep crimson and varsity slate gray',
            'Orange and blue': 'Bright collegiate orange and royal navy blue',
            'Maroon and gold': 'Deep Texas maroon and metallic golden yellow'
        }
        if inner in color_map:
            res = color_map[inner]
            if len(res) >= min_target_len:
                return res
            return f"{res} athletic school colors"

    # 7. Railroads
    if 'railroad' in q_lower or inner in ('Santa Fe', 'Union Pacific', 'Katy Railroad'):
        rr_map = {
            'Santa Fe': 'Atchison, Topeka and Santa Fe Railway',
            'Union Pacific': 'Union Pacific Transcontinental Railroad',
            'Katy Railroad': 'Missouri–Kansas–Texas Railroad (The Katy)'
        }
        if inner in rr_map:
            res = rr_map[inner]
            if len(res) >= min_target_len:
                return res
            return f"{res} regional transit network"

    # 8. Indigenous groups / Tribes
    if 'indigenous' in q_lower or 'tribe' in q_lower or 'nomadic' in q_lower or inner in ('Jumano', 'Cherokee', 'Kiowa', 'Comanche', 'Apache'):
        tribe_map = {
            'Jumano': 'Jumano (pueblo and agricultural trading tribe of West Texas)',
            'Cherokee': 'Cherokee (woodland agricultural tribe displaced to East Texas)',
            'Kiowa': 'Kiowa (nomadic equestrian hunters of the Southern Plains)',
            'Comanche': 'Comanche (dominant equestrian nomads of the Great Plains)',
            'Apache': 'Lipan Apache (nomadic hunter-gatherers of Central Texas)'
        }
        if inner in tribe_map:
            res = tribe_map[inner]
            if len(res) >= min_target_len:
                return res
            return f"{res} of early Texas"

    # 9. Explorers / Historical figures
    if 'explorer' in q_lower or 'mapped' in q_lower or inner in ('Juan de Oñate', 'Hernando de Soto', 'Christopher Columbus', 'Jacques Cartier', 'Samuel de Champlain', 'Louis Juchereau de St. Denis'):
        explorer_map = {
            'Juan de Oñate': 'Don Juan de Oñate (Spanish conquistador and colonial governor)',
            'Hernando de Soto': 'Hernando de Soto (Spanish conquistador who explored the Southeast)',
            'Christopher Columbus': 'Christopher Columbus (Genoese navigator under the Crown of Castile)',
            'Jacques Cartier': 'Jacques Cartier (Breton maritime explorer who claimed Canada for France)',
            'Samuel de Champlain': 'Samuel de Champlain (French explorer known as "The Father of New France")',
            'Louis Juchereau de St. Denis': 'Louis Juchereau de St. Denis (French-Canadian explorer who founded Natchitoches)'
        }
        if inner in explorer_map:
            res = explorer_map[inner]
            if len(res) >= min_target_len:
                return res
            return f"{res} during sixteenth-century expeditions"

    # 10. Missions
    if 'mission' in q_lower or inner.startswith('Mission '):
        mission_map = {
            'Mission San Antonio de Valero': 'Mission San Antonio de Valero (the historic fortress later known as the Alamo)',
            'Mission Concepción': 'Mission Nuestra Señora de la Purísima Concepción de Acuña',
            'Mission Espada': 'Mission San Francisco de la Espada (historic Spanish colonial mission outpost)',
            'San José': 'Mission San José y San Miguel de Aguayo ("Queen of the Missions")',
            'Goliad': 'Presidio Nuestra Señora de Loreto de la Bahía at Goliad',
            'La Bahía': 'Presidio Nuestra Señora de Loreto de la Bahía near Goliad'
        }
        if inner in mission_map:
            res = mission_map[inner]
            if len(res) >= min_target_len:
                return res
            return f"{res} along the San Antonio river basin"

    # 11. Retailers (A. Zimmerman)
    if 'retail' in q_lower or inner in ('Target', 'Kmart', 'Sears'):
        ret_map = {
            'Target': 'Target Corporation (Minneapolis-based discount retail chain)',
            'Kmart': 'Kmart (historic big-box retailer operated by S.S. Kresge)',
            'Sears': 'Sears, Roebuck and Company (historic catalog and department store chain)'
        }
        if inner in ret_map:
            res = ret_map[inner]
            if len(res) >= min_target_len:
                return res
            return f"{res} across store locations nationwide"

    # 11b. People/Executives in A. Zimmerman
    if show == 'A. Zimmerman, Reporter-at-Large!':
        if inner in ('David Glass', 'Lee Scott', 'H. Lee Scott', 'Mike Duke', 'Doug McMillon'):
            res = f"{inner} (former Walmart CEO and corporate board executive)"
            if len(res) >= min_target_len:
                return res
            return f"{res} overseeing global retail operations"
        elif inner in ('Mike Ullman', 'Marvin Traub', 'Mickey Drexler', 'Ron Johnson'):
            res = f"{inner} (veteran department store retail chief executive)"
            if len(res) >= min_target_len:
                return res
            return f"{res} leading major corporate turnaround efforts"
        elif inner in ('Arthur Blank', 'Bernie Marcus', 'Frank Blake', 'Bob Nardelli'):
            res = f"{inner} (former Home Depot executive and retail director)"
            if len(res) >= min_target_len:
                return res
            return f"{res} directing national home-improvement operations"
        elif inner in ('Carl Icahn', 'Bill Ackman', 'Nelson Peltz', 'Edward Lampert'):
            res = f"{inner} (activist hedge fund manager and corporate turnaround investor)"
            if len(res) >= min_target_len:
                return res
            return f"{res} orchestrating multi-billion dollar mergers"
        elif inner in ('Former Governor John Connally', 'Ross Perot Jr.', 'Laura Miller', 'Former Dallas Mayor Ron Kirk'):
            res = f"{inner} (prominent Texas civic leader and public official)"
            if len(res) >= min_target_len:
                return res
            return f"{res} influential in North Texas public affairs"

    # 11c. People in UT Austin
    if show == 'UT Austin':
        ut_people_map = {
            'Dennis Quaid': 'Dennis Quaid (Houston native and veteran Hollywood actor)',
            'Tommy Lee Jones': 'Tommy Lee Jones (Oscar-winning actor and Texas native)',
            'Ethan Hawke': 'Ethan Hawke (acclaimed film actor and Austin native)',
            'Rosalynn Carter': 'Rosalynn Carter (First Lady and mental health advocate)',
            'Barbara Bush': 'Barbara Bush (First Lady and founder of the Barbara Bush Foundation)',
            'Laura Bush': 'Laura Bush (First Lady and former public school librarian)',
            'Dan Rather': 'Dan Rather (veteran CBS Evening News anchor and Texas native)',
            'Tom Brokaw': 'Tom Brokaw (longtime NBC Nightly News anchor and author)',
            'Peter Jennings': 'Peter Jennings (veteran ABC World News Tonight anchor)',
            'Kate Jackson': 'Kate Jackson (original Charlie\'s Angels television star)',
            'Cheryl Ladd': 'Cheryl Ladd (Charlie\'s Angels star and recording artist)',
            'Jaclyn Smith': 'Jaclyn Smith (Charlie\'s Angels star and fashion designer)',
            'Mack Brown': 'Mack Brown (national championship-winning Texas head coach)',
            'Bear Bryant': 'Paul "Bear" Bryant (legendary college football head coach)',
            'Tom Landry': 'Tom Landry (hall of fame Dallas Cowboys head coach)'
        }
        if inner in ut_people_map:
            res = ut_people_map[inner]
            if len(res) >= min_target_len:
                return res
            return f"{res} celebrated in Texas sports and culture"

    # 11d. People in Ben Folds
    if show == 'Ben Folds':
        bf_people_map = {
            'Darren Jessee': 'Darren Jessee (drummer, backing vocalist, and co-songwriter)',
            'Robert Sledge': 'Robert Sledge (fuzz bass virtuoso and backing vocalist)',
            'Caleb Southern': 'Caleb Southern (record producer and Chapel Hill audio engineer)',
            'Jared Reynolds': 'Jared Reynolds (longtime touring bassist with Ben Folds)'
        }
        if inner in bf_people_map:
            res = bf_people_map[inner]
            if len(res) >= min_target_len:
                return res
            return f"{res} who contributed to studio recordings"

    # 11e. People in Texas History
    if show == 'Texas History':
        tx_people_map = {
            'Moses Austin': 'Moses Austin (lead mining pioneer who secured the initial Texas empresario grant)',
            'Sam Houston': 'General Sam Houston (commander-in-chief of the Texian Army at San Jacinto)',
            'William B. Travis': 'Lieutenant Colonel William Barret Travis (co-commander at the Alamo)',
            'Mirabeau B. Lamar': 'Mirabeau B. Lamar (second President of the Republic of Texas)',
            'David G. Burnet': 'David G. Burnet (interim President of the Republic of Texas in 1836)'
        }
        if inner in tx_people_map:
            res = tx_people_map[inner]
            if len(res) >= min_target_len:
                return res
            return f"{res} of nineteenth-century Texas history"

    # 12. Newspapers / Publications
    if 'publication' in q_lower or 'newspaper' in q_lower or inner in ('The New York Times', 'Financial Times', 'Bloomberg Businessweek', 'The Dallas Times Herald', 'The Texas Tribune', 'The Dallas Gazette'):
        pub_map = {
            'The New York Times': 'The New York Times (national daily broadsheet newspaper)',
            'Financial Times': 'Financial Times (international salmon-pink business daily)',
            'Bloomberg Businessweek': 'Bloomberg Businessweek (weekly corporate finance and business magazine)',
            'The Dallas Times Herald': 'The Dallas Times Herald (evening broadsheet competitor founded in 1888)',
            'The Texas Tribune': 'The Texas Tribune (nonpartisan member-supported digital news organization)',
            'The Dallas Gazette': 'The Dallas Gazette (early frontier settlement weekly newspaper)'
        }
        if inner in pub_map:
            res = pub_map[inner]
            if len(res) >= min_target_len:
                return res
            return f"{res} covering corporate finance and investigations"

    # 13. Famous Canadians (People)
    if show == 'Famous Canadians':
        canadian_people = [
            f"{inner} (Order of Canada recipient)",
            f"{inner} (distinguished Canadian cultural icon)",
            f"{inner} (veteran Canadian performer and advocate)",
            f"{inner} (Governor General's Performing Arts Award recipient)",
            f"{inner} (celebrated Canadian pioneer and innovator)",
            f"{inner} (famed Canadian author and public intellectual)",
            f"{inner} (longtime Canadian broadcaster and educator)"
        ]
        choice = canadian_people[seed_idx % len(canadian_people)]
        if len(choice) >= min_target_len:
            return choice
        return f"{inner} (distinguished Canadian pioneer, innovator, and Order of Canada officer)"

    # 14. Music / Studios / Record Labels / Songs (Billboard Hits & Ben Folds)
    if show in ('Billboard Hits', 'Ben Folds'):
        if 'studio' in q_lower or ('recorded' in q_lower and 'studio' in inner.lower()):
            studio_map = {
                'Abbey Road Studios in London': 'Abbey Road Studios (historic EMI Studio Two) in St. John\'s Wood, London',
                'Hitsville U.S.A. in Detroit': 'Hitsville U.S.A. (Studio A / The Snakepit) on West Grand Boulevard in Detroit',
                'Sun Studio in Memphis': 'Sun Studio (historic 706 Union Avenue recording facility) in Memphis, Tennessee',
                'Electric Lady Studios in New York': 'Electric Lady Studios (founded by Jimi Hendrix) in Greenwich Village, New York',
                'Sound City in Van Nuys, California': 'Sound City Studios (famed for its custom Neve console) in Van Nuys, California'
            }
            if inner in studio_map:
                res = studio_map[inner]
                if len(res) >= min_target_len:
                    return res
                return f"{res} where legendary sessions occurred"

        if 'label' in q_lower or inner in ('Epic Records', 'Sub Pop', '550 Music', 'Passenger Records'):
            label_map = {
                'Epic Records': 'Epic Records (major Sony Music commercial label subsidiary)',
                'Sub Pop': 'Sub Pop Records (famed Seattle independent alternative rock label)',
                '550 Music': '550 Music (Sony 550 Music alternative and pop imprint)'
            }
            if inner in label_map:
                res = label_map[inner]
                if len(res) >= min_target_len:
                    return res
                return f"{res} distributed worldwide"

        # Song title or lyrics
        if quote_char:
            fmt = lambda s: f"{quote_char}{inner}{quote_char} {s}"
        else:
            fmt = lambda s: f"{inner} {s}"

        music_suffixes = [
            fmt("(original 45 RPM mono single release)"),
            fmt("(extended studio album track version)"),
            fmt("(unreleased studio session demo recording)"),
            fmt("(Gold-certified radio broadcast edit)"),
            fmt("(recorded live in concert with orchestral backing)"),
            fmt("(alternate studio outtake with acoustic instrumentation)"),
            fmt("(classic single recorded during original studio sessions)"),
            fmt("(chart-topping Billboard Hot 100 hit release)")
        ]
        choice = music_suffixes[seed_idx % len(music_suffixes)]
        if len(choice) >= min_target_len:
            return choice
        return fmt("(extended multi-track studio master recording produced for album release)")

    # 15. Ingredients
    if show == 'Ingredients':
        # Spirits, mixers, and botanicals
        if len(inner.split()) <= 2 and not any(c in inner for c in ';:.,'):
            ing_prefixes = [
                f"Artisanal small-batch {inner.lower()}",
                f"Freshly harvested organic {inner.lower()}",
                f"Cold-pressed premium quality {inner.lower()}",
                f"Traditional Mediterranean imported {inner.lower()}",
                f"Locally sourced heirloom {inner.lower()}"
            ]
            choice = ing_prefixes[seed_idx % len(ing_prefixes)]
            if len(choice) >= min_target_len:
                return choice

        ing_suffixes = [
            f"{inner} (artisanally prepared regional culinary staple)",
            f"{inner} (traditionally aged in oak barrels for distinct flavor)",
            f"{inner} (certified organic harvest from specialty orchards)",
            f"{inner} (handcrafted using time-honored distillation techniques)",
            f"{inner} (infused with aromatic botanical botanicals and spices)"
        ]
        choice = ing_suffixes[seed_idx % len(ing_suffixes)]
        if len(choice) >= min_target_len:
            return choice
        return f"{inner} (artisanally prepared regional culinary staple crafted with organic botanicals)"

    # 16. Fruits & Veggies
    if show == 'Fruits & Veggies':
        # Botanical terms or single vegetables
        if len(inner.split()) <= 2 and not any(c in inner for c in ';:.,'):
            bot_prefixes = [
                f"Carefully cultivated {inner.lower()} (heirloom garden variety)",
                f"Freshly harvested {inner.lower()} (certified organic cultivar)",
                f"Wild-grown {inner.lower()} (native agricultural specimen)",
                f"{inner} (specialized vegetative botanical plant tissue)",
                f"{inner} (fleshy indehiscent botanical structure with protective skin)",
                f"{inner} (botanical angiosperm plant family with varied cultivars)"
            ]
            choice = bot_prefixes[seed_idx % len(bot_prefixes)]
            if len(choice) >= min_target_len:
                return choice

        # Descriptive clauses
        bot_suffixes = [
            f"{inner} throughout the entire vegetative growing cycle of the plant",
            f"{inner} developed directly from the swollen receptacle of the flower",
            f"{inner} providing structural protection to developing interior seed chambers",
            f"{inner} characteristically observed across diverse angiosperm plant families"
        ]
        choice = bot_suffixes[seed_idx % len(bot_suffixes)]
        if len(choice) >= min_target_len:
            return choice
        return f"{inner} developed directly from the swollen floral receptacle throughout the growing cycle"

    # 17. Anglophone Slang
    if show == 'Anglophone Slang':
        if inner.startswith('To '):
            slang_templates = [
                f"{inner} in an exceptionally hurried and energetic manner",
                f"{inner} without receiving any prior advance notice or preparation",
                f"{inner} while actively celebrating with a large gathering of close friends",
                f"{inner} despite encountering numerous unexpected obstacles along the way",
                f"{inner} during a thoroughly chaotic and unpredictable situation"
            ]
        elif inner.startswith(('A ', 'An ', 'The ')):
            slang_templates = [
                f"{inner} commonly encountered across rural and suburban communities",
                f"{inner} widely known for creating unexpected humor and harmless confusion",
                f"{inner} regarded with sincere fondness and nostalgia by local residents",
                f"{inner} frequently utilized during informal backyard social gatherings"
            ]
        elif any(inner.startswith(w) for w in ('Very ', 'Extremely ', 'Severely ', 'Deeply ', 'Bitterly ', 'Completely ')):
            slang_templates = [
                f"{inner} and noticeably overwhelmed by current difficult circumstances",
                f"{inner} after enduring an unexpectedly grueling and exhausting ordeal",
                f"{inner} to an extraordinary and completely unprecedented degree",
                f"{inner} throughout the entire duration of a long and stressful day"
            ]
        else:
            slang_templates = [
                f"{inner} spoken in a relaxed and humorous tone among close peers",
                f"{inner} expressing genuine surprise, disbelief, and hearty amusement",
                f"{inner} commonly heard during informal everyday conversations across the region",
                f"{inner} conveyed with expressive warmth and unmistakable enthusiasm"
            ]

        choice = slang_templates[seed_idx % len(slang_templates)]
        if len(choice) >= min_target_len:
            return choice
        return f"{inner} commonly heard during informal everyday conversations among close peers and family"

    # 18. A. Zimmerman general retail phrases
    if show == 'A. Zimmerman, Reporter-at-Large!':
        zim_templates = [
            f"{inner} across retail store operations nationwide",
            f"{inner} to reduce operating costs and employee overhead",
            f"{inner} through standardized corporate supply chain practices",
            f"{inner} while facing intense scrutiny from Wall Street analysts",
            f"{inner} across regional distribution centers and big-box stores",
            f"{inner} in order to maximize quarterly shareholder earnings"
        ]
        choice = zim_templates[seed_idx % len(zim_templates)]
        if len(choice) >= min_target_len:
            return choice
        return f"{inner} across retail store operations and regional distribution centers nationwide"

    # 19. General History / UT Austin / Dallas general phrases
    gen_templates = [
        f"{inner} (serving as a prominent historical and cultural benchmark)",
        f"{inner} (officially recognized across regional historical documentation)",
        f"{inner} (established under formal administrative and municipal jurisdiction)",
        f"{inner} (documented extensively throughout contemporary regional archives)"
    ]
    choice = gen_templates[seed_idx % len(gen_templates)]
    if len(choice) >= min_target_len:
        return choice
    return f"{inner} (documented extensively throughout contemporary regional historical archives)"

def balance_group():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)

    print(f"Loaded {len(questions)} questions from {INPUT_PATH}")

    shows = defaultdict(list)
    for idx, q in enumerate(questions):
        shows[q['show']].append((idx, q))

    TARGET_PCT = 0.215
    balanced_questions = copy.deepcopy(questions)
    total_elongated = 0

    print("\n--- Balancing Shows in Group 4 ---")
    for show_name, show_items in sorted(shows.items()):
        total_q = len(show_items)
        
        longest_items = []
        for orig_idx, q in show_items:
            opts = q['options']
            ans = q['answer']
            lens = [len(o) for o in opts]
            if lens[ans] == max(lens):
                longest_items.append((orig_idx, q))

        current_longest_count = len(longest_items)
        current_pct = (current_longest_count / total_q) * 100
        target_count = int(total_q * TARGET_PCT)
        needed_reductions = max(0, current_longest_count - target_count)

        print(f"Show '{show_name}': {current_longest_count}/{total_q} ({current_pct:.1f}%) -> Target: {target_count} ({TARGET_PCT*100:.1f}%), Needed reductions: {needed_reductions}")

        if needed_reductions <= 0:
            continue

        items_to_modify = longest_items[:needed_reductions]
        modified_count = 0

        for seed, (orig_idx, q) in enumerate(items_to_modify):
            target_q = balanced_questions[orig_idx]
            ans_idx = target_q['answer']
            orig_opts = target_q['options']
            max_len = max(len(o) for o in orig_opts)
            min_target_len = max_len + 5

            false_indices = [i for i in range(4) if i != ans_idx]
            chosen_false_idx = false_indices[seed % len(false_indices)]
            false_opt = orig_opts[chosen_false_idx]

            new_opt = get_contextual_elongation(show_name, target_q['q'], false_opt, min_target_len, seed_idx=seed)
            
            retry = 0
            while (len(new_opt) <= max_len or new_opt in target_q['options']) and retry < 25:
                retry += 1
                new_opt = get_contextual_elongation(show_name, target_q['q'], false_opt, min_target_len + retry * 6, seed_idx=seed + retry)

            if len(new_opt) <= max_len:
                new_opt = f"{new_opt} (additional verified distinctive detail)"

            target_q['options'][chosen_false_idx] = new_opt

            new_lens = [len(o) for o in target_q['options']]
            assert new_lens[ans_idx] < max(new_lens), f"Failed to elongate: {target_q['options']}"
            assert len(set(target_q['options'])) == 4, f"Options not unique: {target_q['options']}"
            modified_count += 1
            total_elongated += 1

        print(f"  Successfully modified {modified_count} questions for '{show_name}'")

    print(f"\nTotal questions modified across all shows: {total_elongated}")

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(balanced_questions, f, ensure_ascii=False, indent=0)

    print(f"Saved balanced questions to {OUTPUT_PATH}")

if __name__ == "__main__":
    balance_group()
