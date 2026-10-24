#!/usr/bin/env python3
"""
Generate Batch 3 of Streaming TV Shows trivia (100 questions):
Max & Disney+ Flagships: Succession, The White Lotus, Hacks, House of the Dragon,
The Last of Us, Peacemaker, Station Eleven, The Mandalorian, Andor, WandaVision, Loki, Shōgun.
Target: ~20 d1, ~40 d2, ~40 d3.
"""

from streaming_tv_batch_builder import build_batch

BATCH_3 = [
    # 1-16: Succession (Max / HBO)
    {
        "q": "In the acclaimed drama 'Succession', what is the name of the global media and entertainment conglomerate founded by patriarch Logan Roy?",
        "correct": "Waystar Royco",
        "distractors": ["Pierce Global Media", "Vaulter Media", "Furness Media Group"],
        "d": 1
    },
    {
        "q": "Which Scottish actor portrays the ruthless, commanding media titan Logan Roy in 'Succession'?",
        "correct": "Brian Cox",
        "distractors": ["Jeremy Strong", "Alan Ruck", "Matthew Macfadyen"],
        "d": 1
    },
    {
        "q": "What song does Kendall Roy perform in baseball jersey and rap attire at his father's 50th-anniversary company gala in Season 2?",
        "correct": "L to the OG",
        "distractors": ["All the Roy Girls", "King Logan", "Big Star Waystar"],
        "d": 1
    },
    {
        "q": "In the series finale of 'Succession', who is named the new American CEO of Waystar Royco following GoJo's acquisition?",
        "correct": "Tom Wambsgans",
        "distractors": ["Kendall Roy", "Siobhan 'Shiv' Roy", "Roman Roy"],
        "d": 1
    },
    {
        "q": "In 'Succession' Season 4 Episode 3 ('Connor's Wedding'), where is Logan Roy when he suffers his fatal cardiac arrest?",
        "correct": "Aboard a private jet en route to Sweden",
        "distractors": [
            "At the church rehearsal dinner for Connor's wedding",
            "In his Fifth Avenue penthouse library",
            "Aboard the family yacht in the Mediterranean"
        ],
        "d": 2
    },
    {
        "q": "Which Swedish eccentric tech billionaire, founder of GoJo, is played by Alexander Skarsgård in 'Succession'?",
        "correct": "Lukas Matsson",
        "distractors": ["Oskar Gudjohnsen", "Lawrence Yee", "Josh Aaronson"],
        "d": 2
    },
    {
        "q": "What British television creator and former 'Peep Show' writer created and served as showrunner for 'Succession'?",
        "correct": "Jesse Armstrong",
        "distractors": ["Armando Iannucci", "Sam Bain", "Peter Morgan"],
        "d": 2
    },
    {
        "q": "What is the name of the right-wing cable news network owned by Waystar Royco where Tom and Greg work?",
        "correct": "ATN (American Television Network)",
        "distractors": ["ANC News", "GBS World", "LNN America"],
        "d": 2
    },
    {
        "q": "What culinary concoction do Kendall, Shiv, and Roman make for Kendall in their mother's kitchen in the 'Succession' series finale?",
        "correct": "A meal fit for a king, containing milk, hot sauce, raw egg, and bread crusts",
        "distractors": [
            "A traditional English Sunday roast with burnt Yorkshire puddings",
            "A bowl of frosted flakes mixed with expensive champagne",
            "A smoothie made with protein powder and single-malt scotch"
        ],
        "d": 2
    },
    {
        "q": "Which method actor won a Lead Actor Emmy for playing Kendall Roy, known for his intense character immersion?",
        "correct": "Jeremy Strong",
        "distractors": ["Kieran Culkin", "Matthew Macfadyen", "Nicholas Braun"],
        "d": 1
    },
    {
        "q": "In 'Succession' Season 2, what cruise ship scandal cover-up becomes the central liability threatening Waystar?",
        "correct": "The Brightstar cruise line sexual misconduct and wrongful death cover-up ('Mo' Lester)",
        "distractors": [
            "Unreported maritime pollution and toxic waste dumping",
            "Illegal offshore tax shelters in the Cayman Islands",
            "Bribery of foreign port officials in Southeast Asia"
        ],
        "d": 3
    },
    {
        "q": "What board game do the Roys and their extended family play during Thanksgiving in Season 1, leading to an argument?",
        "correct": "I Went to Market",
        "distractors": ["Monopoly", "Scrabble", "Charades"],
        "d": 3
    },
    {
        "q": "Who wrote the iconic piano-and-strings theme music for 'Succession' that became a viral cultural sensation?",
        "correct": "Nicholas Britell",
        "distractors": ["Max Richter", "Ramin Djawadi", "Ludwig Göransson"],
        "d": 2
    },
    {
        "q": "In 'Succession' Season 3, what controversial election-night decision does ATN make under Roman and Tom's direction?",
        "correct": "Prematurely projecting far-right nationalist Jeryd Mencken as the presidential winner",
        "distractors": [
            "Declaring Connor Roy the surprise winner of Kentucky",
            "Refusing to broadcast live election returns",
            "Falsely reporting that electronic voting machines were hacked"
        ],
        "d": 2
    },
    {
        "q": "What is the title of the acclaimed Season 4 episode that captured Logan Roy's death in real time using 35mm cameras?",
        "correct": "Connor's Wedding",
        "distractors": ["America Decides", "Church and State", "With Open Eyes"],
        "d": 2
    },
    {
        "q": "What percent of the national vote was Connor Roy desperately trying to reach in his quixotic presidential campaign?",
        "correct": "One percent",
        "distractors": ["Five percent", "Ten percent", "Zero point five percent"],
        "d": 3
    },

    # 17-26: The White Lotus (Max / HBO)
    {
        "q": "Who created, wrote, and directed both seasons of the anthology satire 'The White Lotus'?",
        "correct": "Mike White",
        "distractors": ["Ryan Murphy", "David White", "Chuck Lorre"],
        "d": 1
    },
    {
        "q": "Which actress won back-to-back Emmys for her unforgettable performance as heiress Tanya McQuoid in 'The White Lotus'?",
        "correct": "Jennifer Coolidge",
        "distractors": ["Connie Britton", "Aubrey Plaza", "Laura Dern"],
        "d": 1
    },
    {
        "q": "Where are the luxury White Lotus resorts located in Season 1 and Season 2, respectively?",
        "correct": "Hawaii (Maui) and Italy (Sicily)",
        "distractors": [
            "Hawaii (Maui) and Thailand (Koh Samui)",
            "The Bahamas and French Polynesia (Bora Bora)",
            "Costa Rica and Greece (Santorini)"
        ],
        "d": 1
    },
    {
        "q": "Which Australian actor played Armond, the stressed, spiraling resort manager in 'The White Lotus' Season 1?",
        "correct": "Murray Bartlett",
        "distractors": ["Guy Pearce", "Simon Baker", "David Wenham"],
        "d": 2
    },
    {
        "q": "What famous panicked line does Tanya McQuoid utter to the ship captain before trying to escape the yacht in the Season 2 finale?",
        "correct": "These gays, they're trying to murder me!",
        "distractors": [
            "I know what you did in Palermo!",
            "Greg never loved me from the start!",
            "Take me back to Taormina right now!"
        ],
        "d": 1
    },
    {
        "q": "How does Tanya McQuoid tragically die in the final moments of 'The White Lotus' Season 2?",
        "correct": "She slips off the railing of the yacht trying to jump into a dinghy, hits her head, and drowns",
        "distractors": [
            "She is shot by Quentin inside the luxury stateroom",
            "She is poisoned with champagne during the farewell dinner",
            "She is thrown overboard during a struggle on the open sea"
        ],
        "d": 2
    },
    {
        "q": "Which composer created the tribal, jungle-inspired, operatic theme score for 'The White Lotus'?",
        "correct": "Cristobal Tapia de Veer",
        "distractors": ["Bear McCreary", "Hans Zimmer", "Clint Mansell"],
        "d": 3
    },
    {
        "q": "Which Italian actress won a SAG Award and received an Emmy nomination for playing aspiring singer Mia in Season 2?",
        "correct": "Simona Tabasco",
        "distractors": ["Beatrice Grannò", "Sabrina Impacciatore", "Monica Bellucci"],
        "d": 3
    },
    {
        "q": "In 'The White Lotus' Season 1, what pineapple-themed suite dispute consumes Shane Patton (Jake Lacy) during his honeymoon?",
        "correct": "The Pineapple Suite",
        "distractors": ["The Royal Hibiscus Villa", "The Palm Veranda", "The Orchid Bungalow"],
        "d": 2
    },
    {
        "q": "What Greek mythological legend regarding male vanity is referenced by Bert Di Grasso at the ancient theatre in Taormina?",
        "correct": "The myth of Hades and Persephone",
        "distractors": ["The myth of Narcissus and Echo", "The myth of Oedipus", "The myth of Icarus"],
        "d": 3
    },

    # 27-36: Hacks (Max)
    {
        "q": "In the Max comedy series 'Hacks', who stars as legendary Las Vegas stand-up comedy diva Deborah Vance?",
        "correct": "Jean Smart",
        "distractors": ["Christine Baranski", "Jane Fonda", "Bette Midler"],
        "d": 1
    },
    {
        "q": "What is the name of the canceled twenty-something comedy writer hired to refresh Deborah's aging material?",
        "correct": "Ava Daniels (Hannah Einbinder)",
        "distractors": ["Kayla Daniels (Meg Stalter)", "Robin Buckley (Maya Hawke)", "Phoebe Waller (Abbi Jacobson)"],
        "d": 1
    },
    {
        "q": "What major upset occurred at the 76th Primetime Emmy Awards in 2024 when 'Hacks' defeated front-runner 'The Bear'?",
        "correct": "It won Outstanding Comedy Series",
        "distractors": [
            "It won Outstanding Casting for a Comedy Series",
            "It set the record for most technical Emmys won by Max",
            "Hannah Einbinder tied for Lead Actress in a Comedy Series"
        ],
        "d": 1
    },
    {
        "q": "What is the name of the fictional Las Vegas casino where Deborah Vance performs her residency in Season 1?",
        "correct": "The Palmetto Casino",
        "distractors": ["The Mirage", "The Golden Nugget", "The Bellagio Palace"],
        "d": 2
    },
    {
        "q": "Who created 'Hacks' alongside Paul W. Downs and Jen Statsky?",
        "correct": "Lucia Aniello",
        "distractors": ["Amy Sherman-Palladino", "Mindy Kaling", "Ilana Glazer"],
        "d": 2
    },
    {
        "q": "What major career goal does Deborah Vance pursue and ultimately achieve in Season 3 of 'Hacks'?",
        "correct": "Hosting a network late-night talk show",
        "distractors": [
            "Starring in a Broadway revival of 'Gypsy'",
            "Directing an autobiographical indie film",
            "Winning a Lifetime Achievement Grammy Award"
        ],
        "d": 2
    },
    {
        "q": "Which actor plays Deborah and Ava's long-suffering, neurotic manager Jimmy LuSaque on 'Hacks'?",
        "correct": "Paul W. Downs",
        "distractors": ["Carl Clemons-Hopkins", "Mark Indelicato", "Christopher McDonald"],
        "d": 2
    },
    {
        "q": "What piece of vintage kitchen equipment did Deborah famously sign and sell on QVC that made her tens of millions?",
        "correct": "The Deborah Vance Non-Stick Pan collection",
        "distractors": ["The Vance Waffle Iron", "The Vegas Air Fryer", "The Deborah Immersion Blender"],
        "d": 3
    },
    {
        "q": "What is the secret Deborah Vance has carried for decades regarding her former husband's house burning down?",
        "correct": "She didn't burn it down, but let the rumor persist because it made people afraid of her",
        "distractors": [
            "She deliberately threw a lit cigarette onto his mattress",
            "Her sister accidentally started the grease fire",
            "It was an insurance fraud scam orchestrated by the casino"
        ],
        "d": 3
    },
    {
        "q": "In Season 2, where do Deborah and Ava embark on a low-budget tour to workshop her raw new stand-up set?",
        "correct": "On a tour bus across small clubs in the American South and Midwest",
        "distractors": [
            "On a luxury comedy cruise through the Caribbean",
            "Across performing arts centers in Western Europe",
            "In independent college campuses across the Pacific Northwest"
        ],
        "d": 2
    },

    # 37-48: House of the Dragon & The Last of Us (Max / HBO)
    {
        "q": "In 'House of the Dragon', which Targaryen civil war over the Iron Throne forms the central conflict of the series?",
        "correct": "The Dance of the Dragons",
        "distractors": ["The Blackfyre Rebellion", "The Conquest of Dorne", "The War of the Ninepenny Kings"],
        "d": 1
    },
    {
        "q": "Which two actresses portray Princess Rhaenyra Targaryen as a youth and as an adult, respectively?",
        "correct": "Milly Alcock and Emma D'Arcy",
        "distractors": [
            "Emily Carey and Olivia Cooke",
            "Sophie Turner and Emilia Clarke",
            "Maisie Williams and Natalie Dormer"
        ],
        "d": 1
    },
    {
        "q": "Which actor won widespread critical acclaim for his poignant portrayal of King Viserys I Targaryen in Season 1?",
        "correct": "Paddy Considine",
        "distractors": ["Matt Smith", "Rhys Ifans", "Fabien Frankel"],
        "d": 1
    },
    {
        "q": "What is the name of the colossal, ancient female dragon ridden by Prince Aemond Targaryen?",
        "correct": "Vhagar",
        "distractors": ["Caraxes", "Syrax", "Meleys"],
        "d": 1
    },
    {
        "q": "What infamous revenge act orchestrated by Daemon Targaryen in the Season 2 premiere shocks King's Landing?",
        "correct": "Blood and Cheese infiltrating the Red Keep to murder Prince Jaehaerys",
        "distractors": [
            "The poisoning of the royal wine cellars during a council feast",
            "The burning of the Dragonpit by Sunfyre",
            "The kidnapping of Dowager Queen Alicent Hightower"
        ],
        "d": 2
    },
    {
        "q": "Which George R.R. Martin book serves as the primary historical source text for 'House of the Dragon'?",
        "correct": "Fire & Blood",
        "distractors": ["The World of Ice & Fire", "A Knight of the Seven Kingdoms", "The Rise of the Dragon"],
        "d": 2
    },
    {
        "q": "In HBO's 'The Last of Us', what real-world fungal pathogen mutates to infect and collapse human civilization?",
        "correct": "Cordyceps",
        "distractors": ["Aspergillus", "Candida auris", "Claviceps purpurea"],
        "d": 1
    },
    {
        "q": "Which two actors star as Joel Miller and Ellie Williams in 'The Last of Us'?",
        "correct": "Pedro Pascal and Bella Ramsey",
        "distractors": [
            "Troy Baker and Ashley Johnson",
            "Oscar Isaac and Cailee Spaeny",
            "Karl Urban and Dafne Keen"
        ],
        "d": 1
    },
    {
        "q": "Which critically acclaimed standalone Season 1 episode depicts the decades-long love story between survivalists Bill and Frank?",
        "correct": "Long, Long Time",
        "distractors": ["Left Behind", "Please Hold to My Hand", "Look for the Light"],
        "d": 1
    },
    {
        "q": "Which actor won the Primetime Emmy Award for Outstanding Guest Actor in a Drama Series for playing Bill in 'Long, Long Time'?",
        "correct": "Nick Offerman",
        "distractors": ["Murray Bartlett", "Lamar Johnson", "Keivonn Montreal Woodard"],
        "d": 2
    },
    {
        "q": "Who co-created and wrote HBO's 'The Last of Us' television adaptation alongside original game director Neil Druckmann?",
        "correct": "Craig Mazin (creator of 'Chernobyl')",
        "distractors": ["Damon Lindelof", "Noah Hawley", "Nic Pizzolatto"],
        "d": 2
    },
    {
        "q": "What 1970 Linda Ronstadt ballad serves as a recurring emotional anchor throughout 'The Last of Us' Season 1?",
        "correct": "Long Long Time",
        "distractors": ["Blue Bayou", "You're No Good", "Desperado"],
        "d": 2
    },

    # 49-58: Peacemaker, Station Eleven, Shōgun
    {
        "q": "In the Max DC series 'Peacemaker', what is the name of Peacemaker's devoted bald eagle pet and sidekick?",
        "correct": "Eagly",
        "distractors": ["Freedom", "Claw", "Patriot"],
        "d": 1
    },
    {
        "q": "What Norwegian glam metal band wrote and recorded 'Do Ya Wanna Taste It', the infectious theme song for 'Peacemaker'?",
        "correct": "Wig Wam",
        "distractors": ["The Darkness", "Steel Panther", "Lordi"],
        "d": 2
    },
    {
        "q": "Who wrote all eight episodes and directed the majority of 'Peacemaker' Season 1 before taking over DC Studios?",
        "correct": "James Gunn",
        "distractors": ["Zack Snyder", "David Ayer", "Peter Safran"],
        "d": 1
    },
    {
        "q": "In 'Station Eleven', what post-apocalyptic traveling troupe performs Shakespearean plays for survivor settlements?",
        "correct": "The Traveling Symphony",
        "distractors": ["The Bard Caravan", "The Great Lakes Players", "The Michigan Troubadours"],
        "d": 2
    },
    {
        "q": "What graphic novel within 'Station Eleven' provides spiritual meaning and prophecy to both Kirsten and the Prophet?",
        "correct": "Station Eleven",
        "distractors": ["Dr. Eleven's Orbit", "The Undersea", "Tales of the Starship"],
        "d": 2
    },
    {
        "q": "Which author wrote the 2014 post-apocalyptic pandemic novel 'Station Eleven' adapted into the Max limited series?",
        "correct": "Emily St. John Mandel",
        "distractors": ["Jeff VanderMeer", "Cormac McCarthy", "Margaret Atwood"],
        "d": 2
    },
    {
        "q": "At the 76th Primetime Emmy Awards in 2024, what all-time record did FX/Hulu/Disney+'s 'Shōgun' smash?",
        "correct": "Most Emmy wins by any show in a single television season in history with 18 wins",
        "distractors": [
            "Most Emmy wins by a comedy series with 12 wins",
            "Highest percentage of viewer votes for an international drama",
            "First series to sweep every technical and acting category without loss"
        ],
        "d": 1
    },
    {
        "q": "Which Japanese cinematic icon starred as Lord Yoshii Toranaga and won Outstanding Lead Actor in a Drama Series for 'Shōgun'?",
        "correct": "Hiroyuki Sanada",
        "distractors": ["Ken Watanabe", "Tadanobu Asano", "Takehiro Hira"],
        "d": 1
    },
    {
        "q": "Which actress made history at the 2024 Emmys as the first Japanese actress to win Lead Actress in a Drama Series for 'Shōgun'?",
        "correct": "Anna Sawai",
        "distractors": ["Rinko Kikuchi", "Moeka Hoshi", "Fumi Nikaido"],
        "d": 1
    },
    {
        "q": "Which English navigator washed ashore in Feudal Japan in 'Shōgun', portrayed by Cosmo Jarvis?",
        "correct": "John Blackthorne (Anjin)",
        "distractors": ["William Adams", "Richard Cocks", "Thomas Cavendish"],
        "d": 2
    },

    # 59-75: The Mandalorian & Andor (Disney+)
    {
        "q": "In Disney+'s flagship Star Wars series 'The Mandalorian', what is the canonical given name of 'The Child'?",
        "correct": "Grogu",
        "distractors": ["Yaddle", "Minch", "Goran"],
        "d": 1
    },
    {
        "q": "What sacred metal is used to forge the virtually indestructible armor of the Mandalorians?",
        "correct": "Beskar (Mandalorian iron)",
        "distractors": ["Cortosis", "Phrik", "Durasteel"],
        "d": 1
    },
    {
        "q": "What is the solemn creed recited by orthodox Mandalorians of the Children of the Watch?",
        "correct": "This is the Way",
        "distractors": ["Strength Through Beskar", "Honor in Battle", "For Mandalore"],
        "d": 1
    },
    {
        "q": "Which veteran actor and filmmaker portrayed Greef Karga, magistrate of Nevarro, and directed episodes of 'The Mandalorian' before his passing in 2024?",
        "correct": "Carl Weathers",
        "distractors": ["Giancarlo Esposito", "Forest Whitaker", "Laurence Fishburne"],
        "d": 1
    },
    {
        "q": "What ancient black-bladed lightsaber symbolizes the right to rule Mandalore?",
        "correct": "The Darksaber",
        "distractors": ["The Shadow Blade", "The Beskar Saber", "The Obsidian Saber"],
        "d": 1
    },
    {
        "q": "Who created and serves as head showrunner for 'The Mandalorian'?",
        "correct": "Jon Favreau",
        "distractors": ["J.J. Abrams", "Rian Johnson", "Gareth Edwards"],
        "d": 1
    },
    {
        "q": "What revolutionary virtual production technology, featuring wrap-around LED video walls, was pioneered for 'The Mandalorian'?",
        "correct": "StageCraft (The Volume)",
        "distractors": ["Holocube", "CineMatrix LED", "ChromaDome"],
        "d": 2
    },
    {
        "q": "In 'The Mandalorian' Season 2 finale, which iconic Star Wars hero makes a shocking de-aged cameo rescue aboard Moff Gideon's cruiser?",
        "correct": "Luke Skywalker",
        "distractors": ["Han Solo", "Obi-Wan Kenobi", "Mace Windu"],
        "d": 1
    },
    {
        "q": "In Disney+'s critically acclaimed spy drama 'Andor', which actor reprises his role as Cassian Andor from 'Rogue One'?",
        "correct": "Diego Luna",
        "distractors": ["Pedro Pascal", "Oscar Isaac", "Tenoch Huerta"],
        "d": 1
    },
    {
        "q": "Who created, wrote, and served as showrunner for 'Andor', bringing a grounded political thriller tone to Star Wars?",
        "correct": "Tony Gilroy",
        "distractors": ["Dave Filoni", "Leslye Headland", "Jon Favreau"],
        "d": 2
    },
    {
        "q": "What impassioned three-word rally chant does floor manager Kino Loy (Andy Serkis) broadcast during the Narkina 5 prison breakout?",
        "correct": "One way out!",
        "distractors": ["Swim to shore!", "Fight the Empire!", "Break the floor!"],
        "d": 2
    },
    {
        "q": "What heartbreaking revelation does Kino Loy confess to Cassian Andor at the prison exit edge overlooking the ocean?",
        "correct": "I can't swim",
        "distractors": ["I'm going back", "I was never imprisoned", "My family is gone"],
        "d": 2
    },
    {
        "q": "What planetary celestial event provides the cover for Cassian and the rebel squad's payroll heist in 'Andor'?",
        "correct": "The Eye of Aldhani",
        "distractors": ["The Eclipse of Coruscant", "The Aurora of Ferrix", "The Comets of Jedha"],
        "d": 2
    },
    {
        "q": "Which Swedish actor portrays Luthen Rael, the antique dealer secretly running an anti-Imperial rebel network in 'Andor'?",
        "correct": "Stellan Skarsgård",
        "distractors": ["Mads Mikkelsen", "Peter Stormare", "Fares Fares"],
        "d": 2
    },
    {
        "q": "What haunting funeral speech is delivered via holographic projection from a brick on Ferrix in the 'Andor' Season 1 finale?",
        "correct": "Maarva Andor's speech inciting the crowd to 'Fight the Empire!'",
        "distractors": [
            "Bix Caleen's call to arms",
            "Brasso's memorial poem",
            "Luthen Rael's declaration of war"
        ],
        "d": 2
    },
    {
        "q": "What is the name of the Imperial Security Bureau supervisor whose ruthless investigation drives the hunt for Cassian in 'Andor'?",
        "correct": "Dedra Meero (Denise Gough)",
        "distractors": ["Bix Caleen", "Vel Sartha", "Cinta Kaz"],
        "d": 3
    },
    {
        "q": "What is the title of Luthen Rael's celebrated monologue in Episode 10 about sacrificing his own soul for the rebellion?",
        "correct": "What do I sacrifice? Everything!",
        "distractors": ["A Sunrise I Shall Never See", "The Dark Path of Duty", "Architect of Shadows"],
        "d": 3
    },

    # 76-88: WandaVision & Loki (Disney+)
    {
        "q": "What was the very first Marvel Cinematic Universe streaming television series released on Disney+ in January 2021?",
        "correct": "WandaVision",
        "distractors": ["The Falcon and the Winter Soldier", "Loki", "Hawkeye"],
        "d": 1
    },
    {
        "q": "In 'WandaVision', what New Jersey suburban town is ensnared inside Wanda Maximoff's reality-altering 'Hex'?",
        "correct": "Westview",
        "distractors": ["Eastwick", "Fairview", "Riverdale"],
        "d": 1
    },
    {
        "q": "What Emmy-winning viral earworm song reveals that nosy neighbor Agnes is actually ancient witch Agatha Harkness?",
        "correct": "Agatha All Along",
        "distractors": ["It Was Agatha", "The Witch of Westview", "Spells and Hexes"],
        "d": 1
    },
    {
        "q": "Which classic 1950s sitcom directly inspired the filming style, live studio audience, and look of the 'WandaVision' pilot episode?",
        "correct": "The Dick Van Dyke Show",
        "distractors": ["I Love Lucy", "The Honeymooners", "Father Knows Best"],
        "d": 2
    },
    {
        "q": "Who created and served as head writer for 'WandaVision'?",
        "correct": "Jac Schaeffer",
        "distractors": ["Michael Waldron", "Kate Herron", "Malcolm Spellman"],
        "d": 2
    },
    {
        "q": "What famous philosophical line about sorrow does Vision (Paul Bettany) say to Wanda in a quiet flashback?",
        "correct": "What is grief, if not love persevering?",
        "distractors": [
            "Grief is the memory of joy fading away",
            "Love remains when the physical form perishes",
            "To love someone is to accept endless sorrow"
        ],
        "d": 2
    },
    {
        "q": "Which actor, who played Quicksilver in Fox's 'X-Men' films, made a meta-casting appearance as 'Fietro' in 'WandaVision'?",
        "correct": "Evan Peters",
        "distractors": ["Aaron Taylor-Johnson", "Nicholas Hoult", "Taron Egerton"],
        "d": 2
    },
    {
        "q": "In Disney+'s 'Loki', what mysterious bureaucratic institution exists outside time and space to prune rogue timelines?",
        "correct": "The Time Variance Authority (TVA)",
        "distractors": ["The Chrono Protection Agency", "The Temporal Oversight Bureau", "The Multiverse Enforcers"],
        "d": 1
    },
    {
        "q": "Which actor portrays Mobius M. Mobius, the jet-ski-obsessed TVA agent who partners with Loki?",
        "correct": "Owen Wilson",
        "distractors": ["Luke Wilson", "Matthew McConaughey", "Woody Harrelson"],
        "d": 1
    },
    {
        "q": "What female variant of Loki is played by Sophia Di Martino in 'Loki'?",
        "correct": "Sylvie",
        "distractors": ["Sigyn", "Angerboda", "Hela"],
        "d": 2
    },
    {
        "q": "In the Season 1 finale of 'Loki', which mysterious entity living at the Citadel at the End of Time is introduced?",
        "correct": "He Who Remains",
        "distractors": ["Kang the Conqueror", "The Living Tribunal", "Immortus"],
        "d": 2
    },
    {
        "q": "In the Season 2 finale of 'Loki', what cosmic role does Loki take upon himself to preserve the dying multiverse?",
        "correct": "He weaves the dying timelines with his magic and sits upon a throne holding the temporal tree (Yggdrasil)",
        "distractors": [
            "He assumes the mantle of permanent Director of the TVA",
            "He merges with the Temporal Loom to power time forever",
            "He becomes the Supreme Sovereign of Asgard across all timelines"
        ],
        "d": 2
    },
    {
        "q": "What is the name of the sentient cartoon clock mascot of the TVA voiced by Tara Strong in 'Loki'?",
        "correct": "Miss Minutes",
        "distractors": ["Clocky", "Timey", "Lady Hour"],
        "d": 2
    },

    # 89-100: Max & Disney+ Deep Cuts
    {
        "q": "In 'Succession' Season 4, what is the title of the disastrous living-quarters project for seniors that Kendall hypes at Investor Day?",
        "correct": "Living+",
        "distractors": ["Waystar Haven", "Roy Life", "Golden Years"],
        "d": 3
    },
    {
        "q": "What is the name of Roman Roy's ill-fated management-training mentor at Waystar who nicknamed him 'Roman the Showman'?",
        "correct": "Brian (the eccentric intellectual trainee)",
        "distractors": ["Gerri Kellman", "Karl Muller", "Frank Vernon"],
        "d": 3
    },
    {
        "q": "In 'The White Lotus' Season 2, what luxury hotel in Taormina, Sicily served as the real-world filming location for the resort?",
        "correct": "San Domenico Palace, Taormina, A Four Seasons Hotel",
        "distractors": [
            "Villa d'Este, Lake Como",
            "Belmond Grand Hotel Timeo",
            "Hotel Cipriani, Venice"
        ],
        "d": 3
    },
    {
        "q": "In 'Hacks' Season 1, what item does Ava accidentally lose at Deborah's palatial mansion that Deborah forces her to recover from the trash?",
        "correct": "An antique pepper mill",
        "distractors": ["A diamond tennis bracelet", "A vintage silver flask", "A handwritten letter from Joan Rivers"],
        "d": 3
    },
    {
        "q": "In 'House of the Dragon' Season 1, what rare illness slowly disfigures and rots King Viserys over several decades?",
        "correct": "A form of necrotizing leprosy",
        "distractors": ["Greyscale", "The Shivers", "Targaryen blood rot"],
        "d": 3
    },
    {
        "q": "In 'The Last of Us', what is the name of the revolutionary militia movement in Kansas City led by Kathleen Coghlan (Melanie Lynskey)?",
        "correct": "The People's Free Army (overthrow of FEDRA)",
        "distractors": ["The Fireflies Chapter 4", "The Hunters of KC", "The Resistance Movement"],
        "d": 3
    },
    {
        "q": "In Disney+'s 'Andor', what type of precious mineral are the prisoners forced to construct machinery components for on Narkina 5?",
        "correct": "Components later revealed in the post-credits scene to be part of the Death Star superlaser",
        "distractors": [
            "Hyperdrive motivators for Imperial Star Destroyers",
            "Targeting computers for TIE Fighters",
            "Shield generators for the second Death Star"
        ],
        "d": 3
    },
    {
        "q": "In 'The Mandalorian' Season 1, what IG-series assassin droid voiced by Taika Waititi is reprogrammed by Kuiil to protect Grogu?",
        "correct": "IG-11",
        "distractors": ["IG-88", "IG-90", "IG-55"],
        "d": 2
    },
    {
        "q": "Which Emmy-winning cinematographer served as a primary director of photography on 'Succession', establishing its signature cinema-verité zoom lens look?",
        "correct": "Andrij Parekh",
        "distractors": ["Roger Deakins", "Emmanuel Lubezki", "Hoyte van Hoytema"],
        "d": 3
    },
    {
        "q": "In 'Loki' Season 2, which Oscar-winning actor joined the cast as O.B. (Ouroboros), the quirky head of the TVA's Repairs and Advancement Department?",
        "correct": "Ke Huy Quan",
        "distractors": ["Daniel Wu", "Randall Park", "Steven Yeun"],
        "d": 2
    },
    {
        "q": "In 'Peacemaker', what alien parasitic species is burrowing inside human bodies in Project Butterfly?",
        "correct": "The Butterflies",
        "distractors": ["The Starro Spores", "The Dominators", "The Reach Larvae"],
        "d": 3
    },
    {
        "q": "What is the name of the Ferrix marching band's musical instrument made of scrap metal and played during funerals in 'Andor'?",
        "correct": "The Ferrix anvil (rung by the time grappler)",
        "distractors": ["The beskar bugle", "The scrap horn", "The plasma chime"],
        "d": 3
    }
]

if __name__ == "__main__":
    build_batch(BATCH_3, "tools/staging/streaming_tv_batch3.json", batch_num=3)
