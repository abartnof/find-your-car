import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from utils import assemble_batch, save_json

raw_questions = [
    # --- PILOT & SEASON 1 (1-18) ---
    {
        "q": "In the pilot episode 'The Seinfeld Chronicles', what was Kramer's character named?",
        "correct": "Kessler",
        "wrong": ["Hoffman", "Feldman", "Hesselman"],
        "d": 1
    },
    {
        "q": "In the pilot episode, what is the name of the female friend visiting from Michigan who stays at Jerry's apartment?",
        "correct": "Laura",
        "wrong": ["Vanessa", "Claire", "Marlene"],
        "d": 3
    },
    {
        "q": "What original diner waitress character appeared in the pilot episode before Elaine Benes was introduced?",
        "correct": "Claire",
        "wrong": ["Arlene", "Loretta", "Bernice"],
        "d": 3
    },
    {
        "q": "In 'The Stake Out', what fake name does George Costanza invent for the very first time?",
        "correct": "Art Vandelay",
        "wrong": ["Art Corvelay", "Buck Naked", "H.E. Pennypacker"],
        "d": 1
    },
    {
        "q": "What profession does George claim Art Vandelay practices when he invents the persona in 'The Stake Out'?",
        "correct": "Architect",
        "wrong": ["Latex manufacturer", "Marine biologist", "Civil engineer"],
        "d": 1
    },
    {
        "q": "In 'The Robbery', why is Jerry's apartment robbed while he is away doing stand-up in Minneapolis?",
        "correct": "Kramer left the apartment door wide open",
        "wrong": ["The building superintendent lost the master key", "Newman gave the front door buzzer code to a burglar", "Jerry forgot to lock the fire escape window"],
        "d": 2
    },
    {
        "q": "In 'The Stock Tip', what company stock does George convince Jerry to buy based on a confidential insider tip?",
        "correct": "Sendrax",
        "wrong": ["Spector-Soft", "Vandelay Industries", "OmniTech"],
        "d": 1
    },
    {
        "q": "How much money does Jerry initially invest in the Sendrax stock tip alongside George?",
        "correct": "$2,500",
        "wrong": ["$1,000", "$5,000", "$10,000"],
        "d": 3
    },
    {
        "q": "In 'The Ex-Girlfriend', what is the profession of George's ex-girlfriend Marlene, whom Jerry secretly begins dating?",
        "correct": "Cashier at a restaurant",
        "wrong": ["Real estate agent", "High school guidance counselor", "Dental hygienist"],
        "d": 3
    },
    {
        "q": "Why does Marlene ultimately break up with Jerry in 'The Ex-Girlfriend'?",
        "correct": "She finds his stand-up comedy act completely unfunny",
        "wrong": ["She realizes she is still in love with George", "She catches him snooping through her medicine cabinet", "She discovers he still talks to his mother every day"],
        "d": 2
    },
    {
        "q": "In 'The Pony Remark', what casual comment does Jerry make at Manya's anniversary dinner that deeply offends her?",
        "correct": "He hates anyone who grew up having a pony",
        "wrong": ["He believes immigrants complain too much about their past", "He thinks Polish food lacks adequate seasoning", "He dislikes large family dinner gatherings"],
        "d": 1
    },
    {
        "q": "From which European country did Manya emigrate, where she had owned a cherished pony as a young girl?",
        "correct": "Poland",
        "wrong": ["Hungary", "Austria", "Czechoslovakia"],
        "d": 3
    },
    {
        "q": "In 'The Pony Remark', what major apartment project does Kramer insist he is going to build in his living room?",
        "correct": "Levels with custom wood steps and carpeting",
        "wrong": ["A private sauna inside his walk-in closet", "An authentic brick wood-fired pizza oven", "A full-sized elevated indoor putting green"],
        "d": 1
    },
    {
        "q": "In 'The Jacket', what eye-catching interior lining does Jerry's expensive new suede jacket feature?",
        "correct": "Pink candy cane stripes",
        "wrong": ["Bright yellow polka dots", "Red and green tartan plaid", "Leopard print silk fabric"],
        "d": 1
    },
    {
        "q": "Who plays Elaine's intimidating novelist father, Alton Benes, in 'The Jacket'?",
        "correct": "Lawrence Tierney",
        "wrong": ["Veteran actor Brian Keith", "Character actor Robert Prosky", "Hollywood legend Jack Palance"],
        "d": 2
    },
    {
        "q": "What song does Alton Benes repeatedly sing while driving Jerry and George in his car?",
        "correct": "\"Master of the House\" from Les Misérables",
        "wrong": ["\"Ol' Man River\" from Show Boat", "\"Mack the Knife\" from The Threepenny Opera", "\"The Impossible Dream\" from Man of La Mancha"],
        "d": 3
    },
    {
        "q": "In 'The Phone Message', what does George try desperately to steal from his girlfriend Carol's apartment?",
        "correct": "Her answering machine cassette tape",
        "wrong": ["Her personal diary notebook", "A compromising polaroid photograph", "An unmailed angry letter he sent"],
        "d": 1
    },
    {
        "q": "In 'The Apartment', how much is the monthly rent for the vacant apartment above Jerry's that Elaine hopes to rent?",
        "correct": "$400 per month",
        "wrong": ["$350 per month plus utilities", "$600 per month with security deposit", "$850 per month including parking"],
        "d": 3
    },

    # --- SEASON 2 CLASSICS (19-45) ---
    {
        "q": "In 'The Statue', what item does George believe Ray, the apartment cleaner, stole from Jerry's apartment?",
        "correct": "A small statue inherited from his grandfather",
        "wrong": ["An antique silver cigarette lighter", "A vintage Montblanc fountain pen", "A pair of gold cuff links from his bar mitzvah"],
        "d": 2
    },
    {
        "q": "What character persona does Kramer assume when he confronts Ray to retrieve the stolen statue?",
        "correct": "A hard-boiled police detective",
        "wrong": ["An aggressive insurance investigator", "A high-powered mafia enforcer", "An undercover FBI field agent"],
        "d": 3
    },
    {
        "q": "In 'The Revenge', what does George slip into his former boss Rick Levitan's drink at an office party?",
        "correct": "A mickey powder slipped into his drink",
        "wrong": ["A double dose of liquid laxatives", "A strong sedative sleeping pill", "An overdose of hot pepper oil extract"],
        "d": 1
    },
    {
        "q": "What business does George work for before rashly quitting and then trying to poison his boss in 'The Revenge'?",
        "correct": "Rick Barr Properties",
        "wrong": ["Pendant Publishing", "Sanfilippo & Sons Real Estate", "Vandelay Latex Corporation"],
        "d": 3
    },
    {
        "q": "Why does Kramer dump a bag of wet cement into a commercial washing machine in 'The Revenge'?",
        "correct": "The laundromat owner refused to refund his money",
        "wrong": ["He wanted to see if the drum would stop spinning", "He was trying to mix concrete for his apartment levels", "He thought it would clean the interior lint traps"],
        "d": 2
    },
    {
        "q": "In 'The Heart Attack', what medical condition does George actually have after fearing he suffered a heart attack?",
        "correct": "An inflamed tonsil condition",
        "wrong": ["Severe acid reflux disease", "A pinched nerve in his shoulder", "An acute panic attack"],
        "d": 2
    },
    {
        "q": "What is the name of the eccentric holistic healer recommended by Kramer whom George visits in 'The Heart Attack'?",
        "correct": "Tor Eckman",
        "wrong": ["Dr. Martin van Nostrand", "Dr. Bob Malooga", "Maestro Bob Cobb"],
        "d": 2
    },
    {
        "q": "What color does George's skin turn after drinking the herbal tea concoction prepared by Tor Eckman?",
        "correct": "Purple",
        "wrong": ["Bright orange", "Pale green", "Deep crimson"],
        "d": 3
    },
    {
        "q": "In 'The Deal', what gift does Jerry give Elaine for her birthday that makes her feel unappreciated?",
        "correct": "An envelope containing $182 in cash",
        "wrong": ["A gift certificate to a grocery store", "A set of plain white kitchen dish towels", "A discounted bench scraper"],
        "d": 2
    },
    {
        "q": "What lavish birthday gift does Kramer present to Elaine in 'The Deal'?",
        "correct": "A high-end countertop benchtop espresso maker",
        "wrong": ["A cashmere sweater from a luxury department store", "A pair of gold designer hoop earrings", "An authentic leather messenger briefcase"],
        "d": 3
    },
    {
        "q": "In 'The Baby Shower', why is George desperate to confront Leslie at her baby shower?",
        "correct": "She ruined his shirt with chocolate sauce years earlier",
        "wrong": ["She never repaid a hundred dollar personal loan", "She rejected his prom invitation in high school", "She claimed he was a terrible kisser at a party"],
        "d": 3
    },
    {
        "q": "In 'The Chinese Restaurant', what host repeatedly tells Jerry, George, and Elaine that their table will be ready in '5, 10 minutes'?",
        "correct": "Mr. Cohen",
        "wrong": ["Host Mr. Henderson", "Head waiter Mr. Fong", "Host Mr. Sterling"],
        "d": 2
    },
    {
        "q": "In 'The Chinese Restaurant', what movie are Jerry, Elaine, and George trying to see after dinner?",
        "correct": "Plan 9 from Outer Space",
        "wrong": ["Night of the Living Dead", "Invasion of the Body Snatchers", "Attack of the 50 Foot Woman"],
        "d": 2
    },
    {
        "q": "What name does the maître d' call out when George is waiting for an urgent payphone call in 'The Chinese Restaurant'?",
        "correct": "\"Cartwright!\"",
        "wrong": ["\"Costanza!\"", "\"Castelli!\"", "\"Conrad!\""],
        "d": 1
    },
    {
        "q": "In 'The Busboy', why does the restaurant busboy Antonio get fired?",
        "correct": "George carelessly left a burning menu on the table",
        "wrong": ["Elaine accidentally knocked over a tray of expensive glasses", "Jerry publicly complained about the dirty silverware", "Kramer took photos in the restaurant kitchen"],
        "d": 2
    },
    {
        "q": "What happens to Antonio the busboy's apartment shortly after Jerry and George visit him to apologize?",
        "correct": "An accidental kitchen explosion occurs",
        "wrong": ["It is flooded by a broken main water pipe", "A burglar breaks in through the unlocked window", "He gets evicted for keeping an illegal pet cat"],
        "d": 3
    },

    # --- SEASON 3 HIGHLIGHTS (35-70) ---
    {
        "q": "In 'The Note', what does George confess to Jerry after receiving a massage from a male physical therapist?",
        "correct": "\"I think it moved!\"",
        "wrong": ["\"I felt completely healed!\"", "\"I gave him a huge tip!\"", "\"I asked for his home number!\""],
        "d": 1
    },
    {
        "q": "In 'The Note', what sports legend does Kramer repeatedly claim he saw at Dinky Donuts?",
        "correct": "Joe DiMaggio",
        "wrong": ["Mickey Mantle", "Willie Mays", "Ted Williams"],
        "d": 1
    },
    {
        "q": "What habit does Kramer notice Joe DiMaggio doing at the donut counter that proves his deep focus?",
        "correct": "Dunking his donuts into his coffee",
        "wrong": ["Reading the morning paper without glasses", "Eating three powdered donuts in under two minutes", "Signing paper napkins for the counter staff"],
        "d": 3
    },
    {
        "q": "In 'The Truth', what profession does George's girlfriend Patrice have, which causes Jerry major anxiety?",
        "correct": "Internal Revenue Service tax auditor",
        "wrong": ["Criminal court prosecutor", "Health department food safety inspector", "Corporate ethics investigator"],
        "d": 3
    },
    {
        "q": "In 'The Pen', what special feature does Jack Klompus's pen have that he offers to Jerry?",
        "correct": "It can write completely upside down in space",
        "wrong": ["It features an erasable pressurized ink cartridge", "It was custom-made for the White House press corps", "It has a built-in miniature magnifying glass"],
        "d": 2
    },
    {
        "q": "What retirement community in Florida do Jerry's parents Helen and Morty live in?",
        "correct": "Del Boca Vista",
        "wrong": ["Century Village", "Boca Lago Pines", "Pines of Delray"],
        "d": 1
    },
    {
        "q": "Why does Elaine suffer severe back pain while staying with Jerry's parents in 'The Pen'?",
        "correct": "She slept on an uncomfortable sofa pull-out bed",
        "wrong": ["She dropped a heavy suitcase down the exterior steps", "She tripped over a metal sprinkler head on the lawn", "She spent five hours sitting in an unpadded metal chair"],
        "d": 2
    },
    {
        "q": "What famous Tennessee Williams line does a muscle-relaxant intoxicated Elaine shout at the banquet in 'The Pen'?",
        "correct": "\"Stella! Stella!\"",
        "wrong": ["\"Blanche! Blanche!\"", "\"Stanley! Stanley!\"", "\"Mitch! Mitch!\""],
        "d": 1
    },
    {
        "q": "In 'The Dog', what is the name of the unruly dog Jerry is forced to dog-sit for a drunk airline passenger?",
        "correct": "Farfel",
        "wrong": ["Rusty", "Smuckers", "Snowball"],
        "d": 2
    },
    {
        "q": "What film do George and Elaine go see together while waiting for Jerry in 'The Dog'?",
        "correct": "Prognosis Negative",
        "wrong": ["Rochelle, Rochelle: A Young Girl's Journey", "Chow Fun: The Musical", "Ponce de Leon: Fountain of Youth"],
        "d": 3
    },
    {
        "q": "In 'The Library', what is the name of the eccentric library investigations officer pursuing Jerry?",
        "correct": "Mr. Bookman",
        "wrong": ["Inspector Henderson", "Investigator Dewey", "Officer Fitzpatrick"],
        "d": 1
    },
    {
        "q": "Which actor brilliantly portrayed library detective Mr. Bookman in 'The Library'?",
        "correct": "Philip Baker Hall",
        "wrong": ["Character actor M. Emmet Walsh", "Veteran star R. Lee Ermey", "Character actor Harris Yulin"],
        "d": 3
    },
    {
        "q": "What classic novel did Jerry fail to return to the New York Public Library back in 1971?",
        "correct": "Tropic of Capricorn",
        "wrong": ["Slaughterhouse-Five by Kurt Vonnegut", "The Catcher in the Rye by J.D. Salinger", "A Farewell to Arms by Ernest Hemingway"],
        "d": 2
    },
    {
        "q": "In 'The Parking Garage', where is the shopping mall parking garage located where the group loses their car?",
        "correct": "Paramus, New Jersey",
        "wrong": ["White Plains, New York", "Fort Lee, New Jersey", "Stamford, Connecticut"],
        "d": 3
    },
    {
        "q": "In 'The Parking Garage', what pet does Kramer purchase that is in danger of dying in its plastic bag?",
        "correct": "Goldfish",
        "wrong": ["A miniature turtle", "A pet hermit crab", "A baby chameleon"],
        "d": 2
    },
    {
        "q": "What major automotive problem occurs in the final shot of 'The Parking Garage' after they finally locate the car?",
        "correct": "The car engine refuses to start",
        "wrong": ["All four tires have gone completely flat", "The parking exit gate is padlocked shut", "A tow truck is already hoisting the front bumper"],
        "d": 2
    },
    {
        "q": "In 'The Cafe', what is the name of the Pakistani immigrant who opens the Dream Cafe across from Jerry's building?",
        "correct": "Babu Bhatt",
        "wrong": ["Babu Patel", "Rajiv Bhatt", "Tariq Khan"],
        "d": 1
    },
    {
        "q": "What culinary advice does Jerry give Babu that leads directly to the complete financial ruin of the Dream Cafe?",
        "correct": "Serve exclusively authentic Pakistani cuisine",
        "wrong": ["Convert the diner into an American breakfast buffet", "Offer free bottomless coffee refills all morning", "Lower all lunch prices by fifty percent across the board"],
        "d": 2
    },
    {
        "q": "In 'The Tape', what does Elaine anonymously record onto Jerry's handheld tape recorder?",
        "correct": "A seductive, breathy erotic message",
        "wrong": ["A confession that she stole money from his desk", "A rehearsal of her stand-up comedy material", "An audio recording of Kramer singing opera"],
        "d": 2
    },
    {
        "q": "What dubious product does George purchase from China in 'The Tape' to fix his baldness?",
        "correct": "A traditional herbal hair growth cream",
        "wrong": ["A magnetic scalp stimulation headcap", "A bottle of rare snake venom restorative oil", "An acupuncture needle therapy kit"],
        "d": 3
    },
    {
        "q": "In 'The Nose Job', what does Kramer bluntly tell George's girlfriend Audrey about her appearance?",
        "correct": "She needs to get a nose job immediately",
        "wrong": ["Her hairstyle makes her face look enormous", "She wears far too much cheap perfume", "Her posture makes her look ten years older"],
        "d": 2
    },
    {
        "q": "In 'The Stranded', what famous quote does Elaine deliver when an annoying party guest talks about her fiancé?",
        "correct": "\"Maybe the dingo ate your baby!\"",
        "wrong": ["\"These pretzels are making me thirsty!\"", "\"No soup for you!\"", "\"You want a piece of me?!\""],
        "d": 1
    },
    {
        "q": "In 'The Alternate Side', what line is George given to recite in Woody Allen's movie shooting on their block?",
        "correct": "\"These pretzels are making me thirsty!\"",
        "wrong": ["\"I think it moved!\"", "\"Here's to feeling good all the time!\"", "\"Serenity now!\""],
        "d": 1
    },
    {
        "q": "Why does George fail at his job of moving parked cars for alternate side parking in 'The Alternate Side'?",
        "correct": "He causes a massive multi-car traffic gridlock",
        "wrong": ["He loses the ignition keys to every single vehicle", "He parks six consecutive cars in a red tow zone", "He crashes an expensive foreign sedan into an ambulance"],
        "d": 2
    },
    {
        "q": "In 'The Red Dot', what defect is on the discounted cashmere sweater George buys for Elaine as a thank-you gift?",
        "correct": "A tiny red dot stain on the fabric",
        "wrong": ["A torn seam under the right armpit", "A missing hand-carved mother-of-pearl button", "A moth hole right in the center chest area"],
        "d": 1
    },
    {
        "q": "In 'The Red Dot', who does George have sex with on his desk at his office, leading to his firing?",
        "correct": "Evie the cleaning woman",
        "wrong": ["Ada the receptionist", "Patrice the accounting clerk", "Cheryl the office manager"],
        "d": 2
    },
    {
        "q": "What defense does George give to his boss Mr. Lippman when caught having sex on his office desk?",
        "correct": "\"Was that wrong? Should I not have done that?\"",
        "wrong": ["\"I was under tremendous workplace stress!\"", "\"It was entirely consensual between two adults!\"", "\"I didn't think anyone was working late tonight!\""],
        "d": 2
    },
    {
        "q": "In 'The Subway', what happens to George when he follows an attractive blonde woman to a hotel room?",
        "correct": "She handcuffs him to the bed and robs him",
        "wrong": ["She turns out to be an undercover vice detective", "Her jealous husband bursts into the bedroom with a bat", "She abandons him with a massive room service bill"],
        "d": 2
    },
    {
        "q": "In 'The Subway', who does Jerry strike up a conversation with while riding the subway train to Coney Island?",
        "correct": "A completely naked passenger sitting across from him",
        "wrong": ["A subway busker playing accordion tunes", "An angry conductor on a work strike", "A fortune teller offering psychic palm readings"],
        "d": 2
    },
    {
        "q": "In 'The Subway', what horse does Kramer bet on at the off-track betting parlor after receiving a tip?",
        "correct": "Papanick",
        "wrong": ["Captain Nemo", "Little Jerry", "Prickly Pete"],
        "d": 3
    },
    {
        "q": "In 'The Pez Dispenser', which cartoon character is featured on the Pez dispenser Jerry places on Elaine's lap?",
        "correct": "Tweety Bird",
        "wrong": ["Bugs Bunny", "Daffy Duck", "Woody Woodpecker"],
        "d": 1
    },
    {
        "q": "Why does George's pianist girlfriend Noel break up with him after her recital in 'The Pez Dispenser'?",
        "correct": "She heard Elaine burst into laughter during her performance",
        "wrong": ["George fell asleep and began snoring loudly in the front row", "George refused to attend the formal post-recital reception", "She discovered George had no interest in classical music"],
        "d": 3
    },

    # --- SEASONS 3 CLIMAX & ICONIC EPISODES (71-100) ---
    {
        "q": "In 'The Boyfriend', which New York Mets baseball star does Jerry meet and develop a man-crush on?",
        "correct": "Keith Hernandez",
        "wrong": ["Dwight Gooden", "Darryl Strawberry", "Ron Darling"],
        "d": 1
    },
    {
        "q": "What conspiracy theory parody from the JFK assassination is reenacted in 'The Boyfriend'?",
        "correct": "The 'Second Spitter' magic loogie theory",
        "wrong": ["The single bullet pristine trajectory theory", "The grassy knoll umbrella man conspiracy", "The babushka lady photographic evidence"],
        "d": 1
    },
    {
        "q": "According to Jerry's reenactment in 'The Boyfriend', who was the actual second spitter behind the bushes?",
        "correct": "Roger McDowell",
        "wrong": ["Mets relief pitcher Jesse Orosco", "Second baseman Wally Backman", "Mets outfielder Mookie Wilson"],
        "d": 3
    },
    {
        "q": "In 'The Boyfriend', what lie does George tell the unemployment office regarding Vandelay Industries?",
        "correct": "He is on the verge of being hired as a latex salesman",
        "wrong": ["He is the chief executive officer of latex distribution", "He manages a team of architectural draftsmen", "He is waiting for a contract to design baseball stadiums"],
        "d": 2
    },
    {
        "q": "What does George shout as he rushes frantically out of Jerry's bathroom with his trousers around his ankles?",
        "correct": "\"Say Vandelay! Say Vandelay!\"",
        "wrong": ["\"Get the phone! Get the phone!\"", "\"Don't pick up! Don't pick up!\"", "\"Tell them I'm an architect!\""],
        "d": 3
    },
    {
        "q": "In 'The Fix-Up', what defect does George obsess over when Jerry and Elaine try to set him up with Cynthia?",
        "correct": "Whether she has a big nose or thick facial hair",
        "wrong": ["Whether she is taller than him in high heels", "Whether she has an annoying laugh or high-pitched voice", "Whether she comes from an excessively wealthy family"],
        "d": 1
    },
    {
        "q": "What expired item does George use during his encounter with Cynthia in 'The Fix-Up'?",
        "correct": "A punctured condom from his wallet",
        "wrong": ["A dried-out tube of lubricant ointment", "An expired bottle of prescription cologne", "A faded strip of breath mint strips"],
        "d": 3
    },
    {
        "q": "In 'The Limo', what white supremacist leader's name does George assume to take a private airport limousine?",
        "correct": "Donald O'Brien",
        "wrong": ["White supremacist Colin Ferguson", "Activist leader Patrick Murphy", "Public speaker Sean Flaherty"],
        "d": 3
    },
    {
        "q": "What major sports event is the real Donald O'Brien scheduled to speak at in 'The Limo'?",
        "correct": "A neo-Nazi rally at Madison Square Garden",
        "wrong": ["A private militia assembly at the Meadowlands", "A political debate at the Jacob Javits Center", "A televised press conference at the Nassau Coliseum"],
        "d": 2
    },
    {
        "q": "What fictional high-society alias does Jerry use alongside George in 'The Limo'?",
        "correct": "Dylan Murphy",
        "wrong": ["Arthur Pennypacker", "Martin van Nostrand", "Kel Varnsen"],
        "d": 3
    },
    {
        "q": "In 'The Good Samaritan', what television host's voice causes Kramer to suffer sudden neurological seizures?",
        "correct": "Mary Hart from Entertainment Tonight",
        "wrong": ["Leeza Gibbons", "Kathie Lee Gifford", "Connie Chung"],
        "d": 1
    },
    {
        "q": "In 'The Letter', what famous Neil Simon play does Jerry's girlfriend Nina plagiarize in her love letter to him?",
        "correct": "Chapter Two",
        "wrong": ["The Odd Couple", "Barefoot in the Park", "Lost in Yonkers"],
        "d": 3
    },
    {
        "q": "What iconic oil painting portrait of Kramer is created by Nina in 'The Letter'?",
        "correct": "\"The Kramer\"",
        "wrong": ["\"The Cosmo\"", "\"The Hipster Doofus\"", "\"The Visionary\""],
        "d": 2
    },
    {
        "q": "What wealthy couple purchases 'The Kramer' painting from the gallery in 'The Letter'?",
        "correct": "An elderly art patron couple who find him captivating",
        "wrong": ["A pair of modern art dealers from SoHo", "An eccentric Wall Street investment banker", "A museum curator looking for outsider folk art"],
        "d": 1
    },
    {
        "q": "In 'The Parking Space', who does George engage in an hours-long standoff with over a street parking space?",
        "correct": "Mike Moffitt",
        "wrong": ["Jack Klompus", "Bob Cobb", "Ramon the pool guy"],
        "d": 2
    },
    {
        "q": "What is the technical parking debate between George and Mike Moffitt in 'The Parking Space'?",
        "correct": "Backing into the space versus pulling in head-first",
        "wrong": ["Using a turn signal before claiming the curb", "Waiting with hazard lights versus holding the spot on foot", "Parallel parking on the left versus right side of the street"],
        "d": 1
    },
    {
        "q": "In 'The Keys', why does Jerry demand his spare apartment keys back from Kramer?",
        "correct": "Kramer entered while Jerry was with a woman without knocking",
        "wrong": ["Kramer lost three spare sets in a single week", "Kramer gave copies of the key to Newman and Bob Sacamano", "Kramer raided Jerry's refrigerator while hosting a party"],
        "d": 3
    },
    {
        "q": "Where does Kramer travel to follow his acting dreams after Jerry revokes his spare key privileges in 'The Keys'?",
        "correct": "Los Angeles, California",
        "wrong": ["Chicago, Illinois in the Midwest", "San Francisco, Northern California", "Miami Beach down in South Florida"],
        "d": 3
    },
    {
        "q": "What famous television sitcom does Kramer land a guest role on while in Hollywood in 'The Keys'?",
        "correct": "Murphy Brown",
        "wrong": ["Northern Exposure", "Designing Women", "Mad About You"],
        "d": 1
    },
    {
        "q": "What character role does Kramer play on 'Murphy Brown' in 'The Keys'?",
        "correct": "Steven Snell, one of Murphy's rotating secretaries",
        "wrong": ["An investigative television news reporter", "A delivery driver delivering confidential documents", "A quirky building maintenance handyman"],
        "d": 1
    },
    {
        "q": "In 'The Suicide', what neighbor of Jerry's falls into a coma after a failed suicide attempt?",
        "correct": "Martin",
        "wrong": ["Harold", "Phillip", "Emmanuel"],
        "d": 2
    },
    {
        "q": "What is the name of Martin's attractive girlfriend who attempts to seduce Jerry while Martin is in a coma?",
        "correct": "Gina",
        "wrong": ["Marlene", "Sasha", "Patrice"],
        "d": 2
    },
    {
        "q": "In 'The Cafe', what does Babu Bhatt call Jerry when the restaurant closes down permanently?",
        "correct": "\"You very bad man! Very, very bad man!\"",
        "wrong": ["\"You ruined my entire American dream!\"", "\"Never show your face around my family again!\"", "\"You are the worst friend in New York!\""],
        "d": 2
    },
    {
        "q": "In 'The Alternate Side', why does Kramer miss his acting scene in Woody Allen's movie?",
        "correct": "He drank all the prop beer and got too drunk",
        "wrong": ["He forgot his lines completely on camera", "He got into a physical brawl with the director", "He arrived three hours late after getting lost on the subway"],
        "d": 2
    },
    {
        "q": "In 'The Stake Out', what excuse do Jerry and George give for lingering in the lobby of the SAG office building?",
        "correct": "Waiting for an architect named Art Vandelay",
        "wrong": ["Auditioning for an off-Broadway musical production", "Picking up tax documents for an independent film crew", "Delivering legal briefs to an entertainment attorney"],
        "d": 2
    },
    {
        "q": "In 'The Baby Shower', what illegal service does Kramer hook Jerry up with through two shady Russian technicians?",
        "correct": "Pirated illegal cable television service",
        "wrong": ["An unlisted high-voltage electrical line", "Tapped long-distance telephone calls", "Black market imported Russian vodka"],
        "d": 2
    },
    {
        "q": "In 'The Deal', what two relationship elements do Jerry and Elaine attempt to combine under their strict agreement?",
        "correct": "\"This\" (friendship) and \"That\" (physical intimacy)",
        "wrong": ["Living together and maintaining separate bank accounts", "Dating other people and spending every holiday together", "Sharing meals and sharing apartment chores"],
        "d": 2
    },
    {
        "q": "In 'The Chinese Restaurant', what bet does Jerry propose to Elaine regarding eating food off another customer's plate?",
        "correct": "Fifty dollars to eat an egg roll off an elderly woman's plate",
        "wrong": ["Twenty dollars to drink a stranger's hot tea", "One hundred dollars to take a spare rib from a businessman", "Twenty-five dollars to finish a bowl of wonton soup"],
        "d": 2
    },
    {
        "q": "In 'The Busboy', what is the name of Antonio the busboy's lost cat that George helps locate?",
        "correct": "Pequita",
        "wrong": ["Snowball", "Bonita", "Chiquita"],
        "d": 3
    },
    {
        "q": "In 'The Library', what was Marion the head librarian's relationship with Jerry back in high school?",
        "correct": "Jerry was deeply infatuated with her poetry reading",
        "wrong": ["She had given him his first kiss behind the book stacks", "She caught him defacing encyclopedias with funny sketches", "She was his study partner who failed algebra with him"],
        "d": 2
    },
    {
        "q": "In 'The Suicide', which classic Drake's snack cake does Newman greedily demand from Jerry?",
        "correct": "Drake's Coffee Cake",
        "wrong": ["Hostess Chocolate Cupcakes", "Tastykake Butterscotch Krimpets", "Little Debbie Swiss Cake Rolls"],
        "d": 1
    },
    {
        "q": "In 'The Alternate Side', what famous observation does Jerry make to the car rental agent about car reservations?",
        "correct": "\"You know how to take the reservation, you just don't know how to hold the reservation.\"",
        "wrong": ["\"A reservation without a car is simply an empty promise on paper.\"", "\"If you don't have cars, why are you sitting behind a rental counter?\"", "\"Taking reservations is meaningless if anyone who walks in takes the keys.\""],
        "d": 1
    },
    {
        "q": "In 'The Statue', what is the profession of Ray's eccentric girlfriend Rava?",
        "correct": "A published Finnish poet",
        "wrong": ["A contemporary ballet choreographer", "An avant-garde experimental playwright", "A modern classical pianist"],
        "d": 2
    },
    {
        "q": "In 'The Busboy', why does Antonio the fired busboy ultimately thank George and Jerry?",
        "correct": "He wasn't at work when a deadly fire destroyed the restaurant",
        "wrong": ["The incident motivated him to finish his degree in computer science", "He found a high-paying executive job at a gourmet catering company", "He received a major financial settlement from the restaurant owner"],
        "d": 2
    }
]

if __name__ == "__main__":
    out = assemble_batch(raw_questions, 1)
    save_json(out, "tools/staging/seinfeld_batch1.json")
