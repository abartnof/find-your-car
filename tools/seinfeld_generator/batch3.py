import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from utils import assemble_batch, save_json

raw_questions = [
    # --- SEASON 6 CLASSICS (1-50) ---
    {
        "q": "In 'The Chaperone', what beauty pageant contestant does Kramer coach to the Miss America competition?",
        "correct": "Miss Rhode Island (Karen)",
        "wrong": ["Miss Connecticut (Cheryl)", "Miss Massachusetts (Christine)", "Miss New York (Brenda)"],
        "d": 2
    },
    {
        "q": "What tragic accident ruins Miss Rhode Island's talent rehearsal in 'The Chaperone'?",
        "correct": "Kramer accidentally smothers her trained doves",
        "wrong": ["Her baton flew into the auditorium lighting rig", "Her evening dress ripped down the center zipper", "Her music cassette tape was erased by a magnet"],
        "d": 3
    },
    {
        "q": "In 'The Big Salad', what restaurant food item causes huge friction between George and his girlfriend Julie?",
        "correct": "The Big Salad from Monk's diner",
        "wrong": ["A Cobb Salad with blue cheese dressing", "A bowl of Matzo ball soup with crackers", "A pastrami sandwich on sourdough bread"],
        "d": 1
    },
    {
        "q": "Why is George infuriated with Julie regarding the Big Salad bought for Elaine?",
        "correct": "Julie accepted Elaine's thank-you despite George paying for it",
        "wrong": ["Julie ordered expensive imported avocado without asking", "Julie ate half of Elaine's imported gourmet cherry tomatoes on the walk back", "Julie forgot to request the dressing on the side"],
        "d": 1
    },
    {
        "q": "In 'The Pledge Drive', what candy bar does Mr. Pitt eat with a knife and fork, starting a bizarre trend?",
        "correct": "A Snickers chocolate bar",
        "wrong": ["A Milky Way caramel bar", "A 3 Musketeers nougat bar", "A Butterfinger crisp bar"],
        "d": 1
    },
    {
        "q": "Why does Jerry's grandmother Nana write him dozens of tiny checks in 'The Pledge Drive'?",
        "correct": "She suffers from progressive memory loss",
        "wrong": ["She thinks Jerry is struggling as an accountant", "She gives him five dollars for every phone call", "She sends him royalties from an old family trust"],
        "d": 3
    },
    {
        "q": "In 'The Chinese Woman', what is the actual cultural background of George's phone date Donna Chang?",
        "correct": "She is a white woman from Long Island whose name was shortened",
        "wrong": ["She is a second-generation Taiwanese immigrant from Queens", "She is an exchange student studying literature at the University of Hong Kong", "She is a third-generation Chinese-American pediatrician"],
        "d": 1
    },
    {
        "q": "What undergarment invention do Kramer and Frank Costanza create for men needing support?",
        "correct": "\"The Manssiere\" (or \"The Bro\")",
        "wrong": ["\"The Chest Guard Vest\"", "\"The Male Athletic Corset\"", "\"The Torso Support Sling\""],
        "d": 1
    },
    {
        "q": "What dispute between Kramer and Frank Costanza derails their marketing of the male bra?",
        "correct": "They cannot agree on whether to call it 'The Bro' or 'The Manssiere'",
        "wrong": ["They couldn't secure a patent from the United States Patent Office", "Frank refused to allow George to model the prototype garment", "Kramer insisted on manufacturing the product exclusively in Latvia"],
        "d": 3
    },
    {
        "q": "In 'The Couch', what does Poppie do to Jerry's brand-new living room sofa?",
        "correct": "He accidentally urinates on the cushion due to a medical condition",
        "wrong": ["He spills an entire bowl of steaming hot marinara sauce across the fabric", "He tears the delicate velvet fabric with his heavy ring", "He leaves a permanent cigar burn hole right on the armrest"],
        "d": 1
    },
    {
        "q": "What political topic divides Jerry, Elaine, and Poppie in 'The Couch'?",
        "correct": "The legal right to abortion",
        "wrong": ["New York City rent control ordinances", "Mandatory federal recycling programs", "Funding for the National Endowment for the Arts"],
        "d": 2
    },
    {
        "q": "In 'The Gymnast', what food item does George eat directly out of the trash can at his girlfriend's mother's house?",
        "correct": "An éclair resting on top of a magazine",
        "wrong": ["A half-eaten slice of raspberry cheesecake", "A chocolate cream puff in a paper wrapper", "A leftover gourmet powdered jelly donut"],
        "d": 1
    },
    {
        "q": "What defense does George give to Jerry when caught eating an éclair out of the garbage?",
        "correct": "\"It was hovering above the rim! It was on a magazine!\"",
        "wrong": ["\"It was completely untouched by human hands!\"", "\"Trash is merely a social construct created by society!\"", "\"Food that is still wrapped cannot be considered waste!\""],
        "d": 2
    },
    {
        "q": "What nationality is Jerry's Olympic gymnast girlfriend Katya in 'The Gymnast'?",
        "correct": "Romanian",
        "wrong": ["Bulgarian", "Russian", "Hungarian"],
        "d": 3
    },
    {
        "q": "In 'The Mom & Pop Store', whose celebrity Chrysler LeBaron does George believe he purchased?",
        "correct": "Actor Jon Voight",
        "wrong": ["Actor Dustin Hoffman", "Singer Billy Joel", "Comedian Woody Allen"],
        "d": 1
    },
    {
        "q": "What clue inside the glove compartment reveals that George's car belonged to 'John' Voight the periodontist?",
        "correct": "A prescription pad and an owner's manual signed with an 'h'",
        "wrong": ["A complete medical license registration receipt from the state of New York", "A dental floss container printed with a practice logo", "An appointment scheduling book from Manhattan Dental"],
        "d": 3
    },
    {
        "q": "What Macy's Thanksgiving Day Parade balloon does Jerry puncture in 'The Mom & Pop Store'?",
        "correct": "The Woody Woodpecker balloon",
        "wrong": ["The Bullwinkle Moose balloon", "The Snoopy as the Astronaut balloon", "The Mighty Mouse balloon"],
        "d": 3
    },
    {
        "q": "In 'The Soup', what does hack comic Kenny Bania offer to give Jerry in exchange for a dinner?",
        "correct": "A brand-new brand-name Armani suit",
        "wrong": ["A vintage tailored cashmere sports jacket", "Front row tickets to the David Letterman show", "A vintage leather weekend duffel bag"],
        "d": 1
    },
    {
        "q": "What argument erupts between Jerry and Bania at Mendy's restaurant in 'The Soup'?",
        "correct": "Whether soup ordered with crackers qualifies as a full meal",
        "wrong": ["Whether Jerry is obligated to introduce Bania to his talent agent", "Whether ordering appetizers counts against their dinner agreement", "Whether Mendy's swordfish is superior to their prime rib"],
        "d": 1
    },
    {
        "q": "In 'The Secretary', why does George pay his new secretary Ada higher wages than his own salary?",
        "correct": "He was blinded by desire and promised her massive raises",
        "wrong": ["The Yankees collective bargaining agreement mandated the rate", "Steinbrenner personally ordered a mandatory departmental raise", "She threatened to expose his nap habit to management"],
        "d": 3
    },
    {
        "q": "In 'The Switch', what romantic arrangement does Jerry attempt to propose to his girlfriend and her roommate?",
        "correct": "A ménage à trois (a threesome)",
        "wrong": ["An open relationship without mutual jealousy", "Moving into a shared three-bedroom apartment", "A double date with George and a fashion model"],
        "d": 1
    },
    {
        "q": "According to George, why is pulling off 'The Switch' considered nearly impossible in human history?",
        "correct": "\"In the entire history of the world, no one has ever pulled off the switch!\"",
        "wrong": ["\"Human jealousy prevents multiple partners from cooperating peacefully!\"", "\"Women can sense manipulation across entire city blocks!\"", "\"The logistics alone require military precision and divine luck!\""],
        "d": 3
    },
    {
        "q": "In 'The Label Maker', what gift does Tim Whatley give Jerry that Elaine originally gave to Whatley?",
        "correct": "A desktop label maker device",
        "wrong": ["A set of silver-plated ballpoint pens", "An electric wine bottle cork extractor", "A leather-bound desktop calendar planner"],
        "d": 1
    },
    {
        "q": "What term does Elaine coin in 'The Label Maker' to describe someone who gives away a received gift?",
        "correct": "A \"regifter\"",
        "wrong": ["A \"pass-alonger\"", "A \"recycle-giver\"", "A \"frugal-swapper\""],
        "d": 1
    },
    {
        "q": "What board game do Kramer and Newman play obsessively on the subway in 'The Label Maker'?",
        "correct": "Risk",
        "wrong": ["Battleship", "Stratego", "Monopoly"],
        "d": 1
    },
    {
        "q": "What country does a Ukrainian subway passenger defend when Kramer insults it in 'The Label Maker'?",
        "correct": "Ukraine",
        "wrong": ["Poland", "Lithuania", "Romania"],
        "d": 3
    },
    {
        "q": "In 'The Beard', what does George start wearing that dramatically boosts his dating confidence?",
        "correct": "A custom toupee hairpiece",
        "wrong": ["A pair of designer sunglasses indoors", "A custom tailored European leather jacket", "Elevated platform dress shoes with thick soles"],
        "d": 1
    },
    {
        "q": "What does Elaine do with George's toupee when she becomes fed up with his newfound arrogance in 'The Beard'?",
        "correct": "She rips it off his head and throws it out Jerry's window",
        "wrong": ["She drops it into a pot of boiling pasta water", "She flushes the expensive custom hairpiece down the apartment bathroom toilet", "She cuts it into pieces with kitchen shears"],
        "d": 1
    },
    {
        "q": "What does George scream in utter despair after Elaine throws his toupee out the window?",
        "correct": "\"I'm hairless, Jerry! Hairless!\"",
        "wrong": ["\"My confidence is ruined forever!\"", "\"You destroyed three hundred dollars worth of hair!\"", "\"I cannot face the world without my piece!\""],
        "d": 2
    },
    {
        "q": "In 'The Kiss Hello', what tenant policy does Kramer institute in the lobby of Jerry's apartment building?",
        "correct": "Posting photos of every building resident so neighbors greet each other",
        "wrong": ["Installing a surveillance camera outside every apartment door", "Setting up a communal espresso bar by the mailboxes", "Banning all commercial outside food delivery drivers from entering the lobby"],
        "d": 3
    },
    {
        "q": "In 'The Doorman', who plays Mr. Pitt's manipulative, mind-game playing residential doorman?",
        "correct": "Larry Miller",
        "wrong": ["Character actor Kevin Nealon", "Richard Kind", "Jon Lovitz"],
        "d": 3
    },
    {
        "q": "In 'The Jimmy', what peculiar speech habit does Elaine's gym acquaintance Jimmy have?",
        "correct": "He constantly refers to himself in the third person",
        "wrong": ["He speaks exclusively in rhyming poetic couplets", "He whispers every sentence before repeating it loudly", "He ends every sentence by asking rhetorical questions"],
        "d": 1
    },
    {
        "q": "What specialized footwear does Jimmy wear that improves vertical leaping ability?",
        "correct": "Plyometric training shoes with elevated platforms",
        "wrong": ["Heavy weighted resistance sprint boots with ankle straps", "Pneumatic air-pump running sneakers", "Spring-loaded agility workout shoes"],
        "d": 3
    },
    {
        "q": "Why is Kramer mistaken for an individual with developmental disabilities at the AMCA benefit banquet in 'The Jimmy'?",
        "correct": "Dental anesthesia numbed his face and he wore Jimmy's platform shoes",
        "wrong": ["He suffered a mild concussion from slipping on wet tiles", "He forgot his glasses and bumped into tables repeatedly", "He had an acute allergic reaction to restaurant seafood that slurred his speech"],
        "d": 1
    },
    {
        "q": "What legendary singer performs 'When You're Smiling' for Kramer at the benefit banquet in 'The Jimmy'?",
        "correct": "Mel Tormé",
        "wrong": ["Tony Bennett", "Vic Damone", "Bobby Darin"],
        "d": 3
    },
    {
        "q": "In 'The Doodle', what caricature drawing does George's girlfriend Paula create that triggers his insecurities?",
        "correct": "A drawing of George with a giant papier-mâché nose",
        "wrong": ["A sketch depicting George completely bald with thick glasses", "A cartoon showing George stuffing his face with pastries", "A caricature showing George running away from a kitchen fire"],
        "d": 3
    },
    {
        "q": "In 'The Fusilli Jerry', what pasta creation does Kramer craft as a gift for Jerry?",
        "correct": "A small statuette of Jerry sculpted from fusilli pasta",
        "wrong": ["A miniature portrait of Jerry made from dried macaroni", "A pasta model of Jerry's apartment built from lasagna sheets", "A bust of Jerry Seinfeld sculpted from linguine and glue"],
        "d": 1
    },
    {
        "q": "What vanity license plate does the New York DMV mistakenly issue to Kramer in 'The Fusilli Jerry'?",
        "correct": "\"ASSMAN\"",
        "wrong": ["\"KRAMER\"", "\"HIPSTER\"", "\"COSMO\""],
        "d": 1
    },
    {
        "q": "What freak physical injury does Frank Costanza suffer involving the Fusilli Jerry statuette?",
        "correct": "He falls backwards and lands directly on top of the pasta sculpture",
        "wrong": ["He bites into the raw pasta and chips his front dental crown", "He steps barefoot onto the dried pasta base in the dark", "He drops the heavy dried pasta sculpture onto his bare foot and fractures his toe"],
        "d": 1
    },
    {
        "q": "What comment does the proctologist make when examining Frank Costanza in 'The Fusilli Jerry'?",
        "correct": "\"Million to one shot, doc. Million to one.\"",
        "wrong": ["\"This is the fifth pasta accident I have treated this month.\"", "\"You would be astonished what people manage to fall upon.\"", "\"Modern art belongs in museums, not in private examinations.\""],
        "d": 2
    },
    {
        "q": "In 'The Face Painter', what sports team does David Puddy support by painting his face as a devil?",
        "correct": "The New Jersey Devils hockey team",
        "wrong": ["The New York Rangers hockey team", "The New York Islanders hockey franchise", "The Philadelphia Flyers hockey club"],
        "d": 1
    },
    {
        "q": "What catchphrase does David Puddy aggressively bark while sporting his devil face paint?",
        "correct": "\"Gotta support the team!\"",
        "wrong": ["\"Devils rule the ice!\"", "\"Don't mess with Jersey!\"", "\"Victory or death!\""],
        "d": 1
    },
    {
        "q": "What Broadway musical star gets injured in a softball collision involving George in 'The Understudy'?",
        "correct": "Bette Midler",
        "wrong": ["Bernadette Peters", "Patti LuPone", "Liza Minnelli"],
        "d": 2
    },
    {
        "q": "What musical adaptation is Bette Midler starring in during 'The Understudy'?",
        "correct": "Rochelle, Rochelle: The Musical",
        "wrong": ["Prognosis Negative: On Broadway", "CheckMate: The Musical Spectacle", "Chow Fun: The American Premiere"],
        "d": 3
    },
    {
        "q": "In 'The Diplomat's Club', why does George go to absurd lengths to befriend Mr. Morgan at Yankee Stadium?",
        "correct": "To prove to Mr. Morgan that he is not racially prejudiced",
        "wrong": ["To secure complimentary box tickets for the World Series", "To convince Morgan to write him a promotion recommendation", "To get advice on buying an executive apartment in the Bronx"],
        "d": 3
    },
    {
        "q": "In 'The Chaperone', what does Kramer do to Miss Rhode Island's evening gown on the night of the pageant?",
        "correct": "He accidentally burns a massive hole with a clothing iron",
        "wrong": ["He spills hot tea down the delicate silk bodice", "He tears the entire formal hemline while trying to shorten the length with scissors", "He stains the collar with dark shoe polish wax"],
        "d": 3
    },
    {
        "q": "In 'The Kiss Hello', what medical condition causes Kramer to demand physical greetings from everyone?",
        "correct": "He believes genuine human affection promotes longevity and health",
        "wrong": ["He was diagnosed with severe social deprivation syndrome", "His holistic healer ordered him to hug twelve people daily", "He read a study proving physical touch eliminates common colds"],
        "d": 3
    },
    {
        "q": "In 'The Doorman', what valuable piece of furniture is stolen while Jerry covers the doorman's post?",
        "correct": "A valuable lobby couch belonging to the apartment building",
        "wrong": ["An antique mahogany parcel table from the main foyer", "A brass sculpture of an eagle gifted by the building founder", "A set of four imported Italian leather waiting armchairs"],
        "d": 3
    },
    {
        "q": "In 'The Understudy', who steps in as Bette Midler's understudy in 'Rochelle, Rochelle'?",
        "correct": "Gennice, Jerry's emotional girlfriend who cries at trivial things",
        "wrong": ["Elaine Benes, who memorized the entire musical score", "Karen, the former Miss Rhode Island beauty contestant from the pageant", "Laura, the deaf lineswoman with perfect stage presence"],
        "d": 3
    },
    {
        "q": "In 'The Fusilli Jerry', what does proctologist Dr. Cooperman proudly call himself?",
        "correct": "The real \"Assman\"",
        "wrong": ["The Rear Admiral", "The Bottom Line", "The Tailgate Specialist"],
        "d": 3
    },

    # --- SEASON 7 HIGHLIGHTS & TRAGIC CLIMAX (51-100) ---
    {
        "q": "In 'The Engagement', what pact do Jerry and George make at Monk's diner to change their lives?",
        "correct": "To mature, stop dating casually, and seek serious commitments",
        "wrong": ["To quit their current careers and launch a boutique Manhattan catering business", "To invest all their savings into Florida real estate condos", "To cut ties with Kramer and Newman for six months"],
        "d": 1
    },
    {
        "q": "Who does George immediately propose to after making the maturity pact in 'The Engagement'?",
        "correct": "Susan Ross",
        "wrong": ["Marla the virgin", "Paula the artist", "Diane DeConn"],
        "d": 1
    },
    {
        "q": "Why does George panic almost immediately after proposing marriage to Susan Ross in 'The Engagement'?",
        "correct": "Jerry backed out of the maturity pact after breaking up with his date",
        "wrong": ["Susan demanded they relocate immediately to suburban New Jersey", "Susan insisted on controlling their joint household finances", "Susan's wealthy parents demanded a strict prenuptial financial agreement in writing"],
        "d": 2
    },
    {
        "q": "In 'The Postponement', who leaks George's private anxieties about his engagement to everyone in the neighborhood?",
        "correct": "Rabbi Glickman",
        "wrong": ["Father Curtis", "Reverend Popovich", "Cantor Meyer"],
        "d": 3
    },
    {
        "q": "In 'The Maestro', what title does conductor Bob Cobb insist on being called by his friends?",
        "correct": "\"The Maestro\"",
        "wrong": ["\"The Virtuoso\"", "\"The Conductor\"", "\"The Maestro Di Musica\""],
        "d": 2
    },
    {
        "q": "What region in Italy does Bob Cobb claim has zero available rental villas when Jerry asks in 'The Maestro'?",
        "correct": "Tuscany",
        "wrong": ["Umbria", "Lombardy", "Campania"],
        "d": 2
    },
    {
        "q": "In 'The Wink', what fruit juice squirts into George's eye, causing involuntary winking?",
        "correct": "Grapefruit juice",
        "wrong": ["Fresh squeezed tart lemon juice", "Orange juice", "Lime juice"],
        "d": 2
    },
    {
        "q": "What unintended consequence occurs when George winks at coworkers in 'The Wink'?",
        "correct": "People interpret his statements as secret, knowing conspiracies",
        "wrong": ["Colleagues believe he is developing an acute neurological tremor", "His supervisor suspects he is mocking company productivity goals", "Susan assumes he is secretly planning an exotic honeymoon surprise"],
        "d": 2
    },
    {
        "q": "In 'The Hot Tub', what runner from Trinidad and Tobago stays with Jerry before the New York City Marathon?",
        "correct": "Jean-Paul Jean-Paul",
        "wrong": ["Ato Boldon", "Dwight Phillips", "Olympic gold medalist Donovan Bailey"],
        "d": 3
    },
    {
        "q": "Why did Jean-Paul Jean-Paul famously miss his marathon race at the previous Olympic Games?",
        "correct": "He overslept because his alarm clock failed to go off",
        "wrong": ["He suffered severe food poisoning from street vendor food", "His official race registration bib was stolen from his room", "He got trapped inside an automatic hotel elevator car"],
        "d": 2
    },
    {
        "q": "In 'The Soup Nazi', what is the strict ordering procedure demanded by soup vendor Yev Kassem?",
        "correct": "Pick your soup, have money ready, step to the extreme right, and move",
        "wrong": ["Place orders in writing on paper slips and wait outside", "Greet the chef in German, order in numerical sequence, and bow", "Remain completely silent until pointed at by the chef, pay exact cash, and leave"],
        "d": 1
    },
    {
        "q": "What legendary catchphrase does the Soup Nazi bark when a customer disobeys his strict rules?",
        "correct": "\"No soup for you!\"",
        "wrong": ["\"Get out of my line!\"", "\"You have been banned!\"", "\"Soup privileges revoked!\""],
        "d": 1
    },
    {
        "q": "What piece of furniture does Kramer try to guard on the street for Elaine in 'The Soup Nazi'?",
        "correct": "An antique wooden armoire",
        "wrong": ["A Victorian dressing vanity table", "A French provincial headboard frame", "A hand-carved mahogany bookcase"],
        "d": 3
    },
    {
        "q": "How does Elaine bring down the Soup Nazi's business at the conclusion of 'The Soup Nazi'?",
        "correct": "She discovers his secret handwritten soup recipes inside the armoire",
        "wrong": ["She reports his kitchen health code violations to inspectors", "She stages an aggressive consumer boycott outside his storefront with protest leaflets", "She convinces Monk's diner to serve identical soups at half price"],
        "d": 2
    },
    {
        "q": "In 'The Secret Code', what is George's top secret four-letter ATM bank card password?",
        "correct": "\"BOSCO\"",
        "wrong": ["\"OVALTINE\"", "\"YANKEE\"", "\"VANDELAY\""],
        "d": 1
    },
    {
        "q": "What dying words does J. Peterman's elderly mother repeat over and over in 'The Secret Code'?",
        "correct": "\"Bosco! Bosco!\"",
        "wrong": ["\"Elaine! Elaine!\"", "\"Sombrero! Sombrero!\"", "\"Burma! Burma!\""],
        "d": 3
    },
    {
        "q": "In 'The Pool Guy', what telephone movie listing service does Kramer accidentally mimic when his phone number is similar?",
        "correct": "Moviefone (555-FILK)",
        "wrong": ["CinemaGuide (555-FILM)", "FilmPass (555-TICK)", "ShowFinder (555-THEA)"],
        "d": 3
    },
    {
        "q": "What greeting does Kramer say when pretending to be the Moviefone automated operator?",
        "correct": "\"Hello, and welcome to Moviefone!\"",
        "wrong": ["\"Greetings, moviegoers across Manhattan!\"", "\"Welcome to New York's ultimate cinema hotline!\"", "\"Thanks for dialing Hollywood's premiere phone guide!\""],
        "d": 2
    },
    {
        "q": "What does George fear will happen when Susan becomes friends with Jerry and Elaine in 'The Pool Guy'?",
        "correct": "\"Worlds are colliding! George is getting upset!\"",
        "wrong": ["\"My boundaries are evaporating before my eyes!\"", "\"My entire identity is being dismantled by my fiancé!\"", "\"There will be no sanctuary left in my life!\""],
        "d": 2
    },
    {
        "q": "In 'The Sponge', why does Elaine go on a frantic quest across Manhattan pharmacies?",
        "correct": "Her favorite brand of contraceptive sponge has been discontinued",
        "wrong": ["Her prescription daily allergy medication was permanently removed from pharmacy shelves", "A specialty imported hair conditioner was pulled by suppliers", "A rare homeopathic throat lozenge was banned by inspectors"],
        "d": 1
    },
    {
        "q": "What question does Elaine rigorously ask herself before consenting to intimacy in 'The Sponge'?",
        "correct": "\"Is he sponge-worthy?\"",
        "wrong": ["\"Is he worthy of my stock?\"", "\"Does he meet the standard?\"", "\"Is this relationship premium?\""],
        "d": 1
    },
    {
        "q": "In 'The Gum', what does Lloyd Braun buy an absurd quantity of to convince people he is sane?",
        "correct": "Chinese chewing gum",
        "wrong": ["Imported licorice twists", "Spearmint breath lozenges", "Wintergreen dental drops"],
        "d": 2
    },
    {
        "q": "What line does Kramer famously deliver about Lloyd Braun's chewing gum in 'The Gum'?",
        "correct": "\"That's a lot of gum!\"",
        "wrong": ["\"That is an immense amount of mint!\"", "\"Nobody chews that much gum!\"", "\"That's an Olympic quantity of gum!\""],
        "d": 3
    },
    {
        "q": "In 'The Rye', what specialty loaf of bread do George's parents bring to dinner at Susan's parents' townhouse?",
        "correct": "A marble rye from Schnitzer's bakery",
        "wrong": ["A braided challah from Zabar's gourmet deli", "A sourdough baguette from Eli's Manhattan bakehouse", "A pumpernickel loaf from Orwashers bakery"],
        "d": 3
    },
    {
        "q": "Why does Frank Costanza take the marble rye back after dinner in 'The Rye'?",
        "correct": "Susan's parents failed to serve the bread with the dinner meal",
        "wrong": ["Mrs. Ross made a derogatory public comment about cheap bakeries located in Queens", "Mr. Ross accidentally dropped the loaf on the dining room rug", "Frank noticed Susan's father had already hidden the loaf away"],
        "d": 2
    },
    {
        "q": "How does Jerry acquire the last marble rye from an elderly woman, Mabel Choate, on the street?",
        "correct": "He snatches it from her hands and runs away screaming",
        "wrong": ["He bids one hundred dollars cash in the bakery aisle", "He trades an expensive cashmere scarf for the bread bag", "He claims he needs it for an emergency theatrical production"],
        "d": 2
    },
    {
        "q": "How does George attempt to hoist the replacement marble rye into Susan's parents' third-story window?",
        "correct": "Using a deep-sea fishing pole and hook from the street",
        "wrong": ["Using an extendable twenty-foot aluminum painter's utility ladder", "Using a mechanical rope pulley tied to a roof drain", "Tying the bakery bag to helium party balloons"],
        "d": 3
    },
    {
        "q": "In 'The Caddy', what fashion habit of candy heiress Sue Ellen Mischke causes a massive car crash?",
        "correct": "Walking down the sidewalk wearing only a bra as a top",
        "wrong": ["Wearing blinding reflective mirrored sunglasses in traffic", "Walking a pair of massive Afghan hounds into traffic lanes", "Riding a bicycle while wearing an oversized feathered hat"],
        "d": 2
    },
    {
        "q": "Who serves as Kramer's eccentric personal advisor on golf and legal strategy in 'The Caddy'?",
        "correct": "Stan the Caddy",
        "wrong": ["Maestro Bob Cobb", "Cousin Jeffrey", "Izzy Mandelbaum"],
        "d": 2
    },
    {
        "q": "In 'The Caddy', what courtroom blunder mimics the O.J. Simpson murder trial?",
        "correct": "Demanding Sue Ellen try the bra on over her clothing, which doesn't fit",
        "wrong": ["Presenting a bloody leather glove found behind a golf clubhouse", "Introducing a pair of luxury Bruno Magli Italian dress shoes as crucial evidence", "Cross-examining a police detective regarding racial slurs"],
        "d": 3
    },
    {
        "q": "What legal declaration does attorney Jackie Chiles make when the bra doesn't fit over Sue Ellen's clothes?",
        "correct": "\"A bra's gotta fit right up against a person's skin! Like a glove!\"",
        "wrong": ["\"If the bra will not adhere, the charges must disappear!\"", "\"No court can convict a client when the fabric does not cling!\"", "\"The garment must clasp, or the court must release its grasp!\""],
        "d": 2
    },
    {
        "q": "In 'The Seven', what number does George insist is the absolute greatest name for a child?",
        "correct": "Seven (honoring baseball icon Mickey Mantle)",
        "wrong": ["Eleven (honoring basketball legend Bob Cousy)", "Three (honoring baseball slugger Babe Ruth)", "Nine (honoring baseball legend Ted Williams)"],
        "d": 2
    },
    {
        "q": "In 'The Shower Head', why are Jerry, Kramer, and Newman furious about their apartment building's renovations?",
        "correct": "Low-flow shower heads were installed, reducing water pressure",
        "wrong": ["The hot water supply was shut off after ten in the evening", "The building converted from gas heating to noisy radiator units", "Water meters were installed in every single unit's bathroom"],
        "d": 2
    },
    {
        "q": "What black market high-powered shower head do Kramer and Newman procure from the back of a van?",
        "correct": "The Commando 8 (manufactured for commercial elephants)",
        "wrong": ["The Hydro-Max 5000 industrial pressurized pipeline nozzle attachment", "The Niagara Power-Blast commercial carwash nozzle", "The Fire-Hose Extreme industrial sanitation head"],
        "d": 2
    },
    {
        "q": "In 'The Doll', what object in Susan's collection bears an eerie, terrifying resemblance to George's mother Estelle?",
        "correct": "A vintage porcelain collectible doll",
        "wrong": ["A framed needlepoint portrait from Susan's grandmother", "A hand-carved marionette puppet from Switzerland", "A ceramic cookie jar shaped like a middle-aged woman"],
        "d": 2
    },
    {
        "q": "In 'The Friars Club', what prestigious jacket does Jerry borrow for an event and accidentally lose?",
        "correct": "A Friars Club crest blazer jacket",
        "wrong": ["A Harvard Club burgundy tweed sport coat", "An Lambs Club vintage embroidered wool dinner coat", "A Lambs Club official member dinner tuxedo jacket"],
        "d": 2
    },
    {
        "q": "What eccentric sleep experiment does Kramer undertake in 'The Friars Club'?",
        "correct": "Polyphasic sleep (twenty-minute naps every two hours)",
        "wrong": ["Sleeping exclusively on hardwood floors without pillows", "Hypnotherapy sessions designed to induce lucid dreaming", "Staying awake for seventy-two consecutive hours every week"],
        "d": 2
    },
    {
        "q": "In 'The Wig Master', what fabulous piece of theatrical clothing does Kramer wear around Manhattan?",
        "correct": "The colorful Technicolor Dreamcoat from a Broadway tour",
        "wrong": ["A royal velvet cape from The King and I revival", "A gold lamé tuxedo jacket from Phantom of the Opera", "A sequined tuxedo blazer from a touring production of Chicago"],
        "d": 2
    },
    {
        "q": "What does the NYPD mistake Kramer for when he wears the Technicolor Dreamcoat and a feathered hat?",
        "correct": "A high-rolling urban pimp",
        "wrong": ["An escaped mental asylum patient", "A street performance drag artist", "An undercover foreign drug runner"],
        "d": 2
    },
    {
        "q": "In 'The Calzone', what food does George purchase daily for George Steinbrenner from Paisano's?",
        "correct": "An authentic Italian eggplant and cheese calzone",
        "wrong": ["A deep-dish meatball, pepperoni, and Italian sausage stromboli roll", "A wood-fired four-cheese personal pizza slice", "A hot pastrami and provolone toasted panini"],
        "d": 2
    },
    {
        "q": "Why does George get banned from Paisano's pizzeria in 'The Calzone'?",
        "correct": "He tried to put tip money in the jar, took it back to be seen, and was caught",
        "wrong": ["He complained loudly about stale dough in front of lunchtime patrons", "He tried to pay for calzones using expired supermarket coupons", "He demanded a corporate volume discount on behalf of the Yankees"],
        "d": 2
    },
    {
        "q": "In 'The Bottle Deposit', what scheme do Kramer and Newman devise to make massive recycling profits?",
        "correct": "Hauling thousands of bottles to Michigan for a ten-cent deposit",
        "wrong": ["Collecting discarded aluminum soda cans from recycling bins all across Central Park", "Smuggling empty glass bottles into Canada for deposit refund", "Falsifying return receipts at Manhattan supermarket machines"],
        "d": 2
    },
    {
        "q": "What vehicle do Kramer and Newman use to transport their massive bottle haul to Michigan?",
        "correct": "A United States Postal Service mail truck loaded for Mother's Day",
        "wrong": ["An overloaded commercial U-Haul moving box truck", "An abandoned commercial refrigeration delivery truck Kramer rented from a friend", "A flatbed agricultural transport truck borrowed from upstate"],
        "d": 2
    },
    {
        "q": "In 'The Bottle Deposit', what prized historical sports memorabilia is inside Jerry's stolen Saab trunk?",
        "correct": "John F. Kennedy's antique personal golf clubs",
        "wrong": ["Babe Ruth's original game-used autographed wooden bat", "Mickey Mantle's 1956 Triple Crown championship ring", "Vince Lombardi's handwritten Super Bowl play diagram notebook"],
        "d": 2
    },
    {
        "q": "Who steals Jerry's Saab with JFK's golf clubs in 'The Bottle Deposit'?",
        "correct": "Tony, Jerry's obsessed, possessive car mechanic",
        "wrong": ["Grossbard, George's long-lost high school nemesis", "Mike Moffitt, who owed Jerry bookmaking money", "Joe Davola, seeking revenge against Jerry"],
        "d": 2
    },
    {
        "q": "In 'The Invitations', what wedding planning task does George take charge of to save money?",
        "correct": "Purchasing the cheapest possible wedding invitations",
        "wrong": ["Booking an uncertified amateur wedding photographer", "Hiring an inexpensive accordion trio for the reception", "Ordering discounted expired bulk sparkling wine"],
        "d": 2
    },
    {
        "q": "What tragic fate befalls Susan Ross in the Season 7 finale 'The Invitations'?",
        "correct": "She dies from licking the toxic adhesive on the cheap envelopes",
        "wrong": ["She suffers fatal injuries in a collapse of the wedding tent", "She contracts severe food poisoning from expired seafood samples", "She is struck by an errant golf cart on the country club course"],
        "d": 2
    },
    {
        "q": "What is George's chillingly indifferent reaction upon learning Susan has passed away in the hospital?",
        "correct": "He asks Jerry and Elaine, \"Well, let's get some coffee.\"",
        "wrong": ["He immediately asks if the wedding deposit can be refunded", "He checks his watch and asks if the movie is still playing", "He asks the nurse where he can validate his parking ticket"],
        "d": 2
    },
    {
        "q": "What does George immediately do the next morning after Susan's untimely passing?",
        "correct": "He calls Marla the virgin to see if she is available to date",
        "wrong": ["He applies for a luxury bachelor apartment on the Upper West Side", "He goes shopping for expensive imported sports jackets", "He books a solo vacation cruise to the Caribbean islands"],
        "d": 2
    },
    {
        "q": "In 'The Invitations', who informs Susan's wealthy parents that Susan has died?",
        "correct": "George, Jerry, Elaine, and Kramer at the hospital",
        "wrong": ["The attending emergency room physician in the waiting room", "A hospital chaplain who delivers the tragic notification", "The hospital administrative supervisor via an emergency phone call"],
        "d": 2
    }
]

if __name__ == "__main__":
    out = assemble_batch(raw_questions, 3)
    save_json(out, "tools/staging/seinfeld_batch3.json")
