#!/usr/bin/env python3
"""
Generate Batch 1: NBC 'Must See TV' Titans (100 questions)
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from sitcom_builder import make_batch

q_batch1 = [
    # Seinfeld (25 questions)
    {
        "q": "In the Season 6 episode 'The Switch', what is Cosmo Kramer's first name finally revealed to be after years of mystery?",
        "correct": "Cosmo",
        "distractors": ["Conrad", "Casper", "Cornelius"],
        "d": 1
    },
    {
        "q": "What is George Costanza's favorite fake alias and occupation whenever he wants to sound sophisticated or avoid being recognized?",
        "correct": "Art Vandelay, Architect",
        "distractors": ["Kel Varnsen, Importer-Exporter", "H.E. Pennypacker, Industrialist", "Martin Van Nostrand, Physician"],
        "d": 1
    },
    {
        "q": "What name did George and Jerry give to Elaine Benes' bizarre, spasmodic dance moves in 'The Little Kicks'?",
        "correct": "A full body dry heave set to music",
        "distractors": ["The frantic windmill shimmy", "A caffeinated flamingo convulsion", "The Elaine shuffle tremor"],
        "d": 2
    },
    {
        "q": "What iconic catchphrase does the strict proprietor of the soup stand, dubbed 'The Soup Nazi', bark at customers who violate ordering protocol?",
        "correct": "No soup for you!",
        "distractors": ["Step outside now!", "One year ban!", "Soup is over!"],
        "d": 1
    },
    {
        "q": "Introduced by Frank Costanza, what is the slogan of the secular holiday Festivus?",
        "correct": "A Festivus for the rest of us!",
        "distractors": ["Grievances bring us together!", "Feats of strength for all!", "No tinsel, just truth!"],
        "d": 1
    },
    {
        "q": "In the award-winning Seinfeld episode 'The Contest', what specific euphemism did the four friends use to describe refraining from self-gratification?",
        "correct": "Master of your domain",
        "distractors": ["Captain of your vessel", "Ruler of your urges", "King of your castle"],
        "d": 1
    },
    {
        "q": "In the episode 'The Junior Mint', what candy inadvertently falls into an open surgical cavity during an operation watched by Jerry and Kramer?",
        "correct": "A Junior Mint",
        "distractors": ["A Milk Dud", "A Good & Plenty", "A Raisinet"],
        "d": 1
    },
    {
        "q": "In 'The Marine Biologist', what object does George triumphantly pull from the blowhole of a beached whale at the climax of his famous monologue?",
        "correct": "A Titleist golf ball",
        "distractors": ["A Wilson tennis ball", "A Spalding baseball", "A Top Flite golf tee"],
        "d": 1
    },
    {
        "q": "In 'The Puffy Shirt', why did Jerry unintentionally agree to wear an outrageous pirate-style shirt on The Today Show?",
        "correct": "Kramer's girlfriend was a low-talker and Jerry nodded without hearing her",
        "distractors": ["He lost a bet over a game of Risk with Newman", "George accidentally swapped their dry cleaning bags", "Kramer convinced him it was the new Parisian haute couture"],
        "d": 2
    },
    {
        "q": "In 'The Rye', how do Jerry and George sneak a loaf of marble rye back into the Rosses' apartment after Frank Costanza took it back?",
        "correct": "They hoist it up through a third-story window on a fishing line",
        "distractors": ["Newman delivers it concealed inside a US Postal bag", "Kramer slides it down an air conditioning vent", "George smuggles it under his trench coat disguised as a baby"],
        "d": 2
    },
    {
        "q": "Why was restaurant owner Babu Bhatt ultimately deported to Pakistan in Season 4 of Seinfeld?",
        "correct": "Jerry held Babu's mail while he was away and Babu's visa renewal application arrived too late",
        "distractors": ["Elaine accidentally shredded Babu's green card in the Peterman office", "George reported his restaurant to the health board out of spite", "Kramer provided false testimony at an immigration hearing"],
        "d": 2
    },
    {
        "q": "What argument do Jerry and Kenny Bania repeatedly have regarding their agreement for Jerry to receive an Armani suit?",
        "correct": "Whether soup at Mendy's counts as an official meal",
        "distractors": ["Whether Kenny can open for Jerry at Carolines", "Whether dry cleaning costs are included with the jacket", "Whether a hot dog at Yankee Stadium fulfills the promise"],
        "d": 1
    },
    {
        "q": "What is Newman's official day job throughout the run of Seinfeld?",
        "correct": "United States Postal Service mail carrier",
        "distractors": ["Building superintendent and handyman", "New York City sanitation inspector", "Transit authority token booth clerk"],
        "d": 1
    },
    {
        "q": "What job did Elaine Benes hold after leaving Pendant Publishing and before editing the J. Peterman Catalog?",
        "correct": "Personal assistant to the eccentric socialite Mr. Pitt",
        "distractors": ["Fact-checker for The New Yorker", "Copywriter for Barney's New York", "Manuscript screener for Simon & Schuster"],
        "d": 2
    },
    {
        "q": "In the landmark Season 2 bottle episode 'The Chinese Restaurant', who is the hostess calling out for repeatedly over the loudspeaker while the group waits?",
        "correct": "Cartwright",
        "distractors": ["Costanza", "Vandelay", "Kramer"],
        "d": 2
    },
    {
        "q": "In 'The Parking Garage', where is the group stranded for the entirety of the episode?",
        "correct": "A multi-level parking garage in a New Jersey shopping mall",
        "distractors": ["The basement garage of Yankee Stadium", "The Port Authority bus terminal basement", "The long-term parking lot at JFK Airport"],
        "d": 1
    },
    {
        "q": "During the development of Seinfeld, which NBC executive famously risked his own division's budget to order four episodes after the pilot tested poorly?",
        "correct": "Rick Ludwin",
        "distractors": ["Warren Littlefield", "Brandon Tartikoff", "Don Ohlmeyer"],
        "d": 3
    },
    {
        "q": "Who was the real-life former neighbor of Larry David who inspired the character of Cosmo Kramer?",
        "correct": "Kenny Kramer",
        "distractors": ["Pete Kramer", "Arthur Kramer", "Stanley Kramer"],
        "d": 2
    },
    {
        "q": "What historic American entertainment figure passed away on the evening of May 14, 1998, as millions of Americans were tuned to the Seinfeld series finale?",
        "correct": "Frank Sinatra",
        "distractors": ["Dean Martin", "Bob Hope", "Sammy Davis Jr."],
        "d": 2
    },
    {
        "q": "In Newman's first voice-only appearance in Season 2's 'The Revenge', who originally provided his voice before Wayne Knight re-recorded it for syndication?",
        "correct": "Larry David",
        "distractors": ["Jerry Seinfeld", "Jason Alexander", "Tom Cherones"],
        "d": 3
    },
    {
        "q": "Who was originally cast as the female lead in the Seinfeld pilot ('The Seinfeld Chronicles') before Julia Louis-Dreyfus joined as Elaine?",
        "correct": "Lee Garlington, playing a waitress named Claire",
        "distractors": ["Patricia Heaton, playing Jerry's sister Ellen", "Megan Mullally, playing an ex-girlfriend named Laura", "Janeane Garofalo, playing a comedian named Jeannie"],
        "d": 3
    },
    {
        "q": "How much money per episode did NBC reportedly offer Jerry Seinfeld to return for a tenth season, an offer he famously declined?",
        "correct": "$5 million per episode",
        "distractors": ["$2 million per episode", "$3.5 million per episode", "$7.5 million per episode"],
        "d": 2
    },
    {
        "q": "In the Season 9 episode 'The Betrayal' (the backwards episode), where does the entire gang travel for Sue Ellen Mishke's wedding?",
        "correct": "India",
        "distractors": ["Italy", "Mexico", "Morocco"],
        "d": 2
    },
    {
        "q": "What book did George Costanza take into the Brentano's bookstore bathroom, forcing him to buy it because it was 'flagged'?",
        "correct": "A French Impressionist art book",
        "distractors": ["A biography of Winston Churchill", "An encyclopedia of world architecture", "A coffee table book about vintage sports cars"],
        "d": 2
    },
    {
        "q": "What was the final dialogue spoken between Jerry and George inside the prison cell at the conclusion of the Seinfeld series finale?",
        "correct": "A conversation about the placement of the second button on George's shirt",
        "distractors": ["A debate about whether cereal is better than eggs for breakfast", "An argument about whether Newman had intentionally ratted them out", "A discussion about whether Art Vandelay would represent them on appeal"],
        "d": 2
    },

    # Frasier (20 questions)
    {
        "q": "What are the call letters and AM frequency of the Seattle radio station where Dr. Frasier Crane hosts his call-in therapy show?",
        "correct": "KACL 780 AM",
        "distractors": ["KXYL 950 AM", "KSEA 1010 AM", "KWMT 640 AM"],
        "d": 2
    },
    {
        "q": "What is the name of Frasier Crane's spirited, sharp-tongued radio producer at KACL?",
        "correct": "Roz Doyle",
        "distractors": ["Daphne Moon", "Lilith Sternin", "Faye Moskowitz"],
        "d": 1
    },
    {
        "q": "While Dr. Frasier Crane adheres to Freudian psychiatry, which school of psychological thought does his brother Dr. Niles Crane strictly champion?",
        "correct": "Jungian",
        "distractors": ["Behavioral", "Cognitive-Constructivist", "Gestalt"],
        "d": 2
    },
    {
        "q": "What brand of blue-collar canned beer does Martin Crane stubbornly insist on drinking, to the horror of his connoisseur sons?",
        "correct": "Ballantine",
        "distractors": ["Schlitz", "Pabst Blue Ribbon", "Hamm's"],
        "d": 2
    },
    {
        "q": "What dog breed was Eddie, Martin Crane's intensely staring companion who frequently tormented Frasier?",
        "correct": "Jack Russell Terrier",
        "distractors": ["Wire Fox Terrier", "Beagle", "Parson Russell Terrier"],
        "d": 1
    },
    {
        "q": "What was the name of Niles Crane's wealthy, hyper-germophobic, unseen first wife throughout the early seasons of Frasier?",
        "correct": "Maris",
        "distractors": ["Mel", "Lilith", "Sherry"],
        "d": 1
    },
    {
        "q": "At which upscale coffee shop do Frasier and Niles meet daily to drink macchiatos, lattes, and dissect their anxieties?",
        "correct": "Cafe Nervosa",
        "distractors": ["The Daily Grind", "Espresso Royale", "Cafe Seattle"],
        "d": 1
    },
    {
        "q": "In which English city was physical therapist and self-proclaimed psychic Daphne Moon raised alongside her rowdy brothers?",
        "correct": "Manchester",
        "distractors": ["Liverpool", "Birmingham", "Leeds"],
        "d": 2
    },
    {
        "q": "How many consecutive Primetime Emmy Awards for Outstanding Comedy Series did Frasier win between 1994 and 1998?",
        "correct": "Five",
        "distractors": ["Three", "Four", "Six"],
        "d": 2
    },
    {
        "q": "What was the biological age difference between Kelsey Grammer and John Mahoney, who portrayed his father Martin Crane?",
        "correct": "John Mahoney was only 15 years older than Kelsey Grammer",
        "distractors": ["John Mahoney was 24 years older than Kelsey Grammer", "John Mahoney was only 8 years older than Kelsey Grammer", "They were the exact same age in real life"],
        "d": 3
    },
    {
        "q": "Why did the creators of Frasier create the role of Niles Crane specifically for David Hyde Pierce?",
        "correct": "The casting director noticed his striking physical resemblance to a young Kelsey Grammer",
        "distractors": ["He had played Frasier's cousin in an un-aired Cheers episode", "Kelsey Grammer had co-starred with him on Broadway and demanded his hiring", "He originally auditioned to play Frasier Crane on Cheers back in 1984"],
        "d": 2
    },
    {
        "q": "Who was originally cast and began rehearsals as radio producer Roz Doyle before being replaced by Peri Gilpin?",
        "correct": "Lisa Kudrow",
        "distractors": ["Jane Lynch", "Bonnie Hunt", "Cynthia Nixon"],
        "d": 2
    },
    {
        "q": "What is Frasier Crane's signature sign-off catchphrase at the end of each KACL radio broadcast?",
        "correct": "Good night, Seattle, and good mental health",
        "distractors": ["Stay thoughtful, Seattle, and stay balanced", "Seattle, you have been heard and understood", "Be kind to your minds, Seattle"],
        "d": 1
    },
    {
        "q": "Who sang the iconic closing credits theme song 'Tossed Salads and Scrambled Eggs' on Frasier?",
        "correct": "Kelsey Grammer",
        "distractors": ["David Hyde Pierce", "Bruce Miller", "Tom Anderson"],
        "d": 1
    },
    {
        "q": "In the classic French farce-style episode 'The Ski Lodge', who was the handsome French ski instructor Guy actually attempting to seduce?",
        "correct": "Niles",
        "distractors": ["Frasier", "Daphne", "Annie the swimsuit model"],
        "d": 2
    },
    {
        "q": "What is the name of Frasier's high-rise condominium complex overlooking the Seattle skyline?",
        "correct": "The Elliott Bay Towers",
        "distractors": ["The Space Needle Promenade", "The Puget Sound Terraces", "The Cascade Heights"],
        "d": 2
    },
    {
        "q": "What was the name of the boisterous, obnoxious sports show host at KACL played by Dan Butler?",
        "correct": "Bob 'Bulldog' Briscoe",
        "distractors": ["Gil Chesterton", "Noel Shempsky", "Kenny Daly"],
        "d": 1
    },
    {
        "q": "What was the name of the show's resident food and wine critic at KACL, known for his refined theatrical manner?",
        "correct": "Gil Chesterton",
        "distractors": ["Noel Shempsky", "Father Mike", "Chopper Dave"],
        "d": 2
    },
    {
        "q": "What was the name of the canine actor that originally portrayed Martin's dog Eddie and became one of TV's biggest animal stars?",
        "correct": "Moose",
        "distractors": ["Enzo", "Skippy", "Spike"],
        "d": 2
    },
    {
        "q": "In the Season 7 finale 'Something Borrowed, Someone Blue', whose impending wedding does Daphne Moon run away from to be with Niles?",
        "correct": "Donny Douglas",
        "distractors": ["Clive Cabot", "Rodney Banks", "Dr. Mel Karnofsky"],
        "d": 2
    },

    # Mad About You (12 questions)
    {
        "q": "On Mad About You, what is Paul Buchman's creative profession in New York City?",
        "correct": "Documentary filmmaker",
        "distractors": ["Advertising copywriter", "Architectural draftsman", "Stand-up comedian"],
        "d": 1
    },
    {
        "q": "What field did Jamie Buchman (played by Helen Hunt) work in during the majority of Mad About You?",
        "correct": "Public relations",
        "distractors": ["Fashion journalism", "Corporate law", "Interior design"],
        "d": 2
    },
    {
        "q": "What breed of lovable, somewhat lethargic dog was Murray on Mad About You?",
        "correct": "Collie mix",
        "distractors": ["Golden Retriever", "Basset Hound", "Old English Sheepdog"],
        "d": 2
    },
    {
        "q": "What acronym inspired the name of Paul and Jamie's daughter Mabel, born in Season 5?",
        "correct": "Mothers Always Bring Extra Love",
        "distractors": ["May All Babies Experience Laughter", "Miracles Always Begin Everyday Life", "Mom And Buchman Everlasting Love"],
        "d": 2
    },
    {
        "q": "Which Friends character originated as an eccentric, neglectful waitress at Riff's Bar on Mad About You?",
        "correct": "Ursula Buffay",
        "distractors": ["Phoebe Buffay", "Janice Hosenstein", "Gunther"],
        "d": 1
    },
    {
        "q": "In a Season 1 crossover episode, which Seinfeld character appears in Paul's old bachelor apartment because he sublets it from him?",
        "correct": "Cosmo Kramer",
        "distractors": ["George Costanza", "Newman", "Jerry Seinfeld"],
        "d": 1
    },
    {
        "q": "Which legendary comedy icon won three consecutive Primetime Emmy Awards for Outstanding Guest Actor playing Paul's Uncle Phil?",
        "correct": "Mel Brooks",
        "distractors": ["Carl Reiner", "Sid Caesar", "Buddy Hackett"],
        "d": 2
    },
    {
        "q": "How many consecutive Emmy Awards for Outstanding Lead Actress in a Comedy Series did Helen Hunt win for Mad About You?",
        "correct": "Four",
        "distractors": ["Two", "Three", "Five"],
        "d": 3
    },
    {
        "q": "What technical feat made the Season 6 Mad About You episode 'The Conversation' famous in television history?",
        "correct": "It was filmed in a single continuous 20-minute take outside baby Mabel's bedroom door",
        "distractors": ["It was broadcast completely live across all US time zones without a tape delay", "It contained zero spoken dialogue for the entire 22 minutes", "It was shot entirely from the perspective of Murray the dog"],
        "d": 3
    },
    {
        "q": "Who sang the original version of the Mad About You theme song 'Final Frontier' during the show's early seasons?",
        "correct": "Andrew Gold",
        "distractors": ["Paul Reiser", "Anita Baker", "James Taylor"],
        "d": 3
    },
    {
        "q": "Prior to Season 7, Helen Hunt and Paul Reiser made industry headlines by negotiating contracts that paid them how much per episode?",
        "correct": "$1 million per episode",
        "distractors": ["$500,000 per episode", "$750,000 per episode", "$1.5 million per episode"],
        "d": 2
    },
    {
        "q": "What was the name of Jamie's neurotic, chronically wandering sister played by Leila Kenzle?",
        "correct": "Fran Devanow",
        "distractors": ["Lisa Stemple", "Debbie Buchman", "Sylvia Buchman"],
        "d": 2
    },

    # Wings (10 questions)
    {
        "q": "What small airfield on Nantucket Island, Massachusetts serves as the primary setting for the sitcom Wings?",
        "correct": "Tom Nevers Field",
        "distractors": ["Cape Cod Regional Airport", "Martha's Vineyard Field", "Brant Point Municipal Airport"],
        "d": 2
    },
    {
        "q": "What is the name of the one-plane commuter airline operated by brothers Joe and Brian Hackett?",
        "correct": "Sandpiper Air",
        "distractors": ["Nantucket Flyer", "Seagull Airways", "Island Hopper Air"],
        "d": 1
    },
    {
        "q": "Who operated Aeromass, the larger, ruthless rival airline located across the terminal from Sandpiper Air?",
        "correct": "Roy Biggins",
        "distractors": ["Lowell Mather", "Carlton Blanchard", "Alex Lambert"],
        "d": 1
    },
    {
        "q": "What business did Helen Chappel operate inside the airport terminal before later marrying Joe Hackett?",
        "correct": "The airport lunch counter",
        "distractors": ["The souvenir gift kiosk", "The baggage claim office", "The car rental desk"],
        "d": 1
    },
    {
        "q": "What was the profession of eccentric, dim-witted airport regular Lowell Mather, played by Thomas Haden Church?",
        "correct": "Aircraft and terminal mechanic",
        "distractors": ["Air traffic controller", "Luggage loader", "Fuel truck driver"],
        "d": 1
    },
    {
        "q": "Which actor had his comedic breakout role on Wings as the earnest, melancholic Italian immigrant taxi driver Antonio Scarpacci?",
        "correct": "Tony Shalhoub",
        "distractors": ["Hank Azaria", "Joe Mantegna", "Dan Castellaneta"],
        "d": 2
    },
    {
        "q": "Wings was created by David Angell, Peter Casey, and David Lee, who also created which other legendary NBC sitcom?",
        "correct": "Frasier",
        "distractors": ["NewsRadio", "Mad About You", "Just Shoot Me!"],
        "d": 2
    },
    {
        "q": "Why did Thomas Haden Church leave Wings in Season 6?",
        "correct": "To star in the Fox sitcom 'Ned and Stacey' opposite Debra Messing",
        "distractors": ["To star in the feature film 'George of the Jungle'", "Contract disputes regarding his salary demands", "To direct independent feature films in Texas"],
        "d": 3
    },
    {
        "q": "What classical musical instrument did Helen Chappel aspire to play professionally throughout the series?",
        "correct": "Cello",
        "distractors": ["Violin", "Flute", "Oboe"],
        "d": 2
    },
    {
        "q": "Which Cheers character made a famous crossover guest appearance on Wings with his wife Lilith in the episode 'Planes, Trains and Visiting Cranes'?",
        "correct": "Dr. Frasier Crane",
        "distractors": ["Norm Peterson", "Cliff Clavin", "Woody Boyd"],
        "d": 2
    },

    # NewsRadio (13 questions)
    {
        "q": "What is the name and format of the New York City radio station setting in the critically acclaimed sitcom NewsRadio?",
        "correct": "WNYX, an all-news AM station",
        "distractors": ["WKRP, a top-40 music station", "WNYP, a shock-jock morning station", "WNYC, an NPR-style public station"],
        "d": 1
    },
    {
        "q": "Who portrayed the eccentric, fabulously wealthy station owner Jimmy James on NewsRadio?",
        "correct": "Stephen Root",
        "distractors": ["Phil Hartman", "Dave Foley", "Maury Chaykin"],
        "d": 1
    },
    {
        "q": "Dave Nelson, the mild-mannered news director hired to run WNYX, was played by which Canadian comedy troupe alumnus?",
        "correct": "Dave Foley (The Kids in the Hall)",
        "distractors": ["Kevin McDonald", "Mark McKinney", "Scott Thompson"],
        "d": 1
    },
    {
        "q": "What was the name of the narcissistic, pompous, yet deeply insecure anchor brilliantly portrayed by Phil Hartman on NewsRadio?",
        "correct": "Bill McNeal",
        "distractors": ["Dave Nelson", "Matthew Brock", "Joe Garrelli"],
        "d": 1
    },
    {
        "q": "Which future podcast giant and UFC commentator played the conspiracy-obsessed handyman and broadcast technician Joe Garrelli on NewsRadio?",
        "correct": "Joe Rogan",
        "distractors": ["Adam Carolla", "Marc Maron", "Jimmy Kimmel"],
        "d": 1
    },
    {
        "q": "In the famous NewsRadio episode 'Super Karate Monkey Death Car', what was the titular phrase actually taken from?",
        "correct": "Jimmy James' autobiography translated into Japanese and awkwardly re-translated back into English",
        "distractors": ["A bootlegged Japanese martial arts VHS tape found in the basement", "A punk rock album recorded by Matthew Brock in college", "An unlicensed arcade game installed in the breakroom by Joe Garrelli"],
        "d": 2
    },
    {
        "q": "Following the tragic death of Phil Hartman in 1998, which close personal friend of Hartman joined the cast of NewsRadio as Max Louis?",
        "correct": "Jon Lovitz",
        "distractors": ["Dana Carvey", "Kevin Nealon", "Dennis Miller"],
        "d": 2
    },
    {
        "q": "What was the title of the emotional Season 5 premiere of NewsRadio that addressed the sudden death of Phil Hartman's character Bill McNeal?",
        "correct": "Bill Moves On",
        "distractors": ["Farewell to Bill", "The Anchor's Final Sign-off", "Remembering WNYX"],
        "d": 2
    },
    {
        "q": "Who created NewsRadio after spending years as a writer on Late Night with David Letterman and The Larry Sanders Show?",
        "correct": "Paul Simms",
        "distractors": ["Garry Shandling", "Chuck Lorre", "Bill Lawrence"],
        "d": 3
    },
    {
        "q": "In Season 3 of NewsRadio, why was Jimmy James arrested and investigated by the FBI?",
        "correct": "He was accused of being the legendary fugitive skyjacker D.B. Cooper",
        "distractors": ["He was suspected of running an offshore tax shelter in Bermuda", "He was mistakenly identified as an international art thief", "He intercepted classified military satellite signals from the roof"],
        "d": 2
    },
    {
        "q": "What was the name of the bumbling, perpetually bullied dentist-turned-reporter played by Andy Dick on NewsRadio?",
        "correct": "Matthew Brock",
        "distractors": ["Stewart Bell", "Arthur Fortune", "Frank Lambert"],
        "d": 1
    },
    {
        "q": "What distinct physical comedy prop becomes the center of a battle for office dominance between Dave and Bill in Season 2's 'The Cane'?",
        "correct": "A stylish antique walking stick",
        "distractors": ["An oversized executive leather throne", "A vintage brass megaphone", "A championship wrestling belt"],
        "d": 2
    },
    {
        "q": "Which actress played Lisa Miller, Dave Nelson's ambitious co-worker and on-again/off-again girlfriend who could do complex math in her head?",
        "correct": "Maura Tierney",
        "distractors": ["Vicki Lewis", "Khandi Alexander", "Lauren Graham"],
        "d": 2
    },

    # 3rd Rock from the Sun (10 questions)
    {
        "q": "What human identity and university teaching post does the alien High Commander assume on 3rd Rock from the Sun?",
        "correct": "Dick Solomon, Professor of Physics",
        "distractors": ["Arthur Solomon, Professor of Anthropology", "Donald Solomon, Professor of Astronomy", "Richard Solomon, Professor of Philosophy"],
        "d": 1
    },
    {
        "q": "Which decorated military officer alien is furious at having been assigned the body of an attractive human female on 3rd Rock from the Sun?",
        "correct": "Lieutenant Sally Solomon",
        "distractors": ["Commander Mary Albright", "Ensign Nina Campbell", "Sergeant Vicki Dubcek"],
        "d": 1
    },
    {
        "q": "What is the alien communications officer Harry Solomon's physical method of receiving transmissions from home?",
        "correct": "His body violently jerks, his eyes roll back, and his mouth opens as an audio speaker",
        "distractors": ["His left ear glows green and emits Morse code beeps", "He begins involuntarily tap-dancing across the furniture", "His fingers automatically type transcripts on any flat surface"],
        "d": 2
    },
    {
        "q": "Despite being the oldest and wisest member of the alien mission, Tommy Solomon is assigned to inhabit which human form?",
        "correct": "A pubescent teenage boy",
        "distractors": ["An elderly grandfather", "A newborn infant", "A family sheepdog"],
        "d": 1
    },
    {
        "q": "What is the title of the supreme, god-like leader of the alien expedition on 3rd Rock from the Sun?",
        "correct": "The Big Giant Head",
        "distractors": ["The Supreme Overseer", "The Cosmic Commander", "The Grand Celestial Mind"],
        "d": 1
    },
    {
        "q": "Which science-fiction television icon was cast as the human manifestation of The Big Giant Head in Season 5?",
        "correct": "William Shatner",
        "distractors": ["Leonard Nimoy", "Patrick Stewart", "George Takei"],
        "d": 1
    },
    {
        "q": "How many Primetime Emmy Awards for Outstanding Lead Actor in a Comedy Series did John Lithgow win for playing Dick Solomon?",
        "correct": "Three",
        "distractors": ["One", "Two", "Four"],
        "d": 2
    },
    {
        "q": "What is the name of the Solomons' brassy, sexually uninhibited landlady who lives downstairs?",
        "correct": "Mrs. Dubcek",
        "distractors": ["Mrs. Albright", "Mrs. Strudwick", "Mrs. McGovern"],
        "d": 1
    },
    {
        "q": "Which Saturday Night Live original cast member starred opposite John Lithgow as Dr. Mary Albright?",
        "correct": "Jane Curtin",
        "distractors": ["Laraine Newman", "Gilda Radner", "Catherine O'Hara"],
        "d": 2
    },
    {
        "q": "Which young actor launched his celebrated Hollywood career portraying the alien teenager Tommy Solomon on 3rd Rock from the Sun?",
        "correct": "Joseph Gordon-Levitt",
        "distractors": ["Elijah Wood", "Jonathan Taylor Thomas", "Seth Green"],
        "d": 1
    },

    # Will & Grace (10 questions)
    {
        "q": "What were the respective professions of Will Truman and Grace Adler when the series debuted in 1998?",
        "correct": "Will was a corporate lawyer and Grace was an interior designer",
        "distractors": ["Will was an art dealer and Grace was an architect", "Will was a prosecutor and Grace was a fashion stylist", "Will was a literary agent and Grace was a graphic artist"],
        "d": 1
    },
    {
        "q": "What was the title of Jack McFarland's flamboyant, self-produced one-man cabaret show in the early seasons?",
        "correct": "Just Jack",
        "distractors": ["Jack Spectacular", "All About Jack", "Jack Attack!"],
        "d": 1
    },
    {
        "q": "What was the name of Karen Walker's sharp-witted Salvadoran maid and confidante, played by Shelley Morrison?",
        "correct": "Rosario Salazar",
        "distractors": ["Consuela Lopez", "Maria Gomez", "Esperanza Ramos"],
        "d": 1
    },
    {
        "q": "What vocal change did Megan Mullally famously introduce to her character Karen Walker after shooting the pilot episode?",
        "correct": "She dramatically elevated Karen's pitch to a squeaky, martini-fueled nasal register",
        "distractors": ["She adopted a transatlantic Katharine Hepburn aristocratic cadence", "She introduced a deep husky smoker's drawl", "She adopted a faux British finishing school accent"],
        "d": 2
    },
    {
        "q": "Will & Grace joined which elite group of only three sitcoms in television history where every credited principal cast member won an Emmy?",
        "correct": "All in the Family and The Golden Girls",
        "distractors": ["Seinfeld and Cheers", "The Mary Tyler Moore Show and Frasier", "M*A*S*H and Taxi"],
        "d": 3
    },
    {
        "q": "What was the name of Karen Walker's extremely wealthy, notoriously obese husband who was never clearly seen on camera?",
        "correct": "Stan Walker",
        "distractors": ["Lyle Finster", "Malcolm Widmark", "Scott Woolley"],
        "d": 1
    },
    {
        "q": "What breed and name was Jack McFarland's beloved dog in the early seasons of Will & Grace?",
        "correct": "A Jack Russell Terrier named Klaus Von Puppy",
        "distractors": ["A Yorkshire Terrier named Coco Chanel", "A French Bulldog named Monsieur Fifi", "A Chihuahua named Guapo"],
        "d": 2
    },
    {
        "q": "In the pilot episode of Will & Grace, what event nearly causes Grace to move in with her fiancé rather than Will?",
        "correct": "Grace is about to marry her boyfriend Danny before walking out on the wedding",
        "distractors": ["Grace gets an offer to move to Paris for a design firm", "Grace buys a loft in Soho with her business partner", "Grace gets back together with her college boyfriend"],
        "d": 2
    },
    {
        "q": "Which future U.S. President famously praised Will & Grace on Meet the Press in 2012 for educating the public on LGBTQ+ rights?",
        "correct": "Joe Biden",
        "distractors": ["Barack Obama", "Bill Clinton", "Al Gore"],
        "d": 2
    },
    {
        "q": "Who created Will & Grace, drawing heavily on their own real-life friendship as a gay man and a straight Jewish woman?",
        "correct": "David Kohan and Max Mutchnick",
        "distractors": ["Marta Kauffman and David Crane", "Chuck Lorre and Bill Prady", "Steve Levitan and Christopher Lloyd"],
        "d": 2
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "staging", "90s_sitcoms_batch1.json")
    make_batch(q_batch1, 1, out)
