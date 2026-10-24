#!/usr/bin/env python3
"""
Generate SNL Batch 6: Metatextual 2 - Cast Tenures, Head Writers, Directors, Crew & Emmy Records
100 questions: exactly 30 d1, 40 d2, 30 d3.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from builder import build_batch

questions = [
    # 1
    {
        "q": "Who is the longest-tenured cast member in Saturday Night Live history, having joined in 2003 and performed for over 21 seasons?",
        "correct": "Kenan Thompson",
        "distractors": ["Darrell Hammond", "Seth Meyers", "Fred Armisen"],
        "d": 1
    },
    # 2
    {
        "q": "Who held the record for the longest cast tenure before Kenan Thompson surpassed him, having served 14 seasons from 1995 to 2009?",
        "correct": "Darrell Hammond",
        "distractors": ["Tim Meadows", "Kevin Nealon", "Phil Hartman"],
        "d": 1
    },
    # 3
    {
        "q": "Who served as the legendary announcer of Saturday Night Live from the premiere in 1975 until his death in 2014 at age 96?",
        "correct": "Don Pardo",
        "distractors": ["Ernie Anderson", "Charlie O'Donnell", "Johnny Olson"],
        "d": 1
    },
    # 4
    {
        "q": "Which former cast member took over as the permanent announcer of SNL in 2014 following Don Pardo's passing?",
        "correct": "Darrell Hammond",
        "distractors": ["Dana Carvey", "Kevin Nealon", "Bill Hader"],
        "d": 1
    },
    # 5
    {
        "q": "Who was the original musical director of Saturday Night Live (1975-1980) who later won three Academy Awards for scoring 'The Lord of the Rings' trilogy?",
        "correct": "Howard Shore",
        "distractors": ["Paul Shaffer", "G.E. Smith", "Lenny Pickett"],
        "d": 1
    },
    # 6
    {
        "q": "Which distinctive blonde guitarist led the Saturday Night Live Band from 1985 to 1995, famous for his energetic facial expressions and Fender Telecaster solos?",
        "correct": "G.E. Smith",
        "distractors": ["Paul Shaffer", "Howard Shore", "Lenny Pickett"],
        "d": 1
    },
    # 7
    {
        "q": "Which tenor saxophone virtuoso and former Tower of Power member has led the SNL Band since 1995, famous for his screaming altissimo closing solos?",
        "correct": "Lenny Pickett",
        "distractors": ["Clarence Clemons", "Michael Brecker", "David Sanborn"],
        "d": 1
    },
    # 8
    {
        "q": "Which musician played keyboards in the original SNL Band, frequently impersonated Don Kirshner, and later spent three decades leading David Letterman's band?",
        "correct": "Paul Shaffer",
        "distractors": ["Leon Pendarvis", "Cheryl Hardwick", "Tom Malone"],
        "d": 1
    },
    # 9
    {
        "q": "Who was appointed as the first female head writer in Saturday Night Live history in 1999?",
        "correct": "Tina Fey",
        "distractors": ["Paula Pell", "Sarah Schneider", "Marilyn Suzanne Miller"],
        "d": 1
    },
    # 10
    {
        "q": "Who holds the record as the most nominated individual in the history of the Primetime Emmy Awards, with over 100 nominations?",
        "correct": "Lorne Michaels",
        "distractors": ["David Letterman", "Norman Lear", "Steven Spielberg"],
        "d": 1
    },
    # 11
    {
        "q": "Which television program has received more Primetime Emmy Award nominations and wins than any other show in television history?",
        "correct": "Saturday Night Live",
        "distractors": ["Game of Thrones", "ER", "The Simpsons"],
        "d": 1
    },
    # 12
    {
        "q": "Who was the primary head writer and dark comedic visionary behind SNL's earliest seasons, nicknamed 'Mr. Mike'?",
        "correct": "Michael O'Donoghue",
        "distractors": ["Jim Downey", "Al Franken", "Herb Sargent"],
        "d": 2
    },
    # 13
    {
        "q": "Which veteran writer spent nearly 30 years at SNL and penned the vast majority of its most celebrated presidential debates and political parodies?",
        "correct": "Jim Downey",
        "distractors": ["Jack Handey", "Adam McKay", "Robert Smigel"],
        "d": 2
    },
    # 14
    {
        "q": "Which Oscar-winning writer-director served as SNL's head writer from 1996 to 2001, frequently collaborating with Will Ferrell?",
        "correct": "Adam McKay",
        "distractors": ["Spike Jonze", "Paul Thomas Anderson", "Judd Apatow"],
        "d": 2
    },
    # 15
    {
        "q": "Who served as SNL's head writer from 2005 until his departure in 2014, while also anchoring Weekend Update?",
        "correct": "Seth Meyers",
        "distractors": ["Colin Jost", "Michael Che", "John Mulaney"],
        "d": 2
    },
    # 16
    {
        "q": "Which female writer penned many of SNL's most beloved sketches, including the Spartan Cheerleaders, Debbie Downer, and O沉默 Culps?",
        "correct": "Paula Pell",
        "distractors": ["Emily Spivey", "Marilyn Suzanne Miller", "Sarah Schneider"],
        "d": 2
    },
    # 17
    {
        "q": "Who directed the live broadcast of Saturday Night Live for its first two decades (1975-1995)?",
        "correct": "Dave Wilson",
        "distractors": ["Don Roy King", "Beth McCarthy-Miller", "Paul Miller"],
        "d": 2
    },
    # 18
    {
        "q": "Which trailblazing director helmed SNL from 1995 to 2006 before going on to direct '30 Rock' and high-profile comedy specials?",
        "correct": "Beth McCarthy-Miller",
        "distractors": ["Liz Patrick", "Pamela Fryman", "Gail Mancuso"],
        "d": 2
    },
    # 19
    {
        "q": "Which television director won a record 11 Primetime Emmy Awards for directing Saturday Night Live between 2006 and 2021?",
        "correct": "Don Roy King",
        "distractors": ["Dave Wilson", "Beth McCarthy-Miller", "James Burrows"],
        "d": 2
    },
    # 20
    {
        "q": "Who took over as the live broadcast director of Saturday Night Live in 2021 following Don Roy King's retirement?",
        "correct": "Liz Patrick",
        "distractors": ["Beth McCarthy-Miller", "Paul Pennolino", "Carrie Havel"],
        "d": 2
    },
    # 21
    {
        "q": "In which iconic Manhattan skyscraper and studio space is Saturday Night Live produced and broadcast live?",
        "correct": "Studio 8H at 30 Rockefeller Plaza",
        "distractors": ["Studio 6A at 30 Rockefeller Plaza", "The Ed Sullivan Theater", "Kaufman Astoria Studios"],
        "d": 1
    },
    # 22
    {
        "q": "For which legendary classical music conductor was Studio 8H originally constructed in 1937 as an orchestral radio studio?",
        "correct": "Arturo Toscanini (and the NBC Symphony Orchestra)",
        "distractors": ["Leonard Bernstein", "Leopold Stokowski", "Arthur Fiedler"],
        "d": 2
    },
    # 23
    {
        "q": "Approximately how many live audience members does Studio 8H accommodate during an SNL broadcast?",
        "correct": "Between 300 and 330",
        "distractors": ["Around 750", "Over 1,200", "Under 100"],
        "d": 2
    },
    # 24
    {
        "q": "Who produced Saturday Night Live during Season 6 (1980-1981) following the departure of Lorne Michaels and the entire original cast?",
        "correct": "Jean Doumanian",
        "distractors": ["Dick Ebersol", "Brandon Tartikoff", "Lorne Michaels"],
        "d": 2
    },
    # 25
    {
        "q": "Who took over as executive producer in the spring of 1981, bringing stability and commercial success back to SNL until 1985?",
        "correct": "Dick Ebersol",
        "distractors": ["Jean Doumanian", "Michael O'Donoghue", "Lorne Michaels"],
        "d": 2
    },
    # 26
    {
        "q": "In what year did Lorne Michaels return to produce Saturday Night Live after his five-year hiatus?",
        "correct": "1985 (Season 11)",
        "distractors": ["1983", "1987", "1989"],
        "d": 2
    },
    # 27
    {
        "q": "Which future Academy Award-winning actress was a cast member on SNL during the notorious 1985-1986 Season 11?",
        "correct": "Joan Cusack",
        "distractors": ["Helen Hunt", "Marisa Tomei", "Mira Sorvino"],
        "d": 2
    },
    # 28
    {
        "q": "Which future superstar actor was cast in Season 11 (1985-1986) at age 20 before being let go during the cast overhaul?",
        "correct": "Robert Downey Jr.",
        "distractors": ["Tom Cruise", "Johnny Depp", "Brad Pitt"],
        "d": 1
    },
    # 29
    {
        "q": "Which celebrated stand-up comedian and future 'Seinfeld' star was a cast member on SNL from 1982 to 1985?",
        "correct": "Julia Louis-Dreyfus",
        "distractors": ["Laurie Metcalf", "Catherine O'Hara", "Jane Lynch"],
        "d": 1
    },
    # 30
    {
        "q": "At what age did Eddie Murphy join the cast of Saturday Night Live in the fall of 1980, making him one of the youngest cast members in history?",
        "correct": "19 years old",
        "distractors": ["17 years old", "21 years old", "23 years old"],
        "d": 1
    },
    # 31
    {
        "q": "Who holds the record as the absolute youngest cast member ever hired in SNL history at just 17 years old?",
        "correct": "Anthony Michael Hall",
        "distractors": ["Eddie Murphy", "Pete Davidson", "Robert Downey Jr."],
        "d": 2
    },
    # 32
    {
        "q": "What legendary cue-card coordinator has been writing and handling the cue cards on SNL since 1990 and frequently appears on camera?",
        "correct": "Wally Feresten",
        "distractors": ["Joe Dicso", "Tony Mendez", "Steve Higgins"],
        "d": 1
    },
    # 33
    {
        "q": "Why does Saturday Night Live famously refuse to use electronic teleprompters for its sketch dialogue and Weekend Update?",
        "correct": "Cue cards allow rapid, last-second rewrites right up until the camera is live",
        "distractors": ["Studio 8H's lights create too much glare on teleprompters", "The actors union mandates paper cue cards", "Teleprompters were deemed too expensive in 1975 and the habit stuck"],
        "d": 2
    },
    # 34
    {
        "q": "Who serves as the longtime announcer for 'The Tonight Show Starring Jimmy Fallon' and a key producer/writer on SNL since 1995?",
        "correct": "Steve Higgins",
        "distractors": ["Erik Kenward", "Ken Aymong", "Bryan Tucker"],
        "d": 2
    },
    # 35
    {
        "q": "Which female cast member won back-to-back Primetime Emmy Awards for Outstanding Supporting Actress in a Comedy Series in 2016 and 2017?",
        "correct": "Kate McKinnon",
        "distractors": ["Kristen Wiig", "Cecily Strong", "Aidy Bryant"],
        "d": 1
    },
    # 36
    {
        "q": "Who was the first Saturday Night Live performer ever to win a Primetime Emmy Award for individual performance on the show?",
        "correct": "Chevy Chase (1976)",
        "distractors": ["John Belushi", "Gilda Radner", "Dana Carvey"],
        "d": 2
    },
    # 37
    {
        "q": "In 1978, which beloved original cast member won the Primetime Emmy Award for Outstanding Continuing or Single Performance by a Supporting Actress?",
        "correct": "Gilda Radner",
        "distractors": ["Jane Curtin", "Laraine Newman", "Candice Bergen"],
        "d": 2
    },
    # 38
    {
        "q": "Which cast member won the Primetime Emmy Award for Outstanding Individual Performance in a Variety or Music Program in 1993 for his impressions and characters?",
        "correct": "Dana Carvey",
        "distractors": ["Phil Hartman", "Mike Myers", "Chris Farley"],
        "d": 2
    },
    # 39
    {
        "q": "Who won a posthumous Primetime Emmy nomination in 1998 for his brilliant body of work on SNL following his tragic death?",
        "correct": "Phil Hartman",
        "distractors": ["Chris Farley", "John Belushi", "Danitra Vance"],
        "d": 2
    },
    # 40
    {
        "q": "Which long-serving cast member earned the moniker 'The Glue' from castmates and Lorne Michaels because of his rock-solid professionalism and ability to hold sketches together?",
        "correct": "Phil Hartman",
        "distractors": ["Dan Aykroyd", "Kevin Nealon", "Darrell Hammond"],
        "d": 1
    },
    # 41
    {
        "q": "What was the moniker bestowed upon the original seven cast members of Season 1 in the opening credits?",
        "correct": "The Not Ready for Prime Time Players",
        "distractors": ["The 8H Troupe", "The Midnight Comedians", "The Live from New York Crew"],
        "d": 1
    },
    # 42
    {
        "q": "Which original cast member left the show early in Season 2 (November 1976) to pursue a Hollywood film career?",
        "correct": "Chevy Chase",
        "distractors": ["John Belushi", "Dan Aykroyd", "Bill Murray"],
        "d": 1
    },
    # 43
    {
        "q": "Who was brought in to replace Chevy Chase in the cast during Season 2 in early 1977?",
        "correct": "Bill Murray",
        "distractors": ["Buck Henry", "Steve Martin", "Brian Doyle-Murray"],
        "d": 1
    },
    # 44
    {
        "q": "Which two original cast members simultaneously departed SNL at the conclusion of Season 4 in 1979 to film 'The Blues Brothers'?",
        "correct": "Dan Aykroyd and John Belushi",
        "distractors": ["Chevy Chase and Bill Murray", "Jane Curtin and Gilda Radner", "Garrett Morris and Laraine Newman"],
        "d": 2
    },
    # 45
    {
        "q": "Which writer-performer duo performed their own signature news commentaries on SNL in the late 1970s and declared the 1980s their personal decade?",
        "correct": "Al Franken and Tom Davis",
        "distractors": ["Jim Downey and Herb Sargent", "Brian Doyle-Murray and Bill Murray", "Bob Odenkirk and Robert Smigel"],
        "d": 2
    },
    # 46
    {
        "q": "What did Al Franken famously dub the 1980s on SNL?",
        "correct": "The Al Franken Decade",
        "distractors": ["The Decade of Smalley", "The Me-Franken Era", "The Stuart Years"],
        "d": 2
    },
    # 47
    {
        "q": "Which former SNL writer and cast member was elected to the United States Senate representing Minnesota in 2008?",
        "correct": "Al Franken",
        "distractors": ["Jim Downey", "Don Novello", "Kevin Nealon"],
        "d": 1
    },
    # 48
    {
        "q": "Which cast member holds the unfortunate record of appearing in only one single episode of SNL as a repertory player in April 1981?",
        "correct": "Laurie Metcalf",
        "distractors": ["Emily Prager", "Morwenna Banks", "Catherine O'Hara"],
        "d": 3
    },
    # 49
    {
        "q": "Which British actress appeared in only four episodes of SNL during the turbulent final weeks of Season 20 in 1995?",
        "correct": "Morwenna Banks",
        "distractors": ["Laura Kightlinger", "Sarah Silverman", "Janeane Garofalo"],
        "d": 3
    },
    # 50
    {
        "q": "Which acclaimed stand-up comedian and actress quit the SNL cast mid-season in early 1995, citing toxic writer culture?",
        "correct": "Janeane Garofalo",
        "distractors": ["Sarah Silverman", "Laura Kightlinger", "Julia Sweeney"],
        "d": 2
    },
    # 51
    {
        "q": "Which future stand-up superstar and Emmy-winning creator was a featured player and writer during Season 19 (1993-1994), never getting a sketch on air?",
        "correct": "Sarah Silverman",
        "distractors": ["Mindy Kaling", "Amy Schumer", "Chelsea Handler"],
        "d": 2
    },
    # 52
    {
        "q": "Which future late-night talk show host was hired as an SNL writer in 1988 and co-wrote classic sketches like 'Five-Timers Club' and 'Mr. Short-Term Memory'?",
        "correct": "Conan O'Brien",
        "distractors": ["Jimmy Kimmel", "Stephen Colbert", "Craig Ferguson"],
        "d": 1
    },
    # 53
    {
        "q": "Which future 'Better Call Saul' star worked as an SNL writer from 1987 to 1991 and created the character Matt Foley with Chris Farley at Second City?",
        "correct": "Bob Odenkirk",
        "distractors": ["Bryan Cranston", "David Cross", "Paul F. Tompkins"],
        "d": 1
    },
    # 54
    {
        "q": "Which iconic writer created the deadpan, absurd philosophical segment 'Deep Thoughts'?",
        "correct": "Jack Handey",
        "distractors": ["George Meyer", "Robert Smigel", "Jim Downey"],
        "d": 1
    },
    # 55
    {
        "q": "Who provided the calm, soothing narration voice for Jack Handey's 'Deep Thoughts' interstitials?",
        "correct": "Jack Handey himself",
        "distractors": ["Don Pardo", "Phil Hartman", "Steve Martin"],
        "d": 3
    },
    # 56
    {
        "q": "Which writer-performer was the mastermind behind 'TV Funhouse', including 'The Ambiguously Gay Duo' and puppet segments?",
        "correct": "Robert Smigel",
        "distractors": ["Conan O'Brien", "Adam McKay", "Jack Handey"],
        "d": 1
    },
    # 57
    {
        "q": "What famous foul-mouthed canine puppet character did Robert Smigel create on 'Late Night with Conan O'Brien'?",
        "correct": "Triumph the Insult Comic Dog",
        "distractors": ["Barkley the Hound", "Cynical Buster", "Scruffy the Pug"],
        "d": 1
    },
    # 58
    {
        "q": "Which writing duo served as co-head writers in Season 42 (2016-2017) and created acclaimed pre-tapes like 'Wells for Boys'?",
        "correct": "Chris Kelly and Sarah Schneider",
        "distractors": ["Colin Jost and Michael Che", "Kent Sublette and Alison Gates", "Bryan Tucker and Rob Klein"],
        "d": 2
    },
    # 59
    {
        "q": "In what year did Colin Jost and Michael Che step down as co-head writers of SNL, while remaining Weekend Update anchors?",
        "correct": "2022",
        "distractors": ["2019", "2020", "2024"],
        "d": 3
    },
    # 60
    {
        "q": "Who became co-head writers of SNL in 2022 following the tenure of Colin Jost and Michael Che?",
        "correct": "Kent Sublette, Alison Gates, and Streeter Seidell",
        "distractors": ["John Mulaney and Simon Rich", "Mikey Day and Streeter Seidell", "Dave McCary and Kyle Mooney"],
        "d": 3
    },
    # 61
    {
        "q": "Which writer-director directed many of Kyle Mooney and Beck Bennett's surreal pre-taped digital shorts before directing the film 'Brigsby Bear'?",
        "correct": "Dave McCary",
        "distractors": ["Paul Briganti", "Oz Rodriguez", "Matt Villines"],
        "d": 2
    },
    # 62
    {
        "q": "Which SNL director married Five-Timers Club member Emma Stone after they met when she hosted in 2016?",
        "correct": "Dave McCary",
        "distractors": ["Colin Jost", "Don Roy King", "Akiva Schaffer"],
        "d": 2
    },
    # 63
    {
        "q": "Which two directing partners, collectively known as 'Matt & Oz', directed dozens of visually stunning pre-taped sketches from 2011 to 2016?",
        "correct": "Matt Villines and Osmany Rodriguez",
        "distractors": ["Akiva Schaffer and Jorma Taccone", "Dave McCary and Ryan Perez", "Paul Briganti and Mike Diva"],
        "d": 3
    },
    # 64
    {
        "q": "What visual effects director joined SNL in 2021, directing high-energy, hyper-stylized digital shorts like 'Meatballs'?",
        "correct": "Mike Diva",
        "distractors": ["Dave McCary", "Paul Briganti", "Akiva Schaffer"],
        "d": 2
    },
    # 65
    {
        "q": "What is the traditional weekly production schedule on SNL: on which night do the writers pitch concepts to the host in Lorne's office?",
        "correct": "Monday evening",
        "distractors": ["Sunday morning", "Tuesday afternoon", "Wednesday night"],
        "d": 2
    },
    # 66
    {
        "q": "On which night does the entire writing staff stay up all night writing first drafts of sketches?",
        "correct": "Tuesday night into Wednesday morning",
        "distractors": ["Monday night", "Wednesday night", "Thursday night"],
        "d": 1
    },
    # 67
    {
        "q": "On which afternoon does the famous 40-to-50 sketch table read take place around the massive table in Room 8H?",
        "correct": "Wednesday afternoon",
        "distractors": ["Tuesday morning", "Thursday afternoon", "Friday morning"],
        "d": 2
    },
    # 68
    {
        "q": "Approximately how many sketches are read aloud during the Wednesday table read before Lorne and the head writers make cuts?",
        "correct": "Between 35 and 50 sketches",
        "distractors": ["Between 10 and 15 sketches", "Over 100 sketches", "Around 20 sketches"],
        "d": 2
    },
    # 69
    {
        "q": "On which day do the cast and crew block sketches on stage and rehearse camera positions for the first time?",
        "correct": "Thursday and Friday",
        "distractors": ["Wednesday night", "Saturday morning only", "Sunday afternoon"],
        "d": 2
    },
    # 70
    {
        "q": "At what time on Saturday evening does the full-length dress rehearsal begin in front of a live audience before final cuts are made?",
        "correct": "8:00 PM EST",
        "distractors": ["6:00 PM EST", "9:30 PM EST", "10:30 PM EST"],
        "d": 2
    },
    # 71
    {
        "q": "How much material is typically cut from the 8:00 PM dress rehearsal before the 11:30 PM live show airs?",
        "correct": "Approximately 20 to 30 minutes (2 to 4 entire sketches)",
        "distractors": ["Over 60 minutes", "Only about 5 minutes", "No sketches are cut, only trimmed"],
        "d": 2
    },
    # 72
    {
        "q": "What term is used for a finished sketch that was rehearsed but discarded right before or during the live broadcast?",
        "correct": "Cut for time",
        "distractors": ["Shelved on 8", "Dead on arrival", "Table draft"],
        "d": 1
    },
    # 73
    {
        "q": "Which costume designer has dressed the cast of Saturday Night Live since 1990, coordinating rapid multi-second costume changes?",
        "correct": "Tom Broecker",
        "distractors": ["Bob Mackie", "Edith Head", "Patricia Field"],
        "d": 3
    },
    # 74
    {
        "q": "How fast are some of the fastest live costume and prosthetic quick-changes executed in the wings of Studio 8H?",
        "correct": "Under 90 seconds (during commercial breaks)",
        "distractors": ["Around 10 minutes", "Between 4 and 5 minutes", "Quick-changes are not done live"],
        "d": 2
    },
    # 75
    {
        "q": "What is the longest cold open sketch in SNL history, which ran over 12 minutes in Season 42?",
        "correct": "The 2016 town hall presidential debate parody",
        "distractors": ["The 2000 Bush vs. Gore debate", "The 1975 Wolverine opening", "The 2024 Vice Presidential debate"],
        "d": 3
    },
    # 76
    {
        "q": "Which commercial parody was written by Dan Aykroyd and Chevy Chase in 1976 about a floor wax that doubled as a dessert topping?",
        "correct": "Shimmer",
        "distractors": ["Glisten", "Sparkle", "Glow-Brite"],
        "d": 2
    },
    # 77
    {
        "q": "What was the famous tag line in the 'Shimmer Floor Wax' commercial parody?",
        "correct": "It's a floor wax! No, it's a dessert topping! It's both!",
        "distractors": ["Wax your kitchen, feed your children!", "Tastes great, shines bright!", "Clean floors, sweet treats!"],
        "d": 2
    },
    # 78
    {
        "q": "Which fake commercial in Season 18 advertised a luxury car with a diamond-tipped stylus that played vinyl records on potholes?",
        "correct": "The Chameleon XLE",
        "distractors": ["The Regal Tourer", "The Stuyvesant Coupe", "The Lincoln Town Glider"],
        "d": 3
    },
    # 79
    {
        "q": "What feature did the 'Chameleon XLE' car commercial boast to keep the vehicle safe from carjackers?",
        "correct": "An exterior that looked like a rusted, dented 1972 Pontiac beat-up car",
        "distractors": ["An electrified steering wheel", "An invisible cloaking paint job", "A fake police siren on the roof"],
        "d": 3
    },
    # 80
    {
        "q": "Which fake razor commercial from the 1970s famously joked about a razor with an absurd number of blades, decades before it became real?",
        "correct": "The Triple-Trac razor (three blades)",
        "distractors": ["The Quintuple-Blade 5000", "The Octo-Shave", "The Mach-Seven"],
        "d": 2
    },
    # 81
    {
        "q": "What was the punchline tag for the 'Triple-Trac' razor in Season 1?",
        "correct": "Because you'll believe anything",
        "distractors": ["For the closest shave ever", "Three blades are better than two", "Sharpness beyond reason"],
        "d": 3
    },
    # 82
    {
        "q": "Which cast member has appeared in more total sketches than any other performer in SNL history?",
        "correct": "Kenan Thompson",
        "distractors": ["Darrell Hammond", "Phil Hartman", "Fred Armisen"],
        "d": 1
    },
    # 83
    {
        "q": "Approximately how many sketches has Kenan Thompson performed in over his record-breaking tenure?",
        "correct": "Over 1,500 sketches",
        "distractors": ["Around 500 sketches", "Around 800 sketches", "Over 3,000 sketches"],
        "d": 2
    },
    # 84
    {
        "q": "Which former cast member holds the record for the most celebrity impressions performed on the show (over 100)?",
        "correct": "Darrell Hammond",
        "distractors": ["Dana Carvey", "Bill Hader", "Jay Pharoah"],
        "d": 2
    },
    # 85
    {
        "q": "Which cast member holds the record for the most consecutive seasons appearing as an impersonator of sitting U.S. presidents (Bill Clinton for 8 years)?",
        "correct": "Darrell Hammond",
        "distractors": ["Dana Carvey", "Phil Hartman", "Will Ferrell"],
        "d": 2
    },
    # 86
    {
        "q": "Who portrayed President George W. Bush on SNL from 2000 to 2002, coining the iconic term 'Strategery'?",
        "correct": "Will Ferrell",
        "distractors": ["Darrell Hammond", "Jason Sudeikis", "Chris Parnell"],
        "d": 1
    },
    # 87
    {
        "q": "Which SNL writer actually coined the word 'Strategery' in the famous 2000 debate sketch, which the real Bush White House later adopted?",
        "correct": "Jim Downey",
        "distractors": ["Adam McKay", "Tina Fey", "Al Franken"],
        "d": 2
    },
    # 88
    {
        "q": "In that same 2000 debate sketch, what single word did Darrell Hammond's Al Gore repeat endlessly to describe his budget plan?",
        "correct": "Lockbox",
        "distractors": ["Safehouse", "Ironclad", "Fortress"],
        "d": 1
    },
    # 89
    {
        "q": "Which writer was nominated for a Primetime Emmy for co-writing the critically acclaimed 2023 sketch 'Washington's Dream'?",
        "correct": "Mikey Day, Streeter Seidell, and Nate Bargatze",
        "distractors": ["Colin Jost and Michael Che", "Kent Sublette and Alison Gates", "John Higgins and Martin Herlihy"],
        "d": 3
    },
    # 90
    {
        "q": "Which cast member portrayed British Prime Minister Theresa May on Weekend Update during the Brexit negotiations?",
        "correct": "Kate McKinnon",
        "distractors": ["Cecily Strong", "Aidy Bryant", "Vanessa Bayer"],
        "d": 2
    },
    # 91
    {
        "q": "In what year did Saturday Night Live celebrate its 25th Anniversary with a primetime special from Studio 8H?",
        "correct": "1999",
        "distractors": ["2000", "1998", "2001"],
        "d": 2
    },
    # 92
    {
        "q": "In what year did Saturday Night Live celebrate its 15th Anniversary Special?",
        "correct": "1989",
        "distractors": ["1990", "1988", "1991"],
        "d": 3
    },
    # 93
    {
        "q": "Who was the executive producer who originally developed Saturday Night Live for NBC in 1974-1975 under the title 'NBC's Saturday Night'?",
        "correct": "Dick Ebersol (alongside Lorne Michaels)",
        "distractors": ["Fred Silverman", "Grant Tinker", "Herbert Schlosser"],
        "d": 3
    },
    # 94
    {
        "q": "What NBC executive was responsible for commissioning a live late-night weekend show to replace reruns of 'The Tonight Show Starring Johnny Carson' in 1974?",
        "correct": "Herbert Schlosser",
        "distractors": ["Fred Silverman", "David Sarnoff", "Brandon Tartikoff"],
        "d": 3
    },
    # 95
    {
        "q": "Why was the show originally titled 'NBC's Saturday Night' rather than 'Saturday Night Live' when it debuted in 1975?",
        "correct": "ABC was broadcasting a competing prime-time variety show titled 'Saturday Night Live with Howard Cosell'",
        "distractors": ["CBS owned the trademark to the phrase 'Saturday Night Live'", "NBC executives felt the word 'Live' was unnecessary", "A radio show in Chicago held the federal copyright"],
        "d": 2
    },
    # 96
    {
        "q": "In what year did NBC officially change the title of the show to 'Saturday Night Live' after Howard Cosell's show was cancelled?",
        "correct": "1977 (Season 2)",
        "distractors": ["1976", "1978", "1980"],
        "d": 2
    },
    # 97
    {
        "q": "Which long-time producer served as SNL's line producer and co-producer overseeing daily physical production for over 30 years?",
        "correct": "Ken Aymong",
        "distractors": ["Steve Higgins", "Erik Kenward", "Lorne Michaels"],
        "d": 3
    },
    # 98
    {
        "q": "Which producer has served as an integral producer alongside Lorne Michaels since joining the show in the 1990s and became a senior producer in 2000?",
        "correct": "Erik Kenward",
        "distractors": ["Bryan Tucker", "Steve Higgins", "Mike Shoemaker"],
        "d": 3
    },
    # 99
    {
        "q": "Who was the head of makeup at SNL for over 30 years, transforming cast members into flawless replicas of presidents and celebrities?",
        "correct": "Louie Zakarian",
        "distractors": ["Rick Baker", "Dick Smith", "Stan Winston"],
        "d": 3
    },
    # 100
    {
        "q": "How many total Primetime Emmy Awards had Saturday Night Live won as of its 50th season milestone, more than any show in history?",
        "correct": "Over 100 Primetime Emmy Awards",
        "distractors": ["Around 50 Primetime Emmy Awards", "Around 75 Primetime Emmy Awards", "Over 200 Primetime Emmy Awards"],
        "d": 1
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "staging", "snl_batch6.json")
    build_batch(questions, out, batch_num=6)
