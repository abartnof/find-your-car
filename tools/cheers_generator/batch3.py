import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from utils import assemble_batch, save_json

raw_questions = [
    # --- TEXTUAL DEEP CUTS & CLASSIC EPISODES (1-20) ---
    {
        "q": "In the classic Season 5 episode 'Thanksgiving Orphans', what legendary event breaks out among the entire gang?",
        "correct": "A chaotic, full-scale food fight across the dining room table",
        "wrong": ["A heated political debate about the mayoral election", "A poker tournament for all of Norm's savings", "A musical sing-along of Broadway showtunes"],
        "d": 1
    },
    {
        "q": "In 'Thanksgiving Orphans', why is the turkey delayed for hours, leaving everyone starving?",
        "correct": "It is completely frozen solid and takes hours to roast in Carla's oven",
        "wrong": ["Cliff forgot to turn on the gas stove", "Woody accidentally dropped it on the floor", "The power went out on Carla's block in Boston"],
        "d": 2
    },
    {
        "q": "Who throws the very first piece of food that initiates the legendary food fight in 'Thanksgiving Orphans'?",
        "correct": "Carla Tortelli (throwing mashed potatoes or stuffing at Norm)",
        "wrong": ["Woody Boyd throwing cranberry sauce", "Sam Malone throwing a bread roll", "Diane Chambers throwing gravy"],
        "d": 2
    },
    {
        "q": "In Season 1, who is Sam Malone's suave, handsome brother who charms Diane and excels at everything?",
        "correct": "Derek Malone",
        "wrong": ["Danny Malone", "Donald Malone", "David Malone"],
        "d": 1
    },
    {
        "q": "What impressive talents does Sam's brother Derek possess that make Sam intensely jealous?",
        "correct": "He flies airplanes, speaks multiple languages, and plays classical cello",
        "wrong": ["He won three World Series rings with the Yankees", "He is a renowned thoracic surgeon and novelist", "He is a champion polo player and state senator"],
        "d": 2
    },
    {
        "q": "In the Season 6 premiere 'Home Is the Sailor', what does Sam discover upon returning to Cheers after sailing?",
        "correct": "The bar was sold to a corporation and is run by Rebecca Howe",
        "wrong": ["The bar was closed down by the Boston board of health", "Norm had legally taken over the lease of the building", "Melville's had expanded downstairs and replaced the bar"],
        "d": 1
    },
    {
        "q": "What position does Sam Malone have to accept when returning to Cheers under Rebecca's management?",
        "correct": "A regular bartender working for hourly wages",
        "wrong": ["Assistant floor manager", "Barback and dishwasher", "Night custodian"],
        "d": 1
    },
    {
        "q": "What is the name of the elderly, curmudgeonly bar regular who frequently delivers blunt one-word punchlines?",
        "correct": "Al",
        "wrong": ["Gus", "Walter", "Frank"],
        "d": 2
    },
    {
        "q": "What name does the elderly patron Al famously shout out whenever music or pop culture is mentioned?",
        "correct": "\"Sinatra!\"",
        "wrong": ["\"Elvis!\"", "\"Bing!\"", "\"Beatles!\""],
        "d": 2
    },
    {
        "q": "What is the name of the recurring, round-faced bar regular played by Paul Willson?",
        "correct": "Paul Krapence",
        "wrong": ["Phil Henderson", "Pete Jenkins", "Perry Stone"],
        "d": 2
    },
    {
        "q": "What is the name of the quiet background bar regular portrayed by Rhea Perlman's real-life father?",
        "correct": "Phil",
        "wrong": ["Vito", "Rocco", "Gino"],
        "d": 2
    },
    {
        "q": "In Season 10, where do Carla and Eddie LeBec hold their winter wedding ceremony?",
        "correct": "At a local ice-skating rink",
        "wrong": ["On the field at Fenway Park", "In the backroom of Gary's Olde Towne Tavern", "On a Boston Harbor cruise ferry"],
        "d": 3
    },
    {
        "q": "In the Season 9 episode 'Days of Wine and Neuroses', where does Robin propose to Rebecca after hiding an engagement ring?",
        "correct": "Inside a glass of champagne",
        "wrong": ["Inside a lobster shell at Melville's", "Inside a hollowed-out corporate annual report", "Under a napkin on the corner of the bar"],
        "d": 3
    },
    {
        "q": "In Season 8, what wager does Sam make regarding his Corvette that he ends up losing to a sleazy sports bettor?",
        "correct": "He bets his Corvette on a Boston sporting event / bet with a rival",
        "wrong": ["He wagers his car in a high-stakes craps game in Atlantic City", "He bets his car that Woody cannot finish a marathon", "He wagers his car in a pool trick-shot challenge"],
        "d": 3
    },
    {
        "q": "In the Season 3 episode 'King of the Hill', what athletic contest does Sam enter against Coach?",
        "correct": "A table tennis (ping pong) match",
        "wrong": ["An arm-wrestling contest", "A 100-meter dash in the alley", "A free-throw shooting match"],
        "d": 3
    },
    {
        "q": "In Season 11, what does Woody Boyd discover about his wife Kelly's religious background?",
        "correct": "She was raised Lutheran while he was raised in a strict, quirky rural church",
        "wrong": ["She is an ordained minister in a new-age movement", "Her family secretly converted to Quakerism", "She was raised Greek Orthodox"],
        "d": 3
    },
    {
        "q": "In the series finale 'One for the Road', what does Sam consider doing with Diane before realizing they don't belong together?",
        "correct": "Moving to California to marry her and start a new life",
        "wrong": ["Opening a luxury wine tavern together in Napa Valley", "Adopting a French orphan child together", "Writing an autobiography about their relationship"],
        "d": 1
    },
    {
        "q": "In 'One for the Road', what municipal government job does Norm finally secure with Woody's help?",
        "correct": "A city planning clerk / municipal desk job",
        "wrong": ["Chief postal route inspector", "Assistant commissioner of Boston parks", "Harbor master deputy"],
        "d": 3
    },
    {
        "q": "What happens to the bar's beloved wooden Indian statue in the episode 'The Barstool Home'?",
        "correct": "Norm accidentally damages it or it is held for ransom",
        "wrong": ["It is stolen by college fraternity pranksters from Harvard", "It is struck by lightning during a nor'easter", "Carla chops it into firewood during a blizzard"],
        "d": 3
    },
    {
        "q": "In Season 1, what does Sam Malone keep locked in his desk drawer that he occasionally stares at to maintain his sobriety?",
        "correct": "A bottle of vodka / liquor that he never opens",
        "wrong": ["His Red Sox championship ring", "A silver AA sobriety medallion", "A framed photo of his high school coach"],
        "d": 2
    },

    # --- METATEXTUAL: EMMY AWARDS & CRITICAL RECOGNITION (21-50) ---
    {
        "q": "How many Primetime Emmy Awards did Cheers win during its 11-season run?",
        "correct": "28",
        "wrong": ["18", "37", "42"],
        "d": 1
    },
    {
        "q": "How many total Primetime Emmy Award nominations did Cheers receive throughout its run?",
        "correct": "117",
        "wrong": ["75", "92", "144"],
        "d": 2
    },
    {
        "q": "How many times did Cheers win the Primetime Emmy Award for Outstanding Comedy Series?",
        "correct": "4 times",
        "wrong": ["2 times", "6 times", "8 times"],
        "d": 1
    },
    {
        "q": "In which four television seasons did Cheers win Outstanding Comedy Series at the Emmys?",
        "correct": "1983, 1984, 1989, and 1991",
        "wrong": ["1982, 1985, 1987, and 1990", "1983, 1986, 1988, and 1992", "1984, 1985, 1990, and 1993"],
        "d": 3
    },
    {
        "q": "Which comedy series eventually broke Cheers' all-time record for most Primetime Emmy Awards won?",
        "correct": "Frasier",
        "wrong": ["Friends", "Seinfeld", "Modern Family"],
        "d": 1
    },
    {
        "q": "How many Primetime Emmy Awards did Rhea Perlman win for portraying Carla Tortelli?",
        "correct": "4",
        "wrong": ["2", "3", "5"],
        "d": 1
    },
    {
        "q": "Out of 11 seasons of Cheers, how many times was Rhea Perlman nominated for an Emmy for Carla?",
        "correct": "10 times",
        "wrong": ["6 times", "8 times", "11 times"],
        "d": 2
    },
    {
        "q": "How many Primetime Emmy Awards did Ted Danson win for his portrayal of Sam Malone?",
        "correct": "2",
        "wrong": ["1", "4", "5"],
        "d": 1
    },
    {
        "q": "How many consecutive seasons was Ted Danson nominated for Outstanding Lead Actor in a Comedy Series?",
        "correct": "All 11 seasons",
        "wrong": ["8 seasons", "9 seasons", "10 seasons"],
        "d": 2
    },
    {
        "q": "Which year did Ted Danson finally win his first Emmy Award for Cheers after eight straight nominations?",
        "correct": "1990",
        "wrong": ["1986", "1988", "1992"],
        "d": 2
    },
    {
        "q": "Which actress won the Primetime Emmy for Outstanding Lead Actress in a Comedy Series for Season 1?",
        "correct": "Shelley Long",
        "wrong": ["Rhea Perlman", "Kirstie Alley", "Bebe Neuwirth"],
        "d": 1
    },
    {
        "q": "In which year did Kirstie Alley win both an Emmy Award and a Golden Globe for playing Rebecca Howe?",
        "correct": "1991",
        "wrong": ["1988", "1989", "1993"],
        "d": 2
    },
    {
        "q": "In what year did Woody Harrelson win the Primetime Emmy Award for Outstanding Supporting Actor?",
        "correct": "1989",
        "wrong": ["1986", "1987", "1992"],
        "d": 2
    },
    {
        "q": "How many Primetime Emmy Awards did Bebe Neuwirth win for her supporting role as Lilith Sternin?",
        "correct": "2",
        "wrong": ["1", "3", "4"],
        "d": 2
    },
    {
        "q": "Which British comedy legend won an Emmy for Outstanding Guest Performer on Cheers in 1987?",
        "correct": "John Cleese",
        "wrong": ["Michael Palin", "Eric Idle", "Rowan Atkinson"],
        "d": 1
    },
    {
        "q": "What character did John Cleese play in his Emmy-winning Season 5 guest appearance on Cheers?",
        "correct": "Dr. Simon Finch-Royce",
        "wrong": ["Sir Reginald Drake", "Professor Alistair Higgins", "Dr. Arthur Campbell"],
        "d": 2
    },
    {
        "q": "How many Primetime Emmy nominations did George Wendt receive for playing Norm Peterson?",
        "correct": "6",
        "wrong": ["3", "8", "10"],
        "d": 3
    },
    {
        "q": "How many Primetime Emmy nominations did John Ratzenberger receive for playing Cliff Clavin?",
        "correct": "2",
        "wrong": ["0", "4", "5"],
        "d": 3
    },
    {
        "q": "How many Primetime Emmy Awards for Outstanding Directing for a Comedy Series did James Burrows win for Cheers?",
        "correct": "2",
        "wrong": ["1", "4", "5"],
        "d": 3
    },
    {
        "q": "For which pilot episode did James Burrows win his first directing Emmy for Cheers in 1983?",
        "correct": "\"Give Me a Ring Sometime\"",
        "wrong": ["\"Showdown: Part 2\"", "\"Thanksgiving Orphans\"", "\"I Do, Adieu\""],
        "d": 2
    },
    {
        "q": "In what year was Cheers inducted into the Television Hall of Fame?",
        "correct": "It was recognized as one of TV Guide's 50 Greatest TV Shows of All Time in 2002",
        "wrong": ["1988", "1995", "1999"],
        "d": 3
    },
    {
        "q": "In 1997, which Cheers episode was ranked #7 on TV Guide's 100 Greatest Episodes of All Time?",
        "correct": "\"Thanksgiving Orphans\"",
        "wrong": ["\"Showdown: Part 2\"", "\"One for the Road\"", "\"I Do, Adieu\""],
        "d": 2
    },
    {
        "q": "Which prestigious broadcast journalism honor did Cheers win in 1983 for distinguished achievement?",
        "correct": "The Peabody Award",
        "wrong": ["The Pulitzer Prize", "The DuPont-Columbia Award", "The Edward R. Murrow Award"],
        "d": 2
    },
    {
        "q": "Why did the Peabody Board award Cheers in 1983?",
        "correct": "For bringing wit, rich character development, and literate humor to commercial television",
        "wrong": ["For pioneering multi-camera digital audio recording techniques", "For addressing working-class economic struggles in urban Boston", "For raising public awareness about substance abuse recovery"],
        "d": 3
    },
    {
        "q": "How many Golden Globe Awards did Cheers win across its entire series run?",
        "correct": "6",
        "wrong": ["2", "11", "15"],
        "d": 2
    },
    {
        "q": "How many times was Cheers nominated for Outstanding Comedy Series at the Emmys during its 11 seasons?",
        "correct": "Every single season (11 times)",
        "wrong": ["7 times", "9 times", "10 times"],
        "d": 2
    },
    {
        "q": "Which show won the Emmy for Outstanding Comedy Series in 1985, preventing Cheers from a three-peat?",
        "correct": "The Cosby Show",
        "wrong": ["Family Ties", "Night Court", "The Golden Girls"],
        "d": 2
    },
    {
        "q": "Which show won the Emmy for Outstanding Comedy Series in 1986, beating Cheers?",
        "correct": "The Golden Girls",
        "wrong": ["The Cosby Show", "Moonlighting", "Night Court"],
        "d": 2
    },
    {
        "q": "Which show won the Emmy for Outstanding Comedy Series in 1990, defeating Cheers?",
        "correct": "Murphy Brown",
        "wrong": ["The Golden Girls", "The Wonder Years", "Designing Women"],
        "d": 3
    },
    {
        "q": "Which show won Outstanding Comedy Series in 1993 for Cheers' final eligible season?",
        "correct": "Seinfeld",
        "wrong": ["Frasier", "Home Improvement", "The Larry Sanders Show"],
        "d": 2
    },

    # --- METATEXTUAL: RATINGS, MUST SEE TV & BROADCAST MILESTONES (51-80) ---
    {
        "q": "On what date did the pilot episode of Cheers premiere on NBC?",
        "correct": "September 30, 1982",
        "wrong": ["October 15, 1981", "September 18, 1983", "November 4, 1982"],
        "d": 2
    },
    {
        "q": "Where did Cheers rank in the Nielsen television ratings during its first season (1982-1983)?",
        "correct": "74th out of 77 network shows (near the absolute bottom)",
        "wrong": ["25th out of 77 network shows", "45th out of 77 network shows", "60th out of 77 network shows"],
        "d": 1
    },
    {
        "q": "Which legendary NBC entertainment president championed Cheers and saved it from early cancellation?",
        "correct": "Brandon Tartikoff",
        "wrong": ["Grant Tinker", "Fred Silverman", "Warren Littlefield"],
        "d": 1
    },
    {
        "q": "Why did Brandon Tartikoff refuse to cancel Cheers despite catastrophic Season 1 ratings?",
        "correct": "He believed passionately in the show's exceptional writing quality and critical praise",
        "wrong": ["Paramount Television threatened to pull all studio programming from NBC", "The show was extraordinarily cheap to produce because of a single set", "Ted Danson had a personal five-year non-cancellable contract"],
        "d": 2
    },
    {
        "q": "What helped Cheers' viewership surge dramatically between Seasons 1 and 2?",
        "correct": "Reruns aired in the summer of 1983 along with sweeping Emmy Award wins",
        "wrong": ["A massive billboard ad campaign launched in New York and Boston", "A primetime television movie crossover with Taxi", "A change in the theme song vocalist and tempo"],
        "d": 2
    },
    {
        "q": "What famous NBC promotional marketing brand did Cheers help anchor on Thursday nights?",
        "correct": "\"Must See TV\"",
        "wrong": ["\"Comedy Power Hour\"", "\"NBC Thursday Night Live\"", "\"Prime Time Showtime\""],
        "d": 1
    },
    {
        "q": "What time slot did Cheers occupy for most of its historic Thursday night run on NBC?",
        "correct": "9:00 PM Eastern / 8:00 PM Central",
        "wrong": ["8:00 PM Eastern / 7:00 PM Central", "8:30 PM Eastern / 7:30 PM Central", "9:30 PM Eastern / 8:30 PM Central"],
        "d": 1
    },
    {
        "q": "Which blockbuster sitcom aired directly before Cheers at 8:30 PM in the mid-to-late 1980s?",
        "correct": "Family Ties (and later A Different World)",
        "wrong": ["Night Court", "Seinfeld", "The Golden Girls"],
        "d": 1
    },
    {
        "q": "Which courtroom comedy sitcom aired immediately following Cheers at 9:30 PM on Thursdays?",
        "correct": "Night Court",
        "wrong": ["Wings", "Empty Nest", "Dear John"],
        "d": 1
    },
    {
        "q": "In which season did Cheers finally achieve the #1 ranking in all of US television ratings?",
        "correct": "Season 9 (1990-1991)",
        "wrong": ["Season 5 (1986-1987)", "Season 7 (1988-1989)", "Season 11 (1992-1993)"],
        "d": 1
    },
    {
        "q": "On what date did the series finale of Cheers, 'One for the Road', air on NBC?",
        "correct": "May 20, 1993",
        "wrong": ["April 28, 1992", "June 15, 1993", "May 24, 1994"],
        "d": 2
    },
    {
        "q": "Approximately how many viewers in the United States watched the series finale of Cheers live?",
        "correct": "Over 80 million viewers (approx. 80.4 to 84 million)",
        "wrong": ["Over 45 million viewers", "Over 60 million viewers", "Over 105 million viewers"],
        "d": 1
    },
    {
        "q": "What Nielsen household rating did the series finale 'One for the Road' achieve?",
        "correct": "45.5 rating",
        "wrong": ["32.1 rating", "52.8 rating", "28.4 rating"],
        "d": 3
    },
    {
        "q": "What audience share did the series finale of Cheers capture during its primetime broadcast?",
        "correct": "64 share (64% of all TVs in use)",
        "wrong": ["48 share", "55 share", "78 share"],
        "d": 3
    },
    {
        "q": "At the time of its 1993 broadcast, where did the Cheers finale rank among the most-watched TV episodes in history?",
        "correct": "Second most-watched finale in television history, behind only M*A*S*H",
        "wrong": ["Most-watched finale of all time", "Third most-watched, behind M*A*S*H and The Fugitive", "Fifth most-watched episode in history"],
        "d": 1
    },
    {
        "q": "How many total broadcast episodes of Cheers were produced across its 11 seasons?",
        "correct": "275",
        "wrong": ["250", "292", "300"],
        "d": 2
    },
    {
        "q": "How long was the super-sized series finale episode 'One for the Road' in its original broadcast window?",
        "correct": "98 minutes (commercial-inclusive triple episode / three-part finale)",
        "wrong": ["60 minutes", "75 minutes", "120 minutes"],
        "d": 2
    },
    {
        "q": "Which live talk show broadcast special originated from the Bull & Finch Pub in Boston right after the finale?",
        "correct": "The Tonight Show with Jay Leno",
        "wrong": ["Late Night with David Letterman", "The Arsenio Hall Show", "Good Morning America"],
        "d": 1
    },
    {
        "q": "What notoriously chaotic condition were the Cheers cast members in during the live Jay Leno post-finale broadcast?",
        "correct": "Visibly intoxicated and unruly after celebrating hours of drinking at the Boston pub",
        "wrong": ["Refusing to appear on stage due to a contract payment dispute", "Trapped in an elevator beneath Beacon Hill", "Devastated and weeping uncontrollably in silence"],
        "d": 2
    },
    {
        "q": "What was the estimated cost for a 30-second commercial during the Cheers series finale in 1993?",
        "correct": "650,000 to 700,000 dollars",
        "wrong": ["250,000 dollars", "1.2 million dollars", "400,000 dollars"],
        "d": 3
    },
    {
        "q": "During its peak seasons (Seasons 5 through 9), where did Cheers consistently rank in annual Nielsen ratings?",
        "correct": "In the Top 5 of all network television programs",
        "wrong": ["Between 10th and 15th place", "Exclusively at #1 every single year", "Between 15th and 25th place"],
        "d": 2
    },
    {
        "q": "In Season 1, what other critically acclaimed but low-rated show debuted on NBC alongside Cheers?",
        "correct": "St. Elsewhere",
        "wrong": ["Miami Vice", "Hill Street Blues", "The Golden Girls"],
        "d": 3
    },
    {
        "q": "How many households in the United States tuned in to watch the final episode of Cheers?",
        "correct": "Approximately 42.4 million homes",
        "wrong": ["25.1 million homes", "58.3 million homes", "18.2 million homes"],
        "d": 3
    },
    {
        "q": "What special television special preceded the Cheers finale broadcast on May 20, 1993?",
        "correct": "A retrospective special hosted by Bob Costas titled 'Last Call: A Cheers Retrospective'",
        "wrong": ["A documentary about the real Boston bars hosted by Tip O'Neill", "A musical salute to Cheers by the Boston Pops Orchestra", "A blooper reel special narrated by Woody Harrelson"],
        "d": 3
    },
    {
        "q": "Which network executive took over from Brandon Tartikoff and oversaw Cheers' final seasons?",
        "correct": "Warren Littlefield",
        "wrong": ["Les Moonves", "Robert Iger", "Jeff Zucker"],
        "d": 3
    },
    {
        "q": "What rating did the final season of Cheers (Season 11) achieve in the overall seasonal Nielsen rankings?",
        "correct": "8th place overall",
        "wrong": ["1st place overall", "14th place overall", "20th place overall"],
        "d": 3
    },
    {
        "q": "What was the average weekly viewership for Cheers during its peak #1 season in 1990-1991?",
        "correct": "Over 21 million households (approx. 33 million viewers weekly)",
        "wrong": ["12 million households", "45 million households", "16 million households"],
        "d": 3
    },
    {
        "q": "Why was Season 11 announced as the final season of Cheers despite astronomical ratings?",
        "correct": "Ted Danson decided to leave the show, and creators felt Cheers could not continue without Sam",
        "wrong": ["NBC canceled the series to cut escalating production costs", "Paramount lost the rights to the bar set design in arbitration", "The writing staff collectively resigned to develop cable television"],
        "d": 1
    },
    {
        "q": "How much money was NBC reportedly willing to pay Ted Danson per episode to return for a Season 12?",
        "correct": "Over 10 million dollars for the season / nearly 500,000 dollars per episode",
        "wrong": ["2 million dollars for the season", "25 million dollars for the season", "100,000 dollars per episode"],
        "d": 3
    },
    {
        "q": "What was the final episode count of Shelley Long's tenure before her Season 5 departure?",
        "correct": "121 episodes",
        "wrong": ["98 episodes", "145 episodes", "110 episodes"],
        "d": 3
    },

    # --- METATEXTUAL: THEME SONG, CREATORS & PRODUCTION (81-100) ---
    {
        "q": "What is the official title of the iconic Cheers theme song?",
        "correct": "\"Where Everybody Knows Your Name\"",
        "wrong": ["\"A Place to Call Home\"", "\"Here at Cheers\"", "\"Down at the Bar\""],
        "d": 1
    },
    {
        "q": "Who wrote and composed the Cheers theme song 'Where Everybody Knows Your Name'?",
        "correct": "Gary Portnoy and Judy Hart Angelo",
        "wrong": ["Mike Post and Pete Carpenter", "Alan Thicke and Gloria Loring", "Charles Fox and Norman Gimbel"],
        "d": 1
    },
    {
        "q": "Who sang the vocal track on the iconic Cheers theme song?",
        "correct": "Gary Portnoy",
        "wrong": ["Michael McDonald", "Kenny Loggins", "Randy Newman"],
        "d": 1
    },
    {
        "q": "What opening line begins the televised cut of the Cheers theme song?",
        "correct": "\"Making your way in the world today takes everything you've got...\"",
        "wrong": ["\"When the work day is finally done and you want to sit right down...\"", "\"Sometimes you want to go where everybody knows your name...\"", "\"Roll out of bed and head for the door, heading into the rain...\""],
        "d": 1
    },
    {
        "q": "What darker opening lyrics from the full version of the theme song were omitted from the TV version?",
        "correct": "\"All those nights when you've got no lights, the check is in the mail / And your little cat turned blue...\"",
        "wrong": ["\"When you're down on your luck and your wallet is dry / And your lover said goodbye...\"", "\"Your boss is a creep and your landlord is mad / And you're having the worst day you've had...\"", "\"The subway was late and the coffee was cold / And you're feeling so tired and old...\""],
        "d": 3
    },
    {
        "q": "Who were the three co-creators of Cheers?",
        "correct": "James Burrows, Glen Charles, and Les Charles",
        "wrong": ["Norman Lear, Bud Yorkin, and James Burrows", "Garry Marshall, Lowell Ganz, and Babaloo Mandel", "Larry David, Jerry Seinfeld, and James Burrows"],
        "d": 1
    },
    {
        "q": "What production company was formed by the creators to produce Cheers?",
        "correct": "Charles-Burrows-Charles Productions",
        "wrong": ["Boston Pub Television", "Paramount Creative Partners", "Beacon Hill Entertainment"],
        "d": 2
    },
    {
        "q": "Which critically acclaimed sitcom did James Burrows, Glen Charles, and Les Charles all write/direct for prior to Cheers?",
        "correct": "Taxi",
        "wrong": ["M*A*S*H", "All in the Family", "Happy Days"],
        "d": 2
    },
    {
        "q": "What legendary comedy writer was the father of director James Burrows?",
        "correct": "Abe Burrows (Pulitzer Prize-winning playwright and director)",
        "wrong": ["Sammy Burrows", "Edgar Burrows", "Irving Burrows"],
        "d": 3
    },
    {
        "q": "What major studio produced Cheers in association with Charles-Burrows-Charles Productions?",
        "correct": "Paramount Television",
        "wrong": ["Warner Bros. Television", "Universal Television", "20th Century Fox Television"],
        "d": 2
    },
    {
        "q": "What visual imagery is featured throughout the opening credits sequence of Cheers behind the actor titles?",
        "correct": "Archival vintage black-and-white and sepia photographs of historical American taverns and patrons",
        "wrong": ["Live action video of the Boston Common and Charles River", "Color watercolor illustrations of Beacon Hill pubs", "Behind-the-scenes photographs of the cast on set"],
        "d": 1
    },
    {
        "q": "Where did the producers source the vintage bar photographs featured in the opening title sequence?",
        "correct": "Historical archives, library collections, and vintage photography books",
        "wrong": ["The Boston Globe newspaper morgue exclusively", "Personal family albums of the Charles brothers", "The Smithsonian Institution bar and brewing collection"],
        "d": 2
    },
    {
        "q": "What font was famously used for the main title logo of 'Cheers' in yellow serif lettering?",
        "correct": "Wordian / custom modified Windsor EF Elongated",
        "wrong": ["Cooper Black", "Helvetica Neue Bold", "Times New Roman Bold"],
        "d": 3
    },
    {
        "q": "What phrase was spoken by an announcer at the start of every Cheers episode broadcast?",
        "correct": "\"Cheers was filmed before a live studio audience.\"",
        "wrong": ["\"Cheers was recorded on location in Boston, Massachusetts.\"", "\"Recorded live in front of a studio audience in Hollywood.\"", "\"Cheers is brought to you live from Paramount Studios.\""],
        "d": 1
    },
    {
        "q": "What sound stage at Paramount Studios in Hollywood served as the permanent home of Cheers?",
        "correct": "Stage 25",
        "wrong": ["Stage 12", "Stage 9", "Stage 18"],
        "d": 3
    },
    {
        "q": "Which other legendary sitcom later filmed on the same Paramount Stage 25 after Cheers ended?",
        "correct": "Frasier",
        "wrong": ["Friends", "Seinfeld", "The Golden Girls"],
        "d": 2
    },
    {
        "q": "What camera technique and format was used to shoot Cheers?",
        "correct": "A traditional multi-camera setup shot on 35mm film",
        "wrong": ["Single camera 16mm film", "Standard broadcast videotape (NTSC)", "Early digital video cameras"],
        "d": 2
    },
    {
        "q": "Why did the creators specifically choose to film Cheers on 35mm film instead of videotape?",
        "correct": "Film provided a warmer, richer, timeless cinematic aesthetic suited to an old tavern",
        "wrong": ["Videotape was legally prohibited by the Screen Actors Guild in 1982", "Paramount Studios had run out of videotape recording facilities", "It was required for European syndication broadcast standards"],
        "d": 2
    },
    {
        "q": "What was the original concept the Charles brothers and James Burrows considered before choosing a Boston bar?",
        "correct": "A hotel in California or a desert tavern in the American West",
        "wrong": ["A radio station in Seattle", "A diner in Queens, New York", "An auto repair shop in Chicago"],
        "d": 3
    },
    {
        "q": "Why did the creators ultimately settle on Boston as the setting for Cheers?",
        "correct": "Boston was a great sports city with a distinct history, intellectual universities, and a pub culture",
        "wrong": ["James Burrows was born and raised in South Boston", "The state of Massachusetts offered massive tax incentives for TV productions", "Paramount already owned an authentic Boston bar set from a failed movie"],
        "d": 2
    }
]

assert len(raw_questions) == 100, f"Expected 100, got {len(raw_questions)}"

d_counts = {1: 0, 2: 0, 3: 0}
for q in raw_questions:
    d_counts[q["d"]] += 1

print(f"DEBUG Batch 3 d_counts: {d_counts}")
assert d_counts[1] == 30, f"Expected 30 d1, got {d_counts[1]}"
assert d_counts[2] == 40, f"Expected 40 d2, got {d_counts[2]}"
assert d_counts[3] == 30, f"Expected 30 d3, got {d_counts[3]}"

formatted = assemble_batch(raw_questions, 3)
save_json(formatted, "tools/staging/cheers_batch3.json")
print("Saved tools/staging/cheers_batch3.json successfully!")
