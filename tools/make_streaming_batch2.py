#!/usr/bin/env python3
"""
Generate Batch 2 of Streaming TV Shows trivia (100 questions):
Apple TV+ & Prime Video Flagships: Ted Lasso, Severance, The Morning Show,
Slow Horses, For All Mankind, Silo, Shrinking, The Marvelous Mrs. Maisel,
The Boys, Fleabag, Fallout, Invincible, Reacher, The Rings of Power, Good Omens.
Target: ~28 d1, ~38 d2, ~34 d3.
"""

from streaming_tv_batch_builder import build_batch

BATCH_2 = [
    # 1-15: Ted Lasso (Textual, Metatextual, Extratextual)
    {
        "q": "In Apple TV+'s 'Ted Lasso', which English association football club does American coach Ted Lasso arrive to manage?",
        "correct": "AFC Richmond",
        "distractors": ["West Ham United", "Manchester City", "Everton FC"],
        "d": 1
    },
    {
        "q": "What yellow word is emblazoned on the iconic motivational sign Ted Lasso tapes above his office door?",
        "correct": "BELIEVE",
        "distractors": ["HOPE", "COURAGE", "TOGETHER"],
        "d": 1
    },
    {
        "q": "What homemade treat does Ted Lasso bring to club owner Rebecca Welton every morning for their 'Biscuits with the Boss' chats?",
        "correct": "Shortbread biscuits",
        "distractors": ["Scones", "Chocolate chip cookies", "Lemon bars"],
        "d": 1
    },
    {
        "q": "Which gruff veteran Richmond player famously screams 'He's here, he's there, he's every-fucking-where' about himself in fan chants?",
        "correct": "Roy Kent",
        "distractors": ["Jamie Tartt", "Dani Rojas", "Sam Obisanya"],
        "d": 1
    },
    {
        "q": "What enthusiastic catchphrase is constantly shouted by cheerful Mexican striker Dani Rojas in 'Ted Lasso'?",
        "correct": "Football is life!",
        "distractors": ["Goal is joy!", "Believe every day!", "Richmond forever!"],
        "d": 1
    },
    {
        "q": "In 'Ted Lasso' Season 2, which former kit man betrays Ted and leaks Ted's panic attacks to the press before managing rival West Ham United?",
        "correct": "Nate Shelley",
        "distractors": ["Leslie Higgins", "Will Kitman", "Trent Crimm"],
        "d": 1
    },
    {
        "q": "What support group do Ted, Beard, Higgins, and later Roy Kent form to discuss personal relationships and emotional vulnerabilities?",
        "correct": "The Diamond Dogs",
        "distractors": ["The Greyhounds", "The Richmond Council", "The Locker Room Knights"],
        "d": 2
    },
    {
        "q": "Which actor, who initially served as a staff writer on 'Ted Lasso', was cast as Roy Kent and won consecutive Emmys for the role?",
        "correct": "Brett Goldstein",
        "distractors": ["Brendan Hunt", "Nick Mohammed", "Phil Dunster"],
        "d": 2
    },
    {
        "q": "Which British journalist from 'The Independent' quits his newspaper job to write an in-depth book about Richmond in Season 3?",
        "correct": "Trent Crimm",
        "distractors": ["George Cartrick", "Marcus Mumford", "Rupert Mannion"],
        "d": 2
    },
    {
        "q": "What Emmy record did 'Ted Lasso' achieve with its freshman season in 2021?",
        "correct": "Most Emmy nominations for a freshman comedy series in history with 20 nominations",
        "distractors": [
            "First streaming series to win 12 Emmys in a single night",
            "Highest percentage of viewers watching an Emmy telecast",
            "First British-filmed comedy to sweep all writing and directing categories"
        ],
        "d": 2
    },
    {
        "q": "In the Season 2 Christmas episode 'Carol of the Bells', what instrument does Rebecca Welton play and sing outside Higgins' house?",
        "correct": "Guitar",
        "distractors": ["Piano", "Violin", "Accordion"],
        "d": 3
    },
    {
        "q": "In 'Ted Lasso' Season 3, what Dutch tactical philosophy does Ted accidentally reinvent while hallucinating at an Amsterdam restaurant?",
        "correct": "Total Football",
        "distractors": ["Catenaccio", "Tiki-Taka", "Gegenpressing"],
        "d": 2
    },
    {
        "q": "Who originated the character of Ted Lasso in a series of comedic commercials for NBC Sports' coverage of the Premier League in 2013?",
        "correct": "Jason Sudeikis",
        "distractors": ["Bill Lawrence", "Brendan Hunt", "Joe Kelly"],
        "d": 1
    },
    {
        "q": "What is Coach Beard's actual first name, as revealed in passing by Jane Payne in the series finale?",
        "correct": "Willis",
        "distractors": ["Arthur", "Henry", "Brendan"],
        "d": 3
    },
    {
        "q": "Which real-life soccer stadium in London stands in for AFC Richmond's home ground, Nelson Road?",
        "correct": "Selhurst Park (Crystal Palace F.C.)",
        "distractors": ["Craven Cottage (Fulham F.C.)", "The Den (Millwall F.C.)", "Stamford Bridge (Chelsea F.C.)"],
        "d": 3
    },

    # 16-30: Severance (Textual, Metatextual, Extratextual)
    {
        "q": "In Apple TV+'s 'Severance', what surgical medical procedure surgically separates employees' work memories from their non-work memories?",
        "correct": "The Severance procedure",
        "distractors": ["The Bifurcation protocol", "The Lumon partition", "The Amnesiac division"],
        "d": 1
    },
    {
        "q": "What is the name of the biotechnology corporation that subjects employees to the Severance procedure on its severed floor?",
        "correct": "Lumon Industries",
        "distractors": ["Massive Dynamic", "Veridian Dynamics", "Initech"],
        "d": 1
    },
    {
        "q": "Who stars as Mark Scout, an employee grieving the death of his wife who volunteers for severance at Lumon?",
        "correct": "Adam Scott",
        "distractors": ["Ben Stiller", "Zach Cherry", "Tramell Tillman"],
        "d": 1
    },
    {
        "q": "What department do Mark, Helly, Dylan, and Irving work in on the severed floor of Lumon Industries?",
        "correct": "Macrodata Refinement (MDR)",
        "distractors": ["Optics & Design", "Disposal & Reclamation", "Research & Development"],
        "d": 1
    },
    {
        "q": "In 'Severance', what do the Macrodata Refinement workers actually do on their retro CRT monitors?",
        "correct": "Sort floating numbers that elicit specific emotions into digital bins",
        "distractors": [
            "Transcribe encrypted phone conversations from foreign countries",
            "Censor objectionable words from corporate legal briefs",
            "Delete metadata logs from executive correspondence"
        ],
        "d": 2
    },
    {
        "q": "Who created 'Severance', having written the original pilot script as a spec sample while working an unfulfilling corporate desk job?",
        "correct": "Dan Erickson",
        "distractors": ["Ben Stiller", "Noah Hawley", "Sam Esmail"],
        "d": 2
    },
    {
        "q": "Which Hollywood comedy star directed the majority of 'Severance' Season 1, including the acclaimed pilot and finale?",
        "correct": "Ben Stiller",
        "distractors": ["Adam McKay", "David Wain", "Jay Roach"],
        "d": 1
    },
    {
        "q": "What is the shocking revelation about Helly R's real-world 'Outie' identity revealed in the Season 1 finale?",
        "correct": "She is Helena Eagan, daughter of Lumon CEO Jame Eagan",
        "distractors": [
            "She is an undercover FBI investigator seeking to dismantle Lumon",
            "She is Mark Scout's long-lost younger sister",
            "She is the neurosurgeon who invented the severance brain chip"
        ],
        "d": 1
    },
    {
        "q": "In 'Severance', what coveted reward does Dylan George choose after completing his quarterly refinement quota?",
        "correct": "A Waffle Party",
        "distractors": ["A Finger Trap Party", "A Melon Bar Buffet", "A Disco Dance Experience"],
        "d": 2
    },
    {
        "q": "What is the name of the pseudo-religious founder of Lumon Industries revered through statues, quotes, and the Perpetuity Wing?",
        "correct": "Kier Eagan",
        "distractors": ["Ambrose Eagan", "Pip Eagan", "Leonora Eagan"],
        "d": 2
    },
    {
        "q": "Which legendary Hollywood actor portrays Irving Bailiff, who forms a tender romantic bond with Optics & Design employee Burt Goodman?",
        "correct": "John Turturro",
        "distractors": ["Christopher Walken", "F. Murray Abraham", "Donald Sutherland"],
        "d": 2
    },
    {
        "q": "Who portrays Burt Goodman, the head of Optics & Design opposite John Turturro in 'Severance'?",
        "correct": "Christopher Walken",
        "distractors": ["Alan Arkin", "Martin Sheen", "Michael Keaton"],
        "d": 2
    },
    {
        "q": "In the Season 1 finale of 'Severance', what emergency system switch protocol is activated to awaken the Innies in the outside world?",
        "correct": "The Overtime Contingency",
        "distractors": ["The Glasgow Protocol", "The Open House Protocol", "The Elephant Contingency"],
        "d": 2
    },
    {
        "q": "What phrase does Mark Scout gasp in the final second of the Season 1 cliffhanger finale before the feed cuts out?",
        "correct": "She's alive!",
        "distractors": ["Kier is a lie!", "They're watching us!", "Helly is an Eagan!"],
        "d": 1
    },
    {
        "q": "Which room on the severed floor is used for psychological conditioning and forced repetition of the 'Compunction Statement'?",
        "correct": "The Break Room",
        "distractors": ["The Quiet Room", "The Solitude Tank", "The White Room"],
        "d": 2
    },

    # 31-40: The Morning Show, Slow Horses, Silo, For All Mankind, Shrinking
    {
        "q": "In Apple TV+'s 'The Morning Show', which two Hollywood stars executive produce and lead the series as rival morning news anchors?",
        "correct": "Jennifer Aniston and Reese Witherspoon",
        "distractors": [
            "Jennifer Aniston and Courteney Cox",
            "Reese Witherspoon and Nicole Kidman",
            "Julianna Margulies and Jennifer Aniston"
        ],
        "d": 1
    },
    {
        "q": "Which actor won an Emmy for Outstanding Supporting Actor in a Drama Series for playing the cunning network executive Cory Ellison in 'The Morning Show'?",
        "correct": "Billy Crudup",
        "distractors": ["Mark Duplass", "Steve Carell", "Jon Hamm"],
        "d": 2
    },
    {
        "q": "In Apple TV+'s spy thriller 'Slow Horses', what is the derogatory nickname for Slough House's disgraced MI5 intelligence officers?",
        "correct": "Slow Horses",
        "distractors": ["Lame Ducks", "Dead Wood", "Flatliners"],
        "d": 1
    },
    {
        "q": "Who stars as Jackson Lamb, the slovenly, flatulent, yet brilliant head of Slough House in 'Slow Horses'?",
        "correct": "Gary Oldman",
        "distractors": ["Colin Firth", "Mark Rylance", "Kenneth Branagh"],
        "d": 1
    },
    {
        "q": "Which British writer won the Primetime Emmy Award for Outstanding Writing for a Drama Series in 2024 for 'Slow Horses'?",
        "correct": "Will Smith",
        "distractors": ["Jesse Armstrong", "Peter Morgan", "Mick Herron"],
        "d": 3
    },
    {
        "q": "In Apple TV+'s sci-fi series 'For All Mankind', what historical event alters the space race timeline in the pilot episode?",
        "correct": "The Soviet Union lands the first human, Alexei Leonov, on the Moon before Apollo 11",
        "distractors": [
            "The Apollo 11 lunar module crashes on the moon",
            "The United States launches a manned mission to Mars in 1968",
            "A permanent lunar military base is discovered by NASA satellites"
        ],
        "d": 2
    },
    {
        "q": "Who created 'For All Mankind', having previously reimagined 'Battlestar Galactica'?",
        "correct": "Ronald D. Moore",
        "distractors": ["J.J. Abrams", "David Simon", "Carlton Cuse"],
        "d": 2
    },
    {
        "q": "In Apple TV+'s dystopian series 'Silo', based on Hugh Howey's novels, what fatal punishment is given to residents who request to leave?",
        "correct": "They are sent outside into the toxic atmosphere to clean the exterior sensors before dying",
        "distractors": [
            "They are locked into subterranean incinerator chutes",
            "They are banished into the flooded lowest mining levels",
            "They are executed publicly at the central judicial spire"
        ],
        "d": 2
    },
    {
        "q": "Which Swedish actress stars as engineer Juliette Nichols and executive produces Apple TV+'s 'Silo'?",
        "correct": "Rebecca Ferguson",
        "distractors": ["Noomi Rapace", "Alicia Vikander", "Malin Åkerman"],
        "d": 2
    },
    {
        "q": "In the Apple TV+ comedy 'Shrinking', which screen legend portrays veteran therapist Dr. Paul Rhoades who battles Parkinson's disease?",
        "correct": "Harrison Ford",
        "distractors": ["Michael Douglas", "Tommy Lee Jones", "Robert De Niro"],
        "d": 1
    },

    # 41-55: The Marvelous Mrs. Maisel & Fleabag (Amazon Prime Video)
    {
        "q": "In Amazon Prime Video's 'The Marvelous Mrs. Maisel', what 1950s Greenwich Village comedy venue launches Midge Maisel's stand-up career?",
        "correct": "The Gaslight Cafe",
        "distractors": ["The Bitter End", "The Village Gate", "Cafe Wha?"],
        "d": 1
    },
    {
        "q": "Who created, wrote, and directed 'The Marvelous Mrs. Maisel', bringing her signature rapid-fire dialogue from 'Gilmore Girls'?",
        "correct": "Amy Sherman-Palladino",
        "distractors": ["Mindy Kaling", "Tina Fey", "Jenji Kohan"],
        "d": 1
    },
    {
        "q": "Which actress won an Emmy for Lead Actress in a Comedy Series for portraying Miriam 'Midge' Maisel?",
        "correct": "Rachel Brosnahan",
        "distractors": ["Alex Borstein", "Marin Hinkle", "Jane Lynch"],
        "d": 1
    },
    {
        "q": "Which fiery, tough-talking talent manager is played by Alex Borstein, winning three Primetime Emmy Awards for the role?",
        "correct": "Susie Myerson",
        "distractors": ["Imogene Cleary", "Sophie Lennon", "Shirley Maisel"],
        "d": 1
    },
    {
        "q": "Which real-life pioneering counterculture stand-up comic is portrayed by Luke Kirby as Midge's close friend and mentor?",
        "correct": "Lenny Bruce",
        "distractors": ["Mort Sahl", "George Carlin", "Don Rickles"],
        "d": 2
    },
    {
        "q": "In 'The Marvelous Mrs. Maisel' Season 3, which superstar singer does Midge open for on an international concert tour?",
        "correct": "Shy Baldwin",
        "distractors": ["Harry Belafonte", "Sam Cooke", "Nat King Cole"],
        "d": 2
    },
    {
        "q": "What major milestone did 'The Marvelous Mrs. Maisel' achieve at the 70th Primetime Emmy Awards in 2018?",
        "correct": "It became the first series on a streaming service to win Outstanding Comedy Series",
        "distractors": [
            "It set the all-time comedy record with 15 wins in one year",
            "Rachel Brosnahan became the youngest Lead Comedy winner in history",
            "Amy Sherman-Palladino swept every technical category"
        ],
        "d": 2
    },
    {
        "q": "What department store makeup counter does Midge work at in 'The Marvelous Mrs. Maisel' Season 1?",
        "correct": "B Altman & Co.",
        "distractors": ["Macy's Herald Square", "Lord & Taylor", "Saks Fifth Avenue"],
        "d": 2
    },
    {
        "q": "In the series finale of 'The Marvelous Mrs. Maisel', what television program gives Midge her breakthrough four minutes of live stand-up?",
        "correct": "The Gordon Ford Show",
        "distractors": ["The Ed Sullivan Show", "The Steve Allen Show", "The Tonight Show"],
        "d": 2
    },
    {
        "q": "Who wrote, created, and starred in the critically acclaimed comedy series 'Fleabag'?",
        "correct": "Phoebe Waller-Bridge",
        "distractors": ["Michaela Coel", "Sharon Horgan", "Daisy May Cooper"],
        "d": 1
    },
    {
        "q": "In 'Fleabag' Season 2, which character played by Andrew Scott became an internet cultural phenomenon?",
        "correct": "The Priest (The Hot Priest)",
        "distractors": ["The Bank Manager", "The Lecturer", "The Counselor"],
        "d": 1
    },
    {
        "q": "What kind of animal-themed cafe does Fleabag run in London, opened in memory of her late best friend Boo?",
        "correct": "Guinea pig cafe",
        "distractors": ["Hedgehog cafe", "Cat cafe", "Ferret cafe"],
        "d": 1
    },
    {
        "q": "What signature stylistic device does Fleabag constantly employ to share intimate thoughts with the audience?",
        "correct": "Breaking the fourth wall by glancing and speaking directly into the camera",
        "distractors": [
            "Voiceover narration by an omniscient narrator",
            "Black-and-white flashbacks with subtitles",
            "Subconscious animated doodles on screen"
        ],
        "d": 1
    },
    {
        "q": "What does the Priest uniquely notice about Fleabag that shocks her in Season 2?",
        "correct": "He notices when she disassociates and turns to address the camera",
        "distractors": [
            "He realizes she stole her Godmother's headless sculpture",
            "He guesses her true birth name before she speaks it",
            "He catches her whispering prayers under her breath"
        ],
        "d": 2
    },
    {
        "q": "What major upset victory did 'Fleabag' achieve at the 71st Primetime Emmy Awards in 2019?",
        "correct": "It won Outstanding Comedy Series, defeating heavily favored multi-time winner 'Veep'",
        "distractors": [
            "It won every single guest acting category in television history",
            "It was the first non-American production to win Outstanding Drama Series",
            "Phoebe Waller-Bridge won four acting Emmys in the same night"
        ],
        "d": 2
    },

    # 56-70: The Boys & Invincible (Amazon Prime Video)
    {
        "q": "On Amazon Prime Video's 'The Boys', what corrupt mega-corporation owns and manages the superhero team The Seven?",
        "correct": "Vought International",
        "distractors": ["Oscorp Global", "LexCorp", "Acrodyne Corporation"],
        "d": 1
    },
    {
        "q": "What is the name of the chemical serum engineered by Vought that artificially grants superpowers to infants?",
        "correct": "Compound V",
        "distractors": ["Serum X", "Mirakuru", "Formula 9"],
        "d": 1
    },
    {
        "q": "Which actor portrays the psychopathic, milk-drinking nationalist superhero Homelander in 'The Boys'?",
        "correct": "Antony Starr",
        "distractors": ["Karl Urban", "Jack Quaid", "Chace Crawford"],
        "d": 1
    },
    {
        "q": "What cockney catchphrase does vigilante leader Billy Butcher (Karl Urban) frequently utter in 'The Boys'?",
        "correct": "Diabolical",
        "distractors": ["Bollocks", "Sensational", "Disastrous"],
        "d": 1
    },
    {
        "q": "What is the superhero alter ego of Annie January, who joins The Seven before realizing Vought's monstrous corruption?",
        "correct": "Starlight",
        "distractors": ["Queen Maeve", "Popclaw", "Crimson Countess"],
        "d": 1
    },
    {
        "q": "In 'The Boys' Season 3, which legendary 'Supernatural' actor portrays the awakened World War II superhero Soldier Boy?",
        "correct": "Jensen Ackles",
        "distractors": ["Jared Padalecki", "Jeffrey Dean Morgan", "Misha Collins"],
        "d": 2
    },
    {
        "q": "What is the title of the notorious Season 3 episode of 'The Boys' set at an annual secret superhero orgy in Vermont?",
        "correct": "Herogasm",
        "distractors": ["The Only Man in the Sky", "Glorious Five Year Plan", "Over the Hill with the Swords of a Thousand Men"],
        "d": 2
    },
    {
        "q": "Who created and developed 'The Boys' for Amazon Prime Video, having previously created 'Supernatural'?",
        "correct": "Eric Kripke",
        "distractors": ["Garth Ennis", "Robert Kirkman", "Damon Lindelof"],
        "d": 2
    },
    {
        "q": "What aquatic superhero in 'The Boys' is repeatedly humiliated and forced to eat his own pet octopus, Timothy?",
        "correct": "The Deep (Kevin Moskowitz)",
        "distractors": ["A-Train", "Translucent", "Tek Knight"],
        "d": 2
    },
    {
        "q": "In 'The Boys' comic book series by Garth Ennis and Darick Robertson, which actor's likeness originally inspired the character of Wee Hughie Campbell?",
        "correct": "Simon Pegg",
        "distractors": ["Jack Quaid", "Martin Freeman", "Elijah Wood"],
        "d": 3
    },
    {
        "q": "In Amazon Prime Video's animated superhero series 'Invincible', what alien race does Nolan Grayson (Omni-Man) secretly belong to?",
        "correct": "Viltrumites",
        "distractors": ["Kryptonians", "Kree", "Skrulls"],
        "d": 1
    },
    {
        "q": "Which Oscar-winning actor voices Omni-Man in 'Invincible'?",
        "correct": "J.K. Simmons",
        "distractors": ["Bryan Cranston", "Michael Shannon", "Kurt Russell"],
        "d": 1
    },
    {
        "q": "In the shocking climax of 'Invincible' Season 1 Episode 1, what does Omni-Man do to the Guardians of the Globe?",
        "correct": "He brutally murders every single member of the team in their headquarters",
        "distractors": [
            "He strips them of their superpowers with alien technology",
            "He reveals his true identity to the president and surrenders",
            "He banishes them through a dimensional portal to outer space"
        ],
        "d": 2
    },
    {
        "q": "What devastating weapon does Omni-Man use Mark's body as in the Season 1 finale of 'Invincible' to prove human fragility?",
        "correct": "He forces Mark's body through an oncoming crowded passenger subway train",
        "distractors": [
            "He drops Mark through a skyscraper in downtown Chicago",
            "He hurls Mark into an erupting volcano in Hawaii",
            "He throws Mark into an orbiting space station"
        ],
        "d": 2
    },
    {
        "q": "Which comic book creator wrote both 'The Walking Dead' and the graphic novel series 'Invincible' upon which the show is based?",
        "correct": "Robert Kirkman",
        "distractors": ["Mark Millar", "Alan Moore", "Brian Michael Bendis"],
        "d": 2
    },

    # 71-85: Fallout, Reacher, The Rings of Power, Good Omens
    {
        "q": "In Amazon Prime Video's 2024 adaptation of 'Fallout', what Vault number does naive protagonist Lucy MacLean emerge from?",
        "correct": "Vault 33",
        "distractors": ["Vault 101", "Vault 111", "Vault 76"],
        "d": 1
    },
    {
        "q": "Which actor portrays Cooper Howard, the mutated 200-year-old gunslinging bounty hunter known as The Ghoul in 'Fallout'?",
        "correct": "Walton Goggins",
        "distractors": ["Timothy Olyphant", "Garret Dillahunt", "Barry Pepper"],
        "d": 1
    },
    {
        "q": "What power armor-wearing military faction does squire Maximus seek to rise within in 'Fallout'?",
        "correct": "The Brotherhood of Steel",
        "distractors": ["The Enclave", "The Minutemen", "The New California Republic"],
        "d": 1
    },
    {
        "q": "In 'Fallout', what pre-war corporate entity is revealed to have orchestrated and potentially dropped the nuclear bombs to secure market monopoly?",
        "correct": "Vault-Tec",
        "distractors": ["RobCo Industries", "General Atomics", "Nuka-Cola Corporation"],
        "d": 2
    },
    {
        "q": "Which executive producers of HBO's 'Westworld' developed the live-action 'Fallout' series for Prime Video alongside Bethesda Game Studios?",
        "correct": "Jonathan Nolan and Lisa Joy",
        "distractors": ["David Benioff and D.B. Weiss", "Damon Lindelof and Carlton Cuse", "J.J. Abrams and Bryan Burk"],
        "d": 2
    },
    {
        "q": "What was the capital city of the New California Republic that Hank MacLean destroyed with a nuclear warhead in 'Fallout'?",
        "correct": "Shady Sands",
        "distractors": ["New Vegas", "Boneyard", "San Francisco"],
        "d": 2
    },
    {
        "q": "Which 6-foot-3 actor stars as the towering former Army military police investigator Jack Reacher on Prime Video's 'Reacher'?",
        "correct": "Alan Ritchson",
        "distractors": ["Tom Cruise", "Alexander Skarsgård", "Wyatt Russell"],
        "d": 1
    },
    {
        "q": "Season 1 of Prime Video's 'Reacher' adapts which debut 1997 Jack Reacher novel by author Lee Child?",
        "correct": "Killing Floor",
        "distractors": ["Bad Luck and Trouble", "One Shot", "Die Trying"],
        "d": 2
    },
    {
        "q": "In 'The Lord of the Rings: The Rings of Power', what is the estimated record-setting budget Amazon committed to producing five seasons of the show?",
        "correct": "$1 billion",
        "distractors": ["$300 million", "$500 million", "$2 billion"],
        "d": 2
    },
    {
        "q": "In 'The Rings of Power' Season 1, what mortal disguise is used by the dark lord Sauron to deceive Galadriel?",
        "correct": "Halbrand, a shipwrecked human claiming to be King of the Southlands",
        "distractors": [
            "Annatar, an Elven emissary of the Valar",
            "Adar, the corrupted Elf leading the Orcs",
            "Ar-Pharazôn, chancellor of Númenor"
        ],
        "d": 2
    },
    {
        "q": "Which Welsh actress portrays the younger, warrior incarnation of Elven commander Galadriel in 'The Rings of Power'?",
        "correct": "Morfydd Clark",
        "distractors": ["Cate Blanchett", "Sophie Turner", "Anya Chalotra"],
        "d": 2
    },
    {
        "q": "Which master Elven smith is manipulated into forging the three Elven rings of power in Eregion in 'The Rings of Power'?",
        "correct": "Celebrimbor",
        "distractors": ["Gil-galad", "Elrond", "Círdan"],
        "d": 2
    },
    {
        "q": "In Amazon Prime Video's 'Good Omens', which duo plays the demon Crowley and the angel Aziraphale?",
        "correct": "David Tennant and Michael Sheen",
        "distractors": [
            "Benedict Cumberbatch and Martin Freeman",
            "Tom Hiddleston and Hugh Laurie",
            "Matt Smith and Peter Capaldi"
        ],
        "d": 1
    },
    {
        "q": "In 'Good Omens', what band's cassette tapes are the only music Crowley's vintage 1926 Bentley car will play?",
        "correct": "Queen",
        "distractors": ["The Beatles", "The Rolling Stones", "Led Zeppelin"],
        "d": 2
    },
    {
        "q": "Which two British authors collaborated on the original 1990 fantasy novel 'Good Omens'?",
        "correct": "Neil Gaiman and Terry Pratchett",
        "distractors": ["Neil Gaiman and Philip Pullman", "Terry Pratchett and Douglas Adams", "Alan Moore and Grant Morrison"],
        "d": 2
    },

    # 86-100: Deep Cuts & Behind the Scenes (Apple TV+ & Prime Video)
    {
        "q": "Which British comedy writer created 'The IT Crowd' and co-created 'Father Ted' before developing 'Slow Horses' for television?",
        "correct": "Will Smith (not to be confused with the American actor)",
        "distractors": ["Graham Linehan", "Arthur Mathews", "Armando Iannucci"],
        "d": 3
    },
    {
        "q": "In Apple TV+'s 'Severance', what is the full four-word name of the mysterious room where Mark finds baby goats being bottle-fed?",
        "correct": "There is no official door label, but the feeder yells 'They aren't ready yet!'",
        "distractors": [
            "The Caprine Incubation Chamber",
            "The Pastoral Biological Reserve",
            "Sub-basement Fauna Sector"
        ],
        "d": 3
    },
    {
        "q": "What specific vintage automobile does Jackson Lamb drive in Season 1 of 'Slow Horses'?",
        "correct": "He does not own a car and relies almost entirely on London black cabs and walking",
        "distractors": ["A rusted Rover 75", "A battered blue Ford Mondeo", "A 1980s Jaguar XJ"],
        "d": 3
    },
    {
        "q": "What is the name of the fictional morning show broadcast at the center of Apple TV+'s 'The Morning Show'?",
        "correct": "The Morning Show (on UBA)",
        "distractors": ["Daybreak America (on NBS)", "Good Morning USA (on CNA)", "Rise & Shine (on GBS)"],
        "d": 2
    },
    {
        "q": "In 'Ted Lasso', which real Premier League club manager made a high-profile cameo appearance interacting with Ted in Season 3?",
        "correct": "Pep Guardiola (Manchester City)",
        "distractors": ["Jürgen Klopp (Liverpool)", "Mikel Arteta (Arsenal)", "José Mourinho (Roma)"],
        "d": 2
    },
    {
        "q": "In 'Severance', what is the title of the self-help book written by Mark's brother-in-law Ricken Lazlo Hale that inspires the MDR revolt?",
        "correct": "The You You Are",
        "distractors": ["The Mind Inside", "Being Whole", "Ascending the Corporate Ladder"],
        "d": 2
    },
    {
        "q": "What is the name of the Lumon floor manager who oversees severed employees with unsettling charm, played by Tramell Tillman?",
        "correct": "Seth Milchick",
        "distractors": ["Mark Scout", "Doug Graner", "Peter Kilmer"],
        "d": 2
    },
    {
        "q": "In 'The Boys' Season 4, which new member joins The Seven billed as the world's smartest person?",
        "correct": "Sister Sage",
        "distractors": ["Firecracker", "Webweaver", "Splinter"],
        "d": 3
    },
    {
        "q": "In 'Invincible' Season 2, which multi-dimensional villain traps Mark Grayson across multiple alternate universes?",
        "correct": "Angstrom Levy",
        "distractors": ["Conquest", "Thragg", "Battle Beast"],
        "d": 3
    },
    {
        "q": "What real-life corporate acquisition deal in 2021 gave Amazon ownership of the James Bond catalog and major IP like 'Stargate' and 'RoboCop'?",
        "correct": "The $8.5 billion acquisition of MGM",
        "distractors": [
            "The $10 billion purchase of Paramount Pictures",
            "The $7 billion acquisition of Lionsgate",
            "The $12 billion merger with Warner Bros."
        ],
        "d": 3
    },
    {
        "q": "In 'The Marvelous Mrs. Maisel', how many total Primetime Emmy Awards did the series win across its five-season run?",
        "correct": "22",
        "distractors": ["14", "18", "27"],
        "d": 3
    },
    {
        "q": "What song does Midge Maisel's father Abe Weissman play on the piano during a poignant scene in Season 4 of 'Mrs. Maisel'?",
        "correct": "Rachmaninoff's Prelude in C-sharp minor",
        "distractors": ["Chopin's Nocturne in E-flat major", "Beethoven's Moonlight Sonata", "Debussy's Clair de Lune"],
        "d": 3
    },
    {
        "q": "In 'Silo' Season 1, what mechanical component must Juliette and the engineering team fix in an emergency without shutting down the Silo's power forever?",
        "correct": "The steam turbine generator",
        "distractors": ["The water filtration pump", "The air recirculation fan", "The central geothermal shaft"],
        "d": 3
    },
    {
        "q": "In 'Ted Lasso', what is the name of the London pub run by Mae where the die-hard Richmond fans gather to watch matches?",
        "correct": "The Crown & Anchor",
        "distractors": ["The Red Lion", "The Greyhound Arms", "The Queen's Head"],
        "d": 2
    },
    {
        "q": "In 'Fallout' Season 1, what component does scientist Siggi Wilzig inject into his own neck before his death?",
        "correct": "A cold fusion particle capsule",
        "distractors": ["A platinum encryption chip", "A miniaturized nuclear battery", "A FEV strain inoculant"],
        "d": 3
    }
]

if __name__ == "__main__":
    build_batch(BATCH_2, "tools/staging/streaming_tv_batch2.json", batch_num=2)
