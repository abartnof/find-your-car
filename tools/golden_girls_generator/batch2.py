from utils import build_golden_girls_batch

RAW_QUESTIONS = [
    # 1
    {
        "q": "In the Season 5 episode '72 Hours', why must Rose undergo an urgent medical test?",
        "correct": "She received a transfusion that may have been contaminated with HIV",
        "wrong": ["She was exposed to tuberculosis at the hospital", "She had an abnormal mammogram result", "She was bitten by a rabid stray dog"],
        "d": 1
    },
    # 2
    {
        "q": "In 'High Anxiety', what substance has Rose been secretly addicted to for thirty years?",
        "correct": "Prescription pain pills and tranquilizers",
        "wrong": ["Diet pills", "Sleeping syrups", "Alcohol"],
        "d": 1
    },
    # 3
    {
        "q": "In the classic Season 1 episode 'A Little Romance', what surprises the girls about Rose's handsome date Dr. Jonathan Newman?",
        "correct": "He is a little person",
        "wrong": ["He is half her age", "He is an escaped felon", "He cannot speak English"],
        "d": 1
    },
    # 4
    {
        "q": "In the Season 2 episode 'Isn't It Romantic?', which of the roommates does Dorothy's lesbian friend Jean fall in love with?",
        "correct": "Rose",
        "wrong": ["Blanche", "Dorothy", "Sophia"],
        "d": 1
    },
    # 5
    {
        "q": "What happens when mean neighbor Mrs. Frieda Claxton refuses to save an ancient oak tree and Rose yells at her at a city council meeting?",
        "correct": "Mrs. Claxton drops dead on the spot",
        "wrong": ["Mrs. Claxton slaps Rose across the face", "Mrs. Claxton donates the property to the church", "Mrs. Claxton sues Rose for slander"],
        "d": 1
    },
    # 6
    {
        "q": "Why do the girls attend Mrs. Claxton's funeral when none of her family or neighbors show up?",
        "correct": "To fulfill a legal requirement to secure land for a public park",
        "wrong": ["Out of Christian guilt and shame", "Because Sophia mistook it for an Italian wake", "To retrieve a borrowed gardening rake"],
        "d": 3
    },
    # 7
    {
        "q": "In the touching Season 3 episode 'Old Friends', what condition affects Sophia's new boardwalk friend Alvin?",
        "correct": "Alzheimer's disease",
        "wrong": ["Parkinson's disease", "Terminal lung cancer", "Macular degeneration"],
        "d": 1
    },
    # 8
    {
        "q": "In the Season 7 two-part murder mystery weekend episode 'The Case of the Libertine Belle', who is framed for real murder?",
        "correct": "Blanche",
        "wrong": ["Dorothy", "Rose", "Sophia"],
        "d": 1
    },
    # 9
    {
        "q": "In 'The Case of the Libertine Belle', which roommate channels her inner detective to solve the real murder and clear Blanche?",
        "correct": "Dorothy",
        "wrong": ["Rose", "Sophia", "Blanche"],
        "d": 1
    },
    # 10
    {
        "q": "What was the name of the abusive, condescending fiancé Blanche's daughter Rebecca brought home in Season 3?",
        "correct": "Jeremy",
        "wrong": ["Bradley", "Trevor", "Todd"],
        "d": 3
    },
    # 11
    {
        "q": "In Season 6's 'My Brother, My Father', what do Dorothy and Stan pretend to be to fool visiting Uncle Angelo?",
        "correct": "Still happily married",
        "wrong": ["Wealthy real estate tycoons", "Devout church deacons", "Professional ballroom dancers"],
        "d": 1
    },
    # 12
    {
        "q": "What holy persona does Sophia adopt in 'My Brother, My Father' when Uncle Angelo arrives?",
        "correct": "A Catholic nun who took a vow of poverty",
        "wrong": ["A missionary nurse from Africa", "A cloistered mother superior", "A parish choir director"],
        "d": 1
    },
    # 13
    {
        "q": "What valuable object does Sophia claim to have hidden in her wicker purse when mugged?",
        "correct": "Her emergency cannoli and family rosary",
        "wrong": ["A solid gold crucifix", "A bearer bond from 1954", "A diamond engagement ring"],
        "d": 3
    },
    # 14
    {
        "q": "In Season 2, after a home break-in, the girls purchase a mace can and a handgun. What does Rose accidentally shoot?",
        "correct": "Blanche's prized antique vase",
        "wrong": ["The living room television", "The kitchen refrigerator", "Stan's toupee on the hat rack"],
        "d": 1
    },
    # 15
    {
        "q": "What guard dog breed do the girls briefly adopt for home security after the robbery, only to find it completely docile?",
        "correct": "A Doberman Pinscher",
        "wrong": ["A German Shepherd", "A Rottweiler", "A Bullmastiff"],
        "d": 3
    },
    # 16
    {
        "q": "What name does Rose give to the supposedly terrifying guard dog they adopt?",
        "correct": "Baby",
        "wrong": ["Killer", "Fang", "Hercules"],
        "d": 3
    },
    # 17
    {
        "q": "In Season 2's 'The Actor', what is the name of the handsome community theater lead who secretly seduces all three women?",
        "correct": "Patrick Vaughn",
        "wrong": ["Julian Drake", "Harrison Stone", "Derek Richardson"],
        "d": 3
    },
    # 18
    {
        "q": "What local theater production is Patrick Vaughn starring in when the girls compete for the female lead?",
        "correct": "The Postman Always Rings Twice",
        "wrong": ["A Streetcar Named Desire", "Cat on a Hot Tin Roof", "Death of a Salesman"],
        "d": 3
    },
    # 19
    {
        "q": "In 'The Housekeeper', what spiritual practice does housekeeper Marguerite allegedly use against the roommates?",
        "correct": "Santería voodoo curses",
        "wrong": ["Wiccan witchcraft", "Astrological hexes", "Gypsy spells"],
        "d": 1
    },
    # 20
    {
        "q": "What physical symptom causes the girls to panic and believe Marguerite's curse is working?",
        "correct": "Dorothy's toothache and Blanche's unexplained spots",
        "wrong": ["Rose losing her voice completely", "Sophia getting locked in the pantry", "All the house lights flickering"],
        "d": 3
    },
    # 21
    {
        "q": "In Season 5's 'Love Under the Big Top', what profession does Dorothy's lawyer boyfriend Ken decide to pursue instead?",
        "correct": "Circus clown",
        "wrong": ["Trapeze artist", "Lion tamer", "Magician"],
        "d": 1
    },
    # 22
    {
        "q": "What legendary comedy actor played Ken, Dorothy's clown-turned lawyer boyfriend?",
        "correct": "Dick Van Dyke",
        "wrong": ["Carl Reiner", "Tim Conway", "Bob Newhart"],
        "d": 1
    },
    # 23
    {
        "q": "In Season 4's 'Brother, Can You Spare That Jacket?', what valuable item is accidentally donated inside an old jacket to a thrift store?",
        "correct": "A winning lottery ticket",
        "wrong": ["A diamond tennis bracelet", "Five thousand dollars in cash", "Blanche's deed to the house"],
        "d": 1
    },
    # 24
    {
        "q": "Where do the girls end up spending the night while searching for the donated jacket with the lottery ticket?",
        "correct": "A homeless shelter",
        "wrong": ["A Miami police precinct cell", "A bus terminal waiting room", "An all-night laundromat"],
        "d": 1
    },
    # 25
    {
        "q": "What do the girls decide to do after retrieving the winning ticket at the homeless shelter?",
        "correct": "They donate the entire prize money to the shelter",
        "wrong": ["They buy a brand-new roof for their house", "They split the cash four ways", "They take a luxury cruise to the Bahamas"],
        "d": 1
    },
    # 26
    {
        "q": "In the Season 7 episode 'Questions and Answers', what iconic TV game show does Dorothy audition for in her dream?",
        "correct": "Jeopardy!",
        "wrong": ["Wheel of Fortune", "The $25,000 Pyramid", "Tic-Tac-Dough"],
        "d": 1
    },
    # 27
    {
        "q": "Who hosts the game show in Dorothy's dream audition on 'Jeopardy!'?",
        "correct": "Alex Trebek",
        "wrong": ["Art Fleming", "Pat Sajak", "Bob Barker"],
        "d": 1
    },
    # 28
    {
        "q": "What talk show icon and Jeopardy! creator appears in Dorothy's dream to declare Rose a genius?",
        "correct": "Merv Griffin",
        "wrong": ["Dick Cavett", "Johnny Carson", "Mike Douglas"],
        "d": 1
    },
    # 29
    {
        "q": "In the Season 1 episode 'The Heart Attack', who experiences severe chest pains during an intense late-night storm?",
        "correct": "Sophia",
        "wrong": ["Dorothy", "Rose", "Blanche"],
        "d": 1
    },
    # 30
    {
        "q": "In 'The Operation' (Season 1), what procedure does Dorothy require that terrifies her due to a childhood phobia?",
        "correct": "Foot surgery",
        "wrong": ["Cataract surgery", "Tonsillectomy", "Appendectomy"],
        "d": 3
    },
    # 31
    {
        "q": "What dance do Dorothy and Rose practice to perform at an upcoming charity banquet in 'The Operation'?",
        "correct": "A tap-dance routine",
        "wrong": ["A waltz", "A tango", "A polka"],
        "d": 2
    },
    # 32
    {
        "q": "In Season 4's 'Yes, We Have No Havanas', what dashing Cuban widower do Sophia and Blanche both compete to date?",
        "correct": "Fidel Santiago",
        "wrong": ["Mateo Alvarez", "Eduardo Morales", "Alejandro Cruz"],
        "d": 3
    },
    # 33
    {
        "q": "In 'The Competition' (Season 1), what sport do Dorothy and Blanche play against each other where Blanche cheats?",
        "correct": "Bowling",
        "wrong": ["Tennis", "Golf", "Racquetball"],
        "d": 2
    },
    # 34
    {
        "q": "What bet did Dorothy and Blanche make on the outcome of their bowling match?",
        "correct": "The loser must wait on the winner hand and foot for a week",
        "wrong": ["The loser must pay a month of rent", "The loser must clean all the bathrooms", "The loser must dye her hair gray"],
        "d": 3
    },
    # 35
    {
        "q": "In 'The Flu' (Season 1), all the women come down with the flu right before attending what major event?",
        "correct": "The South Florida Medical Society awards banquet",
        "wrong": ["A governor's charity ball", "A high school reunion", "A local premiere of an opera"],
        "d": 2
    },
    # 36
    {
        "q": "In 'The Break-In' (Season 1), where were the girls when their house was burglarized?",
        "correct": "At a drive-in movie theater seeing 'Psycho'",
        "wrong": ["At a church bingo game", "At an all-you-can-eat seafood buffet", "At an art gallery reception"],
        "d": 3
    },
    # 37
    {
        "q": "In 'In a Bed of Rose's' (Season 1), what tragic event occurs when Rose spends the night with her new boyfriend Al?",
        "correct": "He dies in Rose's bed during the night",
        "wrong": ["He steals her mother's heirloom necklace", "He turns out to be Stan's cousin", "He reveals he is married to Dorothy's principal"],
        "d": 2
    },
    # 38
    {
        "q": "In 'Nice and Easy' (Season 1), who visits Blanche and quickly drives the roommates crazy with her promiscuity?",
        "correct": "Blanche's niece Lucy",
        "wrong": ["Blanche's niece Cindy", "Blanche's cousin Melanie", "Blanche's stepdaughter Brenda"],
        "d": 3
    },
    # 39
    {
        "q": "In 'Blind Ambitions' (Season 1), who visits Rose and reveals she has suddenly become blind?",
        "correct": "Rose's sister Lily",
        "wrong": ["Rose's daughter Kirsten", "Rose's aunt Sigrid", "Rose's cousin Ingrid"],
        "d": 3
    },
    # 40
    {
        "q": "In 'A Visit From Little Sven' (Season 3), who comes from St. Olaf and falls for Blanche?",
        "correct": "Rose's cousin Sven",
        "wrong": ["Rose's nephew Lars", "Rose's brother Hans", "Rose's childhood sweetheart Ole"],
        "d": 3
    },
    # 41
    {
        "q": "In 'Second Motherhood' (Season 1), what man does Blanche date who expects her to help raise his young children?",
        "correct": "Dirk",
        "wrong": ["Jerry", "Frank", "David"],
        "d": 3
    },
    # 42
    {
        "q": "In 'Family Affair' (Season 2), which two family members are caught in bed together, horrifying Dorothy and Blanche?",
        "correct": "Dorothy's son Michael and Blanche's daughter Bridget",
        "wrong": ["Stan and Blanche's sister Virginia", "Uncle Angelo and Aunt Angela", "Michael and Blanche's niece Lucy"],
        "d": 2
    },
    # 43
    {
        "q": "In 'Take Him, He's Mine' (Season 2), why does Dorothy spend time with Stan, causing tension with Blanche?",
        "correct": "Stan is depressed over Chrissy leaving him",
        "wrong": ["Stan offers to buy Dorothy a brand-new condo", "Stan needs a bone marrow donor", "Stan asks Dorothy to co-sign a loan"],
        "d": 3
    },
    # 44
    {
        "q": "In Season 2's 'It's a Miserable Life', what town relic do the girls fight Mrs. Claxton to preserve?",
        "correct": "A 200-year-old oak tree",
        "wrong": ["A historic cobblestone fountain", "The city's first post office", "A memorial statue of a civil war general"],
        "d": 2
    },
    # 45
    {
        "q": "In 'Whose Face Is This, Anyway?' (Season 6), what cosmetic procedure does Blanche consider undergoing?",
        "correct": "Plastic surgery / a face-lift",
        "wrong": ["Liposuction", "Rhinoplasty", "Hair transplant"],
        "d": 2
    },
    # 46
    {
        "q": "In 'Miles to Go' (Season 6), what is the profession of Nicholas Carbone (Miles Webber) in his past life?",
        "correct": "An accountant for the Chicago mob",
        "wrong": ["A hitman for the Gambino family", "A corrupt federal judge", "A getaway driver for bank robberies"],
        "d": 3
    },
    # 47
    {
        "q": "Where must Rose travel to visit Miles while he is temporarily relocated into witness protection?",
        "correct": "A cheese farm in Pennsylvania / Amish country",
        "wrong": ["A remote cabin in Alaska", "A desert town in New Mexico", "A motel in North Dakota"],
        "d": 3
    },
    # 48
    {
        "q": "What is the name of the younger, athletic fitness instructor Blanche dates in Season 3's 'In a Nutshell'?",
        "correct": "Dirk",
        "wrong": ["Brad", "Troy", "Brett"],
        "d": 3
    },
    # 49
    {
        "q": "How much younger is Dirk than Blanche, leading Blanche to realize she cannot keep up with him?",
        "correct": "Nearly twenty years younger",
        "wrong": ["Five years younger", "Ten years younger", "Thirty years younger"],
        "d": 2
    },
    # 50
    {
        "q": "In Season 6's 'There Goes the Bride', who does Dorothy almost remarry before walking away at the altar?",
        "correct": "Stan Zbornak",
        "wrong": ["Miles Webber", "Glen O'Brien", "Lucas Hollingsworth"],
        "d": 1
    },
    # 51
    {
        "q": "What document does Stan demand Dorothy sign right before their planned second wedding, prompting her to call it off?",
        "correct": "A prenuptial agreement",
        "wrong": ["A life insurance policy", "A deed transfer for her mother's house", "A waiver for alimony"],
        "d": 2
    },
    # 52
    {
        "q": "In 'The President's Coming! The President's Coming!' (Season 5), which U.S. President is scheduled to visit Miami and meet the girls?",
        "correct": "George H.W. Bush",
        "wrong": ["Ronald Reagan", "Bill Clinton", "Jimmy Carter"],
        "d": 2
    },
    # 53
    {
        "q": "Which future Oscar-winning director made an uncredited appearance as an Elvis impersonator in 'Sophia's Wedding'?",
        "correct": "Quentin Tarantino",
        "wrong": ["Steven Spielberg", "James Cameron", "Ron Howard"],
        "d": 1
    },
    # 54
    {
        "q": "In 'The One That Got Away' (Season 4), Blanche is eager to reunite with Ham Lushbough, but is shocked to discover what?",
        "correct": "He has gained enormous weight and let himself go",
        "wrong": ["He has become a Catholic monk", "He has gone completely deaf", "He has lost all his fortune"],
        "d": 3
    },
    # 55
    {
        "q": "In 'The Artist' (Season 3), what famous European artist invites the girls to pose for him in his studio?",
        "correct": "Laszlo",
        "wrong": ["Marcel", "Jean-Pierre", "Marco"],
        "d": 3
    },
    # 56
    {
        "q": "What do Blanche, Dorothy, and Rose discover when they arrive at Laszlo's studio to pose for him?",
        "correct": "He expects them to pose completely nude",
        "wrong": ["He only paints still-life bowls of fruit", "He wants them to scrub his kitchen floors", "He has hired a police sketch artist"],
        "d": 2
    },
    # 57
    {
        "q": "In 'The Days and Nights of Sophia Petrillo' (Season 4), what does Sophia actually do all day while the girls assume she is napping?",
        "correct": "She volunteers at a hospital, shops for groceries, and plays in an orchestra",
        "wrong": ["She goes to the dog track and places bets", "She visits her secret second apartment in Miami Beach", "She runs an illegal bingo game in the park"],
        "d": 2
    },
    # 58
    {
        "q": "In 'An Illegitimate Concern' (Season 5), what does Blanche discover about George Devereaux's past?",
        "correct": "He fathered a son out of wedlock named David",
        "wrong": ["He had an annulled marriage in high school", "He secretly worked for the CIA in Cuba", "He was disinherited by his wealthy parents"],
        "d": 3
    },
    # 59
    {
        "q": "In 'All Bets Are Off' (Season 5), what vice does Dorothy struggle with after accompanying Sophia to the race track?",
        "correct": "Compulsive gambling",
        "wrong": ["Chain-smoking cigarettes", "Binge drinking martinis", "Shoplifting designer scarves"],
        "d": 2
    },
    # 60
    {
        "q": "In 'Allies' (Season 5), Dorothy's student tries to bribe her with concert tickets for what rock band?",
        "correct": "The Rolling Stones",
        "wrong": ["Led Zeppelin", "The Who", "Aerosmith"],
        "d": 3
    },
    # 61
    {
        "q": "In 'Cheaters' (Season 5), where do Blanche and Sophia get arrested during a raid on an illicit establishment?",
        "correct": "An illegal gambling club",
        "wrong": ["A counterfeit purse warehouse", "An underground drag parlor", "An unlicensed bingo hall"],
        "d": 3
    },
    # 62
    {
        "q": "In 'Like the Beickets of the Field' (Season 5), what glamorous hobby does Blanche take up to boost her self-esteem?",
        "correct": "High-fashion modeling",
        "wrong": ["Ballroom dancing", "French gourmet cooking", "Equestrian horse jumping"],
        "d": 3
    },
    # 63
    {
        "q": "In 'Ebb Tide' (Season 5), Blanche returns to Georgia for Big Daddy's funeral and clashes with Virginia over what item?",
        "correct": "Big Daddy's estate and personal possessions",
        "wrong": ["His antique pocket watch", "His plantation burial plot", "His prize-winning hunting rifle"],
        "d": 3
    },
    # 64
    {
        "q": "In 'Snap Out of It' (Season 6), what condition does Sophia suffer from that causes Dorothy immense worry?",
        "correct": "Severe clinical depression",
        "wrong": ["Temporary amnesia", "Acute appendicitis", "Severe hearing loss"],
        "d": 3
    },
    # 65
    {
        "q": "In 'Wham, Bam, Thank You, Mammy' (Season 6), what song does Blanche sing with her former nanny Viola Watkins?",
        "correct": "I Wanna Be Loved by You",
        "wrong": ["Dixie", "Moon River", "Amazing Grace"],
        "d": 3
    },
    # 66
    {
        "q": "In 'How Do You Solve a Problem Like Sophia?' (Season 6), what institution does Sophia decide to enter after her friend passes away?",
        "correct": "A convent to become a nun",
        "wrong": ["A monastery in Vermont", "A full-time silent retreat", "A culinary institute in Rome"],
        "d": 2
    },
    # 67
    {
        "q": "In 'Mrs. George Devereaux' (Season 6), what shocking event apparently happens to Blanche's deceased husband George?",
        "correct": "He appears at her front door, having faked his death for nine years",
        "wrong": ["His body is exhumed for a murder investigation", "His secret twin brother arrives to claim his estate", "His voice is heard through a psychic channeler"],
        "d": 2
    },
    # 68
    {
        "q": "What is revealed at the end of the emotional episode 'Mrs. George Devereaux'?",
        "correct": "The entire return of George was only a vivid dream Blanche had",
        "wrong": ["George was actually an impostor named Frank", "George had lost his memory in Europe", "George was in the federal witness protection program"],
        "d": 2
    },
    # 69
    {
        "q": "In 'What a Difference a Date Makes' (Season 6), what does Dorothy wear to meet John Neretti, the man who stood her up in high school?",
        "correct": "A replica of her original prom dress",
        "wrong": ["A black leather jacket and jeans", "A glamorous sequined evening gown", "Her high school graduation robe"],
        "d": 3
    },
    # 70
    {
        "q": "What actor played Dorothy's long-lost high school prom date John Neretti?",
        "correct": "Hal Linden",
        "wrong": ["Alan Alda", "Gene Saks", "Peter Falk"],
        "d": 2
    },
    # 71
    {
        "q": "In 'Stand by Your Man' (Season 6), what physical condition does Blanche's wealthy new suitor Ted have?",
        "correct": "He uses a wheelchair",
        "wrong": ["He is completely blind", "He is hard of hearing", "He walks with two canes"],
        "d": 3
    },
    # 72
    {
        "q": "In 'Never Yell Fire in a Crowded Retirement Home' (Season 6), who is accused of deliberately starting the Shady Pines fire?",
        "correct": "Sophia",
        "wrong": ["Stan", "Dorothy", "Uncle Angelo"],
        "d": 2
    },
    # 73
    {
        "q": "What appliance was Sophia supposedly using that was blamed for sparking the Shady Pines fire?",
        "correct": "An illegal hot plate in her room",
        "wrong": ["A faulty electric toaster", "A space heater", "A curling iron left plugged in"],
        "d": 2
    },
    # 74
    {
        "q": "In 'Witness' (Season 6), what does Miles Webber buy for Rose that makes her suspicious he is hiding something?",
        "correct": "An expensive new car with cash",
        "wrong": ["A five-carat diamond ring", "A vacation home in the Keys", "A luxury mink coat"],
        "d": 3
    },
    # 75
    {
        "q": "In 'Ro$e Love$ Mile$' (Season 6), what cheapskate habit of Miles frustrates Rose when they go out on dates?",
        "correct": "He uses expired coupons and takes her to budget buffets",
        "wrong": ["He makes her split the bill down to the penny", "He sneaks food out of restaurants in napkins", "He refuses to tip the waitstaff"],
        "d": 2
    },
    # 76
    {
        "q": "In 'The Pope's Ring' (Season 6), what heirloom does Sophia acquire from a visiting relative that causes high drama?",
        "correct": "A ring blessed by the Pope",
        "wrong": ["A crucifix made from the True Cross", "A rosary carved by St. Francis", "A chalice used in the Vatican"],
        "d": 3
    },
    # 77
    {
        "q": "In 'The Commitments' (Season 7), who takes Dorothy on a date to a rock-and-roll concert?",
        "correct": "A Beatles tribute band promoter named Frank",
        "wrong": ["An aging motorcycle enthusiast", "A high school gym teacher", "A radio disk jockey"],
        "d": 3
    },
    # 78
    {
        "q": "In 'Beauty and the Beast' (Season 7), what does Blanche hire a hunky handyman to do around the house?",
        "correct": "Install a hot tub on the lanai",
        "wrong": ["Paint the entire exterior white", "Build a walk-in shoe closet", "Repair the kitchen cabinets"],
        "d": 3
    },
    # 79
    {
        "q": "In 'Room 7' (Season 7), Blanche visits her childhood home Twin Oaks and is devastated to discover what plan?",
        "correct": "The house is scheduled to be demolished to build a retail development",
        "wrong": ["It has been converted into a pig farm", "It was seized by the federal tax authorities", "It was purchased by a northern textile company"],
        "d": 3
    },
    # 80
    {
        "q": "In 'From Here to the Pharmacy' (Season 7), what returning soldier from the Gulf War catches Blanche's eye?",
        "correct": "A handsome marine named Bill",
        "wrong": ["An army captain named Steve", "A naval aviator named Brad", "An air force pilot named Tom"],
        "d": 3
    },
    # 81
    {
        "q": "In 'The Men in Our Lives' (Season 7), who is the legendary baseball player Rose claims stayed with her family in Minnesota?",
        "correct": "Ted Williams",
        "wrong": ["Babe Ruth", "Joe DiMaggio", "Mickey Mantle"],
        "d": 3
    },
    # 82
    {
        "q": "In 'Home Again, Rose' (Season 7 two-parter), what life-threatening medical emergency does Rose suffer?",
        "correct": "A massive heart attack requiring triple bypass surgery",
        "wrong": ["A ruptured brain aneurysm", "Severe kidney failure", "A ruptured appendix"],
        "d": 2
    },
    # 83
    {
        "q": "During Rose's heart surgery in 'Home Again, Rose', who initially bars Dorothy, Blanche, and Sophia from visiting Rose in ICU?",
        "correct": "Rose's estranged, hostile daughter Kirsten",
        "wrong": ["A strict head nurse who enforces blood-relative rules", "The hospital administrator", "Rose's boyfriend Miles"],
        "d": 2
    },
    # 84
    {
        "q": "What blistering speech does Dorothy give to Kirsten outside Rose's intensive care hospital room?",
        "correct": "She explains that the roommates are Rose's true daily family through thick and thin",
        "wrong": ["She demands Kirsten repay Charlie's funeral expenses", "She threatens to have Kirsten banned from Florida", "She reveals Rose wrote Kirsten out of her will"],
        "d": 2
    },
    # 85
    {
        "q": "In the series finale 'One Flew Out of the Cuckoo's Nest', who does Blanche set Dorothy up with on a blind date as a joke?",
        "correct": "Blanche's wealthy uncle Lucas Hollingsworth",
        "wrong": ["Blanche's eccentric cousin Billy", "Stan's former divorce lawyer", "A country-western singer named Bobby"],
        "d": 1
    },
    # 86
    {
        "q": "What acclaimed comic movie actor portrayed Blanche's uncle Lucas Hollingsworth in the series finale?",
        "correct": "Leslie Nielsen",
        "wrong": ["Lloyd Bridges", "Jack Lemmon", "Walter Matthau"],
        "d": 1
    },
    # 87
    {
        "q": "How do Dorothy and Lucas initially react to Blanche setting them up on a blind date?",
        "correct": "They pretend to be madly in love to play an elaborate prank on Blanche",
        "wrong": ["They get into a shouting match at the restaurant", "Dorothy dumps a drink on Lucas's head", "Lucas abandons Dorothy at a gas station"],
        "d": 2
    },
    # 88
    {
        "q": "What happens while Dorothy and Lucas are pretending to be engaged to prank Blanche?",
        "correct": "They realize they have genuinely fallen deeply in love with each other",
        "wrong": ["Stan finds out and challenges Lucas to a duel", "Lucas reveals he is penniless and living in his car", "Dorothy discovers Lucas is secretly married"],
        "d": 1
    },
    # 89
    {
        "q": "Where does Dorothy move with her new husband Lucas after their wedding in the series finale?",
        "correct": "Atlanta, Georgia",
        "wrong": ["Savannah, Georgia", "Charleston, South Carolina", "New York City"],
        "d": 1
    },
    # 90
    {
        "q": "Why does Sophia decide not to move to Atlanta with Dorothy and Lucas at the end of the series finale?",
        "correct": "She realizes Blanche and Rose still need her, and she wants Dorothy to have her own life",
        "wrong": ["She hates the climate in Atlanta", "Stan buys her a luxury condo in Miami Beach", "She decides to move back to Sicily with Angela"],
        "d": 2
    },
    # 91
    {
        "q": "In the final scene of the series finale, how many times does Dorothy come back into the house to hug her friends before finally leaving?",
        "correct": "Three times",
        "wrong": ["Once", "Five times", "Twice"],
        "d": 2
    },
    # 92
    {
        "q": "What iconic final words does Dorothy say through tears to Rose, Blanche, and Sophia in the finale's final embrace?",
        "correct": "'You'll always be my sisters. Always.'",
        "wrong": ["'Thank you for being my friends.'", "'I will love you forever and ever.'", "'Don't you dare eat cheesecake without me.'"],
        "d": 2
    },
    # 93
    {
        "q": "In Season 3's 'Three on a Couch', why do the four women see a professional psychologist together?",
        "correct": "Nonstop bickering and household friction threaten to tear them apart",
        "wrong": ["To get certified as foster parents", "To prepare for a joint appearance on a television talk show", "Because Blanche believes the house is haunted"],
        "d": 2
    },
    # 94
    {
        "q": "What therapist helps the women resolve their conflicts in 'Three on a Couch'?",
        "correct": "Dr. Ashley",
        "wrong": ["Dr. Freud", "Dr. Miller", "Dr. Stone"],
        "d": 3
    },
    # 95
    {
        "q": "In Season 4's 'The Auction', what do the girls buy at an estate auction hoping it will be worth a fortune?",
        "correct": "A painting by a famous artist",
        "wrong": ["A vintage mahogany wardrobe", "A silver tea service from the 1800s", "A rare stamp collection"],
        "d": 2
    },
    # 96
    {
        "q": "In 'The Accurate Conception' (Season 5), what does Blanche's daughter Rebecca announce she is doing to have a baby?",
        "correct": "Undergoing artificial insemination at a fertility clinic",
        "wrong": ["Adopting a child from an overseas agency", "Hiring a surrogate mother in California", "Marrying a wealthy older aristocrat"],
        "d": 2
    },
    # 97
    {
        "q": "How does Blanche initially react to Rebecca's plan to have a baby via artificial insemination?",
        "correct": "She is horrified and considers it scandalous and unnatural",
        "wrong": ["She offers to pay for the entire procedure", "She organizes a baby shower immediately", "She suggests adopting Dorothy's grandson instead"],
        "d": 2
    },
    # 98
    {
        "q": "In 'Yokel Hero' (Season 4), what exaggerated claim does Rose make in an application that wins St. Olaf's Woman of the Year?",
        "correct": "She saved the town from a devastating flood by sticking her arm in a dam",
        "wrong": ["She caught a runaway bull with her bare hands", "She personally cured a town epidemic with herbal tea", "She milked 500 cows in a single afternoon"],
        "d": 3
    },
    # 99
    {
        "q": "In 'The Audit' (Season 3), what agency investigates Dorothy and Stan's past joint finances?",
        "correct": "The Internal Revenue Service (IRS)",
        "wrong": ["The Florida Department of Revenue", "The FBI Fraud Bureau", "The Miami Municipal Court"],
        "d": 2
    },
    # 100
    {
        "q": "In 'The Audit', what bizarre deduction did Stan claim on their taxes that triggers the audit?",
        "correct": "Novelty gag gifts and an offshore pleasure yacht as business expenses",
        "wrong": ["Tuition for a clown college in France", "Hairpiece maintenance fees as medical expenses", "Church tithes paid in lottery scratchers"],
        "d": 3
    }
]

if __name__ == "__main__":
    build_golden_girls_batch(RAW_QUESTIONS, 2, "tools/staging/golden_girls_batch2.json")
