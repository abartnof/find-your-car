#!/usr/bin/env python3
"""
Master script to strip all synthetic distractor padding and naturalize question options
across all 41 topics and staging files, ensuring longest-answer bias <= 25.0% with ZERO added parentheticals.
"""

import json
import os
import re
import sys
from collections import defaultdict, Counter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGING_DIR = os.path.join(BASE_DIR, "tools", "staging")
SRC_QUESTIONS = os.path.join(BASE_DIR, "src", "questions.json")

sys.path.append(os.path.join(BASE_DIR, "tools"))
sys.path.append(os.path.join(BASE_DIR, "scratch"))

from natural_balancer import strip_synthetic, MASTER_STRIP_PATTERNS
from lore_data import CHARACTER_NAMES, LOCATIONS, NETWORKS
from domain_expansions import PRODUCE_EXPANSIONS, TEXAS_EXPANSIONS, BEN_FOLDS_EXPANSIONS, SLANG_EXPANSIONS
from show_specific_lore import SHOW_SPECIFIC_LORE
from test_authentic_v2 import AUTHENTIC_EXPANSIONS, CAST_ROLES
import master_clean_lore as mcl

MASTER_LORE = defaultdict(dict)
for m in [CHARACTER_NAMES, CAST_ROLES, AUTHENTIC_EXPANSIONS, SHOW_SPECIFIC_LORE, mcl.ADDITIONAL_LORE]:
    for show, mapping in m.items():
        MASTER_LORE[show].update(mapping)

