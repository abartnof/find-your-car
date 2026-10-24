#!/usr/bin/env python3
"""
Generate tools/staging/friends_batch5.json (100 questions, Metatextual: Broadcast, Ratings, Milestones).
"""
import sys
import os

from build_friends_batch import build_batch

questions = [
    {
        "q": "On what date did the Pilot episode of Friends make its original television broadcast debut on NBC?",
        "correct": "September 22, 1994",
        "distractors": ["August 15, 1994", "October 12, 1994", "November 3, 1994"],
        "d": 1
    },
    {
        "q": "On what date was the hour-long series finale 'The Last One' broadcast on NBC?",
        "correct": "May 6, 2004",
        "distractors": ["May 20, 2004", "April 29, 2004", "June 10, 2004"],
        "d": 1
    },
    {
        "q": "How many total television seasons of Friends were produced and broadcast during its original run?",
        "correct": "10 seasons",
        "distractors": ["8 seasons", "9 seasons", "11 seasons"],
        "d": 1
    },
    {
        "q": "How many total broadcast episodes comprise the complete run of Friends across its ten seasons?",
        "correct": "236 episodes",
        "distractors": ["218 episodes", "248 episodes", "252 episodes"],
        "d": 1
    },
    {
        "q": "What major American television network broadcast Friends throughout its entire ten-year original run?",
        "correct": "NBC",
        "distractors": ["CBS", "ABC", "FOX"],
        "d": 1
    },
    {
        "q": "What iconic NBC marketing branding block did Friends anchor on Thursday evenings?",
        "correct": "\"Must See TV\"",
        "distractors": ["\"Comedy Night Done Right\"", "\"TGIF\"", "\"Super Thursday\""],
        "d": 1
    },
    {
        "q": "What timeslot on Thursday evenings did Friends predominantly occupy during its prime run?",
        "correct": "8:00 PM Eastern / Pacific",
        "distractors": ["9:00 PM Eastern / Pacific", "8:30 PM Eastern / Pacific", "9:30 PM Eastern / Pacific"],
        "d": 1
    },
    {
        "q": "What hit sitcom originally preceded Friends at 8:00 PM during early Season 1 before Friends moved to the lead-off slot?",
        "correct": "'Mad About You'",
        "distractors": ["'Seinfeld'", "'Frasier'", "'Wings'"],
        "d": 2
    },
    {
        "q": "What massive sporting event served as the lead-in to the highest-rated single episode of Friends in history in January 1996?",
        "correct": "Super Bowl XXX",
        "distractors": ["The 1996 Summer Olympics", "Super Bowl XXIX", "The 1994 World Series"],
        "d": 1
    },
    {
        "q": "Approximately how many viewers tuned in to watch 'The One After the Superbowl' on January 28, 1996?",
        "correct": "52.9 million viewers",
        "distractors": ["41.2 million viewers", "62.4 million viewers", "35.8 million viewers"],
        "d": 2
    },
    {
        "q": "Approximately how many viewers watched the series finale 'The Last One' on May 6, 2004?",
        "correct": "52.5 million viewers",
        "distractors": ["38.2 million viewers", "68.4 million viewers", "44.1 million viewers"],
        "d": 1
    },
    {
        "q": "Where does the Friends series finale rank among the most-watched television series finales in U.S. history?",
        "correct": "Fifth most-watched series finale",
        "distractors": ["Most-watched series finale of all time", "Second most-watched series finale", "Tenth most-watched series finale"],
        "d": 2
    },
    {
        "q": "Which three television show finales drew higher viewership in U.S. broadcast history than Friends?",
        "correct": "M*A*S*H, Cheers, and Seinfeld",
        "distractors": ["Seinfeld, The Sopranos, and ER", "M*A*S*H, The Cosby Show, and Home Improvement", "Cheers, Dallas, and The Fugitive"],
        "d": 2
    },
    {
        "q": "Approximately how much did NBC charge advertisers for a single 30-second commercial spot during the series finale in 2004?",
        "correct": "$2.0 million",
        "distractors": ["$750,000", "$1.0 million", "$3.5 million"],
        "d": 2
    },
    {
        "q": "In which season did Friends finish as the undisputed number one ranked show overall in the Nielsen primetime ratings?",
        "correct": "Season 8 (2001–2002)",
        "distractors": ["Season 2 (1995–1996)", "Season 5 (1998–1999)", "Season 10 (2003–2004)"],
        "d": 1
    },
    {
        "q": "What CBS reality television powerhouse posed the most formidable ratings challenge to Friends when moved to Thursdays in 2001?",
        "correct": "'Survivor'",
        "distractors": ["'The Amazing Race'", "'Big Brother'", "'American Idol'"],
        "d": 1
    },
    {
        "q": "What outdoor public Manhattan venue broadcast the series finale live on a giant Astrovision screen for thousands of gathered fans?",
        "correct": "Times Square",
        "distractors": ["Central Park Great Lawn", "Rockefeller Plaza", "Bryant Park"],
        "d": 1
    },
    {
        "q": "What standard naming formula was utilized for nearly every episode title across the ten-season run?",
        "correct": "\"The One with...\" or \"The One Where...\"",
        "distractors": ["\"The Case of...\"", "\"A Tale of...\"", "\"Life with...\""],
        "d": 1
    },
    {
        "q": "What is the official title of the 1994 series premiere episode on original broadcast schedules?",
        "correct": "\"The Pilot\"",
        "distractors": ["\"The First One\"", "\"The One Where It All Began\"", "\"The One Where Rachel Runs In\""],
        "d": 1
    },
    {
        "q": "What alternative title was appended to the pilot episode on syndication prints and DVD releases?",
        "correct": "\"The One Where Monica Gets a Roommate\"",
        "distractors": ["\"The One with the Wedding Dress\"", "\"The One Where Rachel Escapes\"", "\"The One in Central Perk\""],
        "d": 2
    },
    {
        "q": "What is the official title of the two-part series finale broadcast in May 2004?",
        "correct": "\"The Last One\"",
        "distractors": ["\"The One Where They Say Goodbye\"", "\"The One with the Final Keys\"", "\"The End of Central Perk\""],
        "d": 1
    },
    {
        "q": "In which television season did Friends debut in the Nielsen Top 10 by finishing at #8 overall?",
        "correct": "Season 1 (1994–1995)",
        "distractors": ["Season 2 (1995–1996)", "Season 3 (1996–1997)", "Season 4 (1997–1998)"],
        "d": 2
    },
    {
        "q": "What was the average weekly viewership for Friends during its peak-rated second season (1995–1996)?",
        "correct": "Approximately 31.7 million viewers per episode",
        "distractors": ["Approximately 22.1 million viewers per episode", "Approximately 40.5 million viewers per episode", "Approximately 18.3 million viewers per episode"],
        "d": 2
    },
    {
        "q": "In what year did Friends first enter broadcast syndication on local television stations across the United States?",
        "correct": "Autumn 1998",
        "distractors": ["Autumn 1996", "Autumn 2000", "Spring 2002"],
        "d": 2
    },
    {
        "q": "Which major studio produced Friends and earned multi-billion-dollar syndication and streaming licensing windfalls?",
        "correct": "Warner Bros. Television",
        "distractors": ["Paramount Television", "Universal Television", "Sony Pictures Television"],
        "d": 1
    },
    {
        "q": "What subscription streaming service acquired exclusive SVOD rights to all 236 episodes in 2014 for debut in January 2015?",
        "correct": "Netflix",
        "distractors": ["Hulu", "Amazon Prime Video", "Apple TV+"],
        "d": 1
    },
    {
        "q": "Approximately how much did Netflix pay WarnerMedia to retain non-exclusive domestic streaming rights to Friends for the year 2019 alone?",
        "correct": "Approximately $100 million",
        "distractors": ["Approximately $20 million", "Approximately $45 million", "Approximately $250 million"],
        "d": 2
    },
    {
        "q": "What WarnerMedia streaming platform acquired exclusive domestic rights starting in May 2020 in a five-year, $425 million deal?",
        "correct": "HBO Max",
        "distractors": ["Peacock", "Paramount+", "Discovery+"],
        "d": 1
    },
    {
        "q": "What British terrestrial broadcaster served as the original UK home of Friends from 1995 until the finale in 2004?",
        "correct": "Channel 4",
        "distractors": ["BBC One", "ITV", "BBC Two"],
        "d": 2
    },
    {
        "q": "What British pay-television network aired premiering first-run episodes of Friends in the UK prior to their terrestrial airing?",
        "correct": "Sky1",
        "distractors": ["E4", "Living TV", "UKTV Gold"],
        "d": 3
    },
    {
        "q": "On what date did the unscripted retrospective special 'Friends: The Reunion' premiere globally on HBO Max?",
        "correct": "May 27, 2021",
        "distractors": ["November 15, 2020", "September 22, 2021", "January 1, 2022"],
        "d": 1
    },
    {
        "q": "What British talk-show host served as the moderator and master of ceremonies for 'Friends: The Reunion' in 2021?",
        "correct": "James Corden",
        "distractors": ["Graham Norton", "Jimmy Fallon", "Conan O'Brien"],
        "d": 1
    },
    {
        "q": "Who directed the 2021 retrospective special 'Friends: The Reunion'?",
        "correct": "Ben Winston",
        "distractors": ["James Burrows", "Kevin S. Bright", "David Schwimmer"],
        "d": 2
    },
    {
        "q": "How many total Thanksgiving-themed episodes were produced over the ten seasons of Friends?",
        "correct": "10 episodes (one in each season)",
        "distractors": ["8 episodes", "9 episodes", "12 episodes"],
        "d": 1
    },
    {
        "q": "Which season of Friends is the only season featuring a shorter order of 18 episodes instead of 24?",
        "correct": "Season 10",
        "distractors": ["Season 1", "Season 7", "Season 9"],
        "d": 1
    },
    {
        "q": "Why was the final season of Friends truncated to 18 episodes instead of a full standard 24-episode order?",
        "correct": "The cast requested a shorter season to pursue film careers and family commitments",
        "distractors": ["NBC lacked the budget to pay the cast for 24 episodes", "The writers ran out of storyline material for Monica and Chandler", "A writers' strike shut down television production in early 2004"],
        "d": 2
    },
    {
        "q": "What lead-out medical drama on NBC's 'Must See TV' Thursday lineup frequently shared the top two Nielsen slots with Friends?",
        "correct": "'ER'",
        "distractors": ["'Chicago Hope'", "'NYPD Blue'", "'Law & Order'"],
        "d": 1
    },
    {
        "q": "What Thursday night comedy powerhouse broadcast directly following Friends at 8:30 or 9:00 PM during the late 1990s?",
        "correct": "'Seinfeld'",
        "distractors": ["'Home Improvement'", "'Roseanne'", "'Murphy Brown'"],
        "d": 1
    },
    {
        "q": "What Emmy-winning comedy about two gay men and their female best friends joined NBC's Thursday lineup in 1998 alongside Friends?",
        "correct": "'Will & Grace'",
        "distractors": ["'Frasier'", "'Just Shoot Me!'", "'NewsRadio'"],
        "d": 1
    },
    {
        "q": "What was the final Nielsen rank of Friends during its tenth and farewell season (2003–2004)?",
        "correct": "Fourth overall (averaging 22.8 million viewers)",
        "distractors": ["First overall", "Eighth overall", "Eleventh overall"],
        "d": 2
    },
    {
        "q": "Which single episode in Season 2 features the most high-profile ensemble of celebrity guest stars in the series' history?",
        "correct": "\"The One After the Superbowl\" (Parts 1 & 2)",
        "distractors": ["\"The One with the Prom Video\"", "\"The One with the Lesbian Wedding\"", "\"The One with All the Jealousy\""],
        "d": 1
    },
    {
        "q": "What was the Nielsen household rating for the series finale of Friends on May 6, 2004?",
        "correct": "29.8 rating / 43 share",
        "distractors": ["20.2 rating / 31 share", "38.5 rating / 55 share", "15.4 rating / 24 share"],
        "d": 3
    },
    {
        "q": "What special programming event did NBC broadcast immediately preceding the series finale on May 6, 2004?",
        "correct": "A one-hour retrospective clip special titled 'The One with All the Other Ones'",
        "distractors": ["The pilot episode remastered in high definition", "A live concert special featuring The Rembrandts", "A live red-carpet pre-show from Central Park"],
        "d": 2
    },
    {
        "q": "Approximately how many viewers watched the one-hour retrospective special directly preceding the series finale?",
        "correct": "Approximately 36 million viewers",
        "distractors": ["Approximately 18 million viewers", "Approximately 48 million viewers", "Approximately 25 million viewers"],
        "d": 2
    },
    {
        "q": "What was the highest-rated episode of Friends in Season 1, drawing over 31 million viewers in February 1995?",
        "correct": "\"The One with Two Parts, Part 2\"",
        "distractors": ["\"The Pilot\"", "\"The One with the Blackout\"", "\"The One Where Rachel Finds Out\""],
        "d": 3
    },
    {
        "q": "What was the title of the spin-off series centered on Matt LeBlanc's character that premiered in Friends' former timeslot in autumn 2004?",
        "correct": "'Joey'",
        "distractors": ["'Tribbiani'", "'Days in LA'", "'How You Doin''"],
        "d": 1
    },
    {
        "q": "How many seasons did the spin-off sitcom 'Joey' air on NBC before being canceled due to low ratings?",
        "correct": "2 seasons",
        "distractors": ["1 season", "3 seasons", "4 seasons"],
        "d": 1
    },
    {
        "q": "To which West Coast city did Joey Tribbiani relocate in the spin-off series 'Joey'?",
        "correct": "Los Angeles, California",
        "distractors": ["San Francisco, California", "San Diego, California", "Las Vegas, Nevada"],
        "d": 1
    },
    {
        "q": "Which actress starred as Joey's sister Gina Tribbiani in the spin-off sitcom 'Joey'?",
        "correct": "Drea de Matteo",
        "distractors": ["Edie Falco", "Marisa Tomei", "Leah Remini"],
        "d": 2
    },
    {
        "q": "Which major Canadian broadcast network aired Friends during its original run simultaneously with NBC?",
        "correct": "Global Television Network",
        "distractors": ["CBC Television", "CTV", "Citytv"],
        "d": 3
    },
    {
        "q": "What Australian commercial network held the primary terrestrial first-run broadcast rights to Friends?",
        "correct": "Nine Network",
        "distractors": ["Seven Network", "Network 10", "ABC Australia"],
        "d": 3
    },
    {
        "q": "In which season of Friends did the series experience its lowest overall average Nielsen rank (#5 overall)?",
        "correct": "Season 6 and Season 7 (both ranked #5)",
        "distractors": ["Season 1 and Season 2", "Season 3 and Season 4", "Season 9 and Season 10"],
        "d": 3
    },
    {
        "q": "How many episodes of Friends were filmed in an extended supersized format ('super-sized' 40-minute episodes) for sweeps?",
        "correct": "Several episodes in Season 7 and Season 9",
        "distractors": ["None, every episode was strictly 22 minutes", "Every episode in Season 10", "Only the Thanksgiving episodes"],
        "d": 2
    },
    {
        "q": "What programming gimmick did NBC use during February 2001 sweeps by expanding Friends episodes to 40 minutes?",
        "correct": "\"Super-Sized Thursdays\"",
        "distractors": ["\"Mega Comedy Night\"", "\"Expanded Must See TV\"", "\"Friends Extra Large\""],
        "d": 2
    },
    {
        "q": "What was the first episode of Friends to air in the 'super-sized' 40-minute format?",
        "correct": "\"The One with Joey's New Brain\"",
        "distractors": ["\"The One with the Holiday Armadillo\"", "\"The One Where They All Turn Thirty\"", "\"The One with All the Cheesecakes\""],
        "d": 3
    },
    {
        "q": "In what broadcast season did Friends surpass 'ER' as NBC's highest-rated program of the week?",
        "correct": "2001–2002 (Season 8)",
        "distractors": ["1996–1997 (Season 3)", "1998–1999 (Season 5)", "2003–2004 (Season 10)"],
        "d": 2
    },
    {
        "q": "What tragic real-world event in autumn 2001 led viewers to turn heavily to Friends for comfort, boosting Season 8 ratings to #1?",
        "correct": "The September 11 terrorist attacks in New York City",
        "distractors": ["The bursting of the dot-com stock market bubble", "The Northeast blackout of 2003", "The 2000 presidential election recount"],
        "d": 1
    },
    {
        "q": "What storyline was hastily removed and re-shot from Season 8 Episode 3 following the September 11 attacks?",
        "correct": "Chandler joking about airport security and bombs while boarding a honeymoon flight",
        "distractors": ["Joey accidentally setting off an emergency fire sprinkler system", "Ross getting trapped inside a collapsing subway tunnel", "Phoebe getting arrested for protesting at City Hall"],
        "d": 1
    },
    {
        "q": "What tribute message appeared at the end of the Season 8 premiere 'The One After 'I Do''?",
        "correct": "\"Dedicated to the People of New York City\"",
        "distractors": ["\"In Memory of Our Fallen Heroes\"", "\"We Love New York Always\"", "\"To the Firefighters and Police of Manhattan\""],
        "d": 1
    },
    {
        "q": "What item displayed behind the door in Chandler and Joey's apartment frequently displayed supportive NYC messages post-9/11?",
        "correct": "The Magna Doodle drawing board",
        "distractors": ["The bathroom mirror", "The refrigerator chalkboard", "The cork bulletin board"],
        "d": 1
    },
    {
        "q": "Who was responsible for drawing the famous changing sketches on the Magna Doodle on the back of Joey and Chandler's door?",
        "correct": "Crew member Paul Swain (art department)",
        "distractors": ["David Schwimmer", "Matt LeBlanc", "Creator David Crane"],
        "d": 3
    },
    {
        "q": "What was the estimated total domestic syndication revenue generated by Friends by its 10th anniversary in 2004?",
        "correct": "Over $1 billion",
        "distractors": ["$250 million", "$500 million", "$100 million"],
        "d": 2
    },
    {
        "q": "How much residual income does each of the six main cast members reportedly continue to earn annually from syndication and streaming?",
        "correct": "Approximately $20 million per year",
        "distractors": ["Approximately $2 million per year", "Approximately $50 million per year", "Approximately $500,000 per year"],
        "d": 1
    },
    {
        "q": "What percentage of Warner Bros.' syndication and backend profits do each of the six cast members reportedly receive under their contract?",
        "correct": "2 percent each",
        "distractors": ["0.5 percent each", "5 percent each", "10 percent each"],
        "d": 3
    },
    {
        "q": "What episode was originally broadcast on February 1, 1996, directly following 'The One After the Superbowl'?",
        "correct": "\"The One with the Prom Video\"",
        "distractors": ["\"The One Where Ross Finds Out\"", "\"The One with the Two Parties\"", "\"The One Where Dr. Ramoray Dies\""],
        "d": 2
    },
    {
        "q": "What television rating system code was Friends typically designated under the TV Parental Guidelines implemented in 1997?",
        "correct": "TV-14 (often with D for dialogue and S for sexual situations)",
        "distractors": ["TV-PG", "TV-G", "TV-MA"],
        "d": 2
    },
    {
        "q": "What was the title of the special two-part episode set in Las Vegas that concluded Season 5 in May 1999?",
        "correct": "\"The One in Vegas\" (Parts 1 & 2)",
        "distractors": ["\"The One with the Casino Wedding\"", "\"The One at Caesar's Palace\"", "\"The One with the Hand Twin\""],
        "d": 2
    },
    {
        "q": "What was the title of the two-part Season 4 finale set abroad in the United Kingdom?",
        "correct": "\"The One with Ross's Wedding\" (Parts 1 & 2)",
        "distractors": ["\"The One in London\"", "\"The One Where Ross Marries Emily\"", "\"The One with London, Baby!\""],
        "d": 1
    },
    {
        "q": "What was the title of the Season 9 two-part finale set in a Caribbean resort?",
        "correct": "\"The One in Barbados\" (Parts 1 & 2)",
        "distractors": ["\"The One in the Tropics\"", "\"The One with the Paleontology Conference\"", "\"The One with the Frizzy Hair\""],
        "d": 1
    },
    {
        "q": "How many total two-part (hour-long) season finale episodes did Friends produce across its ten seasons?",
        "correct": "Five season finales (Seasons 4, 5, 8, 9, and 10)",
        "distractors": ["All ten season finales", "Only two season finales (Seasons 4 and 10)", "Seven season finales"],
        "d": 3
    },
    {
        "q": "What was the average Nielsen viewer rating for Season 3 of Friends (1996–1997)?",
        "correct": "25.8 million viewers",
        "distractors": ["19.5 million viewers", "31.2 million viewers", "14.8 million viewers"],
        "d": 2
    },
    {
        "q": "What Fox prime-time teen drama competed directly against Friends at 8:00 PM on Thursdays during the mid-1990s?",
        "correct": "'Martin' and later 'Living Single'",
        "distractors": ["'Beverly Hills 90210'", "'The X-Files'", "'That '70s Show'"],
        "d": 3
    },
    {
        "q": "What was the average weekly audience for Season 4 of Friends (1997–1998)?",
        "correct": "24.7 million viewers",
        "distractors": ["18.1 million viewers", "30.4 million viewers", "35.2 million viewers"],
        "d": 2
    },
    {
        "q": "What milestone broadcast episode marked the 100th episode of Friends in autumn 1998?",
        "correct": "\"The One with the Triplets\" (Season 5, Episode 3)",
        "distractors": ["\"The One with the Thanksgiving Flashbacks\"", "\"The One with Ross's Wedding\"", "\"The One Where Everybody Finds Out\""],
        "d": 2
    },
    {
        "q": "What milestone broadcast episode marked the 200th episode of Friends in November 2002?",
        "correct": "\"The One with the Male Nanny\" (Season 9, Episode 6)",
        "distractors": ["\"The One with the Mugging\"", "\"The One Where Rachel Has a Baby\"", "\"The One with Rachel's Other Sister\""],
        "d": 2
    },
    {
        "q": "What milestone broadcast episode marked the 150th episode of Friends in early 2001?",
        "correct": "\"The One with Joey's New Brain\" (Season 7, Episode 15)",
        "distractors": ["\"The One with All the Cheesecakes\"", "\"The One with the Nap Partners\"", "\"The One with the Holiday Armadillo\""],
        "d": 3
    },
    {
        "q": "Which season of Friends had the highest season-long average rating rank (#1)?",
        "correct": "Season 8",
        "distractors": ["Season 2", "Season 5", "Season 10"],
        "d": 1
    },
    {
        "q": "What is the only season of Friends where the series finale was NOT the highest-rated episode of that particular season?",
        "correct": "Season 2 (where 'The One After the Superbowl' was highest)",
        "distractors": ["Season 1", "Season 8", "Season 5"],
        "d": 3
    },
    {
        "q": "How many total episodes of Friends did NBC broadcast during its inaugural 1994–1995 freshman season?",
        "correct": "24 episodes",
        "distractors": ["22 episodes", "26 episodes", "18 episodes"],
        "d": 2
    },
    {
        "q": "How many total episodes comprise Season 2 (1995–1996)?",
        "correct": "24 episodes",
        "distractors": ["22 episodes", "25 episodes", "26 episodes"],
        "d": 2
    },
    {
        "q": "How many total episodes comprise Season 3 (1996–1997)?",
        "correct": "25 episodes",
        "distractors": ["22 episodes", "24 episodes", "28 episodes"],
        "d": 3
    },
    {
        "q": "How many total episodes comprise Season 4 (1997–1998)?",
        "correct": "24 episodes",
        "distractors": ["22 episodes", "23 episodes", "26 episodes"],
        "d": 2
    },
    {
        "q": "How many total episodes comprise Season 5 (1998–1999)?",
        "correct": "24 episodes",
        "distractors": ["22 episodes", "25 episodes", "26 episodes"],
        "d": 2
    },
    {
        "q": "How many total episodes comprise Season 6 (1999–2000)?",
        "correct": "25 episodes",
        "distractors": ["22 episodes", "24 episodes", "26 episodes"],
        "d": 3
    },
    {
        "q": "How many total episodes comprise Season 7 (2000–2001)?",
        "correct": "24 episodes",
        "distractors": ["22 episodes", "23 episodes", "25 episodes"],
        "d": 2
    },
    {
        "q": "How many total episodes comprise Season 8 (2001–2002)?",
        "correct": "24 episodes",
        "distractors": ["22 episodes", "25 episodes", "26 episodes"],
        "d": 2
    },
    {
        "q": "How many total episodes comprise Season 9 (2002–2003)?",
        "correct": "24 episodes",
        "distractors": ["22 episodes", "23 episodes", "25 episodes"],
        "d": 2
    },
    {
        "q": "How many total episodes comprise Season 10 (2003–2004)?",
        "correct": "18 episodes (including the two-part finale)",
        "distractors": ["20 episodes", "16 episodes", "22 episodes"],
        "d": 1
    },
    {
        "q": "What British digital multichannel station launched in 2001 by Channel 4 frequently broadcast Friends reruns non-stop?",
        "correct": "E4",
        "distractors": ["BBC Three", "ITV2", "Dave"],
        "d": 2
    },
    {
        "q": "What format was Friends originally shot in on 35mm film that allowed for later remastering in 16:9 widescreen HD?",
        "correct": "35mm color film (3-perf Super 35)",
        "distractors": ["Standard definition Betacam SP videotape", "Multi-camera 16mm reversal film", "High-definition digital video tape"],
        "d": 2
    },
    {
        "q": "In what year were all 236 episodes of Friends officially remastered in 1080p high definition and released on Blu-ray?",
        "correct": "2012",
        "distractors": ["2006", "2009", "2015"],
        "d": 2
    },
    {
        "q": "What aspect ratio was Friends originally framed and broadcast in during its 1994–2004 network run?",
        "correct": "4:3 fullscreen standard definition",
        "distractors": ["16:9 anamorphic widescreen", "1.85:1 theatrical widescreen", "2.35:1 cinemascope"],
        "d": 1
    },
    {
        "q": "What unintended visual artifact became noticeable on the sides of the screen after Friends was remastered into 16:9 widescreen?",
        "correct": "Stand-in body doubles, lighting equipment, and crew members",
        "distractors": ["Boom microphones dropping from the ceiling", "Script binders left on the orange couch", "Visible studio cameras in wide shots"],
        "d": 2
    },
    {
        "q": "What specific body double swap is famously visible on the right side of the screen in 'The One with the Mugging' in widescreen?",
        "correct": "An obvious stand-in double for Rachel Green",
        "distractors": ["A male stand-in double for Monica Geller", "A crew member holding a cue card for Joey", "A dummy replacing Chandler Bing"],
        "d": 2
    },
    {
        "q": "Which major television guide magazine named Friends the #5 Best TV Show of All Time in a 2013 retrospective list?",
        "correct": "TV Guide",
        "distractors": ["Rolling Stone", "Entertainment Weekly", "Time Magazine"],
        "d": 2
    },
    {
        "q": "What prestigious television industry award did Friends win in 2002 for Outstanding Comedy Series?",
        "correct": "Primetime Emmy Award",
        "distractors": ["Peabody Award", "BAFTA TV Award", "Television Critics Association Heritage Award"],
        "d": 1
    },
    {
        "q": "How many total Primetime Emmy Award nominations did Friends accumulate over its ten seasons?",
        "correct": "62 nominations",
        "distractors": ["45 nominations", "78 nominations", "112 nominations"],
        "d": 2
    },
    {
        "q": "How many total Primetime Emmy Awards did Friends win throughout its run?",
        "correct": "6 Emmy Awards",
        "distractors": ["12 Emmy Awards", "18 Emmy Awards", "2 Emmy Awards"],
        "d": 2
    },
    {
        "q": "What was the title of the official Friends soundtrack album released by Reprise Records in autumn 1995?",
        "correct": "'Friends (Music from the TV Series)'",
        "distractors": ["'Songs from Central Perk'", "'I'll Be There for You: The Central Perk Collection'", "'Must See Music: Friends Volume 1'"],
        "d": 2
    },
    {
        "q": "What RIAA sales certification did the 1995 Friends official soundtrack album achieve in the United States?",
        "correct": "Double Platinum (over 2 million copies sold)",
        "distractors": ["Gold (500,000 copies)", "Platinum (1 million copies)", "Diamond (10 million copies)"],
        "d": 3
    }
]

if __name__ == "__main__":
    out_path = os.path.join(os.path.dirname(__file__), "staging", "friends_batch5.json")
    build_batch(questions, out_path, batch_num=5)
