#!/usr/bin/env python3
"""
Generate SNL Batch 2: 90s & 2000s Golden Eras Catchphrases, Sketches & Characters (1990-2009)
100 questions: exactly 30 d1, 40 d2, 30 d3.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from builder import build_batch

questions = [
    # 1
    {
        "q": "Where did Chris Farley's iconic motivational speaker character Matt Foley constantly warn kids he was living?",
        "correct": "In a van down by the river",
        "distractors": ["In a basement under the bridge", "In an abandoned trailer in the swamp", "In a cardboard box behind a warehouse"],
        "d": 1
    },
    # 2
    {
        "q": "What piece of living room furniture did Chris Farley's Matt Foley famously crush and shatter during his debut sketch in 1993?",
        "correct": "The coffee table",
        "distractors": ["The television set", "The recliner chair", "The coat rack"],
        "d": 1
    },
    # 3
    {
        "q": "Which guest host played the teenage daughter alongside David Spade in the original 1993 Matt Foley sketch?",
        "correct": "Christina Applegate",
        "distractors": ["Drew Barrymore", "Sarah Michelle Gellar", "Winona Ryder"],
        "d": 2
    },
    # 4
    {
        "q": "What physical routine did Matt Foley perform repeatedly while shouting his motivational advice?",
        "correct": "Hitching up his trousers and tucking in his shirt",
        "distractors": ["Banging a clipboard against his forehead", "Doing frantic jumping jacks", "Drinking straight from a coffee pot"],
        "d": 2
    },
    # 5
    {
        "q": "What daily affirmation mantra did Al Franken's character Stuart Smalley recite into a mirror?",
        "correct": "I'm good enough, I'm smart enough, and doggone it, people like me!",
        "distractors": ["I'm strong, I'm capable, and the universe loves me unconditionally!", "Every day in every way I am getting better and better!", "I am a beacon of light, love, and emotional maturity!"],
        "d": 1
    },
    # 6
    {
        "q": "In Mike Myers' recurring 'Coffee Talk' sketch, what was host Linda Richman's signature catchphrase when she became overwhelmed with emotion?",
        "correct": "I'm all verklempt! Talk amongst yourselves.",
        "distractors": ["I'm fainting away! Give me a minute.", "I'm lost for words! Have a pastry.", "My heart is fluttering! Take a sip."],
        "d": 1
    },
    # 7
    {
        "q": "Which legendary singer made a surprise guest appearance on 'Coffee Talk' alongside Mike Myers, Madonna, and Roseanne Barr in 1992?",
        "correct": "Barbra Streisand",
        "distractors": ["Bette Midler", "Liza Minnelli", "Cher"],
        "d": 2
    },
    # 8
    {
        "q": "In 'Coffee Talk', what did Linda Richman famously declare about the Holy Roman Empire?",
        "correct": "It was neither holy, nor Roman, nor an empire",
        "distractors": ["It was too grand, too expensive, and ended too soon", "It had the best bread, the worst wine, and too many popes", "It was divided by mountains, conquered by barbarians, and ruined by taxes"],
        "d": 2
    },
    # 9
    {
        "q": "Who portrayed Alex Trebek as the long-suffering host of 'Celebrity Jeopardy!' on SNL?",
        "correct": "Will Ferrell",
        "distractors": ["Phil Hartman", "Darrell Hammond", "Norm Macdonald"],
        "d": 1
    },
    # 10
    {
        "q": "Which belligerent contestant, played by Darrell Hammond, perpetually insulted Will Ferrell's Alex Trebek on 'Celebrity Jeopardy!'?",
        "correct": "Sean Connery",
        "distractors": ["Burt Reynolds", "Nicolas Cage", "French Stewart"],
        "d": 1
    },
    # 11
    {
        "q": "What pseudonym did Norm Macdonald's Burt Reynolds demand Alex Trebek call him on 'Celebrity Jeopardy!' while wearing an oversized yellow foam cowboy hat?",
        "correct": "Turd Ferguson",
        "distractors": ["Rusty Shackleford", "Burt the Great", "Big Tex Reynolds"],
        "d": 1
    },
    # 12
    {
        "q": "On 'Celebrity Jeopardy!', how did Darrell Hammond's Sean Connery consistently misread the category 'Therapists'?",
        "correct": "The Rapists",
        "distractors": ["The Pistachio", "The Rip-offs", "The Rats"],
        "d": 2
    },
    # 13
    {
        "q": "How did Sean Connery misread the category 'An Album Cover' on 'Celebrity Jeopardy!'?",
        "correct": "Anal Bum Cover",
        "distractors": ["An Alba Clover", "And All Bum Cover", "Animals Undercover"],
        "d": 2
    },
    # 14
    {
        "q": "In the famous 2000 sketch 'More Cowbell', which rock band's recording session for '(Don't Fear) The Reaper' was being depicted?",
        "correct": "Blue Öyster Cult",
        "distractors": ["Black Sabbath", "Deep Purple", "Lynyrd Skynyrd"],
        "d": 1
    },
    # 15
    {
        "q": "What was the name of the music producer portrayed by Christopher Walken who insisted on having 'More Cowbell'?",
        "correct": "The Bruce Dickinson",
        "distractors": ["Gene Frenkle", "Mick Jones", "Bob Rock"],
        "d": 1
    },
    # 16
    {
        "q": "What is the full famous quote delivered by Christopher Walken in the 'More Cowbell' sketch?",
        "correct": "I got a fever, and the only prescription is more cowbell!",
        "distractors": ["I need more rhythm, and the only cure is that sweet cowbell!", "Turn up the treble, because the cowbell needs to breathe!", "There's an itch in my soul, and that cowbell just scratched it!"],
        "d": 1
    },
    # 17
    {
        "q": "What was the name of the fictional cowbell player in Blue Öyster Cult played by Will Ferrell?",
        "correct": "Gene Frenkle",
        "distractors": ["Eric Bloom", "Buck Dharma", "Joe Bouchard"],
        "d": 2
    },
    # 18
    {
        "q": "What garment was Will Ferrell's Gene Frenkle wearing in 'More Cowbell' that kept riding up to expose his midriff?",
        "correct": "A tight blue tight-fitting short shirt",
        "distractors": ["A fringed leather vest", "An unbuttoned silk shirt", "A ripped flannel cut-off"],
        "d": 2
    },
    # 19
    {
        "q": "Which cast member infamously broke character and could not stop laughing while playing acoustic guitar in 'More Cowbell'?",
        "correct": "Jimmy Fallon",
        "distractors": ["Horatio Sanz", "Chris Parnell", "Chris Kattan"],
        "d": 2
    },
    # 20
    {
        "q": "In the 'Delicious Dish' holiday sketch, what seasonal food item did guest baker Pete Schweddy (Alec Baldwin) bring to Margaret Jo and Terry?",
        "correct": "Schweddy Balls",
        "distractors": ["Schweddy Pies", "Schweddy Buns", "Schweddy Logs"],
        "d": 1
    },
    # 21
    {
        "q": "Which two cast members played public radio hosts Margaret Jo McCullen and Terry Rialto on NPR's 'The Delicious Dish'?",
        "correct": "Ana Gasteyer and Molly Shannon",
        "distractors": ["Cheri Oteri and Rachel Dratch", "Tina Fey and Amy Poehler", "Kristen Wiig and Maya Rudolph"],
        "d": 2
    },
    # 22
    {
        "q": "What was the recurring character played by Rachel Dratch whose depressing conversational interjections ruined fun social gatherings?",
        "correct": "Debbie Downer",
        "distractors": ["Sad Sally", "Gloomy Gladys", "Negative Nancy"],
        "d": 1
    },
    # 23
    {
        "q": "In the original 2004 Debbie Downer sketch where the entire cast broke character laughing, where were the characters vacationing?",
        "correct": "Walt Disney World",
        "distractors": ["Las Vegas", "A ski resort in Aspen", "A Hawaiian luau"],
        "d": 2
    },
    # 24
    {
        "q": "What sound effect played every time Debbie Downer delivered a devastating piece of trivia?",
        "correct": "A muted sad trombone 'wah-wah'",
        "distractors": ["A screeching violin sting", "A funeral bell toll", "A thunderstorm strike"],
        "d": 1
    },
    # 25
    {
        "q": "Which guest host starred in the famously derailed Walt Disney World Debbie Downer sketch alongside Rachel Dratch?",
        "correct": "Lindsay Lohan",
        "distractors": ["Cameron Diaz", "Drew Barrymore", "Hilary Duff"],
        "d": 2
    },
    # 26
    {
        "q": "What was the name of Will Forte's parody action-hero character whose bomb-defusal attempts always failed due to personal bickering?",
        "correct": "MacGruber",
        "distractors": ["McBain", "Commander Danger", "Dirk Danger"],
        "d": 1
    },
    # 27
    {
        "q": "Which 1980s television adventure series did 'MacGruber' spoof?",
        "correct": "MacGyver",
        "distractors": ["The A-Team", "Miami Vice", "Knight Rider"],
        "d": 1
    },
    # 28
    {
        "q": "Which two cast members regularly co-starred with Will Forte in the MacGruber sketches as his sidekicks Vicki and Piper?",
        "correct": "Kristen Wiig and various guest hosts",
        "distractors": ["Amy Poehler and Seth Meyers", "Maya Rudolph and Fred Armisen", "Abby Elliott and Andy Samberg"],
        "d": 2
    },
    # 29
    {
        "q": "What song played as the theme song for the brothers Steve and Doug Butabi, the Roxbury Guys?",
        "correct": "'What Is Love' by Haddaway",
        "distractors": ["'Rhythm Is a Dancer' by Snap!", "'Pump Up the Jam' by Technotronic", "'Scatman' by Scatman John"],
        "d": 1
    },
    # 30
    {
        "q": "Which guest host joined Will Ferrell and Chris Kattan as their third head-bobbing brother in a classic Roxbury Guys sketch in 1996?",
        "correct": "Jim Carrey",
        "distractors": ["Tom Hanks", "Sylvester Stallone", "Alec Baldwin"],
        "d": 1
    },
    # 31
    {
        "q": "What odd habit did Catholic schoolgirl Mary Katherine Gallagher (Molly Shannon) have when she became nervous?",
        "correct": "Putting her hands under her armpits and smelling her fingers",
        "distractors": ["Twisting her earlobes until they turned red", "Biting her fingernails into jagged shapes", "Tapping her heels three times while reciting Latin"],
        "d": 1
    },
    # 32
    {
        "q": "What exclamation did Mary Katherine Gallagher shout while thrusting her arms into the air and falling into folding chairs?",
        "correct": "Superstar!",
        "distractors": ["Fabulous!", "Sensational!", "Victory!"],
        "d": 1
    },
    # 33
    {
        "q": "What was the title of the 1999 feature film based on Molly Shannon's Mary Katherine Gallagher character?",
        "correct": "Superstar",
        "distractors": ["Catholic Girl", "High School Glory", "Armpit Fever"],
        "d": 2
    },
    # 34
    {
        "q": "What was the mystery surrounding Julia Sweeney's recurring character 'Pat'?",
        "correct": "Whether Pat was male or female",
        "distractors": ["Pat's actual legal name", "Pat's country of citizenship", "Pat's actual profession"],
        "d": 1
    },
    # 35
    {
        "q": "What was the name of Pat's equally androgynous romantic partner, played by Charles Rocket in 1991 and later Harvey Keitel?",
        "correct": "Chris",
        "distractors": ["Terry", "Sam", "Alex"],
        "d": 2
    },
    # 36
    {
        "q": "What was the catchphrase of Phil Hartman's recurring character Keyrock, a prehistoric hominid who became an attorney?",
        "correct": "I'm just a caveman, your world frightens and confuses me",
        "distractors": ["Me make law, me win trial", "From stone age to courtroom, justice prevails", "I don't know much about modern times, but I know tort law"],
        "d": 1
    },
    # 37
    {
        "q": "What luxury car did Keyrock the Unfrozen Caveman Lawyer proudly mention leasing despite claiming to not understand technology?",
        "correct": "BMW",
        "distractors": ["Mercedes-Benz", "Porsche", "Lexus"],
        "d": 3
    },
    # 38
    {
        "q": "What was the name of Christopher Walken's recurring character who lounged in a smoking jacket and tried to seduce reluctant women with 'champagna'?",
        "correct": "The Continental",
        "distractors": ["The Casanova", "The Baron", "The Aristocrat"],
        "d": 1
    },
    # 39
    {
        "q": "How was 'The Continental' sketch visually framed to immerse the viewer in the woman's perspective?",
        "correct": "Shot entirely through a first-person point-of-view camera",
        "distractors": ["Shot in stark black-and-white 16mm film", "Shot through a fish-eye door peephole lens", "Shot in a continuous single static take with split screens"],
        "d": 2
    },
    # 40
    {
        "q": "Which cast member portrayed the exotic, hyper-athletic male stripper Mango, whom men found inexplicably irresistible?",
        "correct": "Chris Kattan",
        "distractors": ["Cheri Oteri", "Jimmy Fallon", "Horatio Sanz"],
        "d": 1
    },
    # 41
    {
        "q": "What dramatic catchphrase did Mango utter whenever admirers professed their undying love for him?",
        "correct": "You cannot have the Mango!",
        "distractors": ["Mango is a bird who flies free!", "Do not touch the fruit!", "Mango belongs to no man!"],
        "d": 1
    },
    # 42
    {
        "q": "What was the name of the feral, suspender-wearing ape-man portrayed by Chris Kattan who bit into apples and spat the pieces?",
        "correct": "Mr. Peepers",
        "distractors": ["Monkey Boy", "Baboon Bob", "Chimp Charlie"],
        "d": 2
    },
    # 43
    {
        "q": "What retail department store cashier did Kristen Wiig portray with a red vest, feathered hair, and an overactive cash register finger?",
        "correct": "The Target Lady",
        "distractors": ["The Walmart Greeter", "The Kmart Shopper", "The Sears Consultant"],
        "d": 1
    },
    # 44
    {
        "q": "What was the name of the Spartan cheerleading duo played by Will Ferrell and Cheri Oteri?",
        "correct": "Craig and Arianna",
        "distractors": ["Brad and Courtney", "Chad and Tiffany", "Todd and Brittany"],
        "d": 2
    },
    # 45
    {
        "q": "Why were Craig and Arianna not on the official East Chessington High School varsity cheerleading squad?",
        "correct": "They were cut at cheer camp tryouts",
        "distractors": ["They were suspended for bad grades", "They graduated five years earlier", "They refused to wear the official colors"],
        "d": 2
    },
    # 46
    {
        "q": "What was the title of the seminal 2005 SNL Digital Short starring Andy Samberg and Chris Parnell that revolutionized internet viral video?",
        "correct": "Lazy Sunday",
        "distractors": ["Chronicles of Cupcake", "Saturday Night Fever", "Sunday Afternoon"],
        "d": 1
    },
    # 47
    {
        "q": "In the rap video 'Lazy Sunday', what fantasy film were Andy Samberg and Chris Parnell desperately trying to watch at the movie theater?",
        "correct": "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe",
        "distractors": ["The Lord of the Rings: The Fellowship of the Ring", "Harry Potter and the Goblet of Fire", "Star Wars: Episode III – Revenge of the Sith"],
        "d": 1
    },
    # 48
    {
        "q": "What New York bakery's cupcakes did Samberg and Parnell devour in 'Lazy Sunday'?",
        "correct": "Magnolia Bakery",
        "distractors": ["Levain Bakery", "Georgetown Cupcake", "Momofuku Milk Bar"],
        "d": 2
    },
    # 49
    {
        "q": "Which pop superstar collaborated with Andy Samberg on the 2006 holiday Digital Short 'Dick in a Box'?",
        "correct": "Justin Timberlake",
        "distractors": ["Justin Bieber", "Bruno Mars", "Adam Levine"],
        "d": 1
    },
    # 50
    {
        "q": "What Primetime Emmy Award did 'Dick in a Box' win in 2007, marking a milestone for SNL digital comedy?",
        "correct": "Outstanding Original Music and Lyrics",
        "distractors": ["Outstanding Short-Form Comedy", "Outstanding Sound Editing", "Outstanding Variety Special Writing"],
        "d": 2
    },
    # 51
    {
        "q": "Who directed the vast majority of The Lonely Island's iconic SNL Digital Shorts, including 'Lazy Sunday' and 'Dick in a Box'?",
        "correct": "Akiva Schaffer",
        "distractors": ["Jorma Taccone", "Adam McKay", "Paul Feig"],
        "d": 2
    },
    # 52
    {
        "q": "What dramatic indie pop song by Imogen Heap was parodied in the 2007 SNL Digital Short 'The Shooting' (also known as 'Dear Sister')?",
        "correct": "Hide and Seek",
        "distractors": ["Goodnight and Go", "Speeding Cars", "First Train Home"],
        "d": 2
    },
    # 53
    {
        "q": "Which teen drama television series finale was directly spoofed by 'The Shooting' (Dear Sister)?",
        "correct": "The O.C.",
        "distractors": ["One Tree Hill", "Dawson's Creek", "Gossip Girl"],
        "d": 2
    },
    # 54
    {
        "q": "Which auto-tune hip-hop artist guest starred with Andy Samberg on the Grammy-nominated 2009 Digital Short 'I'm on a Boat'?",
        "correct": "T-Pain",
        "distractors": ["Lil Wayne", "Kanye West", "Snoop Dogg"],
        "d": 1
    },
    # 55
    {
        "q": "What actresses played the mothers in Justin Timberlake and Andy Samberg's Mother's Day song 'Motherlover'?",
        "correct": "Susan Sarandon and Patricia Clarkson",
        "distractors": ["Glenn Close and Sigourney Weaver", "Meryl Streep and Diane Keaton", "Sally Field and Blythe Danner"],
        "d": 3
    },
    # 56
    {
        "q": "What was the name of Tracy Morgan's eccentric nature show host who was terrified of ordinary animals and obsessed with conspiracy theories?",
        "correct": "Brian Fellow",
        "distractors": ["Safari Steve", "Dr. Wildlife", "Professor Paws"],
        "d": 1
    },
    # 57
    {
        "q": "What animal did Brian Fellow accuse of being a liar and trying to steal his identity?",
        "correct": "A parrot",
        "distractors": ["A goat", "A beaver", "A ferret"],
        "d": 2
    },
    # 58
    {
        "q": "What catchphrase did Tracy Morgan repeatedly deliver on 'Brian Fellow's Safari Planet'?",
        "correct": "I'm Brian Fellow!",
        "distractors": ["Look at that wild beast!", "Animals be crazy!", "Nature is scary!"],
        "d": 2
    },
    # 59
    {
        "q": "What middle school music teacher duo did Will Ferrell and Ana Gasteyer play who performed overly earnest pop song medleys at school assemblies?",
        "correct": "The Culps (Bob and Marty Culp)",
        "distractors": ["The Meltons (Dan and Carol)", "The Millers (Ron and Nancy)", "The Harmons (Phil and Linda)"],
        "d": 2
    },
    # 60
    {
        "q": "What medical condition did Will Ferrell's character Jacob Silj suffer from on Weekend Update?",
        "correct": "Voice Modulation Disorder",
        "distractors": ["Involuntary Pitch Syndrome", "Acoustic Nerve Spasm", "Laryngeal Echo Phobia"],
        "d": 2
    },
    # 61
    {
        "q": "Which real U.S. Attorney General made a cameo appearance to dance alongside Will Ferrell during the final 'Janet Reno's Dance Party' sketch in 2001?",
        "correct": "Janet Reno",
        "distractors": ["Madeleine Albright", "Donna Shalala", "Janet Napolitano"],
        "d": 2
    },
    # 62
    {
        "q": "What dismissal catchphrase did David Spade make famous as flight attendant Dick in the 'Total Bastard Airlines' sketches?",
        "correct": "Buh-bye!",
        "distractors": ["See ya!", "Move along!", "Flight cleared!"],
        "d": 1
    },
    # 63
    {
        "q": "What was the catchphrase of Adam Sandler's Opera Man on Weekend Update?",
        "correct": "Opera Man bye-bye!",
        "distractors": ["Aria complete!", "Encore no more!", "Bravissimo exit!"],
        "d": 2
    },
    # 64
    {
        "q": "What song did Adam Sandler perform on Weekend Update in 1994 listing Jewish celebrities to cheer up kids feeling left out during Christmas?",
        "correct": "The Chanukah Song",
        "distractors": ["The Menorah Melody", "Eight Crazy Nights", "Festival of Lights Anthem"],
        "d": 1
    },
    # 65
    {
        "q": "What Thanksgiving tune did Adam Sandler debut on Weekend Update in 1992 declaring 'Turkey for me, turkey for you'?",
        "correct": "The Thanksgiving Song",
        "distractors": ["The Cranberry Rhapsody", "Gobble Gobble Hymn", "Pilgrim Boogie"],
        "d": 1
    },
    # 66
    {
        "q": "What was the name of the snooty retail clothing boutique run by Jimmy Fallon and Will Ferrell where they insulted shoppers?",
        "correct": "Jeffrey's",
        "distractors": ["Maurice's", "Armand's", "Pierre's"],
        "d": 2
    },
    # 67
    {
        "q": "What dismissive phrase did Jimmy Fallon's arrogant computer tech Nick Burns snap at frustrated office workers before taking their keyboards?",
        "correct": "MOVE!",
        "distractors": ["OUT!", "SHOO!", "STEP ASIDE!"],
        "d": 1
    },
    # 68
    {
        "q": "In the 'Barry Gibb Talk Show' recurring sketch, which Bee Gees member was portrayed by Justin Timberlake alongside Jimmy Fallon's Barry?",
        "correct": "Robin Gibb",
        "distractors": ["Maurice Gibb", "Andy Gibb", "Hugh Gibb"],
        "d": 2
    },
    # 69
    {
        "q": "What was Robin Gibb's primary role on 'The Barry Gibb Talk Show'?",
        "correct": "Sitting silently and occasionally singing high-pitched harmonies",
        "distractors": ["Reading legal disclaimers from notecards", "Playing keyboard solos on an electric synth", "Translating Barry's insults into French"],
        "d": 2
    },
    # 70
    {
        "q": "What was the name of Kenan Thompson's recurring BET talk show host on 'What Up with That?'",
        "correct": "Diondre Cole",
        "distractors": ["Marcus King", "Jerome Sparks", "Trey Campbell"],
        "d": 1
    },
    # 71
    {
        "q": "Which real-life Fleetwood Mac musician was played by Bill Hader on 'What Up with That?', constantly sitting as a guest who ran out of time?",
        "correct": "Lindsey Buckingham",
        "distractors": ["Mick Fleetwood", "Stevie Nicks", "John McVie"],
        "d": 1
    },
    # 72
    {
        "q": "What did Jason Sudeikis do in the background of every 'What Up with That?' sketch as the character Vance?",
        "correct": "Danced vigorously in a red-and-white tracksuit with a high flat-top wig",
        "distractors": ["Ate giant sandwiches silently behind the couch", "Played a small cowbell off-beat in a tuxedo", "Pretended to sleep on a beanbag chair"],
        "d": 2
    },
    # 73
    {
        "q": "What was the catchphrase of Kristen Wiig's mischievous, wide-smiling schoolgirl character Gilly after causing mayhem?",
        "correct": "Sorry!",
        "distractors": ["Oopsie!", "Not me!", "Did I do that?"],
        "d": 1
    },
    # 74
    {
        "q": "What was the name of the high school teacher played by Will Forte who constantly interrogated Gilly about classroom disasters?",
        "correct": "Mr. Dingiecary",
        "distractors": ["Mr. Henderson", "Mr. Harrison", "Mr. Bradley"],
        "d": 3
    },
    # 75
    {
        "q": "What was the name of the morning talk show spoof hosted by Amy Poehler and Maya Rudolph as loudmouthed suburban women Betty and Jodi?",
        "correct": "Bronx Beat",
        "distractors": ["Queens Morning", "Brooklyn Chat", "Staten Island Brew"],
        "d": 2
    },
    # 76
    {
        "q": "What was the signature catchphrase of the clueless, gum-chewing couple 'The Two A-Holes' played by Jason Sudeikis and Kristen Wiig?",
        "correct": "Babe, look at him...",
        "distractors": ["Whatever, who cares!", "Like, totally not interested!", "Get over yourself, dude!"],
        "d": 3
    },
    # 77
    {
        "q": "In the 1996 sketch 'The Culps', which hit hip-hop song did Bob and Marty Culp famously arrange into an upbeat acoustic medley for high school students?",
        "correct": "Poison / Gin and Juice / Waterfalls",
        "distractors": ["Rapper's Delight", "California Love", "Lose Yourself"],
        "d": 3
    },
    # 78
    {
        "q": "Which musical artist did Andy Samberg serenade with the hilarious, whisper-quiet character 'Shy Ronnie' in a 2009 Digital Short?",
        "correct": "Rihanna",
        "distractors": ["Beyoncé", "Katy Perry", "Lady Gaga"],
        "d": 2
    },
    # 79
    {
        "q": "What was the name of the recurring 1990s sketch starring Adam Sandler, Chris Farley, and David Spade working at an apparel store counter?",
        "correct": "Gap Girls",
        "distractors": ["J. Crew Chics", "Banana Republic Belles", "Mall Divas"],
        "d": 2
    },
    # 80
    {
        "q": "What line did Chris Farley scream while shoving French fries into his mouth as Cindy in the 'Gap Girls' sketch?",
        "correct": "Lay off me, I'm starving!",
        "distractors": ["Don't you judge my body!", "I need my carbohydrates!", "I skipped lunch for this skirt!"],
        "d": 1
    },
    # 81
    {
        "q": "What superhero duo in Robert Smigel's animated 'Saturday TV Funhouse' flew around in a car that drew constant suspicion from onlookers?",
        "correct": "The Ambiguously Gay Duo",
        "distractors": ["The Dynamic Duo", "The Super Pals", "The Metro Crusaders"],
        "d": 1
    },
    # 82
    {
        "q": "Which two famous comedy stars provided the original voices of superheroes Ace and Gary in 'The Ambiguously Gay Duo'?",
        "correct": "Stephen Colbert and Steve Carell",
        "distractors": ["Jon Stewart and Stephen Colbert", "Will Ferrell and Chris Kattan", "David Spade and Chris Farley"],
        "d": 2
    },
    # 83
    {
        "q": "In a 2008 SNL sketch that achieved viral fame, Tina Fey played Sarah Palin beside Amy Poehler's Hillary Clinton, famously uttering what line penned by head writer Seth Meyers?",
        "correct": "I can see Russia from my house!",
        "distractors": ["Moose hunting is my cardio!", "You betcha, hockey moms rock!", "Drill baby drill, right here in 30 Rock!"],
        "d": 1
    },
    # 84
    {
        "q": "Who portrayed vice presidential candidate Joe Biden in the 2008 vice presidential debate parody opposite Tina Fey's Sarah Palin?",
        "correct": "Jason Sudeikis",
        "distractors": ["Darrell Hammond", "Will Forte", "Bill Hader"],
        "d": 2
    },
    # 85
    {
        "q": "What product did Will Ferrell pitch as Dale O'Sample in a late-1990s commercial parody featuring tiny flags?",
        "correct": "Old Glory Insurance (protecting against robot attacks)",
        "distractors": ["Patriot Life Policies", "Heritage Home Guard", "Liberty Senior Care"],
        "d": 2
    },
    # 86
    {
        "q": "According to the famous 'Old Glory Insurance' parody, what did robots eat for fuel that endangered seniors?",
        "correct": "Old people's medicine for energy",
        "distractors": ["Social security checks", "Metamucil", "Prune juice"],
        "d": 3
    },
    # 87
    {
        "q": "What was the name of the recurring 1990s talk show host played by Chris Rock that was broadcast on public access Channel 43 at 2:30 AM?",
        "correct": "The Dark Side with Nat X",
        "distractors": ["Black History Live with Marcus", "Late Night with Jamal", "Urban Truth with Malcolm"],
        "d": 2
    },
    # 88
    {
        "q": "Who played Sandman, the afro-wearing sidekick on 'The Dark Side with Nat X' who blew a whistle and danced wildly?",
        "correct": "David Spade",
        "distractors": ["Chris Farley", "Adam Sandler", "Rob Schneider"],
        "d": 3
    },
    # 89
    {
        "q": "What was the name of the hyper-enthusiastic, sweater-clad copy machine guy played by Rob Schneider?",
        "correct": "Richard Laymer (The Richmeister)",
        "distractors": ["Carl the Copier", "Kenny Xerox", "Bob the Paper Pusher"],
        "d": 2
    },
    # 90
    {
        "q": "What verbal pattern did Rob Schneider's Richmeister use when colleagues approached the office photocopier?",
        "correct": "Making copies! The Steve-o! Steve-a-rino!",
        "distractors": ["Print it up, paper boy, paper man!", "Paper jam, jammin' in the name of love!", "Xerox hero, copy machine master!"],
        "d": 1
    },
    # 91
    {
        "q": "What was the title of the recurring sketch starring Cheri Oteri and Will Ferrell as an aggressively dysfunctional married couple fighting at office parties?",
        "correct": "The Lewises (Marty and Bobbi Mohan-Culp) / The Bickersons",
        "distractors": ["The Millers", "The Hendersons", "The Bakers"],
        "d": 3
    },
    # 92
    {
        "q": "In the recurring 'Jarret's Room' web-show sketches from the early 2000s, who played Jarret alongside Seth Meyers' character Gobi?",
        "correct": "Jimmy Fallon",
        "distractors": ["Horatio Sanz", "Andy Samberg", "Fred Armisen"],
        "d": 2
    },
    # 93
    {
        "q": "Which cast member played the perpetually screaming infomercial pitchman Billy Mays in late-2000s parodies?",
        "correct": "Dean Edwards / Darrell Hammond / Jason Sudeikis",
        "distractors": ["Bill Hader", "Kenan Thompson", "Will Forte"],
        "d": 3
    },
    # 94
    {
        "q": "What was the name of the fast-talking, chain-smoking casting agent portrayed by Cheri Oteri?",
        "correct": "Laura Kightlinger's co-worker Rita DelVecchio",
        "distractors": ["Mickey Day's agent", "Beverly Gelfand", "Shelley Duvall"],
        "d": 3
    },
    # 95
    {
        "q": "What absurd prop was featured in the 2008 SNL Digital Short 'Space Olympics' starring Andy Samberg?",
        "correct": "A sword made of light that cuts a hotdog in half",
        "distractors": ["A zero-gravity basketball hoop", "A laser-guided bowling ball", "A hoverboard powered by rockets"],
        "d": 3
    },
    # 96
    {
        "q": "In a 2001 sketch, what iconic character did Christopher Walken play alongside Amy Poehler and Horatio Sanz in an eccentric family reunion?",
        "correct": "A member of the bizarre Walken family",
        "distractors": ["Santa Claus", "The King of Sweden", "A retired mob boss"],
        "d": 3
    },
    # 97
    {
        "q": "Which action film star was depicted by Darrell Hammond in a recurring parody where he pitched unlikely luxury cars and aftershaves?",
        "correct": "Sean Connery",
        "distractors": ["Pierce Brosnan", "Roger Moore", "Timothy Dalton"],
        "d": 3
    },
    # 98
    {
        "q": "What was the name of the morning drive-time radio shock jocks portrayed by Chris Kattan and Jimmy Fallon?",
        "correct": "The Morning Zoo with Joey Mack",
        "distractors": ["Shock Waves with Danny and Donny", "The Morning Buzz with Mike and Bob", "Mad Dog and the Captain"],
        "d": 3
    },
    # 99
    {
        "q": "In the 2006 Digital Short 'Laser Cats', which director made a surprise cameo appearance praising the feline sci-fi home video?",
        "correct": "Steven Spielberg",
        "distractors": ["George Lucas", "James Cameron", "Peter Jackson"],
        "d": 2
    },
    # 100
    {
        "q": "What did the characters in 'Laser Cats' use as futuristic laser-blaster weapons?",
        "correct": "Real domestic cats that fired laser beams from their mouths",
        "distractors": ["Flashlights taped to cat collars", "Hairdryers painted metallic silver", "Cardboard tubes with glowsticks"],
        "d": 1
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "staging", "snl_batch2.json")
    build_batch(questions, out, batch_num=2)