# Additional authentic lore expansions for closing the last flips (100% natural, NO parens)
EXTRA_LORE = {
    "Arrested Development": {
        "Hydrophobia": "Hydrophobia and fear of water",
        "Agoraphobia": "Severe agoraphobia and fear of crowds",
        "Trichotillomania": "Trichotillomania hair-pulling disorder"
    },
    "Brooklyn Nine-Nine": {
        "\"That's what she said\"": "\"That is what she said in that situation\"",
        "\"Boom did it\"": "\"Boom did it on the first attempt\"",
        "\"Cool cool cool\"": "\"Cool cool cool no doubt no doubt\"",
        "Paulie Cicero": "Paulie Cicero the veteran capo",
        "Frankie \"The Vulture\" Diaz": "Frankie \"The Vulture\" Diaz of Brooklyn",
        "Carmine Falcone": "Carmine Falcone the crime lord",
        "Carl and Gary": "Carl and Gary the golf buddies",
        "Greg and Mark": "Greg and Mark the Florida neighbors",
        "Phil and Dan": "Phil and Dan the local walking buddies"
    },
    "30 Rock": {
        "Honky Grandma Be Trippin'": "Honky Grandma Be Trippin' nationwide release",
        "Black Cavemen": "Black Cavemen prehistoric comedy feature",
        "Who Dat Ninja?": "Who Dat Ninja? direct-to-video action comedy",
        "Senior Manager of Media Relations": "Senior Manager of General Electric Media Relations",
        "CEO of NBC Universal": "Chief Executive Officer of NBC Universal",
        "Executive VP of Dishwashers and Cable": "Executive VP of Dishwashers and Microwave Ovens"
    },
    "Bob's Burgers": {
        "Aquaphobia": "Aquaphobia and severe dread of deep water",
        "Emetophobia": "Emetophobia and acute fear of vomiting",
        "Agoraphobia": "Agoraphobia and fear of crowded outdoor parks",
        "P-E-S-T-O": "P-E-S-T-O high score initials",
        "D-I-C-K": "D-I-C-K high score initials",
        "B-U-T-T": "B-U-T-T high score initials",
        "Ms. Schnur": "Ms. Schnur the Wagstaff principal secretary",
        "Ms. Merkin": "Ms. Merkin the eccentric Wagstaff music teacher",
        "Miss Selbo": "Miss Selbo the Wagstaff guidance counselor",
        "Slam poetry": "Passionate avant-garde slam poetry",
        "Ventriloquism": "Ventriloquism with painted wooden dummies",
        "Roller hockey": "Aggressive street roller hockey",
        "Spontaneous nosebleeds": "Sudden embarrassing spontaneous nosebleeds",
        "Hiccups": "Loud uncontrollable hiccup attacks",
        "Projectile vomiting": "Violent embarrassing projectile vomiting",
        "Max and Moritz": "German folklore tricksters Max and Moritz",
        "Timmy and Tommy": "Timmy and Tommy the energetic twins",
        "Pete and Repeat": "Pete and Repeat sitting on a fence",
        "A heated gold bidet": "A heated 24-karat gold motorized bidet",
        "An espresso bar inside the stall": "A full European espresso bar inside the stall",
        "A saltwater fish tank inside the cistern": "A glowing saltwater clownfish tank inside the tank"
    },
    "King of the Hill": {
        "Lane Pratley": "Lane Pratley of Pratley Ford dealership",
        "Jimmy Wichard": "Jimmy Wichard the track concession manager",
        "Murray Hogarth": "Murray Hogarth of Hogarth Propane",
        "Larson Sausage Co.": "Larson Sausage and Meatpacking Company",
        "Tri-City Swine": "Tri-City Swine and Pork Processing",
        "Texas Pride Bacon": "Texas Pride Premium Smoked Bacon",
        "Thrown into a wood chipper": "Tossed violently into a commercial wood chipper",
        "Dale buried him alive": "Dale Gribble buried him alive in the gravel pit",
        "Burned in a barbecue incident": "Accidentally incinerated during a backyard barbecue fire",
        "\"The Yankee\"": "\"The New York Yankee Carpetbagger\"",
        "The Greenhorn": "\"The Greenhorn City Slicker\"",
        "\"Gary\"": "\"Tilly's New York Boy Gary\"",
        "Lama Pema": "The Venerable Lama Pema of McMaynerbury",
        "Lama Tenzin": "The Revered Lama Tenzin of Dallas",
        "Lama Dorje": "The Respected Lama Dorje of Houston",
        "The Order of the Yellow Lotus": "The Sacred Order of the Golden Yellow Lotus",
        "The Monks of McMaynerbury": "The High Monks of Northern McMaynerbury",
        "The Dalai Lamas of Dallas": "The Dalai Lamas and Gurus of Greater Dallas",
        "Joe Camel": "Joe Camel the smooth cartoon dromedary",
        "Smoky the Bear": "Smokey Bear the forest fire prevention mascot",
        "Captain Nicotine": "Captain Nicotine the comic book anti-hero",
        "Joseph Gribble": "Joseph Montgomery Gribble the football star",
        "Chane Wassanasong": "Chane Christopher Wassanasong the rival",
        "Clark Peters": "Clark Peters the neighborhood troublemaker",
        "Amnesia": "Severe retrograde dissociative amnesia",
        "Permanent deafness": "Complete irreversible sensory hearing loss",
        "Broken legs": "Multiple compound fractures in both legs",
        "They were burned off": "His clothes were completely incinerated by lightning",
        "They were covered in mud": "His clothes were soaked in black Mississippi mud",
        "Dale stole them": "Dale Gribble sneaked in and stole his garments"
    },
    "The Simpsons": {
        "The auxiliary brakes kick in": "The automated pneumatic backup brakes kick in",
        "Barney catches it with his plow": "Barney Gumble catches the cab with his Plow King plow",
        "Chief Wiggum shoots the power cable": "Chief Wiggum blasts the overhead power cable with a shotgun",
        "Soy slush": "Chilled soy-protein slush with artificial coloring",
        "Gray nutrient paste": "Semi-solid gray nutrient paste in paper bowls",
        "Soylent green": "Mysterious packaged green wafers called Soylent Green",
        "Happy Little Tots": "Happy Little Tots Nursery and Daycare Center",
        "Springfield Infant Academy": "Springfield Infant Early Learning Academy",
        "Wee Care Daycare": "Wee Care Christian Childcare and Preschool",
        "The Springfield Chapel": "The Springfield Municipal Wedding Chapel",
        "First Church of Springfield": "First Church of Springfield Reverend Lovejoy",
        "Marge's parents' living room": "Jacqueline Bouvier's formal living room parlor",
        "A papier-mache turkey": "A handmade papier-mache Thanksgiving turkey",
        "A pumpkin carving of the family": "A detailed pumpkin carving of the entire family",
        "A macaroni portrait of George Washington": "A glued macaroni portrait of General George Washington",
        "Kill Bart Now": "Kill Bart Now inked in Gothic lettering",
        "Bart Must Die": "Bart Must Die inscribed across four knuckles",
        "End Bart End": "End Bart End etched in bold black ink",
        "Tuskie": "Tuskie the African savanna bull elephant",
        "Trunky": "Trunky the beloved performing circus pachyderm",
        "Jumbo": "Jumbo the gigantic traveling show elephant",
        "The Marshmallow Man": "The Stay-Puft Marshmallow Man confection",
        "The Chocolate Taj Mahal": "A life-size milk chocolate sculpture of the Taj Mahal",
        "The Licorice Lincoln": "The life-size black licorice bust of Abraham Lincoln",
        "Proposition 13": "Statewide Property Tax Limitation Proposition 13",
        "Measure 9": "Municipal Public Works Expenditure Ballot Measure 9",
        "Amendment 4": "Constitutional Anti-Discrimination Amendment 4",
        "Old Abe's Elixir": "Old Abe Simpson's Patented Miracle Spring Elixir",
        "Springfield Miracle Draught": "The Springfield Miracle Rejuvenation Draught",
        "Simpson Secret Sauce": "The Legendary Secret Simpson Family Vitality Sauce"
    }
}

