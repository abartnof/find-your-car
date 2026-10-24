#!/usr/bin/env python3
"""
Generate Batch 1 of Streaming TV Shows trivia (100 questions):
Netflix & Hulu Flagships: Stranger Things, The Crown, Squid Game, The Bear,
Only Murders in the Building, Ozark, Bridgerton, Beef, The Queen's Gambit, BoJack Horseman.
Target: 30 d1, 40 d2, 30 d3.
"""

from streaming_tv_batch_builder import build_batch

BATCH_1 = [
    # 1-10: Stranger Things (Textual & Metatextual)
    {
        "q": "In 'Stranger Things' Season 1, what snack food does Eleven become obsessed with after escaping Hawkins National Laboratory?",
        "correct": "Eggo waffles",
        "distractors": ["Pop-Tarts", "Twinkies", "Oreos"],
        "d": 1
    },
    {
        "q": "What song by Kate Bush plays a vital narrative role by saving Max Mayfield from Vecna's curse in 'Stranger Things' Season 4?",
        "correct": "Running Up That Hill (A Deal with God)",
        "distractors": ["Wuthering Heights", "Cloudbusting", "Hounds of Love"],
        "d": 1
    },
    {
        "q": "In 'Stranger Things', what is the actual identity and backstory of the monster Vecna?",
        "correct": "Henry Creel, also known as One (001)",
        "distractors": ["Dr. Martin Brenner transformed", "A mutated clone of Will Byers", "Billy Hargrove resurrected"],
        "d": 1
    },
    {
        "q": "Which Dungeons & Dragons club at Hawkins High School is led by Eddie Munson in 'Stranger Things' Season 4?",
        "correct": "The Hellfire Club",
        "distractors": ["The Dungeon Masters", "The Shadow Guild", "The Mind Flayers"],
        "d": 1
    },
    {
        "q": "In the Season 4 finale of 'Stranger Things', what Metallica song does Eddie Munson perform on his electric guitar in the Upside Down?",
        "correct": "Master of Puppets",
        "distractors": ["Enter Sandman", "Seek & Destroy", "Fade to Black"],
        "d": 1
    },
    {
        "q": "Where is Jim Hopper imprisoned during the first half of 'Stranger Things' Season 4 before Joyce and Murray rescue him?",
        "correct": "Kamchatka, Russia",
        "distractors": ["Siberia, Russia", "Vladivostok, Russia", "Chernobyl, Ukraine"],
        "d": 2
    },
    {
        "q": "What is the name of the secret Russian underground base hidden beneath the Starcourt Mall in 'Stranger Things' Season 3?",
        "correct": "Operation Child",
        "distractors": ["The Red Dawn Project", "The Key Bunker", "The Ozero Facility"],
        "d": 3
    },
    {
        "q": "In 'Stranger Things' Season 2, what nickname does Dustin Henderson give to the baby Demogorgon he initially keeps as a pet?",
        "correct": "Dart (D'Artagnan)",
        "distractors": ["Gorgon", "Spike", "Yurtle"],
        "d": 2
    },
    {
        "q": "Which real-life town and state serve as the primary setting for the supernatural events of 'Stranger Things'?",
        "correct": "Hawkins, Indiana",
        "distractors": ["Castlerock, Maine", "Roanoke, Virginia", "Eerie, Pennsylvania"],
        "d": 1
    },
    {
        "q": "Before settling on the title 'Stranger Things', what was the original working title pitched by the Duffer Brothers?",
        "correct": "Montauk",
        "distractors": ["The Nether", "Camp Hero", "The Upside Down"],
        "d": 2
    },

    # 11-20: Stranger Things Deep Cuts
    {
        "q": "In 'Stranger Things' Season 1, how does Joyce Byers first successfully establish two-way communication with Will in the Upside Down?",
        "correct": "Painting the alphabet on her living room wall with Christmas lights",
        "distractors": ["Using a shortwave ham radio", "Flashing headlights on her car", "Typing on an electric typewriter"],
        "d": 1
    },
    {
        "q": "What board game do Will, Mike, Dustin, and Lucas play for 10 hours in the opening scene of the 'Stranger Things' pilot?",
        "correct": "Dungeons & Dragons",
        "distractors": ["Risk", "Axis & Allies", "Stratego"],
        "d": 1
    },
    {
        "q": "Which character serves as the paranoid investigative journalist and Russian translator who helps Joyce and Hopper in 'Stranger Things'?",
        "correct": "Murray Bauman",
        "distractors": ["Keith Higgins", "Ted Wheeler", "Bob Newby"],
        "d": 2
    },
    {
        "q": "What is the name of the Hawkins newspaper where Nancy Wheeler and Jonathan Byers work as interns in Season 3?",
        "correct": "The Hawkins Post",
        "distractors": ["The Hawkins Gazette", "The Hawkins Daily Chronicle", "The Indiana Tribune"],
        "d": 3
    },
    {
        "q": "Which actress made her breakout streaming debut playing Robin Buckley, Steve Harrington's Scoops Ahoy coworker in Season 3?",
        "correct": "Maya Hawke",
        "distractors": ["Sadie Sink", "Natalia Dyer", "Margaret Qualley"],
        "d": 2
    },
    {
        "q": "What was the estimated production budget per episode for 'Stranger Things' Season 4, making it one of television's most expensive seasons?",
        "correct": "$30 million",
        "distractors": ["$15 million", "$20 million", "$45 million"],
        "d": 3
    },
    {
        "q": "In 'Stranger Things' Season 2, Sean Astin portrays Bob Newby, the lovable manager of which local electronic retail franchise?",
        "correct": "RadioShack",
        "distractors": ["Circuit City", "Best Buy", "The Sound Shack"],
        "d": 2
    },
    {
        "q": "Which heavy metal band saw their 1986 track surge into the Billboard Hot 100 top 40 for the first time in 2022 after 'Stranger Things' featured it?",
        "correct": "Metallica",
        "distractors": ["Iron Maiden", "Judas Priest", "Megadeth"],
        "d": 2
    },
    {
        "q": "In 'Stranger Things' Season 4, what is the name of the California stoner pizza delivery company where Argyle works?",
        "correct": "Surfer Boy Pizza",
        "distractors": ["Big Wave Pizza", "Pipeline Pies", "Sunken Crust"],
        "d": 2
    },
    {
        "q": "How many total Emmy nominations did 'Stranger Things' receive for its first four seasons on Netflix?",
        "correct": "51",
        "distractors": ["32", "41", "64"],
        "d": 3
    },

    # 21-35: The Crown (Textual, Metatextual, Extratextual)
    {
        "q": "Which three British actresses portrayed Queen Elizabeth II across the six seasons of Netflix's 'The Crown'?",
        "correct": "Claire Foy, Olivia Colman, and Imelda Staunton",
        "distractors": [
            "Emma Thompson, Helen Mirren, and Judi Dench",
            "Claire Foy, Helena Bonham Carter, and Kristin Scott Thomas",
            "Olivia Colman, Imelda Staunton, and Vanessa Redgrave"
        ],
        "d": 1
    },
    {
        "q": "Who created and served as head writer for all six seasons of 'The Crown'?",
        "correct": "Peter Morgan",
        "distractors": ["Julian Fellowes", "Steven Moffat", "Russell T Davies"],
        "d": 1
    },
    {
        "q": "Which critically acclaimed Season 3 episode of 'The Crown' depicts the 1966 Welsh mining disaster and the Queen's delayed visit?",
        "correct": "Aberfan",
        "distractors": ["Tywysog Cymru", "Moondust", "Cri de Coeur"],
        "d": 2
    },
    {
        "q": "Which actress won an Emmy and Golden Globe for her portrayal of Princess Diana in Season 4 of 'The Crown'?",
        "correct": "Emma Corrin",
        "distractors": ["Elizabeth Debicki", "Emerald Fennell", "Carey Mulligan"],
        "d": 2
    },
    {
        "q": "Which actress took over the role of Princess Diana in Seasons 5 and 6 of 'The Crown', winning an Emmy in 2024?",
        "correct": "Elizabeth Debicki",
        "distractors": ["Rosamund Pike", "Vanessa Kirby", "Rebecca Hall"],
        "d": 2
    },
    {
        "q": "Who played Prince Philip, Duke of Edinburgh, in the first two seasons of 'The Crown' opposite Claire Foy?",
        "correct": "Matt Smith",
        "distractors": ["Tobias Menzies", "Jonathan Pryce", "Paul Bettany"],
        "d": 1
    },
    {
        "q": "In 'The Crown' Season 4, which renowned actress portrayed British Prime Minister Margaret Thatcher?",
        "correct": "Gillian Anderson",
        "distractors": ["Meryl Streep", "Kristin Scott Thomas", "Miranda Richardson"],
        "d": 1
    },
    {
        "q": "What major milestone did 'The Crown' achieve at the 73rd Primetime Emmy Awards in 2021?",
        "correct": "It swept all seven top drama categories, including Drama Series, Directing, Writing, and all four acting prizes",
        "distractors": [
            "It set the all-time record for most Emmys won by any show in a single year with 18 wins",
            "It became the first foreign-language drama to win Outstanding Drama Series",
            "It tied 'Game of Thrones' for 12 wins in a single ceremony"
        ],
        "d": 2
    },
    {
        "q": "In 'The Crown' Season 1, what does Winston Churchill's wife Clementine do with the 80th-birthday portrait painted by Graham Sutherland?",
        "correct": "She burns it in the estate furnace",
        "distractors": ["She locks it in the Tower of London", "She throws it into the Thames", "She cuts it into pieces and buries it"],
        "d": 3
    },
    {
        "q": "Which actor portrayed Prince Charles as an adult in Seasons 3 and 4 of 'The Crown'?",
        "correct": "Josh O'Connor",
        "distractors": ["Dominic West", "Eddie Redmayne", "George MacKay"],
        "d": 2
    },
    {
        "q": "In 2018, 'The Crown' sparked significant media controversy regarding gender pay equity when producers revealed what discrepancy?",
        "correct": "Matt Smith was paid more than lead actress Claire Foy",
        "distractors": [
            "Helena Bonham Carter took a 50% salary reduction",
            "The series refused to compensate real royal family advisors",
            "Gillian Anderson was paid less than her male cabinet co-stars"
        ],
        "d": 2
    },
    {
        "q": "Which Season 5 episode of 'The Crown' recreates Princess Diana's bombshell 1995 interview on the BBC program 'Panorama'?",
        "correct": "Gunpowder",
        "distractors": ["The System", "Ipatiev House", "Decommissioned"],
        "d": 3
    },
    {
        "q": "In 'The Crown' Season 2, which renowned photographer marries Princess Margaret?",
        "correct": "Antony Armstrong-Jones (Lord Snowdon)",
        "distractors": ["Peter Townsend", "Robin Woods", "Roddy Llewellyn"],
        "d": 2
    },
    {
        "q": "Approximately how much was the reported production budget for the first season of 'The Crown' across its 10 episodes?",
        "correct": "$100 million",
        "distractors": ["$40 million", "$180 million", "$250 million"],
        "d": 3
    },
    {
        "q": "What is the final scene of 'The Crown' series finale ('Sleep, Dearie, Sleep')?",
        "correct": "Queen Elizabeth II walks through St George's Chapel as visions of her younger selves fade into the distance",
        "distractors": [
            "The Queen meets Tony Blair for a final audience at Buckingham Palace",
            "Prince William proposes to Kate Middleton at St Andrews",
            "Queen Elizabeth II addresses the nation live on television"
        ],
        "d": 3
    },

    # 36-50: Squid Game (Textual, Metatextual, Extratextual)
    {
        "q": "In the global Netflix phenomenon 'Squid Game', what is the cash prize waiting in the giant piggy bank for the sole surviving winner?",
        "correct": "45.6 billion South Korean won",
        "distractors": ["10 billion won", "25.5 billion won", "100 billion won"],
        "d": 1
    },
    {
        "q": "Who wrote, directed, and created 'Squid Game', having initially conceived the premise in 2008 as a feature film script?",
        "correct": "Hwang Dong-hyuk",
        "distractors": ["Bong Joon-ho", "Park Chan-wook", "Lee Chang-dong"],
        "d": 2
    },
    {
        "q": "What Korean traditional candy requires players in 'Squid Game' to carve out shapes without cracking the brittle sugar?",
        "correct": "Dalgona (Ppopgi)",
        "distractors": ["Yayak", "Dasik", "Tteok"],
        "d": 1
    },
    {
        "q": "What is the name of the colossal robotic motion-detecting doll featured in the 'Red Light, Green Light' game?",
        "correct": "Young-hee",
        "distractors": ["Cheol-soo", "Min-ji", "Sun-hee"],
        "d": 2
    },
    {
        "q": "Which South Korean actor made history at the 74th Primetime Emmy Awards by winning Outstanding Lead Actor in a Drama Series for 'Squid Game'?",
        "correct": "Lee Jung-jae",
        "distractors": ["Park Hae-soo", "Wi Ha-joon", "Lee Byung-hun"],
        "d": 1
    },
    {
        "q": "In 'Squid Game', what is the shocking identity revealed behind Player 001, Oh Il-nam?",
        "correct": "He is the wealthy creator and host of the games",
        "distractors": [
            "He is Seong Gi-hun's biological father",
            "He is an undercover South Korean police commissioner",
            "He is a disguised VIP who replaced the original player"
        ],
        "d": 1
    },
    {
        "q": "Which game is played in the gut-wrenching sixth episode, titled 'Gganbu'?",
        "correct": "Marbles",
        "distractors": ["Tug of War", "Glass Stepping Stones", "Ddakji"],
        "d": 2
    },
    {
        "q": "What shape is worn on the masks of the highest-ranking guards who give orders and speak to players in 'Squid Game'?",
        "correct": "Square",
        "distractors": ["Triangle", "Circle", "Star"],
        "d": 2
    },
    {
        "q": "According to Netflix, how many million households watched 'Squid Game' within its first 28 days of release, making it Netflix's most-watched series launch ever?",
        "correct": "142 million",
        "distractors": ["82 million", "111 million", "195 million"],
        "d": 3
    },
    {
        "q": "Which international breakout star won the SAG Award for Outstanding Performance by a Female Actor in a Drama Series for playing Kang Sae-byeok (Player 067)?",
        "correct": "Jung Ho-yeon",
        "distractors": ["Kim Joo-ryoung", "Park So-dam", "Bae Doona"],
        "d": 2
    },
    {
        "q": "What is the weapon Seong Gi-hun and Cho Sang-woo are given to fight each other in the final Squid Game during the torrential downpour?",
        "correct": "Steak knives",
        "distractors": ["Revolvers", "Baseball bats", "Iron pipes"],
        "d": 3
    },
    {
        "q": "Who plays the enigmatic Front Man in 'Squid Game', revealed when he shoots his detective brother Hwang Jun-ho off a cliff?",
        "correct": "Lee Byung-hun",
        "distractors": ["Gong Yoo", "Ma Dong-seok", "Song Kang-ho"],
        "d": 2
    },
    {
        "q": "What game does the Salesman played by Gong Yoo use to recruit Gi-hun in the subway station while slapping him repeatedly?",
        "correct": "Ddakji",
        "distractors": ["Gonggi", "Yut Nori", "Omok"],
        "d": 2
    },
    {
        "q": "How long did Hwang Dong-hyuk keep the script of 'Squid Game' shelved due to studios rejecting it as too grotesque and unrealistic before Netflix bought it in 2019?",
        "correct": "Roughly 10 years",
        "distractors": ["3 years", "15 years", "20 years"],
        "d": 3
    },
    {
        "q": "At the 74th Primetime Emmy Awards, what milestone did 'Squid Game' achieve in the Outstanding Drama Series category?",
        "correct": "It was the first non-English language series to be nominated for Outstanding Drama Series",
        "distractors": [
            "It was the first streaming series to win Outstanding Drama Series",
            "It received nominations in every single acting category simultaneously",
            "It set the record for most Emmy wins by a freshman series with 14 wins"
        ],
        "d": 2
    },

    # 51-65: The Bear (Textual, Metatextual, Extratextual)
    {
        "q": "In FX on Hulu's 'The Bear', what is the original name of the chaotic family sandwich shop in Chicago before its fine-dining reboot?",
        "correct": "The Original Beef of Chicagoland",
        "distractors": ["Carmy's Italian Beef", "The Chicago Slice", "Berzatto & Sons Beef"],
        "d": 1
    },
    {
        "q": "In 'The Bear' Season 1 finale, where does Carmy discover thousands of dollars hidden by his late brother Mikey?",
        "correct": "Inside sealed cans of San Marzano tomatoes",
        "distractors": [
            "Behind the stainless-steel backsplash of the stove",
            "Underneath the floorboards of the walk-in freezer",
            "Inside bags of imported Italian breadcrumbs"
        ],
        "d": 1
    },
    {
        "q": "Which actor stars as Carmen 'Carmy' Berzatto in 'The Bear', winning back-to-back Lead Actor Emmys in 2023 and 2024?",
        "correct": "Jeremy Allen White",
        "distractors": ["Ebon Moss-Bachrach", "Ayo Edebiri", "Jon Bernthal"],
        "d": 1
    },
    {
        "q": "In 'The Bear' Season 2, which high-end fine-dining restaurant in Chicago does Richie stage at in the acclaimed episode 'Forks'?",
        "correct": "Ever",
        "distractors": ["Alinea", "Next", "Smyth"],
        "d": 2
    },
    {
        "q": "What song by Taylor Swift does Richie sing at the top of his lungs in his car after a transformative week of staging in 'Forks'?",
        "correct": "Love Story",
        "distractors": ["Cruel Summer", "Shake It Off", "Blank Space"],
        "d": 2
    },
    {
        "q": "What cinematic technique is famously used for the chaotic 20-minute episode 'Review' in 'The Bear' Season 1?",
        "correct": "It was filmed as an unbroken continuous single shot",
        "distractors": [
            "It was filmed entirely in black-and-white",
            "It featured no spoken dialogue whatsoever",
            "It was presented in split-screen four-way perspective"
        ],
        "d": 2
    },
    {
        "q": "Which guest star plays the deeply troubled Berzatto family matriarch Donna in the flashback episode 'Fishes'?",
        "correct": "Jamie Lee Curtis",
        "distractors": ["Catherine O'Hara", "Patricia Clarkson", "Laura Dern"],
        "d": 2
    },
    {
        "q": "In 'The Bear' Season 2, where is pastry chef Marcus sent to stage and learn dessert craft under Chef Luca (played by Will Poulter)?",
        "correct": "Copenhagen, Denmark",
        "distractors": ["Paris, France", "Tokyo, Japan", "Modena, Italy"],
        "d": 2
    },
    {
        "q": "What record did 'The Bear' set at the 76th Primetime Emmy Awards in 2024 for a comedy series in a single year?",
        "correct": "Most Emmy wins by a comedy series in a single season with 11 wins",
        "distractors": [
            "First comedy series to win every acting award",
            "Most viewers for an Emmy-winning comedy premiere",
            "Longest episode to win Outstanding Comedy Writing"
        ],
        "d": 2
    },
    {
        "q": "Who created, co-showran, and directed many of the most acclaimed episodes of 'The Bear'?",
        "correct": "Christopher Storer",
        "distractors": ["Rian Johnson", "Bill Hader", "Mike White"],
        "d": 2
    },
    {
        "q": "What phrase do the kitchen staff members yell to acknowledge orders and respect the kitchen hierarchy in 'The Bear'?",
        "correct": "Yes, Chef!",
        "distractors": ["Heard!", "Corner!", "All day!"],
        "d": 1
    },
    {
        "q": "In 'The Bear' Season 2 finale, what catastrophic accident traps Carmy for the entirety of Friends & Family opening night?",
        "correct": "He gets locked inside the walk-in refrigerator",
        "distractors": [
            "The fire suppression system triggers and seals the kitchen doors",
            "His chef knife slips and requires emergency stitches at the hospital",
            "The electrical breaker blows and traps him in the basement storage"
        ],
        "d": 1
    },
    {
        "q": "Which real-life celebrity chef and restaurateur makes a cameo appearance in 'Forks' as Chef Terry, peeling mushrooms beside Richie?",
        "correct": "Olivia Colman",
        "distractors": ["Gillian Anderson", "Emma Thompson", "Sarah Lancashire"],
        "d": 2
    },
    {
        "q": "Who portrays Mikey Berzatto, Carmy and Sugar's late older brother who appears in pivotal flashbacks in 'The Bear'?",
        "correct": "Jon Bernthal",
        "distractors": ["Shea Whigham", "John Mulaney", "Bob Odenkirk"],
        "d": 2
    },
    {
        "q": "What culinary dish is Sydney testing endlessly in Season 2 that she finally perfects with boursin cheese and sour cream & onion potato chips?",
        "correct": "French rolled omelet",
        "distractors": ["Beef short rib risotto", "Savory tartlet", "Lobster agnolotti"],
        "d": 3
    },

    # 66-78: Only Murders in the Building (Textual, Metatextual, Extratextual)
    {
        "q": "In Hulu's 'Only Murders in the Building', what is the name of the historic Upper West Side apartment building where the main trio lives?",
        "correct": "The Arconia",
        "distractors": ["The Dakota", "The Belnord", "The Ansonia"],
        "d": 1
    },
    {
        "q": "Which trio of actors stars as the amateur true-crime podcasting team in 'Only Murders in the Building'?",
        "correct": "Steve Martin, Martin Short, and Selena Gomez",
        "distractors": [
            "Steve Martin, Chevy Chase, and Martin Short",
            "Martin Short, Eugene Levy, and Catherine O'Hara",
            "Steve Martin, Michael Keaton, and Selena Gomez"
        ],
        "d": 1
    },
    {
        "q": "What is the famous TV detective role that Charles-Haden Savage played in the 1990s on 'Only Murders in the Building'?",
        "correct": "Brazzos",
        "distractors": ["Columbo", "Kojak", "Barnaby Jones"],
        "d": 1
    },
    {
        "q": "Who was revealed to be the killer of Tim Kono in the Season 1 finale of 'Only Murders in the Building'?",
        "correct": "Jan Bellows, the bassoonist dating Charles",
        "distractors": ["Bunny Folger", "Oscar Torres", "Cinda Canning"],
        "d": 2
    },
    {
        "q": "Which Broadway superstar joined Season 3 of 'Only Murders in the Building' playing the struggling nanny and actress Loretta Durkin?",
        "correct": "Meryl Streep",
        "distractors": ["Glenn Close", "Patti LuPone", "Barbra Streisand"],
        "d": 1
    },
    {
        "q": "What was the ill-fated Broadway musical directed by Oliver Putnam that sank into financial ruin when an actor fell into an orchestra pit of water?",
        "correct": "Splash!",
        "distractors": ["The Iceman Cometh", "Death Rattle Dazzle", "Singin' in the Rain"],
        "d": 2
    },
    {
        "q": "Which actor plays Ben Glenroy, the Hollywood action star who collapses on stage during opening night of 'Death Rattle' in Season 3?",
        "correct": "Paul Rudd",
        "distractors": ["Jesse Williams", "Matthew Broderick", "Nathan Lane"],
        "d": 2
    },
    {
        "q": "Who portrays Sazz Pataki, Charles-Haden Savage's longtime stunt double who is mysteriously shot in Charles's kitchen at the end of Season 3?",
        "correct": "Jane Lynch",
        "distractors": ["Tina Fey", "Amy Ryan", "Shirley MacLaine"],
        "d": 2
    },
    {
        "q": "Which comedian and writer portrays Cinda Canning, the ultra-successful rival true-crime podcaster in 'Only Murders in the Building'?",
        "correct": "Tina Fey",
        "distractors": ["Amy Poehler", "Maya Rudolph", "Kristen Wiig"],
        "d": 2
    },
    {
        "q": "What real-life historic New York City building serves as the exterior facade for The Arconia?",
        "correct": "The Belnord",
        "distractors": ["The Dakota", "The Apthorp", "The San Remo"],
        "d": 3
    },
    {
        "q": "In Season 2 of 'Only Murders in the Building', what valuable stolen object is central to the mystery surrounding Bunny Folger's murder?",
        "correct": "An erotic Rose Cooper painting featuring Charles's father",
        "distractors": ["An antique emerald necklace", "A first-edition manuscript of Brazzos", "A 19th-century coin collection"],
        "d": 3
    },
    {
        "q": "Which guest star won a Primetime Emmy for Outstanding Guest Actor in a Comedy Series for playing Teddy Dimas in Season 1?",
        "correct": "Nathan Lane",
        "distractors": ["Da'Vine Joy Randolph", "Sting", "Matthew Broderick"],
        "d": 3
    },
    {
        "q": "What song from Oliver's musical 'Death Rattle Dazzle' was submitted for Emmy consideration for Outstanding Original Music and Lyrics in 2024?",
        "correct": "Which of the Pickwick Triplets Did It?",
        "distractors": ["Look for the Light", "Creatures of the Night", "Babies on the Board"],
        "d": 3
    },

    # 79-88: Ozark & Bridgerton
    {
        "q": "In Netflix's 'Ozark', what business scheme does financial planner Marty Byrde propose to save his life from the Navarro drug cartel?",
        "correct": "Laundering $500 million in the Missouri Ozarks",
        "distractors": [
            "Setting up offshore shell accounts in Panama",
            "Smuggling fentanyl across the Canadian border",
            "Buying an American commercial bank"
        ],
        "d": 1
    },
    {
        "q": "Which actress won three Primetime Emmy Awards for Outstanding Supporting Actress in a Drama Series for playing Ruth Langmore in 'Ozark'?",
        "correct": "Julia Garner",
        "distractors": ["Laura Linney", "Sofia Hublitz", "Janet McTeer"],
        "d": 1
    },
    {
        "q": "What is the name of the riverboat casino that Marty and Wendy Byrde open to launder millions in 'Ozark' Season 2 and 3?",
        "correct": "The Missouri Belle",
        "distractors": ["The Ozark Empress", "The Blue Cat", "The Lake Queen"],
        "d": 2
    },
    {
        "q": "In the series finale of 'Ozark', who fatally shoots cartel boss Omar Navarro's sister, Camila Elizonndro, or who kills Ruth Langmore?",
        "correct": "Camila Elizonndro shoots Ruth Langmore",
        "distractors": [
            "Javi Elizonndro shoots Ruth Langmore",
            "Marty Byrde shoots Ruth Langmore",
            "Wendy Byrde poisons Ruth Langmore"
        ],
        "d": 2
    },
    {
        "q": "What famous line did Ruth Langmore scream at Marty Byrde in a memorable Season 4 scene of 'Ozark'?",
        "correct": "If you want to stop me, you're gonna have to fucking kill me!",
        "distractors": [
            "I don't know shit about fuck, Marty!",
            "You ruined my whole damn family!",
            "I am the queen of this lake!"
        ],
        "d": 3
    },
    {
        "q": "On Netflix's hit series 'Bridgerton', whose secret identity is revealed to be the gossip columnist Lady Whistledown?",
        "correct": "Penelope Featherington",
        "distractors": ["Eloise Bridgerton", "Cressida Cowper", "Lady Danbury"],
        "d": 1
    },
    {
        "q": "Which British actor became an international sensation as Simon Basset, Duke of Hastings, in 'Bridgerton' Season 1?",
        "correct": "Regé-Jean Page",
        "distractors": ["Jonathan Bailey", "Luke Thompson", "Reece Ritchie"],
        "d": 1
    },
    {
        "q": "Which author wrote the Regency romance novel series upon which Netflix's 'Bridgerton' is adapted?",
        "correct": "Julia Quinn",
        "distractors": ["Georgette Heyer", "Sarah J. Maas", "Lisa Kleypas"],
        "d": 2
    },
    {
        "q": "Which production company, founded by Shonda Rhimes, produces 'Bridgerton' under an expansive nine-figure Netflix deal?",
        "correct": "Shondaland",
        "distractors": ["Bad Robot", "Monkeypaw Productions", "Plan B Entertainment"],
        "d": 2
    },
    {
        "q": "What orchestral pop covers feature prominently on 'Bridgerton' soundtracks, arranged by the Vitamin String Quartet and Duomo?",
        "correct": "Modern pop songs like 'Thank U, Next', 'Bad Guy', and 'Girls Like You'",
        "distractors": [
            "Classic 1970s disco tracks arranged as waltzes",
            "Broadway showtunes arranged for harpsichord",
            "Traditional Scottish folk melodies with full choir"
        ],
        "d": 2
    },

    # 89-100: Beef, BoJack Horseman, The Queen's Gambit, Dead to Me
    {
        "q": "In Netflix's 2023 limited series 'Beef', what inciting incident triggers the spiraling feud between Danny Cho and Amy Lau?",
        "correct": "A road rage incident in a home improvement store parking lot",
        "distractors": [
            "A stolen handbag at a luxury art gallery",
            "A botched contractor remodeling job",
            "An aggressive bidding war over a prime piece of real estate"
        ],
        "d": 1
    },
    {
        "q": "Which two lead actors made Emmy history by sweeping the Lead Actor and Lead Actress in a Limited Series awards for 'Beef'?",
        "correct": "Steven Yeun and Ali Wong",
        "distractors": ["Randall Park and Constance Wu", "Daniel Dae Kim and Sandra Oh", "Bowen Yang and Awkwafina"],
        "d": 1
    },
    {
        "q": "Who created and served as showrunner for 'Beef', based loosely on his own real-life road rage altercation?",
        "correct": "Lee Sung Jin",
        "distractors": ["Lulu Wang", "Daniel Kwan", "Jon M. Chu"],
        "d": 3
    },
    {
        "q": "In Netflix's animated series 'BoJack Horseman', what animal species is BoJack's hyper-competent agent and former girlfriend, Princess Carolyn?",
        "correct": "Persian cat",
        "distractors": ["Poodle dog", "Pink rabbit", "Red fox"],
        "d": 1
    },
    {
        "q": "What is unique about the acclaimed Season 5 episode 'Free Churro' in 'BoJack Horseman'?",
        "correct": "It consists almost entirely of a single uninterrupted eulogy delivered by BoJack at a funeral",
        "distractors": [
            "It is completely silent with no dialogue until the final second",
            "It was rendered entirely in stop-motion claymation",
            "It takes place entirely in reverse chronological order"
        ],
        "d": 2
    },
    {
        "q": "Which 'BoJack Horseman' Season 3 episode is set almost entirely underwater at the Pacific Ocean Film Festival and features virtually zero dialogue?",
        "correct": "Fish Out of Water",
        "distractors": ["The View from Halfway Down", "Time's Arrow", "Escape from L.A."],
        "d": 2
    },
    {
        "q": "In 'The Queen's Gambit', who teaches nine-year-old Beth Harmon how to play chess in the basement of the orphanage?",
        "correct": "Mr. Shaibel, the custodian",
        "distractors": ["Mr. Ganz, the math teacher", "Mrs. Deardorff, the headmistress", "Harry Beltik"],
        "d": 2
    },
    {
        "q": "What green tranquilizer pill is Beth Harmon given in the orphanage that she abuses to visualize chess games on her ceiling?",
        "correct": "Xanzolam",
        "distractors": ["Librium", "Valium", "Soma"],
        "d": 3
    },
    {
        "q": "Which chess grandmaster serves as the menacing Soviet World Champion that Beth Harmon must defeat in Moscow in the series finale?",
        "correct": "Vasily Borgov",
        "distractors": ["Viktor Korchnoi", "Luchenko", "Georgi Girev"],
        "d": 2
    },
    {
        "q": "Which real-life legendary chess grandmaster and former World Champion served as a key consultant for 'The Queen's Gambit'?",
        "correct": "Garry Kasparov",
        "distractors": ["Magnus Carlsen", "Anatoly Karpov", "Viswanathan Anand"],
        "d": 3
    },
    {
        "q": "In Netflix's dark comedy 'Dead to Me', what secret binds Judy Hale to grieving widow Jen Harding?",
        "correct": "Judy was the driver in the hit-and-run that killed Jen's husband",
        "distractors": [
            "Judy was having an affair with Jen's husband",
            "Judy stole millions from Jen's real estate business",
            "Judy is Jen's secret half-sister"
        ],
        "d": 1
    },
    {
        "q": "Which two actresses star as Jen Harding and Judy Hale in 'Dead to Me'?",
        "correct": "Christina Applegate and Linda Cardellini",
        "distractors": [
            "Amy Poehler and Tina Fey",
            "Reese Witherspoon and Laura Dern",
            "Jane Krakowski and Ellie Kemper"
        ],
        "d": 1
    }
]

if __name__ == "__main__":
    build_batch(BATCH_1, "tools/staging/streaming_tv_batch1.json", batch_num=1)
