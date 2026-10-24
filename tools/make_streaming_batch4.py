#!/usr/bin/env python3
"""
Generate Batch 4 of Streaming TV Shows trivia (100 questions):
Metatextual Focus: Emmy records & sweeps, platform launches & streaming wars,
binge vs weekly release models, Nielsen streaming rankings & metrics,
showrunners, auteurs, and writing credits.
Target: ~20 d1, ~32 d2, ~48 d3.
"""

from streaming_tv_batch_builder import build_batch

BATCH_4 = [
    # 1-25: Emmy Records, Golden Globes, and Industry Awards Sweeps
    {
        "q": "What all-time Primetime Emmy record did FX/Hulu's 'Shōgun' set in 2024 for the most wins by any series in a single television season?",
        "correct": "18 Emmys",
        "distractors": ["14 Emmys", "16 Emmys", "20 Emmys"],
        "d": 1
    },
    {
        "q": "What was the first television show produced by a streaming service to win the Primetime Emmy Award for Outstanding Drama Series?",
        "correct": "The Handmaid's Tale (Hulu, 2017)",
        "distractors": [
            "House of Cards (Netflix, 2014)",
            "The Crown (Netflix, 2021)",
            "Stranger Things (Netflix, 2017)"
        ],
        "d": 2
    },
    {
        "q": "What was the first television show produced by a streaming service to win the Primetime Emmy Award for Outstanding Comedy Series?",
        "correct": "The Marvelous Mrs. Maisel (Amazon Prime Video, 2018)",
        "distractors": [
            "Transparent (Amazon Prime Video, 2015)",
            "Fleabag (Amazon Prime Video, 2019)",
            "Ted Lasso (Apple TV+, 2021)"
        ],
        "d": 2
    },
    {
        "q": "At the 76th Primetime Emmy Awards in 2024, what comedy record did 'The Bear' set for most Emmy wins in a single season for a comedy?",
        "correct": "11 Emmys",
        "distractors": ["8 Emmys", "9 Emmys", "13 Emmys"],
        "d": 2
    },
    {
        "q": "Which show held the previous record of 10 Emmy wins in a single season for a comedy series, set in 2021, before 'The Bear' broke it?",
        "correct": "Schitt's Creek",
        "distractors": ["Ted Lasso", "Modern Family", "30 Rock"],
        "d": 3
    },
    {
        "q": "How many times did British creator Jesse Armstrong win the Primetime Emmy Award for Outstanding Writing for a Drama Series for 'Succession'?",
        "correct": "Four times (one for each season)",
        "distractors": ["Two times", "Three times", "Five times"],
        "d": 2
    },
    {
        "q": "At the 74th Primetime Emmy Awards in 2022, who became the first Asian actor in history to win Outstanding Lead Actor in a Drama Series?",
        "correct": "Lee Jung-jae (Squid Game)",
        "distractors": ["Hiroyuki Sanada (Shōgun)", "Steven Yeun (Beef)", "John Cho (Cowboy Bebop)"],
        "d": 1
    },
    {
        "q": "Which actress won three Primetime Emmy Awards for Outstanding Supporting Actress in a Drama Series playing Ruth Langmore in 'Ozark'?",
        "correct": "Julia Garner",
        "distractors": ["Sarah Snook", "Laura Linney", "Gillian Anderson"],
        "d": 1
    },
    {
        "q": "At the 73rd Primetime Emmy Awards in 2021, which series achieved an unprecedented sweep of all seven major Drama categories?",
        "correct": "The Crown (Season 4)",
        "distractors": ["Succession (Season 2)", "Game of Thrones (Season 8)", "Better Call Saul (Season 5)"],
        "d": 2
    },
    {
        "q": "How many total Emmy nominations did AMC/Netflix's 'Better Call Saul' receive across its six seasons without winning a single Emmy?",
        "correct": "53 nominations (0 wins)",
        "distractors": ["32 nominations (0 wins)", "41 nominations (0 wins)", "65 nominations (0 wins)"],
        "d": 2
    },
    {
        "q": "Which actor won the Emmy for Outstanding Supporting Actor in a Drama Series in both 2020 and 2022 for playing Tom Wambsgans in 'Succession'?",
        "correct": "Matthew Macfadyen",
        "distractors": ["Kieran Culkin", "Nicholas Braun", "Alan Ruck"],
        "d": 1
    },
    {
        "q": "Who won the Primetime Emmy for Outstanding Directing for a Comedy Series in 2023 and 2024 for 'The Bear'?",
        "correct": "Christopher Storer",
        "distractors": ["Bill Hader", "Lucia Aniello", "Taika Waititi"],
        "d": 3
    },
    {
        "q": "In 2024, which Japanese star became the first Japanese actress to win an Emmy for Lead Actress in a Drama Series?",
        "correct": "Anna Sawai (Shōgun)",
        "distractors": ["Rinko Kikuchi", "Tao Okamoto", "Moeka Hoshi"],
        "d": 1
    },
    {
        "q": "Which limited series swept eight Emmy awards in 2024, including wins for stars Steven Yeun and Ali Wong?",
        "correct": "Beef",
        "distractors": ["Fargo", "Lessons in Chemistry", "Baby Reindeer"],
        "d": 1
    },
    {
        "q": "Who became the first person in Emmy history to win Directing, Writing, and Lead Actress for a Comedy Series in the same night in 2019?",
        "correct": "Phoebe Waller-Bridge (Fleabag)",
        "distractors": ["Amy Sherman-Palladino", "Tina Fey", "Issa Rae"],
        "d": 2
    },
    {
        "q": "In 2018, Amy Sherman-Palladino made Emmy history by becoming the first woman to win which two awards in the same ceremony?",
        "correct": "Outstanding Writing and Outstanding Directing for a Comedy Series ('The Marvelous Mrs. Maisel')",
        "distractors": [
            "Outstanding Comedy Series and Lead Actress in a Comedy Series",
            "Outstanding Writing for a Drama and Comedy Series",
            "Outstanding Directing and Outstanding Editing"
        ],
        "d": 3
    },
    {
        "q": "What record did 'Ted Lasso' set in 2021 with its 20 Emmy nominations for Season 1?",
        "correct": "Most Emmy nominations received by a freshman comedy series in history",
        "distractors": [
            "Most nominations for any comedy series in history",
            "Most technical nominations for a British-filmed series",
            "Most nominations for an Apple original program"
        ],
        "d": 2
    },
    {
        "q": "Which actor won back-to-back Primetime Emmys for Outstanding Lead Actor in a Comedy Series in 2021 and 2022 for 'Ted Lasso'?",
        "correct": "Jason Sudeikis",
        "distractors": ["Bill Hader", "Eugene Levy", "Donald Glover"],
        "d": 1
    },
    {
        "q": "In 2024, Richard Gadd won three Emmys for writing, producing, and starring in which breakthrough Netflix limited series?",
        "correct": "Baby Reindeer",
        "distractors": ["Ripley", "Bodkin", "The Gentlemen"],
        "d": 1
    },
    {
        "q": "Which actress won Outstanding Supporting Actress in a Limited Series in 2024 for portraying Martha Scott in 'Baby Reindeer'?",
        "correct": "Jessica Gunning",
        "distractors": ["Nava Mau", "Dakota Fanning", "Aja Naomi King"],
        "d": 2
    },
    {
        "q": "How many total Primetime Emmy nominations did HBO's 'Game of Thrones' receive across its run, setting the all-time drama record?",
        "correct": "160 nominations",
        "distractors": ["112 nominations", "135 nominations", "190 nominations"],
        "d": 3
    },
    {
        "q": "Which star of 'The White Lotus' won the Emmy for Supporting Actress in a Limited Series in 2022 and Supporting Actress in a Drama Series in 2023?",
        "correct": "Jennifer Coolidge",
        "distractors": ["Connie Britton", "Aubrey Plaza", "Sydney Sweeney"],
        "d": 1
    },
    {
        "q": "In 2024, which Max comedy scored a major upset by defeating 'The Bear' for the Outstanding Comedy Series Emmy?",
        "correct": "Hacks",
        "distractors": ["Abbott Elementary", "Only Murders in the Building", "Curb Your Enthusiasm"],
        "d": 1
    },
    {
        "q": "Which veteran actor won an Emmy for Outstanding Supporting Actor in a Drama Series for 'The Morning Show' in 2020 and 2024?",
        "correct": "Billy Crudup",
        "distractors": ["Mark Duplass", "Jon Hamm", "Jack Lowden"],
        "d": 2
    },
    {
        "q": "At the 70th Primetime Emmy Awards, what historic milestone did Netflix achieve regarding Emmy nominations?",
        "correct": "It ended HBO's 17-year streak by earning the most Emmy nominations of any network/platform (112 nominations)",
        "distractors": [
            "It won every single acting category across comedy and drama",
            "It became the first platform to win 50 Emmys in one evening",
            "It swept all four major series categories in the same year"
        ],
        "d": 3
    },

    # 26-50: Platform Launch Dates, Platform Wars, and Corporate History
    {
        "q": "In what year did Netflix officially launch its revolutionary video-on-demand streaming service alongside its legacy DVD-by-mail service?",
        "correct": "2007",
        "distractors": ["2005", "2009", "2011"],
        "d": 2
    },
    {
        "q": "What political drama starring Kevin Spacey and Robin Wright debuted in February 2013 as Netflix's first major original streaming series?",
        "correct": "House of Cards",
        "distractors": ["Orange Is the New Black", "Hemlock Grove", "Lilyhammer"],
        "d": 1
    },
    {
        "q": "What was the Norwegian-American comedy series starring Steven Van Zandt that technically premiered in 2012 as Netflix's first exclusive co-production?",
        "correct": "Lilyhammer",
        "distractors": ["Norsemen", "Ragnarok", "Occupied"],
        "d": 3
    },
    {
        "q": "On what date did Disney+ officially launch in the United States, signing up over 10 million subscribers on its very first day?",
        "correct": "November 12, 2019",
        "distractors": ["November 1, 2019", "December 15, 2019", "January 1, 2020"],
        "d": 2
    },
    {
        "q": "On what date did Apple TV+ officially launch worldwide with a lineup featuring 'The Morning Show', 'See', and 'For All Mankind'?",
        "correct": "November 1, 2019",
        "distractors": ["October 15, 2019", "November 12, 2019", "December 1, 2019"],
        "d": 2
    },
    {
        "q": "When WarnerMedia launched its flagship streaming platform HBO Max in May 2020, what price point did it controversially debut at?",
        "correct": "$14.99 per month",
        "distractors": ["$9.99 per month", "$11.99 per month", "$19.99 per month"],
        "d": 3
    },
    {
        "q": "In May 2023, Warner Bros. Discovery officially rebranded its flagship streaming service HBO Max to what simplified name?",
        "correct": "Max",
        "distractors": ["Warner Max", "Discovery+", "WB Stream"],
        "d": 1
    },
    {
        "q": "Which major broadcast and entertainment conglomerate initially launched Hulu in 2007 as a joint venture between NBCUniversal and News Corporation?",
        "correct": "NBCUniversal and News Corporation (later joined by Disney)",
        "distractors": [
            "Sony Pictures and Paramount",
            "CBS Corporation and Time Warner",
            "Viacom and Metro-Goldwyn-Mayer"
        ],
        "d": 3
    },
    {
        "q": "In December 2023, The Walt Disney Company agreed to pay NBCUniversal's parent Comcast at least how much to acquire full remaining ownership of Hulu?",
        "correct": "$8.6 billion",
        "distractors": ["$4.2 billion", "$12.5 billion", "$15.0 billion"],
        "d": 3
    },
    {
        "q": "In March 2021, ViacomCBS rebranded its legacy subscription streaming service CBS All Access to what new name?",
        "correct": "Paramount+",
        "distractors": ["Showtime Anytime", "CBS Stream", "Pluto Premium"],
        "d": 2
    },
    {
        "q": "Which NBCUniversal streaming service launched in July 2020, named after the iconic feathered logo of NBC?",
        "correct": "Peacock",
        "distractors": ["Pelican", "Eagle", "Falcon"],
        "d": 1
    },
    {
        "q": "What short-form mobile-only streaming platform founded by Jeffrey Katzenberg raised $1.75 billion and shut down just six months after launching in 2020?",
        "correct": "Quibi",
        "distractors": ["Vessel", "Seeso", "Fullscreen"],
        "d": 2
    },
    {
        "q": "In what year did Netflix roll out its algorithmic 'Skip Intro' button, which users now click billions of times per year?",
        "correct": "2017",
        "distractors": ["2014", "2015", "2019"],
        "d": 3
    },
    {
        "q": "In 2023, Netflix implemented a controversial global crackdown on what widespread consumer behavior, resulting in an unexpected surge of new subscribers?",
        "correct": "Password/account sharing across multiple households",
        "distractors": [
            "Use of Virtual Private Networks (VPNs)",
            "Offline downloading of 4K content",
            "Third-party profile picture customizations"
        ],
        "d": 2
    },
    {
        "q": "In November 2022, Netflix launched its first-ever cheaper subscription tier supported by what feature it had previously resisted for decades?",
        "correct": "Commercial advertisements ('Basic with Ads')",
        "distractors": [
            "Daily viewing time limits",
            "480p standard-definition restrictions",
            "Mandatory two-year annual contracts"
        ],
        "d": 1
    },
    {
        "q": "Which major streaming platform pioneered the introduction of 'X-Ray', an interactive feature powered by IMDb that displays cast and trivia in real time?",
        "correct": "Amazon Prime Video",
        "distractors": ["Netflix", "Apple TV+", "Disney+"],
        "d": 2
    },
    {
        "q": "In what year did Amazon officially acquire the legendary Hollywood movie studio Metro-Goldwyn-Mayer (MGM) for $8.5 billion?",
        "correct": "2021 (closing in 2022)",
        "distractors": ["2018", "2019", "2023"],
        "d": 3
    },
    {
        "q": "What landmark 2022 film won the Academy Award for Best Picture, making Apple TV+ the first streaming service in history to win Hollywood's top Oscar?",
        "correct": "CODA",
        "distractors": ["Roma", "The Power of the Dog", "Killers of the Flower Moon"],
        "d": 2
    },
    {
        "q": "In 2017, which superstar television creator departed ABC to sign a historic five-year deal with Netflix valued at an estimated $150 million?",
        "correct": "Shonda Rhimes",
        "distractors": ["Ryan Murphy", "Kenya Barris", "Greg Berlanti"],
        "d": 2
    },
    {
        "q": "In 2018, which prolific producer behind 'American Horror Story' and 'Glee' signed a record-breaking five-year Netflix development deal valued at up to $300 million?",
        "correct": "Ryan Murphy",
        "distractors": ["Dick Wolf", "Chuck Lorre", "Carlton Cuse"],
        "d": 2
    },
    {
        "q": "Which streaming platform debuted the Star tile internationally, offering Hulu and FX mature content to Disney+ subscribers outside the United States?",
        "correct": "Disney+",
        "distractors": ["Paramount+", "Amazon Prime Video", "Max"],
        "d": 3
    },
    {
        "q": "What was the name of HBO's original standalone direct-to-consumer streaming service that launched in 2015 prior to HBO Max?",
        "correct": "HBO NOW",
        "distractors": ["HBO GO", "HBO Direct", "HBO Plus"],
        "d": 3
    },
    {
        "q": "In 2024, which mega-streamer acquired exclusive worldwide rights to WWE's flagship weekly wrestling program 'Raw' in a 10-year, $5 billion deal?",
        "correct": "Netflix",
        "distractors": ["Amazon Prime Video", "Peacock", "Apple TV+"],
        "d": 2
    },
    {
        "q": "Which streaming platform secured exclusive rights to the NFL's 'Thursday Night Football' beginning in 2022 in an 11-year deal worth $1 billion per season?",
        "correct": "Amazon Prime Video",
        "distractors": ["Netflix", "Apple TV+", "Peacock"],
        "d": 2
    },
    {
        "q": "In 2022, Apple signed a historic 10-year, $2.5 billion worldwide broadcast partnership with which North American professional sports league?",
        "correct": "Major League Soccer (MLS)",
        "distractors": ["Major League Baseball (MLB)", "National Hockey League (NHL)", "WNBA"],
        "d": 2
    },

    # 51-75: Binge vs. Weekly Strategies, Viewership Records & Nielsen Metrics
    {
        "q": "What term describes the release strategy popularized by Netflix where all episodes of a television season are made available simultaneously?",
        "correct": "The binge-drop model (or batch drop)",
        "distractors": ["The linear rollout", "The episodic flow", "The syndicated trickle"],
        "d": 1
    },
    {
        "q": "How did Netflix release Season 4 of 'Stranger Things' in 2022 to sustain subscriber engagement and Emmy buzz over the summer?",
        "correct": "Splitting the season into two volumes released one month apart (May and July 2022)",
        "distractors": [
            "Releasing one episode every Friday over nine consecutive weeks",
            "Dropping three episodes every weekend for three weeks",
            "Streaming the episodes live as a continuous 24-hour marathon"
        ],
        "d": 2
    },
    {
        "q": "Which streaming service standardizes a hybrid rollout model: dropping the first three episodes on premiere day, followed by weekly installments?",
        "correct": "Amazon Prime Video (and Apple TV+ for many series)",
        "distractors": ["Netflix", "YouTube Premium", "Pluto TV"],
        "d": 2
    },
    {
        "q": "According to Nielsen streaming data, which legal procedural originally broadcast on USA Network shattered all-time records in summer 2023 with 57.7 billion minutes viewed?",
        "correct": "Suits",
        "distractors": ["The Good Wife", "White Collar", "Boston Legal"],
        "d": 1
    },
    {
        "q": "In what year did Nielsen officially launch its SVOD (Subscription Video on Demand) Content Ratings to track streaming minutes viewed on television sets?",
        "correct": "2020",
        "distractors": ["2016", "2018", "2022"],
        "d": 3
    },
    {
        "q": "What primary metric did Netflix use for its public Top 10 lists beginning in 2021 before shifting to 'Views' (Hours Viewed divided by Runtime) in 2023?",
        "correct": "Total hours viewed in the first 28 days",
        "distractors": [
            "Total accounts that watched at least 2 minutes",
            "Unique household reach over 7 days",
            "Average completion rate per season"
        ],
        "d": 3
    },
    {
        "q": "According to Netflix's historical data, which non-English language series holds the all-time record as the platform's most-watched television season ever?",
        "correct": "Squid Game (Season 1) with over 2.2 billion hours viewed",
        "distractors": [
            "Money Heist (Part 4)",
            "Lupin (Part 1)",
            "Dark (Season 3)"
        ],
        "d": 2
    },
    {
        "q": "Which Tim Burton-directed supernatural mystery became Netflix's most popular English-language series of all time in 2022, surpassing 'Stranger Things 4' in total views?",
        "correct": "Wednesday",
        "distractors": ["The Queen's Gambit", "Dahmer – Monster", "Bridgerton Season 1"],
        "d": 1
    },
    {
        "q": "In 2022, which controversial Ryan Murphy limited series starring Evan Peters crossed 1 billion hours viewed within 60 days on Netflix?",
        "correct": "Dahmer – Monster: The Jeffrey Dahmer Story",
        "distractors": ["The Watcher", "Ratched", "Hollywood"],
        "d": 2
    },
    {
        "q": "What viral social media trend helped propel Netflix's 'Wednesday' to global viewership records, soundtracked to Lady Gaga's 'Bloody Mary'?",
        "correct": "Recreating Jenna Ortega's idiosyncratic Rave'N dance choreography on TikTok",
        "distractors": [
            "A cello tutorial playing The Rolling Stones' 'Paint It Black'",
            "Baking black gothic pastries with Thing hands",
            "A high-school fencing duel challenge"
        ],
        "d": 1
    },
    {
        "q": "Which HBO Max / Max premiere drew 10 million viewers across linear TV and streaming on its premiere night in August 2022, the largest debut in HBO history?",
        "correct": "House of the Dragon",
        "distractors": ["The Last of Us", "Euphoria Season 2", "Succession Season 4"],
        "d": 2
    },
    {
        "q": "According to Amazon, how many global viewers tuned into the premiere of 'The Lord of the Rings: The Rings of Power' in its first 24 hours?",
        "correct": "25 million viewers",
        "distractors": ["10 million viewers", "45 million viewers", "60 million viewers"],
        "d": 3
    },
    {
        "q": "What video game adaptation drew 8.2 million viewers for its Season 1 finale on HBO/Max in March 2023, competing directly against the Oscars telecast?",
        "correct": "The Last of Us",
        "distractors": ["Fallout", "Halo", "Twisted Metal"],
        "d": 2
    },
    {
        "q": "Which animated video game adaptation produced by Riot Games and Fortiche on Netflix won the Emmy for Outstanding Animated Program in 2022?",
        "correct": "Arcane (League of Legends)",
        "distractors": ["Castlevania", "Cyberpunk: Edgerunners", "DOTA: Dragon's Blood"],
        "d": 2
    },
    {
        "q": "In 2020, what bizarre true-crime docuseries about private zoo owner Joe Exotic became an unprecedented cultural sensation during the early COVID-19 lockdowns?",
        "correct": "Tiger King: Murder, Mayhem and Madness",
        "distractors": ["Making a Murderer", "The Jinx", "Don't F**k with Cats"],
        "d": 1
    },
    {
        "q": "According to Nielsen, how many billion minutes of 'The Office' were streamed on Netflix in the United States in 2020 before it moved exclusively to Peacock?",
        "correct": "57.1 billion minutes",
        "distractors": ["25.4 billion minutes", "38.7 billion minutes", "72.0 billion minutes"],
        "d": 3
    },
    {
        "q": "In 2019, how much did NBCUniversal reportedly pay to license the exclusive domestic streaming rights of 'The Office' for five years on Peacock?",
        "correct": "$500 million ($100 million per year)",
        "distractors": ["$250 million", "$425 million", "$750 million"],
        "d": 3
    },
    {
        "q": "How much did WarnerMedia reportedly pay in 2019 to secure the exclusive five-year domestic streaming rights of 'Friends' for HBO Max?",
        "correct": "$425 million ($85 million per year)",
        "distractors": ["$200 million", "$300 million", "$600 million"],
        "d": 3
    },
    {
        "q": "How much did Netflix pay in 2019 to secure the worldwide global streaming rights to 'Seinfeld' starting in 2021?",
        "correct": "Over $500 million",
        "distractors": ["$200 million", "$350 million", "$800 million"],
        "d": 3
    },
    {
        "q": "What was the reported completion rate among domestic viewers for the first season of Amazon's 'The Rings of Power', according to a 2023 Hollywood Reporter investigative report?",
        "correct": "37% of US domestic viewers completed the entire season",
        "distractors": ["65% of US viewers", "19% of US viewers", "82% of US viewers"],
        "d": 3
    },
    {
        "q": "In 2021, which animated superhero series on Prime Video saw its viewership quadruple between its premiere and finale thanks to word-of-mouth and memes?",
        "correct": "Invincible",
        "distractors": ["The Boys Presents: Diabolical", "The Legend of Vox Machina", "Undone"],
        "d": 2
    },
    {
        "q": "What chess board retail surge occurred globally in late 2020 following the premiere of 'The Queen's Gambit' on Netflix?",
        "correct": "Chess set sales surged by over 80% to 1,000% across major retailers like eBay and Goliath Games",
        "distractors": [
            "Chess set sales declined due to online mobile apps",
            "Only wooden antique boards saw a modest 10% increase",
            "Manufacturers faced a total wood shortage halting all production"
        ],
        "d": 2
    },
    {
        "q": "Which historical romance author saw four of her novels on the New York Times bestseller list simultaneously after 'Bridgerton' debuted?",
        "correct": "Julia Quinn",
        "distractors": ["Diana Gabaldon", "Colleen Hoover", "Emily Henry"],
        "d": 2
    },
    {
        "q": "What Spanish heist drama became an unexpected global phenomenon after Netflix acquired global streaming rights in late 2017 and recut its episodes?",
        "correct": "Money Heist (La Casa de Papel)",
        "distractors": ["Elite", "Cable Girls", "Vis a Vis (Locked Up)"],
        "d": 1
    },
    {
        "q": "What German sci-fi thriller about time travel and family lineages ran for three critically acclaimed seasons on Netflix from 2017 to 2020?",
        "correct": "Dark",
        "distractors": ["1899", "Biohackers", "Babylon Berlin"],
        "d": 2
    },

    # 76-100: Showrunners, Creators, Directors & Writers
    {
        "q": "Who are the twin brother creators, writers, and directors of Netflix's 'Stranger Things'?",
        "correct": "Matt and Ross Duffer (The Duffer Brothers)",
        "distractors": ["Anthony and Joe Russo", "Joel and Ethan Coen", "Jonathan and Christopher Nolan"],
        "d": 1
    },
    {
        "q": "Which showrunner created 'The Crown' after having previously written the film 'The Queen' (2006) and the stage play 'The Audience' (2013)?",
        "correct": "Peter Morgan",
        "distractors": ["Tom Stoppard", "David Hare", "Julian Fellowes"],
        "d": 2
    },
    {
        "q": "Which creator and showrunner wrote every single episode of 'The White Lotus' Seasons 1 and 2, also directing all episodes himself?",
        "correct": "Mike White",
        "distractors": ["Damon Lindelof", "Noah Hawley", "David E. Kelley"],
        "d": 2
    },
    {
        "q": "Which former showrunner of 'Gilmore Girls' and 'Bunheads' created the award-winning Amazon series 'The Marvelous Mrs. Maisel'?",
        "correct": "Amy Sherman-Palladino",
        "distractors": ["Marta Kauffman", "Liz Meriwether", "Mindy Kaling"],
        "d": 1
    },
    {
        "q": "Which screenwriter wrote the Oscar-nominated screenplay for 'The Social Network' before creating the Netflix limited film/theatrical projects and Apple/HBO series?",
        "correct": "Aaron Sorkin",
        "distractors": ["David Fincher", "Steve Zaillian", "Tony Gilroy"],
        "d": 2
    },
    {
        "q": "Who wrote and directed the acclaimed HBO limited series 'Chernobyl' before co-creating and adapting 'The Last of Us'?",
        "correct": "Craig Mazin",
        "distractors": ["Johan Renck", "Scott Frank", "Cary Joji Fukunaga"],
        "d": 2
    },
    {
        "q": "Which filmmaker wrote and directed all seven episodes of Netflix's hit 2020 limited series 'The Queen's Gambit'?",
        "correct": "Scott Frank",
        "distractors": ["David Fincher", "Steven Soderbergh", "Edgar Wright"],
        "d": 3
    },
    {
        "q": "Which Oscar-nominated director served as executive producer and directed seven episodes across Seasons 1 and 2 of Netflix's 'Mindhunter'?",
        "correct": "David Fincher",
        "distractors": ["Denis Villeneuve", "Christopher Nolan", "Michael Mann"],
        "d": 2
    },
    {
        "q": "Who created the Netflix animated dark comedy 'BoJack Horseman', exploring depression and existential dread in Hollywoo?",
        "correct": "Raphael Bob-Waksberg",
        "distractors": ["Pendleton Ward", "Dan Harmon", "Alex Hirsch"],
        "d": 2
    },
    {
        "q": "Which comic book writer created the gritty graphic novel series 'The Boys' published by WildStorm and Dynamite Entertainment?",
        "correct": "Garth Ennis",
        "distractors": ["Warren Ellis", "Grant Morrison", "Mark Millar"],
        "d": 3
    },
    {
        "q": "Which showrunners served as creators and executive producers of Netflix's '3 Body Problem' after having run HBO's 'Game of Thrones'?",
        "correct": "David Benioff, D.B. Weiss, and Alexander Woo",
        "distractors": [
            "Jonathan Nolan and Lisa Joy",
            "Damon Lindelof and Carlton Cuse",
            "The Duffer Brothers"
        ],
        "d": 2
    },
    {
        "q": "Who created the acclaimed sci-fi anthology series 'Black Mirror', which originally debuted on British Channel 4 before moving to Netflix?",
        "correct": "Charlie Brooker",
        "distractors": ["Russell T Davies", "Steven Moffat", "Mark Gatiss"],
        "d": 2
    },
    {
        "q": "Which showrunner created 'Downton Abbey' before creating the HBO streaming period drama 'The Gilded Age'?",
        "correct": "Julian Fellowes",
        "distractors": ["Peter Morgan", "Anthony Horowitz", "Andrew Davies"],
        "d": 2
    },
    {
        "q": "Who wrote the teleplay for the Emmy-winning 'San Junipero' episode of 'Black Mirror'?",
        "correct": "Charlie Brooker",
        "distractors": ["William Bridges", "Jesse Armstrong", "Rashida Jones"],
        "d": 3
    },
    {
        "q": "Which playwright and screenwriter created the mystery comedy-drama 'Dead to Me' starring Christina Applegate and Linda Cardellini?",
        "correct": "Liz Feldman",
        "distractors": ["Jenji Kohan", "Mindy Kaling", "Nahnatchka Khan"],
        "d": 3
    },
    {
        "q": "Who directed the four-episode series finale of 'The Crown' and previously directed the theatrical films 'The Iron Lady' and 'Mamma Mia!'?",
        "correct": "Phyllida Lloyd did not direct; Christian Schwochow and Stephen Daldry directed major installments",
        "distractors": [
            "Tom Hooper directed all six season finales",
            "Kenneth Branagh directed the final season",
            "Stephen Daldry directed the entire six-season run solo"
        ],
        "d": 3
    },
    {
        "q": "Which director directed the influential 20-minute unbroken single-take kitchen episode 'Review' in 'The Bear' Season 1?",
        "correct": "Christopher Storer",
        "distractors": ["Joanna Calo", "Ramy Youssef", "Hiro Murai"],
        "d": 3
    },
    {
        "q": "Which acclaimed director of 'Atlanta' and Childish Gambino's 'This Is America' directed the series premiere of 'Station Eleven'?",
        "correct": "Hiro Murai",
        "distractors": ["Boots Riley", "Barry Jenkins", "Donald Glover"],
        "d": 3
    },
    {
        "q": "Which screenwriter adapted Walter Tevis's 1983 novel into the critically praised Netflix limited series 'The Queen's Gambit'?",
        "correct": "Scott Frank and Allan Scott",
        "distractors": ["Craig Mazin", "Alex Garland", "David Koepp"],
        "d": 3
    },
    {
        "q": "Who co-created and wrote the mockumentary vampire comedy series 'What We Do in the Shadows' for FX and Hulu?",
        "correct": "Jemaine Clement and Taika Waititi",
        "distractors": ["Bret McKenzie and Jemaine Clement", "Rhys Darby and Taika Waititi", "Bill Hader and Alec Berg"],
        "d": 2
    },
    {
        "q": "Which writer-producer created the post-apocalyptic thriller 'The Rain', Netflix's first Danish original series?",
        "correct": "Jannik Tai Mosholt, Christian Potalivo, and Esben Toft Jacobsen",
        "distractors": ["Baran bo Odar and Jantje Friese", "Søren Sveistrup", "Lars Mikkelsen"],
        "d": 3
    },
    {
        "q": "Which showrunner created the hit prison comedy-drama 'Orange Is the New Black' and previously created Showtime's 'Weeds'?",
        "correct": "Jenji Kohan",
        "distractors": ["Marta Kauffman", "Shonda Rhimes", "Jill Soloway"],
        "d": 2
    },
    {
        "q": "Who created the acclaimed dystopian miniseries 'Watchmen' for HBO in 2019, winning 11 Primetime Emmy Awards?",
        "correct": "Damon Lindelof",
        "distractors": ["Noah Hawley", "Sam Esmail", "Jonathan Nolan"],
        "d": 2
    },
    {
        "q": "Which writer-director wrote and directed the entire third season of 'Twin Peaks' ('The Return') for Showtime/streaming in 2017?",
        "correct": "David Lynch (co-written with Mark Frost)",
        "distractors": ["Mark Frost solo", "David Cronenberg", "Denis Villeneuve"],
        "d": 3
    },
    {
        "q": "Which creator served as showrunner for the sci-fi techno-thriller 'Mr. Robot' before creating the Netflix psychological thriller film 'Leave the World Behind'?",
        "correct": "Sam Esmail",
        "distractors": ["Nic Pizzolatto", "Cary Joji Fukunaga", "Noah Hawley"],
        "d": 2
    }
]

if __name__ == "__main__":
    build_batch(BATCH_4, "tools/staging/streaming_tv_batch4.json", batch_num=4)