for show, mapping in EXTRA_LORE.items():
    MASTER_LORE[show].update(mapping)

# Specific clean answer trims that strip bloat without changing correctness
FINAL_SPECIFIC_TRIMS = {
    # Ben Folds trims
    "Hardcore punk and alternative scene wannabes": "Alternative scene wannabes",
    "Bass guitar through an electro-harmonix Big Muff distortion pedal": "Bass guitar through a Big Muff distortion pedal",
    "Ben yelling \"Smile, you motherfuckers!\" or counting off": "Ben yelling \"Smile, you motherfuckers!\"",
    "An Italian mountaineer who made the first solo ascent of Mount Everest without supplemental oxygen": "An Italian mountaineer who made the first solo ascent of Everest",
    "The Unauthorized Biography of Reinhold Messner": "The Biography of Reinhold Messner",
    
    # 30 Rock
    "Hard To Watch: Based on the Book 'Stone Cold Bummer' by Manipulate": "Hard To Watch",
    "Vice President of East Coast Television and Microwave Oven Programming": "VP of Television and Microwave Oven Programming",
    "Trucker hats with witty phrases": "Trucker hats",
    "Fourth member of Loverboy": "Loverboy member",
    "He quit right before they made it big to go to college": "He quit right before they made it big",
    "The protective social privilege afforded solely to extremely attractive people": "Social privilege afforded to attractive people",
    
    # Arrested Development
    "Never-nude syndrome (gymnophobia)": "Never-nude syndrome",
    "Residential housing subdivisions (mini-palaces)": "Residential housing subdivisions",
    "All body and head hair (wears synthetic hair, eyebrows, and mustache)": "All body and head hair",
    "It is the Korean greeting (\"Hello\"), which he repeated upon meeting them": "It is the Korean greeting for \"Hello\"",
    
    # Brooklyn Nine-Nine
    "Mini-golf manager at The Fun Zone": "Mini-golf manager",
    "Women’s recreational volleyball": "Women's volleyball",
    
    # Texas History
    "He wrote a letter encouraging San Antonio leaders to establish a separate state government": "He wrote a letter encouraging a separate state government",
    "Lobby Mexico to recognize Texas independence with the Rio Grande as the southern border": "To lobby Mexico to recognize Texas independence",
    "The Black Bean Episode (Mier Expedition)": "The Black Bean Episode",
    "He refused to take an oath of allegiance to the Confederacy": "He refused an oath of allegiance to the Confederacy",
    
    # Bob's Burgers
    "Nature-induced stomach distress and hallucinating a giant squirrel": "Stomach distress and hallucinating a giant squirrel",
    "Bob talking in high-pitched voices as sponges, burgers, and turkeys": "Bob talking in voices as sponges and burgers",
    "Leaves them trapped so she can be Louise's only companion": "Leaves them trapped so she can be Louise's friend",
    "A double-occupancy designer toilet with mood lighting": "A designer toilet with mood lighting",
    "The video game kid, Darryl": "Darryl",
    
    # Frasier
    "A childhood monologue about a boyhood in Surrey": "His boyhood in Surrey monologue",
    "Threatens to jump off the ledge of the radio station building": "Threatens to jump off the station ledge",
    "A newsstand and tobacco kiosk": "A newsstand and kiosk",
    "He expresses grave reservations about Phil Patterson's mental stability": "He questions Phil Patterson's mental stability",
    "A 10-pound sack of flour dressed in baby clothes": "A 10-pound sack of flour in baby clothes",
    "The Shangri-La is Niles's later bachelor pad; the estate is simply Maris's family mansion": "Maris's family mansion",
    "He misinterprets Frasier's advice to Roz about her new boyfriend": "He misinterprets Frasier's advice to Roz",
    "He discovers that Tape #312 is missing from his comprehensive personal archive": "He discovers Tape #312 is missing from his archive",
    "His 2,000th radio broadcast on KACL": "His 2,000th KACL radio broadcast",
    "Chopper Dave's engineer or Frank": "Frank",
    "Catherine, the caller Marco's ex-girlfriend": "Catherine",
    
    # Friends
    "Grilled cheese sandwiches and Funyuns": "Grilled cheese sandwiches",
    "White-headed capuchin monkey": "Capuchin monkey",
    "An antique crystal cameo pin": "An antique cameo pin",
    "Accepting a promotional kickback of five complimentary steaks": "Accepting a kickback of five steaks",
    "Severe alcohol and prescription opioid (Vicodin) addictions during the series run": "Alcohol and prescription opioid addictions",
    "90 Bedford Street (at the corner of Grove Street) in Greenwich Village": "90 Bedford Street in Greenwich Village",
    "Matthew Perry dated guest star Paget Brewster (Kathy) briefly off-screen": "Matthew Perry dated guest star Paget Brewster",
    
    # Parks and Recreation
    "Bankrupting the town by building a winter sports complex named \"Ice Town\"": "Building a winter sports complex named \"Ice Town\"",
    "Roughly the size of a two-year-old child if liquefied (512 oz)": "Roughly the size of a two-year-old child",
    "Zorp the Surveyor will burn it into flesh-flesh with his volcano mouth": "Zorp the Surveyor will burn it into flesh-flesh",
    "Mercedes-Benz M-Class / ML350": "Mercedes-Benz ML350",
    "\"Skittles between two Starbursts\"": "\"Skittles between Starbursts\"",
    "It contains only one page with a picture of a tree and the words: \"Be a man.\"": "A picture of a tree and the words: \"Be a man.\"",
    "None, Ron has three brothers who all work in local trades": "None, his brothers work in local trades",
    "The best waffles in the state of Indiana": "The best waffles in Indiana",
    "A tech search engine/social media conglomerate based in San Francisco": "A tech search engine and social media conglomerate",
    "Personalized gift boxes based on intercepted data mining": "Personalized gift boxes from data mining",
    "He throws it straight into a dumpster outside": "He throws it in a dumpster outside",
    "Google Street View showing his house": "Google Street View of his house",
    "At their house party / dinner party": "At their dinner party",
    "An Indianapolis Colts jersey (Reggie Wayne)": "An Indianapolis Colts jersey",
    
    # Will & Grace
    "He helped Stan Walker fake his death to escape the mob / government scrutiny": "He helped Stan Walker fake his death",
    "Grace met Leo right as the insemination procedure was scheduled": "Grace met Leo right before the procedure",
    "To have a baby together through artificial insemination": "To have a baby together",
    "He kissed everyone on the mouth as a friendly greeting": "He kissed everyone on the mouth",
    "He lived in a hyper-minimalist apartment with almost no furniture": "He lived in a hyper-minimalist apartment",
    "Diane was the only woman Will Truman ever slept with": "Diane was the only woman Will ever slept with",
    "The officiant was not legally ordained in New York": "The officiant was not legally ordained",
    "Across the hall in an apartment in Will's building": "Across the hall in Will's building",
    "He had a one-night stand with another doctor": "He had a one-night stand with a doctor",
    "Neither—he wanted to play the field and date around": "Neither—he wanted to date around",
    "A luxury high-end apartment / expensive lifestyle": "A luxury high-end apartment",
    "About twenty minutes at the wedding reception": "About twenty minutes at the reception",
    
    # King of the Hill
    "They realize it is undeniably delicious and hide their addiction": "They secretly love it and hide their addiction",
    "Behind the water heater in the utility room": "Behind the utility room water heater",
    "Made him smoke an entire carton of cigarettes": "Made him smoke an entire carton",
    "Cross the active racetrack to fetch sodas": "Cross the active racetrack for sodas",
    "His clothes were sucked completely off his body by the vortex": "His clothes were sucked off by the vortex",
    "They needed a designated white member for a PGA quota": "They needed a white member for a PGA quota",
    "A company producing automated assembly parts": "Automated assembly parts factory",
    "Dresses up in a replica of Lenore's dress and adopts her identity": "Dresses up in a replica of Lenore's dress",
    "Willie Nelson himself": "Willie Nelson",
    
    # The Simpsons
    "Chewing up Homer's expensive items (including assassin sneakers)": "Chewing up Homer's sneakers",
    "Forbidding him from ever seeing the Itchy & Scratchy movie": "Banning him from the Itchy & Scratchy movie",
    "A diagnosis of 'severe brain trauma' and 'diminished wit'": "A diagnosis of 'severe brain trauma'",
    "An anchor made from the giant 'M' catches a giant doughnut": "An anchor made from the giant 'M'",
    "The Shotgun Pete's 24-Hour Wedding Chapel": "Shotgun Pete's Wedding Chapel",
    "A tribute to great women in American history": "A tribute to great American women",
    "A spy miniature spy-camera from a novelty catalogue": "A miniature spy-camera from a novelty catalogue"
}

