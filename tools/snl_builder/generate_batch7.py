#!/usr/bin/env python3
"""
Generate SNL Batch 7: Extratextual 1 - Auditions, Castings, Near Misses & Writer Histories
100 questions: exactly 30 d1, 40 d2, 30 d3.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from builder import build_batch

questions = [
    # 1
    {
        "q": "Who was the very first cast member officially hired by Lorne Michaels in 1975 for the inaugural season of Saturday Night Live?",
        "correct": "Gilda Radner",
        "distractors": ["Chevy Chase", "John Belushi", "Dan Aykroyd"],
        "d": 1
    },
    # 2
    {
        "q": "Chevy Chase was originally hired for Saturday Night Live in 1975 in what capacity before Lorne Michaels placed him on camera?",
        "correct": "As a writer only",
        "distractors": ["As a costume designer", "As an associate producer", "As a talent scout"],
        "d": 1
    },
    # 3
    {
        "q": "Which future box-office comedy superstar auditioned for SNL in 1980 and 1985, but was rejected by producers both times?",
        "correct": "Jim Carrey",
        "distractors": ["Robin Williams", "Eddie Murphy", "Martin Short"],
        "d": 1
    },
    # 4
    {
        "q": "Which future star of 'The Office' auditioned for SNL in 1995 alongside his wife Nancy Walls, but was passed over in favor of Will Ferrell?",
        "correct": "Steve Carell",
        "distractors": ["Rainn Wilson", "Ed Helms", "John Krasinski"],
        "d": 1
    },
    # 5
    {
        "q": "Which comedian and future late-night host auditioned for SNL in 1992, was rejected, but later voiced Ace in 'The Ambiguously Gay Duo'?",
        "correct": "Stephen Colbert",
        "distractors": ["Jon Stewart", "Jimmy Kimmel", "Craig Ferguson"],
        "d": 1
    },
    # 6
    {
        "q": "Which multi-hyphenate artist auditioned twice for SNL, including for the role of Barack Obama in 2008, before starring on 'Community' and winning Grammys?",
        "correct": "Donald Glover",
        "distractors": ["Jordan Peele", "Keegan-Michael Key", "Hannibal Buress"],
        "d": 1
    },
    # 7
    {
        "q": "Which future 'Friends' star auditioned for SNL in 1990, but lost the spot to Julia Sweeney?",
        "correct": "Lisa Kudrow",
        "distractors": ["Courteney Cox", "Jennifer Aniston", "David Schwimmer"],
        "d": 2
    },
    # 8
    {
        "q": "Which star of 'The Office' and 'The Mindy Project' was offered an SNL writing job in 2006, but had to turn it down due to her sitcom contract?",
        "correct": "Mindy Kaling",
        "distractors": ["Ellie Kemper", "Rashida Jones", "Angela Kinsey"],
        "d": 2
    },
    # 9
    {
        "q": "Which stand-up comic and podcast pioneer wrote a famous chapter about his disastrous 1995 meeting with Lorne Michaels over a bowl of Jolly Ranchers?",
        "correct": "Marc Maron",
        "distractors": ["Joe Rogan", "Bill Burr", "Bert Kreischer"],
        "d": 2
    },
    # 10
    {
        "q": "Which future superstar stand-up auditioned in the early 2000s doing an impression of NBA coach Avery Johnson that mystified the casting room?",
        "correct": "Kevin Hart",
        "distractors": ["Dave Chappelle", "Chris Tucker", "Katt Williams"],
        "d": 1
    },
    # 11
    {
        "q": "Which actress interned in the SNL design department, auditioned with absurd characters in 2008, and was immediately recommended for 'Parks and Recreation'?",
        "correct": "Aubrey Plaza",
        "distractors": ["Amy Poehler", "Rashida Jones", "Chelsea Peretti"],
        "d": 2
    },
    # 12
    {
        "q": "Which comedic actress auditioned in 1995 alongside Will Ferrell and Cheri Oteri, performing impressions before breaking out in 'American Pie' and 'The White Lotus'?",
        "correct": "Jennifer Coolidge",
        "distractors": ["Jane Lynch", "Megan Mullally", "Catherine O'Hara"],
        "d": 2
    },
    # 13
    {
        "q": "During his miserable season as an SNL writer in 1984-1985, which comedy legend angrily quit on Friday night and returned on Monday acting like it never happened?",
        "correct": "Larry David",
        "distractors": ["Jerry Seinfeld", "Garry Shandling", "Mel Brooks"],
        "d": 1
    },
    # 14
    {
        "q": "Which classic episode of 'Seinfeld' was directly based on Larry David quitting SNL and returning to work the following Monday?",
        "correct": "The Revenge (where George Costanza quits his job at Rick Barr Properties)",
        "distractors": ["The Contest", "The Parking Garage", "The Opposite"],
        "d": 1
    },
    # 15
    {
        "q": "How many of Larry David's sketches actually made it to air during his entire full season as an SNL writer in 1984-1985?",
        "correct": "Only one sketch (which aired at 12:55 AM)",
        "distractors": ["Zero sketches", "Five sketches", "Twelve sketches"],
        "d": 2
    },
    # 16
    {
        "q": "Which original cast member initially refused to audition because he hated television and considered it a commercial wasteland?",
        "correct": "John Belushi",
        "distractors": ["Dan Aykroyd", "Chevy Chase", "Garrett Morris"],
        "d": 2
    },
    # 17
    {
        "q": "Why was Bill Murray not among the original cast members who debuted on October 11, 1975?",
        "correct": "He had committed to ABC's 'Saturday Night Live with Howard Cosell'",
        "distractors": ["He failed the NBC medical physical exam", "He was filming a movie in Canada", "Lorne Michaels disliked his audition tape"],
        "d": 2
    },
    # 18
    {
        "q": "Which future 'Seinfeld' star met Larry David while they were both struggling cast members/writers on SNL between 1982 and 1985?",
        "correct": "Julia Louis-Dreyfus",
        "distractors": ["Michael Richards", "Jason Alexander", "Wayne Knight"],
        "d": 1
    },
    # 19
    {
        "q": "How old was Julia Louis-Dreyfus when she joined the cast of Saturday Night Live in 1982?",
        "correct": "21 years old",
        "distractors": ["18 years old", "25 years old", "28 years old"],
        "d": 2
    },
    # 20
    {
        "q": "What legendary comedy troupe in Chicago served as the primary talent feeder for SNL, supplying John Belushi, Bill Murray, Chris Farley, and Tina Fey?",
        "correct": "The Second City",
        "distractors": ["The Groundlings", "Upright Citizens Brigade", "Steppenwolf Theatre"],
        "d": 1
    },
    # 21
    {
        "q": "What Los Angeles improv school and theater supplied SNL with Phil Hartman, Jon Lovitz, Will Ferrell, Kristen Wiig, and Maya Rudolph?",
        "correct": "The Groundlings",
        "distractors": ["The Second City", "ImprovOlympic", "UCB Theatre"],
        "d": 1
    },
    # 22
    {
        "q": "What New York-based improv comedy theater co-founded by Amy Poehler became a major talent incubator for 2000s and 2010s SNL cast and writers?",
        "correct": "Upright Citizens Brigade (UCB)",
        "distractors": ["The PIT (People's Improv Theater)", "Magnet Theater", "Annoyance Theatre"],
        "d": 1
    },
    # 23
    {
        "q": "Which television star discovered Bill Hader performing at a tiny Los Angeles comedy club and personally recommended him to Lorne Michaels?",
        "correct": "Megan Mullally",
        "distractors": ["Sean Hayes", "Cheri Oteri", "Debra Messing"],
        "d": 1
    },
    # 24
    {
        "q": "What celebrity impression did Bill Hader perform during his 2005 audition that instantly captivated Lorne Michaels?",
        "correct": "An Italian man on a talk show and Al Pacino",
        "distractors": ["Christopher Walken and Jack Nicholson", "Arnold Schwarzenegger and Clint Eastwood", "Woody Allen and Robert De Niro"],
        "d": 2
    },
    # 25
    {
        "q": "What bizarre prop did Will Ferrell bring to his 1995 audition that he used to play a frantic businessman obsessed with cat toys?",
        "correct": "A briefcase filled with fake money and small cat toys",
        "distractors": ["A bowling ball wrapped in foil", "A live turtle in a shoebox", "A giant wooden mallet"],
        "d": 2
    },
    # 26
    {
        "q": "What character did Kristen Wiig perform at her 2005 audition that was put on the air almost verbatim in her very first episode?",
        "correct": "The Target Lady",
        "distractors": ["Aunt Linda", "Dooneese", "Penelope"],
        "d": 2
    },
    # 27
    {
        "q": "Why was Lorne Michaels initially hesitant to audition Kenan Thompson in 2003?",
        "correct": "Kenan had already starred on Nickelodeon's 'All That' and Lorne preferred fresh discoveries",
        "distractors": ["Kenan had never performed live sketch comedy", "Kenan was under exclusive contract with Disney", "Kenan was living in London at the time"],
        "d": 2
    },
    # 28
    {
        "q": "Which stand-up comic and 'Between Two Ferns' host spent two weeks as an SNL guest writer in 1999 before leaving the show?",
        "correct": "Zach Galifianakis",
        "distractors": ["Demetri Martin", "Todd Barry", "Nick Swardson"],
        "d": 2
    },
    # 29
    {
        "q": "What absurd sketch idea did Zach Galifianakis pitch to host Britney Spears during his brief 1999 writing stint?",
        "correct": "An interview where his belly button eats a submarine sandwich",
        "distractors": ["Britney shopping for vintage military tanks", "A duet with a singing toaster", "A dance battle against a librarian"],
        "d": 3
    },
    # 30
    {
        "q": "Which future 'Arrested Development' and 'Mr. Show' star auditioned for SNL in 1990 and was turned down?",
        "correct": "David Cross",
        "distractors": ["Will Arnett", "Tony Hale", "Jason Bateman"],
        "d": 2
    },
    # 31
    {
        "q": "Which future 'Modern Family' star auditioned for SNL in the 1990s, doing impressions of Christopher Walken and various anchors?",
        "correct": "Ty Burrell",
        "distractors": ["Ed O'Neill", "Jesse Tyler Ferguson", "Eric Stonestreet"],
        "d": 3
    },
    # 32
    {
        "q": "Which comedy star was hired as an SNL writer in 2008 and wrote famous sketches like 'What Up with That?' and 'Diner Lobster' before becoming a Five-Timers host?",
        "correct": "John Mulaney",
        "distractors": ["Simon Rich", "Mike O'Brien", "Jorma Taccone"],
        "d": 1
    },
    # 33
    {
        "q": "Which acclaimed writer published best-selling comedic short story collections like 'Ant Farm' and 'Sell Out' while on the SNL writing staff?",
        "correct": "Simon Rich",
        "distractors": ["John Mulaney", "Streeter Seidell", "Colin Jost"],
        "d": 2
    },
    # 34
    {
        "q": "How old was Simon Rich when he was hired as an SNL writer in 2007, making him one of the youngest writers in the show's history?",
        "correct": "23 years old",
        "distractors": ["19 years old", "21 years old", "26 years old"],
        "d": 3
    },
    # 35
    {
        "q": "Which future stand-up superstar and 'Broad City' executive producer was a staff writer on SNL from 2009 to 2010?",
        "correct": "Hannibal Buress",
        "distractors": ["John Mulaney", "Michael Che", "Pete Davidson"],
        "d": 2
    },
    # 36
    {
        "q": "Which beloved digital short creator was an SNL writer from 2007 to 2015 and starred in '7 Minutes in Heaven' webisodes from a closet?",
        "correct": "Mike O'Brien",
        "distractors": ["John Higgins", "Martin Herlihy", "Tim Robinson"],
        "d": 2
    },
    # 37
    {
        "q": "Which creator of Netflix's 'I Think You Should Leave' was an SNL cast member for Season 38 (2012-2013) and then moved to the writing staff?",
        "correct": "Tim Robinson",
        "distractors": ["Sam Richardson", "Kyle Mooney", "Beck Bennett"],
        "d": 1
    },
    # 38
    {
        "q": "What was the name of the viral sketch written by Tim Robinson and Zach Kanin about a baby who is an absolute jerk?",
        "correct": "Baby Boss / Baby Crying",
        "distractors": ["Infant Terror", "Bratty Toddler", "Diaper Dave"],
        "d": 3
    },
    # 39
    {
        "q": "Which iconic Second City performer was hired to join SNL in 1981, but quit before her first episode aired because of backstage chaos under Jean Doumanian?",
        "correct": "Catherine O'Hara",
        "distractors": ["Andrea Martin", "Gail Matthius", "Robin Duke"],
        "d": 2
    },
    # 40
    {
        "q": "Who replaced Catherine O'Hara on the cast after O'Hara walked away before Season 6 began airing?",
        "correct": "Robin Duke",
        "distractors": ["Mary Gross", "Julia Louis-Dreyfus", "Denny Dillon"],
        "d": 3
    },
    # 41
    {
        "q": "Which 'Key & Peele' star auditioned for SNL in 2008 to portray Barack Obama, narrowly losing out to Fred Armisen?",
        "correct": "Jordan Peele",
        "distractors": ["Keegan-Michael Key", "Jay Pharoah", "Dean Edwards"],
        "d": 2
    },
    # 42
    {
        "q": "Which famous actor and director was cast in Season 11 (1985-1986) along with Robert Downey Jr., but was let go after one season?",
        "correct": "Anthony Michael Hall",
        "distractors": ["Judd Nelson", "Emilio Estevez", "Rob Lowe"],
        "d": 2
    },
    # 43
    {
        "q": "Which Academy Award-nominated actor and brother of Randy Quaid was an SNL cast member during the 1985-1986 season?",
        "correct": "Randy Quaid",
        "distractors": ["Dennis Quaid", "Beau Bridges", "Jeff Daniels"],
        "d": 2
    },
    # 44
    {
        "q": "What ranking did Rolling Stone notoriously give to Robert Downey Jr. in its 2015 retrospective ranking of all 145 SNL cast members?",
        "correct": "Dead last (Number 145)",
        "distractors": ["Number 100", "Number 120", "Number 135"],
        "d": 2
    },
    # 45
    {
        "q": "Which performer did Rolling Stone rank as the Number 1 greatest SNL cast member of all time in that 2015 list?",
        "correct": "John Belushi",
        "distractors": ["Eddie Murphy", "Phil Hartman", "Will Ferrell"],
        "d": 2
    },
    # 46
    {
        "q": "Which performer was ranked Number 2 on Rolling Stone's 2015 list, celebrated for saving the show during the early 1980s?",
        "correct": "Eddie Murphy",
        "distractors": ["Dana Carvey", "Bill Murray", "Tina Fey"],
        "d": 2
    },
    # 47
    {
        "q": "Which stand-up comedian auditioned for SNL by performing an impression of Christopher Walken giving a speech to kids, which landed him on the show in 2005?",
        "correct": "Jason Sudeikis",
        "distractors": ["Bill Hader", "Andy Samberg", "Fred Armisen"],
        "d": 2
    },
    # 48
    {
        "q": "Jason Sudeikis was originally hired on SNL in 2003 in what position before joining the cast in 2005?",
        "correct": "Staff writer",
        "distractors": ["Production assistant", "Talent scout", "Cue-card grip"],
        "d": 2
    },
    # 49
    {
        "q": "Which comedy star was hired as a featured player in 2012, spent only one season on camera, and became a massive sitcom star on 'Fresh Off the Boat'?",
        "correct": "Randall Park (auditioned) / Tim Robinson",
        "distractors": ["Kumail Nanjiani", "Ronny Chieng", "Jimmy O. Yang"],
        "d": 3
    },
    # 50
    {
        "q": "Which actress auditioned in 2000, was hired in 2001, and became famous for her impressions of Donatella Versace, Whitney Houston, and Maya Angelou?",
        "correct": "Maya Rudolph",
        "distractors": ["Ana Gasteyer", "Cheri Oteri", "Rachel Dratch"],
        "d": 1
    },
    # 51
    {
        "q": "Who is Maya Rudolph's famous singer mother, known for the multi-octave 1975 hit 'Lovin' You'?",
        "correct": "Minnie Riperton",
        "distractors": ["Chaka Khan", "Donna Summer", "Roberta Flack"],
        "d": 1
    },
    # 52
    {
        "q": "Which Second City Chicago duo known for their two-woman stage show were hired together by Lorne Michaels in 1999?",
        "correct": "Tina Fey and Rachel Dratch",
        "distractors": ["Amy Poehler and Tina Fey", "Kristen Wiig and Maya Rudolph", "Aidy Bryant and Cecily Strong"],
        "d": 2
    },
    # 53
    {
        "q": "What was the title of Tina Fey and Rachel Dratch's hit two-woman comedy revue at Chicago's Second City that caught Lorne's attention?",
        "correct": "Dratch & Fey",
        "distractors": ["Two Women Talking", "Windy City Ladies", "Fey & Dratch Live"],
        "d": 2
    },
    # 54
    {
        "q": "Which cast member was hired after submitting a homemade VHS audition tape featuring impressions of Prince and an elderly blind man?",
        "correct": "Fred Armisen",
        "distractors": ["Bill Hader", "Andy Samberg", "Horatio Sanz"],
        "d": 2
    },
    # 55
    {
        "q": "Before entering comedy and joining SNL, what was Fred Armisen's primary career in the late 1980s and 1990s?",
        "correct": "A professional rock drummer (for Trenchmouth and Blue Man Group)",
        "distractors": ["A graphic designer for album covers", "A classical ballet dancer", "A professional skateboarder"],
        "d": 2
    },
    # 56
    {
        "q": "Which current cast member was hired in 2019 as a writer, promoted to cast, and became the first Chinese-American cast member in SNL history?",
        "correct": "Bowen Yang",
        "distractors": ["Devon Walker", "Andrew Dismukes", "Marcello Hernandez"],
        "d": 1
    },
    # 57
    {
        "q": "What viral social media videos helped Bowen Yang gain national attention before being hired at SNL?",
        "correct": "Lip-syncing dramatic pop-culture movie and TV dialogue on Twitter",
        "distractors": ["Pranking strangers on the NYC subway on TikTok", "Cooking gourmet meals while reviewing Broadway shows", "Impersonating Disney princesses singing rap songs"],
        "d": 2
    },
    # 58
    {
        "q": "Which stand-up comic joined SNL as a writer in 2017 before being promoted to featured player in 2020?",
        "correct": "Andrew Dismukes",
        "distractors": ["Michael Longfellow", "James Austin Johnson", "Punkie Johnson"],
        "d": 2
    },
    # 59
    {
        "q": "Which cast member was the first openly non-binary performer hired in the cast of Saturday Night Live in 2022?",
        "correct": "Molly Kearney",
        "distractors": ["Punkie Johnson", "Sarah Sherman", "Chloe Troast"],
        "d": 2
    },
    # 60
    {
        "q": "Which stand-up comedian was announced as a new cast member in September 2019, but was fired just four days later after past racist podcast clips surfaced?",
        "correct": "Shane Gillis",
        "distractors": ["Matt McCusker", "Mark Normand", "Theo Von"],
        "d": 1
    },
    # 61
    {
        "q": "In February 2024, what major milestone did Shane Gillis achieve after having been fired before his first season in 2019?",
        "correct": "He returned to Studio 8H to host the show",
        "distractors": ["He was re-hired as head writer", "He won a Primetime Emmy for writing", "He performed as musical guest"],
        "d": 1
    },
    # 62
    {
        "q": "What was Shane Gillis' self-deprecating opening line in his February 2024 monologue?",
        "correct": "Yeah, I probably shouldn't be up here, honestly",
        "distractors": ["Well, that took long enough!", "Look who's back in the building!", "Did you miss me?"],
        "d": 2
    },
    # 63
    {
        "q": "Which ground-breaking female cast member joined SNL in 1985 as the show's first Black female repertory player?",
        "correct": "Danitra Vance",
        "distractors": ["Yvonne Hudson", "Ellen Cleghorne", "Sasheer Zamata"],
        "d": 2
    },
    # 64
    {
        "q": "Which Black actress was a featured player on SNL in Season 6 (1980-1981) and became the first Black woman credited in the cast?",
        "correct": "Yvonne Hudson",
        "distractors": ["Danitra Vance", "Ellen Cleghorne", "Sasheer Zamata"],
        "d": 3
    },
    # 65
    {
        "q": "Which stand-up comic joined the cast in 1991, becoming the first Black woman to spend more than one season as a repertory player?",
        "correct": "Ellen Cleghorne",
        "distractors": ["Danitra Vance", "Leslie Jones", "Maya Rudolph"],
        "d": 2
    },
    # 66
    {
        "q": "Which comedian joined SNL as a writer in early 2014, was promoted to cast in October 2014 at age 47, and earned two Emmy nominations?",
        "correct": "Leslie Jones",
        "distractors": ["Wanda Sykes", "Tiffany Haddish", "Sherri Shepherd"],
        "d": 1
    },
    # 67
    {
        "q": "Who was the oldest rookie cast member ever hired in Saturday Night Live history at age 47?",
        "correct": "Leslie Jones",
        "distractors": ["Michael McKean", "George Coe", "Darrell Hammond"],
        "d": 1
    },
    # 68
    {
        "q": "Which veteran comedy actor joined the SNL cast in 1994 at age 46 after already starring in 'Laverne & Shirley' and 'This Is Spinal Tap'?",
        "correct": "Michael McKean",
        "distractors": ["Christopher Guest", "Harry Shearer", "Martin Short"],
        "d": 2
    },
    # 69
    {
        "q": "Who is the only person to have been an SNL musical guest, a host, and a repertory cast member across his career?",
        "correct": "Michael McKean",
        "distractors": ["Bill Murray", "Paul Simon", "Dan Aykroyd"],
        "d": 2
    },
    # 70
    {
        "q": "Which original 'Spinal Tap' bassist joined SNL twice as a cast member (1979-1980 and 1984-1985) and quit both times due to creative frustration?",
        "correct": "Harry Shearer",
        "distractors": ["Christopher Guest", "Michael McKean", "Rob Reiner"],
        "d": 2
    },
    # 71
    {
        "q": "Which legendary improv comic and director of 'Waiting for Guffman' joined the SNL cast for the star-studded 1984-1985 season?",
        "correct": "Christopher Guest",
        "distractors": ["Eugene Levy", "John Candy", "Rick Moranis"],
        "d": 2
    },
    # 72
    {
        "q": "Which famous SCTV stars were invited to join SNL in 1984 by Dick Ebersol for a single one-year 'all-star' season?",
        "correct": "Martin Short, Billy Crystal, and Christopher Guest",
        "distractors": ["John Candy, Eugene Levy, and Catherine O'Hara", "Rick Moranis, Dave Thomas, and Joe Flaherty", "Andrea Martin, Harold Ramis, and Robin Duke"],
        "d": 2
    },
    # 73
    {
        "q": "Why was Billy Crystal's original appearance in SNL's very first episode on October 11, 1975 abruptly cancelled hours before airtime?",
        "correct": "His stand-up monologue was cut down to two minutes due to time constraints, so his manager pulled him",
        "distractors": ["He came down with acute laryngitis backstage", "He had an argument with host George Carlin", "Lorne Michaels fired him during dress rehearsal"],
        "d": 2
    },
    # 74
    {
        "q": "In what season did Billy Crystal finally join SNL as a full-time cast member, nine years after being cut from the premiere?",
        "correct": "Season 10 (1984-1985)",
        "distractors": ["Season 8 (1982-1983)", "Season 11 (1985-1986)", "Season 12 (1986-1987)"],
        "d": 2
    },
    # 75
    {
        "q": "Which Groundlings alumna auditioned in 1995 with the character of an overly enthusiastic middle-school teacher and was hired immediately?",
        "correct": "Cheri Oteri",
        "distractors": ["Molly Shannon", "Ana Gasteyer", "Rachel Dratch"],
        "d": 2
    },
    # 76
    {
        "q": "Which future 'Silicon Valley' and 'Portlandia' star auditioned for SNL in 2009 and later appeared as a writer and guest performer?",
        "correct": "Kumail Nanjiani (auditioned) / Carrie Brownstein",
        "distractors": ["Thomas Middleditch", "Martin Starr", "Zach Woods"],
        "d": 3
    },
    # 77
    {
        "q": "Which future 'Unbreakable Kimmy Schmidt' star auditioned for SNL in 2008 and was cast in 'The Office' shortly thereafter?",
        "correct": "Ellie Kemper",
        "distractors": ["Jane Krakowski", "Tituss Burgess", "Carol Kane"],
        "d": 2
    },
    # 78
    {
        "q": "Which comedian and impressionist was hired in 2010 and was famous for uncanny impressions of Denzel Washington, Will Smith, and Barack Obama?",
        "correct": "Jay Pharoah",
        "distractors": ["Dean Edwards", "Finesse Mitchell", "Chris Redd"],
        "d": 1
    },
    # 79
    {
        "q": "Which cast member was hired in 2010 and became famous for her impressions of Miley Cyrus, Hillary Clinton, and the 'Secret Word' contestant?",
        "correct": "Vanessa Bayer",
        "distractors": ["Nasim Pedrad", "Abby Elliott", "Heidi Gardner"],
        "d": 2
    },
    # 80
    {
        "q": "Who was the first Iranian-American cast member in Saturday Night Live history, joining the show in 2009?",
        "correct": "Nasim Pedrad",
        "distractors": ["Vanessa Bayer", "Noël Wells", "Melissa Villaseñor"],
        "d": 2
    },
    # 81
    {
        "q": "Who was the first Latina cast member in Saturday Night Live history, hired in 2016?",
        "correct": "Melissa Villaseñor",
        "distractors": ["Ego Nwodim", "Sasheer Zamata", "Chloe Fineman"],
        "d": 1
    },
    # 82
    {
        "q": "Which cast member who joined in 2008 is the daughter of former SNL cast member Chris Elliott?",
        "correct": "Abby Elliott",
        "distractors": ["Casey Wilson", "Michaela Watkins", "Jenny Slate"],
        "d": 2
    },
    # 83
    {
        "q": "Who was Abby Elliott's grandfather, making her part of the first three-generation family to perform on SNL?",
        "correct": "Bob Elliott (of comedy duo Bob and Ray)",
        "distractors": ["Jack Paar", "Carl Reiner", "Mel Brooks"],
        "d": 3
    },
    # 84
    {
        "q": "Which cast member was fired after just one season (2008-2009) despite creating popular characters like Angie Tempura on 'Bitch Plez'?",
        "correct": "Michaela Watkins",
        "distractors": ["Casey Wilson", "Abby Elliott", "Jenny Slate"],
        "d": 2
    },
    # 85
    {
        "q": "What reason did Lorne Michaels famously give Michaela Watkins when letting her go after Season 34?",
        "correct": "He told her she deserved to have her own television show rather than being stuck on SNL",
        "distractors": ["He said she missed too many table reads", "He told her the network mandated budget cuts", "He said she broke character too frequently"],
        "d": 2
    },
    # 86
    {
        "q": "Which future 'Happy Endings' star was a cast member for two seasons from 2008 to 2009 before being let go?",
        "correct": "Casey Wilson",
        "distractors": ["Elisha Cuthbert", "Eliza Coupe", "Michaela Watkins"],
        "d": 2
    },
    # 87
    {
        "q": "Which cast member was hired in 2012, left after one season, and went on to create and star in Netflix's 'Master of None' and direct 'Mr. Roosevelt'?",
        "correct": "Noël Wells",
        "distractors": ["Sasheer Zamata", "Brooks Wheelan", "John Milhiser"],
        "d": 2
    },
    # 88
    {
        "q": "Which stand-up comic joined in Season 39 (2013-2014) and later turned his single-season firing into a hit stand-up comedy special?",
        "correct": "Brooks Wheelan",
        "distractors": ["John Milhiser", "Mike O'Brien", "Luke Null"],
        "d": 3
    },
    # 89
    {
        "q": "Which musical comedian was hired for Season 43 (2017-2018) with a guitar in his audition, only to be let go after one season?",
        "correct": "Luke Null",
        "distractors": ["Paul Brittain", "Jon Rudnitsky", "Alex Moffat"],
        "d": 3
    },
    # 90
    {
        "q": "Which stand-up comedian and impressionist joined the cast in 2015, famously performing an elaborate 'Dirty Dancing' routine on Weekend Update?",
        "correct": "Jon Rudnitsky",
        "distractors": ["Pete Davidson", "Chris Redd", "Brooks Wheelan"],
        "d": 3
    },
    # 91
    {
        "q": "Which Groundlings alumnus joined in 2010 and played eccentric characters like 'Lord Cecil Wyndemere' and 'Sex' ed teacher Greg Stink?",
        "correct": "Paul Brittain",
        "distractors": ["Taran Killam", "Bobby Moynihan", "Tim Robinson"],
        "d": 3
    },
    # 92
    {
        "q": "Which prolific cast member joined in 2010, performed for six seasons, and played characters like Jebidiah Atkinson and movie villains?",
        "correct": "Taran Killam",
        "distractors": ["Jay Pharoah", "Alex Moffat", "Beck Bennett"],
        "d": 1
    },
    # 93
    {
        "q": "Which popular cast member was hired in 2008 and spent nine seasons playing iconic characters like Drunk Uncle and Jacob the Bar Mitzvah Boy?",
        "correct": "Bobby Moynihan",
        "distractors": ["Horatio Sanz", "Andy Samberg", "Bill Hader"],
        "d": 1
    },
    # 94
    {
        "q": "Which cast member was hired in 1998 and spent eight seasons on SNL, famous for playing Aaron Neville and constantly cracking up on air with Jimmy Fallon?",
        "correct": "Horatio Sanz",
        "distractors": ["Chris Kattan", "Tracy Morgan", "Finesse Mitchell"],
        "d": 1
    },
    # 95
    {
        "q": "Which stand-up comedian was hired in 2017 and won an Emmy in 2018 for co-writing the musical parody 'Come Back Barack'?",
        "correct": "Chris Redd",
        "distractors": ["Jay Pharoah", "Pete Davidson", "Kenan Thompson"],
        "d": 2
    },
    # 96
    {
        "q": "Which member of Please Don't Destroy is the son of legendary longtime SNL head writer and producer Steve Higgins?",
        "correct": "John Higgins",
        "distractors": ["Martin Herlihy", "Ben Marshall", "Streeter Seidell"],
        "d": 2
    },
    # 97
    {
        "q": "Which member of Please Don't Destroy is the son of former SNL head writer and Weekend Update writer Tim Herlihy?",
        "correct": "Martin Herlihy",
        "distractors": ["John Higgins", "Ben Marshall", "Dave McCary"],
        "d": 2
    },
    # 98
    {
        "q": "What college comedy troupe at NYU did the three members of Please Don't Destroy form before joining SNL?",
        "correct": "Hammerkatz",
        "distractors": ["Dangerbox", "The Upright Citizens", "The Lampooners"],
        "d": 3
    },
    # 99
    {
        "q": "Which current cast member joined in Season 47 (2021) and was previously an acclaimed impressionist on YouTube doing Trump and podcast hosts?",
        "correct": "James Austin Johnson",
        "distractors": ["Andrew Dismukes", "Michael Longfellow", "Devon Walker"],
        "d": 1
    },
    # 100
    {
        "q": "Who was the first openly gay male cast member in Saturday Night Live history, joining in 1985?",
        "correct": "Terry Sweeney",
        "distractors": ["John Milhiser", "Bowen Yang", "Danitra Vance"],
        "d": 2
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "staging", "snl_batch7.json")
    build_batch(questions, out, batch_num=7)
