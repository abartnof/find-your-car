import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from utils import assemble_batch, save_json

raw_questions = [
    # --- NORM PETERSON (1-25) ---
    {
        "q": "What is Norm Peterson's iconic permanent seat in Cheers?",
        "correct": "The barstool at the corner near the entrance of the bar",
        "wrong": ["The leather booth by the pool table", "The middle barstool directly in front of the tap", "The table by the front window"],
        "d": 1
    },
    {
        "q": "What does the entire bar shout in unison whenever Norm Peterson walks into Cheers?",
        "correct": "\"Norm!\"",
        "wrong": ["\"Cheers!\"", "\"Peterson!\"", "\"Beer time!\""],
        "d": 1
    },
    {
        "q": "What is the name of Norm Peterson's wife, whose face is famously never clearly seen on camera?",
        "correct": "Vera",
        "wrong": ["Loretta", "Doris", "Martha"],
        "d": 1
    },
    {
        "q": "In the Season 5 Thanksgiving episode, what covers Vera Peterson's face right before she can be seen by the audience?",
        "correct": "A thrown pumpkin pie",
        "wrong": ["A massive turkey platter", "A burst bottle of seltzer", "A bouquet of autumn flowers"],
        "d": 1
    },
    {
        "q": "What was Norm Peterson's primary profession in the early seasons of Cheers?",
        "correct": "Accountant",
        "wrong": ["Dentist", "Stockbroker", "Real estate appraiser"],
        "d": 1
    },
    {
        "q": "What second career does Norm Peterson stumble into in later seasons, often working with Woody or Cliff?",
        "correct": "House painter / interior painter",
        "wrong": ["Plumber", "Auto mechanic", "Landscape architect"],
        "d": 2
    },
    {
        "q": "What is the name of Norm's favorite, artery-clogging barbecue restaurant where 'the meat falls right off the bone'?",
        "correct": "The Hungry Heifer",
        "wrong": ["The Rusty Rib", "The Boston Brisket Barn", "Big Dan's Smokehouse"],
        "d": 2
    },
    {
        "q": "In the classic Norm entrance, Coach asks: 'What's shakin', Norm?' How does Norm reply?",
        "correct": "\"All four cheeks and a couple of chins.\"",
        "wrong": ["\"Just the ice in my glass.\"", "\"Nothing a cold beer wouldn't fix.\"", "\"My knees whenever Vera walks in.\""],
        "d": 2
    },
    {
        "q": "When Woody asks Norm: 'What's going down, Mr. Peterson?' how does Norm famously reply?",
        "correct": "\"My cheeks and my bank account.\"",
        "wrong": ["\"The sun and my morale.\"", "\"The Boston temperature.\"", "\"My hopes of going home sober.\""],
        "d": 3
    },
    {
        "q": "When Sam asks Norm: 'How's life treating you, Norm?' what is Norm's witty response?",
        "correct": "\"Like a baby treats a diaper.\"",
        "wrong": ["\"Like a dog treats a fire hydrant.\"", "\"Like a cat treats a ball of yarn.\"", "\"Like a politician treats the truth.\""],
        "d": 3
    },
    {
        "q": "When Woody asks Norm: 'Care for a beer, Mr. Peterson?' how does Norm respond?",
        "correct": "\"Does a bear sit in the woods?\"",
        "wrong": ["\"Does the sun rise in the morning?\"", "\"Is water wet, Woody?\"", "\"Do you take credit cards?\""],
        "d": 2
    },
    {
        "q": "When Woody asks: 'What's the story, Mr. Peterson?' what is Norm's summary of his life?",
        "correct": "\"Boy meets beer, boy drinks beer, boy gets another beer.\"",
        "wrong": ["\"Boy hates work, boy flees wife, boy finds tavern.\"", "\"Boy pays taxes, boy gets thirsty, boy sits down.\"", "\"Boy was born, boy bought a house, boy regretted both.\""],
        "d": 2
    },
    {
        "q": "What dream job does Norm Peterson land in Season 10 that involves drinking beer for a living?",
        "correct": "Official beer taster for the Brewster Brewery",
        "wrong": ["Quality control tester for Samuel Adams", "Draft technician for Budweiser", "Brewmaster apprentice at Boston Ale Works"],
        "d": 2
    },
    {
        "q": "Why is Norm eventually fired from his dream job as a brewery beer taster?",
        "correct": "He cannot bring himself to criticize or give a negative review to any beer",
        "wrong": ["He was caught stealing kegs from the loading dock", "He fell asleep inside a copper fermentation vat", "He was caught secretly drinking a competitor's brand"],
        "d": 3
    },
    {
        "q": "What is the name of Norm Peterson's demanding accounting firm boss who cheats on his wife?",
        "correct": "Anton Kreitzer",
        "wrong": ["Arthur Duncan", "Preston Vance", "Richard Sterling"],
        "d": 3
    },
    {
        "q": "In Season 1, what does Norm reveal about his financial debt to Cheers regarding his bar tab?",
        "correct": "He has a massive running tab that would bankrupt him if paid in full",
        "wrong": ["He secretly owns 10% of the bar's equity to cover it", "He trades free accounting services for beer", "Coach accidentally forgave his tab every Christmas"],
        "d": 3
    },
    {
        "q": "What happens when Rebecca Howe attempts to enforce payment on Norm's enormous outstanding bar tab?",
        "correct": "Norm abandons Cheers and drinks at another pub down the street",
        "wrong": ["Norm sues Cheers for predatory lending", "Norm hires a forensic accountant to audit Sam's books", "Norm stages a hunger strike outside the bar door"],
        "d": 2
    },
    {
        "q": "What is the name of the rival dive bar Norm temporarily frequents when boycotting Cheers?",
        "correct": "The Hungry Heifer (or The Blue Shamrock)",
        "wrong": ["McGinty's Pub", "The Boston Boathouse", "The Brass Rail"],
        "d": 3
    },
    {
        "q": "What is the name of the hungry basset hound / dog Norm adopts and brings into Cheers?",
        "correct": "Sammy",
        "wrong": ["Barney", "Gus", "Buster"],
        "d": 2
    },
    {
        "q": "In Season 7, why does Norm Peterson end up in traction in the hospital?",
        "correct": "He hurt his back painting Rebecca's office or lifting heavy furniture",
        "wrong": ["He fell off his high barstool during closing time", "He slipped on ice outside the Hungry Heifer", "He was tackled by an angry softball outfielder"],
        "d": 3
    },
    {
        "q": "What color did Norm Peterson once accidentally paint an entire executive office suite?",
        "correct": "A garish, nauseating neon pink / peach",
        "wrong": ["A pitch black gothic gloss", "A blinding canary yellow", "A drab camouflage olive drab"],
        "d": 3
    },
    {
        "q": "What is Norm's middle name?",
        "correct": "Hillary",
        "wrong": ["Francis", "Aloysius", "Eugene"],
        "d": 3
    },
    {
        "q": "When asked: 'What would you say to a nice cold beer, Norm?' what does Norm reply?",
        "correct": "\"Going my way?\"",
        "wrong": ["\"I love you.\"", "\"Where have you been all my life?\"", "\"Make it a double.\""],
        "d": 2
    },
    {
        "q": "What does Norm declare to be 'the best smell in the world' in multiple episodes?",
        "correct": "A freshly tapped keg of beer (or barbecue ribs)",
        "wrong": ["Freshly cut grass on opening day", "New car leather", "Freshly baked Italian pizza dough"],
        "d": 1
    },
    {
        "q": "In the series finale 'One for the Road', what does Norm state as his ultimate philosophy of life to Sam?",
        "correct": "That a person always comes back to the one true love of their life—which for Sam is Cheers",
        "wrong": ["That a man should never let work get between him and a good beer", "That happiness is simply sitting on a stool surrounded by friends", "That Boston is the greatest city on Earth"],
        "d": 1
    },

    # --- CLIFF CLAVIN (26-50) ---
    {
        "q": "What is Cliff Clavin's uniform and profession throughout all eleven seasons of Cheers?",
        "correct": "A letter carrier for the United States Postal Service",
        "wrong": ["A meter maid for the Boston Traffic Commission", "A train conductor for Amtrak", "A security guard for the Boston Museum of Fine Arts"],
        "d": 1
    },
    {
        "q": "What is Cliff Clavin's signature catchphrase used before sharing unsolicited, dubious trivia?",
        "correct": "\"It's a little-known fact...\"",
        "wrong": ["\"As common sense dictates...\"", "\"According to historical record...\"", "\"Science has clearly proven...\""],
        "d": 1
    },
    {
        "q": "With whom does Cliff Clavin live for the majority of the series?",
        "correct": "His overbearing mother, Esther Clavin",
        "wrong": ["His eccentric bachelor uncle", "Roommates from the postal distribution center", "He lives alone in a tiny studio apartment"],
        "d": 1
    },
    {
        "q": "What game show does Cliff Clavin appear on in the legendary Season 8 episode 'What Is... Cliff Clavin?'?",
        "correct": "Jeopardy!",
        "wrong": ["Wheel of Fortune", "Who Wants to Be a Millionaire", "The Price Is Right"],
        "d": 1
    },
    {
        "q": "Who hosts the game show when Cliff Clavin makes his disastrous television appearance?",
        "correct": "Alex Trebek",
        "wrong": ["Pat Sajak", "Bob Barker", "Dick Clark"],
        "d": 2
    },
    {
        "q": "What was the category for Cliff Clavin's infamous Final Jeopardy question?",
        "correct": "Final Jeopardy! category: Movies (or Famous Names)",
        "wrong": ["World Postal Routes", "Civil War Generals", "Bavarian Monarchs"],
        "d": 2
    },
    {
        "q": "What bizarre answer did Cliff Clavin write down on Final Jeopardy! that cost him his runaway lead?",
        "correct": "\"Who are three people who have never been in my kitchen?\"",
        "wrong": ["\"Who are the postal workers of America?\"", "\"What is the secret of the universe?\"", "\"Who are my mother's third cousins?\""],
        "d": 1
    },
    {
        "q": "How much money had Cliff Clavin accumulated before wagering and losing it all in Final Jeopardy?",
        "correct": "22,000 dollars",
        "wrong": ["14,500 dollars", "35,000 dollars", "8,200 dollars"],
        "d": 2
    },
    {
        "q": "What cosmetic surgery does Cliff Clavin secretly undergo in Season 4 to improve his dating life?",
        "correct": "A nose job (rhinoplasty)",
        "wrong": ["Hair plug transplants", "Teeth veneers", "Chin implant"],
        "d": 3
    },
    {
        "q": "What is the name of Cliff Clavin's fellow postal worker girlfriend who shares his eccentric personality?",
        "correct": "Margaret O'Keefe",
        "wrong": ["Brenda Walsh", "Sally Albright", "Peggy Harris"],
        "d": 2
    },
    {
        "q": "What is Cliff Clavin's mother's name?",
        "correct": "Esther Clavin",
        "wrong": ["Agnes Clavin", "Mildred Clavin", "Beatrice Clavin"],
        "d": 1
    },
    {
        "q": "Which actress played Cliff Clavin's beloved, no-nonsense mother Esther?",
        "correct": "Frances Sternhagen",
        "wrong": ["Marion Ross", "Estelle Getty", "Charlotte Rae"],
        "d": 2
    },
    {
        "q": "What holiday destination does Cliff take his mother to, only for her to become infatuated with Florida retirement life?",
        "correct": "Walt Disney World in Orlando, Florida",
        "wrong": ["Niagara Falls, New York", "Atlantic City boardwalk", "The Grand Canyon"],
        "d": 2
    },
    {
        "q": "What odd military/civilian organization is Cliff Clavin an obsessed and zealous member of?",
        "correct": "The Florida Postal Reserve / Civil Defense / Men's Lodge",
        "wrong": ["The Boston Coast Guard Auxiliaries", "The Sons of the American Revolution", "The Royal Order of Water Buffaloes"],
        "d": 3
    },
    {
        "q": "What bizarre fact does Cliff share about why postal workers wear gray uniforms instead of blue in certain districts?",
        "correct": "To blend into the New England fog or reduce dog attacks",
        "wrong": ["To save money on indigo dye during the Korean War", "Because Benjamin Franklin personally specified gray wool", "Because pigeons are colorblind to shades of gray"],
        "d": 3
    },
    {
        "q": "What does Cliff Clavin build inside his mother's house using thousands of popsicle sticks and toothpicks?",
        "correct": "A scale model of the Taj Mahal (or historic landmarks)",
        "wrong": ["A scale model of the Boston Postal Distribution Center", "A life-sized bust of Benjamin Franklin", "A miniature replica of Fenway Park"],
        "d": 3
    },
    {
        "q": "In Season 11, what does Cliff Clavin believe he will receive at his retirement party that causes him intense anxiety?",
        "correct": "A humiliating roast by all his peers",
        "wrong": ["A gold watch that is cheap and broken", "A demotion to mail sorting in Alaska", "A forced eviction from his mother's home"],
        "d": 2
    },
    {
        "q": "What does Cliff claim is the most dangerous domestic animal in North America?",
        "correct": "The postman's arch-enemy: the Pomeranian / small terriers",
        "wrong": ["The common Boston street rat", "The feral Canadian goose", "The suburban snapping turtle"],
        "d": 3
    },
    {
        "q": "In Season 9, what does Cliff Clavin discover in his family tree that leads him to believe he is European royalty?",
        "correct": "He claims to be related to the Russian Romanov royal family",
        "wrong": ["He claims to be the rightful Duke of Sussex", "He claims descent from the King of Bavaria", "He claims to be the Prince of Monaco"],
        "d": 2
    },
    {
        "q": "In Season 6, what bizarre device does Cliff invent and attempt to patent?",
        "correct": "The 'Post-a-Bar' / hands-free mail delivery gadget",
        "wrong": ["An automated dog-repelling whistle shoe", "A stamp-licking moisture tongue", "A thermal insulated mail pouch"],
        "d": 3
    },
    {
        "q": "What food item is Cliff Clavin terrified of choking on in multiple episodes?",
        "correct": "Hard-boiled eggs and party pretzels",
        "wrong": ["Raw Boston clams", "Salt water taffy", "Marshmallow circus peanuts"],
        "d": 3
    },
    {
        "q": "What does Cliff do whenever anyone in the bar starts a serious intellectual or emotional discussion?",
        "correct": "Interrupts with an absurd, fabricated piece of trivia",
        "wrong": ["Quietly leaves through the emergency fire exit", "Quotes biblical passages in a booming monotone", "Takes out his postal route map to plan detours"],
        "d": 1
    },
    {
        "q": "In Season 5, what does Cliff Clavin wear to the bar Halloween party that earns him endless mockery?",
        "correct": "A suit of armor (or Ponce de Leon explorer costume)",
        "wrong": ["A giant post-box costume", "A pirate with a stuffed parrot", "A French mime outfit"],
        "d": 2
    },
    {
        "q": "What did Cliff Clavin's estranged father do when he briefly returned to Boston in Season 4?",
        "correct": "Conned Cliff with fake affection before fleeing from the law with stolen goods",
        "wrong": ["Attempted to buy the Cheers building from Sam", "Revealed he was an undercover FBI agent", "Demanded back pay from Cliff's postal pension"],
        "d": 3
    },
    {
        "q": "Which actor portrayed Cliff Clavin's con-artist runaway father, Stephen Clavin?",
        "correct": "Dick O'Neill",
        "wrong": ["Max Gail", "Jerry Van Dyke", "Ken Howard"],
        "d": 3
    },

    # --- CARLA TORTELLI (51-70) ---
    {
        "q": "What is Carla Tortelli's primary role at Cheers throughout the entire run of the series?",
        "correct": "Waitress / cocktail server",
        "wrong": ["Head bartender", "Assistant manager", "Bookkeeper"],
        "d": 1
    },
    {
        "q": "What is Carla Tortelli's general attitude toward Cheers customers and romantic patrons?",
        "correct": "Fiercely sarcastic, combative, and quick to insult",
        "wrong": ["Warm, motherly, and overly hospitable", "Shy, withdrawn, and subservient", "Polite and professionally detached"],
        "d": 1
    },
    {
        "q": "What is the name of Carla's sleazy, deadbeat first ex-husband who constantly torments her?",
        "correct": "Nick Tortelli",
        "wrong": ["Sal Tortelli", "Tony Tortelli", "Gino Tortelli"],
        "d": 1
    },
    {
        "q": "Which actor played Carla's obnoxious ex-husband Nick Tortelli?",
        "correct": "Dan Hedaya",
        "wrong": ["Joe Mantegna", "Robert Pastorelli", "Paul Sorvino"],
        "d": 1
    },
    {
        "q": "What is the name of Nick Tortelli's bubble-headed second blonde trophy wife?",
        "correct": "Loretta",
        "wrong": ["Bambi", "Tiffany", "Crystal"],
        "d": 1
    },
    {
        "q": "Which French-Canadian Boston Bruins hockey goaltender does Carla fall in love with and marry?",
        "correct": "Eddie LeBec",
        "wrong": ["Guy Lafleur", "Rene Gagnon", "Luc Robitaille"],
        "d": 1
    },
    {
        "q": "What was Eddie LeBec's hockey position for the Boston Bruins?",
        "correct": "Goaltender",
        "wrong": ["Center", "Defenseman", "Right wing"],
        "d": 2
    },
    {
        "q": "What superstition does Eddie LeBec believe makes him an invincible goaltender during his winning streak?",
        "correct": "Sleeping with Carla or wearing lucky pre-game ritual charms",
        "wrong": ["Never washing his hockey jersey all season", "Taping his stick with electrical tape counter-clockwise", "Eating raw garlic cloves before stepping on the ice"],
        "d": 2
    },
    {
        "q": "How does Eddie LeBec tragically die in Season 8?",
        "correct": "He is run over by an ice Zamboni while working in an ice traveling show",
        "wrong": ["He crashes his snowmobile into a frozen lake in Quebec", "He suffers a heart attack during an alumni hockey game", "He is crushed by a falling arena scoreboard"],
        "d": 1
    },
    {
        "q": "What shocking secret about Eddie LeBec is revealed at his memorial service in Cheers?",
        "correct": "He had a secret second wife and family in another state",
        "wrong": ["He was secretly a multi-millionaire heir to a Canadian maple fortune", "He was actually born in Cleveland, Ohio, not Canada", "He had never actually legally married Carla"],
        "d": 2
    },
    {
        "q": "How many total children does Carla Tortelli have by the end of the series?",
        "correct": "8",
        "wrong": ["5", "6", "10"],
        "d": 2
    },
    {
        "q": "What are the names of Carla's twin children fathered by Eddie LeBec?",
        "correct": "Elvis and Jesse",
        "wrong": ["Frank and Dean", "Sam and Woody", "Anthony and Michael"],
        "d": 2
    },
    {
        "q": "Who is the father of Carla's intellectual, bespectacled son Ludlow?",
        "correct": "Dr. Bennett Ludlow (Frasier's mentor)",
        "wrong": ["Dr. Frasier Crane", "Sumner Sloane", "Cliff Clavin"],
        "d": 2
    },
    {
        "q": "What cultural heritage is Carla Tortelli fiercely proud of?",
        "correct": "Italian-American",
        "wrong": ["Irish-American", "Greek-American", "Portuguese-American"],
        "d": 1
    },
    {
        "q": "What superstitious practice does Carla frequently threaten enemies with when enraged?",
        "correct": "The Italian 'Evil Eye' (malocchio) and family curses",
        "wrong": ["Voodoo dolls filled with pine needles", "Tarot death card readings", "Spilling black pepper on their shoes"],
        "d": 2
    },
    {
        "q": "What is the name of Carla's eldest son who drops out of school and gets married as a teenager?",
        "correct": "Anthony Tortelli",
        "wrong": ["Gino Tortelli", "Lucia Tortelli", "Sal Tortelli"],
        "d": 2
    },
    {
        "q": "What was the name of Carla's sister who looked identical to her and tried to seduce Sam?",
        "correct": "Annette",
        "wrong": ["Gina", "Rosalia", "Carmela"],
        "d": 3
    },
    {
        "q": "Which Boston sports team does Carla revere with almost religious fanaticism?",
        "correct": "The Boston Red Sox (and Boston Bruins)",
        "wrong": ["The New York Yankees", "The Montreal Canadiens", "The Philadelphia Flyers"],
        "d": 2
    },
    {
        "q": "What did Carla do when an obnoxious patron wore a New York Yankees cap into Cheers?",
        "correct": "Snagged it off his head and ripped or burned it",
        "wrong": ["Poured an entire bottle of tabasco sauce into his beer", "Challenged him to arm-wrestling for 50 dollars", "Refused to speak English to him for an hour"],
        "d": 3
    },
    {
        "q": "What is the name of Carla Tortelli's terrifying, domineering mother who speaks mostly Italian?",
        "correct": "Mama Lozupone",
        "wrong": ["Mama Corleone", "Mama Gambino", "Mama Barzini"],
        "d": 3
    },

    # --- FRASIER CRANE & LILITH STERNIN (71-85) ---
    {
        "q": "In which season of Cheers was Dr. Frasier Crane introduced?",
        "correct": "Season 3",
        "wrong": ["Season 1", "Season 2", "Season 4"],
        "d": 1
    },
    {
        "q": "What brought Dr. Frasier Crane to Cheers for the first time?",
        "correct": "He was dating Diane Chambers after treating her at a psychiatric clinic",
        "wrong": ["He answered an advertisement to rent the upstairs apartment", "He was Sam Malone's court-ordered substance abuse therapist", "He was conducting a sociological study on Boston pub regulars"],
        "d": 1
    },
    {
        "q": "What was Dr. Frasier Crane's academic background and psychiatric training specialty?",
        "correct": "Harvard and Oxford-educated psychiatrist / Freudian psychoanalyst",
        "wrong": ["Yale cognitive behavioral psychologist", "Princeton neurosurgeon", "Columbia addiction specialist"],
        "d": 3
    },
    {
        "q": "Where does Diane leave Frasier standing at the altar in Season 3?",
        "correct": "In Europe (Italy)",
        "wrong": ["At Boston City Hall", "At Trinity Church in Copley Square", "In Paris, France"],
        "d": 2
    },
    {
        "q": "What is the profession of Frasier's stern, intellectual love interest Dr. Lilith Sternin?",
        "correct": "Psychiatrist / research psychologist",
        "wrong": ["Corporate tax attorney", "Pediatric cardiologist", "Professor of ancient literature"],
        "d": 1
    },
    {
        "q": "Which actress portrayed the icy, monotone-voiced Dr. Lilith Sternin?",
        "correct": "Bebe Neuwirth",
        "wrong": ["Christine Baranski", "Julie Hagerty", "Patricia Clarkson"],
        "d": 1
    },
    {
        "q": "What signature hairstyle did Lilith Sternin wear throughout most of Cheers?",
        "correct": "A severely tight, pulled-back hair bun",
        "wrong": ["A loose shoulder-length bob", "A dramatic French twist", "Short pixie cut"],
        "d": 2
    },
    {
        "q": "What is the name of Frasier and Lilith's son born during the run of Cheers?",
        "correct": "Frederick",
        "wrong": ["Niles", "Martin", "Julian"],
        "d": 2
    },
    {
        "q": "What was baby Frederick Crane's very first spoken word, uttered inside the Cheers bar?",
        "correct": "\"Norm!\"",
        "wrong": ["\"Beer!\"", "\"Mama!\"", "\"Freud!\""],
        "d": 2
    },
    {
        "q": "In Season 11, with whom does Lilith have an affair that nearly destroys her marriage to Frasier?",
        "correct": "Dr. Louis Pascal (in an underground eco-pod / biosphere)",
        "wrong": ["Dr. Simon Finch-Royce", "Dr. Bennett Ludlow", "An artist colleague from Harvard"],
        "d": 3
    },
    {
        "q": "Where did Lilith and Dr. Pascal live during their scandalous environmental experiment?",
        "correct": "In an underground biosphere / artificial eco-pod",
        "wrong": ["On an off-grid solar sailboat in the Pacific", "In an Arctic research outpost in Greenland", "In a high-altitude monastery in Tibet"],
        "d": 3
    },
    {
        "q": "What dramatic stunt does a heartbroken Frasier threaten to pull when Lilith leaves him in Season 11?",
        "correct": "Jumping off the ledge of a high-rise building",
        "wrong": ["Setting fire to his Harvard diploma in the middle of Cheers", "Moving permanently to a remote sheep farm in New Zealand", "Drinking an entire pitcher of tap beer in front of the regulars"],
        "d": 2
    },
    {
        "q": "What musical instrument does Frasier Crane frequently play and sing alongside at the Cheers piano?",
        "correct": "Piano",
        "wrong": ["Accordion", "Acoustic guitar", "Violin"],
        "d": 2
    },
    {
        "q": "What dog breed was Lilith's beloved pet that despised Frasier?",
        "correct": "A small dog / Doberman / purebred",
        "wrong": ["A Golden Retriever", "A French Bulldog", "A Great Dane"],
        "d": 3
    },
    {
        "q": "In the Season 10 episode 'Smotherly Love', why does Frasier object to Lilith's mother visiting?",
        "correct": "She undermines their strict parenting methods and criticizes Frasier",
        "wrong": ["She insists on smoking cigars inside their home", "She constantly flirts with Sam Malone", "She attempts to convert Frederick to another faith"],
        "d": 3
    },

    # --- REBECCA HOWE (86-100) ---
    {
        "q": "In which season was Rebecca Howe introduced as the new manager of Cheers?",
        "correct": "Season 6",
        "wrong": ["Season 4", "Season 5", "Season 7"],
        "d": 1
    },
    {
        "q": "Which actress played Rebecca Howe, earning an Emmy and a Golden Globe for the role?",
        "correct": "Kirstie Alley",
        "wrong": ["Shelley Long", "Kim Cattrall", "JoBeth Williams"],
        "d": 1
    },
    {
        "q": "What large corporate conglomerate hired Rebecca Howe to manage Cheers in Season 6?",
        "correct": "The Lillian Corporation",
        "wrong": ["Omni Consumer Products", "The Boston Hospitality Group", "Drake Enterprises"],
        "d": 1
    },
    {
        "q": "What was the name of the smooth-talking corporate executive Rebecca Howe was desperately infatuated with in Season 6?",
        "correct": "Evan Drake",
        "wrong": ["Robin Colcord", "Gordon Finch", "Franklin Stern"],
        "d": 1
    },
    {
        "q": "Which English multi-millionaire corporate raider did Rebecca date in Seasons 8 and 9?",
        "correct": "Robin Colcord",
        "wrong": ["Arthur Sterling", "Nigel Finch", "Julian Croft"],
        "d": 2
    },
    {
        "q": "Which actor played English billionaire Robin Colcord?",
        "correct": "Roger Rees",
        "wrong": ["John Cleese", "Timothy Dalton", "Ian McShane"],
        "d": 2
    },
    {
        "q": "What white-collar crime did Robin Colcord commit using Rebecca's office computer at Cheers?",
        "correct": "Insider trading",
        "wrong": ["Embezzling pension funds", "Money laundering through offshore accounts", "Corporate tax evasion"],
        "d": 2
    },
    {
        "q": "What bad habit did Rebecca Howe constantly try to hide from the staff by smoking in Sam's back office?",
        "correct": "Chain smoking cigarettes",
        "wrong": ["Drinking high-end gin", "Eating whole tubs of chocolate ice cream", "Popping anti-anxiety tranquilizers"],
        "d": 2
    },
    {
        "q": "What was Rebecca Howe's recurring emotional reaction whenever her ambitious plans fell apart?",
        "correct": "Bursting into hysterical, high-pitched sobbing jags",
        "wrong": ["Throwing glasses at the bar mirrors", "Giving the staff the silent treatment for days", "Writing formal letters of reprimand"],
        "d": 2
    },
    {
        "q": "What secret childhood dream did Rebecca Howe confess to having before entering the corporate world?",
        "correct": "Becoming an actress / singer or marrying rich",
        "wrong": ["Becoming a professional ice skater", "Directing broadway musicals", "Joining the Peace Corps in South America"],
        "d": 3
    },
    {
        "q": "In Season 9, what happens to Robin Colcord after his insider trading conviction?",
        "correct": "He goes to minimum-security prison and does community service",
        "wrong": ["He flees to Switzerland on a private yacht", "He receives a presidential pardon", "He fakes his death in a helicopter crash"],
        "d": 2
    },
    {
        "q": "What unglamorous profession does Rebecca Howe's eventual husband Don Santry hold in Season 11?",
        "correct": "Plumber",
        "wrong": ["Garbage collector", "Truck driver", "Short-order cook"],
        "d": 2
    },
    {
        "q": "Which Hollywood star played Rebecca's blue-collar plumber husband Don Santry in Season 11?",
        "correct": "Tom Berenger",
        "wrong": ["Kurt Russell", "Kevin Bacon", "Dennis Quaid"],
        "d": 3
    },
    {
        "q": "What was Rebecca Howe's sister's name who visited Cheers and immediately charmed Sam?",
        "correct": "Susan Howe",
        "wrong": ["Karen Howe", "Jennifer Howe", "Lisa Howe"],
        "d": 3
    },
    {
        "q": "In Season 10, what did Rebecca Howe accidentally do to Sam's back office with a lit cigarette?",
        "correct": "Accidentally set the office desk and paperwork on fire",
        "wrong": ["Melted a vintage vinyl record collection", "Burnt a hole through Sam's prized leather sofa", "Triggered the ceiling foam fire suppression system"],
        "d": 3
    }
]

assert len(raw_questions) == 100, f"Expected 100, got {len(raw_questions)}"

d_counts = {1: 0, 2: 0, 3: 0}
for q in raw_questions:
    d_counts[q["d"]] += 1

print(f"DEBUG Batch 2 d_counts: {d_counts}")
assert d_counts[1] == 30, f"Expected 30 d1, got {d_counts[1]}"
assert d_counts[2] == 40, f"Expected 40 d2, got {d_counts[2]}"
assert d_counts[3] == 30, f"Expected 30 d3, got {d_counts[3]}"

formatted = assemble_batch(raw_questions, 2)
save_json(formatted, "tools/staging/cheers_batch2.json")
print("Saved tools/staging/cheers_batch2.json successfully!")