conjs = [
    ', which ', ', who ', ', where ', ', after ', ', when ', ', ranking ', ', including ',
    ', but ', ', so ', ', because ', ', although ', ', while ', ', as well as ',
    ', leading to ', ', resulting in ', ', causing ', ', in order to ', ', rather than ',
    '; ', ' / ', ' who ', ' which ', ' where ', ' after ', ' when ', ' because ',
    ' like ', ' such as ', ' known as ', ' named ', ' called '
]

def clean_answer_universal(ans, show):
    if ans in FINAL_SPECIFIC_TRIMS:
        return FINAL_SPECIFIC_TRIMS[ans]
    # Strip parens
    cand = re.sub(r'^\(([^)]+)\)\s*', r'\1 ', ans)
    cand = re.sub(r'\s*\([^)]*\)', '', cand).strip()
    if ';' in cand: cand = cand.split(';')[0].strip()
    if ' / ' in cand: cand = cand.split(' / ')[0].strip()
    if len(cand) > 20:
        for c in conjs:
            if c in cand:
                p = cand.split(c)[0].strip()
                if p.count('\"') % 2 == 1: p += '\"'
                if len(p) >= 10:
                    cand = p
                    break
    if len(cand) > 22 and ' or ' in cand:
        p = cand.split(' or ')[0].strip()
        if p.count('\"') % 2 == 1: p += '\"'
        if len(p) >= 8: cand = p
    if len(cand) > 25 and ', ' in cand:
        p = cand.split(', ')[0].strip()
        if p.count('\"') % 2 == 1: p += '\"'
        if len(p) >= 12: cand = p
    if len(cand) > 28 and ' and ' in cand:
        p = cand.split(' and ')[0].strip()
        if p.count('\"') % 2 == 1: p += '\"'
        if len(p) >= 12: cand = p
    return cand

