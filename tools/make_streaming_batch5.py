#!/usr/bin/env python3
"""
Generate Batch 5 of Streaming TV Shows trivia (100 questions):
Extratextual Focus: Production budgets per episode, cutting-edge VFX & Volume/StageCraft,
breakthrough casting stories & auditions, real-world filming locations & architectural landmarks,
critical reception & reviews, Hollywood strikes, renewals & cancellations.
Target: 19 d1, 17 d2, 64 d3.
"""

from streaming_tv_batch_builder import build_batch

BATCH_5 = [
    # 1-20: Production Budgets, High-Stakes Financials & VFX Technology
    {
        "q": "With a total production budget exceeding $465 million for its eight-episode first season, which fantasy series became the most expensive television season ever made?",
        "correct": "The Lord of the Rings: The Rings of Power (Amazon Prime Video)",
        "distractors": [
            "House of the Dragon (HBO/Max)",
            "Stranger Things Season 4 (Netflix)",
            "The Mandalorian (Disney+)"
        ],
        "d": 1
    },
    {
        "q": "How much did each episode of Netflix's 'Stranger Things' Season 4 cost on average to produce?",
        "correct": "$30 million per episode",
        "distractors": ["$12 million per episode", "$18 million per episode", "$45 million per episode"],
        "d": 2
    },
    {
        "q": "Which Amazon spy thriller series saw its budget balloon to over $300 million for just six episodes following massive creative overhauls and reshoots?",
        "correct": "Citadel",
        "distractors": ["Tom Clancy's Jack Ryan", "Reacher", "The Terminal List"],
        "d": 2
    },
    {
        "q": "What was the estimated production budget per episode for Marvel's flagship Disney+ series such as 'WandaVision' and 'The Falcon and the Winter Soldier'?",
        "correct": "$25 million per episode",
        "distractors": ["$10 million per episode", "$15 million per episode", "$40 million per episode"],
        "d": 2
    },
    {
        "q": "What was the estimated production budget per episode for Season 1 of HBO's 'House of the Dragon', keeping it under $20 million per episode?",
        "correct": "Roughly $20 million per episode",
        "distractors": ["$8 million per episode", "$12 million per episode", "$35 million per episode"],
        "d": 3
    },
    {
        "q": "How much did the physical puppet of Grogu (Baby Yoda) used on set in 'The Mandalorian' reportedly cost to design and fabricate?",
        "correct": "$5 million",
        "distractors": ["$500,000", "$1.5 million", "$10 million"],
        "d": 3
    },
    {
        "q": "What cutting-edge game engine powers the real-time photo-realistic backgrounds displayed on LED walls inside Industrial Light & Magic's StageCraft Volume?",
        "correct": "Unreal Engine (Epic Games)",
        "distractors": ["Unity", "CryEngine", "Frostbite"],
        "d": 2
    },
    {
        "q": "How many hours of prosthetic makeup application did actor Jamie Campbell Bower endure each day to transform practically into Vecna in 'Stranger Things' Season 4?",
        "correct": "Between 7 and 8.5 hours",
        "distractors": ["2 to 3 hours", "4 to 5 hours", "12 to 14 hours"],
        "d": 3
    },
    {
        "q": "What percentage of Vecna's on-screen appearance in 'Stranger Things' Season 4 was created using practical prosthetics rather than full CGI, according to makeup designer Barrie Gower?",
        "correct": "Roughly 90% practical",
        "distractors": ["20% practical", "50% practical", "70% practical"],
        "d": 3
    },
    {
        "q": "Which legendary makeup and prosthetics artist designed the Night King for 'Game of Thrones' and Vecna for 'Stranger Things'?",
        "correct": "Barrie Gower",
        "distractors": ["Rick Baker", "Greg Nicotero", "Stan Winston"],
        "d": 3
    },
    {
        "q": "How many real individual background extras were hired to fill the colossal dormitory room during the first game in 'Squid Game'?",
        "correct": "456 real actors and extras",
        "distractors": ["50 extras multiplied by CGI", "100 extras", "250 extras"],
        "d": 3
    },
    {
        "q": "In 'The Mandalorian', which visual effects studio founded by George Lucas pioneered the StageCraft virtual production platform?",
        "correct": "Industrial Light & Magic (ILM)",
        "distractors": ["Wētā FX", "Digital Domain", "Framestore"],
        "d": 1
    },
    {
        "q": "What was the estimated budget per episode for Apple TV+'s period sci-fi drama 'See' starring Jason Momoa in Season 1?",
        "correct": "$15 million per episode",
        "distractors": ["$5 million per episode", "$8 million per episode", "$25 million per episode"],
        "d": 3
    },
    {
        "q": "In Martin Scorsese's Netflix crime epic 'The Irishman', which visual effects technique was heavily employed allowing Robert De Niro and Al Pacino to portray characters across decades?",
        "correct": "De-aging digital markerless facial replacement technology by ILM",
        "distractors": [
            "Deepfake generative neural networks",
            "Full 3D computer-animated body doubles",
            "Traditional silicon prosthetic appliances exclusively"
        ],
        "d": 2
    },
    {
        "q": "How much was the estimated budget for the two-hour series finale episodes (Volume 2) of 'Stranger Things' Season 4 combined?",
        "correct": "Over $60 million",
        "distractors": ["$20 million", "$35 million", "$90 million"],
        "d": 3
    },
    {
        "q": "In 'The Crown', what iconic garment worn by Queen Elizabeth II in the coronation episode was painstakingly recreated by costume designers at a cost of roughly £30,000?",
        "correct": "The Queen's coronation gown and crimson velvet Robe of Estate",
        "distractors": [
            "The Queen's wedding dress",
            "The ceremonial Order of the Garter mantle",
            "The Imperial State Crown with replica diamonds"
        ],
        "d": 3
    },
    {
        "q": "What was the total estimated budget for Netflix's live-action adaptation of 'One Piece' Season 1, costing roughly $18 million per episode?",
        "correct": "$140 million",
        "distractors": ["$80 million", "$100 million", "$200 million"],
        "d": 3
    },
    {
        "q": "Which 2024 Netflix sci-fi series spent an estimated $20 million per episode adapting Liu Cixin's complex Hugo Award-winning novel?",
        "correct": "3 Body Problem",
        "distractors": ["Altered Carbon", "Sense8", "Dark"],
        "d": 2
    },
    {
        "q": "How much was the licensing fee Netflix reportedly paid each year to Sony Pictures Television for the global rights to 'The Crown'?",
        "correct": "An overall production commitment of roughly £100 million per two seasons",
        "distractors": [
            "£20 million per year",
            "£50 million per year",
            "£200 million per year"
        ],
        "d": 3
    },
    {
        "q": "Which streaming platform spent over $450 million in 2021 to acquire the rights to produce two sequels to Rian Johnson's murder mystery 'Knives Out'?",
        "correct": "Netflix",
        "distractors": ["Apple TV+", "Amazon Prime Video", "Max"],
        "d": 2
    },

    # 21-45: Casting Stories, Auditions & Breakthroughs
    {
        "q": "Which Hollywood superstar personally reached out to Martin Short via text message begging to join 'Only Murders in the Building' Season 3 because she loved the show?",
        "correct": "Meryl Streep",
        "distractors": ["Glenn Close", "Shirley MacLaine", "Bette Midler"],
        "d": 1
    },
    {
        "q": "Before landing the role of Eleven in 'Stranger Things' at age 11, Millie Bobby Brown was so devastated by industry rejections that she almost did what?",
        "correct": "Quit acting entirely",
        "distractors": [
            "Moved back to Spain permanently",
            "Switched to professional musical theater",
            "Enrolled full-time in culinary boarding school"
        ],
        "d": 1
    },
    {
        "q": "Which actor, fresh off playing Lip Gallagher for 10 years on 'Shameless', was initially hesitant to take another Chicago working-class role before reading 'The Bear'?",
        "correct": "Jeremy Allen White",
        "distractors": ["Cameron Monaghan", "Noel Fisher", "Steve Howey"],
        "d": 2
    },
    {
        "q": "Which runway fashion model had never acted in any screen production before auditioning for and landing the co-starring role of Kang Sae-byeok (067) in 'Squid Game'?",
        "correct": "Jung Ho-yeon",
        "distractors": ["Kim Joo-ryoung", "Bae Doona", "Park So-dam"],
        "d": 1
    },
    {
        "q": "Which Australian actress initially hesitated and considered turning down the role of Shiv Roy in 'Succession' because she worried American political satire might alienate her?",
        "correct": "Sarah Snook",
        "distractors": ["Rose Byrne", "Toni Collette", "Yvonne Strahovski"],
        "d": 3
    },
    {
        "q": "Which screen icon joined Apple TV+'s comedy 'Shrinking' and Paramount+'s '1923' simultaneously, marking his first major recurring television roles at age 80?",
        "correct": "Harrison Ford",
        "distractors": ["Robert De Niro", "Al Pacino", "Clint Eastwood"],
        "d": 1
    },
    {
        "q": "What British actor was cast as Prince Daemon Targaryen in 'House of the Dragon' after previously starring as Prince Philip in 'The Crown' and the Eleventh Doctor in 'Doctor Who'?",
        "correct": "Matt Smith",
        "distractors": ["David Tennant", "Tobias Menzies", "Tom Glynn-Carney"],
        "d": 1
    },
    {
        "q": "Which comedic actor originally auditioned for the role of Jim Hopper in 'Stranger Things' before David Harbour was ultimately cast?",
        "correct": "No high-profile comedy star was cast, but Harbour was chosen over bigger studio names",
        "distractors": [
            "Will Forte was the studio frontrunner",
            "John C. Reilly turned down the pilot offer",
            "Jason Sudeikis was originally offered the role"
        ],
        "d": 3
    },
    {
        "q": "How did Pedro Pascal secure the lead role of Joel Miller in HBO's 'The Last of Us' while still committed to Disney+'s 'The Mandalorian'?",
        "correct": "His Mandalorian face was rarely shown, allowing stunt doubles (Brendan Wayne and Lateef Crowder) to perform in suit while Pascal voiced the role",
        "distractors": [
            "Disney released him from his Lucasfilm contract early",
            "He filmed both shows concurrently on the same soundstage in Atlanta",
            "Lucasfilm put 'The Mandalorian' on a two-year hiatus to accommodate HBO"
        ],
        "d": 2
    },
    {
        "q": "Which actress and comedian co-wrote the pilot of 'What We Do in the Shadows' and won an Emmy for writing and acting on 'The Bear' as Sydney Adamu?",
        "correct": "Ayo Edebiri",
        "distractors": ["Quinta Brunson", "Janelle James", "Stephanie Hsu"],
        "d": 1
    },
    {
        "q": "Which character in 'The Bear' was specifically written by Christopher Storer for real-life Canadian culinary star and chef Matty Matheson?",
        "correct": "Neil Fak (the handyman)",
        "distractors": ["Gary 'Sweeps' Woods", "Marcus", "Ebraheim"],
        "d": 2
    },
    {
        "q": "What real-life mother and daughter duo played the mother-daughter lead characters in Netflix's 2021 drama miniseries 'Maid'?",
        "correct": "Margaret Qualley and Andie MacDowell",
        "distractors": [
            "Laura Dern and Diane Ladd",
            "Goldie Hawn and Kate Hudson",
            "Blythe Danner and Gwyneth Paltrow"
        ],
        "d": 2
    },
    {
        "q": "Which British actress was cast as Queen Elizabeth II in Seasons 5 and 6 of 'The Crown' after having previously portrayed Dolores Umbridge in the Harry Potter franchise?",
        "correct": "Imelda Staunton",
        "distractors": ["Maggie Smith", "Fiona Shaw", "Julie Walters"],
        "d": 1
    },
    {
        "q": "Which actor portrayed Logan Roy's estranged eldest son Connor Roy in 'Succession', having decades earlier starred in 'Ferris Bueller's Day Off'?",
        "correct": "Alan Ruck",
        "distractors": ["Matthew Broderick", "Jeffrey Jones", "Judge Reinhold"],
        "d": 1
    },
    {
        "q": "Who was the first actor officially cast by the Duffer Brothers for 'Stranger Things', serving as the veteran anchor for the series?",
        "correct": "Winona Ryder (as Joyce Byers)",
        "distractors": ["David Harbour", "Matthew Modine", "Paul Reiser"],
        "d": 2
    },
    {
        "q": "Which actor auditioned for the role of Homelander in 'The Boys' while reading the sides in an American accent before Eric Kripke cast him?",
        "correct": "Antony Starr (a New Zealander)",
        "distractors": ["Karl Urban", "Nathan Fillion", "Alexander Skarsgård"],
        "d": 3
    },
    {
        "q": "Who recommended Bella Ramsey to Craig Mazin for the role of Ellie in 'The Last of Us' after seeing her fierce performance as Lyanna Mormont in 'Game of Thrones'?",
        "correct": "David Benioff and D.B. Weiss",
        "distractors": ["Pedro Pascal", "Neil Druckmann", "Peter Dinklage"],
        "d": 3
    },
    {
        "q": "Which actress landed the breakout role of Wednesday Addams after Tim Burton personally Zoomed with her while she was filming in New Zealand covered in fake horror blood?",
        "correct": "Jenna Ortega",
        "distractors": ["Sadie Sink", "Chloë Grace Moretz", "Kiernan Shipka"],
        "d": 2
    },
    {
        "q": "Which veteran character actor was cast as Hector Salamanca in 'Breaking Bad' and 'Better Call Saul', receiving an Emmy nomination despite having almost no spoken dialogue?",
        "correct": "Mark Margolis",
        "distractors": ["Raymond Cruz", "Steven Bauer", "Giancarlo Esposito"],
        "d": 2
    },
    {
        "q": "In Apple TV+'s 'Severance', which cast member was cast as Dylan George after Ben Stiller saw his viral stand-up comedy and commercial appearances?",
        "correct": "Zach Cherry",
        "distractors": ["Tramell Tillman", "Michael Chernus", "Yul Vazquez"],
        "d": 3
    },
    {
        "q": "Which Broadway legend made a guest appearance as bunny-loving theater legend Bunny Folger's mother Leonora Folger in 'Only Murders in the Building' Season 2?",
        "correct": "Shirley MacLaine",
        "distractors": ["Rita Moreno", "Angela Lansbury", "Liza Minnelli"],
        "d": 3
    },
    {
        "q": "What British actor played both Lord Voldemort's snake Nagini's master and Prince Philip in 'The Crown' Season 3 and 4?",
        "correct": "Tobias Menzies",
        "distractors": ["Jonathan Pryce", "Ben Daniels", "Jason Isaacs"],
        "d": 3
    },
    {
        "q": "Which comedy star was originally cast as Greg Hirsch in 'Succession' before Nicholas Braun took the role?",
        "correct": "Nicholas Braun was cast from the pilot; no other actor shot scenes as Greg",
        "distractors": [
            "Thomas Middleditch was originally cast",
            "Kumail Nanjiani shot test pilot scenes",
            "Pete Davidson was considered for the role"
        ],
        "d": 3
    },
    {
        "q": "Which Oscar-winning actor was cast as eccentric billionaire Peter Weyland in 'Prometheus' and later played Logan Roy's wealthy investor rival Josh Aaronson in 'Succession'?",
        "correct": "Adrien Brody",
        "distractors": ["Guy Pearce", "Mark Rylance", "Sam Rockwell"],
        "d": 3
    },
    {
        "q": "Who portrayed Martha, the relentless stalker in Netflix's 2024 sensation 'Baby Reindeer', winning critical raves for her terrifying yet sympathetic performance?",
        "correct": "Jessica Gunning",
        "distractors": ["Nava Mau", "Daisy May Cooper", "Sharon Horgan"],
        "d": 2
    },

    # 46-70: Filming Locations, Architecture & Logistical Challenges
    {
        "q": "What real-life architectural marvel in Holmdel, New Jersey—designed by legendary modernist Eero Saarinen—serves as the corporate headquarters exterior of Lumon Industries in 'Severance'?",
        "correct": "Bell Works (the former Bell Labs Holmdel Complex)",
        "distractors": [
            "The Armstrong Rubber Building",
            "The TWA Flight Center",
            "The IBM Somers Complex"
        ],
        "d": 2
    },
    {
        "q": "Which real-life Chicago sandwich shop on Orleans Street served as the exterior and pilot-episode interior filming location for 'The Bear'?",
        "correct": "Mr. Beef on Orleans",
        "distractors": ["Al's #1 Italian Beef", "Portillo's", "Johnnie's Beef"],
        "d": 1
    },
    {
        "q": "In 'Succession' Season 3, what magnificent historic estate in the hills of Tuscany, Italy served as the setting for Lady Caroline Collingwood's lavish wedding?",
        "correct": "Villa Cetinale",
        "distractors": ["Villa d'Este", "Villa del Balbianello", "Villa Ephrussi de Rothschild"],
        "d": 3
    },
    {
        "q": "Where were the striking ghost-town desert scenes depicting the apocalyptic California wasteland filmed for Prime Video's 'Fallout'?",
        "correct": "Kolmanskop, a real-life abandoned diamond-mining ghost town in the Namib Desert in Namibia",
        "distractors": [
            "The Mojave Desert near Barstow, California",
            "The Atacama Desert in northern Chile",
            "The White Sands National Park in New Mexico"
        ],
        "d": 3
    },
    {
        "q": "Which ancient Portuguese village built into and around giant granite boulders served as the filming location for the ancestral Targaryen stronghold Dragonstone in 'House of the Dragon'?",
        "correct": "Monsanto, Portugal",
        "distractors": ["Sintra, Portugal", "Marvão, Portugal", "Óbidos, Portugal"],
        "d": 3
    },
    {
        "q": "What luxury resort served as the primary filming and cast-bubble quarantine location for 'The White Lotus' Season 1 during the height of the COVID-19 pandemic in late 2020?",
        "correct": "Four Seasons Resort Maui at Wailea",
        "distractors": [
            "The Ritz-Carlton, Kapalua",
            "Grand Wailea, A Waldorf Astoria Resort",
            "Montage Kapalua Bay"
        ],
        "d": 2
    },
    {
        "q": "In 'The Crown', which historic English country house stood in for Buckingham Palace's grand interior state rooms across multiple seasons?",
        "correct": "Lancaster House (and Wilton House)",
        "distractors": ["Blenheim Palace", "Highclere Castle", "Chatsworth House"],
        "d": 3
    },
    {
        "q": "Which medieval Spanish city, previously used for King's Landing in 'Game of Thrones', returned as the primary exterior location for King's Landing in 'House of the Dragon'?",
        "correct": "Cáceres (Extremadura, Spain)",
        "distractors": ["Dubrovnik, Croatia", "Girona, Spain", "Seville, Spain"],
        "d": 3
    },
    {
        "q": "In 'The Last of Us', which Canadian province served as the primary filming location standing in for various post-apocalyptic American cities including Boston and Jackson?",
        "correct": "Alberta (Calgary, Edmonton, and Canmore)",
        "distractors": ["British Columbia (Vancouver)", "Ontario (Toronto)", "Quebec (Montreal)"],
        "d": 2
    },
    {
        "q": "What Norwegian luxury hotel perched on a fjord cliff served as Lukas Matsson's Scandinavian retreat in 'Succession' Season 4 Episode 5?",
        "correct": "Juvet Landscape Hotel in Valldal, Norway",
        "distractors": [
            "The Arctic TreeHouse Hotel",
            "Treehotel Harads",
            "Manshausen Island Resort"
        ],
        "d": 3
    },
    {
        "q": "Where in the United States does the production of Netflix's 'Stranger Things' primarily film all its Hawkins suburban neighborhoods and school exteriors?",
        "correct": "Atlanta and surrounding towns in Georgia",
        "distractors": ["Vancouver, British Columbia", "Albuquerque, New Mexico", "Wilmington, North Carolina"],
        "d": 2
    },
    {
        "q": "What historic converted psychiatric hospital in Atlanta, Georgia was used as the exterior filming location for the Hawkins National Laboratory in 'Stranger Things'?",
        "correct": "Emory University's Briarcliff Campus (former Georgia Mental Health Institute)",
        "distractors": [
            "Central State Hospital in Milledgeville",
            "Danvers State Hospital",
            "Trenton Psychiatric Hospital"
        ],
        "d": 3
    },
    {
        "q": "In Apple TV+'s 'Ted Lasso', which historic street in southwest London served as the picturesque cobblestone exterior where Ted's flat and pub are located?",
        "correct": "Paved Court in Richmond Green, London",
        "distractors": ["Portobello Road in Notting Hill", "Carnaby Street in Soho", "Columbia Road in Bethnal Green"],
        "d": 3
    },
    {
        "q": "Which luxury cliffside hotel in Taormina, Sicily served as the filming location for 'The White Lotus' Season 2, formerly a 14th-century Dominican convent?",
        "correct": "San Domenico Palace (Four Seasons)",
        "distractors": [
            "Belmond Grand Hotel Timeo",
            "Villa Sant'Andrea",
            "The Ashbee Hotel"
        ],
        "d": 3
    },
    {
        "q": "In 'Squid Game', on what uninhabited South Korean island were the dramatic exterior island cliffs and drone shots of the secret gaming facility filmed?",
        "correct": "Seungbong-do (specifically Guleop-do)",
        "distractors": ["Jeju Island", "Ulleungdo", "Ganghwado"],
        "d": 3
    },
    {
        "q": "In Disney+'s 'Andor', which futuristic high-rise building in London served as the sleek, oppressive Coruscant apartment of Senator Mon Mothma?",
        "correct": "The Brunel Building in Paddington",
        "distractors": ["The Gherkin", "The Shard", "One Blackfriars"],
        "d": 3
    },
    {
        "q": "Which Scottish coastal fishing town served as the location for the vibrant, crowded Ferrix marketplace and funeral procession in 'Andor'?",
        "correct": "Little Marlow in Buckinghamshire (built on a massive outdoor quarry backlot)",
        "distractors": [
            "Stonehaven, Scotland",
            "Oban, Scotland",
            "Portree, Isle of Skye"
        ],
        "d": 3
    },
    {
        "q": "In 'House of the Dragon', where was the dramatic coastal fortress of High Tide on Driftmark (seat of House Velaryon) filmed?",
        "correct": "St Michael's Mount in Cornwall, England",
        "distractors": ["Mont-Saint-Michel in Normandy", "Dunluce Castle in Northern Ireland", "Bamburgh Castle in Northumberland"],
        "d": 3
    },
    {
        "q": "What iconic New York skyscraper served as the real-world filming location for the sleek executive offices of Waystar Royco in 'Succession' Season 1?",
        "correct": "4 World Trade Center (and later 7 World Trade Center)",
        "distractors": ["The Empire State Building", "Rockefeller Plaza", "The Chrysler Building"],
        "d": 3
    },
    {
        "q": "Where in Chicago did the production of 'The Bear' build an exact, working replica of the Mr. Beef kitchen after filming the pilot inside the real restaurant?",
        "correct": "Cinespace Chicago Film Studios",
        "distractors": ["Chicago Studio City", "Essanay Studios", "Trilogy Studios"],
        "d": 3
    },
    {
        "q": "In 'Yellowstone' and its streaming spinoffs '1883' and '1923', what real Montana ranch serves as the iconic Chief Joseph Ranch where the Dutton family resides?",
        "correct": "Chief Joseph Ranch in Darby, Montana",
        "distractors": ["Flying D Ranch", "Bozeman Creek Ranch", "Bitterroot River Ranch"],
        "d": 3
    },
    {
        "q": "Which real estate mansion in Lake of the Ozarks or Atlanta served as the Byrde family lakeside home in Netflix's 'Ozark'?",
        "correct": "Lake Allatoona and Lake Lanier in Georgia (not Missouri)",
        "distractors": [
            "Lake of the Ozarks in Missouri",
            "Table Rock Lake in Missouri",
            "Lake Norman in North Carolina"
        ],
        "d": 3
    },
    {
        "q": "In 'The Mandalorian', how tall is the curved LED StageCraft video wall enclosure constructed on the Manhattan Beach Studios lot?",
        "correct": "20 feet tall and 75 feet in diameter",
        "distractors": ["10 feet tall and 40 feet in diameter", "35 feet tall and 120 feet in diameter", "50 feet tall and 200 feet in diameter"],
        "d": 3
    },
    {
        "q": "Where in the United Kingdom did the production of Prime Video's 'The Rings of Power' relocate for Season 2 after filming Season 1 in New Zealand?",
        "correct": "Bray Film Studios and Bovingdon Airfield in England",
        "distractors": [
            "Leavesden Studios in Watford",
            "Pinewood Studios in Buckinghamshire",
            "Belfast Harbor Studios in Northern Ireland"
        ],
        "d": 3
    },
    {
        "q": "Which iconic street in Albuquerque, New Mexico features the real car wash owned by Walter White in 'Breaking Bad' (Octopus Car Wash, now Mister Car Wash)?",
        "correct": "Snow Heights Circle NE (Menaul Blvd)",
        "distractors": ["Central Avenue", "Lomas Boulevard", "Coors Boulevard"],
        "d": 3
    },

    # 71-100: Critical Reception, Reviews, Cancellations & Industry Upheavals
    {
        "q": "In 2023, what unprecedented simultaneous labor action shut down almost all streaming television productions for nearly five months?",
        "correct": "The joint WGA (Writers Guild of America) and SAG-AFTRA (Screen Actors Guild) strikes",
        "distractors": [
            "The IATSE nationwide technical team walkout",
            "The Directors Guild of America solo strike",
            "The Teamsters theatrical driver boycott"
        ],
        "d": 1
    },
    {
        "q": "What central issue regarding streaming compensation was a primary catalyst for the 2023 Hollywood writers' and actors' strikes?",
        "correct": "Streaming residual formulas based on viewership transparency and success metrics",
        "distractors": [
            "Mandatory 60-day theatrical exclusivity windows",
            "Elimination of foreign language dubbing programs",
            "Banning the use of green screen technology"
        ],
        "d": 2
    },
    {
        "q": "Which high-profile Netflix mystery sci-fi series by the creators of 'Dark' was abruptly canceled in early 2023 after only one season, despite strong European viewing hours?",
        "correct": "1899",
        "distractors": ["The OA", "Sense8", "Archive 81"],
        "d": 2
    },
    {
        "q": "In late 2022, Warner Bros. Discovery shocked the television industry by canceling which critically acclaimed, multi-Emmy-winning HBO sci-fi series and removing it entirely from HBO Max for tax write-downs?",
        "correct": "Westworld",
        "distractors": ["Raised by Wolves", "The Nevers", "Carnivàle"],
        "d": 2
    },
    {
        "q": "Which controversial 2023 HBO/Max drama series created by Sam Levinson and Abel 'The Weeknd' Tesfaye was widely panned by critics at Cannes and canceled after five episodes?",
        "correct": "The Idol",
        "distractors": ["Euphoria", "Industry", "Vinyl"],
        "d": 2
    },
    {
        "q": "Which Netflix supernatural series starring Brit Marling developed a devoted cult following that staged public protests and hunger strikes in Los Angeles when it was canceled in 2019 after Season 2?",
        "correct": "The OA",
        "distractors": ["Sense8", "Chilling Adventures of Sabrina", "Shadow and Bone"],
        "d": 3
    },
    {
        "q": "What live-action superhero series originally developed for DC Universe was saved by fan outcry and moved to HBO Max for Seasons 3 and 4 before concluding in 2023?",
        "correct": "Doom Patrol (and Titans)",
        "distractors": ["Swamp Thing", "Stargirl", "Krypton"],
        "d": 3
    },
    {
        "q": "Which Netflix fantasy series based on Leigh Bardugo's Grishaverse novels was canceled in late 2023 after two seasons, scrapping a planned 'Six of Crows' spinoff?",
        "correct": "Shadow and Bone",
        "distractors": ["Locke & Key", "Fate: The Winx Saga", "The Letter for the King"],
        "d": 3
    },
    {
        "q": "In 2022, Warner Bros. Discovery famously made the unprecedented decision to permanently shelve which completed $90 million DC superhero film intended for HBO Max?",
        "correct": "Batgirl",
        "distractors": ["Supergirl", "Zatanna", "Wonder Twins"],
        "d": 2
    },
    {
        "q": "Which historical comedy-drama starring Elle Fanning and Nicholas Hoult was unexpectedly canceled by Hulu in 2023 after three seasons despite receiving critical acclaim and Emmy nominations?",
        "correct": "The Great",
        "distractors": ["Dickinson", "Harlots", "The Serpent Queen"],
        "d": 3
    },
    {
        "q": "What Rotten Tomatoes approval rating milestone did FX/Hulu's 'Shōgun' achieve upon its 2024 debut, earning widespread comparisons to peak 'Game of Thrones'?",
        "correct": "99% Certified Fresh from critics",
        "distractors": ["82% Fresh", "88% Fresh", "91% Fresh"],
        "d": 3
    },
    {
        "q": "What was the Rotten Tomatoes critic score for the acclaimed first season of 'The Bear' upon its June 2022 release?",
        "correct": "100% Certified Fresh",
        "distractors": ["89% Fresh", "93% Fresh", "96% Fresh"],
        "d": 3
    },
    {
        "q": "Which Netflix series about an 18th-century Austrian monarch, Empress Elisabeth, became an international sleeper hit in 2022 and won the International Emmy for Best Drama?",
        "correct": "The Empress",
        "distractors": ["Sisi", "Charité", "Maximilian"],
        "d": 3
    },
    {
        "q": "Which live-action anime adaptation on Netflix achieved a rare 85%+ critic rating and 95%+ audience score in 2023, reversing Netflix's curse of poorly received anime adaptations?",
        "correct": "One Piece",
        "distractors": ["Cowboy Bebop", "Death Note", "Avatar: The Last Airbender"],
        "d": 3
    },
    {
        "q": "What was the critical response to the live-action 'Cowboy Bebop' series on Netflix in 2021, leading to its swift cancellation less than one month after premiere?",
        "correct": "A 46% Rotten Tomatoes score and swift cancellation due to poor completion rates",
        "distractors": [
            "A 75% score that failed to find an audience",
            "Universal critical praise that was too expensive to renew",
            "Positive domestic ratings but a total boycott in Japan"
        ],
        "d": 3
    },
    {
        "q": "In 2024, what real-world legal action followed the viral success of Netflix's 'Baby Reindeer'?",
        "correct": "A $170 million defamation and emotional distress lawsuit filed by Fiona Harvey, claiming she was defamed as the real-life Martha",
        "distractors": [
            "A trademark infringement lawsuit by the Edinburgh Fringe Festival",
            "A criminal indictment against Richard Gadd for unauthorized recording",
            "A copyright injunction filed by the BBC over script rights"
        ],
        "d": 3
    },
    {
        "q": "Which New York Times television critic wrote the influential review hailing 'Succession' as 'the finest television drama of the decade' during its third season?",
        "correct": "James Poniewozik",
        "distractors": ["Emily Nussbaum", "Matt Zoller Seitz", "Alan Sepinwall"],
        "d": 3
    },
    {
        "q": "Which Rolling Stone television critic published glowing, definitive episode-by-episode recaps and retrospective books on 'The Sopranos', 'Breaking Bad', and 'Succession'?",
        "correct": "Alan Sepinwall",
        "distractors": ["David Bianculli", "Tim Goodman", "Ken Tucker"],
        "d": 3
    },
    {
        "q": "What rare achievement did 'Fleabag' Season 2 attain on review aggregator Metacritic in 2019, making it one of the highest-rated television seasons in Metacritic history?",
        "correct": "A Metascore of 96 out of 100",
        "distractors": ["A Metascore of 88 out of 100", "A Metascore of 91 out of 100", "A Metascore of 100 out of 100"],
        "d": 3
    },
    {
        "q": "Which acclaimed Apple TV+ comedy about video game development created by Rob McElhenney, Charlie Day, and Megan Ganz was renewed for four seasons?",
        "correct": "Mythic Quest",
        "distractors": ["Silicon Valley", "Severance", "Players"],
        "d": 3
    },
    {
        "q": "What streaming service originally commissioned and aired the dark anthology series 'Black Mirror' before Netflix purchased the franchise rights in 2015?",
        "correct": "Channel 4 (United Kingdom)",
        "distractors": ["BBC One", "ITV", "Sky Atlantic"],
        "d": 2
    },
    {
        "q": "Which streaming platform rescued the canceled Fox police comedy 'Brooklyn Nine-Nine' in 2018 within 31 hours of Fox canceling it?",
        "correct": "NBC (broadcast network with immediate streaming on Hulu and Peacock)",
        "distractors": ["Netflix", "Amazon Prime Video", "TBS"],
        "d": 2
    },
    {
        "q": "Which beloved supernatural series canceled by NBC in 2021 was saved by Netflix for a super-sized 20-episode fourth and final season after charting #1 on Netflix for weeks?",
        "correct": "Manifest",
        "distractors": ["Lucifer", "Designated Survivor", "Longmire"],
        "d": 2
    },
    {
        "q": "Which acclaimed fantasy comedy series starring Tom Ellis was canceled by Fox after three seasons in 2018 and picked up by Netflix for three additional seasons?",
        "correct": "Lucifer",
        "distractors": ["Constantine", "Preacher", "Sleepy Hollow"],
        "d": 2
    },
    {
        "q": "Which Netflix sci-fi series created by the Wachowskis was canceled in 2017 due to its massive $9 million per episode budget, but granted a two-hour finale special after global fan petitions?",
        "correct": "Sense8",
        "distractors": ["Altered Carbon", "The OA", "Dark"],
        "d": 3
    },
    {
        "q": "In 2022, what company acquired WarnerMedia from AT&T in a $43 billion mega-merger to form Warner Bros. Discovery under CEO David Zaslav?",
        "correct": "Discovery, Inc.",
        "distractors": ["Comcast", "Paramount Global", "Sony Entertainment"],
        "d": 3
    },
    {
        "q": "Which critically acclaimed Hulu comedy about a Native American teenager and his friends living on an Oklahoma reservation was created by Sterlin Harjo and Taika Waititi?",
        "correct": "Reservation Dogs",
        "distractors": ["Rutherford Falls", "Dark Winds", "Smoke Signals"],
        "d": 2
    },
    {
        "q": "In 2024, what landmark deal allowed Disney+ to officially integrate Hulu content into a single unified app experience for bundle subscribers?",
        "correct": "The Hulu on Disney+ integrated hub",
        "distractors": [
            "The Disney-Comcast unified media interface",
            "The Star Stream launcher",
            "The ABC Unlimited portal"
        ],
        "d": 3
    },
    {
        "q": "Which acclaimed animated sci-fi series was canceled by Max in 2023, only to be licensed to Netflix in 2024 where it found a massive new audience?",
        "correct": "Scavengers Reign",
        "distractors": ["Pantheon", "Inside Job", "Final Space"],
        "d": 3
    },
    {
        "q": "What documentary film won the first Academy Award of any kind for Netflix at the 90th Academy Awards in 2018, exposing state-sponsored Russian Olympic doping?",
        "correct": "Icarus",
        "distractors": ["13th", "The White Helmets", "My Octopus Teacher"],
        "d": 3
    }
]

if __name__ == "__main__":
    build_batch(BATCH_5, "tools/staging/streaming_tv_batch5.json", batch_num=5)
