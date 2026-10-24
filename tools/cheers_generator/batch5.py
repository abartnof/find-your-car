import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from utils import assemble_batch, save_json

raw_questions = [
    # --- SHELLEY LONG DEPARTURE & KIRSTIE ALLEY INTRODUCTION (1-20) ---
    {
        "q": "Why did Shelley Long decide to leave Cheers at the end of Season 5?",
        "correct": "To pursue a film career in feature movies and spend time with her family",
        "wrong": ["She was fired by the network over salary disputes", "She suffered a vocal cord injury that prevented stage work", "She left to star in a competing CBS drama series"],
        "d": 1
    },
    {
        "q": "Which major 1980s film comedies did Shelley Long star in around the time of her Cheers departure?",
        "correct": "Night Shift, The Money Pit, and Outrageous Fortune",
        "wrong": ["Ghostbusters, Splash, and Big", "Tootsie, Broadcast News, and Working Girl", "Overboard, Protocol, and Private Benjamin"],
        "d": 3
    },
    {
        "q": "What iconic sci-fi role had Kirstie Alley played prior to being cast as Rebecca Howe on Cheers?",
        "correct": "Lt. Saavik in Star Trek II: The Wrath of Khan",
        "wrong": ["Princess Leia's stunt double in Return of the Jedi", "A Viper pilot in Battlestar Galactica", "Dr. Beverly Crusher in Star Trek: The Next Generation"],
        "d": 1
    },
    {
        "q": "What hilarious practical joke did Kirstie Alley pull during her very first table read with the Cheers cast?",
        "correct": "She wore a blonde wig modeled after Shelley Long's signature hairstyle",
        "wrong": ["She poured a pitcher of water over Ted Danson's head", "She spoke entirely in a fake Cockney accent", "She pretended to be a tourist looking for the bathroom"],
        "d": 3
    },
    {
        "q": "How did the Cheers producers deliberately differentiate Rebecca Howe from Diane Chambers?",
        "correct": "Making Rebecca an ambitious corporate climber whose confident facade constantly collapsed into neurotic tears",
        "wrong": ["Making Rebecca an illiterate tomboy who loved mechanics", "Giving Rebecca an aristocratic British royal background", "Portraying Rebecca as an aggressive, street-smart loan shark"],
        "d": 2
    },
    {
        "q": "In which season did Shelley Long make her highly anticipated guest return to Cheers?",
        "correct": "Season 11 (the series finale 'One for the Road')",
        "wrong": ["Season 8", "Season 9", "Season 10"],
        "d": 1
    },
    {
        "q": "What secret alternative ending was filmed for Season 5's finale 'I Do, Adieu' to prevent script leaks?",
        "correct": "An ending where Sam and Diane actually went through with their wedding ceremony",
        "wrong": ["An ending where Diane was hit by a taxi outside Cheers", "An ending where Frasier interrupted the ceremony with a restraining order", "An ending where Sam sold the bar and moved to Hawaii alone"],
        "d": 2
    },
    {
        "q": "How did the studio audience react during the taping of 'I Do, Adieu' when Sam and Diane didn't marry?",
        "correct": "Genuinely emotional with audible gasps and tearful applause",
        "wrong": ["They booed the cast off the stage in anger", "They demanded their ticket money back", "They laughed thinking it was an elaborate gag"],
        "d": 3
    },
    {
        "q": "How many Golden Globe Awards did Shelley Long win for playing Diane Chambers on Cheers?",
        "correct": "2",
        "wrong": ["0", "1", "4"],
        "d": 2
    },
    {
        "q": "In what year did Shelley Long win her Primetime Emmy Award for Outstanding Lead Actress?",
        "correct": "1983",
        "wrong": ["1985", "1987", "1990"],
        "d": 2
    },
    {
        "q": "What was the critical and ratings reaction to Kirstie Alley's debut season (Season 6)?",
        "correct": "Huge critical and commercial success, keeping Cheers firmly in the top ratings",
        "wrong": ["A massive ratings drop that nearly caused NBC to cancel the show", "Widespread boycott from fans demanding Shelley Long's return", "Critical panning followed by an immediate mid-season retooling"],
        "d": 2
    },
    {
        "q": "What was the title of Kirstie Alley's memorable 1991 Emmy acceptance speech line about her husband Parker Stevenson?",
        "correct": "She famously thanked him for giving her 'the big one' for the last eight years",
        "wrong": ["She thanked him for teaching her how to pour beer", "She joked that he made better clam chowder than Melville's", "She thanked him for letting her wear her high heels to bed"],
        "d": 3
    },
    {
        "q": "What film franchise did Kirstie Alley star in alongside John Travolta while starring on Cheers?",
        "correct": "Look Who's Talking",
        "wrong": ["Three Men and a Baby", "Police Academy", "National Lampoon's Vacation"],
        "d": 2
    },
    {
        "q": "Which actress was also considered for the role of Rebecca Howe before Kirstie Alley was cast?",
        "correct": "Sharon Stone (and Kim Cattrall)",
        "wrong": ["Julia Roberts", "Demi Moore", "Sigourney Weaver"],
        "d": 3
    },
    {
        "q": "Did Shelley Long ever reprise her role as Diane Chambers on the spin-off series Frasier?",
        "correct": "Yes, in multiple episodes including dream sequences and real visits",
        "wrong": ["No, she declined all invitations to appear on Frasier", "No, because the character of Diane was killed off off-screen", "Only in an uncredited audio voiceover in the pilot"],
        "d": 2
    },
    {
        "q": "What 1989 film starring Shelley Long and Craig T. Nelson became a cult comedy classic about the Wilderness Girls?",
        "correct": "Troop Beverly Hills",
        "wrong": ["Camp Nowhere", "Don't Tell Mom the Babysitter's Dead", "Baby Boom"],
        "d": 3
    },
    {
        "q": "What was the real reason producers decided not to recast Diane Chambers with another actress?",
        "correct": "They felt Shelley Long's portrayal was unique and replacing her directly would alienate the audience",
        "wrong": ["The Screen Actors Guild prohibited recasting existing roles in prime time", "NBC executives insisted on an all-male ensemble", "Paramount had already signed a contract with another studio"],
        "d": 2
    },
    {
        "q": "How was Shelley Long greeted by the Cheers cast when she returned to film the 1993 series finale?",
        "correct": "With warmth and professional celebration after years apart",
        "wrong": ["Tense silence with separate dressing trailers on opposite sides of the lot", "She refused to speak with Ted Danson outside of scripted scenes", "The cast staged a walkout during the first rehearsal"],
        "d": 3
    },
    {
        "q": "In 1990, which television movie saw Shelley Long star alongside Barry Bostwick?",
        "correct": "Fatal Charm / Voices Within: The Lives of Truddi Chase",
        "wrong": ["The Burning Bed", "A Mother's Courage", "Too Young to Die"],
        "d": 3
    },
    {
        "q": "What Emmy Award did Kirstie Alley win for Cheers in 1991?",
        "correct": "Outstanding Lead Actress in a Comedy Series",
        "wrong": ["Outstanding Supporting Actress in a Comedy Series", "Outstanding Guest Actress in a Comedy Series", "Outstanding Variety Performance"],
        "d": 1
    },

    # --- NICHOLAS COLASANTO & WOODY HARRELSON (21-40) ---
    {
        "q": "In what year did beloved actor Nicholas Colasanto pass away during the production of Season 3?",
        "correct": "1985 (February 12, 1985)",
        "wrong": ["1983", "1987", "1989"],
        "d": 1
    },
    {
        "q": "What serious health condition had Nicholas Colasanto battled during the filming of Cheers?",
        "correct": "Heart disease / coronary heart disease",
        "wrong": ["Lung cancer", "Kidney failure", "Parkinson's disease"],
        "d": 3
    },
    {
        "q": "What was Nicholas Colasanto's notable career background in television before playing Coach?",
        "correct": "An accomplished television director, directing episodes of Columbo, Hawaii Five-O, and Starsky & Hutch",
        "wrong": ["A professional opera singer at the New York Metropolitan Opera", "A minor league baseball umpire in the Pacific Coast League", "A stand-up comedian on the Ed Sullivan Show"],
        "d": 2
    },
    {
        "q": "Which iconic 1980 Martin Scorsese boxing masterpiece featured Nicholas Colasanto as mob boss Tommy Como?",
        "correct": "Raging Bull",
        "wrong": ["Goodfellas", "Taxi Driver", "Casino"],
        "d": 2
    },
    {
        "q": "What did the cast and crew do with Nicholas Colasanto's personal dressing room portrait of Geronimo?",
        "correct": "Hung it prominently on the Cheers bar set wall as a permanent tribute to him",
        "wrong": ["Donated it to the Baseball Hall of Fame in Cooperstown", "Auctioned it for charity at the Beverly Hills Hotel", "Buried it under the soundstage floorboards"],
        "d": 1
    },
    {
        "q": "What touching personal ritual did Ted Danson perform before filming every Cheers episode after Colasanto's death?",
        "correct": "Touching the Geronimo portrait on the set wall for good luck and remembrance",
        "wrong": ["Reciting Coach's Albania mnemonic song in the mirror", "Leaving an empty cold beer stein on the corner stool", "Tying a black ribbon around his baseball jacket"],
        "d": 1
    },
    {
        "q": "In the final shot of the entire series in 1993, what does Sam Malone do before walking into the shadows?",
        "correct": "Straightens the framed picture of Geronimo hanging on the wall",
        "wrong": ["Pours one last beer down the sink drain", "Turns off the neon sign in the front window", "Places Coach's baseball cap on the cash register"],
        "d": 1
    },
    {
        "q": "What stage production on Broadway was Woody Harrelson understudying when he auditioned for Cheers?",
        "correct": "Neil Simon's 'Biloxi Blues'",
        "wrong": ["David Mamet's 'Glengarry Glen Ross'", "Arthur Miller's 'Death of a Salesman'", "Tom Stoppard's 'The Real Thing'"],
        "d": 3
    },
    {
        "q": "What did the producers find compelling about Woody Harrelson during his audition for the replacement role?",
        "correct": "His disarming, genuine, Midwestern country-boy innocence and boyish charm",
        "wrong": ["His uncanny vocal impression of Nicholas Colasanto", "His ability to juggle cocktail shakers and liquor bottles", "His fast-talking, cynical Brooklyn comedic delivery"],
        "d": 2
    },
    {
        "q": "What was the real-life background of Woody Harrelson's estranged father, Charles Harrelson?",
        "correct": "A convicted contract hitman who assassinated Federal Judge John H. Wood Jr.",
        "wrong": ["A prominent Texas oil tycoon and state senator", "A professional heavyweight boxer and Olympic medalist", "A touring country-and-western bluegrass fiddle player"],
        "d": 2
    },
    {
        "q": "In what small Ohio college did Woody Harrelson earn a degree in theater and English?",
        "correct": "Hanover College in Indiana (the town his character was named after)",
        "wrong": ["Oberlin College in Ohio", "Kenyon College in Ohio", "DePauw University in Indiana"],
        "d": 3
    },
    {
        "q": "Why did the Cheers writers name Woody Boyd's hometown 'Hanover, Indiana'?",
        "correct": "Because Woody Harrelson had attended Hanover College in Hanover, Indiana",
        "wrong": ["Because co-creator Glen Charles was born on a farm in Hanover", "Because it was the home of the real manufacturer of the barstools", "Because it won a viewer contest held in TV Guide in 1984"],
        "d": 2
    },
    {
        "q": "What blockbuster 1992 sports comedy film starred Woody Harrelson alongside Wesley Snipes?",
        "correct": "White Men Can't Jump",
        "wrong": ["Major League", "Hoosiers", "Blue Chips"],
        "d": 2
    },
    {
        "q": "What 1994 Oliver Stone crime satire starred Woody Harrelson as mass murderer Mickey Knox?",
        "correct": "Natural Born Killers",
        "wrong": ["Pulp Fiction", "The Usual Suspects", "True Romance"],
        "d": 2
    },
    {
        "q": "How many Academy Award (Oscar) nominations has Woody Harrelson received in his film career?",
        "correct": "3 (for The People vs. Larry Flynt, The Messenger, and Three Billboards Outside Ebbing, Missouri)",
        "wrong": ["0", "1", "5"],
        "d": 2
    },
    {
        "q": "How many Primetime Emmy nominations did Woody Harrelson earn for his role as Woody Boyd on Cheers?",
        "correct": "5 consecutive nominations (winning in 1989)",
        "wrong": ["2 nominations", "8 nominations", "11 nominations"],
        "d": 3
    },
    {
        "q": "How was Coach's passing handled in the narrative of Season 4's premiere?",
        "correct": "With poignant, gentle references to his death without showing a funeral",
        "wrong": ["With an elaborate two-part funeral episode with flashbacks", "By stating that Coach had moved to a nursing home in Arizona", "The character was never mentioned again by any regular"],
        "d": 2
    },
    {
        "q": "What was the final episode Nicholas Colasanto filmed before his death?",
        "correct": "\"Cheerio, Cheers\" in Season 3",
        "wrong": ["\"Showdown: Part 2\"", "\"King of the Hill\"", "\"Rescue Me\""],
        "d": 3
    },
    {
        "q": "What was Nicholas Colasanto's final brief on-screen appearance in the Season 3 finale?",
        "correct": "A brief scene filmed earlier that was edited into the cold open",
        "wrong": ["A dream sequence where he appeared in angel wings", "A voiceover phone call to Sam from Florida", "A photograph displayed on the front door"],
        "d": 3
    },
    {
        "q": "What environmental cause did Woody Harrelson become famously known for promoting during his Cheers years?",
        "correct": "Organic farming, veganism, and industrial hemp advocacy",
        "wrong": ["Nuclear energy expansion", "Whale hunting regulation exclusively", "Electric high-speed passenger rail networks"],
        "d": 2
    },

    # --- JOHN RATZENBERGER, GEORGE WENDT & AUDITIONS (41-60) ---
    {
        "q": "What role did John Ratzenberger originally audition for when trying out for Cheers?",
        "correct": "Norm Peterson (or a generic bar customer)",
        "wrong": ["Ernie 'Coach' Pantusso", "Sam Malone", "Dr. Frasier Crane"],
        "d": 1
    },
    {
        "q": "How did John Ratzenberger invent the character of Cliff Clavin on the spot during his audition?",
        "correct": "He asked the creators if they had a 'bar know-it-all' who pretends to know everything",
        "wrong": ["He walked in dressed as a real Boston transit police officer", "He began reciting encyclopedia entries in a thick Irish brogue", "He started checking the mail delivery boxes in the Paramount lobby"],
        "d": 1
    },
    {
        "q": "Where was John Ratzenberger born and raised, giving him his authentic New England cadence?",
        "correct": "Bridgeport, Connecticut",
        "wrong": ["South Boston, Massachusetts", "Providence, Rhode Island", "Portland, Maine"],
        "d": 3
    },
    {
        "q": "What famous film animation studio has featured John Ratzenberger's voice in nearly all of its feature films?",
        "correct": "Pixar Animation Studios",
        "wrong": ["DreamWorks Animation", "Studio Ghibli", "Illumination Entertainment"],
        "d": 1
    },
    {
        "q": "Which iconic piggy bank character did John Ratzenberger voice in the Toy Story film series?",
        "correct": "Hamm",
        "wrong": ["Rex", "Slinky Dog", "Mr. Potato Head"],
        "d": 2
    },
    {
        "q": "What famous sci-fi blockbuster featured John Ratzenberger in a minor role as Major Bren Derlin on Hoth?",
        "correct": "Star Wars: Episode V - The Empire Strikes Back",
        "wrong": ["Star Trek: The Motion Picture", "Alien", "Blade Runner"],
        "d": 2
    },
    {
        "q": "Which sci-fi blockbuster featured John Ratzenberger as a missile control officer alongside Christopher Reeve?",
        "correct": "Superman (1978) and Superman II",
        "wrong": ["Flash Gordon", "Close Encounters of the Third Kind", "The Black Hole"],
        "d": 3
    },
    {
        "q": "What improv comedy troupe in Chicago did George Wendt train with before landing the role of Norm?",
        "correct": "The Second City",
        "wrong": ["The Groundlings", "Upright Citizens Brigade", "ImprovOlympic"],
        "d": 2
    },
    {
        "q": "What was George Wendt's character originally named in the pilot script before being developed into Norm?",
        "correct": "George",
        "wrong": ["Barney", "Gus", "Ralph"],
        "d": 2
    },
    {
        "q": "Which famous Saturday Night Live comedy star is the real-life nephew of George Wendt?",
        "correct": "Jason Sudeikis",
        "wrong": ["Will Forte", "Bill Hader", "Seth Meyers"],
        "d": 2
    },
    {
        "q": "What landmark intellectual property lawsuit was filed by George Wendt and John Ratzenberger in 1993?",
        "correct": "Wendt v. Host International, Inc. (over animatronic airport bar robots modeled after Norm and Cliff)",
        "wrong": ["A trademark suit against Samuel Adams brewery for using their faces on labels", "A copyright infringement suit against the creators of The Simpsons", "A contract lawsuit against Paramount over syndication residuals"],
        "d": 3
    },
    {
        "q": "What were the names of the robotic animatronic figures created by Host International that prompted the lawsuit?",
        "correct": "\"Hank\" and \"Bob\"",
        "wrong": ["\"Ned\" and \"Chet\"", "\"Burt\" and \"Mack\"", "\"Gus\" and \"Al\""],
        "d": 3
    },
    {
        "q": "What legal principle did the Ninth Circuit Court establish in Wendt v. Host International?",
        "correct": "An actor's right of publicity protects against unauthorized commercial robotic replicas evoking their identity",
        "wrong": ["Sitcom characters cannot be copyrighted by individual actors", "Airports have sovereign immunity against all civil copyright claims", "Parody animatronics are entirely protected by the First Amendment"],
        "d": 3
    },
    {
        "q": "Which actor, famous for playing Fred Flintstone and in The Great Escape, originally auditioned for Coach?",
        "correct": "Nicholas Colasanto won the role, beating out several veterans including Sid Caesar considerations",
        "wrong": ["Alan Hale Jr.", "Denver Pyle", "Jack Elam"],
        "d": 3
    },
    {
        "q": "What actor was the creators' initial top choice for Sam Malone when the character was envisioned as a former football player?",
        "correct": "Fred Dryer (former NFL defensive end who later starred in Hunter)",
        "wrong": ["Joe Namath", "Burt Reynolds", "Mark Harmon"],
        "d": 3
    },
    {
        "q": "Why was the character of Sam Malone changed from a former football player to a former baseball pitcher?",
        "correct": "To better fit Ted Danson's lean, athletic build rather than a bulky NFL physique",
        "wrong": ["Because the NFL refused to license team names for the pilot", "Because Boston did not have a professional football team in 1982", "Because baseball was cheaper to film in stadium stock footage"],
        "d": 2
    },
    {
        "q": "Which actress auditioned alongside Fred Dryer as a paired test for the roles of Sam and Diane?",
        "correct": "Julia Duffy",
        "wrong": ["Courteney Cox", "Geena Davis", "Helen Hunt"],
        "d": 3
    },
    {
        "q": "What other actress was paired with Ted Danson in final screen tests before Shelley Long was selected?",
        "correct": "Lisa Eichhorn",
        "wrong": ["Bess Armstrong", "Jane Curtin", "Christine Ebersole"],
        "d": 3
    },
    {
        "q": "What did the creators cite as the deciding factor in casting Ted Danson and Shelley Long together?",
        "correct": "Their undeniable, combustible, romantic on-screen chemistry during paired chemistry reads",
        "wrong": ["They both agreed to work for lower initial salaries than other contenders", "They had previously starred together in an off-Broadway romantic comedy", "They were both personal friends of NBC executive Brandon Tartikoff"],
        "d": 1
    },
    {
        "q": "What famous recurring Saturday Night Live sketch did George Wendt star in as a Chicago sports fanatic?",
        "correct": "\"Bill Swerski's Superfans\" (\"Da Bears!\")",
        "wrong": ["\"Wayne's World\"", "\"The Coneheads\"", "\"Two Wild and Crazy Guys\""],
        "d": 2
    },

    # --- JAY THOMAS, KELSEY GRAMMER & CAST ANECDOTES (61-80) ---
    {
        "q": "Why was actor Jay Thomas abruptly fired from his recurring role as Eddie LeBec in Season 8?",
        "correct": "He made disparaging remarks about kissing Rhea Perlman during a live morning radio broadcast",
        "wrong": ["He demanded a co-lead credit alongside Ted Danson", "He was arrested for vandalism at a Boston Bruins hockey game", "He skipped rehearsals to film a primetime television movie in Toronto"],
        "d": 1
    },
    {
        "q": "What exact insult did Jay Thomas deliver on his radio show that led to his character's immediate demise?",
        "correct": "He said having to kiss Rhea Perlman on Cheers was brutal and required hazard pay",
        "wrong": ["He claimed Rhea Perlman couldn't remember her lines without cue cards", "He mocked Rhea Perlman's real-life husband Danny DeVito on air", "He said the Cheers writing staff was out of fresh ideas"],
        "d": 2
    },
    {
        "q": "How did the Cheers writers retaliate against Jay Thomas for his radio comments?",
        "correct": "They killed off Eddie LeBec in an absurd, off-screen accident involving an ice Zamboni",
        "wrong": ["They had Carla divorce him for an ugly French mime", "They sent Eddie to play hockey in Soviet Siberia forever", "They never explained his disappearance and deleted his character name"],
        "d": 1
    },
    {
        "q": "For how many episodes was Kelsey Grammer originally contracted when cast as Frasier Crane in Season 3?",
        "correct": "Only 4 to 6 episodes",
        "wrong": ["A full 22-episode season", "Only a single two-minute guest scene", "A three-year series regular contract"],
        "d": 1
    },
    {
        "q": "Why did the Cheers producers decide to make Kelsey Grammer a permanent series regular?",
        "correct": "His comedic delivery, refined pomposity, and chemistry with the cast were extraordinarily popular",
        "wrong": ["Paramount studio executives mandated the addition of a psychiatrist character", "Shelley Long refused to film scenes unless Frasier remained in Boston", "Kelsey Grammer purchased an ownership share in Charles-Burrows-Charles Productions"],
        "d": 2
    },
    {
        "q": "For how many total consecutive years did Kelsey Grammer play the character of Frasier Crane across Cheers and Frasier?",
        "correct": "20 consecutive years (1984 to 2004)",
        "wrong": ["11 years", "15 years", "25 years"],
        "d": 1
    },
    {
        "q": "What cosmetic secret about Ted Danson's hair was kept under wraps for much of the series run?",
        "correct": "He wore a small hairpiece (toupee) to conceal a bald spot on his crown",
        "wrong": ["His hair was completely dyed bright red naturally", "He wore a full theatrical lace wig in every scene", "He had undergone experimental scalp grafting"],
        "d": 1
    },
    {
        "q": "On which late-night talk show did Ted Danson famously remove his hairpiece on camera to surprise the audience?",
        "correct": "The Arsenio Hall Show",
        "wrong": ["The Tonight Show Starring Johnny Carson", "Late Night with David Letterman", "The Phil Donahue Show"],
        "d": 2
    },
    {
        "q": "What was Ted Danson's reported salary per episode for the 11th and final season of Cheers?",
        "correct": "Approximately 450,000 to 500,000 dollars per episode (making him the highest-paid actor on TV then)",
        "wrong": ["100,000 dollars per episode", "1 million dollars per episode", "250,000 dollars per episode"],
        "d": 2
    },
    {
        "q": "Who was Philip Perlman, who made over 30 non-speaking and bit appearances as bar regular Phil?",
        "correct": "Rhea Perlman's real-life father",
        "wrong": ["Ted Danson's childhood uncle from San Diego", "James Burrows' personal college roommate", "George Wendt's father-in-law"],
        "d": 1
    },
    {
        "q": "What Hollywood superstar is Rhea Perlman married to in real life?",
        "correct": "Danny DeVito",
        "wrong": ["Joe Pesci", "Harvey Keitel", "Bob Hoskins"],
        "d": 1
    },
    {
        "q": "Did Danny DeVito ever make an on-camera cameo appearance inside Cheers?",
        "correct": "No, he never appeared on camera in Cheers despite his marriage to Rhea Perlman",
        "wrong": ["Yes, as Carla's cousin Vinnie in Season 4", "Yes, as a rival bar owner from Philadelphia in Season 7", "Yes, as a postal supervisor inspecting Cliff's route"],
        "d": 2
    },
    {
        "q": "Which core cast member had a severe fear of flying that required traveling across the country by train?",
        "correct": "John Ratzenberger (Cliff Clavin)",
        "wrong": ["Ted Danson", "George Wendt", "Rhea Perlman"],
        "d": 3
    },
    {
        "q": "What Broadway musical did Bebe Neuwirth star in as Velma Kelly, winning a Tony Award?",
        "correct": "Chicago",
        "wrong": ["Cabaret", "A Chorus Line", "Sweet Charity"],
        "d": 1
    },
    {
        "q": "How many Tony Awards has Bebe Neuwirth won in her illustrious Broadway stage career?",
        "correct": "2 Tony Awards (for Sweet Charity and Chicago)",
        "wrong": ["0", "1", "4"],
        "d": 2
    },
    {
        "q": "What was the atmosphere among the cast members during rehearsals throughout the 11-year run?",
        "correct": "Remarkably harmonious, collaborative, and free of ego clashes compared to most hit shows",
        "wrong": ["Plagued by constant physical fistfights and police interventions", "Actors refused to rehearse together, relying on stand-ins until tape day", "Strictly formal with no personal socializing allowed by the studio"],
        "d": 2
    },
    {
        "q": "What did the cast do together every week on set before taping began in front of the studio audience?",
        "correct": "Gathered in a tight group huddle to share words of encouragement and group affection",
        "wrong": ["Drank a celebratory shot of real Irish whiskey together", "Listened to James Burrows read fan mail from Boston", "Held a moment of silence for Red Sox players"],
        "d": 2
    },
    {
        "q": "What did Ted Danson do immediately after Cheers wrapped in 1993 regarding his personal life and career?",
        "correct": "Starred in the film 'Made in America' and later the CBS sitcom 'Becker'",
        "wrong": ["Retired from acting to become a commercial fisherman in Maine", "Moved permanently to London to study classical Shakespeare", "Directed an independent documentary on Boston baseball"],
        "d": 2
    },
    {
        "q": "Which core cast member appeared in every single one of the 275 broadcast episodes of Cheers?",
        "correct": "Ted Danson (and Rhea Perlman & George Wendt)",
        "wrong": ["Only Ted Danson", "Only Kelsey Grammer", "Every single main cast member"],
        "d": 2
    },
    {
        "q": "Which female star appeared in the most episodes of Cheers across its 11 seasons?",
        "correct": "Rhea Perlman (Carla Tortelli)",
        "wrong": ["Shelley Long (Diane Chambers)", "Kirstie Alley (Rebecca Howe)", "Bebe Neuwirth (Lilith Sternin)"],
        "d": 1
    },

    # --- CELEBRITY GUEST STARS & HISTORICAL CAMEOS (81-100) ---
    {
        "q": "Which late-night television king made a surprise cameo as himself in the Season 10 episode 'The King of Beers'?",
        "correct": "Johnny Carson",
        "wrong": ["David Letterman", "Jay Leno", "Ed McMahon"],
        "d": 1
    },
    {
        "q": "Which speaker of the U.S. House of Representatives and Massachusetts native made a Season 1 cameo in Cheers?",
        "correct": "Tip O'Neill",
        "wrong": ["Ted Kennedy", "John F. Kennedy Jr.", "Michael Dukakis"],
        "d": 1
    },
    {
        "q": "What does Speaker Tip O'Neill do in his Season 1 cameo when Diane Chambers begins venting to him?",
        "correct": "He quietly slips out of the bar into a waiting taxi to escape her pontificating",
        "wrong": ["He offers Diane an internship on Capitol Hill", "He buys a round of draft beers for Norm and Cliff", "He debates politics with Coach over the bar counter"],
        "d": 2
    },
    {
        "q": "Which 1988 Democratic presidential candidate and Massachusetts governor made a guest cameo in Season 9?",
        "correct": "Michael Dukakis",
        "wrong": ["Bill Clinton", "Walter Mondale", "Paul Tsongas"],
        "d": 1
    },
    {
        "q": "Which Boston Celtics Hall of Fame forward guest-starred as himself, obsessively counting parquet floorboards?",
        "correct": "Kevin McHale",
        "wrong": ["Larry Bird", "Robert Parish", "Bill Russell"],
        "d": 1
    },
    {
        "q": "What did the Cheers gang bet on involving Kevin McHale's basketball cameo?",
        "correct": "How many floorboards made up the Boston Garden parquet floor",
        "wrong": ["How many free throws he could make blindfolded in the alley", "Whether he could drink more beer than Norm Peterson", "Whether he could dunk on the ten-foot bar entrance doorway"],
        "d": 2
    },
    {
        "q": "Which Boston Red Sox Hall of Fame third baseman appeared in Season 6, only to have the gang steal his pants?",
        "correct": "Wade Boggs",
        "wrong": ["Roger Clemens", "Carl Yastrzemski", "Dwight Evans"],
        "d": 1
    },
    {
        "q": "Why did the Cheers regulars steal Wade Boggs' pants during his guest appearance?",
        "correct": "They believed he was a fake imposter sent by Gary's Olde Towne Tavern to pull a prank",
        "wrong": ["They wanted to auction them for charity at Melville's", "Carla wanted an authentic autograph on the back pocket", "Norm bet Cliff fifty dollars he couldn't pants a major leaguer"],
        "d": 2
    },
    {
        "q": "Which future Academy Award-winning actress guest-starred as Frasier's singing ex-wife Nanette Guzman ('Nanny G')?",
        "correct": "Emma Thompson",
        "wrong": ["Kate Winslet", "Cate Blanchett", "Helena Bonham Carter"],
        "d": 1
    },
    {
        "q": "What was the title of the Season 10 episode featuring Emma Thompson as Nanny G?",
        "correct": "\"One Hugs, the Other Doesn't\"",
        "wrong": ["\"Frasier's First Love\"", "\"The Song of Boston\"", "\"Children's Hour\""],
        "d": 3
    },
    {
        "q": "Which con artist and magician character did Harry Anderson portray in six early Cheers episodes?",
        "correct": "Harry the Hat (Harry Gittes)",
        "wrong": ["Magic Mike", "Boston Benny", "Slick Sal"],
        "d": 1
    },
    {
        "q": "Which NBC sitcom was created around Harry Anderson following his popular guest appearances on Cheers?",
        "correct": "Night Court",
        "wrong": ["Wings", "Empty Nest", "My Two Dads"],
        "d": 1
    },
    {
        "q": "Which game show host made a famous cameo when Cliff Clavin appeared on Jeopardy!?",
        "correct": "Alex Trebek",
        "wrong": ["Pat Sajak", "Chuck Woolery", "Bob Eubanks"],
        "d": 1
    },
    {
        "q": "What famous talk show host appeared as himself in Season 2, being insulted by Norm in the bar?",
        "correct": "Dick Cavett",
        "wrong": ["Merv Griffin", "Phil Donahue", "Mike Douglas"],
        "d": 2
    },
    {
        "q": "In Dick Cavett's guest appearance, what does he suggest to Sam Malone about Diane?",
        "correct": "That Sam and Diane's passionate fighting is a classic Freudian neurosis masking desire",
        "wrong": ["That Diane should write a book for his publishing imprint", "That Sam should hire a public relations firm for the bar", "That Coach should be booked as a guest on his literary talk show"],
        "d": 3
    },
    {
        "q": "Which famous Senator from Massachusetts made a cameo appearance in the series finale 'One for the Road'?",
        "correct": "John Kerry",
        "wrong": ["Ted Kennedy", "Mitt Romney", "Edward Brooke"],
        "d": 2
    },
    {
        "q": "Which famous Boston Red Sox pitcher appeared as himself in Season 2's episode 'Just Three Friends'?",
        "correct": "Luis Tiant",
        "wrong": ["Jim Lonborg", "Bill Lee", "Roger Clemens"],
        "d": 3
    },
    {
        "q": "Which television star from 'Spenser: For Hire' made a brief cameo referencing Boston detective work?",
        "correct": "Robert Urich",
        "wrong": ["Tom Selleck", "Don Johnson", "Lee Majors"],
        "d": 3
    },
    {
        "q": "Which member of the famous Kennedy family made a cameo appearance on Cheers in Season 10?",
        "correct": "Ethel Kennedy",
        "wrong": ["Maria Shriver", "Caroline Kennedy", "Robert F. Kennedy Jr."],
        "d": 3
    },
    {
        "q": "Which legendary sports announcer made a voiceover cameo as a boxing commentator in Season 4?",
        "correct": "Bob Costas",
        "wrong": ["Al Michaels", "Howard Cosell", "Vin Scully"],
        "d": 3
    }
]

assert len(raw_questions) == 100, f"Expected 100, got {len(raw_questions)}"

d_counts = {1: 0, 2: 0, 3: 0}
for q in raw_questions:
    d_counts[q["d"]] += 1

print(f"DEBUG Batch 5 d_counts: {d_counts}")
assert d_counts[1] == 30, f"Expected 30 d1, got {d_counts[1]}"
assert d_counts[2] == 40, f"Expected 40 d2, got {d_counts[2]}"
assert d_counts[3] == 30, f"Expected 30 d3, got {d_counts[3]}"

formatted = assemble_batch(raw_questions, 5)
save_json(formatted, "tools/staging/cheers_batch5.json")
print("Saved tools/staging/cheers_batch5.json successfully!")