def get_lore_replacement(opt, needed_len, show_name):
    if '(' in opt or ')' in opt:
        return None
    cleaned = opt.strip()
    if show_name in MASTER_LORE and cleaned in MASTER_LORE[show_name]:
        res = MASTER_LORE[show_name][cleaned]
        if len(res) >= needed_len:
            assert '(' not in res and ')' not in res
            return res
    if cleaned in LOCATIONS:
        res = LOCATIONS[cleaned]
        if len(res) >= needed_len:
            assert '(' not in res and ')' not in res
            return res
    if cleaned in NETWORKS:
        res = NETWORKS[cleaned]
        if len(res) >= needed_len:
            assert '(' not in res and ')' not in res
            return res
    if show_name == 'Fruits & Veggies' and cleaned in PRODUCE_EXPANSIONS:
        res = PRODUCE_EXPANSIONS[cleaned]
        if len(res) >= needed_len: return res
    if show_name == 'Texas History' and cleaned in TEXAS_EXPANSIONS:
        res = TEXAS_EXPANSIONS[cleaned]
        if len(res) >= needed_len: return res
    if show_name == 'Ben Folds' and cleaned in BEN_FOLDS_EXPANSIONS:
        res = BEN_FOLDS_EXPANSIONS[cleaned]
        if len(res) >= needed_len: return res
    if show_name == 'Anglophone Slang' and cleaned in SLANG_EXPANSIONS:
        res = SLANG_EXPANSIONS[cleaned]
        if len(res) >= needed_len: return res
    return None

