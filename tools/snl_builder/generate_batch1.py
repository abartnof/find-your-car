#!/usr/bin/env python3
"""
Generate SNL Batch 1: Classic Era Catchphrases, Sketches & Recurring Characters (1975-1989)
100 questions: exactly 30 d1, 40 d2, 30 d3.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from builder import build_batch

questions = [
    # 1
    {
        "q": "Which original cast member uttered the very first 'Live from New York, it's Saturday Night!' in the series premiere on October 11, 1975?",
        "correct": "Chevy Chase",
        "distractors": ["John Belushi", "Dan Aykroyd", "Michael O'Donoghue"],
        "d": 1
    },
    # 2
    {
        "q": "In the cold open of the very first episode of SNL, what was Michael O'Donoghue's character doing before Chevy Chase walked in?",
        "correct": "Teaching John Belushi an English lesson",
        "distractors": ["Fixing a broken television set", "Auditioning a lounge singer", "Tuning an acoustic guitar"],
        "d": 2
    },
    # 3
    {
        "q": "What bizarre phrase did Michael O'Donoghue instruct John Belushi to repeat in the very first sketch of SNL?",
        "correct": "I would like to feed your fingertips to the wolverines",
        "distractors": ["The rain in Spain falls mainly on the plain", "Never look a gift horse in the mouth", "Give me liberty or give me death"],
        "d": 3
    },
    # 4
    {
        "q": "What disguise was frequently used by the 'Land Shark' when knocking on victims' doors in early SNL seasons?",
        "correct": "Candygram",
        "distractors": ["Pizza delivery", "FBI agent", "Census taker"],
        "d": 1
    },
    # 5
    {
        "q": "What home planet did the Coneheads claim to originate from whenever curious humans questioned their appearance?",
        "correct": "Remulak",
        "distractors": ["Melmac", "Krypton", "Ork"],
        "d": 1
    },
    # 6
    {
        "q": "What did the Coneheads famously refer to eating and drinking as in their distinctive monotone speech?",
        "correct": "Consuming mass quantities",
        "distractors": ["Absorbing organic fuel", "Ingesting sustenance units", "Metabolizing Earth rations"],
        "d": 2
    },
    # 7
    {
        "q": "What were the names of the parents in the Coneheads family played by Dan Aykroyd and Jane Curtin?",
        "correct": "Beldar and Prymaat",
        "distractors": ["Gork and Verna", "Zonker and Marsha", "Klaatu and Barada"],
        "d": 2
    },
    # 8
    {
        "q": "In the Conehead sketches, what human profession did Beldar Conehead take up while living in suburban New Jersey?",
        "correct": "Driving instructor",
        "distractors": ["Dentist", "Mail carrier", "Bank teller"],
        "d": 3
    },
    # 9
    {
        "q": "What catchphrase did Steve Martin and Dan Aykroyd popularize as the Czech brothers Georg and Yortuk Festrunk?",
        "correct": "Two wild and crazy guys",
        "distractors": ["Too hot to handle", "Smooth operators from Prague", "Swingers of the world"],
        "d": 1
    },
    # 10
    {
        "q": "What country did Georg and Yortuk Festrunk, the 'Wild and Crazy Guys', emigrate from?",
        "correct": "Czechoslovakia",
        "distractors": ["Yugoslavia", "Hungary", "Poland"],
        "d": 2
    },
    # 11
    {
        "q": "What full names were given to the Blues Brothers alter egos created by John Belushi and Dan Aykroyd?",
        "correct": "'Joliet' Jake and Elwood Blues",
        "distractors": ["Frankie and Johnny Blues", "Big Joe and Blind Boy Blues", "Mack and Buster Blues"],
        "d": 1
    },
    # 12
    {
        "q": "In their earliest SNL musical performance on January 17, 1976, what costumes were Dan Aykroyd and John Belushi wearing when singing 'King Bee'?",
        "correct": "Bee costumes",
        "distractors": ["Black suits and fedoras", "Prison stripes", "Tuxedos"],
        "d": 2
    },
    # 13
    {
        "q": "In the famous 'Olympia Cafe' sketches, what food order was repeatedly refused with the response 'No fries, cheeps!'?",
        "correct": "French fries",
        "distractors": ["Onion rings", "Baked potato", "Coleslaw"],
        "d": 1
    },
    # 14
    {
        "q": "What beverage did John Belushi's short-order cook Pete insist customers drink in the Olympia Cafe sketch?",
        "correct": "Pepsi",
        "distractors": ["Coke", "Tab", "Dr Pepper"],
        "d": 1
    },
    # 15
    {
        "q": "Which real-life Chicago establishment inspired Don Novello and the writers to create the Olympia Cafe sketch?",
        "correct": "Billy Goat Tavern",
        "distractors": ["Lou Malnati's", "Wieners Circle", "Pizzeria Uno"],
        "d": 2
    },
    # 16
    {
        "q": "What lethal weapon did John Belushi's recurring character 'Samurai Futaba' wield behind the counter of various retail businesses?",
        "correct": "Katana sword",
        "distractors": ["Nunchucks", "Meat cleaver", "Bo staff"],
        "d": 1
    },
    # 17
    {
        "q": "Which iconic host engaged in a famous duel with Belushi's Samurai character while running the 'Samurai Delicatessen'?",
        "correct": "Buck Henry",
        "distractors": ["Steve Martin", "Elliott Gould", "Candice Bergen"],
        "d": 2
    },
    # 18
    {
        "q": "In a 1976 episode, John Belushi accidentally sliced Buck Henry on the forehead with a samurai sword, resulting in what visual gag for the rest of the show?",
        "correct": "The entire cast wore bandages on their foreheads",
        "distractors": ["Buck Henry wore a full suit of armor", "Belushi was placed in handcuffs", "A doctor stood on stage taking pulses"],
        "d": 3
    },
    # 19
    {
        "q": "What was the name of Gilda Radner's elderly, hard-of-hearing character who gave misguided editorial replies on Weekend Update?",
        "correct": "Emily Litella",
        "distractors": ["Roseanne Roseannadanna", "Lisa Lupner", "Baba Wawa"],
        "d": 1
    },
    # 20
    {
        "q": "What catchphrase did Emily Litella deliver sheepishly whenever Jane Curtin corrected her misunderstandings?",
        "correct": "Never mind!",
        "distractors": ["My mistake!", "Isn't that special!", "Pardon me!"],
        "d": 1
    },
    # 21
    {
        "q": "Which topic did Emily Litella famously rail against on Weekend Update after misreading the phrase 'endangered species'?",
        "correct": "Endangered feces",
        "distractors": ["Endangered peaches", "Endangered nieces", "Endangered fleeces"],
        "d": 2
    },
    # 22
    {
        "q": "What recurring correspondent character played by Gilda Radner always opened letters from 'Mr. Richard Fader from Fort Lee, New Jersey'?",
        "correct": "Roseanne Roseannadanna",
        "distractors": ["Emily Litella", "Candy Sweeney", "Colleen Dewhurst"],
        "d": 1
    },
    # 23
    {
        "q": "What was Roseanne Roseannadanna's signature philosophical catchphrase when recounting gross encounters?",
        "correct": "It's always something!",
        "distractors": ["Life goes on!", "Ain't that the truth!", "That's how the cookie crumbles!"],
        "d": 1
    },
    # 24
    {
        "q": "Which famous news anchor did Gilda Radner spoof under the caricature name 'Baba Wawa'?",
        "correct": "Barbara Walters",
        "distractors": ["Diane Sawyer", "Connie Chung", "Jane Pauley"],
        "d": 1
    },
    # 25
    {
        "q": "What was the name of the eccentric priest and Vatican gossip columnist portrayed by writer-performer Don Novello?",
        "correct": "Father Guido Sarducci",
        "distractors": ["Father Thomas O'Malley", "Father Joe Rossi", "Father Anthony Moretti"],
        "d": 1
    },
    # 26
    {
        "q": "In Father Guido Sarducci's comedy routine, what was the name of his accelerated higher-education concept that taught only what people remember five years later?",
        "correct": "Five Minute University",
        "distractors": ["Instant Degree College", "Speed Seminary", "Two-Hour Academy"],
        "d": 2
    },
    # 27
    {
        "q": "What product did Dan Aykroyd enthusiastically pitch in a 1976 commercial parody by dropping a whole fish into a kitchen blender?",
        "correct": "Super Bass-O-Matic '76",
        "distractors": ["Fish-O-Grinder 3000", "Aqua-Puree Supreme", "Trout Master Deluxe"],
        "d": 1
    },
    # 28
    {
        "q": "In a classic consumer safety sketch, what hazardous toy did Dan Aykroyd's sleazy manufacturer Irwin Mainway defend selling to children?",
        "correct": "Bag O' Glass",
        "distractors": ["Box O' Rusty Nails", "Tub O' Acid", "Crate O' Razor Blades"],
        "d": 2
    },
    # 29
    {
        "q": "What was the name of Irwin Mainway's dangerous Halloween costume for children that was simply a dry-cleaning plastic bag and rubber band?",
        "correct": "Invisible Knight",
        "distractors": ["Ghost in the Wind", "Phantom Strangler", "Midnight Stalker"],
        "d": 3
    },
    # 30
    {
        "q": "Which television chef did Dan Aykroyd parody in a 1978 sketch where she accidentally slices open her finger and bleeds profusely while advising viewers to 'save the liver'?",
        "correct": "Julia Child",
        "distractors": ["Fanny Cradock", "Graham Kerr", "James Beard"],
        "d": 1
    },
    # 31
    {
        "q": "What disco novelty song did Steve Martin perform in a lavish Egyptian-themed production number on April 22, 1978?",
        "correct": "King Tut",
        "distractors": ["Cleopatra Rock", "Pharaoh's Boogie", "Pyramid Strut"],
        "d": 1
    },
    # 32
    {
        "q": "According to the lyrics of Steve Martin's 'King Tut', where was King Tut born and where did he move?",
        "correct": "Born in Babylonia, moved to Arizona",
        "distractors": ["Born in Alexandria, moved to California", "Born in Cairo, moved to Ohio", "Born in Memphis, moved to Texas"],
        "d": 2
    },
    # 33
    {
        "q": "What popular song's instrumental theme did Bill Murray's character Nick the Lounge Singer invent melodramatic lyrics for?",
        "correct": "Star Wars",
        "distractors": ["Jaws", "Superman", "The Godfather"],
        "d": 1
    },
    # 34
    {
        "q": "In Bill Murray's lounge singer routine, what was the full name of his sweaty, tuxedo-clad persona?",
        "correct": "Nick Winters",
        "distractors": ["Nick Vegas", "Nick St. Cloud", "Nick Fontana"],
        "d": 2
    },
    # 35
    {
        "q": "What cruel act did Bill Murray's nerdy character Todd DiLaMuca routinely inflict upon Gilda Radner's Lisa Lupner?",
        "correct": "Giving her noogies",
        "distractors": ["Pulling her pigtails", "Stealing her glasses", "Giving her wedgies"],
        "d": 1
    },
    # 36
    {
        "q": "What musical instrument did Lisa Lupner claim to play with her nose in talent show sketches?",
        "correct": "Piano",
        "distractors": ["Clarinet", "Recorder", "Xylophone"],
        "d": 2
    },
    # 37
    {
        "q": "What was the name of the medieval physician played by Steve Martin who cured every ailment by applying leeches and bloodletting?",
        "correct": "Theodoric of York",
        "distractors": ["Bartholomew of Leeds", "Geoffrey of Canterbury", "Ignatius of Bristol"],
        "d": 2
    },
    # 38
    {
        "q": "In 'Theodoric of York, Medieval Barber', what epiphany does Theodoric briefly have before dismissing modern medicine and going back to bloodletting?",
        "correct": "Perhaps bleeding patients into a bowl actually causes death",
        "distractors": ["Perhaps bacteria cause infectious disease", "Perhaps the heart pumps blood through arteries", "Perhaps washing hands prevents infection"],
        "d": 3
    },
    # 39
    {
        "q": "What catchphrase was uttered by Garrett Morris as retired Dominican baseball player Chico Escuela on Weekend Update?",
        "correct": "Baseball been berry, berry good to me",
        "distractors": ["Hit the ball, run like wind", "No ball, no strike, just home run", "I play for money, I play for fun"],
        "d": 1
    },
    # 40
    {
        "q": "What was the title of the tell-all exposé book Chico Escuela claimed to have written about former teammate Reggie Jackson?",
        "correct": "Bad Stuff 'Bout the Mets",
        "distractors": ["Behind the Dugout", "Juice and Lies", "My Life in Baseball"],
        "d": 3
    },
    # 41
    {
        "q": "Which rock legend did John Belushi perform an uncanny, spastic split-screen duet with on October 2, 1976?",
        "correct": "Joe Cocker",
        "distractors": ["Mick Jagger", "Rod Stewart", "Bob Dylan"],
        "d": 2
    },
    # 42
    {
        "q": "What classic song did John Belushi and Joe Cocker perform together side-by-side on SNL?",
        "correct": "Feelin' Alright",
        "distractors": ["You Are So Beautiful", "With a Little Help from My Friends", "The Letter"],
        "d": 3
    },
    # 43
    {
        "q": "In a celebrated 1976 sketch, John Belushi played Vito Corleone attending what kind of modern meeting?",
        "correct": "A group therapy session",
        "distractors": ["A PTA meeting", "A traffic school class", "A speed dating event"],
        "d": 2
    },
    # 44
    {
        "q": "What children's show host did Eddie Murphy parody in his recurring sketch 'Mister Robinson's Neighborhood'?",
        "correct": "Fred Rogers",
        "distractors": ["Captain Kangaroo", "Shari Lewis", "Bob Keeshan"],
        "d": 1
    },
    # 45
    {
        "q": "Whenever someone banged loudly on Mister Robinson's apartment door, how did he usually escape?",
        "correct": "Out the window down the fire escape",
        "distractors": ["Through the laundry chute", "Into a secret closet safe", "Down the dumbwaiter"],
        "d": 2
    },
    # 46
    {
        "q": "What type of vocabulary words did Mister Robinson teach his young viewers in 'Mister Robinson's Neighborhood'?",
        "correct": "Words like eviction, scam, and squatter",
        "distractors": ["Words like honesty, integrity, and honor", "Words like subtraction, multiplication, and division", "Words like symphony, harmony, and melody"],
        "d": 2
    },
    # 47
    {
        "q": "Which Little Rascals character did Eddie Murphy famously portray as an adult pop star who sang phonetically garbled hits?",
        "correct": "Buckwheat",
        "distractors": ["Spanky", "Alfalfa", "Stymie"],
        "d": 1
    },
    # 48
    {
        "q": "What did Eddie Murphy's Buckwheat famously sing instead of 'Three Times a Lady'?",
        "correct": "Fee Tines a Mady",
        "distractors": ["Tree Tines a Baby", "Free Pines a Lady", "Wee Lines a Shady"],
        "d": 1
    },
    # 49
    {
        "q": "In 1983, Eddie Murphy grew tired of playing Buckwheat, prompting the show to air a spoof breaking news special where Buckwheat was what?",
        "correct": "Assassinated in front of 30 Rockefeller Plaza",
        "distractors": ["Abducted by extraterrestrials", "Elected Governor of New York", "Arrested for high treason"],
        "d": 2
    },
    # 50
    {
        "q": "What was the name of the crazed assassin who shot Buckwheat in SNL's spoof of the Reagan assassination attempt?",
        "correct": "John David Stutts",
        "distractors": ["Arthur Bremer", "Mark David Chapman", "Lee Harvey Oswald"],
        "d": 3
    },
    # 51
    {
        "q": "What catchphrase did Eddie Murphy's cigar-chomping claymation character Gumby bellow in anger?",
        "correct": "I'm Gumby, dammit!",
        "distractors": ["Green is mean!", "Don't poke the clay!", "Get out of my toybox!"],
        "d": 1
    },
    # 52
    {
        "q": "What was the name of Eddie Murphy's shady character who peddled how-to books like 'I Wanna Be a Ho' on late-night infomercials?",
        "correct": "Velvet Jones",
        "distractors": ["Silky Slim", "Diamond Dave", "Sweet Daddy Williams"],
        "d": 2
    },
    # 53
    {
        "q": "In a famous 1983 sketch, Eddie Murphy played James Brown hosting what unusual television program?",
        "correct": "Celebrity Hot Tub Party",
        "distractors": ["Celebrity Barbecue Cook-Off", "Celebrity Aerobics Workout", "Celebrity Bowling Championship"],
        "d": 2
    },
    # 54
    {
        "q": "In the mockumentary 'White Like Me' (1984), what did Eddie Murphy discover happens in banks when white people are alone?",
        "correct": "Banks give away free money without loan applications",
        "distractors": ["Secret underground nightclubs open behind vault doors", "Cocktail parties are immediately served on silver platters", "All mortgage debt is forgiven automatically"],
        "d": 2
    },
    # 55
    {
        "q": "Which legendary R&B singer made a guest appearance on SNL and judged an Eddie Murphy look-alike contest as Stevie Wonder?",
        "correct": "Stevie Wonder",
        "distractors": ["Ray Charles", "Smokey Robinson", "Marvin Gaye"],
        "d": 2
    },
    # 56
    {
        "q": "What pious catchphrase did Dana Carvey's Church Lady (Enid Strict) deploy whenever guests made dubious moral choices?",
        "correct": "Well, isn't that special?",
        "distractors": ["Bless your sweet soul!", "Heavens to Betsy!", "Lord have mercy!"],
        "d": 1
    },
    # 57
    {
        "q": "When suspecting someone of evil deeds on 'Church Chat', who did the Church Lady always blame with dramatic vocal emphasis?",
        "correct": "Could it be... SATAN?!",
        "distractors": ["Could it be... BEELZEBUB?!", "Could it be... LUCIFER?!", "Could it be... THE DEVIL?!"],
        "d": 1
    },
    # 58
    {
        "q": "What was the title of the recurring talk show hosted by Dana Carvey's Enid Strict?",
        "correct": "Church Chat",
        "distractors": ["Pew Talk", "The Sunday Pulpit", "Holy Hour"],
        "d": 2
    },
    # 59
    {
        "q": "What physical celebration did Enid Strict perform to organ music at the climax of her interviews on Church Chat?",
        "correct": "The Church Lady Dance",
        "distractors": ["The Holy Jump", "The Righteous Tap", "The Altar Strut"],
        "d": 2
    },
    # 60
    {
        "q": "What catchphrase did Dana Carvey and Kevin Nealon chant while pumping their padded muscles as Austrian bodybuilders Hans and Franz?",
        "correct": "Hear me now and believe me later",
        "distractors": ["Watch us now and marvel later", "Look at us and weep later", "Praise us now and thank us later"],
        "d": 1
    },
    # 61
    {
        "q": "What derogatory term did Hans and Franz use to describe people who lacked muscle definition?",
        "correct": "Girly men",
        "distractors": ["Pencil necks", "Puny weaklings", "Sack of potatoes"],
        "d": 1
    },
    # 62
    {
        "q": "Which action superstar appeared alongside Dana Carvey and Kevin Nealon in a famous Hans and Franz sketch in 1991?",
        "correct": "Arnold Schwarzenegger",
        "distractors": ["Sylvester Stallone", "Jean-Claude Van Damme", "Dolph Lundgren"],
        "d": 2
    },
    # 63
    {
        "q": "What was the name of the fictional cable access workout show hosted by Hans and Franz?",
        "correct": "Pumping Up with Hans and Franz",
        "distractors": ["Iron Men of Graz", "The Arnold Hour", "Muscle Power USA"],
        "d": 2
    },
    # 64
    {
        "q": "What catchphrase did Billy Crystal make famous while portraying greasy talk-show host Fernando Lamas?",
        "correct": "You look mahvelous!",
        "distractors": ["You look stunning!", "Darling you shine!", "Look at that face!"],
        "d": 1
    },
    # 65
    {
        "q": "According to Billy Crystal's Fernando, what was more important than feeling good?",
        "correct": "Looking good",
        "distractors": ["Having money", "Being famous", "Staying young"],
        "d": 2
    },
    # 66
    {
        "q": "What triangular-haired, high-trousered character did Martin Short bring to SNL from SCTV in the 1984-1985 season?",
        "correct": "Ed Grimley",
        "distractors": ["Jackie Rogers Jr.", "Nathan Thurm", "Troy McClure"],
        "d": 1
    },
    # 67
    {
        "q": "Which musical instrument did Martin Short's neurotic character Ed Grimley obsessively practice?",
        "correct": "Triangle",
        "distractors": ["Clarinet", "Tambourine", "Accordion"],
        "d": 2
    },
    # 68
    {
        "q": "In a legendary 1984 mockumentary short directed by Christopher Guest, Martin Short and Harry Shearer trained in which improbable Olympic sport?",
        "correct": "Men's synchronized swimming",
        "distractors": ["Curling", "Rhythmic gymnastics", "Two-man bobsled"],
        "d": 2
    },
    # 69
    {
        "q": "What famous catchphrase did Jon Lovitz's Pathological Liar Tommy Flanagan utter whenever caught in an outrageous falsehood?",
        "correct": "Yeah, that's the ticket!",
        "distractors": ["Cross my heart and hope to die!", "Would I lie to you?", "Believe you me!"],
        "d": 1
    },
    # 70
    {
        "q": "Who did Tommy Flanagan frequently claim was his glamorous celebrity wife?",
        "correct": "Morgan Fairchild",
        "distractors": ["Farrah Fawcett", "Cher", "Raquel Welch"],
        "d": 2
    },
    # 71
    {
        "q": "What single word exclamation did Jon Lovitz dramatically shout as the pretentious Master Thespian after deceiving someone?",
        "correct": "ACTING!",
        "distractors": ["GENIUS!", "BRILLIANT!", "DRAMA!"],
        "d": 1
    },
    # 72
    {
        "q": "What was the title of the recurring sketch starring Jan Hooks and Nora Dunn as an overly enthusiastic lounge singing sister duo?",
        "correct": "The Sweeney Sisters",
        "distractors": ["The Andrews Duet", "The Miller Chanteuses", "The Harmonizing Belles"],
        "d": 2
    },
    # 73
    {
        "q": "What musical tic did the Sweeney Sisters (Candy and Liz) frequently insert into their medleys between pop standards?",
        "correct": "Clang clang clang went the trolley / Ding ding ding",
        "distractors": ["Shoo-be-doo-wop", "La-di-da sweet cherry pie", "Boop-oop-a-doop"],
        "d": 3
    },
    # 74
    {
        "q": "What was the fatal flaw of Toonces the Driving Cat in Jack Handey's recurring comedy sketches?",
        "correct": "He invariably steered the car off a cliff",
        "distractors": ["He ran out of gas in the desert", "He drove in reverse down highways", "He fell asleep at red lights"],
        "d": 1
    },
    # 75
    {
        "q": "Who played Toonces' human owner Lyle in the original Toonces the Driving Cat sketches?",
        "correct": "Steve Martin",
        "distractors": ["Dana Carvey", "Phil Hartman", "Kevin Nealon"],
        "d": 2
    },
    # 76
    {
        "q": "In a 1986 sketch, Phil Hartman portrayed President Ronald Reagan revealing what secret persona when reporters left the Oval Office?",
        "correct": "A ruthless, hyper-competent mastermind fluent in Arabic",
        "distractors": ["A secret Soviet KGB agent sending coded Morse radio messages", "A standup comic who wrote all his own zingers", "An opera singer practicing arias"],
        "d": 2
    },
    # 77
    {
        "q": "What was the opening greeting Mike Myers used as Dieter, the black-turtleneck-wearing German avant-garde host of 'Sprockets'?",
        "correct": "Now is the time on Sprockets when we dance!",
        "distractors": ["Let us now celebrate nihilism!", "Welcome to the emptiness of modern Munich!", "Prepare yourself for ultimate despair!"],
        "d": 2
    },
    # 78
    {
        "q": "What pet animal did Dieter encourage his guests to touch during episodes of 'Sprockets'?",
        "correct": "His monkey",
        "distractors": ["His iguana", "His dachshund", "His ferret"],
        "d": 1
    },
    # 79
    {
        "q": "What was the name of Dieter's beloved pet monkey on 'Sprockets'?",
        "correct": "Klaus",
        "distractors": ["Hans", "Fritz", "Otto"],
        "d": 3
    },
    # 80
    {
        "q": "What public access television series did Wayne Campbell and Garth Algar host from an Aurora, Illinois basement beginning in 1989?",
        "correct": "Wayne's World",
        "distractors": ["The Basement Zone", "Rock on Aurora", "Midwest Metal Hour"],
        "d": 1
    },
    # 81
    {
        "q": "What exclamation of unworthiness did Wayne and Garth chant while bowing furiously before rock royalty like Alice Cooper?",
        "correct": "We're not worthy!",
        "distractors": ["Bow down to the gods!", "We are mere worms!", "All hail the kings!"],
        "d": 1
    },
    # 82
    {
        "q": "What was Garth Algar's famous retort whenever Wayne or a guest asked him something awkward on 'Wayne's World'?",
        "correct": "I like to play!",
        "distractors": ["Party on!", "Don't look at me!", "No way, Jose!"],
        "d": 3
    },
    # 83
    {
        "q": "What rock band's song 'Bohemian Rhapsody' was famously revived after being featured in Wayne and Garth's car headbanging routine?",
        "correct": "Queen",
        "distractors": ["Aerosmith", "Led Zeppelin", "Def Leppard"],
        "d": 1
    },
    # 84
    {
        "q": "What nonsense song about vegetables did Dana Carvey perform as pretentious British singer Derek Stevens in a 1986 episode?",
        "correct": "Choppin' Broccoli",
        "distractors": ["Peeling Asparagus", "Mashing Potatoes", "Boiling Cabbage"],
        "d": 2
    },
    # 85
    {
        "q": "What catchphrase did Dana Carvey make ubiquitous when impersonating President George H.W. Bush in the late 1980s?",
        "correct": "Wouldn't be prudent",
        "distractors": ["Read my lips", "No new taxes", "Stay the course"],
        "d": 1
    },
    # 86
    {
        "q": "What phrase did Dana Carvey's George H.W. Bush repeatedly use to dismiss risky political maneuvers?",
        "correct": "Not gonna do it",
        "distractors": ["Count me out", "Never ever", "Out of bounds"],
        "d": 2
    },
    # 87
    {
        "q": "In the 1988 presidential debate sketch, which candidate did Jon Lovitz play who stood atop a stool to look taller?",
        "correct": "Michael Dukakis",
        "distractors": ["George H.W. Bush", "Dan Quayle", "Lloyd Bentsen"],
        "d": 2
    },
    # 88
    {
        "q": "What was Jon Lovitz's memorable deadpan inner thought line as Michael Dukakis during the 1988 debate sketch?",
        "correct": "I can't believe I'm losing to this guy",
        "distractors": ["Why did I ride in that tank?", "I should have smiled more", "Massachusetts has a balanced budget"],
        "d": 3
    },
    # 89
    {
        "q": "Which First Lady did cast member Terry Sweeney famously impersonate in the 1985-1986 season, marking the first time an openly gay male cast member played a First Lady?",
        "correct": "Nancy Reagan",
        "distractors": ["Rosalynn Carter", "Betty Ford", "Barbara Bush"],
        "d": 2
    },
    # 90
    {
        "q": "What was the title of Rich Hall's popular segment where he coined words that don't appear in the dictionary but should?",
        "correct": "Sniglets",
        "distractors": ["Portmanteaus", "Brainwords", "Oddonyms"],
        "d": 2
    },
    # 91
    {
        "q": "What was the name of the manic commercial pitchman played by Dan Aykroyd who hawked the 'Bass-O-Matic' and hazardous toys?",
        "correct": "Irwin Mainway",
        "distractors": ["Crazy Ernie", "Ron Popeil", "Billy Mays"],
        "d": 3
    },
    # 92
    {
        "q": "In the 1970s, what was the name of the recurring sketch series featuring Jane Curtin, Dan Aykroyd, and John Belushi as giant yellow bees?",
        "correct": "The Killer Bees",
        "distractors": ["The Hive Crew", "The Buzz Brothers", "The Honey Stingers"],
        "d": 2
    },
    # 93
    {
        "q": "Who wrote the iconic 1975 'Dead String Quartet' sketch in which four classical musicians sit silently and completely dead on stage?",
        "correct": "Michael O'Donoghue",
        "distractors": ["Al Franken", "Tom Davis", "Dan Aykroyd"],
        "d": 3
    },
    # 94
    {
        "q": "In a 1978 sketch featuring Dan Aykroyd as a late-night talk show host, which real-life host of 'The Tomorrow Show' did he impersonate with a booming laugh and thick eyebrows?",
        "correct": "Tom Snyder",
        "distractors": ["Dick Cavett", "Mike Douglas", "Merv Griffin"],
        "d": 2
    },
    # 95
    {
        "q": "What was the name of the eccentric recurring character played by Gilda Radner who performed dramatic bedroom monologues while bouncing violently on her bed?",
        "correct": "Judy Miller",
        "distractors": ["Rhonda Shear", "Debbie Doody", "Suzy Chapstick"],
        "d": 3
    },
    # 96
    {
        "q": "What line did Garrett Morris shout out the window to provide translation assistance on Weekend Update in the 'News for the Hard of Hearing' segments?",
        "correct": "Repeating the headline at the top of his lungs",
        "distractors": ["Translating the news into Spanish", "Typing on a giant telegraph machine", "Banging on a brass gong"],
        "d": 2
    },
    # 97
    {
        "q": "What was the name of the diner customer played by John Belushi who argued with Pete over his desire to order eggs instead of cheeseburgers?",
        "correct": "Bill Murray",
        "distractors": ["Dan Aykroyd", "Chevy Chase", "Garrett Morris"],
        "d": 3
    },
    # 98
    {
        "q": "In a famous 1977 sketch, Dan Aykroyd as President Jimmy Carter takes phone calls from citizens and calmly talks an anxious young man through what emergency?",
        "correct": "A bad acid trip",
        "distractors": ["A botched home electrical rewiring", "A high-speed car chase", "A failed parachute jump"],
        "d": 3
    },
    # 99
    {
        "q": "What was the title of the recurring sketch featuring Martin Short as sleazy, sweaty corporate lawyer Nathan Thurm?",
        "correct": "The Investigation / 60 Minutes parody",
        "distractors": ["Nightline Parody", "Courtroom 8H", "Wall Street Undercover"],
        "d": 3
    },
    # 100
    {
        "q": "What nervous, defensive catchphrase did Martin Short mutter as shifty lawyer Nathan Thurm whenever confronted with incriminating evidence?",
        "correct": "I know that! Why wouldn't I know that?",
        "distractors": ["I plead the fifth! You can't prove it!", "Who told you that? Was it Frank?", "No comment, no comment at all!"],
        "d": 2
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "staging", "snl_batch1.json")
    build_batch(questions, out, batch_num=1)
