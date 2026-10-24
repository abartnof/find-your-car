#!/usr/bin/env python3
"""
Generate tools/staging/friends_batch7.json (100 questions, Extratextual: Casting, Negotiations, Production Lore).
"""
import sys
import os

from build_friends_batch import build_batch

questions = [
    {
        "q": "What was the starting per-episode salary earned by each of the six main cast members during Season 1?",
        "correct": "$22,500 per episode",
        "distractors": ["$10,000 per episode", "$40,000 per episode", "$75,000 per episode"],
        "d": 1
    },
    {
        "q": "What landmark per-episode salary did each of the six cast members negotiate for Seasons 9 and 10?",
        "correct": "$1,000,000 ($1 million) per episode",
        "distractors": ["$500,000 per episode", "$750,000 per episode", "$2,000,000 per episode"],
        "d": 1
    },
    {
        "q": "Which cast member was the primary instigator behind the cast forming a united front for collective salary bargaining in Season 3?",
        "correct": "David Schwimmer",
        "distractors": ["Matthew Perry", "Jennifer Aniston", "Matt LeBlanc"],
        "d": 1
    },
    {
        "q": "Why was David Schwimmer's salary initiative considered unprecedented and selfless in television history?",
        "correct": "He voluntarily took a pay cut so that all six actors would be paid equally",
        "distractors": ["He donated his entire syndication royalty to the crew", "He gave up his private dressing room to the guest stars", "He waived his per-episode fees for charity"],
        "d": 1
    },
    {
        "q": "Which female cast members became the highest-paid actresses in television history when their salaries reached $1 million per episode?",
        "correct": "Jennifer Aniston, Courteney Cox, and Lisa Kudrow",
        "distractors": ["Helen Hunt and Roseanne Barr", "Julia Louis-Dreyfus and Candice Bergen", "Sarah Jessica Parker and Calista Flockhart"],
        "d": 1
    },
    {
        "q": "What backend financial compensation did the cast secure in 2000 that continues to generate millions annually for each of them?",
        "correct": "2 percent of backend syndication and licensing profits",
        "distractors": ["5 percent of NBC's Thursday advertising revenue", "Direct ownership of the soundstage real estate", "10 percent of international home video sales"],
        "d": 2
    },
    {
        "q": "What character was Courteney Cox originally invited and encouraged to audition for by the show's producers?",
        "correct": "Rachel Green",
        "distractors": ["Phoebe Buffay", "Carol Willick", "Janice Litman"],
        "d": 1
    },
    {
        "q": "Why did Courteney Cox turn down the role of Rachel Green and ask to audition for Monica instead?",
        "correct": "She felt her own personality was much more aligned with Monica's strong, neurotic nature",
        "distractors": ["She felt Rachel had too few lines in the pilot script", "Her agent advised her that Monica was the central lead role", "She disliked the wardrobe chosen for Rachel"],
        "d": 1
    },
    {
        "q": "Which actress, known for 'The Facts of Life', came down to the final two alongside Courteney Cox for the role of Monica?",
        "correct": "Nancy McKeon",
        "distractors": ["Molly Ringwald", "Alyssa Milano", "Justine Bateman"],
        "d": 2
    },
    {
        "q": "Which comedic actress auditioned for Monica and later guest-starred as Lydia in 'The One with the Birth'?",
        "correct": "Leah Remini",
        "distractors": ["Fran Drescher", "Marisa Tomei", "Janeane Garofalo"],
        "d": 2
    },
    {
        "q": "For which character did co-creators David Crane and Marta Kauffman specifically write the role with David Schwimmer in mind?",
        "correct": "Ross Geller",
        "distractors": ["Chandler Bing", "Joey Tribbiani", "Gunther"],
        "d": 1
    },
    {
        "q": "Why did David Schwimmer initially turn down the offer to audition for Ross Geller?",
        "correct": "He had a miserable experience on an earlier canceled sitcom and vowed to stick to Chicago theater",
        "distractors": ["He had signed a multi-picture contract with a film studio", "He was preparing to enter a master's program in anthropology", "He refused to relocate from London to Los Angeles"],
        "d": 2
    },
    {
        "q": "Which actor, who later starred as Will Truman on 'Will & Grace', auditioned multiple times for the role of Ross?",
        "correct": "Eric McCormack",
        "distractors": ["Sean Hayes", "Thomas Gibson", "David Hyde Pierce"],
        "d": 2
    },
    {
        "q": "Which Hollywood actor/director was offered the role of Chandler Bing and turned it down before later guest starring as Pete Becker?",
        "correct": "Jon Favreau",
        "distractors": ["Ben Stiller", "Vince Vaughn", "Jon Cryer"],
        "d": 1
    },
    {
        "q": "Which 'Two and a Half Men' star auditioned for Chandler Bing from London, but had his audition tape delayed by UK customs?",
        "correct": "Jon Cryer",
        "distractors": ["Charlie Sheen", "Thomas Haden Church", "Rob Lowe"],
        "d": 2
    },
    {
        "q": "What futuristic science-fiction pilot was Matthew Perry contractually committed to that nearly prevented him from playing Chandler?",
        "correct": "'LAX 2194' (about airport baggage handlers in the twenty-second century)",
        "distractors": ["'Space Cadets'", "'Galactic Cargo 2000'", "'Subway 3000'"],
        "d": 2
    },
    {
        "q": "Which actor was offered the role of Chandler Bing first, turned it down for 'Madman of the People', and regretted it ever since?",
        "correct": "Craig Bierko",
        "distractors": ["French Stewart", "Steven Weber", "Richard Kind"],
        "d": 3
    },
    {
        "q": "How much money did Matt LeBlanc famously have left in his checking account when he auditioned for Joey Tribbiani?",
        "correct": "Eleven dollars ($11)",
        "distractors": ["Fifty cents ($0.50)", "One hundred dollars ($100)", "Five hundred dollars ($500)"],
        "d": 1
    },
    {
        "q": "What physical injury did Matt LeBlanc show up with at his final network audition for Joey after a drunken stumble?",
        "correct": "A bloody, badly scraped nose from hitting a toilet bowl",
        "distractors": ["A black eye from a bar scuffle", "A broken collarbone in a sling", "A chipped front incisor tooth"],
        "d": 2
    },
    {
        "q": "What was the very first item Matt LeBlanc purchased after receiving his first official Friends paycheck?",
        "correct": "A hot, full restaurant dinner",
        "distractors": ["A vintage motorcycle", "A new television set", "A leather jacket"],
        "d": 2
    },
    {
        "q": "What was the first luxury item Courteney Cox purchased with her initial earnings from the show?",
        "correct": "A brand new Porsche car",
        "distractors": ["A beach house in Malibu", "A diamond tennis bracelet", "An antique grandfather clock"],
        "d": 2
    },
    {
        "q": "Which future movie star auditioned for Joey Tribbiani before Matt LeBlanc secured the role?",
        "correct": "Vince Vaughn",
        "distractors": ["Mark Wahlberg", "Matthew McConaughey", "Owen Wilson"],
        "d": 2
    },
    {
        "q": "Which actor auditioned twice for Joey Tribbiani, was rejected both times, but was subsequently cast as David the Scientist?",
        "correct": "Hank Azaria",
        "distractors": ["Jon Lovitz", "Fisher Stevens", "Paul Rudd"],
        "d": 2
    },
    {
        "q": "Which future talk-show host was originally offered the role of Phoebe Buffay by producers but turned it down?",
        "correct": "Ellen DeGeneres",
        "distractors": ["Rosie O'Donnell", "Bonnie Hunt", "Ricki Lake"],
        "d": 1
    },
    {
        "q": "Which comedic actresses both auditioned for the role of Phoebe Buffay before Lisa Kudrow won the part?",
        "correct": "Kathy Griffin and Jane Lynch",
        "distractors": ["Sarah Silverman and Tina Fey", "Amy Poehler and Maya Rudolph", "Wanda Sykes and Chelsea Handler"],
        "d": 2
    },
    {
        "q": "On what popular NBC sitcom was Lisa Kudrow already portraying the eccentric waitress Ursula Buffay when cast in Friends?",
        "correct": "'Mad About You'",
        "distractors": ["'Seinfeld'", "'Wings'", "'Cheers'"],
        "d": 1
    },
    {
        "q": "Why did producers decide to create the character of Ursula as Phoebe's identical twin sister?",
        "correct": "To explain why Lisa Kudrow was appearing on two different NBC primetime Thursday sitcoms simultaneously",
        "distractors": ["Because Lisa Kudrow asked to play two characters for a higher salary", "Because a storyline required Phoebe to have a criminal background", "To create a crossover promotion with Saturday Night Live"],
        "d": 1
    },
    {
        "q": "Which actress was originally cast as Rachel Green before choosing to star in the ABC sitcom 'The Naked Truth' instead?",
        "correct": "Téa Leoni",
        "distractors": ["Jane Krakowski", "Jami Gertz", "Helen Slater"],
        "d": 2
    },
    {
        "q": "Which '30 Rock' star revealed in interviews that she had auditioned for the role of Rachel Green in 1994?",
        "correct": "Jane Krakowski",
        "distractors": ["Tina Fey", "Kristen Wiig", "Megan Mullally"],
        "d": 2
    },
    {
        "q": "Which 'Saved by the Bell' actress auditioned for Rachel Green but was considered slightly too young at age 20?",
        "correct": "Tiffani Thiessen",
        "distractors": ["Elizabeth Berkley", "Lark Voorhies", "Jennie Garth"],
        "d": 2
    },
    {
        "q": "What pre-taping backstage ritual did the six cast members maintain without fail before every single episode recording?",
        "correct": "A private group huddle and embrace with no producers or crew permitted",
        "distractors": ["Drinking a synchronized espresso toast in the kitchen", "Singing the opening verse of 'Smelly Cat'", "Touching the yellow picture frame on Monica's door for luck"],
        "d": 1
    },
    {
        "q": "What real-life event in Lisa Kudrow's personal life inspired the Season 4 and 5 storyline where Phoebe carries triplets?",
        "correct": "Lisa Kudrow became pregnant with her son Julian",
        "distractors": ["Lisa Kudrow's sister gave birth to triplets in real life", "Lisa Kudrow volunteered as a surrogate mother for a relative", "Lisa Kudrow wanted to wear comfortable maternity clothing on set"],
        "d": 1
    },
    {
        "q": "What real-life personal milestone for Courteney Cox had to be concealed during the filming of the final season in 2004?",
        "correct": "Courteney Cox was pregnant with her daughter Coco",
        "distractors": ["Courteney Cox was nursing a broken ankle in a cast", "Courteney Cox was undergoing laser eye surgery", "Courteney Cox had dyed her hair bright blonde for a movie"],
        "d": 1
    },
    {
        "q": "Why couldn't Courteney Cox's pregnancy be written into the show during Season 10?",
        "correct": "The show had already established that Monica and Chandler were biologically unable to conceive",
        "distractors": ["The producers wanted the finale to focus exclusively on Rachel", "Network censors prohibited pregnant characters from adopting children", "The writers had already finalized all 18 scripts before the season began"],
        "d": 1
    },
    {
        "q": "How did the costume and camera departments conceal Courteney Cox's growing baby bump in Season 10?",
        "correct": "By dressing her in loose, baggy sweaters, long scarves, and holding laundry baskets or props",
        "distractors": ["By filming her exclusively from the shoulders up", "By using a digital CGI body replacement technique", "By having her sit behind the Central Perk counter in every scene"],
        "d": 1
    },
    {
        "q": "What Manhattan street address serves as the exterior facade for Monica, Rachel, Chandler, and Joey's apartment building?",
        "correct": "90 Bedford Street (at the corner of Grove Street) in Greenwich Village",
        "distractors": ["125 Bleecker Street in SoHo", "45 Perry Street in the West Village", "210 East 10th Street in the East Village"],
        "d": 1
    },
    {
        "q": "What restaurant operates in the ground-floor retail space of the real Greenwich Village building used for exterior shots?",
        "correct": "The Little Owl",
        "distractors": ["Central Perk Cafe", "The Village Bistro", "Buvette"],
        "d": 2
    },
    {
        "q": "Was any regular scene of Friends ever filmed on location in the actual streets of New York City during its ten seasons?",
        "correct": "No, the entire series was filmed on soundstages in Burbank, California (except for exterior B-roll and the London shoot)",
        "distractors": ["Yes, the Thanksgiving football game was filmed in Central Park", "Yes, all Central Perk exteriors were filmed in Greenwich Village", "Yes, Season 1 was entirely filmed in Manhattan before moving west"],
        "d": 1
    },
    {
        "q": "In which city did the cast travel on location to film the Season 4 wedding episodes in 1998?",
        "correct": "London, England",
        "distractors": ["Paris, France", "Rome, Italy", "Dublin, Ireland"],
        "d": 1
    },
    {
        "q": "Why was Lisa Kudrow absent from the on-location filming in London for the Season 4 finale?",
        "correct": "She was in the third trimester of her real-life pregnancy and unable to fly internationally",
        "distractors": ["She was shooting a feature film in Vancouver", "She contracted a severe case of bronchitis", "She had a contractual dispute with the British production crew"],
        "d": 2
    },
    {
        "q": "How did the writers explain Phoebe remaining in New York while the other five friends traveled to London?",
        "correct": "Phoebe was heavily pregnant with the triplets and her obstetrician forbade air travel",
        "distractors": ["Phoebe lost her passport on the subway", "Phoebe refused to fly on airplanes due to spiritual beliefs", "Phoebe had to care for Joey's chick and duck"],
        "d": 1
    },
    {
        "q": "Which cast member nearly walked away from the series prior to Season 10, citing burnout and wanting to leave on a high note?",
        "correct": "Jennifer Aniston",
        "distractors": ["Matthew Perry", "Matt LeBlanc", "David Schwimmer"],
        "d": 1
    },
    {
        "q": "What physical prop piece was given to each cast member as a memento after the final episode wrapped in 2004?",
        "correct": "A piece of the pavement/brick from outside Central Perk mounted in a wooden box",
        "distractors": ["Their character's original apartment front door key", "A replica of the yellow door peephole frame", "A signed Central Perk ceramic coffee mug"],
        "d": 2
    },
    {
        "q": "What personal addiction battles did Matthew Perry candidly detail in his 2022 memoir 'Friends, Lovers, and the Big Terrible Thing'?",
        "correct": "Severe alcohol and prescription opioid (Vicodin) addictions during the series run",
        "distractors": ["Pathological gambling and sports betting debts", "Compulsive shopping and luxury car hoarding", "Addiction to performance-enhancing steroids"],
        "d": 1
    },
    {
        "q": "What dramatic physical change in Matthew Perry's appearance between Season 6 and Season 7 was caused by severe pancreatitis?",
        "correct": "He lost approximately 50 pounds following a hospital stay for pancreatitis",
        "distractors": ["He shaved his head completely bald", "He underwent corrective spinal surgery that altered his posture", "He grew a full beard and wore tinted glasses"],
        "d": 2
    },
    {
        "q": "What did the cast and crew do immediately after filming the final take of 'The Last One' on January 23, 2004?",
        "correct": "They sat together on the Central Perk orange sofa drinking champagne and weeping",
        "distractors": ["They immediately destroyed the sets with sledgehammers", "They took an overnight chartered flight to Las Vegas", "They hosted a live televised press conference from Stage 24"],
        "d": 2
    },
    {
        "q": "Who threw the lavish official farewell wrap party for the cast and crew in February 2004?",
        "correct": "Warner Bros. and executive producers at the Park Hyatt in Century City",
        "distractors": ["Brad Pitt and Jennifer Aniston at their Beverly Hills estate", "NBC at the Rainbow Room in New York City", "James Burrows at Caesar's Palace in Las Vegas"],
        "d": 3
    },
    {
        "q": "Which musical superstar performed a private live set at the official Friends wrap party in 2004?",
        "correct": "The Rembrandts and Sheryl Crow",
        "distractors": ["U2", "Bruce Springsteen", "Coldplay"],
        "d": 3
    },
    {
        "q": "What did the six cast members add to their contracts in Season 7 ensuring their equal treatment in marketing?",
        "correct": "Contractual clauses requiring that all promotional posters and magazine covers feature all six equally",
        "distractors": ["A clause banning solo television commercials", "A guarantee of equal dialogue line counts per script", "A veto over any guest star castings"],
        "d": 2
    },
    {
        "q": "What famous magazine cover in May 1995 featured the six stars bundled together in bed, photographed by Mark Seliger?",
        "correct": "Rolling Stone",
        "distractors": ["Vanity Fair", "Entertainment Weekly", "People"],
        "d": 2
    },
    {
        "q": "What photographer captured the iconic 1995 Rolling Stone cover of the cast lying together under white sheets?",
        "correct": "Mark Seliger",
        "distractors": ["Annie Leibovitz", "Herb Ritts", "David LaChapelle"],
        "d": 2
    },
    {
        "q": "How many total times did the cast of Friends appear on the cover of Rolling Stone magazine during the show's run?",
        "correct": "3 times (1995, 1999, and 2004)",
        "distractors": ["Only once in 1995", "5 times", "7 times"],
        "d": 3
    },
    {
        "q": "What real-life romance blossomed on set between a cast member and an executive producer or guest star in Season 4?",
        "correct": "Matthew Perry dated guest star Paget Brewster (Kathy) briefly off-screen",
        "distractors": ["David Schwimmer dated Helen Baxendale (Emily)", "Matt LeBlanc dated Elle Macpherson (Janine)", "Courteney Cox dated Michael Vartan (Timothy Burke)"],
        "d": 3
    },
    {
        "q": "What did Jennifer Aniston and David Schwimmer reveal during the 2021 reunion special about their Season 1 dynamic?",
        "correct": "They had a huge mutual crush on each other but never acted on it because one of them was always in a relationship",
        "distractors": ["They secretly dated for two months before the pilot aired", "They actively disliked each other during the first few table reads", "They originally planned to buy a shared house together in Burbank"],
        "d": 1
    },
    {
        "q": "Where did David Schwimmer and Jennifer Aniston say they channeled all their mutual romantic feelings and adoration?",
        "correct": "Directly into Ross and Rachel's on-screen romance and first kiss at Central Perk",
        "distractors": ["Into late-night phone conversations during hiatus", "Into writing song lyrics together", "Into coaching each other on other dates"],
        "d": 1
    },
    {
        "q": "Which cast member was the youngest of the six leads when the series debuted in September 1994?",
        "correct": "Jennifer Aniston and Matthew Perry (both 25 years old)",
        "distractors": ["Matt LeBlanc (27)", "Courteney Cox (30)", "David Schwimmer (27)"],
        "d": 2
    },
    {
        "q": "Which cast member was the oldest of the six leads when the pilot premiered in 1994?",
        "correct": "Lisa Kudrow (31 years old)",
        "distractors": ["Courteney Cox (30)", "David Schwimmer (27)", "Matt LeBlanc (27)"],
        "d": 2
    },
    {
        "q": "What popular handheld electronic game did the cast frequently play together on set between scene takes in early seasons?",
        "correct": "Game Boy (playing Tetris)",
        "distractors": ["Sega Game Gear", "Tamagotchi", "Nintendo DS"],
        "d": 3
    },
    {
        "q": "What word-puzzle board game did the six actors obsessively play together in their dressing rooms?",
        "correct": "Scrabble",
        "distractors": ["Boggle", "Pictionary", "Trivial Pursuit"],
        "d": 2
    },
    {
        "q": "What daily dietary routine did Courteney Cox, Jennifer Aniston, and Lisa Kudrow share on set for ten straight years?",
        "correct": "Eating the exact same modified Cobb salad together for lunch every single day",
        "distractors": ["Drinking green protein smoothies made by Monica's chef assistant", "Eating sushi platters delivered from Beverly Hills", "Sharing egg white omelets from the studio commissary"],
        "d": 1
    },
    {
        "q": "What special ingredient did Jennifer Aniston add to their daily set salad that made it famous as 'The Jennifer Aniston Salad'?",
        "correct": "Bulgur wheat, diced cucumber, chickpeas, feta cheese, and chopped pistachios",
        "distractors": ["Quinoa, dried cranberries, goat cheese, and walnuts", "Brown rice, grilled shrimp, avocado, and almonds", "Couscous, sun-dried tomatoes, pine nuts, and parmesan"],
        "d": 2
    },
    {
        "q": "Which cast member's father was a veteran daytime soap opera actor on 'Days of Our Lives' in real life?",
        "correct": "Jennifer Aniston (her father John Aniston played Victor Kiriakis)",
        "distractors": ["Matt LeBlanc", "Courteney Cox", "Matthew Perry"],
        "d": 1
    },
    {
        "q": "What irony connects Jennifer Aniston's real father to Joey Tribbiani's character arc?",
        "correct": "John Aniston starred on 'Days of Our Lives' for decades, the exact soap opera Joey joins",
        "distractors": ["Her father guest-starred as Joey's doctor", "Her father directed Joey's audition scenes", "Her father played Dr. Drake Ramoray's father on TV"],
        "d": 1
    },
    {
        "q": "What actor father of Matthew Perry made a cameo guest appearance in 'The One with Rachel's New Dress'?",
        "correct": "John Bennett Perry (playing Joshua Burgin's father)",
        "distractors": ["Dick Van Dyke", "James Brolin", "Robert Foxworth"],
        "d": 2
    },
    {
        "q": "What iconic commercial campaign did Matthew Perry's real father John Bennett Perry star in during the 1970s and 1980s?",
        "correct": "The Old Spice sailor commercial campaign",
        "distractors": ["The Marlboro Man campaign", "The Maytag repairman campaign", "The Campbell's soup father"],
        "d": 3
    },
    {
        "q": "Which cast member was a competitive junior tennis player in Canada before pursuing acting?",
        "correct": "Matthew Perry",
        "distractors": ["David Schwimmer", "Matt LeBlanc", "Lisa Kudrow"],
        "d": 2
    },
    {
        "q": "What prestigious college degree does Lisa Kudrow hold from Vassar College?",
        "correct": "Bachelor of Science in Biology",
        "distractors": ["Bachelor of Arts in English Literature", "Bachelor of Fine Arts in Theater", "Bachelor of Science in Psychology"],
        "d": 2
    },
    {
        "q": "What scientific research did Lisa Kudrow conduct with her physician father Dr. Lee Kudrow prior to acting?",
        "correct": "A clinical study on hemispheric brain dominance and cluster headaches",
        "distractors": ["Cardiovascular response to high-altitude exercise", "Genetic sequencing of botanical pathogens", "Pediatric cognitive developmental milestones"],
        "d": 3
    },
    {
        "q": "Which famous comedic improv troupe in Los Angeles was Lisa Kudrow a member of alongside Conan O'Brien?",
        "correct": "The Groundlings",
        "distractors": ["The Second City", "Upright Citizens Brigade", "ImprovOlympic"],
        "d": 2
    },
    {
        "q": "Which cast member co-founded the Lookingglass Theatre Company in Chicago in 1988?",
        "correct": "David Schwimmer",
        "distractors": ["Matthew Perry", "Matt LeBlanc", "Courteney Cox"],
        "d": 2
    },
    {
        "q": "What university did David Schwimmer attend where he earned a Bachelor of Science in Speech and Theater?",
        "correct": "Northwestern University",
        "distractors": ["University of Southern California", "Yale University", "UCLA"],
        "d": 2
    },
    {
        "q": "What music video for Bruce Springsteen did Courteney Cox famously star in in 1984, dancing on stage?",
        "correct": "\"Dancing in the Dark\"",
        "distractors": ["\"Born in the U.S.A.\"", "\"Glory Days\"", "\"I'm on Fire\""],
        "d": 1
    },
    {
        "q": "Who directed the 1984 Bruce Springsteen music video 'Dancing in the Dark' featuring young Courteney Cox?",
        "correct": "Brian De Palma",
        "distractors": ["Martin Scorsese", "Steven Spielberg", "David Fincher"],
        "d": 2
    },
    {
        "q": "What 1980s hit sitcom did Courteney Cox star in as Alex P. Keaton's girlfriend Lauren Miller?",
        "correct": "'Family Ties'",
        "distractors": ["'Growing Pains'", "'Who's the Boss?'", "'Silver Spoons'"],
        "d": 1
    },
    {
        "q": "What hit horror movie franchise did Courteney Cox star in as reporter Gale Weathers throughout the run of Friends?",
        "correct": "'Scream' (Scream 1, 2, and 3)",
        "distractors": ["'I Know What You Did Last Summer'", "'Halloween'", "'A Nightmare on Elm Street'"],
        "d": 1
    },
    {
        "q": "Which actor did Courteney Cox marry in 1999, changing her screen credits to Courteney Cox Arquette?",
        "correct": "David Arquette",
        "distractors": ["Michael Keaton", "Brad Pitt", "Christian Slater"],
        "d": 1
    },
    {
        "q": "In the Season 6 premiere 'The One After Vegas', what gag did producers add to the opening credits to celebrate Courteney's marriage?",
        "correct": "Every single cast member had 'Arquette' added to their last name in the credits",
        "distractors": ["Wedding bells chimed over the theme song", "A photo of the wedding cake replaced the water fountain", "All six actors were shown wearing wedding veils"],
        "d": 1
    },
    {
        "q": "Which of the six actors appeared in a series of popular Heinz Ketchup commercials in the late 1980s?",
        "correct": "Matt LeBlanc",
        "distractors": ["Matthew Perry", "David Schwimmer", "Jennifer Aniston"],
        "d": 2
    },
    {
        "q": "What television commercial for Coca-Cola featured Matt LeBlanc roller-skating through a warm city street?",
        "correct": "A 1990 Cherry 7-Up commercial (and Coca-Cola commercial)",
        "distractors": ["Pepsi Generation ad", "Mountain Dew extreme ad", "Dr Pepper retro ad"],
        "d": 3
    },
    {
        "q": "What comedy film about an intelligent baseball-playing chimpanzee did Matt LeBlanc star in during hiatus in 1996?",
        "correct": "'Ed'",
        "distractors": ["'Dunston Checks In'", "'MVP: Most Valuable Primate'", "'Monkey Business'"],
        "d": 2
    },
    {
        "q": "What hit film comedy did Matthew Perry star in alongside Bruce Willis in 2000 during the show's run?",
        "correct": "'The Whole Nine Yards'",
        "distractors": ["'The Whole Ten Yards'", "'Fools Rush In'", "'Three to Tango'"],
        "d": 1
    },
    {
        "q": "What romantic comedy did Matthew Perry star in alongside Salma Hayek in 1997?",
        "correct": "'Fools Rush In'",
        "distractors": ["'Three to Tango'", "'Serving Sara'", "'Almost Heroes'"],
        "d": 2
    },
    {
        "q": "What romantic comedy did Jennifer Aniston star in alongside Paul Rudd in 1998?",
        "correct": "'The Object of My Affection'",
        "distractors": ["'Picture Perfect'", "'She's the One'", "'Along Came Polly'"],
        "d": 2
    },
    {
        "q": "What critically acclaimed dark indie comedy did Jennifer Aniston star in in 2002 as frustrated store clerk Justine Last?",
        "correct": "'The Good Girl'",
        "distractors": ["'Office Space'", "'Friends with Money'", "'Rock Star'"],
        "d": 2
    },
    {
        "q": "What cult classic 1999 workplace satire comedy by Mike Judge featured Jennifer Aniston wearing flare buttons at Chotchkie's?",
        "correct": "'Office Space'",
        "distractors": ["'Clerks'", "'Waiting...'", "'Extract'"],
        "d": 1
    },
    {
        "q": "What animated character did David Schwimmer voice in DreamWorks' blockbuster 2005 animated film 'Madagascar'?",
        "correct": "Melman the neurotic giraffe",
        "distractors": ["Alex the lion", "Marty the zebra", "Gloria the hippo"],
        "d": 1
    },
    {
        "q": "What critically acclaimed HBO World War II miniseries did David Schwimmer star in in 2001 as strict Captain Herbert Sobel?",
        "correct": "'Band of Brothers'",
        "distractors": ["'The Pacific'", "'Generation Kill'", "'From the Earth to the Moon'"],
        "d": 1
    },
    {
        "q": "Which critically acclaimed cult comedy series on HBO did Lisa Kudrow create and star in as Valerie Cherish in 2005?",
        "correct": "'The Comeback'",
        "distractors": ["'Web Therapy'", "'Romy and Michele'", "'Unbreakable Kimmy Schmidt'"],
        "d": 1
    },
    {
        "q": "What beloved 1997 buddy comedy film did Lisa Kudrow star in alongside Mira Sorvino?",
        "correct": "'Romy and Michele's High School Reunion'",
        "distractors": ["'Clockwatchers'", "'The Opposite of Sex'", "'Hanging Up'"],
        "d": 1
    },
    {
        "q": "What real-life guest appearance bet did Bruce Willis make with Matthew Perry on the set of 'The Whole Nine Yards'?",
        "correct": "Willis bet that the movie would not open at #1 at the box office; if it did, Willis would guest-star on Friends for free",
        "distractors": ["Willis bet Perry couldn't beat him in ping-pong", "Willis bet that Friends would not win the Emmy for Best Comedy", "Willis bet Perry couldn't run a marathon in under four hours"],
        "d": 1
    },
    {
        "q": "What did Bruce Willis do with his SAG acting salary earned from guest starring on Friends after losing the bet?",
        "correct": "He donated the entire paycheck to multiple children's and AIDS charities",
        "distractors": ["He bought a motorcycle for Matthew Perry", "He paid for the Friends crew wrap party", "He bought a round of drinks for the live studio audience"],
        "d": 1
    },
    {
        "q": "How did Robin Williams and Billy Crystal's cameo in the Season 3 premiere 'The One with the Ultimate Fighting Champion' come about?",
        "correct": "They were shooting a movie on an adjacent Warner Bros. soundstage and agreed to an entirely improvised walk-on",
        "distractors": ["They were invited months in advance by director James Burrows", "They won a charity auction bid to appear on the show", "They were promoting a joint stand-up comedy television special"],
        "d": 1
    },
    {
        "q": "What comedy film were Robin Williams and Billy Crystal filming next door when they dropped into Central Perk?",
        "correct": "'Fathers' Day'",
        "distractors": ["'Patch Adams'", "'City Slickers II'", "'Good Will Hunting'"],
        "d": 2
    },
    {
        "q": "How much of Robin Williams and Billy Crystal's dialogue on the Central Perk couch was written in the script?",
        "correct": "None of it; their entire scene was 100% improvised on the spot",
        "distractors": ["Every line was scripted word-for-word by David Crane", "Only Robin Williams's lines were improvised", "Only the final punchline was scripted"],
        "d": 1
    },
    {
        "q": "Which member of the British royal family agreed to make a brief appearance with Matt LeBlanc in London in 1998?",
        "correct": "Sarah Ferguson, Duchess of York",
        "distractors": ["Prince Harry", "Zara Phillips", "Sophie, Countess of Wessex"],
        "d": 2
    },
    {
        "q": "Which renowned supermodel made a cameo appearance in 'The One with the Flashback' as Joey's dream fantasy?",
        "correct": "No supermodel appeared; Jill Goodacre and Elle Macpherson appeared in other episodes",
        "distractors": ["Cindy Crawford", "Naomi Campbell", "Linda Evangelista"],
        "d": 3
    },
    {
        "q": "Which actor, who famously played Dr. Doug Ross on 'ER', made an emergency room doctor cameo in Season 1?",
        "correct": "George Clooney",
        "distractors": ["Anthony Edwards", "Noah Wyle (appeared alongside Clooney)", "Julianna Margulies"],
        "d": 1
    },
    {
        "q": "What real-life couple was married during Brad Pitt's iconic guest appearance in Season 8's Thanksgiving episode?",
        "correct": "Brad Pitt and Jennifer Aniston were married in real life",
        "distractors": ["Courteney Cox and David Arquette", "Matthew Perry and Julia Roberts", "Lisa Kudrow and Michel Stern"],
        "d": 1
    },
    {
        "q": "In what year did Jennifer Aniston and Brad Pitt marry in Malibu before his appearance on Friends?",
        "correct": "July 2000",
        "distractors": ["June 1998", "September 2001", "December 2002"],
        "d": 2
    },
    {
        "q": "How did Matthew Perry persuade Julia Roberts to make her guest appearance in 'The One After the Superbowl'?",
        "correct": "She demanded he write her a paper on quantum physics, which he faxed to her with flirty notes",
        "distractors": ["He sent three dozen red roses every day for two weeks", "He promised to appear in her next romantic comedy for free", "He cooked her dinner at his apartment in Manhattan"],
        "d": 1
    }
]

if __name__ == "__main__":
    out_path = os.path.join(os.path.dirname(__file__), "staging", "friends_batch7.json")
    build_batch(questions, out_path, batch_num=7)
