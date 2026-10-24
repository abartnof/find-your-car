#!/usr/bin/env python3
"""
Generate Batch 7: Metatextual: Television Industry, Lineups, Ratings Battles, Theme Songs & Syndication (100 questions)
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from sitcom_builder import make_batch

q_batch7 = [
    # NBC 'Must See TV' Thursday Block (25 questions)
    {
        "q": "What promotional branding slogan did NBC famously use throughout the 1990s to market its dominant Thursday night comedy programming block?",
        "correct": "Must See TV",
        "distractors": ["Comedy Central Thursday", "Super Thursday Comedy", "The Primetime Power Hour"],
        "d": 1
    },
    {
        "q": "Which legendary NBC entertainment president coined and championed the 'Must See TV' campaign during the network's 1990s dominance?",
        "correct": "Warren Littlefield",
        "distractors": ["Brandon Tartikoff", "Grant Tinker", "Jeff Zucker"],
        "d": 2
    },
    {
        "q": "In the fall of 1993, which critically acclaimed hit moved to Thursdays at 9:00 PM, anchoring NBC's schedule after Cheers concluded?",
        "correct": "Seinfeld",
        "distractors": ["Frasier", "Mad About You", "Wings"],
        "d": 1
    },
    {
        "q": "What phenomenon occurred in television ratings when Seinfeld aired its series finale on May 14, 1998?",
        "correct": "It drew an estimated 76.3 million viewers, making it one of the most-watched entertainment broadcasts in American history",
        "distractors": ["It was the first television finale watched by over 120 million viewers", "It drew lower ratings than a regular mid-season episode due to a West Coast blackout", "It tied the M*A*S*H finale as the highest-rated broadcast ever"],
        "d": 1
    },
    {
        "q": "How much did a 30-second commercial spot cost advertisers during the Seinfeld series finale in May 1998?",
        "correct": "$1.5 million to $1.7 million (comparable to the Super Bowl)",
        "distractors": ["$400,000", "$750,000", "$3.5 million"],
        "d": 2
    },
    {
        "q": "What was the legendary 1996-1997 NBC Thursday night comedy schedule known as the peak of 'Must See TV'?",
        "correct": "Friends (8:00), The Single Guy (8:30), Seinfeld (9:00), Suddenly Susan (9:30), followed by ER (10:00)",
        "distractors": ["Mad About You (8:00), Wings (8:30), Frasier (9:00), NewsRadio (9:30), followed by Law & Order", "The Fresh Prince (8:00), Blossom (8:30), Seinfeld (9:00), Just Shoot Me! (9:30), followed by ER", "Friends (8:00), Boston Common (8:30), Frasier (9:00), Caroline in the City (9:30), followed by Homicide"],
        "d": 2
    },
    {
        "q": "What term did television critics and industry executives give to the vulnerable 8:30 PM and 9:30 PM slots sandwiched between Friends and Seinfeld?",
        "correct": "The 'hammock' slots (guaranteed top-10 ratings regardless of show quality)",
        "distractors": ["The velvet cushion", "The golden springboard", "The slipstream slot"],
        "d": 2
    },
    {
        "q": "Which sitcom starring Brooke Shields was placed in the coveted 9:30 PM post-Seinfeld hammock slot in 1996 and debuted at #3 in the Nielsen ratings?",
        "correct": "Suddenly Susan",
        "distractors": ["The Naked Truth", "Caroline in the City", "Fired Up"],
        "d": 2
    },
    {
        "q": "Which sitcom starring Lea Thompson was launched into the Thursday night post-Seinfeld slot in 1995, instantly reaching the Nielsen top 5?",
        "correct": "Caroline in the City",
        "distractors": ["Suddenly Susan", "Hope & Gloria", "The Single Guy"],
        "d": 2
    },
    {
        "q": "Why was moving Frasier away from Thursday night to Tuesday at 9:00 PM in 1994 considered a massive strategic gamble for NBC?",
        "correct": "It went head-to-head against ABC's #1 rated juggernaut Home Improvement",
        "distractors": ["Tuesday night was traditionally dominated by CBS murder mystery movies", "Frasier had suffered declining ratings in its first season on Thursday", "Affiliates in major markets threatened to preempt Tuesday comedy"],
        "d": 2
    },
    {
        "q": "In the historic 1994-1995 Tuesday 9:00 PM ratings clash, what was the outcome between Frasier and Home Improvement?",
        "correct": "Home Improvement retained the overall viewership lead, but Frasier captured the high-income 18-49 demographic and critical acclaim",
        "distractors": ["Frasier crushed Home Improvement, causing ABC to move Tim Allen to Friday", "Home Improvement dropped out of the top 30 entirely", "Both shows were cancelled at the end of the season due to cannibalized ratings"],
        "d": 2
    },
    {
        "q": "What medical drama followed NBC's Thursday night comedy block at 10:00 PM, anchoring the highest-grossing night in network history?",
        "correct": "ER",
        "distractors": ["Chicago Hope", "NYPD Blue", "Law & Order"],
        "d": 1
    },
    {
        "q": "What record syndication revenue did Seinfeld generate when Columbia TriStar sold off-network reruns to local broadcast stations in 1998?",
        "correct": "Over $1.7 billion, making it the most lucrative syndication deal in television history",
        "distractors": ["$450 million", "$800 million", "$3.5 billion"],
        "d": 2
    },
    {
        "q": "What unusual ratings distinction did Seinfeld achieve in its final season (1997-1998)?",
        "correct": "It finished the season as the #1 show on television, joining I Love Lucy and The Andy Griffith Show as the only shows to bow out on top",
        "distractors": ["It was the first show to win every single Emmy category for which it was nominated", "It scored higher ratings on West Coast reruns than live East Coast broadcasts", "It drew more teenage viewers than all Saturday morning cartoons combined"],
        "d": 2
    },
    {
        "q": "Which executive succeeded Warren Littlefield as NBC Entertainment President in 1998, overseeing the final seasons of Seinfeld and the rise of Will & Grace?",
        "correct": "Scott Sassa (and later Jeff Zucker)",
        "distractors": ["Garth Ancier", "Les Moonves", "Peter Chernin"],
        "d": 3
    },
    {
        "q": "What was the promotional label given to NBC's Tuesday night comedy programming in the mid-1990s featuring 3rd Rock from the Sun and Frasier?",
        "correct": "Frasier Tuesday / 3rd Rock Tuesday ('Must See Tuesday')",
        "distractors": ["Super Tuesday Laughs", "Alien Comedy Night", "The Comedy Powerhouse"],
        "d": 3
    },
    {
        "q": "Which critically acclaimed, low-rated sitcom was shuffled to more than 11 different time slots across five seasons by NBC executives?",
        "correct": "NewsRadio",
        "distractors": ["Mad About You", "Wings", "Just Shoot Me!"],
        "d": 2
    },
    {
        "q": "In 1998, which groundbreaking sitcom joined NBC's Thursday lineup and became the cultural successor to Seinfeld?",
        "correct": "Will & Grace",
        "distractors": ["Scrubs", "The King of Queens", "Everybody Loves Raymond"],
        "d": 1
    },
    {
        "q": "Why did NBC executives fight aggressively to keep Seinfeld on Thursday nights despite early low test scores?",
        "correct": "Research showed Thursday night viewers had the highest disposable income for movie studios and retailers planning weekend shopping",
        "distractors": ["NBC's contract with General Electric mandated four New York-based sitcoms on Thursdays", "Jerry Seinfeld's agent held an ownership stake in NBC's advertising division", "Thursday was the only night that local affiliates did not demand syndicated game shows"],
        "d": 2
    },
    {
        "q": "What long-running NBC sitcom ended its eight-season run in May 1997 with a one-hour finale at Nantucket airport?",
        "correct": "Wings",
        "distractors": ["Cheers", "Night Court", "Mad About You"],
        "d": 2
    },
    {
        "q": "Which series served as the reliable 8:00 PM Thursday anchor for NBC before Friends premiered in 1994?",
        "correct": "Mad About You",
        "distractors": ["Wings", "The Cosby Show", "A Different World"],
        "d": 2
    },
    {
        "q": "Which popular Thursday night sitcom featured characters from Seinfeld, Friends, and Mad About You crossing over in the same NBC universe?",
        "correct": "Mad About You",
        "distractors": ["Wings", "NewsRadio", "The Single Guy"],
        "d": 2
    },
    {
        "q": "How many total Primetime Emmy Awards did Frasier win over its 11-season run, setting a long-standing record for a comedy series?",
        "correct": "37 Emmy Awards",
        "distractors": ["22 Emmy Awards", "45 Emmy Awards", "52 Emmy Awards"],
        "d": 2
    },
    {
        "q": "What major competitive advantage did NBC's Must See TV block hold over theatrical movies on Friday nights?",
        "correct": "Hollywood movie studios paid record advertising premiums on Thursdays to promote opening-weekend film releases",
        "distractors": ["Actors from NBC sitcoms were barred from appearing in Friday movie premieres", "Movie theaters offered discounts for showing Must See TV in their lobbies", "NBC owned half of the major cinema chains in North America"],
        "d": 2
    },
    {
        "q": "In what year did Friends premiere on NBC's Thursday night schedule, initially titled 'Friends Like Us' during development?",
        "correct": "1994",
        "distractors": ["1992", "1993", "1995"],
        "d": 1
    },

    # ABC TGIF Friday Block (20 questions)
    {
        "q": "What was the official name of ABC's iconic family-friendly Friday night television programming block launched in 1989?",
        "correct": "TGIF ('Thank Goodness It's Friday')",
        "distractors": ["Friday Night Fever", "Family Friday Fun", "ABC Weekend Kickoff"],
        "d": 1
    },
    {
        "q": "Which ABC executive is widely credited with conceptualizing and branding the TGIF lineup to capture child and family audiences?",
        "correct": "Jim Duffy",
        "distractors": ["Ted Harbert", "Brandon Stoddard", "Michael Eisner"],
        "d": 3
    },
    {
        "q": "What classic four-show lineup anchored TGIF during its absolute ratings peak in the 1991-1992 television season?",
        "correct": "Full House (8:00), Family Matters (8:30), Step by Step (9:00), and Perfect Strangers (9:30)",
        "distractors": ["Growing Pains (8:00), Dinosaurs (8:30), Hangin' with Mr. Cooper (9:00), Boy Meets World (9:30)", "Full House (8:00), Boy Meets World (8:30), Sabrina (9:00), Sister, Sister (9:30)", "Dinosaurs (8:00), Family Matters (8:30), Step by Step (9:00), Hangin' with Mr. Cooper (9:30)"],
        "d": 1
    },
    {
        "q": "What prolific television production company founded by Thomas L. Miller and Robert L. Boyett produced almost the entire TGIF lineup?",
        "correct": "Miller-Boyett Productions",
        "distractors": ["Carsey-Werner Productions", "Witt/Thomas/Harris Productions", "Tandem Productions"],
        "d": 2
    },
    {
        "q": "What unique promotional hosting format was used between commercials during the TGIF block?",
        "correct": "Stars of the TGIF shows hosted live-action comedy skits and behind-the-scenes segments in character",
        "distractors": ["Animated claymation characters introduced each broadcast", "Local news anchors delivered weekend weather forecasts", "Stand-up comedians performed five-minute routines"],
        "d": 1
    },
    {
        "q": "Which show debuted on TGIF in the fall of 1993 and went on to run for seven seasons, tracking characters from middle school to college?",
        "correct": "Boy Meets World",
        "distractors": ["Sister, Sister", "Smart Guy", "Hangin' with Mr. Cooper"],
        "d": 1
    },
    {
        "q": "In 1996, which supernatural teen comedy starring Melissa Joan Hart was added to TGIF, instantly becoming the block's highest-rated show?",
        "correct": "Sabrina the Teenage Witch",
        "distractors": ["Charmed", "Buffy the Vampire Slayer", "Teen Angel"],
        "d": 1
    },
    {
        "q": "In 1997, what major network raid disrupted the TGIF lineup when CBS invested $40 million to acquire two flagship Miller-Boyett sitcoms?",
        "correct": "CBS poached Family Matters and Step by Step to launch their own competing 'CBS Block Party'",
        "distractors": ["CBS purchased Full House and Boy Meets World for Sunday evenings", "CBS acquired Sabrina the Teenage Witch and Hangin' with Mr. Cooper", "CBS bought the rights to Dinosaurs to create a prime-time cartoon block"],
        "d": 2
    },
    {
        "q": "What was the ratings fate of CBS's 1997 Friday night 'Block Party' against ABC's revamped TGIF?",
        "correct": "It was a catastrophic failure; ratings plummeted, and both Family Matters and Step by Step were cancelled within a year",
        "distractors": ["It defeated TGIF soundly, leading ABC to abandon Friday comedy", "Both networks tied in viewers and shared syndication rights", "It was renewed for four additional seasons on CBS"],
        "d": 2
    },
    {
        "q": "Which high-concept, short-lived TGIF sitcom featured a teenager who dies from choking on an old hamburger and becomes a guardian angel?",
        "correct": "Teen Angel",
        "distractors": ["Meego", "Aliens in the Family", "You Wish"],
        "d": 2
    },
    {
        "q": "Which short-lived 1997 TGIF series starred Bronson Pinchot as a 9,000-year-old alien shape-shifter acting as a family nanny?",
        "correct": "Meego",
        "distractors": ["Teen Angel", "You Wish", "Brotherly Love"],
        "d": 2
    },
    {
        "q": "Which beloved 1992-1997 TGIF sitcom starred Mark Curry, Holly Robinson Peete, and Raven-Symoné?",
        "correct": "Hangin' with Mr. Cooper",
        "distractors": ["Roc", "In the House", "The Parent 'Hood"],
        "d": 1
    },
    {
        "q": "What animatronic puppet sitcom from Jim Henson Productions aired on TGIF from 1991 to 1994?",
        "correct": "Dinosaurs",
        "distractors": ["The Muppets Tonight", "Pee-wee's Playhouse", "Land of the Lost"],
        "d": 1
    },
    {
        "q": "In the 1990-1991 season, what percentage of American children ages 2 to 11 watching Friday night television were tuned into TGIF?",
        "correct": "Over 70% of viewing children",
        "distractors": ["Roughly 35%", "Just under 50%", "Nearly 95%"],
        "d": 3
    },
    {
        "q": "Which TGIF sitcom had its series finale in May 1995 after eight seasons, choosing not to move to the newly launched WB network?",
        "correct": "Full House",
        "distractors": ["Growing Pains", "Perfect Strangers", "Step by Step"],
        "d": 2
    },
    {
        "q": "What short-lived TGIF sitcom in 1997 starred John Ales as an ancient genie released by a single mother and her kids?",
        "correct": "You Wish",
        "distractors": ["Teen Angel", "Meego", "Free Spirit"],
        "d": 3
    },
    {
        "q": "Which musical duo composed the iconic theme songs for Full House, Family Matters, Step by Step, and Perfect Strangers?",
        "correct": "Jesse Frederick and Bennett Salvay",
        "distractors": ["Mike Post and Pete Carpenter", "Bill Bickford and Gary Portnoy", "Danny Elfman and Alf Clausen"],
        "d": 2
    },
    {
        "q": "What puppet character from The Muppets hosted a memorable TGIF cross-promotional special in 1996?",
        "correct": "Kermit the Frog",
        "distractors": ["Fozzie Bear", "Miss Piggy", "Gonzo"],
        "d": 2
    },
    {
        "q": "Which sitcom featuring Tia and Tamera Mowry was dropped from TGIF after two seasons before finding massive success on The WB?",
        "correct": "Sister, Sister",
        "distractors": ["Smart Guy", "Moesha", "Clueless"],
        "d": 1
    },
    {
        "q": "In what year did ABC officially retire the original classic run of the TGIF brand before later short-lived revivals?",
        "correct": "2000",
        "distractors": ["1997", "1998", "2003"],
        "d": 2
    },

    # FOX, The WB, and UPN Comedy Revolutions (20 questions)
    {
        "q": "What bold scheduling move did Fox make in the fall of 1990 that shocked the television industry?",
        "correct": "Moving The Simpsons to Thursdays at 8:00 PM to challenge TV's #1 show, The Cosby Show",
        "distractors": ["Moving Married... with Children to Monday Night Football's time slot", "Airing In Living Color live against Saturday Night Live", "Moving Beverly Hills, 90210 against 60 Minutes on Sundays"],
        "d": 2
    },
    {
        "q": "Which Fox sitcom became the longest-running live-action sitcom in the network's history, airing from 1987 to 1997?",
        "correct": "Married... with Children",
        "distractors": ["Martin", "Living Single", "Herman's Head"],
        "d": 1
    },
    {
        "q": "What two new commercial broadcast networks launched in January 1995, building their initial audiences on Black sitcoms and teen dramas?",
        "correct": "The WB and UPN",
        "distractors": ["Fox and The CW", "PAX TV and FX", "Paramount Network and WB Network"],
        "d": 1
    },
    {
        "q": "What was the flagship sitcom broadcast on UPN's historic launch night on January 16, 1995?",
        "correct": "Star Trek: Voyager (drama) paired with the sitcom Platypus Man / Pig Sty",
        "distractors": ["Moesha", "The Parkers", "Malcolm & Eddie"],
        "d": 3
    },
    {
        "q": "What was the flagship launch sitcom for The WB on January 11, 1995, starring Shawn and Marlon Wayans?",
        "correct": "The Wayans Bros.",
        "distractors": ["Sister, Sister", "The Jamie Foxx Show", "Smart Guy"],
        "d": 1
    },
    {
        "q": "What was the animated mascot of The WB network who greeted viewers with a top hat and cane, singing 'Hello My Baby'?",
        "correct": "Michigan J. Frog",
        "distractors": ["Bugs Bunny", "Daffy Duck", "Porky Pig"],
        "d": 1
    },
    {
        "q": "Which Fox Sunday night sitcom in 1990 sparked a nationwide conservative boycott campaign led by Michigan activist Terry Rakolta?",
        "correct": "Married... with Children",
        "distractors": ["The Simpsons", "Parker Lewis Can't Lose", "In Living Color"],
        "d": 2
    },
    {
        "q": "What was the ironic result of Terry Rakolta's advertiser boycott against Married... with Children?",
        "correct": "Massive national media coverage caused ratings to skyrocket, cementing the show as a cultural hit",
        "distractors": ["Fox cancelled the show after four episodes", "The FCC fined Fox $5 million for indecency", "Every corporate sponsor permanently pulled advertising"],
        "d": 2
    },
    {
        "q": "What groundbreaking Fox sketch and comedy series launched the careers of Jim Carrey, Jamie Foxx, and the Wayans family?",
        "correct": "In Living Color",
        "distractors": ["Mad TV", "The Edge", "House of Buggin'"],
        "d": 1
    },
    {
        "q": "What counter-programming stunt did Fox execute during CBS's Super Bowl XXVI halftime show in January 1992?",
        "correct": "Broadcasting a live special episode of In Living Color with a live countdown clock, poaching 22 million viewers",
        "distractors": ["Airing the world premiere of The Simpsons music video 'Do the Bartman'", "Broadcasting an uncensored episode of Married... with Children", "Airing a live stand-up special featuring Martin Lawrence"],
        "d": 2
    },
    {
        "q": "What was the direct consequence of Fox's Super Bowl halftime counter-programming stunt in 1992?",
        "correct": "The NFL began booking world-class superstar concerts (beginning with Michael Jackson in 1993) to prevent viewer defection",
        "distractors": ["The FCC banned alternative programming during major sporting events", "CBS refused to broadcast the Super Bowl for the next decade", "Fox was sued for broadcast signal interference"],
        "d": 2
    },
    {
        "q": "In 1993, what seismic sports rights deal allowed Fox to shake off its 'fringe network' status and poach dozens of CBS affiliate stations?",
        "correct": "Fox outbid CBS with a staggering $1.58 billion contract to broadcast NFL NFC football games",
        "distractors": ["Fox secured exclusive rights to Major League Baseball postseason", "Fox signed a 10-year deal for NBA basketball", "Fox purchased exclusive rights to the Olympic Games"],
        "d": 2
    },
    {
        "q": "Which Fox sitcom starred Corin Nemec as a cool, Ferris Bueller-esque high schooler who coordinated operations from his high-tech locker?",
        "correct": "Parker Lewis Can't Lose",
        "distractors": ["Ferris Bueller (the series)", "Get a Life", "Flying Blind"],
        "d": 2
    },
    {
        "q": "What bizarre, surreal sitcom starring Chris Elliott aired on Fox from 1990 to 1992, featuring a 30-year-old paperboy who lived with his parents?",
        "correct": "Get a Life",
        "distractors": ["Ned and Stacey", "Down the Shore", "Bakersfield P.D."],
        "d": 2
    },
    {
        "q": "Which UPN sitcom starring Brandy Norwood became the network's longest-running and highest-rated comedy of the 1990s?",
        "correct": "Moesha",
        "distractors": ["Sister, Sister", "The Parkers", "Girlfriends"],
        "d": 1
    },
    {
        "q": "What night of the week was anchored by The WB's African American sitcom block featuring Sister, Sister, The Wayans Bros., and The Jamie Foxx Show?",
        "correct": "Wednesday night",
        "distractors": ["Monday night", "Thursday night", "Friday night"],
        "d": 2
    },
    {
        "q": "What night of the week did UPN designate for its comedy lineup featuring Moesha, In the House, and Malcolm & Eddie?",
        "correct": "Monday night",
        "distractors": ["Tuesday night", "Wednesday night", "Friday night"],
        "d": 2
    },
    {
        "q": "What Fox sitcom set in Detroit starred Martin Lawrence and anchored Fox's successful Thursday night urban comedy expansion?",
        "correct": "Martin",
        "distractors": ["Roc", "Living Single", "South Central"],
        "d": 1
    },
    {
        "q": "In 1993, which Fox comedy starring Queen Latifah proved that an ensemble cast of four professional Black women could achieve mainstream ratings success?",
        "correct": "Living Single",
        "distractors": ["Moesha", "Sister, Sister", "The Parent 'Hood"],
        "d": 1
    },
    {
        "q": "What parent company owned and operated the UPN network throughout its 1990s run?",
        "correct": "Paramount Communications (later Viacom) and Chris-Craft Industries",
        "distractors": ["Time Warner", "General Electric", "The Walt Disney Company"],
        "d": 2
    },

    # Emmy Awards & Ratings History (15 questions)
    {
        "q": "Which sitcom holds the all-time record for the most consecutive Primetime Emmy Awards for Outstanding Comedy Series, winning five from 1994 to 1998?",
        "correct": "Frasier",
        "distractors": ["Seinfeld", "Cheers", "Modern Family"],
        "d": 1
    },
    {
        "q": "In which single year did Seinfeld win the Primetime Emmy Award for Outstanding Comedy Series?",
        "correct": "1993 (Season 4, 'The Contest' season)",
        "distractors": ["1991", "1995", "1998"],
        "d": 2
    },
    {
        "q": "How many Primetime Emmy Awards for Outstanding Lead Actor in a Comedy Series did Kelsey Grammer win as Frasier Crane during the 1990s?",
        "correct": "Three (1994, 1995, 1998, with a fourth in 2004)",
        "distractors": ["One", "Two", "Five"],
        "d": 2
    },
    {
        "q": "Which actress won four Primetime Emmy Awards for Outstanding Lead Actress in a Comedy Series during the 1990s for Mad About You?",
        "correct": "Helen Hunt",
        "distractors": ["Candice Bergen", "Patricia Heaton", "Julia Louis-Dreyfus"],
        "d": 2
    },
    {
        "q": "Which actress won three consecutive Primetime Emmy Awards for Outstanding Supporting Actress in a Comedy Series for Roseanne (1992, 1993, 1994)?",
        "correct": "Laurie Metcalf",
        "distractors": ["Julia Louis-Dreyfus", "Christine Baranski", "Faith Ford"],
        "d": 2
    },
    {
        "q": "In what year did Julia Louis-Dreyfus win her sole Primetime Emmy Award for Outstanding Supporting Actress for playing Elaine Benes?",
        "correct": "1996",
        "distractors": ["1993", "1994", "1998"],
        "d": 3
    },
    {
        "q": "Which actor won the Primetime Emmy Award for Outstanding Lead Actor in a Comedy Series in 1993 for Cheers' final season, beating Jerry Seinfeld?",
        "correct": "Ted Danson",
        "distractors": ["Craig T. Nelson", "John Goodman", "Garry Shandling"],
        "d": 3
    },
    {
        "q": "Which actor was nominated seven consecutive times for Outstanding Supporting Actor in a Comedy Series for playing George Costanza on Seinfeld, but never won?",
        "correct": "Jason Alexander",
        "distractors": ["Michael Richards", "David Hyde Pierce", "Peter Boyle"],
        "d": 2
    },
    {
        "q": "How many Primetime Emmy Awards for Outstanding Supporting Actor in a Comedy Series did Michael Richards win for playing Cosmo Kramer?",
        "correct": "Three (1993, 1994, 1997)",
        "distractors": ["One", "Two", "Four"],
        "d": 2
    },
    {
        "q": "Which show won the Primetime Emmy Award for Outstanding Comedy Series in 1992, defeating Brooklyn Bridge, Cheers, Home Improvement, and Seinfeld?",
        "correct": "Murphy Brown",
        "distractors": ["Roseanne", "Wings", "The Larry Sanders Show"],
        "d": 3
    },
    {
        "q": "Which show concluded the 1993-1994 television season as the #1 most-watched program in the Nielsen ratings with a 21.9 rating?",
        "correct": "Home Improvement",
        "distractors": ["Seinfeld", "Roseanne", "60 Minutes"],
        "d": 2
    },
    {
        "q": "In the 1989-1990 Nielsen season ratings, which ABC blue-collar comedy finished at #2 in the nation, trailing only The Cosby Show?",
        "correct": "Roseanne",
        "distractors": ["Full House", "Family Matters", "Cheers"],
        "d": 2
    },
    {
        "q": "Which late-night satire series received 56 Emmy nominations across its run on HBO, making history for cable television?",
        "correct": "The Larry Sanders Show",
        "distractors": ["Dream On", "Mr. Show", "Arliss"],
        "d": 2
    },
    {
        "q": "In 1999, which Fox live-action sitcom won the Primetime Emmy Award for Outstanding Comedy Series, becoming the only animated series nominated in modern times?",
        "correct": "The Simpsons (nominated in 1993 for comedy writing, but Ally McBeal won Comedy Series in 1999)",
        "distractors": ["King of the Hill", "Futurama", "Family Guy"],
        "d": 3
    },
    {
        "q": "How many total Emmy nominations did John Goodman receive for playing Dan Conner on Roseanne without ever winning?",
        "correct": "Seven nominations",
        "distractors": ["Three nominations", "Five nominations", "Nine nominations"],
        "d": 2
    },

    # Theme Songs, Composers, and Chart Performance (20 questions)
    {
        "q": "Which American pop rock duo recorded the iconic Friends theme song 'I'll Be There for You'?",
        "correct": "The Rembrandts",
        "distractors": ["Toad the Wet Sprocket", "Gin Blossoms", "Semisonic"],
        "d": 1
    },
    {
        "q": "What incredible radio chart milestone did The Rembrandts' 'I'll Be There for You' achieve in 1995?",
        "correct": "It reached #1 on the Billboard Hot 100 Airplay chart and stayed there for eight consecutive weeks",
        "distractors": ["It sold 10 million physical CD singles in the US alone", "It won the Grammy Award for Record of the Year", "It was the first song streamed 1 million times on the internet"],
        "d": 2
    },
    {
        "q": "Who performed the iconic hip-hop theme song for The Fresh Prince of Bel-Air?",
        "correct": "DJ Jazzy Jeff & The Fresh Prince",
        "distractors": ["Run-D.M.C.", "Heavy D & the Boyz", "Kid 'n Play"],
        "d": 1
    },
    {
        "q": "What jazz bassist and composer created the instantly recognizable, slap-bass transitions and theme music for Seinfeld?",
        "correct": "Jonathan Wolff",
        "distractors": ["Marcus Miller", "Stanley Clarke", "Flea"],
        "d": 2
    },
    {
        "q": "How did Jonathan Wolff customize the Seinfeld slap-bass riffs for each individual episode?",
        "correct": "He improvised and re-recorded the bass lines and mouth pops to match the cadence of Jerry's opening stand-up comedy monologue",
        "distractors": ["He adjusted the musical pitch according to which character entered first", "He matched the tempo to the speed of the New York subway line shown in the establishing shot", "He played the track backwards during the closing credits"],
        "d": 2
    },
    {
        "q": "What was the title and performer of the bouncy, swing-style closing theme song on Frasier?",
        "correct": "'Tossed Salads and Scrambled Eggs', sung by Kelsey Grammer",
        "distractors": ["'Coffee in the Rain', sung by David Hyde Pierce", "'Seattle Calling', sung by Bruce Miller", "'The Doctor is In', sung by John Mahoney"],
        "d": 1
    },
    {
        "q": "What do the cryptic lyrics 'tossed salads and scrambled eggs' actually refer to in Frasier's theme song?",
        "correct": "Metaphors for the mixed-up, neurotic psychological problems of the radio callers",
        "distractors": ["Frasier's favorite gourmet breakfast recipe from Le Cordon Bleu", "The chaotic mess Martin's dog Eddie made in the kitchen", "The scrambled nature of AM radio broadcast signals in the Pacific Northwest"],
        "d": 2
    },
    {
        "q": "Who wrote and performed the bluesy opening saxophone and harmonica theme song for Roseanne?",
        "correct": "Dan Foliart and Howard Pearl (featuring John Popper on harmonica in Season 9)",
        "distractors": ["Clarence Clemons", "Branford Marsalis", "Kenny G"],
        "d": 3
    },
    {
        "q": "What alt-rock band recorded the infectious power-pop anthem 'Cleveland Rocks' used as the theme for The Drew Carey Show?",
        "correct": "The Presidents of the United States of America",
        "distractors": ["Smash Mouth", "Sugar Ray", "Harvey Danger"],
        "d": 1
    },
    {
        "q": "Who originally wrote and recorded 'Cleveland Rocks' in 1979 before it was covered for The Drew Carey Show?",
        "correct": "Ian Hunter (former lead singer of Mott the Hoople)",
        "distractors": ["Alice Cooper", "Michael Stanley", "Bob Seger"],
        "d": 2
    },
    {
        "q": "Who performed the theme song 'Everywhere You Look' for ABC's Full House?",
        "correct": "Jesse Frederick",
        "distractors": ["John Stamos", "Gary Portnoy", "Bennett Salvay"],
        "d": 1
    },
    {
        "q": "What popular 1980s R&B song by Boyz II Men was adapted by the group to serve as a recurring a cappella performance on The Fresh Prince?",
        "correct": "'It's So Hard to Say Goodbye to Yesterday'",
        "distractors": ["'End of the Road'", "'Motownphilly'", "'I'll Make Love to You'"],
        "d": 2
    },
    {
        "q": "What alternative rock band recorded 'Boss of Me', the frenetic theme song for Malcolm in the Middle in late 1999?",
        "correct": "They Might Be Giants",
        "distractors": ["Barenaked Ladies", "Ween", "Cake"],
        "d": 2
    },
    {
        "q": "What legendary New Orleans musician performed the funky piano theme song 'My Opinionation' for Blossom?",
        "correct": "Dr. John",
        "distractors": ["Professor Longhair", "Fats Domino", "Allen Toussaint"],
        "d": 2
    },
    {
        "q": "Who composed the pastoral acoustic guitar and whistling theme song for Northern Exposure?",
        "correct": "David Schwartz",
        "distractors": ["Mark Snow", "Stewart Copeland", "W.G. Snuffy Walden"],
        "d": 3
    },
    {
        "q": "What R&B supergroup composed and performed the vocal theme for Sister, Sister in its early seasons?",
        "correct": "Tia and Tamera Mowry themselves (singing 'Sister, Sister, talk about a two-way tolerance...')",
        "distractors": ["TLC", "En Vogue", "SWV"],
        "d": 2
    },
    {
        "q": "What hip-hop pioneer performed the opening theme song for Martin?",
        "correct": "Martin Lawrence (with musical production by Steve Keitt)",
        "distractors": ["Heavy D", "KRS-One", "Grandmaster Flash"],
        "d": 3
    },
    {
        "q": "What legendary country superstar recorded the theme song for Coach in special promos and guest appearances?",
        "correct": "Clint Black",
        "distractors": ["Garth Brooks", "George Strait", "Alan Jackson"],
        "d": 3
    },
    {
        "q": "What jazz classic piece performed by Big Bad Voodoo Daddy served as transitional music and guest appearances on 3rd Rock from the Sun?",
        "correct": "Jumpin' Jack / You & Me & The Bottle Makes 3 Tonight",
        "distractors": ["Zoot Suit Riot", "Sing Sing Sing", "Jump Jive an' Wail"],
        "d": 3
    },
    {
        "q": "Who composed the iconic, Emmy-winning orchestral theme for Star Trek: The Next Generation and Deep Space Nine that set the standard for 90s TV scoring?",
        "correct": "Dennis McCarthy (adapting Jerry Goldsmith)",
        "distractors": ["James Horner", "Bruce Broughton", "John Debney"],
        "d": 3
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "staging", "90s_sitcoms_batch7.json")
    make_batch(q_batch7, 7, out)
