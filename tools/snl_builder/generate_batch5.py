#!/usr/bin/env python3
"""
Generate SNL Batch 5: Metatextual 1 - Five-Timers Club, Hosts, Season Openers & Milestones
100 questions: exactly 30 d1, 40 d2, 30 d3.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from builder import build_batch

questions = [
    # 1
    {
        "q": "Who was the host of the very first episode of Saturday Night Live on October 11, 1975?",
        "correct": "George Carlin",
        "distractors": ["Steve Martin", "Chevy Chase", "Richard Pryor"],
        "d": 1
    },
    # 2
    {
        "q": "What was unique about George Carlin's hosting stint on the series premiere?",
        "correct": "He did not appear in any sketches, only performing stand-up monologues",
        "distractors": ["He refused to wear shoes on the stage", "He co-anchored Weekend Update from a couch", "He performed as both host and musical guest"],
        "d": 2
    },
    # 3
    {
        "q": "Who were the two musical guests featured on the first-ever episode of SNL?",
        "correct": "Billy Preston and Janis Ian",
        "distractors": ["Paul Simon and Phoebe Snow", "Joe Cocker and Randy Newman", "Stevie Wonder and Bonnie Raitt"],
        "d": 2
    },
    # 4
    {
        "q": "Who was the first woman ever to host Saturday Night Live (Season 1, Episode 4)?",
        "correct": "Candice Bergen",
        "distractors": ["Lily Tomlin", "Raquel Welch", "Louise Lasser"],
        "d": 2
    },
    # 5
    {
        "q": "Who holds the record as the youngest person ever to host Saturday Night Live at just seven years old?",
        "correct": "Drew Barrymore",
        "distractors": ["Macaulay Culkin", "Fred Savage", "Jodie Foster"],
        "d": 1
    },
    # 6
    {
        "q": "In what year and following the release of what blockbuster film did 7-year-old Drew Barrymore host SNL?",
        "correct": "1982, following 'E.T. the Extra-Terrestrial'",
        "distractors": ["1984, following 'Firestarter'", "1980, following 'Altered States'", "1985, following 'Cat's Eye'"],
        "d": 2
    },
    # 7
    {
        "q": "Who holds the record as the oldest person ever to host Saturday Night Live, hosting at age 88 in May 2010?",
        "correct": "Betty White",
        "distractors": ["Carl Reiner", "Mel Brooks", "Angela Lansbury"],
        "d": 1
    },
    # 8
    {
        "q": "What grassroots social media phenomenon directly convinced Lorne Michaels to book Betty White as host in 2010?",
        "correct": "A viral Facebook campaign that gathered hundreds of thousands of members",
        "distractors": ["A trending petition on Twitter with celebrity retweets", "A viral Kickstarter campaign raising charity funds", "A fan-made YouTube video series"],
        "d": 2
    },
    # 9
    {
        "q": "Who holds the all-time record for hosting Saturday Night Live the most times, with 17 hosting gigs?",
        "correct": "Alec Baldwin",
        "distractors": ["Steve Martin", "John Goodman", "Tom Hanks"],
        "d": 1
    },
    # 10
    {
        "q": "Who holds the second-place record for hosting SNL, with 16 hosting appearances?",
        "correct": "Steve Martin",
        "distractors": ["Buck Henry", "John Goodman", "Chevy Chase"],
        "d": 1
    },
    # 11
    {
        "q": "Which actor hosted the season finale of SNL for the first five consecutive seasons (1976-1980)?",
        "correct": "Buck Henry",
        "distractors": ["Steve Martin", "Elliott Gould", "Candice Bergen"],
        "d": 2
    },
    # 12
    {
        "q": "In which host's December 8, 1990 monologue was the 'Five-Timers Club' sketch introduced?",
        "correct": "Tom Hanks",
        "distractors": ["Steve Martin", "Buck Henry", "Paul Simon"],
        "d": 1
    },
    # 13
    {
        "q": "Which two writers co-wrote the iconic original 1990 'Five-Timers Club' sketch starring Tom Hanks?",
        "correct": "Conan O'Brien and Robert Smigel",
        "distractors": ["Adam McKay and Will Ferrell", "Jim Downey and Al Franken", "Jack Handey and George Meyer"],
        "d": 2
    },
    # 14
    {
        "q": "What garment is traditionally bestowed upon hosts when they join the Five-Timers Club?",
        "correct": "A plush velvet robe with a gold '5' patch",
        "distractors": ["A solid gold wrist watch", "A platinum lapel pin", "A custom silk smoking jacket"],
        "d": 1
    },
    # 15
    {
        "q": "Which cast member played the club waiter serving drinks in the original 1990 Five-Timers Club sketch?",
        "correct": "Jon Lovitz",
        "distractors": ["Dana Carvey", "Phil Hartman", "Kevin Nealon"],
        "d": 2
    },
    # 16
    {
        "q": "Which singer-songwriter appeared in the original Five-Timers Club sketch wearing a special robe with the number '4' or '4 1/2'?",
        "correct": "Paul Simon",
        "distractors": ["James Taylor", "Art Garfunkel", "Randy Newman"],
        "d": 2
    },
    # 17
    {
        "q": "Who was the first woman inducted into the Five-Timers Club?",
        "correct": "Candice Bergen",
        "distractors": ["Drew Barrymore", "Tina Fey", "Scarlett Johansson"],
        "d": 2
    },
    # 18
    {
        "q": "Which former SNL cast member was the first female former cast member to join the Five-Timers Club?",
        "correct": "Tina Fey",
        "distractors": ["Amy Poehler", "Kristen Wiig", "Maya Rudolph"],
        "d": 2
    },
    # 19
    {
        "q": "Which actress joined the Five-Timers Club in December 2023, inducted by Tina Fey and Candice Bergen?",
        "correct": "Emma Stone",
        "distractors": ["Scarlett Johansson", "Melissa McCarthy", "Kristen Wiig"],
        "d": 2
    },
    # 20
    {
        "q": "Which former cast member was inducted into the Five-Timers Club in April 2024?",
        "correct": "Kristen Wiig",
        "distractors": ["Maya Rudolph", "Amy Poehler", "Kate McKinnon"],
        "d": 1
    },
    # 21
    {
        "q": "In December 2021, why was Paul Rudd's Five-Timers Club induction episode broadcast with no live studio audience?",
        "correct": "The Omicron COVID-19 surge caused a sudden safety shutdown hours before showtime",
        "distractors": ["Studio 8H suffered an electrical grid fire", "A blizzard stranded the crew across New York", "Lorne Michaels fell ill with the flu"],
        "d": 2
    },
    # 22
    {
        "q": "Who were the only two celebrity guests present to induct Paul Rudd into the Five-Timers Club on that December 2021 broadcast?",
        "correct": "Tom Hanks and Tina Fey",
        "distractors": ["Steve Martin and Martin Short", "Alec Baldwin and John Mulaney", "Scarlett Johansson and Bill Murray"],
        "d": 2
    },
    # 23
    {
        "q": "Which former SNL writer became the fourth former writer (never a cast member) to join the Five-Timers Club in February 2022?",
        "correct": "John Mulaney",
        "distractors": ["Larry David", "Conan O'Brien", "Bob Odenkirk"],
        "d": 1
    },
    # 24
    {
        "q": "What sum of money did Lorne Michaels famously offer live on air in 1976 for The Beatles to reunite on SNL?",
        "correct": "$3,000 (later raised to $3,200)",
        "distractors": ["$10,000", "$50,000", "$1,000,000"],
        "d": 1
    },
    # 25
    {
        "q": "According to Paul McCartney and John Lennon, where were they watching Lorne Michaels offer the $3,000 Beatles reunion check?",
        "correct": "At John Lennon's apartment in the Dakota, just blocks away, nearly taking a cab over",
        "distractors": ["At a recording studio in London", "At a dinner party in Beverly Hills", "At Central Park listening on portable radio"],
        "d": 2
    },
    # 26
    {
        "q": "Which Beatle actually appeared on SNL alongside Paul Simon just weeks after Lorne's offer in November 1976?",
        "correct": "George Harrison",
        "distractors": ["John Lennon", "Paul McCartney", "Ringo Starr"],
        "d": 2
    },
    # 27
    {
        "q": "Which Beatle hosted an episode of Saturday Night Live in December 1984?",
        "correct": "Ringo Starr",
        "distractors": ["George Harrison", "Paul McCartney", "John Lennon"],
        "d": 2
    },
    # 28
    {
        "q": "What British rock band made their only appearance on SNL on September 25, 1982, which proved to be Freddie Mercury's final U.S. performance?",
        "correct": "Queen",
        "distractors": ["The Who", "Led Zeppelin", "The Rolling Stones"],
        "d": 2
    },
    # 29
    {
        "q": "Which iconic Seattle grunge band performed 'Smells Like Teen Spirit' and 'Territorial Pissings' on January 11, 1992, smashing their instruments?",
        "correct": "Nirvana",
        "distractors": ["Pearl Jam", "Soundgarden", "Alice in Chains"],
        "d": 1
    },
    # 30
    {
        "q": "Who was the celebrity host on the night Nirvana performed and tore up the SNL stage in January 1992?",
        "correct": "Charles Barkley",
        "distractors": ["Michael Jordan", "Wayne Gretzky", "Dennis Rodman"],
        "d": 2
    },
    # 31
    {
        "q": "What legendary music artist performed an unprecedented eight-minute continuous medley with 3RDEYEGIRL in November 2014?",
        "correct": "Prince",
        "distractors": ["Stevie Wonder", "David Bowie", "Bruce Springsteen"],
        "d": 2
    },
    # 32
    {
        "q": "Who was the host of the episode where Prince delivered his unbroken 8-minute musical performance?",
        "correct": "Chris Rock",
        "distractors": ["Dave Chappelle", "Eddie Murphy", "Tracy Morgan"],
        "d": 2
    },
    # 33
    {
        "q": "Which avant-garde German countertenor and performance artist performed backing vocals for David Bowie on SNL in December 1979?",
        "correct": "Klaus Nomi",
        "distractors": ["Falco", "Nina Hagen", "Peter Schilling"],
        "d": 3
    },
    # 34
    {
        "q": "What costume was David Bowie locked inside during his 1979 performance of 'The Man Who Sold the World'?",
        "correct": "A rigid, oversized Bauhaus-inspired black-and-white tuxedo",
        "distractors": ["A glass cube on wheels", "A silver metallic astronaut spacesuit", "A mechanical spider corset"],
        "d": 3
    },
    # 35
    {
        "q": "Who hosted the milestone 100th episode of Saturday Night Live on March 15, 1980?",
        "correct": "Bob Newhart",
        "distractors": ["Steve Martin", "Buck Henry", "Elliott Gould"],
        "d": 3
    },
    # 36
    {
        "q": "In May 2021, which tech billionaire hosted SNL, becoming one of the few business executives to host the show?",
        "correct": "Elon Musk",
        "distractors": ["Jeff Bezos", "Bill Gates", "Mark Zuckerberg"],
        "d": 1
    },
    # 37
    {
        "q": "Who was the musical guest on the May 2021 episode hosted by Elon Musk?",
        "correct": "Miley Cyrus",
        "distractors": ["Grimes", "The Weeknd", "Doja Cat"],
        "d": 2
    },
    # 38
    {
        "q": "In February 2015, NBC aired the 'Saturday Night Live 40th Anniversary Special'. How long was the primetime broadcast?",
        "correct": "Three and a half hours",
        "distractors": ["Two hours", "Four hours", "Ninety minutes"],
        "d": 2
    },
    # 39
    {
        "q": "Approximately how many viewers tuned in to the live broadcast of the SNL 40th Anniversary Special in 2015?",
        "correct": "Over 23 million viewers",
        "distractors": ["Around 10 million viewers", "Over 40 million viewers", "Around 15 million viewers"],
        "d": 3
    },
    # 40
    {
        "q": "Who hosted the landmark Season 40 premiere in September 2014, riding high off 'Guardians of the Galaxy'?",
        "correct": "Chris Pratt",
        "distractors": ["Chris Evans", "Chris Hemsworth", "Paul Rudd"],
        "d": 2
    },
    # 41
    {
        "q": "Who hosted the Season 25 premiere in October 1999?",
        "correct": "Jerry Seinfeld",
        "distractors": ["Tom Hanks", "Alec Baldwin", "David Letterman"],
        "d": 2
    },
    # 42
    {
        "q": "Which music superstar pulled double duty as host and musical guest in October 2000, promoting 'Oops!... I Did It Again'?",
        "correct": "Britney Spears",
        "distractors": ["Christina Aguilera", "Jessica Simpson", "Mandy Moore"],
        "d": 2
    },
    # 43
    {
        "q": "Which artist performed double duty as host and musical guest in 2012, showcasing an uncanny impression of Justin Bieber?",
        "correct": "Bruno Mars",
        "distractors": ["Justin Timberlake", "Adam Levine", "Drake"],
        "d": 2
    },
    # 44
    {
        "q": "Which rapper and actor pulled double duty in May 2018 under his real name and musical moniker Childish Gambino?",
        "correct": "Donald Glover",
        "distractors": ["Common", "Ludacris", "Will Smith"],
        "d": 1
    },
    # 45
    {
        "q": "What politically charged music video was premiered online by Childish Gambino immediately following his 2018 SNL performance?",
        "correct": "This Is America",
        "distractors": ["Redbone", "Sober", "Feels Like Summer"],
        "d": 1
    },
    # 46
    {
        "q": "Which British pop superstar pulled double duty in December 2021, performing 'Happier Than Ever' in an oversized Victorian doll dress?",
        "correct": "Billie Eilish",
        "distractors": ["Dua Lipa", "Adele", "Charli XCX"],
        "d": 2
    },
    # 47
    {
        "q": "Which country music icon pulled double duty as host and musical guest in March 1989?",
        "correct": "Dolly Parton",
        "distractors": ["Reba McEntire", "Loretta Lynn", "Emmylou Harris"],
        "d": 2
    },
    # 48
    {
        "q": "Which hip-hop artist hosted and served as musical guest on October 20, 1990, performing 'U Can't Touch This'?",
        "correct": "MC Hammer",
        "distractors": ["Vanilla Ice", "Tone Loc", "LL Cool J"],
        "d": 2
    },
    # 49
    {
        "q": "Which country superstar hosted SNL in 1999 and performed as musical guest under his rock-star alter ego 'Chris Gaines'?",
        "correct": "Garth Brooks",
        "distractors": ["Tim McGraw", "Kenny Chesney", "Alan Jackson"],
        "d": 2
    },
    # 50
    {
        "q": "Who hosted the first-ever 'SNL at Home' remote broadcast during the initial April 2020 COVID shutdown from his kitchen?",
        "correct": "Tom Hanks",
        "distractors": ["Steve Martin", "Alec Baldwin", "Brad Pitt"],
        "d": 1
    },
    # 51
    {
        "q": "Who served as the musical guest on the first 'SNL at Home' episode, performing an acoustic cover of Bob Dylan's 'Shelter from the Storm'?",
        "correct": "Chris Martin (of Coldplay)",
        "distractors": ["Paul Simon", "Billie Eilish", "John Legend"],
        "d": 2
    },
    # 52
    {
        "q": "Which actor portrayed Dr. Anthony Fauci in the cold open of the second 'SNL at Home' episode in April 2020?",
        "correct": "Brad Pitt",
        "distractors": ["Tom Hanks", "Alec Baldwin", "Steve Martin"],
        "d": 1
    },
    # 53
    {
        "q": "What Primetime Emmy nomination did Brad Pitt receive for his brief 3-minute performance as Dr. Anthony Fauci?",
        "correct": "Outstanding Guest Actor in a Comedy Series",
        "distractors": ["Outstanding Short-Form Variety Performance", "Outstanding Variety Special Performance", "Outstanding Lead Actor in a Comedy"],
        "d": 2
    },
    # 54
    {
        "q": "Who hosted the third and final 'SNL at Home' episode to conclude Season 45 in May 2020?",
        "correct": "Kristen Wiig",
        "distractors": ["Tina Fey", "Amy Poehler", "Maya Rudolph"],
        "d": 2
    },
    # 55
    {
        "q": "What legendary rock band made their SNL debut on October 7, 1978, with Mick Jagger licking Mick Taylor / Ronnie Wood on stage?",
        "correct": "The Rolling Stones",
        "distractors": ["The Who", "Led Zeppelin", "The Kinks"],
        "d": 2
    },
    # 56
    {
        "q": "What was unusual about the Season 4 premiere in 1978 featuring The Rolling Stones?",
        "correct": "The Rolling Stones served as both the musical guest and host",
        "distractors": ["The entire episode was performed in Central Park", "The band performed for 60 uninterrupted minutes", "No cast members appeared in the broadcast"],
        "d": 3
    },
    # 57
    {
        "q": "Which action movie icon became a Five-Timers Club member in 2017 after hosting under his wrestling moniker and acting name?",
        "correct": "Dwayne 'The Rock' Johnson",
        "distractors": ["Arnold Schwarzenegger", "John Cena", "Sylvester Stallone"],
        "d": 1
    },
    # 58
    {
        "q": "In which city was the only live road episode of SNL ever broadcast outside of New York City during Season 2 (February 1977)?",
        "correct": "New Orleans (for Mardi Gras)",
        "distractors": ["Chicago", "Los Angeles", "Las Vegas"],
        "d": 2
    },
    # 59
    {
        "q": "Why was the 1977 New Orleans Mardi Gras remote special considered a legendary logistical disaster behind the scenes?",
        "correct": "Technical delays, drunken crowds, lost audio feeds, and missing equipment",
        "distractors": ["A hurricane flooded the entire theater", "The local police arrested half the writing staff", "The broadcast was cancelled after 10 minutes"],
        "d": 3
    },
    # 60
    {
        "q": "Who was the host of the ill-fated 1977 Mardi Gras special in New Orleans?",
        "correct": "There was no traditional host; it was anchored by the cast and Randy Newman",
        "distractors": ["Steve Martin", "Buck Henry", "Paul Simon"],
        "d": 3
    },
    # 61
    {
        "q": "Which Oscar-winning actor hosted SNL six times and famously delivered monologues without shoes or neckties?",
        "correct": "Woody Harrelson",
        "distractors": ["Matthew McConaughey", "Nicolas Cage", "Sean Penn"],
        "d": 2
    },
    # 62
    {
        "q": "Which star hosted the post-9/11 season premiere on September 29, 2001, alongside Mayor Rudy Giuliani and NYC first responders?",
        "correct": "Reese Witherspoon",
        "distractors": ["Tom Hanks", "Billy Crystal", "Alec Baldwin"],
        "d": 2
    },
    # 63
    {
        "q": "What memorable question did Lorne Michaels ask Mayor Rudy Giuliani on the emotional September 29, 2001 premiere?",
        "correct": "Can we be funny?",
        "distractors": ["Are we ready?", "Can we go on?", "Is New York safe?"],
        "d": 1
    },
    # 64
    {
        "q": "What was Mayor Rudy Giuliani's iconic deadpan response to Lorne Michaels' question 'Can we be funny?'",
        "correct": "Why start now?",
        "distractors": ["Go for it!", "God bless you, yes!", "The city needs it!"],
        "d": 1
    },
    # 65
    {
        "q": "Who was the musical guest on the historic September 29, 2001 post-9/11 episode?",
        "correct": "Paul Simon (performing 'The Boxer')",
        "distractors": ["Bruce Springsteen", "Billy Joel", "Bon Jovi"],
        "d": 2
    },
    # 66
    {
        "q": "Which comedy legend made his return to host SNL in December 2019 after a 35-year absence from Studio 8H?",
        "correct": "Eddie Murphy",
        "distractors": ["Bill Murray", "Steve Martin", "Dan Aykroyd"],
        "d": 1
    },
    # 67
    {
        "q": "What Emmy Award did Eddie Murphy win in 2020 for hosting that December 2019 episode?",
        "correct": "Outstanding Guest Actor in a Comedy Series",
        "distractors": ["Outstanding Variety Special", "Outstanding Lead Actor in a Comedy", "Outstanding Writing for a Variety Series"],
        "d": 1
    },
    # 68
    {
        "q": "Which four Black comedy superstars joined Eddie Murphy on stage during his December 2019 monologue?",
        "correct": "Dave Chappelle, Chris Rock, Tracy Morgan, and Kenan Thompson",
        "distractors": ["Martin Lawrence, Jamie Foxx, Kevin Hart, and Chris Tucker", "Steve Harvey, Cedric the Entertainer, D.L. Hughley, and Bernie Mac", "Arsenio Hall, Damon Wayans, David Alan Grier, and Keenan Ivory Wayans"],
        "d": 1
    },
    # 69
    {
        "q": "Which musical artist served as the musical guest on Eddie Murphy's December 2019 return episode?",
        "correct": "Lizzo",
        "distractors": ["Beyoncé", "Megan Thee Stallion", "Rihanna"],
        "d": 2
    },
    # 70
    {
        "q": "Who hosted the first episode following the 2016 presidential election and gave an emotional 11-minute stand-up monologue on race in America?",
        "correct": "Dave Chappelle",
        "distractors": ["Chris Rock", "Trevor Noah", "John Mulaney"],
        "d": 1
    },
    # 71
    {
        "q": "What phrase did Dave Chappelle use at the conclusion of his 2016 monologue regarding Donald Trump?",
        "correct": "I'm wishing Donald Trump luck, and I'm going to give him a chance, and we the historically disenfranchised demand that he give us one too.",
        "distractors": ["Let us hope for peace and unity in our divided nation.", "God bless America, through thick and thin.", "We survived eight years before and we will survive again."],
        "d": 2
    },
    # 72
    {
        "q": "Who was the musical guest on the November 2016 post-election episode hosted by Dave Chappelle?",
        "correct": "A Tribe Called Quest",
        "distractors": ["Kendrick Lamar", "Chance the Rapper", "Kanye West"],
        "d": 2
    },
    # 73
    {
        "q": "Dave Chappelle hosted again following the November 2020 presidential election. What was the musical guest for that episode?",
        "correct": "Foo Fighters",
        "distractors": ["Coldplay", "The Strokes", "Pearl Jam"],
        "d": 2
    },
    # 74
    {
        "q": "Who hosted the episode broadcast immediately after the November 2024 presidential election?",
        "correct": "Bill Burr",
        "distractors": ["Dave Chappelle", "John Mulaney", "Nate Bargatze"],
        "d": 2
    },
    # 75
    {
        "q": "Which Canadian pop star served as musical guest on May 10, 1997, and was played on stage by Will Ferrell as her biggest stalker?",
        "correct": "Shania Twain",
        "distractors": ["Celine Dion", "Alanis Morissette", "Sarah McLachlan"],
        "d": 3
    },
    # 76
    {
        "q": "Which host holds the record for hosting the most season finales in SNL history?",
        "correct": "Buck Henry",
        "distractors": ["Alec Baldwin", "Steve Martin", "Justin Timberlake"],
        "d": 2
    },
    # 77
    {
        "q": "Which Hollywood actor has hosted SNL 13 times, placing him in third place on the all-time host list?",
        "correct": "John Goodman",
        "distractors": ["Alec Baldwin", "Tom Hanks", "Chevy Chase"],
        "d": 2
    },
    # 78
    {
        "q": "Between what years did John Goodman host an episode in every single consecutive season of SNL?",
        "correct": "1989 to 2001 (12 consecutive seasons)",
        "distractors": ["1979 to 1989", "1995 to 2005", "2000 to 2010"],
        "d": 3
    },
    # 79
    {
        "q": "Which actor hosted SNL in 1978 and became the first non-performer athlete to host the show?",
        "correct": "Fran Tarkenton",
        "distractors": ["O.J. Simpson", "Joe Namath", "Bill Russell"],
        "d": 3
    },
    # 80
    {
        "q": "Which NBA legend hosted the Season 19 premiere in September 1993 with musical guest Soul Asylum?",
        "correct": "Charles Barkley",
        "distractors": ["Michael Jordan", "Magic Johnson", "Shaquille O'Neal"],
        "d": 2
    },
    # 81
    {
        "q": "Which Olympian hosted SNL in 1989 after winning five medals at the 1988 Seoul Olympics?",
        "correct": "Florence Griffith Joyner",
        "distractors": ["Jackie Joyner-Kersee", "Carl Lewis", "Janet Evans"],
        "d": 3
    },
    # 82
    {
        "q": "Which Olympic swimmer hosted the Season 34 premiere in September 2008 following his record 8 gold medals in Beijing?",
        "correct": "Michael Phelps",
        "distractors": ["Ryan Lochte", "Ian Thorpe", "Mark Spitz"],
        "d": 2
    },
    # 83
    {
        "q": "Who was the musical guest on the Season 34 premiere hosted by Michael Phelps?",
        "correct": "Lil Wayne",
        "distractors": ["Kanye West", "Coldplay", "Rihanna"],
        "d": 3
    },
    # 84
    {
        "q": "Which legendary boxer hosted SNL in 1999 and participated in several self-deprecating sketches?",
        "correct": "Evander Holyfield",
        "distractors": ["Mike Tyson", "George Foreman", "Sugar Ray Leonard"],
        "d": 3
    },
    # 85
    {
        "q": "Which NFL quarterback hosted the show on his 31st birthday in March 2007, delivering a classic United Way digital short?",
        "correct": "Peyton Manning",
        "distractors": ["Tom Brady", "Eli Manning", "Brett Favre"],
        "d": 1
    },
    # 86
    {
        "q": "What did Peyton Manning do to young children in the iconic 2007 United Way spoof?",
        "correct": "Pelting them aggressively with footballs and teaching them how to break into locked cars",
        "distractors": ["Making them run 20-mile marathons with heavy backpacks", "Stealing their lunch money in the cafeteria", "Forcing them to study game tape until sunrise"],
        "d": 1
    },
    # 87
    {
        "q": "Which other Manning brother followed Peyton and hosted SNL in May 2012, appearing in a sketch about a murder trial search history?",
        "correct": "Eli Manning",
        "distractors": ["Cooper Manning", "Archie Manning", "Arch Manning"],
        "d": 2
    },
    # 88
    {
        "q": "Which NFL tight end hosted SNL in March 2023 with musical guest Kelsea Ballerini?",
        "correct": "Travis Kelce",
        "distractors": ["Rob Gronkowski", "George Kittle", "Jason Kelce"],
        "d": 1
    },
    # 89
    {
        "q": "Who made a surprise cameo in Travis Kelce's monologue to joke about being the family's favorite child?",
        "correct": "His brother Jason Kelce and their parents",
        "distractors": ["Patrick Mahomes", "Andy Reid", "Taylor Swift"],
        "d": 2
    },
    # 90
    {
        "q": "Which political figure hosted SNL in November 2015 while actively campaigning for the Republican presidential nomination?",
        "correct": "Donald Trump",
        "distractors": ["Ben Carson", "Jeb Bush", "Ted Cruz"],
        "d": 1
    },
    # 91
    {
        "q": "Who interrupted Donald Trump's 2015 monologue from the audience shouting 'You're a racist!' to claim a $5,000 bounty from a Hispanic advocacy group?",
        "correct": "Larry David",
        "distractors": ["Michael Moore", "Al Sharpton", "Bill Maher"],
        "d": 2
    },
    # 92
    {
        "q": "What was Larry David's excuse to Donald Trump after shouting 'You're a racist!' during the live monologue?",
        "correct": "I heard if I did that they'd give me five thousand dollars!",
        "distractors": ["I'm just exercising my first amendment rights!", "Lorne Michaels told me to do it backstage!", "I lost a bet to Jerry Seinfeld!"],
        "d": 2
    },
    # 93
    {
        "q": "Which presidential candidate appeared in a cold open in October 2015 playing a bartender named 'Val' opposite Kate McKinnon?",
        "correct": "Hillary Clinton",
        "distractors": ["Bernie Sanders", "Elizabeth Warren", "Joe Biden"],
        "d": 2
    },
    # 94
    {
        "q": "Which 2008 Republican presidential candidate appeared live in Studio 8H alongside Tina Fey's Sarah Palin just days before the election?",
        "correct": "John McCain",
        "distractors": ["Mitt Romney", "Rudy Giuliani", "Mike Huckabee"],
        "d": 2
    },
    # 95
    {
        "q": "Which Democratic presidential candidate appeared in a February 2016 sketch alongside Larry David on a sinking Titanic-like ship?",
        "correct": "Bernie Sanders",
        "distractors": ["Martin O'Malley", "Joe Biden", "Hillary Clinton"],
        "d": 2
    },
    # 96
    {
        "q": "Who was the host of the Season 30 premiere in October 2004 with musical guest Queen Latifah?",
        "correct": "Ben Affleck",
        "distractors": ["Matt Damon", "Will Ferrell", "Jude Law"],
        "d": 3
    },
    # 97
    {
        "q": "Which legendary talk-show host made his sole SNL hosting appearance in November 1989?",
        "correct": "Johnny Carson / Dick Cavett",
        "distractors": ["David Letterman", "Merv Griffin", "Phil Donahue"],
        "d": 3
    },
    # 98
    {
        "q": "Who hosted the special Thanksgiving weekend episode in November 1976 and dressed in a giant bee costume?",
        "correct": "Paul Simon",
        "distractors": ["Steve Martin", "Buck Henry", "Elliott Gould"],
        "d": 3
    },
    # 99
    {
        "q": "Which Oscar-winning actor hosted SNL during the 2000s and became famous for breaking character while playing an eccentric theater director named Don Pardee?",
        "correct": "Philip Seymour Hoffman",
        "distractors": ["Daniel Day-Lewis", "Sean Penn", "Russell Crowe"],
        "d": 3
    },
    # 100
    {
        "q": "Which singer-songwriter made a record 14 appearances as a musical guest on SNL, the most for any musical guest?",
        "correct": "Paul Simon",
        "distractors": ["Dave Grohl / Foo Fighters", "Tom Petty", "Bruce Springsteen"],
        "d": 2
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "staging", "snl_batch5.json")
    build_batch(questions, out, batch_num=5)
