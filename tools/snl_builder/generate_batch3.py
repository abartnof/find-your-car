#!/usr/bin/env python3
"""
Generate SNL Batch 3: 2010s to Season 50 Sketches, Shorts & Characters (2010-present)
100 questions: exactly 30 d1, 40 d2, 30 d3.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from builder import build_batch

questions = [
    # 1
    {
        "q": "What recurring character played by Bill Hader served as Weekend Update's flamboyant New York City city correspondent?",
        "correct": "Stefon",
        "distractors": ["Anthony Peter Coleman", "Devin", "Herb Welch"],
        "d": 1
    },
    # 2
    {
        "q": "What physical gesture did Bill Hader famously do as Stefon because he was trying to hide his genuine laughter at rewritten cue cards?",
        "correct": "Covering his mouth with both hands",
        "distractors": ["Ducking under the Weekend Update desk", "Taking off his oversized sunglasses", "Burying his head in a folder"],
        "d": 1
    },
    # 3
    {
        "q": "Which former SNL writer and stand-up comedian co-created Stefon and routinely changed the cue-card jokes right before the live broadcast to break Bill Hader?",
        "correct": "John Mulaney",
        "distractors": ["Colin Jost", "Michael Che", "Seth Meyers"],
        "d": 1
    },
    # 4
    {
        "q": "What 1990s MTV personality was frequently referenced by Stefon as a bizarre club fixture ('This place has everything... and MTV's...')?",
        "correct": "Dan Cortese",
        "distractors": ["Pauly Shore", "Bill Bellamy", "Kennedy"],
        "d": 2
    },
    # 5
    {
        "q": "In Stefon's nightlife guides, what was a 'human fire hydrant' defined as?",
        "correct": "A midget who sprays water out of his mouth",
        "distractors": ["A bouncer who wears red and stands on one foot", "A bartender who puts out flaming shots", "A dancer painted bright yellow"],
        "d": 2
    },
    # 6
    {
        "q": "In the 2016 Halloween sketch 'Haunted Elevator', what mysterious character played by Tom Hanks bewildered riders with his skeleton sidekicks?",
        "correct": "David S. Pumpkins",
        "distractors": ["Johnny B. Ghoulish", "Captain Jack O'Lantern", "Bones Montgomery"],
        "d": 1
    },
    # 7
    {
        "q": "What was David S. Pumpkins' signature catchphrase whenever the riders asked who he was supposed to be?",
        "correct": "Any questions?",
        "distractors": ["Ready or not!", "Trick or treat!", "Who wants candy?"],
        "d": 1
    },
    # 8
    {
        "q": "Which two cast members played the breakdancing skeleton sidekicks flanking David S. Pumpkins?",
        "correct": "Mikey Day and Bobby Moynihan",
        "distractors": ["Pete Davidson and Beck Bennett", "Colin Jost and Michael Che", "Kyle Mooney and Beck Bennett"],
        "d": 2
    },
    # 9
    {
        "q": "In the recurring sketch 'Close Encounter', which chain-smoking character played by Kate McKinnon gave wildly vulgar accounts of alien abductions?",
        "correct": "Ms. Colleen Rafferty",
        "distractors": ["Mrs. Brenda Johnson", "Donna DeMarco", "Sandy Glazer"],
        "d": 1
    },
    # 10
    {
        "q": "Which A-list guest host broke down in uncontrollable laughter opposite Kate McKinnon in the premiere 'Close Encounter' sketch in December 2015?",
        "correct": "Ryan Gosling",
        "distractors": ["Bradley Cooper", "Adam Driver", "Chris Pine"],
        "d": 1
    },
    # 11
    {
        "q": "In the original 'Close Encounter' sketch, how did Colleen Rafferty describe her experience while her fellow abductees experienced spiritual enlightenment?",
        "correct": "Getting dropped onto a roof with no pants and having her 'coot-coot' examined",
        "distractors": ["Being forced to eat space oatmeal through a funnel", "Having her memories erased by a laser beam", "Being kept in a jar filled with blue slime"],
        "d": 2
    },
    # 12
    {
        "q": "In 'The Californians' soap opera parody, what topic dominated all of the characters' dramatic interpersonal conversations?",
        "correct": "Driving directions and Southern California highway routes",
        "distractors": ["Organic grocery store sales", "Real estate square footage", "Plastic surgery procedures"],
        "d": 1
    },
    # 13
    {
        "q": "What physical routine did Fred Armisen, Kristen Wiig, and Bill Hader perform between dramatic lines in 'The Californians'?",
        "correct": "Staring dramatically into mirrors while speaking in exaggerated vocal fry",
        "distractors": ["Lighting skinny cigarettes on balconies", "Sipping green juice through bamboo straws", "Checking their reflections in sunglasses"],
        "d": 2
    },
    # 14
    {
        "q": "What was the name of Fred Armisen's blonde, sun-drenched patriarch character on 'The Californians'?",
        "correct": "Stuart",
        "distractors": ["Devin", "Chad", "Trey"],
        "d": 2
    },
    # 15
    {
        "q": "Who hosts the recurring game show 'Black Jeopardy!' on SNL?",
        "correct": "Kenan Thompson as Darnell Hayes",
        "distractors": ["Tracy Morgan as Brian Fellow", "Jay Pharoah as Shannon Sharpe", "Michael Che as Lester Holt"],
        "d": 1
    },
    # 16
    {
        "q": "In a critically acclaimed 2016 'Black Jeopardy!' sketch, which guest host played Doug, a MAGA-hat-wearing contestant who bonded with Darnell Hayes?",
        "correct": "Tom Hanks",
        "distractors": ["Woody Harrelson", "Steve Martin", "Bryan Cranston"],
        "d": 1
    },
    # 17
    {
        "q": "In the 2018 'Black Jeopardy!' sketch starring Chadwick Boseman as Marvel's King T'Challa, what did T'Challa answer when asked what Karen brought to the cookout?",
        "correct": "Potato salad with raisins",
        "distractors": ["Dry unseasoned chicken", "Store-bought macaroni salad", "Sparkling water"],
        "d": 2
    },
    # 18
    {
        "q": "What monosyllabic response did Pete Davidson's character Chad give to virtually every life-or-death situation, confession, or threat?",
        "correct": "Okay.",
        "distractors": ["Cool.", "Whatever.", "Sure."],
        "d": 1
    },
    # 19
    {
        "q": "In a 2018 episode hosted by John Mulaney, what Broadway musical was parodied when a customer committed the cardinal sin of ordering lobster at a Greek diner?",
        "correct": "Les Misérables",
        "distractors": ["The Phantom of the Opera", "Sweeney Todd", "West Side Story"],
        "d": 1
    },
    # 20
    {
        "q": "In John Mulaney's 'Diner Lobster' sketch, who emerged from a tank dressed in a giant lobster costume singing 'Who Am I?'?",
        "correct": "Kenan Thompson",
        "distractors": ["Beck Bennett", "Pete Davidson", "Bobby Moynihan"],
        "d": 2
    },
    # 21
    {
        "q": "Following 'Diner Lobster', John Mulaney hosted several more NYC-themed musical parodies. Which sketch parodied 'Willy Wonka & the Chocolate Factory'?",
        "correct": "Bodega Bathroom",
        "distractors": ["Airport Sushi", "Subway Churro", "LaGuardia Kiosk"],
        "d": 2
    },
    # 22
    {
        "q": "What comedy trio joined SNL in Season 47 (2021) as writers and starred in their own surreal pre-taped digital videos?",
        "correct": "Please Don't Destroy",
        "distractors": ["The Lonely Island", "Good Neighbor", "The Whitest Kids U' Know"],
        "d": 1
    },
    # 23
    {
        "q": "What are the first names of the three members of Please Don't Destroy?",
        "correct": "Ben, John, and Martin",
        "distractors": ["Andy, Akiva, and Jorma", "Kyle, Beck, and Nick", "Colin, Michael, and Kent"],
        "d": 2
    },
    # 24
    {
        "q": "Which pop megastar joined Please Don't Destroy and Pete Davidson for the viral 2021 music video 'Three Sad Virgins'?",
        "correct": "Taylor Swift",
        "distractors": ["Billie Eilish", "Dua Lipa", "Olivia Rodrigo"],
        "d": 1
    },
    # 25
    {
        "q": "On Weekend Update, what tragic historical object did Bowen Yang portray as a defiant, fame-seeking diva promoting a debut album?",
        "correct": "The Iceberg that sank the Titanic",
        "distractors": ["The Hindenburg Blimp", "The Trojan Horse", "The Liberty Bell"],
        "d": 1
    },
    # 26
    {
        "q": "What was the iceberg's fiery defense when Colin Jost accused it of sinking the Titanic?",
        "correct": "You came to where I live and you hit ME!",
        "distractors": ["I was minding my business in the fog!", "Water seeks water, baby!", "Ice expands when it freezes!"],
        "d": 2
    },
    # 27
    {
        "q": "Which internet-famous animal did Bowen Yang portray on Weekend Update in Season 50, delivering a dramatic monologue on celebrity burnout?",
        "correct": "Moo Deng the baby pygmy hippo",
        "distractors": ["Pesto the giant king penguin chick", "Harambe the gorilla", "Fiona the Cincinnati hippo"],
        "d": 2
    },
    # 28
    {
        "q": "What was the name of Ego Nwodim's wildly popular character who ordered an extra-well-done steak and shook the entire table violently trying to cut it?",
        "correct": "Lisa from Temecula",
        "distractors": ["Kim from Bakersfield", "Ashley from Fresno", "Tonya from Modesto"],
        "d": 1
    },
    # 29
    {
        "q": "What catchphrase did Lisa from Temecula shout at offended dinner guests who asked her to stop shaking the table?",
        "correct": "Cook my meat!",
        "distractors": ["Mind your plate!", "It's well done, baby!", "Let a sister eat!"],
        "d": 1
    },
    # 30
    {
        "q": "Which guest host broke into uncontrollable giggles while seated next to Ego Nwodim during the debut 'Lisa from Temecula' sketch?",
        "correct": "Pedro Pascal",
        "distractors": ["Austin Butler", "Michael B. Jordan", "Woody Harrelson"],
        "d": 2
    },
    # 31
    {
        "q": "In a celebrated 2023 sketch, host Nate Bargatze played George Washington crossing the Delaware dreaming of what uniquely American system?",
        "correct": "American units of measurement and spelling (gallons, feet, pounds)",
        "distractors": ["The electoral college system", "The two-party political system", "American fast food breakfast menus"],
        "d": 2
    },
    # 32
    {
        "q": "In Nate Bargatze's 'Washington's Dream', what did George Washington declare would be measured in gallons instead of liters?",
        "correct": "Liquid, but only certain liquids like milk and gasoline",
        "distractors": ["Only tea dumped into the harbor", "Only rainwater and whiskey", "Maple syrup and cider"],
        "d": 3
    },
    # 33
    {
        "q": "Who portrayed Kamala Harris on SNL throughout the 2020 election cycle and returned to play her in Season 50 (2024)?",
        "correct": "Maya Rudolph",
        "distractors": ["Cecily Strong", "Ego Nwodim", "Sasheer Zamata"],
        "d": 1
    },
    # 34
    {
        "q": "What nickname did Maya Rudolph's Kamala Harris bestow upon herself as America's cool stepmother?",
        "correct": "The 'Funt' (Fun Aunt)",
        "distractors": ["Auntie Kam", "The Momala", "The Cool Veep"],
        "d": 2
    },
    # 35
    {
        "q": "Which SNL alumnus returned in Season 50 to portray President Joe Biden during the 2024 campaign sketches?",
        "correct": "Dana Carvey",
        "distractors": ["Jason Sudeikis", "Kevin Nealon", "Bill Murray"],
        "d": 1
    },
    # 36
    {
        "q": "Which stand-up comedian was brought in during Season 50 to portray vice presidential nominee Tim Walz?",
        "correct": "Jim Gaffigan",
        "distractors": ["John Mulaney", "Nate Bargatze", "Bill Burr"],
        "d": 2
    },
    # 37
    {
        "q": "Which former cast member returned to portray Second Gentleman Doug Emhoff in Season 50 alongside Maya Rudolph's Kamala Harris?",
        "correct": "Andy Samberg",
        "distractors": ["Jimmy Fallon", "Seth Meyers", "Jason Sudeikis"],
        "d": 2
    },
    # 38
    {
        "q": "Who hosted the landmark Season 50 premiere of Saturday Night Live on September 28, 2024?",
        "correct": "Jean Smart",
        "distractors": ["Steve Martin", "Tom Hanks", "John Mulaney"],
        "d": 2
    },
    # 39
    {
        "q": "Who was the musical guest on the Season 50 premiere episode on September 28, 2024?",
        "correct": "Jelly Roll",
        "distractors": ["Chappell Roan", "Billie Eilish", "Coldplay"],
        "d": 2
    },
    # 40
    {
        "q": "What recurring character played by Cecily Strong lived in the apartment below Weekend Update and yelled gossip through the floor?",
        "correct": "Cathy Anne",
        "distractors": ["Gemma", "Donna Pescow", "Colleen Rafferty"],
        "d": 2
    },
    # 41
    {
        "q": "What prop did Cecily Strong's character Cathy Anne always hold in her hand while appearing on Weekend Update?",
        "correct": "An unlit cigarette",
        "distractors": ["A can of cheap beer", "A flyswatter", "A lottery ticket scratcher"],
        "d": 2
    },
    # 42
    {
        "q": "What prop did Cecily Strong as Fox News host Jeanine Pirro repeatedly spill all over Colin Jost on Weekend Update?",
        "correct": "A large goblet of red wine",
        "distractors": ["A mug of scalding black coffee", "A bowl of chili", "A pitcher of martinis"],
        "d": 2
    },
    # 43
    {
        "q": "In Cecily Strong's final episode as a cast member in December 2022, what Frank Sinatra classic did host Austin Butler and the cast serenade her with?",
        "correct": "Blue Christmas",
        "distractors": ["My Way", "New York, New York", "That's Life"],
        "d": 3
    },
    # 44
    {
        "q": "What was the name of Aidy Bryant and Cecily Strong's recurring sketch about middle-schoolers hosting an amateur talk show?",
        "correct": "Girlfriends Talk Show",
        "distractors": ["Teen Talk Express", "Locker Room Live", "Middle School Confidential"],
        "d": 2
    },
    # 45
    {
        "q": "In 'Girlfriends Talk Show', who was Kyra's older, troubled high-school boyfriend who Morgan openly disliked?",
        "correct": "Aaron",
        "distractors": ["Cody", "Derek", "Trevor"],
        "d": 2
    },
    # 46
    {
        "q": "What was the title of Beck Bennett and Kyle Mooney's recurring public access parody set in Southern California skate culture?",
        "correct": "Inside SoCal",
        "distractors": ["San Diego Vibe", "Beach Boys Live", "Venice Skate Report"],
        "d": 2
    },
    # 47
    {
        "q": "Who portrayed White House Press Secretary Sean Spicer in multiple viral Season 42 sketches, operating a motorized motorized podium?",
        "correct": "Melissa McCarthy",
        "distractors": ["Kate McKinnon", "Aidy Bryant", "Kristen Wiig"],
        "d": 1
    },
    # 48
    {
        "q": "What prop did Melissa McCarthy's Sean Spicer use to ram and intimidate White House correspondents during press briefings?",
        "correct": "A motorized lectern / podium",
        "distractors": ["A fire hose", "A heavy megaphone", "A golf cart"],
        "d": 1
    },
    # 49
    {
        "q": "In the cold open of the post-2016 presidential election episode, Kate McKinnon sat at a solo piano dressed as Hillary Clinton and sang which Leonard Cohen anthem?",
        "correct": "Hallelujah",
        "distractors": ["Tower of Song", "Bird on the Wire", "Famous Blue Raincoat"],
        "d": 2
    },
    # 50
    {
        "q": "What line did Kate McKinnon deliver tearfully to camera after concluding 'Hallelujah' following the 2016 election?",
        "correct": "I'm not giving up, and neither should you.",
        "distractors": ["God bless America.", "Until next time.", "Keep moving forward."],
        "d": 2
    },
    # 51
    {
        "q": "In the recurring sketch 'Undercover Boss: Starkiller Base', which Star Wars villain did Adam Driver play masquerading as radar technician 'Matt'?",
        "correct": "Kylo Ren",
        "distractors": ["Darth Vader", "General Hux", "Supreme Leader Snoke"],
        "d": 1
    },
    # 52
    {
        "q": "In 'Undercover Boss: Starkiller Base', what did Adam Driver's Matt repeatedly boast about Kylo Ren having in the employee break room?",
        "correct": "An eight-pack (being shredded)",
        "distractors": ["The fastest ship in the galaxy", "A private gold lightsaber", "Black belts in five martial arts"],
        "d": 2
    },
    # 53
    {
        "q": "What was the title of the 2016 pre-taped digital sketch parodying Beyoncé's album 'Lemonade' with Melania Trump, Kellyanne Conway, and Ivanka Trump?",
        "correct": "Melanianade",
        "distractors": ["Lemonade 30 Rock", "First Lady Formation", "Pray You Catch Me Melania"],
        "d": 3
    },
    # 54
    {
        "q": "Which cast member was known for her celebrity impressions of Drew Barrymore, Jennifer Coolidge, and Britney Spears?",
        "correct": "Chloe Fineman",
        "distractors": ["Heidi Gardner", "Ego Nwodim", "Punkie Johnson"],
        "d": 2
    },
    # 55
    {
        "q": "What recurring Weekend Update character played by Heidi Gardner was an Instagram influencer who offered terrible dating advice?",
        "correct": "Angel, Every Boxer's Girlfriend from Every Movie About Boxing",
        "distractors": ["Brie from Soho", "Jessica from Scottsdale", "Chloe the Wellness Guru"],
        "d": 2
    },
    # 56
    {
        "q": "What tragic refrain did Heidi Gardner's 'Every Boxer's Girlfriend' repeat whenever Tommy fought in the ring?",
        "correct": "I'm taking the kids to my sister's!",
        "distractors": ["Don't you get knocked out!", "Think of our future!", "You promised me this was the last round!"],
        "d": 2
    },
    # 57
    {
        "q": "In a 2015 sketch, what dramatic teen musical did the SNL cast spoof when host Lin-Manuel Miranda visited?",
        "correct": "High School Musical / Hamilton parodies",
        "distractors": ["Dear Evan Hansen", "Wicked", "Glee"],
        "d": 3
    },
    # 58
    {
        "q": "What was the name of Bobby Moynihan's beloved, slovenly Weekend Update character who wore a stained nightshirt and spewed nonsense from secondhand sources?",
        "correct": "Drunk Uncle",
        "distractors": ["Cousin Sal", "Angry Grandpa", "Bad Uncle Dave"],
        "d": 1
    },
    # 59
    {
        "q": "What song lyrics did Drunk Uncle repeatedly sing under his breath whenever he got wistful about the past?",
        "correct": "Lyrics from various pop and classic rock hits like 'Somebody That I Used to Know'",
        "distractors": ["American Pie", "Born in the USA", "Free Bird"],
        "d": 2
    },
    # 60
    {
        "q": "What was the name of the sweet, nervous 13-year-old boy played by Bobby Moynihan who read a prepared speech from a crumpled cue card on Weekend Update?",
        "correct": "Jacob the Bar Mitzvah Boy",
        "distractors": ["Eli the Yeshiva Student", "Sammy the Junior Scout", "Benny the Altar Boy"],
        "d": 1
    },
    # 61
    {
        "q": "What formulaic joke structure did Jacob the Bar Mitzvah Boy deliver before pausing for Colin Jost's awkward laugh?",
        "correct": "A pun-based dad joke followed by looking down at his paper and clearing his throat",
        "distractors": ["A magic trick using a silver coin", "A knock-knock joke from a greeting card", "A limerick about his rabbi"],
        "d": 2
    },
    # 62
    {
        "q": "What was the title of the viral 2012 pre-taped music video starring cast women singing an anthem about having a 'back-home baller' lifestyle during Thanksgiving?",
        "correct": "Back Home Ballers",
        "distractors": ["Hometown Queens", "Thanksgiving Divas", "Suburban Holiday"],
        "d": 2
    },
    # 63
    {
        "q": "In the music video 'Back Home Ballers', what luxury perk did the women brag about having at their parents' house?",
        "correct": "A bowl of whole bowls of chips and customized bowls",
        "distractors": ["Their own personal chauffeur", "An Olympic swimming pool", "Free valet parking"],
        "d": 3
    },
    # 64
    {
        "q": "Which host appeared in the pre-taped short 'Grouch' (2019), a gritty, R-rated Scorsese-style origin story of Oscar the Grouch?",
        "correct": "David Harbour",
        "distractors": ["Joaquin Phoenix", "Willem Dafoe", "Adam Driver"],
        "d": 2
    },
    # 65
    {
        "q": "Which SNL cast member was famous for his impression of Barack Obama from 2012 to 2016?",
        "correct": "Jay Pharoah",
        "distractors": ["Kenan Thompson", "Finesse Mitchell", "Dean Edwards"],
        "d": 2
    },
    # 66
    {
        "q": "Who portrayed President Barack Obama prior to Jay Pharoah from 2008 to 2012?",
        "correct": "Fred Armisen",
        "distractors": ["Darrell Hammond", "Will Forte", "Horatio Sanz"],
        "d": 2
    },
    # 67
    {
        "q": "What eccentric singing trio did Cecily Strong, Kate McKinnon, and guest hosts play who sang bizarre doo-wop songs to soldiers in WWII?",
        "correct": "The De-Maio Sisters / USO Show Girls",
        "distractors": ["The Andrews Homage", "The Manhattan Sisters", "The Liberty Darlings"],
        "d": 3
    },
    # 68
    {
        "q": "In a 2018 episode hosted by Donald Glover, what 1980s music video was parodied where a band member can't stop playing a 30-minute keyboard solo?",
        "correct": "Oran 'Juice' Jones / 80s R&B slow jam",
        "distractors": ["Careless Whisper", "Purple Rain", "Sweet Child O' Mine"],
        "d": 3
    },
    # 69
    {
        "q": "What sketch starring Pedro Pascal and Marcello Hernandez became a viral TikTok hit about an overprotective mother refusing to let her son date?",
        "correct": "Protective Mom (Mama Flores)",
        "distractors": ["Abuela's House", "Miami Family Dinner", "Sunday Sancocho"],
        "d": 2
    },
    # 70
    {
        "q": "What snack item did Marcello Hernandez and Pedro Pascal offer to guest Chloe Fineman in the 'Protective Mom' sketch?",
        "correct": "Hot chips (Takis)",
        "distractors": ["Empanadas", "Plantain chips", "Churros"],
        "d": 3
    },
    # 71
    {
        "q": "What was the name of the recurring 2010s sketch starring Taran Killam as a pompous 19th-century theater critic who reviewed modern movies?",
        "correct": "Jebidiah Atkinson",
        "distractors": ["Archibald Vance", "Cornelius Crump", "Ebenezer Quirk"],
        "d": 2
    },
    # 72
    {
        "q": "What dismissive sound and action did Jebidiah Atkinson make before slamming down his index cards on Weekend Update?",
        "correct": "NEXT!",
        "distractors": ["TRASH!", "RUBBISH!", "BALDERDASH!"],
        "d": 2
    },
    # 73
    {
        "q": "In the 2021 episode hosted by Kim Kardashian, what satirical legal drama featured her as an attorney who represented famous socialites?",
        "correct": "The People's Kourt",
        "distractors": ["Judge Kim", "Calabasas Court", "Kardashian Law"],
        "d": 2
    },
    # 74
    {
        "q": "What was the title of the 2014 music video starring cast members and host Woody Harrelson rapping about pot-smoking New Yorkers trying to obtain weed legally?",
        "correct": "Camp X-Ray / The New York City Weed Laws",
        "distractors": ["Legalize It 8H", "Brooklyn Dispensary", "The Dime Bag"],
        "d": 3
    },
    # 75
    {
        "q": "What iconic 1980s synth-pop song was featured in the 2019 sketch where Will Ferrell and Cecily Strong played vents at an upscale Italian restaurant?",
        "correct": "'Cinema' / 80s Europop",
        "distractors": ["Blue Monday", "Take On Me", "Never Gonna Give You Up"],
        "d": 3
    },
    # 76
    {
        "q": "What recurring gameshow sketch featured host Bill Hader as Vince Blight asking contestants trivia about their own families that they shockingly failed?",
        "correct": "What's That Name?",
        "distractors": ["Name That Relative", "Who Is That Person?", "Family Blunder"],
        "d": 2
    },
    # 77
    {
        "q": "In the 'What's That Name?' sketch featuring host John Mulaney, what everyday person's name could Mulaney's character not remember?",
        "correct": "His own doorman of ten years",
        "distractors": ["His mother-in-law", "His primary care physician", "His child's pediatrician"],
        "d": 3
    },
    # 78
    {
        "q": "Which pop superstar pulled double duty as host and musical guest in 2024 and performed the hit song 'Espresso'?",
        "correct": "Sabrina Carpenter (musical guest) / Ariana Grande (double duty)",
        "distractors": ["Billie Eilish", "Dua Lipa", "Olivia Rodrigo"],
        "d": 2
    },
    # 79
    {
        "q": "In 2024, which host broke the internet playing a mom in a sketch celebrating the Charli XCX 'Brat summer' trend?",
        "correct": "Maya Rudolph / Bowen Yang",
        "distractors": ["Kristen Wiig", "Ayo Edebiri", "Sydney Sweeney"],
        "d": 3
    },
    # 80
    {
        "q": "What was the title of the viral 2016 sketch where Cecily Strong and Sasheer Zamata sang about the election in 'Girl at a Bar'?",
        "correct": "A Girl's Halloween / Election Bar",
        "distractors": ["Bar Talk 2016", "Night Out", "Ladies First"],
        "d": 3
    },
    # 81
    {
        "q": "Who played Donald Trump on SNL from autumn 2016 through the end of Trump's presidency in 2020?",
        "correct": "Alec Baldwin",
        "distractors": ["Darrell Hammond", "Taran Killam", "James Austin Johnson"],
        "d": 1
    },
    # 82
    {
        "q": "Which current cast member took over the impression of Donald Trump in 2021, earning wide praise for his stream-of-consciousness delivery?",
        "correct": "James Austin Johnson",
        "distractors": ["Michael Longfellow", "Marcello Hernandez", "Devon Walker"],
        "d": 1
    },
    # 83
    {
        "q": "In James Austin Johnson's Trump impression, what pop culture franchise did he frequently wander into discussing during campaign rallies?",
        "correct": "Pokémon and Marvel movies",
        "distractors": ["Game of Thrones", "Harry Potter", "The Lord of the Rings"],
        "d": 2
    },
    # 84
    {
        "q": "What was the name of the recurring 2020s sketch starring Mikey Day and Heidi Gardner as an old-time soap opera couple interrupted by ridiculous stagecraft?",
        "correct": "The Dionne Warwick Talk Show",
        "distractors": ["The Golden Years", "Sunset Romance", "Daytime Drama"],
        "d": 3
    },
    # 85
    {
        "q": "Who portrayed legendary singer Dionne Warwick in the recurring 'Dionne Warwick Talk Show' sketches?",
        "correct": "Ego Nwodim",
        "distractors": ["Sasheer Zamata", "Leslie Jones", "Punkie Johnson"],
        "d": 2
    },
    # 86
    {
        "q": "Which actual celebrity appeared on the 'Dionne Warwick Talk Show' to be interviewed by Ego Nwodim as herself?",
        "correct": "Dionne Warwick",
        "distractors": ["Diana Ross", "Aretha Franklin", "Gladys Knight"],
        "d": 2
    },
    # 87
    {
        "q": "What sketch starring Kenan Thompson and Chris Redd featured a fake courtroom show about rappers on trial for incriminating music video lyrics?",
        "correct": "Rap Lyrics on Trial",
        "distractors": ["Hip Hop Justice", "Courtroom Cypher", "Beats and Bars"],
        "d": 3
    },
    # 88
    {
        "q": "In a celebrated Season 49 sketch, who hosted and played a delightfully weird dad attending an orientation for his son's community theater?",
        "correct": "Josh Brolin",
        "distractors": ["Rami Malek", "Willem Dafoe", "Paul Rudd"],
        "d": 3
    },
    # 89
    {
        "q": "What sketch series featured Kate McKinnon as eccentric former German Chancellor Angela Merkel visiting Weekend Update?",
        "correct": "Angela Merkel on Weekend Update",
        "distractors": ["Chancellor Chat", "European Union Live", "Berlin Dispatch"],
        "d": 2
    },
    # 90
    {
        "q": "What was Angela Merkel's secret recurring romantic crush on Weekend Update?",
        "correct": "Barack Obama",
        "distractors": ["Colin Jost", "Justin Trudeau", "Emmanuel Macron"],
        "d": 2
    },
    # 91
    {
        "q": "What was the title of the 2013 sketch starring Kerry Washington where SNL poked fun at its lack of Black female cast members at the time?",
        "correct": "White House cold open addressing diversity",
        "distractors": ["The Kerry Washington Show", "Diversity 101", "Cast Auditions 2013"],
        "d": 3
    },
    # 92
    {
        "q": "Which Black female comedian was hired mid-season in January 2014 following the public controversy over representation?",
        "correct": "Sasheer Zamata",
        "distractors": ["Leslie Jones", "Ego Nwodim", "Punkie Johnson"],
        "d": 2
    },
    # 93
    {
        "q": "Who portrayed eccentric White House advisor Kellyanne Conway in the 2017 'It' horror movie parody 'Kellyanne Conway in the Sewer'?",
        "correct": "Kate McKinnon",
        "distractors": ["Cecily Strong", "Aidy Bryant", "Vanessa Bayer"],
        "d": 2
    },
    # 94
    {
        "q": "What was the character name of Vanessa Bayer's awkward former child star who appeared on Weekend Update to promote low-budget commercials?",
        "correct": "Laura Parsons",
        "distractors": ["Dawn Lazarus", "Rebecca Stern", "Piper Reese"],
        "d": 3
    },
    # 95
    {
        "q": "What was the signature speech quirk of Vanessa Bayer's Weekend Update meteorologist character Dawn Lazarus?",
        "correct": "Mumbling panicked, garbled nonsense when the teleprompter failed",
        "distractors": ["Shouting storm warnings into a megaphone", "Singing Broadway tunes during cold fronts", "Crying whenever it started to rain"],
        "d": 2
    },
    # 96
    {
        "q": "What was the name of Beck Bennett's recurring sketch character who was a full-grown corporate CEO with the body and motor skills of a baby?",
        "correct": "Baby Boss (Mr. Patterson)",
        "distractors": ["Toddler Exec", "Infant Inc.", "Tiny Tycoon"],
        "d": 2
    },
    # 97
    {
        "q": "In a 2019 pre-taped digital short, what toy doll for little girls was advertised as just having a plastic bowl of water to wash tiny clothes in?",
        "correct": "The Sink",
        "distractors": ["The Sponge", "The Faucet", "The Dishpan"],
        "d": 3
    },
    # 98
    {
        "q": "What was the title of the 2021 pre-taped country music song starring Aidy Bryant and host Carey Mulligan about small-town women bonding?",
        "correct": "Sisterhood Anthem / Bottom of Your Face",
        "distractors": ["Nashville Girls", "Honky Tonk Sisters", "Down Home Divas"],
        "d": 3
    },
    # 99
    {
        "q": "In a classic 2012 sketch, what did host Louis C.K. play as a 19th-century Abraham Lincoln look-alike in a gritty sitcom?",
        "correct": "Lincoln (Louie parody)",
        "distractors": ["Gettysburg Dad", "Abe in the City", "Emancipation Louie"],
        "d": 3
    },
    # 100
    {
        "q": "Who played George Santos on SNL during his high-profile congressional expulsion in late 2023?",
        "correct": "Bowen Yang",
        "distractors": ["Marcello Hernandez", "Colin Jost", "James Austin Johnson"],
        "d": 1
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "staging", "snl_batch3.json")
    build_batch(questions, out, batch_num=3)
