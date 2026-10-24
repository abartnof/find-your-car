#!/usr/bin/env python3
"""
Natural Distractor Balancer & De-Bloater for find-your-car quiz.
Strips all synthetic, robotic boilerplate templates and balances options naturalistically
so that longest-answer bias remains <= 25.0% across all 41 topics.
"""

import json
import os
import re
import sys
from collections import defaultdict, Counter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGING_DIR = os.path.join(BASE_DIR, "tools", "staging")
SRC_QUESTIONS = os.path.join(BASE_DIR, "src", "questions.json")

# Master list of synthetic robotic patterns to completely strip
MASTER_STRIP_PATTERNS = [
    # 1. Boilerplate narrative & episode templates
    r'\s*\((?:as )?described in the episode\)',
    r'\s*\(introduced during the storyline\)',
    r'\s*\(referenced by the characters\)',
    r'\s*\(extended broadcast detail\)',
    r'\s*\(complete uncut extended broadcast version\)',
    r'\s*\(complete uncut extended broadcast edition\)',
    r'\s*\(extended broadcast television cut\)',
    r'\s*\(full cut\)',
    r',\s*full cut',
    r'\s*\(.*?,?\s*full cut\)',
    r'\s*\(.*?,?\s*extended broadcast television cut\)',
    r'\s*\(full version\)',
    r'\s*\(original broadcast\)',
    r'\s*\(original broadcast run\)',
    r'\s*\(original network broadcast run\)',
    r'\s*\(primetime cut\)',
    r'\s*\(extended primetime broadcast\)',
    r'\s*\(full syndicated broadcast run\)',
    r'\s*\(primetime television season\)',
    r'\s*\(fall network premiere lineup\)',
    r'\s*\(in a guest starring appearance\)',
    r'\s*\(featured in a recurring guest appearance\)',
    r'\s*\(credited guest appearance\)',
    r'\s*\(credited writer\)',
    r'\s*\(notable supporting figure\)',
    r'\s*\(notable recurring figure\)',
    r'\s*\(recurring character\)',
    r'\s*\(recurring guest performer\)',
    r'\s*\(senior associate\)',
    r'\s*\(official selection\)',
    r'\s*\(official commemorative broadcast edition\)',
    r'\s*\(verified by official network television archives\)',
    r'\s*\(verified by complete series broadcast records\)',
    r'\s*\(fully verified by series production archives\)',
    r'\s*\(featured extended broadcast appearance\)',
    r'\s*\(holiday celebration\)',
    r'\s*\(annual holiday celebration\)',
    r'\s*\(studio recording\)',
    r'\s*\(longtime friend\)',
    r'\s*\(close confidante\)',
    r'\s*\(close acquaintance\)',
    r'\s*\(frequent family acquaintance\)',
    r'\s*\(longtime family acquaintance\)',
    r'\s*\(trusted close confidante\)',
    r'\s*\(frequent social acquaintance\)',
    r'\s*\(noted in production records\)',
    r'\s*\(and don\'t you ever forget it!\)',
    r'\s*\(handcrafted using time-honored distillation techniques\)',
    r'\s*\(additional verified distinctive detail\)',
    r'\s*with full pedigree papers',
    r'\s*used as a comedic plot device',
    r'\s*as a memorable comedic plot device',
    r'\s*displayed prominently on screen',
    r'\s*mentioned during the episode',
    r'\s*according to official records',
    r'\s*according to documented production records',
    r'\s*in every detail',
    r'\s*behind closed doors',
    r'\s*of the city',
    r'\s*without anyone in the building knowing',
    r'\s*and settle the score once and for all',
    r'\s*and definitively avoid any further complications',
    r'\s*once and for all',
    r'\s*in crisp cash bills',
    r'\s*in unmarked twenty-dollar cash bills',
    r'\s*of surveyed respondents',
    r'\s*of all surveyed television viewers',
    r'\s*at the time of filming',
    r'\s*A total of\s+',
    r'\s*A verified total of\s+',
    r'\s*A verified documented total of\s+',
    r'\s*The calendar year\s+',
    r'\s*and never look back(?:\s+for even a single second)?\.?',
    r'\s*with (?:complete and )?pure conviction!?$',
    r'\s*right (?:now )?at this (?:exact )?moment(?: in time)?\??$',
    r'\s*with absolute and complete certainty\.?$',
    r'\s*without a doubt\.?$',

    # 2. Slang & Pop Culture fillers
    r'\s*developed directly from the swollen (?:floral )?receptacle(?: of the flower| throughout the growing cycle)?',
    r'\s*conveyed with expressive warmth and unmistakable enthusiasm',
    r'\s*characteristically observed across diverse angiosperm plant families',
    r'\s*spoken in a relaxed and humorous tone among close peers',
    r'\s*featured prominently in the storyline',
    r'\s*expressing genuine surprise, disbelief, and hearty amusement',
    r'\s*frequently utilized during informal backyard social gatherings',
    r'\s*regarded with sincere fondness and nostalgia by local residents',
    r'\s*during the notorious incident',
    r'\s*commonly heard during informal everyday conversations across the region',
    r'\s*commonly heard during informal everyday conversations among close peers and family',
    r'\s*commonly encountered across rural and suburban communities',
    r'\s*widely discussed and memorable',
    r'\s*and noticeably overwhelmed by current difficult circumstances',
    r'\s*without receiving any prior advance notice or preparation',
    r'\s*after enduring an unexpectedly grueling and exhausting ordeal',
    r'\s*during a thoroughly chaotic and unpredictable situation',
    r'\s*widely known for creating unexpected humor and harmless confusion',
    r'\s*in an exceptionally hurried and energetic manner',
    r'\s*to an extraordinary and completely unprecedented degree',
    r'\s*despite encountering numerous unexpected obstacles along the way',
    r'\s*during the annual Springfield Whacking Day festival',
    r'\s*at the Springfield Nuclear Power Plant annual company picnic',
    r'\s*according to an investigative report in the Springfield Shopper',
    r'\s*with clean-burning propane and propane accessories',
    r'\s*while standing in the Rainey Street alley holding an Alamo Beer',
    r'\s*during the annual Heimlich County fair lawnmower races',
    r'\s*as officially certified by the Texas Propane Gas Association',
    r'\s*served with a side of freshly seasoned hand-cut french fries',
    r'\s*performed live on the Wagstaff School auditorium stage',
    r'\s*during the chaotic annual Ocean Avenue lobster festival parade',
    r'\s*before the bright morning sun comes up!',
    r'\s*and enjoy the wonderful sunny afternoon!',
    r'\s*while everyone in the room is watching!',
    r'\s*before it gets completely dark outside\?',
    r'\s*across the sunny open courtyard patio',
    r'\s*with all of our cheerful favorite neighbors',
    r'\s*right in the middle of the bright afternoon',
    r'\s*and celebrate together with the entire friendly neighborhood!',
    r'\s*\((?:certified organic cultivar|native agricultural specimen|specialized vegetative botanical plant tissue|infused with aromatic botanical botanicals and spices|artisanally prepared regional culinary staple|documented extensively throughout contemporary regional archives|officially recognized across regional historical documentation|featured headlining stand-up comic and secret set performer|in its classic original format|regular \d+(?:st|nd|rd|th)-grade student at P\.S\. 118 in Brooklyn|curious adventurous toddler from the playpen gang|historic seaside storefront located near Wonder Wharf|regular chalkboard special price with local sales tax|member of the Seymour Bay downtown business council|prominent Heimlich County civic board member|Hank\'s longtime varsity high school football teammate|veteran Arlen High School athletic booster club member|local Springfield animal shelter rescue|Springfield commercial toll-free dispatch line|industrial chemical additive from the nuclear plant|national daily broadsheet newspaper|historic big-box retailer operated by S\.S\. Kresge|former Walmart CEO and corporate board executive|regular prime-time television series ensemble cast member|frequent guest host, musical guest, and comedy sketch performer|certified clean-burning propane system specialist|fleshy indehiscent botanical structure with protective skin|lifelong resident of Rainey Street in Arlen, Texas|full televised quote|frequent longtime customer sitting at Moe\'s Tavern|delivered with dramatic comedic emphasis(?:\s+throughout the scene)?|dedicated senior employee at Strickland Propane|serving as a prominent historical and cultural benchmark|heirloom garden variety|introduced in the episode|veteran Krustylu Studios television cast performer|popular local novelty item purchased at the Kwik-E-Mart|established under formal administrative and municipal jurisdiction|featured in original broadcast|eccentric Springfield Elementary School staff member|Springfield Nuclear Power Plant safety department employee|eccentric lifelong citizen of greater Springfield|complete uncut dialogue line|frequent podcast improviser, character actor, and comedy guest|recurring podcast comedy guest, actor, and bad-movie enthusiast|eccentric Ocean Avenue seaside neighborhood resident|botanical angiosperm plant family with varied cultivars|frequent longtime patron dining at Bob\'s counter|hilarious touring guest comedian, actor, and close personal friend|veteran employee at the Wonder Wharf family boardwalk|eccentric citizen of O-Town in Rocko\'s Modern Life|classic 90s animated Nicktoon fan-favorite character|camper in Bunk 13 at Camp Anawanna|counselor at Camp Anawanna in Salute Your Shorts|featured prominently throughout the storyline|rescued outdoor neighborhood alley cat|staff faculty member at Wagstaff Middle School|recurring ensemble performer on the Nickelodeon sketch stage|certified organic harvest from specialty orchards|champion pedigree racing greyhound|traditionally aged in oak barrels for distinct flavor|frequent late-night talk show guest and comedy performer|SNL alumnus & frequent podcast improviser|historic town square bronze memorial monument|purebred prize-winning show dog|touring stand-up headliner and comedy club veteran|Saturday Night Live repertory player|inaugural television broadcast season|premiering on prime-time television|celebrated fall television premiere|official network syndication release year|officially debuted during prime-time broadcast television programming|special chalkboard lunch combo with fries and a soda|regular chalkboard special price with local sales tax|value meal promotion served with hand-cut fries|everyday discount chalkboard special price|direct telephone customer support hotline|emergency dispatch switchboard number|official twenty-four-hour broadcast hotline|Springfield commercial dispatch line with twenty-four-hour answering service|inaugural legislative charter session|fall administrative opening|statewide constitutional convention|interim municipal governance charter|major municipal downtown fire|severe commercial district blaze|great town square fire disaster|inaugural North Texas agricultural exposition|first regional industrial exhibition|grand opening celebration fair|initial conference realignment vote|formal membership announcement session|preliminary athletic conference agreement|initial television network development|early broadcast programming negotiations|regional telecast launch announcement|original 45 RPM mono single release|extended studio album track version|unreleased studio session demo recording|Gold-certified radio broadcast edit|recorded live in concert with orchestral backing|alternate studio outtake with acoustic instrumentation|classic single recorded during original studio sessions|chart-topping Billboard Hot 100 hit release)\)'
]

MASTER_RE = re.compile('|'.join(MASTER_STRIP_PATTERNS), re.IGNORECASE)

def strip_synthetic(text):
    if not isinstance(text, str):
        return text
    cur = MASTER_RE.sub('', text).strip()
    # Normalize internal quotes and spaces
    cur = re.sub(r'\s+([,\.!\?])', r'\1', cur)
    cur = re.sub(r'\s{2,}', ' ', cur)
    # Fix standalone quote artifacts
    if cur.startswith('\"') and cur.endswith('\"'):
        pass
    elif cur.startswith('\"') and cur.count('\"') == 1:
        cur = cur + '\"'
    elif cur.endswith('\"') and cur.count('\"') == 1:
        cur = '\"' + cur
    # Clean accidental Season prefixes on years/numbers
    m_season_bug = re.match(r'^Season\s+(\d{3,4})$', cur)
    if m_season_bug:
        cur = m_season_bug.group(1)
    return cur.strip()

print("Master stripper compiled successfully.")
