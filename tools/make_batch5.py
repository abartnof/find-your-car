#!/usr/bin/env python3
"""
Generate Batch 5: Teen, High School & Coming-of-Age Sitcoms (100 questions)
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from sitcom_builder import make_batch

q_batch5 = [
    # Saved by the Bell (30 questions)
    {
        "q": "What California high school served as the setting for Zack Morris and his friends on Saved by the Bell?",
        "correct": "Bayside High School",
        "distractors": ["Valley High School", "Pacific Palisades Prep", "West Beverly High"],
        "d": 1
    },
    {
        "q": "What was the name and signature catchphrase greeting of Bayside High's principal, played by Dennis Haskins?",
        "correct": "Mr. Richard Belding ('Hey, hey, hey, what is going on here?')",
        "distractors": ["Mr. Arthur McGee ('Now hold on just a minute!')", "Mr. Edward Rooney ('Quiet down this instant!')", "Mr. Gerald Vance ('Attention all students!')"],
        "d": 1
    },
    {
        "q": "What fourth-wall-breaking supernatural power did Zack Morris possess to freeze live action and address the camera?",
        "correct": "Calling a 'Time out!' with hand gestures",
        "distractors": ["Snapping his fingers twice", "Blinking rapidly into the lens", "Whistling three sharp notes"],
        "d": 1
    },
    {
        "q": "What local diner and teen hangout on Saved by the Bell was run by a proprietor who performed magic tricks?",
        "correct": "The Max",
        "distractors": ["The Peach Pit", "The Hub", "The Smash Club"],
        "d": 1
    },
    {
        "q": "What condescending nickname did high school wrestling champion A.C. Slater (Mario Lopez) constantly call Zack Morris?",
        "correct": "Preppy",
        "distractors": ["Blondie", "Pretty Boy", "Richie"],
        "d": 1
    },
    {
        "q": "What was the name of the sentient, talking robot built by Screech Powers that helped him with homework?",
        "correct": "Kevin",
        "distractors": ["Robbie", "Gizmo", "Buster"],
        "d": 2
    },
    {
        "q": "Which fashionable classmate was the object of Samuel 'Screech' Powers' desperate, unreciprocated romantic obsession?",
        "correct": "Lisa Turtle",
        "distractors": ["Kelly Kapowski", "Jessie Spano", "Tori Scott"],
        "d": 1
    },
    {
        "q": "In the famous 'very special episode' 'Jessie's Song', what over-the-counter substance causes Jessie Spano's manic breakdown?",
        "correct": "Caffeine pills",
        "distractors": ["Diet appetite suppressants", "Ephedrine workout supplements", "Sleeping pills"],
        "d": 1
    },
    {
        "q": "What Pointer Sisters lyric does Jessie Spano hysterically attempt to sing during her emotional breakdown in Zack's arms?",
        "correct": "I'm so excited! I'm so excited! I'm so... scared!",
        "distractors": ["I'm so glad, I'm so glad, I'm so alone!", "Jump for my love, jump, jump... I can't jump!", "Fire in the night, fire... please stop!"],
        "d": 1
    },
    {
        "q": "Why was the script for 'Jessie's Song' altered so that Jessie became hooked on caffeine pills rather than speed?",
        "correct": "NBC Standards and Practices ruled that illegal amphetamines were too severe for Saturday morning kids' television",
        "distractors": ["Elizabeth Berkley refused to portray an illicit narcotics user", "Sponsors threatened to pull advertisements for breakfast cereals", "The cast protested the dark tone during table reads"],
        "d": 2
    },
    {
        "q": "What was the name of the pop music girl group formed by Kelly, Jessie, and Lisa, known for their workout-attire music video?",
        "correct": "Hot Sundae",
        "distractors": ["The Bayside Babes", "Sundae Sweethearts", "California Dreamgirls"],
        "d": 2
    },
    {
        "q": "What was the title of the sentimental graduation anthem recorded by Zack Morris' band, Zack Attack?",
        "correct": "Friends Forever",
        "distractors": ["Did You Ever See a Flying Pig?", "Memories of Bayside", "Forever By Your Side"],
        "d": 1
    },
    {
        "q": "Where did the gang spend their summer vacation working as staff in a special set of Season 3 episodes?",
        "correct": "Malibu Sands Beach Club",
        "distractors": ["Newport Beach Resort", "Catalina Island Yacht Club", "Laguna Palms Country Club"],
        "d": 1
    },
    {
        "q": "Which future sitcom star played Stacey Carosi, the tough New York daughter of the Malibu Sands resort owner who dates Zack?",
        "correct": "Leah Remini",
        "distractors": ["Alyssa Milano", "Marisa Tomei", "Jennifer Aniston"],
        "d": 1
    },
    {
        "q": "Why was the character of leather-jacket-wearing transfer student Tori Scott (Leanna Creel) abruptly brought in during Season 4?",
        "correct": "Tiffani-Amber Thiessen and Elizabeth Berkley chose not to sign contract extensions for extra ordered episodes",
        "distractors": ["Producers wanted to introduce an edgy punk rock element to boost older teen ratings", "Dennis Haskins advocated for a niece character to be written into the show", "Elizabeth Berkley had booked the lead in Showgirls and departed"],
        "d": 2
    },
    {
        "q": "What short-lived Disney Channel predecessor series featured Zack, Screech, Lisa, and Mr. Belding at an Indiana middle school?",
        "correct": "Good Morning, Miss Bliss",
        "distractors": ["Junior High Days", "The Bell Rings at Eight", "Indiana Prep"],
        "d": 2
    },
    {
        "q": "Which Oscar-winning British actress starred as sixth-grade teacher Miss Bliss in the original version of the show?",
        "correct": "Hayley Mills",
        "distractors": ["Julie Andrews", "Vanessa Redgrave", "Maggie Smith"],
        "d": 2
    },
    {
        "q": "What was the name of A.C. Slater's pet chameleon that tragically died, prompting an emotional mock funeral at Bayside?",
        "correct": "Artie",
        "distractors": ["Barnaby", "Sammy", "Iggie"],
        "d": 2
    },
    {
        "q": "What suspiciously astronomical SAT score did slacker Zack Morris achieve, prompting college scouts to recruit him?",
        "correct": "1502",
        "distractors": ["1590", "1420", "1600"],
        "d": 2
    },
    {
        "q": "In the anti-drug episode 'No Hope With Dope', which Hollywood teen celebrity idol turns out to be smoking marijuana at a party?",
        "correct": "Johnny Dakota",
        "distractors": ["Brett Montana", "Lance Vance", "Troy Sterling"],
        "d": 2
    },
    {
        "q": "What valuable natural resource is discovered beneath the athletic field at Bayside High in Season 3's 'Pipe Dreams'?",
        "correct": "Crude oil",
        "distractors": ["Natural gas reserves", "Gold nuggets", "Prehistoric dinosaur bones"],
        "d": 2
    },
    {
        "q": "Who was the executive producer and creative architect behind Saved by the Bell and NBC's entire TNBC teen Saturday morning block?",
        "correct": "Peter Engel",
        "distractors": ["Haim Saban", "Dick Clark", "Dan Schneider"],
        "d": 2
    },
    {
        "q": "In Saved by the Bell: The College Years, what fictional California university did Zack, Slater, Screech, and Kelly attend?",
        "correct": "Cal U",
        "distractors": ["Pacific University", "UCLA South", "Bayside State"],
        "d": 1
    },
    {
        "q": "Which former NFL defensive tackle played Mike Rogers, the gang's college resident advisor and former football player?",
        "correct": "Bob Golic",
        "distractors": ["Howie Long", "Lyle Alzado", "Bubba Smith"],
        "d": 2
    },
    {
        "q": "In the 1994 television film Saved by the Bell: Wedding in Las Vegas, what milestone event takes place?",
        "correct": "Zack Morris and Kelly Kapowski get married",
        "distractors": ["Slater wins the collegiate national wrestling title", "Screech inherits a billion-dollar software fortune", "Mr. Belding is named Chancellor of Cal U"],
        "d": 1
    },
    {
        "q": "What portable technology became Zack Morris' ultimate comedic status symbol in early seasons of Saved by the Bell?",
        "correct": "A massive, brick-sized Motorola cellular phone with a long pull-out antenna",
        "distractors": ["A belt-mounted digital beeper pager", "A pocket cassette recorder", "An early Apple Newton handheld PDA"],
        "d": 1
    },
    {
        "q": "What was the name of Kelly Kapowski's handsome, older boss at The Max with whom she had an affair, breaking Zack's heart?",
        "correct": "Jeff Hunter",
        "distractors": ["Dan Adams", "Craig Miller", "Rick Stevens"],
        "d": 2
    },
    {
        "q": "What mascot costume did Screech Powers wear as the proud spirited symbol of Bayside High?",
        "correct": "A tiger",
        "distractors": ["A bulldog", "A falcon", "A pirate"],
        "d": 2
    },
    {
        "q": "In the episode 'The Prom', why does Kelly Kapowski tell Zack she cannot afford to attend the high school dance?",
        "correct": "Her father lost his defense contractor job and the family has no money for a dress",
        "distractors": ["She has to work an overnight shift at the nursing home", "She lost her baby-sitting earnings paying a parking ticket", "Her family's car broke down and needs an engine overhaul"],
        "d": 2
    },
    {
        "q": "What gesture does Zack Morris make outside the school prom building to give Kelly her dream night?",
        "correct": "He sets up a picnic table outside with candles and slow-dances with her in the courtyard",
        "distractors": ["He buys her an expensive limousine ride across the city", "He brings the live rock band out to the football bleachers", "He serenades her on acoustic guitar under her bedroom window"],
        "d": 2
    },

    # Blossom (25 questions)
    {
        "q": "Which actress, who later earned a Ph.D. in neuroscience, starred as the eccentric teen Blossom Russo?",
        "correct": "Mayim Bialik",
        "distractors": ["Melissa Joan Hart", "Jenna von Oÿ", "Sara Gilbert"],
        "d": 1
    },
    {
        "q": "What signature fashion item did Blossom Russo famously wear and popularize as a 90s teen trend?",
        "correct": "Floppy floral hats with upturned brims and giant sunflowers",
        "distractors": ["Oversized neon flannel shirts tied around the waist", "Platform combat boots with lace trim", "Denim overalls with one strap unbuckled"],
        "d": 1
    },
    {
        "q": "What was the name of Blossom's hyperactive, motor-mouthed best friend played by Jenna von Oÿ?",
        "correct": "Six LeMeure",
        "distractors": ["Seven Miller", "Five O'Connor", "Sunday Brooks"],
        "d": 1
    },
    {
        "q": "How did Six LeMeure explain the bizarre origin of her numerical first name on Blossom?",
        "correct": "She was the sixth child in her family, or referring to the six-pack of beer her parents drank",
        "distractors": ["She was born on the sixth day of June at six in the morning", "Her parents were obsessed with the Six Million Dollar Man", "She weighed six pounds and six ounces at birth"],
        "d": 2
    },
    {
        "q": "What was the famous one-word exclamation and trademark catchphrase of Blossom's handsome brother Joey Russo?",
        "correct": "Whoa!",
        "distractors": ["Dude!", "Yeah!", "Bummer!"],
        "d": 1
    },
    {
        "q": "Which real-life teen idol played middle brother Joey Russo on Blossom?",
        "correct": "Joey Lawrence",
        "distractors": ["Matthew Lawrence", "Andrew Lawrence", "Jason Priestley"],
        "d": 1
    },
    {
        "q": "What was the occupation and personal backstory of eldest brother Anthony Russo (Michael Stoyanov)?",
        "correct": "He was a recovering substance abuser who worked as an EMT / paramedic",
        "distractors": ["He was a former juvenile delinquent who became a public high school history teacher", "He was a high school dropout who worked as an apprentice auto mechanic", "He was an aspiring stand-up comic who worked at a recording studio"],
        "d": 2
    },
    {
        "q": "What was the musical profession of Blossom's divorced single father Nick Russo, played by Ted Wass?",
        "correct": "Session piano player and touring musician",
        "distractors": ["High school marching band conductor", "Commercial jingle composer", "Orchestral violinist"],
        "d": 2
    },
    {
        "q": "Where did Blossom's biological mother Maddy go when she abandoned the family before the series began?",
        "correct": "Paris, France, to pursue her own independent life and career",
        "distractors": ["New York City, to star on Broadway", "Nashville, Tennessee, to pursue country music", "London, England, to work in fashion design"],
        "d": 2
    },
    {
        "q": "What innovative storytelling device did Blossom use in her bedroom to reflect on adolescent anxieties?",
        "correct": "Recording candid video diary entries into her camcorder and imagining imaginary celebrity visits",
        "distractors": ["Writing handwritten entries in a locked leather journal", "Speaking directly to a magical mirror that replied", "Narrating comic book panels drawn on a drafting table"],
        "d": 1
    },
    {
        "q": "Which alien television superstar made a famous fantasy guest appearance in Blossom's video diary?",
        "correct": "ALF",
        "distractors": ["The Great Gazoo", "Mork from Ork", "Uncle Martin"],
        "d": 2
    },
    {
        "q": "What was the name of Blossom's steady, motorcycle-riding Italian-American high school boyfriend?",
        "correct": "Vinnie Bonitardi (David Lascher)",
        "distractors": ["Tony Miller", "Sal Romano", "Frankie DeMarco"],
        "d": 2
    },
    {
        "q": "Who performed the funky, New Orleans-style opening theme song 'My Opinionation' for Blossom?",
        "correct": "Dr. John",
        "distractors": ["Randy Newman", "Leon Russell", "Harry Connick Jr."],
        "d": 2
    },
    {
        "q": "Who created Blossom after previously co-creating The John Larroquette Show and writing on The Golden Girls?",
        "correct": "Don Reo",
        "distractors": ["Susan Harris", "David Angell", "Garry Marshall"],
        "d": 3
    },
    {
        "q": "Which veteran actor portrayed Blossom's cool, swing-dancing maternal grandfather Buzz Richman?",
        "correct": "Barnard Hughes",
        "distractors": ["Art Carney", "Burgess Meredith", "Buddy Ebsen"],
        "d": 2
    },
    {
        "q": "What athletic dream did Joey Russo passionately pursue in the later seasons of Blossom?",
        "correct": "Playing professional minor league baseball",
        "distractors": ["Joining an Olympic gymnastics squad", "Playing college basketball for UCLA", "Becoming a professional surfer"],
        "d": 2
    },
    {
        "q": "Who was originally cast and played Blossom's father in the unaired pilot before Ted Wass assumed the role?",
        "correct": "Richard Masur",
        "distractors": ["Michael Gross", "Alan Thicke", "John Ritter"],
        "d": 3
    },
    {
        "q": "What real-life pop music single by Joey Lawrence charted on the Billboard Hot 100 in 1993 during Blossom's peak?",
        "correct": "Nothin' My Love Can't Fix",
        "distractors": ["Stay the Night", "Whoa Baby", "Feel the Beat"],
        "d": 2
    },
    {
        "q": "What English actress joined the cast in later seasons as Nick Russo's new wife Carol?",
        "correct": "Finola Hughes",
        "distractors": ["Jane Leeves", "Stephanie Beacham", "Joan Collins"],
        "d": 2
    },
    {
        "q": "What was the name of Carol's precocious young daughter who became Blossom's stepsister?",
        "correct": "Kennedy",
        "distractors": ["Madison", "Taylor", "Reagan"],
        "d": 2
    },
    {
        "q": "In an acclaimed Season 2 episode, what traumatic secret does Six confide to Blossom after running away?",
        "correct": "She fears she might be pregnant after an encounter with a college boy",
        "distractors": ["Her mother's boyfriend attempted to strike her", "She was caught shoplifting designer jewelry", "She was expelled from high school for cheating"],
        "d": 2
    },
    {
        "q": "In the series finale of Blossom, what major life step does the Russo family confront?",
        "correct": "Nick and Carol put the family home up for sale as the kids prepare to move out",
        "distractors": ["Blossom graduates from Harvard Medical School", "Joey is called up to the Major Leagues in New York", "Anthony opens his own private clinic in Chicago"],
        "d": 2
    },
    {
        "q": "What musical instrument did Blossom play in the school band in early seasons?",
        "correct": "Trumpet",
        "distractors": ["Flute", "Clarinet", "Drums"],
        "d": 3
    },
    {
        "q": "What famous sitcom star made a cameo as Doogie Howser M.D. in one of Blossom's daydream sequences?",
        "correct": "Neil Patrick Harris",
        "distractors": ["Fred Savage", "Kirk Cameron", "Wil Wheaton"],
        "d": 2
    },
    {
        "q": "What was Anthony Russo's Las Vegas wife's name whom he married after an impulsive drunken night?",
        "correct": "Rhonda",
        "distractors": ["Brenda", "Glenda", "Linda"],
        "d": 3
    },

    # California Dreams (15 questions)
    {
        "q": "What was the central concept and musical genre of NBC's Saturday morning teen series California Dreams?",
        "correct": "A group of Southern California high school friends who form a surf-pop garage band",
        "distractors": ["A competitive high school dance troupe preparing for national championships", "A teen radio broadcasting crew broadcasting from a Venice Beach pier", "A group of teenage lifeguards training on Santa Monica beach"],
        "d": 1
    },
    {
        "q": "What was the name of the band's fast-talking, leather-vest-wearing manager who constantly sought get-rich-quick schemes?",
        "correct": "Sylvester 'Sly' Winkle (Michael Cade)",
        "distractors": ["Zack Logan", "Matt Garrison", "Jake Sommers"],
        "d": 1
    },
    {
        "q": "What was Sly Winkle's trademark slogan whenever he secured a gig or pitched a deal?",
        "correct": "Ba-da-bing, ba-da-boom! Make it happen!",
        "distractors": ["Book it and cook it!", "Show me the green!", "Cash in the bank, baby!"],
        "d": 2
    },
    {
        "q": "What beachside diner and hangout served as the main social hub for the band in California Dreams?",
        "correct": "Sharkey's",
        "distractors": ["The Wave", "The Surf Shack", "Malibu Bites"],
        "d": 1
    },
    {
        "q": "Which blonde actress played bassist and avid surfer Tiffani Smith while also appearing on Baywatch?",
        "correct": "Kelly Packard",
        "distractors": ["Jennie Kwan", "Diana Uribe", "Heidi Noelle Lenhart"],
        "d": 2
    },
    {
        "q": "What was the name of the soulful African-American drummer of the California Dreams band played by William James Jones?",
        "correct": "Tony Wicks",
        "distractors": ["Marcus Vance", "Derrick Hall", "Jamal King"],
        "d": 2
    },
    {
        "q": "When lead singer Matt Garrison left the band in Season 2, which leather-jacket-wearing bad-boy guitarist replaced him as frontman?",
        "correct": "Jake Sommers (Jay Anthony Franke)",
        "distractors": ["Mark Garrison", "Sam Woo", "Keith Del"],
        "d": 2
    },
    {
        "q": "What Asian-American character played keyboards and sang backup vocals in the band, portrayed by Jennie Kwan?",
        "correct": "Samantha 'Sam' Woo",
        "distractors": ["Connie Tanaka", "Kimberly Park", "Amy Chen"],
        "d": 2
    },
    {
        "q": "What wealthy, fiery Costa Rican exchange student joined the band and lived with the Garrisons in later seasons?",
        "correct": "Lorena Costa (Diana Uribe)",
        "distractors": ["Maria Santos", "Elena Alvarez", "Carmen Diaz"],
        "d": 2
    },
    {
        "q": "In whose family garage did the band rehearse and store their instruments throughout California Dreams?",
        "correct": "The Garrison family garage",
        "distractors": ["The Winkle pool house", "The Smith beach cabana", "Sharkey's back storage shed"],
        "d": 2
    },
    {
        "q": "Which producer created and executive produced California Dreams following his massive success with Saved by the Bell?",
        "correct": "Peter Engel",
        "distractors": ["Dan Schneider", "Thomas W. Lynch", "Stan Rogow"],
        "d": 2
    },
    {
        "q": "What lyric opens the upbeat California Dreams theme song?",
        "correct": "Everybody's got a dream...",
        "distractors": ["Catch the wave into the sun...", "Summer days and ocean breeze...", "Wake up, sunshine in your eyes..."],
        "d": 2
    },
    {
        "q": "What was the romantic pairing between the bad boy and the wholesome surfer girl that drove much of the show's drama?",
        "correct": "Jake Sommers and Tiffani Smith",
        "distractors": ["Sly Winkle and Sam Woo", "Matt Garrison and Jenny Garrison", "Tony Wicks and Lorena Costa"],
        "d": 1
    },
    {
        "q": "What Pacific coast city served as the sun-drenched backdrop for California Dreams?",
        "correct": "Pacific Palisades",
        "distractors": ["San Diego", "Santa Barbara", "Huntington Beach"],
        "d": 2
    },
    {
        "q": "What instrument did nerdy band member Mark Garrison play when he was introduced in Season 2?",
        "correct": "Keyboards",
        "distractors": ["Saxophone", "Harmonica", "Rhythm Guitar"],
        "d": 3
    },

    # Smart Guy (15 questions)
    {
        "q": "What was the premise of The WB's hit comedy Smart Guy?",
        "correct": "A 10-year-old child prodigy with an IQ of 180 skips six grades into high school",
        "distractors": ["A teenage computer hacker is secretly recruited by the CIA", "A brilliant science student builds a time machine in his bedroom", "A child inventor sells patent rights to a Fortune 500 tech firm"],
        "d": 1
    },
    {
        "q": "What was the full name of the young prodigy protagonist played by Tahj Mowry?",
        "correct": "T.J. Henderson",
        "distractors": ["Marcus Henderson", "Mo Henderson", "Tyler Henderson"],
        "d": 1
    },
    {
        "q": "What was the name of the Washington D.C. high school that T.J. attended alongside his older brother Marcus?",
        "correct": "Piedmont High School",
        "distractors": ["Georgetown Prep", "Potomac Valley High", "Lincoln Heights High"],
        "d": 2
    },
    {
        "q": "Which actor, who famously sang 'I Just Can't Wait to Be King' as young Simba in Disney's The Lion King, played older brother Marcus Henderson?",
        "correct": "Jason Weaver",
        "distractors": ["Merlin Santana", "Brandon Adams", "Larenz Tate"],
        "d": 1
    },
    {
        "q": "What was the name of Marcus's lovable, food-obsessed, slow-witted best friend played by Omar Gooding?",
        "correct": "Morris L. 'Mo' Tibbs",
        "distractors": ["Waldo Faldo", "Deion Jones", "Craig Dixon"],
        "d": 1
    },
    {
        "q": "Who portrayed T.J. and Marcus's intelligent, stylish older sister Yvette Henderson?",
        "correct": "Essence Atkins",
        "distractors": ["Reagan Gomez-Preston", "Countess Vaughn", "Meagan Good"],
        "d": 1
    },
    {
        "q": "What blue-collar business was owned and operated by the Henderson family patriarch Floyd Henderson (John Marshall Jones)?",
        "correct": "Floyd Henderson Contracting / Roofing",
        "distractors": ["Henderson Automotive Repair", "Capital City Plumbing", "District HVAC Services"],
        "d": 2
    },
    {
        "q": "What was Piedmont High School's school mascot costume that T.J. agreed to wear at football games?",
        "correct": "The Piedmont Penguin",
        "distractors": ["The Piedmont Panther", "The Piedmont Patriot", "The Piedmont Pelican"],
        "d": 2
    },
    {
        "q": "What musical instrument was T.J. Henderson shown to play with immense skill in the Piedmont High jazz band?",
        "correct": "Keyboards / Piano",
        "distractors": ["Saxophone", "Drums", "Trumpet"],
        "d": 2
    },
    {
        "q": "What real-life family connection did Smart Guy lead Tahj Mowry have to another hit 90s sitcom?",
        "correct": "He is the younger brother of identical twins Tia and Tamera Mowry (Sister, Sister)",
        "distractors": ["He is the nephew of Will Smith (The Fresh Prince of Bel-Air)", "He is the younger brother of Jaleel White (Family Matters)", "He is the cousin of Brandy Norwood (Moesha)"],
        "d": 1
    },
    {
        "q": "What was the title of the acclaimed dramatic episode where T.J. is groomed online by an adult predator pretending to be a kid?",
        "correct": "Never Too Young",
        "distractors": ["Stranger in the Chat", "Web of Lies", "Dangerous Net"],
        "d": 3
    },
    {
        "q": "What bizarre culinary habit characterized Mo Tibbs on Smart Guy?",
        "correct": "Inventing bizarre junk food combinations and devouring everything in the Henderson kitchen",
        "distractors": ["Only eating foods that were colored bright green", "Sprinkling hot sauce on ice cream sundaes", "Eating raw onion sandwiches before dates"],
        "d": 2
    },
    {
        "q": "Who was Yvette's eccentric drama teacher at Piedmont High, played by Dann Florek in recurring appearances?",
        "correct": "Mr. Bellows",
        "distractors": ["Mr. Feeny", "Mr. Turner", "Mr. Dixon"],
        "d": 3
    },
    {
        "q": "What sports team did Marcus and Mo play for at Piedmont High?",
        "correct": "Varsity Basketball",
        "distractors": ["Varsity Football", "Track and Field", "Varsity Baseball"],
        "d": 2
    },
    {
        "q": "In what U.S. metropolitan area was Smart Guy set?",
        "correct": "Washington, D.C.",
        "distractors": ["Philadelphia, Pennsylvania", "Atlanta, Georgia", "Baltimore, Maryland"],
        "d": 1
    },

    # Clarissa Explains It All, City Guys, USA High (15 questions)
    {
        "q": "Which actress launched her television career starring as Clarissa Darling on Nickelodeon's Clarissa Explains It All?",
        "correct": "Melissa Joan Hart",
        "distractors": ["Larisa Oleynik", "Amanda Bynes", "Christine Taylor"],
        "d": 1
    },
    {
        "q": "How did Clarissa's best friend Sam Oliver (Sean O'Neal) habitually enter her second-story bedroom?",
        "correct": "Climbing up a ladder propped outside her window to the sound of an electric guitar twang",
        "distractors": ["Swinging in from an adjacent oak tree branch", "Climbing up a trellis of ivy vines", "Using a grappling hook and rope"],
        "d": 1
    },
    {
        "q": "What was the name of Clarissa's annoying, money-obsessed, Young Republican younger brother?",
        "correct": "Ferguson Darling (Jason Zimbler)",
        "distractors": ["Quinn Darling", "Tucker Darling", "Preston Darling"],
        "d": 1
    },
    {
        "q": "What pet reptile lived in a kiddy pool inside Clarissa Darling's bedroom?",
        "correct": "A baby caiman/alligator named Elvis",
        "distractors": ["An iguana named Godzilla", "A chameleon named Rango", "A python named Monty"],
        "d": 1
    },
    {
        "q": "What creative computer activity did Clarissa use to solve everyday teen dilemmas on her desktop computer?",
        "correct": "Programming interactive 8-bit video games simulating her problems",
        "distractors": ["Writing a satirical anonymous blog", "Creating digital comic book animations", "Designing fashion runway outfits"],
        "d": 1
    },
    {
        "q": "What historical programming distinction does Clarissa Explains It All hold for Nickelodeon?",
        "correct": "It was the first live-action series on Nickelodeon to feature a female protagonist lead",
        "distractors": ["It was the first series broadcast in color on the network", "It was the first series to air in prime-time syndication", "It was the network's first live-audience four-camera sitcom"],
        "d": 2
    },
    {
        "q": "What health-food obsession did Clarissa's mother Janet Darling inflict upon the family?",
        "correct": "Cooking bizarre vegetarian recipes featuring tofu, wheat germ, and raw cabbage",
        "distractors": ["Insisting on an all-grapefruit liquid cleanse diet", "Serving powdered protein sludge shakes for dinner", "Fermenting seaweed casseroles"],
        "d": 2
    },
    {
        "q": "What was the architectural profession of Clarissa's father Marshall Darling (Joe O'Connor)?",
        "correct": "Architect designing eccentric, oddly shaped buildings",
        "distractors": ["Civil engineer building suspension bridges", "Landscape designer for theme parks", "Interior decorator for museums"],
        "d": 2
    },
    {
        "q": "What high school setting provided the backdrop for NBC's Saturday morning teen series City Guys?",
        "correct": "Manhattan High School in New York City",
        "distractors": ["Brooklyn Heights Prep", "Queens Vocational High", "Empire State Academy"],
        "d": 2
    },
    {
        "q": "What was the central dynamic of the two male leads, Chris Anderson and Jamal Grant, on City Guys?",
        "correct": "A wealthy white teen from Park Avenue and a working-class Black teen from Harlem who become close friends",
        "distractors": ["Two rival basketball stars competing for a single Division 1 college scholarship", "Two graffiti artists turned campus newspaper photojournalists", "Two cousins from Chicago who move in with their aunt in Manhattan"],
        "d": 2
    },
    {
        "q": "What was the universal dismissal catchphrase used by the teens on City Guys?",
        "correct": "C-ya!",
        "distractors": ["Later!", "Peace out!", "Word!"],
        "d": 2
    },
    {
        "q": "What was the international boarding school setting for the Peter Engel TNBC sitcom USA High?",
        "correct": "An American academy in Paris, France",
        "distractors": ["An international prep school in Geneva, Switzerland", "An American boarding school in London, England", "A diplomat children's school in Rome, Italy"],
        "d": 2
    },
    {
        "q": "Who was the stern, dignified headmaster of USA High, played by veteran character actor Nicholas Pryor?",
        "correct": "Mr. Elliott",
        "distractors": ["Mr. Belding", "Mr. Roman", "Mr. Dupree"],
        "d": 2
    },
    {
        "q": "What was the name of the eccentric, girl-crazy German student who was part of the core friend group on USA High?",
        "correct": "Christian Schrader (Thomas Magiar)",
        "distractors": ["Hans Gruber", "Klaus Zimmerman", "Dieter Müller"],
        "d": 2
    },
    {
        "q": "What American diner-style cafe in Paris served as the primary student hangout on USA High?",
        "correct": "The Eiffel Cafe",
        "distractors": ["The Paris Diner", "Cafe Max", "The French Fry"],
        "d": 3
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "staging", "90s_sitcoms_batch5.json")
    make_batch(q_batch5, 5, out)
