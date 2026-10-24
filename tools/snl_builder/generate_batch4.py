#!/usr/bin/env python3
"""
Generate SNL Batch 4: Weekend Update Lore, Anchors, Catchphrases & Correspondents (1975-2025)
100 questions: exactly 30 d1, 40 d2, 30 d3.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from builder import build_batch

questions = [
    # 1
    {
        "q": "What was Chevy Chase's signature opening greeting on Weekend Update during Season 1?",
        "correct": "I'm Chevy Chase and you're not",
        "distractors": ["Good evening, I'm Chevy Chase", "Live from the Update desk, I'm Chevy Chase", "Here is the news with Chevy Chase"],
        "d": 1
    },
    # 2
    {
        "q": "What recurring running gag did Chevy Chase report on Weekend Update for weeks in late 1975?",
        "correct": "Generalissimo Francisco Franco is still dead",
        "distractors": ["The stock market has officially collapsed", "Richard Nixon is still under house arrest", "The metric system has been rejected again"],
        "d": 1
    },
    # 3
    {
        "q": "In the famous 'Point/Counterpoint' debates on Weekend Update, what opening retort did Dan Aykroyd always sling at Jane Curtin?",
        "correct": "Jane, you ignorant slut!",
        "distractors": ["Jane, you foolish woman!", "Jane, you naive amateur!", "Jane, you blind ideologue!"],
        "d": 1
    },
    # 4
    {
        "q": "What was Jane Curtin's standard opening rebuttal to Dan Aykroyd during 'Point/Counterpoint'?",
        "correct": "Dan, you pompous ass!",
        "distractors": ["Dan, you arrogant clown!", "Dan, you reckless loudmouth!", "Dan, you heartless reactionary!"],
        "d": 2
    },
    # 5
    {
        "q": "Who was the first woman to anchor Weekend Update in SNL history?",
        "correct": "Jane Curtin",
        "distractors": ["Gilda Radner", "Laraine Newman", "Tina Fey"],
        "d": 1
    },
    # 6
    {
        "q": "What was Dennis Miller's signature sign-off catchphrase at the end of every Weekend Update broadcast between 1985 and 1991?",
        "correct": "I am Dennis Miller, and that's the news, and I am outta here!",
        "distractors": ["Good night, good luck, and see you next Saturday!", "That's how the world turns, stay safe out there!", "That's our show, tune in next week for more!"],
        "d": 1
    },
    # 7
    {
        "q": "What physical gesture did Dennis Miller always perform right as he delivered his Weekend Update sign-off?",
        "correct": "Flipping his pencil onto the desk or into the air",
        "distractors": ["Crumping up his script into a ball", "Tapping his glasses on the microphone", "Giving a thumbs-up to the camera"],
        "d": 2
    },
    # 8
    {
        "q": "What was the hallmark of Dennis Miller's comedic style as Weekend Update anchor?",
        "correct": "Esoteric pop culture, classical literature, and historical analogies",
        "distractors": ["Slapstick pratfalls and prop comedy", "Singing Broadway parodies with a ukulele", "Reading audience letters with accents"],
        "d": 2
    },
    # 9
    {
        "q": "During the early 1980s under producer Dick Ebersol, what was the Weekend Update segment renamed?",
        "correct": "SNL NewsBreak and Saturday Night News",
        "distractors": ["The Midnight Report", "Rockefeller Newsline", "NBC Satire News"],
        "d": 2
    },
    # 10
    {
        "q": "Which anchor hosted 'Saturday Night News' from 1982 to 1984 before being succeeded by Christopher Guest?",
        "correct": "Brad Hall",
        "distractors": ["Brian Doyle-Murray", "Charles Rocket", "Joe Piscopo"],
        "d": 3
    },
    # 11
    {
        "q": "What character did Kevin Nealon create on Weekend Update who spoke mundane thoughts aloud while whispering honest, selfish impulses in parentheses?",
        "correct": "Mr. Subliminal (The Subliminal Man)",
        "distractors": ["The Secret Agent", "The Inner Monologue Guy", "The Hypnotist"],
        "d": 1
    },
    # 12
    {
        "q": "What recurring news figure was the relentless target of Norm Macdonald's Weekend Update jokes between 1994 and 1997?",
        "correct": "O.J. Simpson",
        "distractors": ["Bill Clinton", "Bob Dole", "Michael Jackson"],
        "d": 1
    },
    # 13
    {
        "q": "Following the 1995 O.J. Simpson criminal acquittal, what was Norm Macdonald's blunt opening joke on Weekend Update?",
        "correct": "Well, it is finally official: murder is now legal in the state of California",
        "distractors": ["The jury has spoken, and common sense has officially died", "If the glove doesn't fit, you must commit perjury", "Ladies and gentlemen, justice has taken a holiday"],
        "d": 1
    },
    # 14
    {
        "q": "Whenever an obscure crime or bizarre mystery was reported on Weekend Update, whom did Norm Macdonald invariably blame?",
        "correct": "You guessed it: Frank Stallone",
        "distractors": ["None other than David Hasselhoff", "The one and only Gary Busey", "Burt Reynolds, naturally"],
        "d": 1
    },
    # 15
    {
        "q": "Which NBC West Coast executive and personal friend of O.J. Simpson reportedly demanded Norm Macdonald's removal from Weekend Update in 1998?",
        "correct": "Don Ohlmeyer",
        "distractors": ["Warren Littlefield", "Jeff Zucker", "Brandon Tartikoff"],
        "d": 2
    },
    # 16
    {
        "q": "Who replaced Norm Macdonald as the anchor of Weekend Update in early 1998?",
        "correct": "Colin Quinn",
        "distractors": ["Jimmy Fallon", "Kevin Nealon", "Darrell Hammond"],
        "d": 2
    },
    # 17
    {
        "q": "What was Colin Quinn's signature opening question on Weekend Update delivered in his gravelly Brooklyn accent?",
        "correct": "Did you see this? Did you hear about this?",
        "distractors": ["What's the story, New York?", "Are you people following the news?", "Can you believe what happened this week?"],
        "d": 2
    },
    # 18
    {
        "q": "In the fall of 2000, which two performers debuted as a new co-anchoring team on Weekend Update?",
        "correct": "Tina Fey and Jimmy Fallon",
        "distractors": ["Tina Fey and Amy Poehler", "Jimmy Fallon and Horatio Sanz", "Seth Meyers and Amy Poehler"],
        "d": 1
    },
    # 19
    {
        "q": "When Tina Fey took the Weekend Update desk in 2000, what historic role did she already hold on the show?",
        "correct": "First female head writer in SNL history",
        "distractors": ["Youngest female producer in NBC history", "First Second City alumna on the writing staff", "First woman to direct an SNL episode"],
        "d": 1
    },
    # 20
    {
        "q": "When Jimmy Fallon departed SNL in 2004, who joined Tina Fey to create the first all-female Weekend Update anchor team?",
        "correct": "Amy Poehler",
        "distractors": ["Maya Rudolph", "Rachel Dratch", "Kristen Wiig"],
        "d": 1
    },
    # 21
    {
        "q": "What signature segment did Amy Poehler and Seth Meyers popularize where they took turns expressing utter disbelief at absurd headlines?",
        "correct": "Really!?! with Seth and Amy",
        "distractors": ["Are You Serious!?!", "No Way!?! with Seth and Amy", "Come On!?! with Seth and Amy"],
        "d": 1
    },
    # 22
    {
        "q": "Who holds the record as the longest-running anchor pairing in the entire history of Weekend Update?",
        "correct": "Colin Jost and Michael Che",
        "distractors": ["Tina Fey and Jimmy Fallon", "Seth Meyers and Amy Poehler", "Jane Curtin and Dan Aykroyd"],
        "d": 1
    },
    # 23
    {
        "q": "What beloved annual holiday tradition do Colin Jost and Michael Che participate in on the final episode of each calendar year?",
        "correct": "Writing jokes for each other to read completely sight-unseen",
        "distractors": ["Switching suits and identities for the entire broadcast", "Allowing the audience to write all the headlines live", "Donating their entire episode salaries to rival charities"],
        "d": 1
    },
    # 24
    {
        "q": "In one of their most famous joke swaps, what civil rights icon did Michael Che trick Colin Jost into insulting on air while a guest sat beside him?",
        "correct": "Coretta Scott King",
        "distractors": ["Rosa Parks", "Harriet Tubman", "Ruby Bridges"],
        "d": 2
    },
    # 25
    {
        "q": "In a 2023 joke swap, who did Michael Che invite onto the Weekend Update desk to sit in horrified silence next to Colin Jost?",
        "correct": "A practicing rabbi / civil rights activist named Dr. Hattie",
        "distractors": ["Colin Jost's real mother", "Scarlett Johansson's publicist", "A Catholic nun"],
        "d": 2
    },
    # 26
    {
        "q": "Which Hollywood star is married to Weekend Update co-anchor Colin Jost, making her a frequent target of Michael Che's joke swaps?",
        "correct": "Scarlett Johansson",
        "distractors": ["Anne Hathaway", "Emma Stone", "Natalie Portman"],
        "d": 1
    },
    # 27
    {
        "q": "What was the name of David Spade's ruthless 1990s segment where he skewered celebrities who made poor career choices?",
        "correct": "Hollywood Minute",
        "distractors": ["Celebrity Roast", "Spade's Take", "Tinseltown Takedown"],
        "d": 1
    },
    # 28
    {
        "q": "What notorious 1995 'Hollywood Minute' joke by David Spade caused Eddie Murphy to boycott SNL for over two decades?",
        "correct": "Showing a picture of Eddie Murphy and saying 'Look, children, a falling star! Make a wish!'",
        "distractors": ["Criticizing Eddie's performance in 'Beverly Hills Cop III'", "Imitating Eddie's distinctive laugh and calling it annoying", "Saying Eddie was too rich to be funny anymore"],
        "d": 2
    },
    # 29
    {
        "q": "What character did Chris Farley play on Weekend Update who frantically used finger air-quotes to describe his unappealing personal traits?",
        "correct": "Bennett Brauer",
        "distractors": ["Todd O'Connor", "Hank Murphy", "Barney Miller"],
        "d": 2
    },
    # 30
    {
        "q": "What did Bennett Brauer frequently admit via sarcastic air-quotes on Weekend Update?",
        "correct": "That he doesn't 'bathe regularly' and isn't 'what the ladies call handsome'",
        "distractors": ["That he doesn't 'pay taxes' and is 'wanted by Interpol'", "That he isn't 'licensed to practice' and has 'no legal degree'", "That he doesn't 'know how to read' and relies on 'gut feelings'"],
        "d": 2
    },
    # 31
    {
        "q": "What character did Bobby Moynihan portray as Michael Che's competitive high school friend who claimed he could do Che's job better?",
        "correct": "Riblet",
        "distractors": ["T-Bone", "Shorty", "D-Train"],
        "d": 2
    },
    # 32
    {
        "q": "What was Riblet's catchphrase before dropping the mic after delivering a news joke?",
        "correct": "Riblet took your jooooob!",
        "distractors": ["Riblet in the building!", "That's how Riblet does it!", "Bow down to Riblet!"],
        "d": 2
    },
    # 33
    {
        "q": "What was the name of Bill Hader's cantankerous, elderly local news correspondent who battered interviewees with his microphone?",
        "correct": "Herb Welch",
        "distractors": ["Walter Finch", "Chet Harper", "Frank Patterson"],
        "d": 1
    },
    # 34
    {
        "q": "What violent habit did Herb Welch have whenever interviewees annoyed him?",
        "correct": "Hitting them in the face with his handheld microphone",
        "distractors": ["Spitting his chewing tobacco on their shoes", "Throwing hot coffee into their laps", "Kicking them in the shins"],
        "d": 2
    },
    # 35
    {
        "q": "What recurring Weekend Update character played by Alex Moffat offered dating advice while subtly revealing his immense physical insecurities?",
        "correct": "Guy Who Just Bought a Boat",
        "distractors": ["Yacht Club Chad", "Wall Street Bradley", "Tinder Tyler"],
        "d": 1
    },
    # 36
    {
        "q": "What physical feature did 'Guy Who Just Bought a Boat' frequently reveal had embarrassing dimensions?",
        "correct": "His micro-penis",
        "distractors": ["His receding hairline", "His counterfeit luxury watch", "His high-pitched singing voice"],
        "d": 2
    },
    # 37
    {
        "q": "What was the name of Cecily Strong's rambling, uneducated 20-something character who gave nonsensical geopolitical opinions on Weekend Update?",
        "correct": "The Girl You Wish You Hadn't Started a Conversation with at a Party",
        "distractors": ["The Awkward Cousin at the Wedding", "The Uninformed Co-worker", "The Drunk Bridesmaid"],
        "d": 1
    },
    # 38
    {
        "q": "What was 'The Girl You Wish You Hadn't Started a Conversation With at a Party' always holding in her hand?",
        "correct": "A plastic cup of wine",
        "distractors": ["A cigarette holder", "An iPhone with a cracked screen", "A half-eaten taco"],
        "d": 2
    },
    # 39
    {
        "q": "What mispronounced word did 'The Girl You Wish You Hadn't Started a Conversation with at a Party' repeatedly use to sound worldly?",
        "correct": "Quoting incorrect facts about developing nations and saying 'Almost!'",
        "distractors": ["Calling Europe 'The Old Continent of Paris'", "Referring to the United Nations as 'The World Club'", "Calling the economy 'the monetary situation'"],
        "d": 3
    },
    # 40
    {
        "q": "What was the name of Heidi Gardner's socially awkward teen movie critic on Weekend Update who constantly hid behind her sleeves?",
        "correct": "Bailey Gismert",
        "distractors": ["Mackenzie Hollister", "Chloe Jenkins", "Riley Cooper"],
        "d": 2
    },
    # 41
    {
        "q": "Why was Bailey Gismert unable to give coherent movie reviews?",
        "correct": "She got overwhelmed with social anxiety and romantic crushes on actors",
        "distractors": ["She fell asleep in every movie theater", "She read reviews written by her grandmother", "She only watched trailers on YouTube"],
        "d": 2
    },
    # 42
    {
        "q": "What was Kenan Thompson's recurring Weekend Update character Willie known for?",
        "correct": "Finding a sunny, cheerful silver lining in unspeakable personal tragedies",
        "distractors": ["Exposing fraudulent charity organizations", "Inventing useless gadgets out of scrap metal", "Betting his entire life savings on horse races"],
        "d": 2
    },
    # 43
    {
        "q": "How did Sarah Sherman (Sarah Squirm) routinely treat Colin Jost during her Weekend Update appearances?",
        "correct": "Roasting him relentlessly with fake tabloid scandals and graphic body horror images",
        "distractors": ["Serenading him with Broadway love ballads", "Presenting him with homemade baked goods that explode", "Pretending to be his long-lost biological sister"],
        "d": 1
    },
    # 44
    {
        "q": "In 2022, what real-life Staten Island vehicle purchase made by Colin Jost and Pete Davidson became a running punchline on Weekend Update?",
        "correct": "A decommissioned Staten Island Ferry boat",
        "distractors": ["A municipal sanitation dump truck", "A fleet of motorized yellow taxicabs", "An antique horse-drawn carriage"],
        "d": 1
    },
    # 45
    {
        "q": "Which cast member appeared on Weekend Update in 2021 as a nervous 19th-century gold miner discovering modern technology?",
        "correct": "Mikey Day",
        "distractors": ["Kyle Mooney", "Beck Bennett", "Pete Davidson"],
        "d": 3
    },
    # 46
    {
        "q": "What catchphrase did Adam Sandler's Cajun Man use on Weekend Update, ending every single topical word with the sound '-shun'?",
        "correct": "Words like 'Depress-shun', 'Defla-shun', 'Erec-shun'",
        "distractors": ["Words ending in '-osity'", "Words ending in '-esque'", "Words ending in '-itude'"],
        "d": 2
    },
    # 47
    {
        "q": "Who was the anchor of Weekend Update during Season 6 (1980-1981) who infamously dropped the F-word during a live broadcast?",
        "correct": "Charles Rocket",
        "distractors": ["Brian Doyle-Murray", "Joe Piscopo", "Gail Matthius"],
        "d": 2
    },
    # 48
    {
        "q": "In what episode did Charles Rocket say the F-word on live television, leading directly to his firing shortly after?",
        "correct": "The Charlene Tilton episode parodying 'Who Shot J.R.?'",
        "distractors": ["The Bill Murray season opener", "The Steve Martin Christmas show", "The Chevy Chase return episode"],
        "d": 3
    },
    # 49
    {
        "q": "What phrase did Charles Rocket utter at the close of the February 21, 1981 episode that violated broadcast decency rules?",
        "correct": "I'd like to know who the f*** did it",
        "distractors": ["What the f*** is going on here", "This whole f***ing show is crazy", "I don't give a f*** who shot him"],
        "d": 3
    },
    # 50
    {
        "q": "Which anchor co-hosted 'SNL NewsBreak' with Mary Gross during the 1981-1982 season?",
        "correct": "Brian Doyle-Murray",
        "distractors": ["Eddie Murphy", "Joe Piscopo", "Tim Kazurinsky"],
        "d": 3
    },
    # 51
    {
        "q": "What musical instrument did Jimmy Fallon frequently play at the Weekend Update desk to perform comedic song parodies?",
        "correct": "Acoustic guitar",
        "distractors": ["Synthesizer keyboard", "Ukulele", "Harmonica"],
        "d": 1
    },
    # 52
    {
        "q": "Which Weekend Update anchor hosted the segment solo from 2008 until he was joined by Cecily Strong in the fall of 2013?",
        "correct": "Seth Meyers",
        "distractors": ["Jimmy Fallon", "Colin Jost", "Norm Macdonald"],
        "d": 1
    },
    # 53
    {
        "q": "In February 2014, Seth Meyers left the Weekend Update desk to take over which NBC late-night franchise?",
        "correct": "Late Night",
        "distractors": ["The Tonight Show", "Last Call", "Meet the Press"],
        "d": 1
    },
    # 54
    {
        "q": "Who served as Seth Meyers' co-anchor on Weekend Update during his final episode on February 1, 2014?",
        "correct": "Cecily Strong",
        "distractors": ["Colin Jost", "Michael Che", "Amy Poehler"],
        "d": 2
    },
    # 55
    {
        "q": "Who made a surprise appearance alongside Amy Poehler and Bill Hader to bid farewell to Seth Meyers on his last Update show?",
        "correct": "Stefon (who revealed he was married to Seth)",
        "distractors": ["Drunk Uncle", "David S. Pumpkins", "The Church Lady"],
        "d": 2
    },
    # 56
    {
        "q": "When Colin Jost made his Weekend Update anchor debut in March 2014, who was his original co-anchor?",
        "correct": "Cecily Strong",
        "distractors": ["Michael Che", "Tina Fey", "Vanessa Bayer"],
        "d": 2
    },
    # 57
    {
        "q": "In the fall of 2014, who replaced Cecily Strong behind the Weekend Update desk to partner with Colin Jost?",
        "correct": "Michael Che",
        "distractors": ["Pete Davidson", "Jay Pharoah", "Sasheer Zamata"],
        "d": 1
    },
    # 58
    {
        "q": "What historic milestone did Michael Che achieve when he was hired as Weekend Update co-anchor in 2014?",
        "correct": "First Black anchor in Weekend Update history",
        "distractors": ["Youngest anchor in show history", "First writer without sketch appearances to anchor", "First performer to anchor with no improv background"],
        "d": 2
    },
    # 59
    {
        "q": "Before joining SNL as an Update anchor and writer, what Comedy Central news satire was Michael Che a correspondent on?",
        "correct": "The Daily Show with Jon Stewart",
        "distractors": ["The Colbert Report", "Tosh.0", "The Nightly Show with Larry Wilmore"],
        "d": 2
    },
    # 60
    {
        "q": "What collegiate publication did Colin Jost serve as president of before being hired at Saturday Night Live in 2005?",
        "correct": "The Harvard Lampoon",
        "distractors": ["The Yale Record", "The Daily Princetonian", "The Columbia Jester"],
        "d": 2
    },
    # 61
    {
        "q": "What was the name of the recurring 1970s Weekend Update segment where Garrett Morris cupped his hands and shouted news headlines?",
        "correct": "News for the Hard of Hearing",
        "distractors": ["Loud News Network", "The Deaf Digest", "Shouting the Facts"],
        "d": 1
    },
    # 62
    {
        "q": "Which cast member portrayed 'Mickey the Dyke', an early recurring character on Weekend Update in the late 1970s?",
        "correct": "Jane Curtin",
        "distractors": ["Gilda Radner", "Laraine Newman", "Mary Gross"],
        "d": 3
    },
    # 63
    {
        "q": "What was the title of the recurring segment by Dan Aykroyd where he passionately defended bizarre consumer contraptions and dangerous toys?",
        "correct": "Consumer Probe",
        "distractors": ["Buyer Beware", "Watchdog Report", "Mainway On Patrol"],
        "d": 2
    },
    # 64
    {
        "q": "In a 2018 Weekend Update joke swap, what controversial civil rights leader did Colin Jost have to jokingly claim 'was no Martin Luther King'?",
        "correct": "Rosa Parks",
        "distractors": ["Malcolm X", "John Lewis", "Medgar Evers"],
        "d": 3
    },
    # 65
    {
        "q": "In a memorable 2015 appearance, which cast member delivered a candid monologue on Weekend Update defending Colin Jost from online haters while proposing marriage to him?",
        "correct": "Leslie Jones",
        "distractors": ["Kate McKinnon", "Aidy Bryant", "Sasheer Zamata"],
        "d": 2
    },
    # 66
    {
        "q": "What character did Fred Armisen play alongside Kristen Wiig as an unprepared, improvisational folk music duo on Weekend Update?",
        "correct": "Garth and Kat",
        "distractors": ["Craig and Arianna", "The Culps", "Pete and Penny"],
        "d": 1
    },
    # 67
    {
        "q": "What was the comedic gimmick of Fred Armisen and Kristen Wiig's 'Garth and Kat' appearances?",
        "correct": "They had not rehearsed and Fred made up songs on the spot while Kristen desperately tried to lip-sync along",
        "distractors": ["Their acoustic guitars were completely out of tune", "They sang in heavy Swedish accents with no English words", "They insulted the anchor between every single harmony"],
        "d": 2
    },
    # 68
    {
        "q": "What holiday albums did Garth and Kat repeatedly claim to be promoting on Weekend Update?",
        "correct": "Albums for every minor holiday like Flag Day, Arbor Day, and Halloween",
        "distractors": ["A compilation of Renaissance lute melodies", "A series of aggressive heavy metal covers", "Children's lullabies for farm animals"],
        "d": 2
    },
    # 69
    {
        "q": "What was the signature catchphrase of Tim Meadows' smooth-talking radio romantic Leon Phelps?",
        "correct": "Ooh, it's a lady!",
        "distractors": ["Hey there, baby girl!", "Look out now, sweet thing!", "Welcome to the love zone!"],
        "d": 1
    },
    # 70
    {
        "q": "What beverage did Leon Phelps (The Ladies Man) obsessively drink and recommend as an aphrodisiac?",
        "correct": "Courvoisier cognac",
        "distractors": ["Hennessy", "Martell", "Remy Martin"],
        "d": 2
    },
    # 71
    {
        "q": "What was the title of the 2000 feature film starring Tim Meadows as Leon Phelps?",
        "correct": "The Ladies Man",
        "distractors": ["Smooth Operator", "Courvoisier Nights", "Radio Romance"],
        "d": 2
    },
    # 72
    {
        "q": "In a 2017 episode, which cast member played a passionate French snail on Weekend Update speaking about climate change?",
        "correct": "Kate McKinnon",
        "distractors": ["Cecily Strong", "Melissa Villaseñor", "Aidy Bryant"],
        "d": 3
    },
    # 73
    {
        "q": "What was the name of the recurring Weekend Update character played by Marcello Hernandez who gave enthusiastic reports on Latino culture and sports?",
        "correct": "Marcello as himself discussing his Dominican-Cuban heritage",
        "distractors": ["Ramon the Pitcher", "Carlos the Striker", "Papi the Boxer"],
        "d": 2
    },
    # 74
    {
        "q": "What signature topic did stand-up comedian Michael Longfellow discuss with deadpan cynicism in his debut Season 48 Weekend Update appearance?",
        "correct": "His parents' divorce and his multiple stepdads",
        "distractors": ["Cryptocurrency investments", "His fear of flying", "Living in a studio apartment in Queens"],
        "d": 2
    },
    # 75
    {
        "q": "What was the title of the satirical segment created during the 2008 election where Amy Poehler played a frantic political operative?",
        "correct": "Women's News with Amy Poehler",
        "distractors": ["The Gender Gap", "Feminist Daily", "Suffrage Today"],
        "d": 3
    },
    # 76
    {
        "q": "What recurring correspondent character played by Bill Murray in the late 1970s was an abrasive, chain-smoking theater critic?",
        "correct": "Honker the Bum / Movie Critic",
        "distractors": ["Rex Reed Jr.", "Cinema Pete", "Broadway Billy"],
        "d": 3
    },
    # 77
    {
        "q": "What song did Bill Murray famously perform to open his Oscar predictions on Weekend Update in 1979?",
        "correct": "The love theme from 'A Star Is Born' and various Oscar nominated ballads",
        "distractors": ["Over the Rainbow", "Singin' in the Rain", "Moon River"],
        "d": 3
    },
    # 78
    {
        "q": "Which anchor hosted Weekend Update alongside Jane Curtin from 1978 to 1979 before departing for a legendary film career?",
        "correct": "Bill Murray",
        "distractors": ["Dan Aykroyd", "John Belushi", "Garrett Morris"],
        "d": 2
    },
    # 79
    {
        "q": "What prop was famously situated in front of Chevy Chase at the original Weekend Update anchor desk?",
        "correct": "A vintage rotary telephone and a stack of papers",
        "distractors": ["A vintage typewriter and a glass of scotch", "A ticker-tape machine and a desk lamp", "A brass microphone and a megaphone"],
        "d": 2
    },
    # 80
    {
        "q": "What did Chevy Chase do whenever the phone rang at the anchor desk during the broadcast?",
        "correct": "Picked it up and had a private, inappropriate conversation with a lover",
        "distractors": ["Answered it in fake foreign accents", "Threw the receiver across the room", "Pretended it was a call from the President"],
        "d": 2
    },
    # 81
    {
        "q": "Which anchor team helmed Weekend Update during the 2000 presidential election recount saga ('Bush v. Gore')?",
        "correct": "Tina Fey and Jimmy Fallon",
        "distractors": ["Colin Quinn", "Norm Macdonald", "Seth Meyers and Amy Poehler"],
        "d": 2
    },
    # 82
    {
        "q": "What was the satirical recurring segment by Tina Fey and Jimmy Fallon where they judged news figures with thumbs-up or thumbs-down?",
        "correct": "Update Good / Update Bad",
        "distractors": ["The Hot List", "Pass or Fail", "Hot or Not"],
        "d": 3
    },
    # 83
    {
        "q": "What catchphrase did Tina Fey use to dismiss bizarre cosmetic surgeries or absurd lifestyle trends on Update?",
        "correct": "Bitch, please!",
        "distractors": ["Girl, no!", "Shut it down!", "Take a hike!"],
        "d": 2
    },
    # 84
    {
        "q": "What was the name of the recurring Weekend Update segment where Colin Jost and Michael Che hosted a mock awards ceremony for the year's worst stories?",
        "correct": "The Year in Review / Joke Swap Specials",
        "distractors": ["The Golden Turkeys", "The Update Trophies", "The 8H Honors"],
        "d": 3
    },
    # 85
    {
        "q": "What character did Kenan Thompson play who was a reclusive Appalachian man giving absurd mountain advice on Update?",
        "correct": "Dink Cook",
        "distractors": ["Mountain Mike", "Cousin Zeke", "Silas Vance"],
        "d": 3
    },
    # 86
    {
        "q": "Which former SNL cast member was fired from Weekend Update in 1980 after one season behind the desk?",
        "correct": "Charles Rocket",
        "distractors": ["Joe Piscopo", "Eddie Murphy", "Gilbert Gottfried"],
        "d": 3
    },
    # 87
    {
        "q": "Which comedian made his SNL debut in Season 40 as a featured player and immediately appeared on Weekend Update doing stand-up about his mom?",
        "correct": "Pete Davidson",
        "distractors": ["Leslie Jones", "Michael Che", "Chris Redd"],
        "d": 2
    },
    # 88
    {
        "q": "What was the primary comedy style of Pete Davidson's frequent Weekend Update desk appearances?",
        "correct": "Autobiographical stand-up comedy discussing his personal struggles and health",
        "distractors": ["Character sketches with prosthetics", "Musical parodies with an acoustic ukulele", "Impression medleys of movie stars"],
        "d": 1
    },
    # 89
    {
        "q": "What was the name of the eccentric, fast-talking character played by Fred Armisen who was a Native American comedian appearing on Weekend Update?",
        "correct": "Billy Smith",
        "distractors": ["Chief Running Joke", "Tommy Redfeather", "Eagle Dave"],
        "d": 3
    },
    # 90
    {
        "q": "In 2011, what character did Bill Hader play on Weekend Update who was an Italian talk show host obsessed with scandalous gossip?",
        "correct": "Vinny Vedecci",
        "distractors": ["Tony Soprano Jr.", "Enzo Ferrari", "Marco Rossi"],
        "d": 2
    },
    # 91
    {
        "q": "What language did Vinny Vedecci speak while smoking a cigarette and interrogating American movie stars on his talk show?",
        "correct": "Rapid-fire gibberish Italian mixed with occasional English words",
        "distractors": ["Flawless British English", "Broken Spanish", "French street slang"],
        "d": 2
    },
    # 92
    {
        "q": "In a 2014 episode, what did Michael Che reveal as his mother's reaction when he was named Weekend Update co-anchor?",
        "correct": "She asked why he couldn't get a job like Colin Jost",
        "distractors": ["She hung up the phone thinking it was a prank", "She asked if he would meet the President", "She asked for free tickets to the Super Bowl"],
        "d": 3
    },
    # 93
    {
        "q": "What was the title of the primetime Thursday evening special series of Weekend Update produced during several election years?",
        "correct": "Saturday Night Live Weekend Update Thursday",
        "distractors": ["Midweek Update Live", "Update Primetime Edition", "Thursday Night Update"],
        "d": 2
    },
    # 94
    {
        "q": "In what year did 'Weekend Update Thursday' make its initial debut during the fall presidential campaign?",
        "correct": "2008",
        "distractors": ["2000", "2004", "2012"],
        "d": 3
    },
    # 95
    {
        "q": "What character did Will Ferrell play on Weekend Update who was the lead singer of an aggressive rock band giving financial advice?",
        "correct": "David Bennett",
        "distractors": ["Axl Vance", "Slash Roberts", "Bret Michaels Jr."],
        "d": 3
    },
    # 96
    {
        "q": "What catchphrase did Dan Aykroyd deliver at the start of his 'Point/Counterpoint' editorial rejoinders?",
        "correct": "Jane, you ignorant slut!",
        "distractors": ["Jane, you simple creature!", "Jane, you naive toddler!", "Jane, you empty vessel!"],
        "d": 1
    },
    # 97
    {
        "q": "Which anchor holds the record for hosting the most Weekend Update episodes as a solo anchor without a co-host in the modern era?",
        "correct": "Seth Meyers",
        "distractors": ["Dennis Miller", "Norm Macdonald", "Kevin Nealon"],
        "d": 2
    },
    # 98
    {
        "q": "What was the name of the recurring character played by Aidy Bryant on Weekend Update who was a hopelessly inept travel expert?",
        "correct": "Carrie Krum",
        "distractors": ["Samantha Brown Jr.", "Wanderlust Wendy", "Jetset Judy"],
        "d": 3
    },
    # 99
    {
        "q": "What was the comedic quirk of 7th-grade travel journalist Carrie Krum on Weekend Update?",
        "correct": "She reviewed family vacations from the perspective of an excited middle schooler (hotel pools, snacks)",
        "distractors": ["She only reviewed luxury five-star resorts in Monaco", "She had never left her bedroom in Des Moines", "She lost her luggage in every city she visited"],
        "d": 2
    },
    # 100
    {
        "q": "What is the longest continuous sketch/segment franchise in Saturday Night Live history, having appeared in some form in every single season?",
        "correct": "Weekend Update",
        "distractors": ["The Cold Open", "Celebrity Jeopardy!", "Church Chat"],
        "d": 1
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "staging", "snl_batch4.json")
    build_batch(questions, out, batch_num=4)
