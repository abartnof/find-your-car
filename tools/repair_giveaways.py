#!/usr/bin/env python3
"""
Systematic Giveaway Auditor & Fix Script for Find Your Car Quiz.
Inspects and repairs spoilers, self-answering prompts, parenthetical giveaways, and tagline hints across src/questions.json and tools/staging/*_clean.json.
"""

import json
import os
import glob
import re

QUESTIONS_PATH = "src/questions.json"
STAGING_DIR = "tools/staging"

def load_data():
    with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(QUESTIONS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=0)

def main():
    questions = load_data()
    print(f"Loaded {len(questions)} questions from {QUESTIONS_PATH}")

    fixes = {}

    # ==========================================
    # 1. SPECIFIC EXAMPLES & TARGETED AUDIT
    # ==========================================

    # 14519: Soulja Boy
    fixes[14519] = {
        'options': ['Crank That', 'Kiss Me Thru the Phone', 'Turn My Swag On', 'Yahhh!']
    }

    # 2932: Bob's Burgers Boyz4Now
    fixes[2932] = {
        'q': "What is the title of the Boyz4Now Halloween-themed hit single about being terrified of romance?",
        'options': ['"The Right Number of Boys"', '"Whisper in Your Locker"', '"I Love You So Much (It\'s Scary)"', '"Someday We\'ll Touch Hands"']
    }

    # 13218: Miss Congeniality director
    fixes[13218] = {
        'q': "Which filmmaker wrote the hit Sandra Bullock romantic comedy 'Miss Congeniality' and directed her in 'Two Weeks Notice'?",
        'options': ['Jon Turteltaub', 'Andy Tennant', 'Garry Marshall', 'Marc Lawrence']
    }

    # 14922: Tag Team
    fixes[14922] = {
        'q': "Which Miami bass party anthem by Tag Team reached #2 on the Billboard Hot 100 in 1993, featuring the energetic chant 'Party people! Say, ho!'?",
        'options': ['Whoot, There It Is', 'Tootsee Roll', "C'mon N' Ride It (The Train)", 'Whoomp! (There It Is)']
    }

    # ==========================================
    # 2. INGREDIENTS PARENTHETICAL SPOILERS
    # ==========================================
    fixes[15624] = {
        'options': ['Shuba', 'Olivier salad', 'Mimosa salad', 'Vinaigrette salad']
    }
    fixes[15634] = {
        'options': ['Katsuobushi', 'Niboshi', 'Kombu', 'Shiitake']
    }
    fixes[15640] = {
        'options': ['Konjac', 'Yuba', 'Kamaboko', 'Chikuwa']
    }
    fixes[15741] = {
        'q': "Which Modena specialty spread, traditionally known as 'cunza', is made of finely beaten pork lard, rosemary, and garlic, spread over warm tigelle?",
        'options': ['Lardo di Colonnata', 'Pesto alla Trapanese', 'Nduja', 'Pesto Modenese']
    }
    fixes[15752] = {
        'options': ['Doubanjiang', 'Tianmianjiang', 'Hoisin sauce', 'Chujang']
    }
    fixes[15782] = {
        'options': ['Pork shoulder', 'Pork belly', 'Pork tenderloin', 'Spare ribs']
    }
    fixes[15796] = {
        'options': ['Debris', 'Au jus', 'Remoulade', 'Potlikker']
    }
    fixes[15806] = {
        'options': ['Loose meat sandwich', 'Patty melt', 'Sloppy Joe', 'Chopped cheese']
    }
    fixes[15963] = {
        'options': ['Sumeshi', 'Genmai', 'Mochigome', 'Haiga-mai']
    }
    fixes[16002] = {
        'options': ['Char Siu', 'Siu Yuk', 'Lechon Kawali', 'Pork belly adobo']
    }
    fixes[16004] = {
        'options': ['Dongpo Pork', 'Hong Shao Rou', 'Twice Cooked Pork', 'Mao Family Chicken']
    }
    fixes[16010] = {
        'options': ['Lu Rou Fan', 'Hainanese Chicken Rice', 'Claypot Rice', 'Bibimbap']
    }
    fixes[16031] = {
        'options': ['Barberries', 'Dried sour cherries', 'Sumac berries', 'Pomegranate arils']
    }
    fixes[16032] = {
        'options': ['Abgoosht', 'Ghormeh Sabzi', 'Fesenjan', 'Khoresht Gheimeh']
    }
    fixes[16054] = {
        'options': ['Paya', 'Nihari', 'Haleem', 'Yakhni']
    }
    fixes[16057] = {
        'options': ['Ajwain', 'Kalonji', 'Fennel seeds', 'Coriander seeds']
    }
    fixes[16078] = {
        'options': ['Pigeon peas', 'Black beans', 'Red kidney beans', 'Pink beans']
    }
    fixes[16083] = {
        'options': ['Tapioca starch', 'Cornstarch', 'Potato starch', 'Arrowroot starch']
    }
    fixes[16085] = {
        'options': ['Achiote oil', 'Dendê oil', 'Sesame oil', 'Avocado oil']
    }
    fixes[16093] = {
        'options': ['Causa Rellena', 'Papa Rellena', 'Papa a la Huancaína', 'Pastel de Papa']
    }
    fixes[16106] = {
        'options': ['Slaked lime', 'Baking soda', 'Potassium carbonate', 'Wood ash only']
    }
    fixes[16138] = {
        'options': ['Ogiri', 'Soumbala', 'Iru', 'Sumbala']
    }
    fixes[16150] = {
        'options': ['Melktert', 'Malva pudding', 'Koeksister', 'Hertzoggie']
    }
    fixes[16154] = {
        'options': ['Yassa', 'Thieboudienne', 'Ndole', 'Maafe']
    }
    fixes[16191] = {
        'options': ['Amaretti', 'Brutti ma buoni', 'Cantucci', 'Ricciarelli']
    }
    fixes[16210] = {
        'q': "Which round, enclosed French puff pastry pie from the Loiret region is filled with rich frangipane almond cream and decorated with spiral score marks?",
        'options': ['Pithiviers', 'Kouign-amann', 'Tarte Tatin', 'Mille-feuille']
    }

    # ==========================================
    # 3. MOVIE TAGLINES SELF-ANSWERING FIXES
    # ==========================================
    fixes[752] = {
        'q': "What was the official tagline for the 1980 slasher classic set at Camp Crystal Lake?"
    }
    fixes[762] = {
        'q': "What was the official tagline for Quentin Tarantino's 1994 nonlinear crime masterpiece starring John Travolta and Samuel L. Jackson?"
    }
    fixes[771] = {
        'q': "What was the official tagline for Roman Polanski's 1974 neo-noir classic starring Jack Nicholson as private investigator J.J. Gittes?"
    }
    fixes[781] = {
        'q': "What was the official tagline for Ridley Scott's 2000 historical epic starring Russell Crowe as betrayed Roman warrior Maximus?"
    }
    fixes[794] = {
        'q': "What was the official tagline for Harold Ramis's 1993 comedy classic starring Bill Murray as a cynical Pittsburgh weatherman stuck in a time loop?"
    }
    fixes[804] = {
        'q': "What was the official tagline for Michel Gondry's 2004 romantic sci-fi drama starring Jim Carrey and Kate Winslet undergoing memory-erasure?"
    }
    fixes[806] = {
        'q': "What was the official tagline for the 1994 Oscar-winning drama starring Tom Hanks as an Alabama man traversing 20th-century American history?"
    }
    fixes[816] = {
        'q': "What was the official tagline for the 1989 fantasy-drama starring Kevin Costner as an Iowa corn farmer who builds a baseball diamond?"
    }
    fixes[819] = {
        'q': "What was the official tagline for Oliver Stone's 1999 ensemble football drama starring Al Pacino as coach Tony D'Amato?"
    }
    fixes[820] = {
        'q': "What was the official tagline for Peter Berg's 2004 high school football drama set in Odessa, Texas, starring Billy Bob Thornton?"
    }
    fixes[823] = {
        'q': "What was the official tagline for John G. Avildsen's 1984 martial arts drama starring Ralph Macchio and Pat Morita?"
    }
    fixes[835] = {
        'q': "What was the official tagline for Alfonso Cuarón's 2006 dystopian thriller about a world facing two decades of human infertility?"
    }
    fixes[885] = {
        'q': "What was the official tagline for Zack Snyder's 2009 superhero adaptation featuring Rorschach, Dr. Manhattan, and Nite Owl?"
    }
    fixes[900] = {
        'q': "What was the official tagline for the 1984 Steven Spielberg prequel following an intrepid archaeologist into Pankot Palace?"
    }
    fixes[911] = {
        'q': "What was the official tagline for John Carpenter's 1981 sci-fi action film starring Kurt Russell as Snake Plissken?"
    }
    fixes[914] = {
        'q': "What was the official tagline for Brian De Palma's 1976 Stephen King adaptation starring Sissy Spacek as a telekinetic high schooler?"
    }
    fixes[915] = {
        'q': "What was the official tagline for Rob Reiner's 1990 psychological thriller starring Kathy Bates as an obsessive fan holding a novelist captive?"
    }
    fixes[919] = {
        'q': "What was the official tagline for Gore Verbinski's 2002 supernatural horror film centered on a cursed videotape that kills viewers in seven days?"
    }
    fixes[933] = {
        'q': "What was the official tagline for Jennifer Kent's 2014 psychological horror film about a grieving mother and a sinister pop-up book monster?"
    }
    fixes[934] = {
        'q': "What was the official tagline for David Robert Mitchell's 2014 indie horror film about a supernatural entity passed through sexual encounters?"
    }
    fixes[944] = {
        'q': "What was the official tagline for the 2021 action-thriller starring Bob Odenkirk as an unassuming suburban father with a lethal past?"
    }
    fixes[945] = {
        'q': "What was the official tagline for George Miller's 2015 post-apocalyptic spectacle starring Charlize Theron as Imperator Furiosa?"
    }
    fixes[953] = {
        'q': "What was the official tagline for Paul Greengrass's 2007 trilogy-capper starring Matt Damon as an amnesiac black-ops operative?"
    }
    fixes[986] = {
        'q': "What was the official tagline for Peter Weir's 2003 Napoleonic naval epic starring Russell Crowe as Captain Jack Aubrey?"
    }
    fixes[987] = {
        'q': "What was the official tagline for Wolfgang Petersen's 2000 disaster drama starring George Clooney as the captain of the Andrea Gail?"
    }
    fixes[990] = {
        'q': "What was the official tagline for Steve Miner's 1999 creature comedy starring Bill Pullman and Bridget Fonda hunting a 30-foot prehistoric crocodile?"
    }
    fixes[998] = {
        'q': "What was the official tagline for Danny Boyle's 2002 post-apocalyptic thriller starring Cillian Murphy waking from a coma into a rage-virus epidemic?"
    }
    fixes[1004] = {
        'q': "What was the official tagline for Chris Columbus's 1999 sci-fi drama starring Robin Williams as the android NDR-114 'Andrew'?"
    }
    fixes[1012] = {
        'q': "What was the official tagline for the 2011 sci-fi sports film starring Hugh Jackman as an ex-fighter coaching a robot boxer?"
    }
    fixes[1018] = {
        'q': "What was the official tagline for John Singleton's 2003 Miami-set street racing sequel starring Paul Walker and Tyrese Gibson?"
    }
    fixes[1019] = {
        'q': "What was the official tagline for the 2006 Justin Lin car-culture sequel following Sean Boswell into Japan's underground drift racing scene?"
    }
    fixes[1023] = {
        'q': "What was the official tagline for Brian De Palma's 1996 spy thriller starring Tom Cruise as IMF agent Ethan Hunt?"
    }
    fixes[1024] = {
        'q': "What was the official tagline for John Woo's 2000 action sequel starring Tom Cruise as Ethan Hunt tracking the Chimera virus?"
    }

    # ==========================================
    # 4. DIRECT ANSWER & PROMPT SPOILER FIXES
    # ==========================================

    # UT Austin
    fixes[525] = {
        'q': "The Longhorns' football stadium was renamed in 1996 in honor of which legendary three-time national championship-winning head coach?"
    }

    # Late Night TV
    fixes[579] = {
        'q': "Jay Leno returned as host of The Tonight Show in what year following the high-profile late-night conflict with Conan O'Brien?"
    }
    fixes[707] = {
        'q': "Which witty talk-show host, known for intellectual conversations with figures like Truman Capote, Salvador Dalí, and Groucho Marx, hosted an acclaimed namesake late-night show on ABC?"
    }

    # Texas History
    fixes[1173] = {
        'q': "What Texas revolutionary leader rallied volunteers to storm San Antonio with the famous call: 'Who will go with old Ben into San Antonio?'"
    }
    fixes[1189] = {
        'options': ['Adelsverein', 'Germania Bund', 'Hanseatic League', 'Freethinkers Association']
    }
    fixes[1204] = {
        'options': ["Terry's Texas Rangers", "Hood's Brigade", "Ross's Brigade", "Green's Brigade"]
    }
    fixes[1243] = {
        'options': ['LULAC', 'MALDEF', 'The Brown Berets', 'La Raza Unida Party']
    }

    # Famous Canadians
    fixes[1951] = {
        'q': "Which Emmy-winning Canadian actress played Sarah Manning and numerous other clones in BBC America's sci-fi thriller series 'Orphan Black'?"
    }

    # RuPaul's Drag Race
    fixes[2134] = {
        'q': "In 'All Stars 3', which queen eliminated herself in a shocking twist by writing her own name on the lipstick?"
    }
    fixes[2135] = {
        'options': ['A giant beach ball', 'India Ferrah herself', 'A pair of feather boas', 'An oversized telephone']
    }

    # Ann Zimmerman
    fixes[2303] = {
        'options': ['CHIP and Medicaid', 'Social Security Disability Insurance', 'Medicare Part D', 'Veterans Health Administration']
    }

    # Bob's Burgers
    fixes[2725] = {
        'q': "What precious oceanic substance (whale vomit) do the Belcher kids discover washed ashore on the beach in Season 4?",
        'options': ['Black Pearl', 'Ambergris', 'A pirate sunken coin', 'Lost Rolex watch']
    }
    fixes[2757] = {
        'q': "Which variety of mildly hot Mexican chili pepper is the star ingredient of the 'Picasso Burger' on Bob's chalkboard?"
    }
    fixes[2809] = {
        'q': "What is the title of the showstopper mashup ballad Gene and Courtney sing together at the climax of the fall musical episode?"
    }
    fixes[2810] = {
        'q': "In a hilarious Season 3 parody of E.T., what high-tech talking bathroom fixture voiced by Jon Hamm does Gene befriend in the woods?",
        'options': ['The Outside Toilet', 'The Porcelain Prince', 'The Cyber Commode', 'The Golden Throne']
    }
    fixes[2873] = {
        'options': ['"Taffy Butt"', '"Goonies \'R\' Good Enough"', '"Kids on the Loose"', '"Sugar Rush Dreams"']
    }
    fixes[2886] = {
        'q': "In the two-part Christmas musical special, what mythical antlered, anti-Santa creature do the Belcher children investigate after Linda's ornaments are stolen?"
    }
    fixes[2888] = {
        'q': "In Season 11's finale, what Rocky Horror-style cult film does Bob take Tina to see at the theater, desperately hoping she will love it?"
    }
    fixes[2900] = {
        'q': "Which comedic actress provides the distinctive voice of Tina's bratty Wagstaff classmate and nemesis Tammy Larsen?",
        'options': ['Kristen Schaal', 'Sarah Silverman', 'Jenny Slate', 'Megan Mullally'],
        'answer': 2
    }

    # Comedy Bang! Bang!
    fixes[2979] = {
        'q': "Which Aaron Lewis lyric from Staind triggers an immediate singing musical drop whenever spoken on the podcast?"
    }
    fixes[3017] = {
        'q': "What holiday figure is reimagined by Paul F. Tompkins as a gravel-voiced warrior who battles dark mystical forces like the Krampus?"
    }
    fixes[3040] = {
        'q': "What character played by Andy Daly is an eccentric frankfurter enthusiast who was struck by lightning and wears a water-skiing outfit?"
    }

    # How Did This Get Made?
    fixes[3184] = {
        'q': "What food is Jason Mantzoukas deathly allergic to in real life, a fact frequently referenced whenever meals or diner scenes come up?",
        'options': ['Peanuts', 'Shellfish', 'Eggs', 'Soy'],
        'answer': 2
    }
    fixes[3224] = {
        'q': "What 1986 action film featured Sylvester Stallone eating pizza with scissors and playing tough street cop Marion Cobretti?"
    }
    fixes[3290] = {
        'q': "Which 1987 romantic comedy covered on the show features a department store worker who falls in love with a window display figure that magically comes to life?"
    }

    # 90s Nickelodeon
    fixes[3670] = {
        'q': "In the 'Rugrats' episode 'A Rugrats Passover', which character casts herself in the role of the tyrannical Pharaoh during the storytelling?"
    }
    fixes[3806] = {
        'q': "On 'Legends of the Hidden Temple', what was the water-crossing opening challenge called that teams navigated to reach the steps of knowledge?"
    }
    fixes[3814] = {
        'options': ['Dan Schneider', 'Josh Server', 'Kenan Thompson', 'Mark Saul']
    }
    fixes[3872] = {
        'q': "In 'The Ren & Stimpy Show', what breakfast food was advertised by the superhero who flew backward and served slices directly from his head?"
    }
    fixes[3875] = {
        'q': "In 'Rugrats', what was the name of the robotic, shell-bearing monster that battles Reptar in the movie the babies watch?"
    }

    # 30 Rock
    fixes[4266] = {
        'options': ['Terry and Janet', 'Lemon and Criss Jr.', 'Tracy and Jenna', 'Frank and Cerie']
    }
    fixes[4386] = {
        'options': ['Jenna DeCarlo', 'Jenna Vance', 'Jenna Maroney', 'Jenna Smith']
    }
    fixes[4409] = {
        'q': "Which Apollo 11 astronaut famously guest-starred as himself in Season 4, yelling at the night sky with Liz Lemon?"
    }

    # Arrested Development
    fixes[4460] = {
        'q': "What first name does Dr. Fünke paint across his own bare chest in red letters during his audition for the Blue Man Group?"
    }
    fixes[4491] = {
        'q': "What is the name of Oscar Bluth's citrus orchard property?"
    }
    fixes[4514] = {
        'q': "What one-word question does Michael repeatedly and incredulously utter whenever George Michael mentions his girlfriend Ann?"
    }
    fixes[4620] = {
        'options': ['Graft versus host disease', 'Blue skin', 'Temporary muteness', 'Severe blindness']
    }
    fixes[4621] = {
        'options': ['Dr. Stein', 'Dr. Fishman', 'Dr. Zuckerkorn', 'Dr. Roberts']
    }
    fixes[4622] = {
        'options': ['"He\'s gone."', '"It looks like he\'s dead."', '"He\'s going to be all right"', '"There is nothing left of him."']
    }
    fixes[4642] = {
        'q': "What performance art company does Tobias obsessively attempt to join, leading him to constantly cover his skin in blue diamond lotion?",
        'options': ['Blue Man Group', 'Cirque du Soleil', 'The Living Theatre', 'Stomp'],
        'answer': 0
    }
    fixes[4656] = {
        'q': "What comedy legend played the wheelchair-bound, wildly energetic character Uncle Jack who needed to be carried everywhere?"
    }
    fixes[4664] = {
        'options': ['Sharpshooter Medal', 'Marksmanship Medal', 'Purple Heart', 'Distinguished Service Cross']
    }
    fixes[4701] = {
        'q': "What did Buster call the mechanical prize-grabbing arcade game where he honed his uncanny retrieval skills?"
    }
    fixes[4722] = {
        'q': "Which mother-son duo dominated the annual Motherboy pageant costume competition for years with matching elaborate outfits?",
        'options': ['Michael and Lucille', 'Buster and Lucille', 'George Michael and Lindsay', 'G.O.B. and Lucille']
    }
    fixes[4733] = {
        'options': ['Stan Sitwell', 'Bob Loblaw', 'Wayne Jarvis', 'Ted']
    }

    # Ben Folds
    fixes[4797] = {
        'q': "What iconic Ben Folds Five song was re-recorded phonetically in Japanese with the translated title 'Kane Kaese' ('Give Me My Money Back')?",
        'options': ['"Battle of Who Could Care Less"', '"Song for the Dumped"', '"Brick"', '"Kate"'],
        'answer': 1
    }
    fixes[4837] = {
        'q': "Which legendary 'Star Trek' actor did Ben Folds collaborate with on the critically acclaimed 2004 album 'Has Been'?"
    }
    fixes[4852] = {
        'q': "What animated film soundtrack did Ben Folds contribute multiple original songs to in 2006, along with an updated version of 'Rockin' the Suburbs'?"
    }
    fixes[4855] = {
        'q': "What was the title of the 2009 double-disc release that included remixable audio stems alongside official mastered versions of Ben's leaked 'fake songs'?",
        'options': ['The Dublin Sessions', 'Way to Normal: The Prank Edition', 'Stems and Seeds', 'Super D'],
        'answer': 2
    }
    fixes[4880] = {
        'q': "In 2013, Ben Folds Five released an in-concert album capturing their reunion tour under what simple, single-word title?",
        'options': ['Live', 'Tour', 'Reunion', 'Alive']
    }
    fixes[4915] = {
        'q': "Which Ben Folds Five song about youthful indecision begins its second verse with the line: 'Dad said, 'Son, you're fucking high''?"
    }
    fixes[4938] = {
        'q': "'Everything you know is wrong / But you can still be happy' is the upbeat chorus lyric of which classic Ben Folds Five song?"
    }
    fixes[4971] = {
        'options': ['Merton', 'David After Dentist', 'Charlie Bit My Finger', 'Keyboard Cat']
    }
    fixes[4974] = {
        'q': "For which Season 5 episode of NBC's 'Community' did Ben Folds write and perform an original noir-themed song about a mysterious campus coin bandit?",
        'options': ['"Brick"', '"Ass Crack Bandit"', '"The Luckiest"', '"Kate"'],
        'answer': 1
    }
    fixes[5039] = {
        'q': "On the 2023 album 'What Matters Most', which agonizing slow-motion activity serves as the titular metaphor for being trapped in an inescapable relationship conflict?",
        'options': ['Pedaling a rented paddleboat out on a lake', 'Sitting on a stalled ski lift', 'Getting trapped in a revolving door', 'Riding a tandem bicycle uphill']
    }
    fixes[5040] = {
        'q': "Which title track from Ben Folds' 2023 album deals with the bittersweet experience of sorting through a deceased friend's storage locker?"
    }
    fixes[5044] = {
        'q': "Which of the following original songs was written and performed by Ben Folds for the 2006 animated DreamWorks soundtrack 'Over the Hedge'?",
        'options': ['Family of Me', 'Accidentally in Love', "You've Got a Friend in Me", 'Immigrant Song'],
        'answer': 0
    }

    # Brooklyn Nine-Nine
    fixes[5061] = {
        'q': "Which badass detective in the 99th precinct is so fiercely private about her personal life that nobody even knows her real home address or if her name is real?"
    }
    fixes[5233] = {
        'options': ['The PB&J', 'The Dynamic Duo', 'The Nine-Nine Enforcers', 'The Pontiac Patrol']
    }
    fixes[5285] = {
        'q': "In the critically acclaimed Season 4 episode dealing with racial profiling, what favorite bedtime toy belonging to his twin daughters was Terry searching for outside his home?",
        'options': ['A plush stuffed toy cow', 'A toy fire truck', 'A plastic tiara', 'A baby doll']
    }

    # King of the Hill
    fixes[5817] = {
        'options': ['Lumbar air cushion', 'Orthotic gluteal prosthetic', 'Back brace', 'High-density foam seat']
    }
    fixes[5845] = {
        'options': ['A singing bowl', 'A silver bell', 'The mirror', 'A pair of beads']
    }
    fixes[5871] = {
        'options': ['Joe Jack', 'Leon', 'Enrique', 'Donna']
    }
    fixes[5950] = {
        'q': "What was the name of the local video rental store Hank frequented before it was driven out of business by Mega Lo Video?"
    }
    fixes[6042] = {
        'q': "What was the stage name of Peggy's stylish best friend who turned out to be a biological man named Jamie?",
        'options': ['Carolyn', 'Cherry', 'Celeste', 'Carla']
    }
    fixes[6086] = {
        'options': ['"Bobby\'s Water"', 'Sweet tea', 'Kool-Aid with honey', 'Gatorade knockoff']
    }
    fixes[6115] = {
        'options': ['"Pro-Pain!"', '"Grand Theft Auto"', '"Doom"', '"Madden NFL"']
    }
    fixes[6129] = {
        'q': "Who stepped in as a passionate substitute shop teacher at Tom Landry Middle School when the class was threatened with cancellation?",
        'options': ['Mr. Earl', 'Hank Hill', 'Mr. Twilley', 'Coach Sauers']
    }
    fixes[6134] = {
        'q': "Which fast-talking character was voiced by guest star Brad Pitt in the Season 8 episode where Boomhauer's brother gets engaged?",
        'options': ['Patch Boomhauer', 'Rad Thibodeaux', 'Hoyt Platter', 'Trip Larsen']
    }

    # Parks and Recreation
    fixes[6279] = {
        'q': "What did Andy Dwyer call the Mouse Rat song he wrote inspired by his disastrous fall into the construction trench?"
    }
    fixes[6349] = {
        'options': ['Paul Schneider', 'Rob Lowe', 'Nick Offerman', 'Chris Pratt']
    }
    fixes[6403] = {
        'options': ['The Pawnee Gay Men\'s Chorus', 'The Sweetums Vocal Troupe', 'The Snakehole Lounge Choir', 'The Pawnee Chamber Singers']
    }
    fixes[6425] = {
        'q': "How is Mayor Gergich's first name famously misspelled on his gravestone in the series finale?",
        'options': ['Gerry', 'Jerry', 'Larry', 'Terry']
    }

    # Taskmaster UK
    fixes[6671] = {
        'options': ['That Alex is tiny ("Little Alex Horne")', 'That Alex is a giant', 'That Alex is invisible', 'That Alex wears stilts']
    }
    fixes[6708] = {
        'q': "In Series 1, how were the five contestants split up for the team tasks?",
        'options': ['A team of 2 and a team of 3', 'A team of 1 and a team of 4', 'Completely individual for the entire series', 'Random pairings that shifted every episode']
    }

    # Friends
    fixes[6771] = {
        'q': "In the Season 1 Thanksgiving episode, what giant superhero dog parade balloon breaks free from the Macy's Thanksgiving Day Parade and floats over Manhattan?"
    }
    fixes[6927] = {
        'q': "In Season 6, what Japanese concept of total situational awareness (which Rachel and Phoebe point out is actually freshwater eel) does Ross claim to possess?"
    }
    fixes[7130] = {
        'options': ['Her actual biological father', 'A famous actor', 'The frame insert model', 'An album cover musician']
    }
    fixes[7143] = {
        'options': ['Al Zebooker', 'Billy Crystal', 'Bobcat Goldthwait', 'Pauly Shore']
    }
    fixes[7154] = {
        'q': "What miniature tabletop bar game do Joey and Chandler obsessively play in their apartment instead of having a dining table?",
        'options': ['Air hockey', 'Table tennis', 'Foosball', 'Billiards'],
        'answer': 2
    }
    fixes[7257] = {
        'q': "What 1995 soundtrack album featuring The Rembrandts, Hootie & the Blowfish, and Lou Reed reached the top 5 of the Billboard 200?",
        'options': ['Friends Original Soundtrack', 'Central Perk Melodies', 'Coffeehouse Jams', 'The One with All the Music']
    }
    fixes[7306] = {
        'options': ['Leslie Moonves', 'Peter Roth', 'Warren Littlefield', 'Don Ohlmeyer']
    }
    fixes[7352] = {
        'q': "When the hit NBC sitcom premiered on French television in 1996, under what title did it air in France and French-speaking territories?",
        'options': ['Les Amis', 'Copains de Manhattan', 'Friends', 'La Bande']
    }
    fixes[7353] = {
        'q': "When broadcast on German television, under what title was the hit NBC comedy series aired?",
        'options': ['Sechs in Manhattan', 'Friends', 'Die Kumpel', 'New Yorker Nächte']
    }
    fixes[7416] = {
        'options': ['Sega Game Gear', 'Atari Lynx', 'Game Boy', 'Tamagotchi']
    }
    fixes[7420] = {
        'options': ['Courteney Cox', 'Lisa Kudrow', 'Jennifer Aniston', 'Matt LeBlanc']
    }
    fixes[7422] = {
        'options': ['John Bennett Perry', 'Keith Morrison', 'Dick Van Dyke', 'Alan Thicke']
    }
    fixes[7437] = {
        'q': "What popular soft drink brand featured a young Matt LeBlanc roller-skating through warm city streets in a memorable 1990 TV commercial?",
        'options': ['Cherry 7-Up', 'Coca-Cola', 'Pepsi', 'Mountain Dew'],
        'answer': 0
    }
    fixes[7484] = {
        'options': ['Katy Perry', 'Taylor Swift', 'Selena Gomez', 'Lady Gaga']
    }
    fixes[7531] = {
        'q': "Which actress portrayed Ross's ex-wife Carol Willick in the pilot episode before being replaced by Jane Sibbett for the rest of the series?"
    }
    fixes[7545] = {
        'options': ['Conan O\'Brien', 'Jay Leno', 'David Letterman', 'Jon Stewart']
    }
    fixes[7555] = {
        'options': ['Katie the monkey', 'Marcel Jr.', 'Bubbles', 'Cheeta']
    }

    # 90s Sitcoms
    fixes[7559] = {
        'q': "In the Season 6 episode 'The Switch', what is Kramer's first name finally revealed to be after years of mystery?"
    }
    fixes[7748] = {
        'options': ['Kevin Clash', 'Jim Henson', 'Frank Oz', 'Steve Whitmire']
    }
    fixes[7847] = {
        'q': "What New York City borough serves as the residential setting for Doug and Carrie Heffernan?"
    }
    fixes[8180] = {
        'q': "Which Paul Reiser and Helen Hunt NBC comedy established a shared universe with Friends through Ursula Buffay, and with Seinfeld via Kramer subletting Paul's apartment?",
        'options': ['Mad About You', 'Frasier', 'Wings', 'NewsRadio']
    }
    fixes[8221] = {
        'q': "What self-titled Fox comedy set in Detroit anchored the network's successful Thursday night programming from 1992 to 1997?"
    }
    fixes[8237] = {
        'q': "In 1999, which quirky legal comedy-drama created by David E. Kelley won the Primetime Emmy Award for Outstanding Comedy Series for Fox?",
        'options': ['Ally McBeal', 'Spin City', 'Dharma & Greg', 'NewsRadio'],
        'answer': 0
    }
    fixes[8246] = {
        'options': ['Dan Foliart and Howard Pearl', 'Danny Elfman', 'Mark Snow', 'W.G. Snuffy Walden']
    }
    fixes[8254] = {
        'q': "Who performed the catchy opening vocal theme song for the hit 1990s sitcom 'Sister, Sister' in its early seasons?",
        'options': ['SWV', 'Tia and Tamera Mowry', 'En Vogue', 'TLC'],
        'answer': 1
    }
    fixes[8308] = {
        'q': "Which music manager and executive originally conceived the premise for The Fresh Prince of Bel-Air based on his own life story of moving from East L.A. to Beverly Hills?",
        'options': ['Benny Medina', 'Quincy Jones', 'Russell Simmons', 'Clarence Avant']
    }
    fixes[8340] = {
        'options': ['Small Soldiers', 'Antz', 'The Prince of Egypt', 'Toy Story 2']
    }
    fixes[8413] = {
        'options': ['Rider Strong', 'Will Friedle', 'Ben Savage', 'Matthew Lawrence']
    }
    fixes[8416] = {
        'options': ['Tony Shalhoub', 'Steve Buscemi', 'Larry David', 'Hank Azaria']
    }
    fixes[8418] = {
        'options': ['Jennie Garth', 'Shannen Doherty', 'Tori Spelling', 'Alyssa Milano']
    }
    fixes[8515] = {
        'options': [
            "What is Chandler Bing's actual job?",
            "What is the name of Joey's childhood imaginary friend?",
            "How many towel categories does Monica have?",
            "What is Rachel's actual favorite movie?"
        ]
    }
    fixes[8526] = {
        'q': "What surreal Season 4 episode of NewsRadio transported the entire WNYX office staff onto a futuristic vessel in deep orbit?"
    }

    # Frasier
    fixes[8670] = {
        'q': "In 'An Affair to Forget', what foreign language did Marta learn while working for a family in Guatemala, allowing her to converse with Maris's fencing instructor?",
        'options': ['German', 'Italian', 'French', 'Portuguese'],
        'answer': 0
    }
    fixes[8734] = {
        'q': "In a memorable Season 2 episode, what private boundary of Daphne's does Frasier repeatedly violate while trying to replace a mattress, causing her to threaten to quit?"
    }
    fixes[8754] = {
        'q': "In a memorable Season 3 episode, what classic two-player board game does Frasier obsessively try to defeat Martin at, suffering repeated humiliating losses?",
        'options': ['Scrabble', 'Backgammon', 'Checkers', 'Chess']
    }
    fixes[9054] = {
        'q': "In the series finale, what closing farewell words does Frasier speak into his KACL microphone before signing off the Seattle airwaves for good?"
    }
    fixes[9058] = {
        'options': ['Goodnight, Seattle.', "Here's to new beginnings.", "I'm listening.", '"Wish me luck."']
    }
    fixes[9100] = {
        'q': "Which iconic television comedy legend who played news producer Mary Richards called into Frasier's radio show in Season 2 as Marjorie?"
    }
    fixes[9144] = {
        'options': ['Grace Under Fire', 'Home Improvement', 'Roseanne', 'Full House']
    }
    fixes[9156] = {
        'options': ['All 11 seasons', '9 seasons', '7 seasons', '5 seasons']
    }
    fixes[9196] = {
        'options': [
            'The Space Needle perfectly framed in front of downtown skyscrapers',
            'Mount Rainier hovering directly above Puget Sound ferries',
            'The Pacific Ocean visible on the western horizon',
            'The Kingdome immediately adjacent to Lake Union'
        ]
    }
    fixes[9200] = {
        'options': ['My Coffee with Niles', 'The Good Son', 'Dinner at Eight', 'Author, Author']
    }
    fixes[9201] = {
        'options': ['The Matchmaker', 'The Innkeepers', 'An Affair to Forget', 'Flour Child']
    }
    fixes[9202] = {
        'q': "Which celebrated Season 5 episode of 'Frasier' written by Joe Keenan was nominated for the Primetime Emmy Award for Outstanding Writing?",
        'options': ['Voyage of the Damned', 'Room Service', 'Halloween', 'The Ski Lodge'],
        'answer': 3
    }
    fixes[9203] = {
        'options': ['Merry Christmas, Mrs. Moskowitz', 'Frasier\'s Curse', 'Dial M for Martin', 'Three Valentines']
    }
    fixes[9217] = {
        'q': "In the classic farcical radio drama episode 'Ham Radio', what was the name of the elderly Foley sound effects artist who loses his voice before broadcast?",
        'options': ['Mel White', 'Gil Chesterton', 'Mr. Wing', 'Noel Shempsky'],
        'answer': 2
    }
    fixes[9232] = {
        'options': ['The Candidate', 'The Matchmaker', 'Adventures in Paradise', 'A Word to the Wiseguy']
    }
    fixes[9233] = {
        'options': ['Out with Dad', 'They\'re Playing Our Song', 'Something Borrowed, Someone Blue', 'Radio Days']
    }
    fixes[9246] = {
        'q': "Which legendary director from 'Cheers' directed the pilot and dozens of episodes of 'Frasier'?",
        'options': ['James Burrows', 'Pamela Fryman', 'Andy Ackerman', 'David Trainer'],
        'answer': 0
    }
    fixes[9247] = {
        'q': "Before agreeing to reprise Frasier Crane in a spin-off, what character concept did Kelsey Grammer initially want to play in a new sitcom?",
        'options': [
            'A paralyzed, eccentric media mogul living in a Manhattan penthouse',
            'A cynical political consultant in Washington D.C.',
            'A disgraced Ivy League law professor starting over',
            'A high-end art dealer navigating romance in Paris'
        ],
        'answer': 0
    }
    fixes[9256] = {
        'options': ['Woody Gets An Election', 'One for the Road', 'The Last Picture Show', 'Bar Wars VII']
    }
    fixes[9257] = {
        'options': ['Do Not Forsake Me, O\' My Postman', 'Rebecca Gaines, Rebecca Loses', 'The King of Beers', 'It\'s a Wonderful Wife']
    }
    fixes[9296] = {
        'options': ['Jane Leeves', 'Faith Ford', 'Julia Campbell', 'Lisa Darr']
    }
    fixes[9297] = {
        'q': "Which British slapstick sketch comedy show featured Jane Leeves as one of the glamorous 'Hill's Angels' dancers early in her career?"
    }

    # Will & Grace
    fixes[9364] = {
        'options': ['None', 'Michael', 'Patrick', 'Edward']
    }
    fixes[9548] = {
        'q': "What was the name of the hunky closeted NYPD officer Jack dated across multiple seasons?"
    }
    fixes[9729] = {
        'q': "While Will & Grace was filmed in front of a live studio audience in Los Angeles, where were the iconic exterior building shots actually filmed?",
        'options': ['New York City', 'Chicago', 'Boston', 'Philadelphia']
    }
    fixes[9761] = {
        'options': [
            'To file a restraining order against an obsessive stalker',
            'To negotiate a Broadway musical contract',
            'To contest an unfair copyright lawsuit',
            'To draft an adoption pre-nuptial agreement'
        ]
    }
    fixes[9799] = {
        'options': ['Columbia University', 'NYU', 'Harvard', 'Vassar']
    }
    fixes[9820] = {
        'options': ['"Boardroom Bunny"', '"Cheaters"', '"Lows in the Mid-Eighties"', '"Mad Dogs and Average Men"']
    }
    fixes[9851] = {
        'options': ['Megan Mullally', 'Debra Messing', 'Sean Hayes', 'Eric McCormack']
    }
    fixes[9897] = {
        'q': "In a special Season 11 tribute episode, what classic 1950s sitcom do Grace, Jack, and Karen recreate in fantasy dream sequences with Lucie Arnaz guest-starring?"
    }
    fixes[9990] = {
        'options': ['"The New Adventures of Old Christine"', '"Two and a Half Men"', '"The Big Bang Theory"', '"Mike & Molly"']
    }
    fixes[10011] = {
        'options': ['Seinfeld', 'Friends', 'Mad About You', 'The Fresh Prince of Bel-Air']
    }
    fixes[10024] = {
        'options': ['Eric McCormack', 'Sean Hayes', 'Debra Messing', 'Megan Mullally']
    }
    fixes[10034] = {
        'options': ['Nicollette Sheridan', 'Christine Baranski', 'Bebe Neuwirth', 'Julia Louis-Dreyfus']
    }

    # 80s TV Shows
    fixes[10301] = {
        'q': "Which notorious Colombian drug kingpin, responsible for the murder of Tubbs' brother, did Crockett and Tubbs relentlessly pursue across early seasons of Miami Vice?"
    }
    fixes[10442] = {
        'options': ['Allison Sugarbaker', 'Bernice Clifton', 'Carlene Dobber', 'Mary Jo Shively']
    }
    fixes[10591] = {
        'q': "Which flamboyant British Culture Club frontman guest-starred on The A-Team when Face accidentally booked him to perform at a country-western saloon?"
    }
    fixes[10629] = {
        'q': "What cold, chilling question did Thomas Magnum ask KGB operative Ivan before executing him in the legendary Season 3 two-part episode?"
    }
    fixes[10633] = {
        'q': "What was the title of the Season 7 finale where Magnum was shot, drifted between life and death as a spirit, and was originally meant to be the series finale?"
    }
    fixes[10675] = {
        'q': "What was the name of J.R.'s petite, rebellious niece played by Charlene Tilton on Dallas?"
    }
    fixes[10686] = {
        'q': "Which actress and former wife of Elvis Presley portrayed Bobby Ewing's old flame Jenna Wade on Dallas from 1983 to 1988?"
    }
    fixes[10776] = {
        'options': ['Al Jarreau', 'George Benson', 'Kenny Loggins', 'Michael McDonald']
    }
    fixes[10787] = {
        'q': "In Moonlighting's stylish Season 3 episode, what brassy Billy Joel track from 'The Bridge' soundtracked David Addison's elaborate dream sequence dance?"
    }
    fixes[10822] = {
        'q': "Which legendary production company, founded by Mary Tyler Moore and Grant Tinker, produced Remington Steele and St. Elsewhere?",
        'options': ['Universal Television', 'MTM Enterprises', 'Aaron Spelling Productions', 'Stephen J. Cannell Productions']
    }
    fixes[10857] = {
        'q': "What was the on-air broadcast title of the two-hour television movie that launched Bruce Willis and Cybill Shepherd's detective series on ABC in March 1985?",
        'options': ['Moonlighting', 'Blue Moon Detective Agency', 'Tears of a Model', 'The Case of the Smuggled Diamonds']
    }
    fixes[10878] = {
        'options': ['Mike Post', 'Jan Hammer', 'Stu Phillips', 'Dominic Frontiere']
    }
    fixes[10903] = {
        'options': ['Cheers patrons', 'The Golden Girls', 'Taxi drivers', 'Barney Miller detectives']
    }
    fixes[10975] = {
        'options': ['Chocolate candy bars', 'Chewing gum', 'Peanut butter', 'Baking flour']
    }
    fixes[11005] = {
        'options': ['Michael Hagarty', 'Harry McGraw', 'Dennis Stanton', 'Mort Metzger']
    }
    fixes[11028] = {
        'options': ['21 Jump Street', 'Miami Vice', 'Starsky & Hutch', 'The A-Team']
    }
    fixes[11122] = {
        'options': ['Cut... it... out!', 'Have mercy!', 'How rude!', 'You got it, dude!']
    }
    fixes[11155] = {
        'q': "Which groundbreaking blue-collar sitcom set in the fictional town of Lanford debuted on ABC in 1988 starring John Goodman and a titular comedian?"
    }

    # The Simpsons
    fixes[11178] = {
        'q': "What annual May 10th Springfield holiday involves driving snakes into the center of town and clubbing them with sticks?"
    }
    fixes[11212] = {
        'q': "In Season 4, what eye-catching piece of custom apparel convinces Homer to launch his own snow-clearing business?",
        'options': ['A custom satin jacket with embroidery', 'A faux-fur ushanka winter hat', 'A pair of steel-toed leather work boots', 'A neon-yellow reflective snow jumpsuit'],
        'answer': 0
    }
    fixes[11243] = {
        'q': "In the very first 'Treehouse of Horror', which classic Edgar Allan Poe poem about grief and a persistent black bird is recited with James Earl Jones narrating?"
    }
    fixes[11332] = {
        'q': "In Season 5, what adult education course about relationship dynamics does Homer Simpson teach at the Springfield Learning Center?"
    }
    fixes[11341] = {
        'q': "In 'Homer the Great', what exalted title is Homer granted by the Stonecutters after a sacred birthmark is discovered on his body?"
    }
    fixes[11377] = {
        'q': "In Season 8, what radical, sunglasses-wearing cartoon dog voiced by Homer is added to Krusty's hit cartoon to boost declining ratings?"
    }
    fixes[11443] = {
        'q': "When Homer and his family attend the Movementarian retreat at the compound, what mind-numbing six-hour orientation film are they forced to watch?"
    }
    fixes[11550] = {
        'q': "Which iconic sci-fi actor guest-starred as himself at the Bi-Mon-Sci-Fi-Con and sang 'Luke, be a Jedi tonight' in 'Mayored to the Mob'?"
    }
    fixes[11562] = {
        'q': "What crispety, crunchety peanut-butter candy bar featured Bart Simpson in a long-running 1990s ad campaign with the slogan 'Nobody better lay a finger on my...'?"
    }
    fixes[11567] = {
        'q': "What town motto word coined for Jebediah Springfield in 'Lisa the Iconoclast' ('A noble spirit _____ the smallest man') was officially added to Merriam-Webster in 2018?"
    }
    fixes[11581] = {
        'q': "What real-life street in Portland, Oregon (which was also Matt Groening's mother's maiden name) provided the surname for Springfield's inept police chief?"
    }
    fixes[11590] = {
        'q': "What word coined by writer David X. Cohen in 'Lisa the Iconoclast' ('It's a perfectly _____ word') was added to the Oxford English Dictionary in 2013?"
    }
    fixes[11594] = {
        'options': ['Portland', 'Eugene', 'Seattle', 'Spokane']
    }
    fixes[11596] = {
        'options': ['Margaret', 'Marjorie', 'Marguerite', 'Mary']
    }
    fixes[11614] = {
        'q': "In 1991, what major championship sporting event featured an iconic animated promo where Homer correctly picked the Washington Redskins to win?",
        'options': ['Super Bowl XXVI', '1991 World Series', 'NBA Finals', 'Stanley Cup Finals']
    }
    fixes[11648] = {
        'options': ['The Simpsons', 'Bally Midway', 'Stern Pinball', 'Williams Special']
    }

    # SNL
    fixes[11713] = {
        'q': "Which legendary blind Motown superstar made a guest appearance on SNL and hilariously failed to win a look-alike contest judged against Eddie Murphy?"
    }
    fixes[11735] = {
        'q': "What famous invitation did Mike Myers repeatedly declare as Dieter, the black-turtlenecked German avant-garde talk show host, before gyrating to techno music?"
    }
    fixes[11816] = {
        'q': "What introductory catchphrase did Tracy Morgan's unqualified, animal-hating nature show host repeatedly exclaim on his Safari Planet show?"
    }
    fixes[11819] = {
        'q': "Which real Clinton administration Attorney General made a surprise cameo appearance to dance alongside Will Ferrell during her namesake sketch in 2001?"
    }
    fixes[11936] = {
        'q': "Which pop superstar was the musical guest on the Season 49 finale in May 2024 and performed her breakthrough smash hit 'Espresso'?",
        'options': ['Billie Eilish', 'Dua Lipa', 'Sabrina Carpenter', 'Olivia Rodrigo'],
        'answer': 2
    }
    fixes[11944] = {
        'q': "Which legendary singer appeared as a surprise guest on Ego Nwodim's parody talk show to be interviewed by her own fictionalized self?"
    }
    fixes[11957] = {
        'q': "In a classic 2012 sketch parodying his FX comedy series, what historical U.S. President did Louis C.K. portray as an awkward stand-up comedian living in NYC?",
        'options': ['Abraham Lincoln', 'George Washington', 'Andrew Jackson', 'Theodore Roosevelt']
    }
    fixes[12013] = {
        'options': ['Stefon', 'The Continental', 'Jacob the Bar Mitzvah Boy', 'Herb Welch']
    }
    fixes[12238] = {
        'options': ['The Triple-Trac razor', 'The Mach Speed razor', 'The Quattro Sharp', 'The Infinity Edge']
    }
    fixes[12301] = {
        'q': "Which Academy Award-nominated actor and brother of Dennis Quaid was an SNL cast member during the 1985-1986 season?"
    }
    fixes[12302] = {
        'options': ['Dead last', 'Number 100', 'Top 50', 'Runner-up']
    }
    fixes[12334] = {
        'options': ['Thomas Middleditch', 'Martin Starr', 'Kumail Nanjiani', 'Zach Woods']
    }

    # Fruits & Veggies
    fixes[12531] = {
        'options': ['Petiole', 'Blade', 'Root', 'Stem internode']
    }
    fixes[12601] = {
        'options': ['(E,Z)-3,6-nonadien-1-ol', 'Linalool', 'Myrcene', 'Geraniol']
    }
    fixes[12627] = {
        'q': "What historic Kent research station developed the globally famous numbered series of dwarfing rootstocks (such as M9 and M26) for apple trees?"
    }
    fixes[12702] = {
        'q': "In 1873, which classic red-skinned potato variety produced the seedling that botanist Luther Burbank selected to develop the legendary Burbank potato?",
        'options': ['Early Rose', 'Yukon Gold', 'Kennebec', 'Katahdin'],
        'answer': 0
    }
    fixes[12722] = {
        'options': ['Central leader system', 'Spindle bush system', 'Open center system', 'Trellis cordons']
    }
    fixes[12729] = {
        'options': ['Buddha\'s hand', 'Etrog', 'Corsican citron', 'Diamante citron']
    }
    fixes[12886] = {
        'options': ['Bhut Jolokia', 'Habanero', 'Trinidad Moruga Scorpion', 'Carolina Reaper']
    }
    fixes[12933] = {
        'options': ['Penticton Peach Festival', 'Kelowna Apple Fair', 'Vernon Cherry Jubilee', 'Osoyoos Grape Gala']
    }
    fixes[12934] = {
        'q': "What southwest Ohio village hosts an annual Sauerkraut Festival that draws hundreds of thousands of visitors to celebrate fermented cabbage?"
    }
    fixes[12941] = {
        'options': ['Porrophagus', 'Alliumphile', 'Scorodite', 'Cepaicus']
    }

    # Romantic Comedies
    fixes[12981] = {
        'q': "What is Robbie Hart's primary musical occupation in the 1998 Adam Sandler comedy set in 1985?"
    }
    fixes[13040] = {
        'q': "In Woody Allen's 'Midnight in Paris', at the stroke of what hour does the antique Peugeot arrive each night to transport Gil back to the 1920s?"
    }
    fixes[13088] = {
        'q': "In 'The Princess Bride', which Spanish fencing master repeatedly declares: 'Hello. My name is... You killed my father. Prepare to die'?"
    }

    # Streaming TV Shows
    fixes[13537] = {
        'q': "In the pilot of Netflix's hit crime drama, what money laundering scheme does financial advisor Marty Byrde pitch to save his life from Camino Del Rio?"
    }
    fixes[13574] = {
        'q': "In Apple TV+'s dystopian workplace thriller, what controversial brain surgery separates employees' work memories from their personal memories?"
    }
    fixes[13591] = {
        'q': "In Apple TV+'s spy thriller, what derogatory nickname is given to the disgraced MI5 service rejects relegated to Slough House under Jackson Lamb?"
    }
    fixes[13647] = {
        'q': "What is the on-air title of the fictional breakfast news program hosted by Alex Levy on the UBA network?",
        'options': ['Daybreak America', 'The Morning Show', 'Good Morning USA', 'Rise & Shine']
    }
    fixes[13711] = {
        'q': "In the post-apocalyptic saga based on Emily St. John Mandel's novel, what fictional graphic novel created by Miranda Carroll becomes a sacred text for survivors?"
    }
    fixes[13731] = {
        'q': "In the Season 1 finale of 'Andor', which deceased resident of Ferrix delivers a posthumous holographic funeral speech inciting the citizens to 'Fight the Empire!'?",
        'options': ['Maarva Andor', 'Bix Caleen', 'Salman Paak', 'Taramyn Barcona'],
        'answer': 0
    }
    fixes[13791] = {
        'q': "Which pair of media giants initially founded Hulu in 2007 as a joint venture streaming platform to compete with YouTube?",
        'options': ['NBCUniversal and News Corporation', 'CBS and Viacom', 'Disney and WarnerMedia', 'Sony Pictures and Time Warner'],
        'answer': 0
    }
    fixes[13904] = {
        'options': ['Bell Works', 'MetLife Complex', 'AT&T Center', 'Prudential Plaza']
    }
    fixes[13910] = {
        'options': ['Lancaster House', 'Chatsworth House', 'Blenheim Palace', 'Highclere Castle']
    }
    fixes[13915] = {
        'options': ["Emory University's Briarcliff Campus", 'Peachtree Sanitarium', 'Decatur State Hospital', 'Buckhead Memorial']
    }
    fixes[13922] = {
        'options': ['4 World Trade Center', 'One Vanderbilt', 'Chrysler Building', 'Empire State Building']
    }
    fixes[13950] = {
        'options': ['NBC', 'CBS', 'ABC', 'The CW']
    }

    # Billboard Hits
    fixes[14023] = {
        'q': "Which Four Tops soul anthem topped the Billboard Hot 100 for two weeks in October 1966 with Levi Stubbs passionately shouting the dramatic lead vocals?"
    }
    fixes[14137] = {
        'q': "Which Barry Gibb-written title track for the 1978 musical film starring John Travolta and Olivia Newton-John hit #1 on the Billboard Hot 100, performed by Frankie Valli?"
    }
    fixes[14149] = {
        'q': "Which 1973 soft rock classic by Seals and Crofts reached #6 on the Billboard Hot 100, featuring the line 'blowing through the jasmine in my mind'?"
    }
    fixes[14156] = {
        'q': "Which 1977 acoustic-led philosophical ballad by Kansas reached #6 on the Billboard Hot 100, featuring a famous fingerpicked guitar melody and violin solo?"
    }
    fixes[14249] = {
        'q': "Which Toto soft-rock hit reached #1 on the Billboard Hot 100 in February 1983, featuring the famous chorus about blessing the rains down on a distant continent?"
    }
    fixes[14340] = {
        'q': "Which Montell Jordan party track reached #1 on the Billboard Hot 100 in 1995, declaring 'It's Friday night, and I feel all right'?"
    }
    fixes[14350] = {
        'q': "Which Next R&B party anthem topped the Billboard Hot 100 for five weeks in 1998, describing the friction of slow-dancing on the club dance floor?"
    }
    fixes[14390] = {
        'q': "Which member of the Fugees won five Grammy Awards in 1999 for her critically acclaimed, multi-platinum solo debut album 'The Miseducation of...'?"
    }
    fixes[14413] = {
        'q': "Which 1998 breakout single by Jay-Z, produced by The 45 King, sampled a children's chorus from the Broadway musical 'Annie'?",
        'options': ['Hard Knock Life', 'Can I Get A...', 'Money, Cash, Hoes', 'Nigga What, Nigga Who']
    }
    fixes[14443] = {
        'q': "Which rapid-fire pop-rock single by Barenaked Ladies reached #1 on the Billboard Hot 100 in October 1998 with references to Sailor Moon and Kurosawa films?"
    }
    fixes[14455] = {
        'q': "Which bounce anthem by Juvenile (featuring Mannie Fresh and Lil Wayne) became Cash Money Records' breakout national hit in 1999?"
    }
    fixes[14478] = {
        'q': "Which Neptunes-produced party anthem topped the Billboard Hot 100 for seven weeks in summer 2002, advising clubgoers to take off all their clothes?"
    }
    fixes[14525] = {
        'q': "Which orchestral pop-rock anthem from Coldplay's 2008 Brian Eno-produced fourth album became the British band's first US Billboard Hot 100 #1?"
    }
    fixes[14534] = {
        'q': "Which post-grunge rock band formed by a fifth-place American Idol finalist saw their self-titled debut album become the top-selling album of 2007?"
    }
    fixes[14543] = {
        'q': "What self-titled debut album by the girl group formed on MTV's 'Making the Band 3' debuted at #1 on the Billboard 200 in 2006?"
    }
    fixes[14571] = {
        'q': "Which 1991 novelty dance hit by Right Said Fred was officially credited as interpolated into the rhythm and cadence of Taylor Swift's 2017 #1 hit 'Look What You Made Me Do'?"
    }
    fixes[14575] = {
        'q': "Which Drake single spent 10 weeks at #1 in summer 2018, fueled by comedian Shiggy's viral 'Kiki, do you love me?' dance challenge?"
    }
    fixes[14607] = {
        'q': "Maroon 5 and Cardi B's collaboration 'Girls Like You' tied an all-time Billboard Hot 100 record by spending how many weeks inside the top 10?"
    }
    fixes[14634] = {
        'q': "Which Walk the Moon indie-pop anthem peaked at #4 on the Billboard Hot 100 in 2015, featuring a backless dress and retro 80s dance rhythm?"
    }
    fixes[14678] = {
        'q': "Which martial-arts revenge film directed by Quentin Tarantino provided the storyline and title inspiration for SZA's 2023 Hot 100 #1 hit?"
    }
    fixes[14696] = {
        'q': "Glass Animals' sleeper hit 'Heat Waves' broke the record for the most total weeks on the Billboard Hot 100 by charting for how many weeks?"
    }
    fixes[14726] = {
        'q': "Which Mustard-produced West Coast diss track by Kendrick Lamar aimed at Drake debuted at #1 on the Billboard Hot 100 in May 2024?"
    }
    fixes[14733] = {
        'q': "Which Tommy Richman alternative R&B single reached #2 on the Billboard Hot 100 in May 2024 after going viral on TikTok with its catchy falsetto hook?"
    }
    fixes[14745] = {
        'q': "Which Charli XCX studio album featuring a lime-green cover reached #3 on the Billboard 200 in summer 2024, sparking a defining viral summer aesthetic?"
    }
    fixes[14799] = {
        'q': "Which blind Motown multi-instrumentalist had a 22-year gap between his 1963 breakthrough #1 'Fingertips' and his 1985 chart-topper 'Part-Time Lover'?"
    }
    fixes[14808] = {
        'options': ['Matchbox 20', 'Counting Crows', 'Third Eye Blind', 'Goo Goo Dolls']
    }
    fixes[14877] = {
        'q': "Which British synth-pop group topped the Billboard Hot 100 in 1986 with a mid-tempo R&B ballad written and produced by Jimmy Jam and Terry Lewis?"
    }
    fixes[14898] = {
        'q': "On which 1980 solo album (nicknamed 'Melt') did Peter Gabriel and engineer Hugh Padgham pioneer the famous gated reverb drum sound on the track 'Intruder'?",
        'options': ['Peter Gabriel 3', 'So', 'Us', 'Security']
    }
    fixes[14924] = {
        'q': "What 1996 Quad City DJ's party track served as the theme song for the live-action and animated basketball blockbuster starring Michael Jordan?"
    }
    fixes[14950] = {
        'q': "Which Los Angeles hip-hop producer, known for defining the 2010s ratchet sound, produced Kendrick Lamar's 2024 #1 smash 'Not Like Us'?",
        'options': ['Mustard', 'Metro Boomin', 'Hit-Boy', 'Mike WiLL Made-It']
    }
    fixes[14956] = {
        'q': "Which 1972 Black Sabbath piano ballad was covered by Ozzy Osbourne and sampled for the hook in Eminem's 2010 song 'Going Through Changes'?"
    }

    # Cheers
    fixes[15045] = {
        'options': ['A live sheep', 'A baby pig', 'A noisy goat', 'A caged rooster']
    }
    fixes[15141] = {
        'q': "What musical instrument does Frasier Crane frequently play and sing showtunes alongside in the bar?"
    }
    fixes[15247] = {
        'options': ['Abe Burrows', 'Neil Simon', 'George S. Kaufman', 'Moss Hart']
    }
    fixes[15336] = {
        'options': ['One dollar', 'One thousand dollars', 'Five thousand dollars', 'Ten thousand dollars']
    }
    fixes[15407] = {
        'q': "Before writers renamed him Norm Peterson, what first name was given to the barfly in the original pilot script (matching the actor's real first name)?",
        'options': ['George', 'John', 'Ted', 'Woody']
    }
    fixes[15413] = {
        'options': ['Fred Dryer', 'William Devane', 'Ed O\'Neill', 'Tom Selleck']
    }
    fixes[15449] = {
        'options': ['Harry the Hat', 'Slick Harry', 'Fast Eddie', 'Magic Harry']
    }

    # Ingredients general
    fixes[15487] = {
        'q': "What staple liquid sweetener made from equal parts water and granulated sugar is an essential component in classic cocktail making?"
    }
    fixes[15522] = {
        'q': "Which distinctive French grape brandy produced in Gascony is traditionally column-distilled and aged in oak barrels?"
    }
    fixes[15527] = {
        'q': "Which Japanese muskmelon-flavored liqueur with an electric neon green hue is the key ingredient in a Japanese Slipper and neon melon cocktails?"
    }
    fixes[15533] = {
        'q': "Which Italian vermouth produced by Carpano in Turin combines classic sweet vermouth with a point of bitterness from quina, meaning 'a point and a half' in Piedmontese?"
    }
    fixes[15543] = {
        'q': "Which aniseed-flavored national spirit of Greece turns cloudy milky-white when water or ice is added due to the spontaneous emulsification louche effect?"
    }
    fixes[15596] = {
        'q': "Which tangy, deep-red ground spice derived from dried Mediterranean shrub berries gives Fattoush salad its distinctive tart, lemony zing?"
    }
    fixes[15682] = {
        'q': "Which traditional cultured, slightly acidic dairy beverage provides the rich tangy base for classic homemade ranch dressing?"
    }
    fixes[15686] = {
        'q': "What golden nectar produced by bees is blended with prepared mustard and mayonnaise to create classic sweet sandwich dressing?"
    }
    fixes[15995] = {
        'q': "Which Japanese savory cabbage pancake, whose name translates to 'grilled as you like', is griddled on a teppan and topped with sweet brown sauce, kewpie mayo, and bonito flakes?"
    }
    fixes[16066] = {
        'q': "Which traditional dough made of nixtamalized corn flour and lard is wrapped in corn husks or banana leaves and steamed to make Mexican Tamales?"
    }
    fixes[16183] = {
        'q': "Which Australasian dessert, created in honor of a touring Russian ballerina, features a crisp meringue shell with a marshmallow center topped with whipped cream and fresh fruit?"
    }

    # The Golden Girls
    fixes[16332] = {
        'q': "In Season 4, what prestigious hometown civic honor does Rose mistakenly receive before discovering she wasn't the intended recipient?",
        'options': ['St. Olaf Butter Queen', 'St. Olaf Woman of the Year', 'Lutefisk Princess of Crow Wing County', 'Miss Dairy Days']
    }
    fixes[16434] = {
        'q': "In Season 6, what sacred heirloom does Sophia acquire from a visiting relative that she believes brings miracles, causing major drama in the house?"
    }
    fixes[16528] = {
        'options': ['Seven nominations', 'Five nominations', 'Three nominations', 'Nine nominations']
    }
    fixes[16529] = {
        'options': ['Seven nominations', 'Five nominations', 'Three nominations', 'Nine nominations']
    }
    fixes[16581] = {
        'q': "Which Season 2 episode focusing on the girls' neurotic neighboring couple served as the backdoor pilot for a spin-off sitcom?",
        'options': ["'The Neighbor Next Door'", "'Dr. Weston Moves In'", "'Empty Nests'", "'Miami Physicians'"]
    }
    fixes[16621] = {
        'options': ['Danny Thomas', 'Bob Hope', 'Shecky Greene', 'Milton Berle']
    }
    fixes[16657] = {
        'options': ['Bea Arthur', 'Estelle Getty', 'Betty White', 'Rue McClanahan']
    }
    fixes[16720] = {
        'options': ['Marc Cherry', 'Michael J. LaRue', 'Brandon Tartikoff', 'Norman Lear']
    }
    fixes[16728] = {
        'options': ['Lee Grant', 'Elaine Stritch', 'Doris Roberts', 'Marion Ross']
    }
    fixes[16737] = {
        'options': ['Betty White', 'Rue McClanahan', 'None of them', 'Estelle Getty']
    }
    fixes[16745] = {
        'options': ['Rue McClanahan', 'Bea Arthur', 'None of them', 'Estelle Getty']
    }

    print(f"Total targeted fixes defined: {len(fixes)}")

    # Automatically align answer index whenever options were modified without an explicit answer
    aligned_answers = 0
    for idx, change in fixes.items():
        if 'options' in change and 'answer' not in change:
            orig = questions[idx]
            orig_ans = orig['options'][orig['answer']]
            c_orig = re.sub(r'\s*\([^)]*\)', '', orig_ans).strip().lower()
            c_orig = re.sub(r'[\"\'\s]', '', c_orig)
            
            # 1. Exact match against cleaned option
            exact = [i for i, o in enumerate(change['options']) if re.sub(r'[\"\'\s]', '', o.lower()) == c_orig]
            if len(exact) == 1:
                change['answer'] = exact[0]
                aligned_answers += 1
                continue
            
            # 2. Substring / fuzzy match
            fuzzy = []
            for o_idx, opt in enumerate(change['options']):
                c_opt = re.sub(r'\s*\([^)]*\)', '', opt).strip().lower()
                c_opt = re.sub(r'[\"\'\s]', '', c_opt)
                if c_orig in c_opt or c_opt in c_orig:
                    fuzzy.append((o_idx, opt))
            if len(fuzzy) == 1:
                change['answer'] = fuzzy[0][0]
                aligned_answers += 1

    print(f"Aligned answer index for {aligned_answers} options updates.")

    # Keep track of old_q -> new_item to update staging clean files
    old_to_new = {}

    for idx, change in fixes.items():
        original_item = questions[idx]
        old_q = original_item['q']
        
        # Apply changes
        for k, v in change.items():
            original_item[k] = v
            
        old_to_new[old_q] = original_item

    # Validate all questions
    print("Validating dataset integrity...")
    assert len(questions) == 16759, f"Question count mismatch: {len(questions)} != 16759"
    for i, q in enumerate(questions):
        assert isinstance(q['q'], str) and len(q['q'].strip()) > 0, f"Empty question at {i}"
        assert isinstance(q['options'], list) and len(q['options']) == 4, f"Invalid options length at {i}: {q}"
        assert len(set(q['options'])) == 4, f"Duplicate options at {i}: {q['options']}"
        assert q['answer'] in (0, 1, 2, 3), f"Invalid answer at {i}: {q['answer']}"
        assert q['d'] in (1, 2, 3), f"Invalid difficulty at {i}: {q['d']}"

    print("All 16,759 questions passed strict validation!")

    # Save questions.json
    save_data(questions)
    print(f"Saved updated questions to {QUESTIONS_PATH}")

    # Synchronize staging clean files
    print("Updating matching staging clean files...")
    staging_files = glob.glob(os.path.join(STAGING_DIR, "*_clean.json"))
    updated_files_count = 0
    updated_questions_in_staging = 0

    for sfile in staging_files:
        with open(sfile, 'r', encoding='utf-8') as f:
            sdata = json.load(f)
        
        modified = False
        for sitem in sdata:
            sq = sitem.get('q')
            if sq in old_to_new:
                updated_item = old_to_new[sq]
                sitem['q'] = updated_item['q']
                sitem['options'] = updated_item['options']
                sitem['answer'] = updated_item['answer']
                sitem['d'] = updated_item['d']
                modified = True
                updated_questions_in_staging += 1

        if modified:
            with open(sfile, 'w', encoding='utf-8') as f:
                json.dump(sdata, f, ensure_ascii=False, indent=2)
            updated_files_count += 1
            print(f"  Updated staging file: {sfile}")

    print(f"Updated {updated_questions_in_staging} questions across {updated_files_count} staging clean files.")

if __name__ == "__main__":
    main()
