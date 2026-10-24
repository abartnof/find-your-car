from utils import build_golden_girls_batch

RAW_QUESTIONS = [
    # --- TEXTUAL QUESTIONS (1-20: Questions 201-220 of Textual) ---
    # 1
    {
        "q": "In the Season 7 episode 'Journey to the Center of Attention', what local bar do Blanche and Dorothy visit where Dorothy unexpectedly becomes the singing sensation?",
        "correct": "The Rusty Anchor",
        "wrong": ["The Pelican Cove", "The Flaming Star", "The Blue Marlin"],
        "d": 1
    },
    # 2
    {
        "q": "What torch ballad does Dorothy sing at The Rusty Anchor that brings down the house and infuriates Blanche?",
        "correct": "What'll I Do?",
        "wrong": ["Stormy Weather", "The Man That Got Away", "My Funny Valentine"],
        "d": 1
    },
    # 3
    {
        "q": "In 'The Monkey Show' (Season 7), what object does Stan cling to during his nervous breakdown and therapy sessions?",
        "correct": "A traffic cone",
        "wrong": ["A sock puppet", "A bowling pin", "A rubber chicken"],
        "d": 3
    },
    # 4
    {
        "q": "What is the name of Stan's younger, obnoxious brother who visits Miami and tries to seduce Dorothy in Season 7?",
        "correct": "Ted",
        "wrong": ["Irving", "Morty", "Lou"],
        "d": 1
    },
    # 5
    {
        "q": "In the Season 2 episode 'Dorothy's Prized Pupil', what threat does Dorothy's gifted high school student Mario Sanchez face?",
        "correct": "Deportation by the Immigration and Naturalization Service (INS)",
        "wrong": ["Expulsion for cheating on a standardized test", "Losing his college baseball scholarship", "Arrest for grand theft auto"],
        "d": 1
    },
    # 6
    {
        "q": "In 'Goodbye, Mr. Gordon' (Season 7), who is the visiting teacher Dorothy has an intellectual romance with?",
        "correct": "Her former high school English teacher Mr. Gordon",
        "wrong": ["Her college poetry professor Dr. Vance", "Her former high school principal Mr. Allen", "Her summer writing seminar instructor Mr. Miller"],
        "d": 3
    },
    # 7
    {
        "q": "Why does Dorothy break off her romance with Mr. Gordon in 'Goodbye, Mr. Gordon'?",
        "correct": "He plagiarizes her article and submits it under his own name",
        "wrong": ["He confesses he is secretly married with four children", "He insults Sophia's cooking at dinner", "He asks her for a five-thousand-dollar personal loan"],
        "d": 1
    },
    # 8
    {
        "q": "In 'The Sisters' (Season 2), what animal does Sophia's sister Angela bring with her from Sicily to the house?",
        "correct": "A live goat",
        "wrong": ["A caged rooster", "A Sicilian donkey", "A prize-winning pig"],
        "d": 1
    },
    # 9
    {
        "q": "What was the name of the man Angela and Sophia fought over in Sicily sixty years prior?",
        "correct": "Guido Spirelli",
        "wrong": ["Salvadore Petrillo", "Giancarlo Rossi", "Marco Moretti"],
        "d": 3
    },
    # 10
    {
        "q": "In 'Larceny and Old Lace' (Season 3), what eccentric criminal history does Sophia's boyfriend Rocco claim to have?",
        "correct": "He claims to have robbed a bank",
        "wrong": ["He claims to have hijacked an armored car", "He claims to have stolen a diamond from the Vatican", "He claims to have run illegal rum during Prohibition"],
        "d": 3
    },
    # 11
    {
        "q": "What legendary actor portrayed Sophia's elderly boyfriend Rocco in 'Larceny and Old Lace'?",
        "correct": "Mickey Rooney",
        "wrong": ["Red Buttons", "Art Carney", "Milton Berle"],
        "d": 1
    },
    # 12
    {
        "q": "In 'Letter to Gorbachev' (Season 3), why does Rose receive an official invitation to meet Soviet leader Mikhail Gorbachev?",
        "correct": "A little girl wrote a letter to him and signed Rose's name, or Rose wrote a heartfelt letter about world peace",
        "wrong": ["Rose was mistakenly identified as a top Cold War diplomat", "Mikhail Gorbachev was a huge fan of St. Olaf herring", "Sophia forged Rose's signature on a diplomatic petition"],
        "d": 1
    },
    # 13
    {
        "q": "In 'The Stan Who Came to Dinner' (Season 2), why does Stan move into Blanche's house and demand constant care from Dorothy?",
        "correct": "He underwent quadruple bypass heart surgery",
        "wrong": ["He broke both legs in a skiing accident", "He was evicted from his luxury apartment", "He claimed to have temporary blindness"],
        "d": 1
    },
    # 14
    {
        "q": "In 'Mixed Blessings' (Season 3), what causes Dorothy anxiety about her son Michael's upcoming wedding to Lorraine?",
        "correct": "Lorraine is an African-American woman who is considerably older than Michael",
        "wrong": ["Lorraine is a high-stakes poker player in Las Vegas", "Michael plans to drop out of music school to join a carnival", "Lorraine's family refuses to allow any Italian food at the reception"],
        "d": 1
    },
    # 15
    {
        "q": "What happens to Michael and Lorraine's wedding when both sets of parents object to their marriage?",
        "correct": "Michael and Lorraine decide to elope on their own",
        "wrong": ["They cancel the wedding permanently", "Dorothy and Lorraine's mother team up to stop the minister", "Stan bribes the minister to delay the vows"],
        "d": 3
    },
    # 16
    {
        "q": "In 'My Father, My Brother' (Season 6), what does Sophia tell Uncle Angelo happened to Dorothy's husband Stan?",
        "correct": "She claims Stan is a successful neurosurgeon",
        "wrong": ["She claims Stan passed away in a tragic yacht explosion", "She claims Stan became a missionary in South America", "She claims Stan was elected to the United States Senate"],
        "d": 3
    },
    # 17
    {
        "q": "In 'The President's Coming! The President's Coming!' (Season 5), who is assigned by the Secret Service to vet the girls and their home?",
        "correct": "Secret Service agents who interrogate the girls and sweep the house",
        "wrong": ["Local Miami police detectives", "The mayor of Miami Beach", "A White House protocol officer"],
        "d": 1
    },
    # 18
    {
        "q": "In 'The Monkey Show' Part 2, how does Dorothy discover that her sister Gloria slept with Stan?",
        "correct": "Stan confesses to Dorothy because he feels overwhelming guilt",
        "wrong": ["Sophia finds Gloria's earring in Stan's convertible", "Blanche spots them kissing at the marina", "Gloria brags about it at dinner to spite Dorothy"],
        "d": 1
    },
    # 19
    {
        "q": "In 'Mother's Day' (Season 3), where is Rose traveling when she gets stranded at an airport and comforts a lonely mother?",
        "correct": "She is flying to St. Olaf to visit Charlie's grave",
        "wrong": ["She is flying to Minneapolis for a dairy convention", "She is flying to Chicago to see her grandchildren", "She is flying to New York to visit the Empire State Building"],
        "d": 3
    },
    # 20
    {
        "q": "In the series finale, what gift do Rose, Blanche, and Sophia give Dorothy right before her wedding to Lucas?",
        "correct": "A beautiful photo album and heartfelt family blessings",
        "wrong": ["A solid gold friendship locket", "A ticket back to Miami if things don't work out", "A cookbook of all their late-night cheesecake recipes"],
        "d": 1
    },

    # --- METATEXTUAL QUESTIONS (21-100: Questions 1-80 of Metatextual) ---
    # 21
    {
        "q": "Who created the television sitcom 'The Golden Girls'?",
        "correct": "Susan Harris",
        "wrong": ["Diane English", "Marta Kauffman", "Linda Bloodworth-Thomason"],
        "d": 1
    },
    # 22
    {
        "q": "Which television network originally broadcast 'The Golden Girls' during its prime-time run from 1985 to 1992?",
        "correct": "NBC",
        "wrong": ["CBS", "ABC", "Fox"],
        "d": 1
    },
    # 23
    {
        "q": "On which night of the week did 'The Golden Girls' air on NBC, anchoring a dominant comedy block?",
        "correct": "Saturday night",
        "wrong": ["Thursday night", "Tuesday night", "Sunday night"],
        "d": 1
    },
    # 24
    {
        "q": "What was the regular prime-time time slot for 'The Golden Girls' on NBC's Saturday night lineup?",
        "correct": "9:00 PM Eastern / 8:00 PM Central",
        "wrong": ["8:00 PM Eastern / 7:00 PM Central", "9:30 PM Eastern / 8:30 PM Central", "10:00 PM Eastern / 9:00 PM Central"],
        "d": 1
    },
    # 25
    {
        "q": "What is the title of the iconic theme song for 'The Golden Girls'?",
        "correct": "Thank You for Being a Friend",
        "wrong": ["As Long as We Got Each Other", "Forever Friends", "Through the Years with You"],
        "d": 1
    },
    # 26
    {
        "q": "Who wrote and originally recorded the song 'Thank You for Being a Friend' in 1978?",
        "correct": "Andrew Gold",
        "wrong": ["Paul Williams", "Barry Manilow", "Harry Nilsson"],
        "d": 1
    },
    # 27
    {
        "q": "Which vocalist recorded the upbeat version of 'Thank You for Being a Friend' used as the opening theme for 'The Golden Girls'?",
        "correct": "Cindy Fee",
        "wrong": ["Jennifer Warnes", "Rita Coolidge", "Maureen McGovern"],
        "d": 1
    },
    # 28
    {
        "q": "In what year did 'The Golden Girls' premiere on NBC?",
        "correct": "1985",
        "wrong": ["1983", "1987", "1989"],
        "d": 1
    },
    # 29
    {
        "q": "In what year did the original series of 'The Golden Girls' conclude its final broadcast season?",
        "correct": "1992",
        "wrong": ["1990", "1994", "1995"],
        "d": 1
    },
    # 30
    {
        "q": "How many total seasons of 'The Golden Girls' were produced and broadcast?",
        "correct": "Seven",
        "wrong": ["Six", "Eight", "Nine"],
        "d": 1
    },
    # 31
    {
        "q": "How many total half-hour episodes of 'The Golden Girls' aired across its seven seasons?",
        "correct": "180 episodes",
        "wrong": ["154 episodes", "204 episodes", "222 episodes"],
        "d": 1
    },
    # 32
    {
        "q": "Which legendary television production company produced 'The Golden Girls'?",
        "correct": "Witt/Thomas/Harris Productions",
        "wrong": ["Carsey-Werner Productions", "Tandem Productions", "MTM Enterprises"],
        "d": 1
    },
    # 33
    {
        "q": "Who were the primary male executive producers alongside creator Susan Harris?",
        "correct": "Paul Junger Witt and Tony Thomas",
        "wrong": ["Norman Lear and Bud Yorkin", "Marcy Carsey and Tom Werner", "James L. Brooks and Allan Burns"],
        "d": 2
    },
    # 34
    {
        "q": "Which studio's television division co-produced and distributed 'The Golden Girls'?",
        "correct": "Touchstone Television (Walt Disney Studios)",
        "wrong": ["Paramount Television", "Warner Bros. Television", "Columbia Pictures Television"],
        "d": 2
    },
    # 35
    {
        "q": "What NBC entertainment president famously championed greenlighting 'The Golden Girls' despite skepticism about a show about older women?",
        "correct": "Brandon Tartikoff",
        "wrong": ["Fred Silverman", "Grant Tinker", "Warren Littlefield"],
        "d": 1
    },
    # 36
    {
        "q": "What historic Primetime Emmy milestone did 'The Golden Girls' achieve regarding its four lead actresses?",
        "correct": "All four lead actresses won Primetime Emmy Awards for their roles on the show",
        "wrong": ["All four actresses were nominated in the same category in a single year", "All four actresses shared a single ensemble Emmy trophy", "Each actress won back-to-back Emmys three years in a row"],
        "d": 1
    },
    # 37
    {
        "q": "Along with 'All in the Family' and later 'Schitt's Creek', 'The Golden Girls' is one of only three comedy series in Emmy history to achieve what honor?",
        "correct": "Having all principal cast members win Primetime Emmy Awards",
        "wrong": ["Sweeping all writing and directing categories every season", "Winning Best Comedy Series five consecutive years", "Averaging over 40 million viewers every season"],
        "d": 1
    },
    # 38
    {
        "q": "Which of the four Golden Girls actresses was the first to win a Primetime Emmy for her performance on the show in 1986?",
        "correct": "Betty White",
        "wrong": ["Bea Arthur", "Rue McClanahan", "Estelle Getty"],
        "d": 2
    },
    # 39
    {
        "q": "In 1987, which actress won the Primetime Emmy Award for Outstanding Lead Actress in a Comedy Series for 'The Golden Girls'?",
        "correct": "Rue McClanahan",
        "wrong": ["Betty White", "Bea Arthur", "Estelle Getty"],
        "d": 2
    },
    # 40
    {
        "q": "In 1988, which actress won the Primetime Emmy Award for Outstanding Lead Actress in a Comedy Series for 'The Golden Girls'?",
        "correct": "Bea Arthur",
        "wrong": ["Betty White", "Rue McClanahan", "Estelle Getty"],
        "d": 2
    },
    # 41
    {
        "q": "In 1988, in which Emmy category did Estelle Getty win her Primetime Emmy Award?",
        "correct": "Outstanding Supporting Actress in a Comedy Series",
        "wrong": ["Outstanding Lead Actress in a Comedy Series", "Outstanding Guest Actress in a Comedy Series", "Outstanding Supporting Actress in a Miniseries"],
        "d": 2
    },
    # 42
    {
        "q": "How many times did 'The Golden Girls' win the Primetime Emmy Award for Outstanding Comedy Series?",
        "correct": "Two times (1986 and 1987)",
        "wrong": ["One time (1986)", "Three times (1986, 1987, 1988)", "Four times (1986-1989)"],
        "d": 2
    },
    # 43
    {
        "q": "How many times did 'The Golden Girls' win the Golden Globe Award for Best Television Series – Musical or Comedy?",
        "correct": "Three consecutive times (1986, 1987, 1988)",
        "wrong": ["One time (1986)", "Two times (1986, 1987)", "Five consecutive times (1986-1990)"],
        "d": 2
    },
    # 44
    {
        "q": "Approximately how many total Primetime Emmy nominations did 'The Golden Girls' receive during its seven-year run?",
        "correct": "68 nominations",
        "wrong": ["34 nominations", "92 nominations", "115 nominations"],
        "d": 3
    },
    # 45
    {
        "q": "Who directed the pilot episode of 'The Golden Girls' and helped establish the show's comedic timing and blocking?",
        "correct": "Jay Sandrich",
        "wrong": ["Terry Hughes", "James Burrows", "John Rich"],
        "d": 2
    },
    # 46
    {
        "q": "Which British director took over directing duties after Season 1, helming over 100 episodes and winning two Emmy Awards for directing?",
        "correct": "Terry Hughes",
        "wrong": ["Peter Bonerz", "Noam Pitlik", "David Steinberg"],
        "d": 2
    },
    # 47
    {
        "q": "Which future creator of 'Desperate Housewives' worked as a writer and producer on 'The Golden Girls' in its later seasons?",
        "correct": "Marc Cherry",
        "wrong": ["David E. Kelley", "Chuck Lorre", "Ryan Murphy"],
        "d": 2
    },
    # 48
    {
        "q": "Which future creator of 'Arrested Development' got his early start as a staff writer on 'The Golden Girls'?",
        "correct": "Mitchell Hurwitz",
        "wrong": ["Greg Daniels", "Dan Harmon", "Mike Schur"],
        "d": 2
    },
    # 49
    {
        "q": "Approximately how many viewers tuned in to watch the one-hour series finale of 'The Golden Girls' on May 9, 1992?",
        "correct": "Over 38 million viewers",
        "wrong": ["18 million viewers", "24 million viewers", "55 million viewers"],
        "d": 2
    },
    # 50
    {
        "q": "Where did 'The Golden Girls' rank in the overall Nielsen television ratings for each of its first six seasons?",
        "correct": "Consistently inside the Top 10",
        "wrong": ["Consistently inside the Top 3", "Hovering between #15 and #25", "Ranked #1 every single year"],
        "d": 2
    },
    # 51
    {
        "q": "What was the highest Nielsen year-end ranking achieved by 'The Golden Girls' during its run?",
        "correct": "Number 5 (Seasons 2 and 3)",
        "wrong": ["Number 1 (Season 3)", "Number 2 (Season 4)", "Number 8 (Season 1)"],
        "d": 3
    },
    # 52
    {
        "q": "What spin-off series followed the characters of Rose, Blanche, and Sophia after Dorothy's departure?",
        "correct": "The Golden Palace",
        "wrong": ["Miami Nights", "Golden Years", "Retirement Living"],
        "d": 1
    },
    # 53
    {
        "q": "On which television network did the spin-off 'The Golden Palace' air during the 1992–1993 season?",
        "correct": "CBS",
        "wrong": ["NBC", "ABC", "Fox"],
        "d": 2
    },
    # 54
    {
        "q": "In 'The Golden Palace', what new business venture do Rose, Blanche, and Sophia invest in and operate?",
        "correct": "A boutique hotel in Miami Beach",
        "wrong": ["A bed and breakfast in Key West", "A cruise ship travel agency", "An Italian fine dining restaurant"],
        "d": 1
    },
    # 55
    {
        "q": "What future Oscar-nominated actor starred alongside Betty White, Rue McClanahan, and Estelle Getty in 'The Golden Palace' as hotel manager Roland Wilson?",
        "correct": "Don Cheadle",
        "wrong": ["Cuba Gooding Jr.", "Forest Whitaker", "Denzel Washington"],
        "d": 2
    },
    # 56
    {
        "q": "What comedy legend co-starred in 'The Golden Palace' as Mexican chef Chuy Castillos?",
        "correct": "Cheech Marin",
        "wrong": ["Paul Rodriguez", "George Lopez", "Tommy Chong"],
        "d": 2
    },
    # 57
    {
        "q": "How many seasons did the spin-off 'The Golden Palace' last before being canceled?",
        "correct": "One season (24 episodes)",
        "wrong": ["Two seasons", "Three seasons", "Half a season (13 episodes)"],
        "d": 2
    },
    # 58
    {
        "q": "Did Bea Arthur reprise her role as Dorothy Zbornak on 'The Golden Palace'?",
        "correct": "Yes, as a guest star in a two-part special episode",
        "wrong": ["No, she refused to appear on the spin-off entirely", "Yes, as a regular recurring character in the second half", "No, her character was killed off off-screen"],
        "d": 2
    },
    # 59
    {
        "q": "What successful spin-off sitcom, also created by Susan Harris, was set next door to the Golden Girls in Miami?",
        "correct": "Empty Nest",
        "wrong": ["Nurses", "Dear John", "Night Court"],
        "d": 1
    },
    # 60
    {
        "q": "Who played the lead character, widowed pediatrician Dr. Harry Weston, in the sister series 'Empty Nest'?",
        "correct": "Richard Mulligan",
        "wrong": ["Hal Linden", "Jerry Orbach", "David Ogden Stiers"],
        "d": 2
    },
    # 61
    {
        "q": "What was the name of the beloved Saint Bernard/Golden Retriever mix dog featured on 'Empty Nest'?",
        "correct": "Dreyfuss",
        "wrong": ["Barnaby", "Pepe", "Buddy"],
        "d": 2
    },
    # 62
    {
        "q": "Which spin-off series focused on the staff of Miami's Community Memorial Hospital, sharing continuity with 'The Golden Girls'?",
        "correct": "Nurses",
        "wrong": ["Scrubs", "ER Miami", "General Ward"],
        "d": 2
    },
    # 63
    {
        "q": "In November 1991, NBC aired an interconnected three-show crossover event involving 'The Golden Girls', 'Empty Nest', and 'Nurses' centered on what weather disaster?",
        "correct": "A major hurricane hitting Miami",
        "wrong": ["A record heat wave causing a citywide blackout", "A freak winter blizzard in South Florida", "A tropical tsunami threatening the coast"],
        "d": 2
    },
    # 64
    {
        "q": "What was the official promotional name given to the three-show hurricane crossover night on NBC?",
        "correct": "Hurricane Saturday",
        "wrong": ["Stormy Evening", "Miami Tempest Night", "The Great Gale of 1991"],
        "d": 3
    },
    # 65
    {
        "q": "Which production company produced both 'The Golden Girls' and its hit 1970s predecessor 'Soap'?",
        "correct": "Witt/Thomas/Harris Productions",
        "wrong": ["Norman Lear Productions", "Lorimar Television", "Stephen J. Cannell Productions"],
        "d": 2
    },
    # 66
    {
        "q": "What groundbreaking 1970s sitcom did Susan Harris create before creating 'The Golden Girls'?",
        "correct": "Soap",
        "wrong": ["Rhoda", "Phyllis", "Alice"],
        "d": 2
    },
    # 67
    {
        "q": "Which iconic sitcom starred Bea Arthur and Rue McClanahan together in the 1970s before 'The Golden Girls'?",
        "correct": "Maude",
        "wrong": ["The Mary Tyler Moore Show", "All in the Family", "One Day at a Time"],
        "d": 1
    },
    # 68
    {
        "q": "What character did Rue McClanahan play on 'Maude' opposite Bea Arthur?",
        "correct": "Vivian Harmon",
        "wrong": ["Carol Traynor", "Florida Evans", "Mrs. Naugatuck"],
        "d": 2
    },
    # 69
    {
        "q": "Which classic 1970s sitcom starred Betty White as the scheming, man-hungry Happy Homemaker Sue Ann Nivens?",
        "correct": "The Mary Tyler Moore Show",
        "wrong": ["Rhoda", "The Bob Newhart Show", "WKRP in Cincinnati"],
        "d": 1
    },
    # 70
    {
        "q": "How many total Primetime Emmy nominations did Betty White receive specifically for playing Rose Nylund?",
        "correct": "Seven nominations (nominated every single season)",
        "wrong": ["Three nominations", "Five nominations", "Nine nominations"],
        "d": 3
    },
    # 71
    {
        "q": "How many total Primetime Emmy nominations did Estelle Getty receive for playing Sophia Petrillo?",
        "correct": "Seven nominations (nominated every single season)",
        "wrong": ["Four nominations", "Five nominations", "Six nominations"],
        "d": 3
    },
    # 72
    {
        "q": "How many total Primetime Emmy nominations did Bea Arthur receive for playing Dorothy Zbornak?",
        "correct": "Four nominations",
        "wrong": ["Seven nominations", "Two nominations", "Five nominations"],
        "d": 3
    },
    # 73
    {
        "q": "How many total Primetime Emmy nominations did Rue McClanahan receive for playing Blanche Devereaux?",
        "correct": "Four nominations",
        "wrong": ["Two nominations", "Seven nominations", "Five nominations"],
        "d": 3
    },
    # 74
    {
        "q": "In which season of 'The Golden Girls' did both Bea Arthur and Estelle Getty win their respective Emmy Awards on the same night?",
        "correct": "Season 3 (1988)",
        "wrong": ["Season 1 (1986)", "Season 2 (1987)", "Season 4 (1989)"],
        "d": 2
    },
    # 75
    {
        "q": "What was unique about the four lead actresses' Emmy categories during the run of 'The Golden Girls'?",
        "correct": "Bea Arthur, Betty White, and Rue McClanahan competed in Lead Actress, while Estelle Getty competed in Supporting Actress",
        "wrong": ["All four competed in the Lead Actress category every year", "All four competed in the Supporting Actress category every year", "They rotated who entered the Lead category each season"],
        "d": 2
    },
    # 76
    {
        "q": "Who was the president of NBC Entertainment who envisioned an ensemble comedy about mature women after seeing a skit on an NBC special?",
        "correct": "Brandon Tartikoff",
        "wrong": ["Les Moonves", "Robert Iger", "Michael Eisner"],
        "d": 2
    },
    # 77
    {
        "q": "What 1984 NBC preview special featured a comedy sketch with Selma Diamond and Doris Roberts that inspired the concept for 'The Golden Girls'?",
        "correct": "Miami Nice (a parody of Miami Vice)",
        "wrong": ["Golden Seniors", "Old Wives' Tales", "Autumn Leaves"],
        "d": 3
    },
    # 78
    {
        "q": "What was the initial working title or pitch inspiration inspired by NBC's hit drama 'Miami Vice'?",
        "correct": "Miami Nice",
        "wrong": ["Miami Sunset", "Retirement Vice", "Sunny Seniors"],
        "d": 2
    },
    # 79
    {
        "q": "Why did Bea Arthur decide to leave 'The Golden Girls' in 1992, bringing the series to an end?",
        "correct": "She felt the show had reached its creative peak and wanted to leave while still on top",
        "wrong": ["She was offered a multi-million-dollar movie contract in Hollywood", "She had a severe falling out with the studio executives over syndication", "She decided to retire from acting entirely"],
        "d": 2
    },
    # 80
    {
        "q": "Which soundstage at Sunset Gower Studios in Hollywood served as the primary taping location for 'The Golden Girls'?",
        "correct": "Stage 9",
        "wrong": ["Stage 3", "Stage 18", "Stage 24"],
        "d": 3
    },
    # 81
    {
        "q": "What live taping setup was used to record 'The Golden Girls' in front of a studio audience?",
        "correct": "Multi-camera setup with four cameras",
        "wrong": ["Single-camera cinematic film setup", "Two-camera live broadcast setup", "Three-camera videotape setup"],
        "d": 2
    },
    # 82
    {
        "q": "Why did the kitchen set of 'The Golden Girls' feature only three chairs around the round kitchen table?",
        "correct": "To leave the camera-facing side completely open for clean sightlines and multi-camera blocking",
        "wrong": ["The fourth chair was broken during the pilot taping and never replaced", "Because Sophia always preferred to stand while serving food", "The kitchen set was physically too small to accommodate a fourth chair"],
        "d": 2
    },
    # 83
    {
        "q": "What cable network purchased the exclusive off-network syndication rights for 'The Golden Girls' in the late 1990s, driving a major resurgence in popularity?",
        "correct": "Lifetime Television",
        "wrong": ["USA Network", "TBS Superstation", "Nick at Nite"],
        "d": 2
    },
    # 84
    {
        "q": "In what year did 'The Golden Girls' enter national broadcast syndication in local television markets?",
        "correct": "Fall 1990",
        "wrong": ["Fall 1988", "Fall 1992", "Fall 1994"],
        "d": 3
    },
    # 85
    {
        "q": "What cable network aired marathons of 'The Golden Girls' with the popular tagline 'Television for Women'?",
        "correct": "Lifetime",
        "wrong": ["Oxygen", "WE tv", "Hallmark Channel"],
        "d": 2
    },
    # 86
    {
        "q": "Which television comedy block did NBC build on Saturday nights around 'The Golden Girls' and 'Empty Nest' in the late 1980s?",
        "correct": "The Florida Comedy Block",
        "wrong": ["Must See TV Saturday", "Golden Comedy Night", "Sunshine State Hour"],
        "d": 3
    },
    # 87
    {
        "q": "What other NBC Saturday sitcom followed 'The Golden Girls' at 9:30 PM for several seasons?",
        "correct": "Empty Nest",
        "wrong": ["227", "Amen", "Dear John"],
        "d": 2
    },
    # 88
    {
        "q": "What popular sitcom starring Marla Gibbs preceded 'The Golden Girls' at 8:30 PM on NBC's Saturday night lineup in earlier seasons?",
        "correct": "227",
        "wrong": ["Amen", "Gimme a Break!", "Diff'rent Strokes"],
        "d": 2
    },
    # 89
    {
        "q": "What popular church-centered sitcom starring Sherman Hemsley anchored Saturday nights on NBC alongside 'The Golden Girls'?",
        "correct": "Amen",
        "wrong": ["Family Matters", "Night Court", "Good Times"],
        "d": 2
    },
    # 90
    {
        "q": "Who composed the upbeat incidental and transition music used throughout 'The Golden Girls' between scenes?",
        "correct": "George Aliceson Tipton",
        "wrong": ["Mike Post", "David Shire", "Earle Hagen"],
        "d": 3
    },
    # 91
    {
        "q": "In 2014, the Writers Guild of America ranked 'The Golden Girls' at what position on its list of the 101 Best Written TV Series of All Time?",
        "correct": "Number 69",
        "wrong": ["Number 12", "Number 34", "Number 98"],
        "d": 3
    },
    # 92
    {
        "q": "What famous design firm created the iconic banana leaf palm wallpaper originally featured in the Beverly Hills Hotel and seen in Blanche's bedroom?",
        "correct": "CW Stockwell (the 'Martinique' pattern)",
        "wrong": ["Schumacher", "Laura Ashley", "Cole & Son"],
        "d": 3
    },
    # 93
    {
        "q": "In what year were the complete series DVD box sets of 'The Golden Girls' first released by Buena Vista Home Entertainment?",
        "correct": "2004 to 2007",
        "wrong": ["1998 to 2001", "2010 to 2012", "2015 to 2017"],
        "d": 3
    },
    # 94
    {
        "q": "What was the format of the series finale 'One Flew Out of the Cuckoo's Nest' when it originally aired?",
        "correct": "A special one-hour broadcast event",
        "wrong": ["A two-hour television movie", "Two separate half-hour episodes aired over two weeks", "A live broadcast from New York"],
        "d": 2
    },
    # 95
    {
        "q": "Which major streaming service secured the exclusive streaming rights for all seven seasons of 'The Golden Girls' in 2017 in the US?",
        "correct": "Hulu",
        "wrong": ["Netflix", "Amazon Prime Video", "Max"],
        "d": 2
    },
    # 96
    {
        "q": "What real-life residential house in California was used for the exterior establishing shots of Blanche's Miami home?",
        "correct": "A private residence on North Saltair Avenue in Brentwood, Los Angeles",
        "wrong": ["A mansion on Ocean Drive in South Beach, Miami", "A house on Palm Way in Coral Gables", "A home on Sunset Boulevard in Beverly Hills"],
        "d": 3
    },
    # 97
    {
        "q": "What theme park featured a replica of the exterior Golden Girls house on its residential street tour until 2003?",
        "correct": "Disney-MGM Studios (now Disney's Hollywood Studios) in Florida",
        "wrong": ["Universal Studios Florida", "Paramount's Kings Island", "Six Flags Great Adventure"],
        "d": 2
    },
    # 98
    {
        "q": "On what famous backlot attraction at Disney-MGM Studios was the Golden Girls house facade located?",
        "correct": "Residential Street on the Studio Backlot Tour",
        "wrong": ["New York Street", "Sunset Plaza", "Boulevard of the Stars"],
        "d": 3
    },
    # 99
    {
        "q": "In what year was the Golden Girls house facade on Residential Street at Disney's Hollywood Studios torn down?",
        "correct": "2003",
        "wrong": ["1995", "1999", "2012"],
        "d": 3
    },
    # 100
    {
        "q": "Which television rating classification was commonly assigned to 'The Golden Girls' during its broadcast runs for adult humor and sexual innuendo?",
        "correct": "TV-PG",
        "wrong": ["TV-G", "TV-14", "TV-MA"],
        "d": 2
    }
]

if __name__ == "__main__":
    build_golden_girls_batch(RAW_QUESTIONS, 3, "tools/staging/golden_girls_batch3.json")