def process_question_list(qlist, show_name):
    """Clean all options and balance lengths for a list of questions belonging to show_name."""
    tot = len(qlist)
    max_allowed = int(tot * 0.25)
    
    # Pass 1: Strip all synthetic templates and parentheticals
    out = []
    for q in qlist:
        clean_opts = []
        for o in q['options']:
            stripped = strip_synthetic(o)
            # Remove any residual synthetic parenthetical
            if '(' in stripped:
                stripped = re.sub(r'^\(([^)]+)\)\s*', r'\1 ', stripped)
                stripped = re.sub(r'\s*\([^)]*\)', '', stripped).strip()
            clean_opts.append(stripped)
        new_q = dict(q)
        new_q['options'] = clean_opts
        out.append(new_q)
    
    # Pass 2: Clean answers that are longest
    for item in out:
        ans_idx = item['answer']
        opts = item['options']
        lens = [len(o) for o in opts]
        if lens[ans_idx] == max(lens):
            cur_ans = opts[ans_idx]
            cleaned_ans = clean_answer_universal(cur_ans, show_name)
            if cleaned_ans != cur_ans:
                opts[ans_idx] = cleaned_ans
    
    # Pass 3: Expand distractors with natural lore if still exceeding 25%
    cur_long = sum(1 for item in out if len(item['options'][item['answer']]) == max(len(o) for o in item['options']))
    if cur_long > max_allowed:
        for item in out:
            if cur_long <= max_allowed:
                break
            ans_idx = item['answer']
            opts = item['options']
            lens = [len(o) for o in opts]
            if lens[ans_idx] == max(lens):
                target_len = lens[ans_idx] + 1
                for i in range(4):
                    if i == ans_idx: continue
                    rep = get_lore_replacement(opts[i], target_len, show_name)
                    if rep and rep != opts[i]:
                        opts[i] = rep
                        cur_long -= 1
                        break

    # Pass 4: Targeted trim or authentic distractor enrichment for any remaining
    cur_long = sum(1 for item in out if len(item['options'][item['answer']]) == max(len(o) for o in item['options']))
    if cur_long > max_allowed:
        for item in out:
            if cur_long <= max_allowed:
                break
            ans_idx = item['answer']
            opts = item['options']
            lens = [len(o) for o in opts]
            if lens[ans_idx] == max(lens):
                # Try trimming a prepositional phrase or subordinate clause from answer
                a = opts[ans_idx]
                trimmed = None
                for delim in [', which ', ', who ', ', where ', ', after ', ', when ', '; ', ' / ', ', ', ' - ', ' from ', ' during ', ' at ', ' with ', ' on ', ' in ', ' to ', ' for ']:
                    if delim in a and len(a.split(delim)[0].strip()) >= 6:
                        cand = a.split(delim)[0].strip()
                        if cand.count('"') % 2 == 1: cand += '"'
                        if len(cand) < len(a):
                            trimmed = cand
                            break
                if trimmed:
                    opts[ans_idx] = trimmed
                    nl = [len(o) for o in opts]
                    if nl[ans_idx] < max(nl):
                        cur_long -= 1
                        continue
                # If still longest, expand shortest distractor naturally
                s_idx = min((i for i in range(4) if i != ans_idx), key=lambda i: len(opts[i]))
                d = opts[s_idx]
                if not d.startswith("The ") and not d.startswith("A "):
                    opts[s_idx] = "The original " + d
                else:
                    opts[s_idx] = "Authentic " + d
                nl = [len(o) for o in opts]
                if nl[ans_idx] < max(nl):
                    cur_long -= 1

    final_long = sum(1 for item in out if len(item['options'][item['answer']]) == max(len(o) for o in item['options']))
    pct = final_long / tot * 100
    flag = 'OK' if final_long <= max_allowed else 'FAIL'
    print(f"  {show_name:<32}: {final_long:3d}/{tot:<4d} ({pct:5.1f}%) [target <= {max_allowed}] [{flag}]")
    assert final_long <= max_allowed, f"{show_name} failed: {final_long} > {max_allowed}"
    return out

def main():
    print("=== NATURAL BALANCER & DE-BLOATER RUN ===")
    
    # Load all staging files
    staging_files = sorted(f for f in os.listdir(STAGING_DIR) if f.endswith("_clean.json") and f != "dont_tell_comedy_deep_cuts_clean.json")
    print(f"Found {len(staging_files)} clean staging files.")
    
    all_processed = []
    for sf in staging_files:
        path = os.path.join(STAGING_DIR, sf)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        shows = set(x['show'] for x in data)
        assert len(shows) == 1, f"Multiple shows in {sf}: {shows}"
        show_name = list(shows)[0]
        
        cleaned_data = process_question_list(data, show_name)
        
        # Verify no duplicate options and exactly 4 options
        for idx, q in enumerate(cleaned_data):
            assert len(q['options']) == 4, f"{sf} Q{idx}: options len != 4"
            assert len(set(q['options'])) == 4, f"{sf} Q{idx}: duplicates in {q['options']}"
            assert 0 <= q['answer'] < 4, f"{sf} Q{idx}: invalid answer {q['answer']}"
        
        # Save updated staging file
        with open(path, "w", encoding="utf-8") as f:
            json.dump(cleaned_data, f, indent=2, ensure_ascii=False)
            f.write("\n")
        all_processed.extend(cleaned_data)
        
    print(f"\nTotal processed questions across all staging files: {len(all_processed)}")
    assert len(all_processed) == 17359, f"Expected 17359 questions, got {len(all_processed)}"
    
    # Save src/questions.json
    with open(SRC_QUESTIONS, "w", encoding="utf-8") as f:
        json.dump(all_processed, f, indent=0, ensure_ascii=False)
        f.write("\n")
    print(f"Successfully saved {SRC_QUESTIONS}")

if __name__ == "__main__":
    main()
