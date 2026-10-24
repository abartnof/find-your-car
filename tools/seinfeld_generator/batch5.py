import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from utils import assemble_batch, save_json

raw_questions = [
    # --- FRANK & ESTELLE COSTANZA (1-20) ---
    {
        "q": "Which veteran comedic actor played George's explosive, short-tempered father, Frank Costanza?",
        "correct": "Jerry Stiller",
        "wrong": ["Jack Carter", "Character actor Harold Gould", "Alan King"],
        "d": 1
    },
    {
        "q": "Which actress brilliantly portrayed George's high-strung, shrill mother, Estelle Costanza?",
        "correct": "Estelle Harris",
        "wrong": ["Sitcom veteran Doris Roberts", "Liz Sheridan", "Charlotte Rae"],
        "d": 1
    },
    {
        "q": "What annoying driving habit does Frank Costanza accuse Kramer of doing with Estelle in his car?",
        "correct": "\"Stopping short\" (reaching an arm across the passenger)",
        "wrong": ["Tailgating municipal transit buses on the Queensboro Bridge", "Failing to engage the handbrake on steep street hills", "Honking the horn aggressively at every green traffic light"],
        "d": 1
    },
    {
        "q": "What prized vintage coin collection does Frank Costanza obsessively keep in his house?",
        "correct": "A collection of rare silver dollars",
        "wrong": ["A chest of mint-condition Indian head pennies", "A binder of uncirculated Mercury dimes", "A jar of pre-war buffalo nickels from Chicago"],
        "d": 3
    },
    {
        "q": "What room in the Costanza home does Frank turn into his private bachelor sanctuary?",
        "correct": "A billiard game room with a full pool table",
        "wrong": ["A private home cigar smoking lounge", "A basement workshop for making custom cabana shirts", "A darkroom for developing vintage black-and-white prints"],
        "d": 3
    },
    {
        "q": "What casual resort clothing line does Frank Costanza proudly wear around New York?",
        "correct": "Vintage cabana resort shirts and shorts sets",
        "wrong": ["Hawaiian floral print button-down rayon shirts", "Velour leisure athletic tracksuits with stripes", "Embroidered linen bowling team jerseys"],
        "d": 2
    },
    {
        "q": "What medical procedure does Estelle Costanza undergo before declaring 'I'm out there, George!'?",
        "correct": "Corrective eye surgery on both of her eyes",
        "wrong": ["A cosmetic facial rejuvenation facelift", "A dental bridge installation procedure", "A knee replacement physical therapy session"],
        "d": 2
    },
    {
        "q": "What game does Estelle Costanza regularly play with her neighborhood friends in Queens?",
        "correct": "Competitive mahjong with tiles",
        "wrong": ["Canasta card tournaments", "Contract bridge at the community center", "Scrabble at the local bakery"],
        "d": 2
    },
    {
        "q": "What battle challenge does Frank Costanza scream when challenged to a physical fight by Elaine?",
        "correct": "\"You want a piece of me?! You got it!\"",
        "wrong": ["\"Step outside right now if you dare!\"", "\"Nobody talks to a Costanza like that!\"", "\"I will drop you right where you stand!\""],
        "d": 1
    },
    {
        "q": "What baseball trade does Frank Costanza furiously berate George Steinbrenner about in George's living room?",
        "correct": "Trading away power hitter Jay Buhner to the Seattle Mariners",
        "wrong": ["Failing to re-sign slugger Don Mattingly to a contract", "Trading away pitching ace David Cone to Kansas City", "Letting superstar leadoff hitter Rickey Henderson walk away in free agency"],
        "d": 1
    },
    {
        "q": "What foreign language did Frank Costanza learn during his military service that he speaks fluently?",
        "correct": "Korean",
        "wrong": ["Japanese", "Tagalog", "Vietnamese"],
        "d": 3
    },
    {
        "q": "Why does Estelle Costanza refuse to eat paella prepared by Frank Costanza?",
        "correct": "She claims it is a monstrous concoction of strange meats and yellow rice",
        "wrong": ["She was diagnosed with an acute allergic reaction to imported saffron", "She insists genuine Spanish paella must never contain commercial shellfish", "She refuses to eat any hot meal cooked after six in the evening"],
        "d": 3
    },
    {
        "q": "What does Estelle Costanza do when she catches George in a compromising position with Glamour magazine?",
        "correct": "She falls to the floor and throws her back out in shock",
        "wrong": ["She faints onto the sofa and drops her grocery bags", "She runs screaming into the street to notify the neighbors", "She locks herself inside the guest bedroom for twenty-four hours"],
        "d": 1
    },
    {
        "q": "What vehicle does Frank Costanza drive throughout most of the series?",
        "correct": "A blue Ford Granada sedan",
        "wrong": ["A brown Buick LeSabre sedan", "A green Plymouth Valiant sedan", "A beige Chevrolet Caprice station wagon"],
        "d": 3
    },
    {
        "q": "In which New York City borough do Frank and Estelle Costanza reside?",
        "correct": "Queens (Flushing)",
        "wrong": ["Brooklyn (Bay Ridge)", "The Bronx (Riverdale)", "Staten Island (Todt Hill)"],
        "d": 1
    },
    {
        "q": "What does Frank Costanza refuse to take off his feet due to a phobia of barefoot contact?",
        "correct": "His shoes (he has a foot phobia)",
        "wrong": ["His woolen socks (he fears drafts)", "His rubber slippers (he fears static electricity)", "His leather moccasins (he fears wooden splinters)"],
        "d": 2
    },
    {
        "q": "What does Estelle Costanza buy George that she claims makes him look like a handsome young prince?",
        "correct": "A puffy green winter coat with a fur collar",
        "wrong": ["A double-breasted navy blazer with gold brass buttons", "A camel hair tailored trench coat from Macy's", "A patterned silk necktie with matching pocket square"],
        "d": 3
    },
    {
        "q": "Who was originally cast and filmed as Frank Costanza before Jerry Stiller reshot the scenes?",
        "correct": "John Randolph",
        "wrong": ["Veteran actor Jack Warden", "Vic Tayback", "Herb Edelman"],
        "d": 3
    },
    {
        "q": "What business venture did Frank Costanza pursue before retirement?",
        "correct": "Selling religious novelty items and cabana clothing",
        "wrong": ["Managing a regional wholesale plumbing fixture warehouse", "Operating an independent dry cleaning franchise in Queens", "Working as a senior claims adjuster for MetLife insurance"],
        "d": 3
    },
    {
        "q": "What does Frank Costanza shout when celebrating the successful completion of Festivus feats?",
        "correct": "\"Another Festivus miracle!\"",
        "wrong": ["\"Festivus reigns supreme once again!\"", "\"Strength and honor have prevailed tonight!\"", "\"The pole has blessed our household!\""],
        "d": 1
    },

    # --- MORTY & HELEN SEINFELD (21-35) ---
    {
        "q": "Which actor portrayed Jerry's father, Morty Seinfeld, for the vast majority of the series?",
        "correct": "Barney Martin",
        "wrong": ["Phil Bruns", "Character actor Harold Gould", "Ralph Bellamy"],
        "d": 1
    },
    {
        "q": "Which actress played Jerry's loving, fiercely protective mother, Helen Seinfeld?",
        "correct": "Liz Sheridan",
        "wrong": ["Sitcom veteran Doris Roberts", "Marion Ross", "Audra Lindley"],
        "d": 1
    },
    {
        "q": "What iconic question does Helen Seinfeld constantly ask whenever someone dislikes Jerry?",
        "correct": "\"How could anyone not like him?!\"",
        "wrong": ["\"What is wrong with people these days?!\"", "\"Who could possibly criticize my Jerry?!\"", "\"Why do people always have to be so judgmental?!\""],
        "d": 1
    },
    {
        "q": "What was Morty Seinfeld's proudest career achievement in the garment industry?",
        "correct": "Creating 'The Executive' beltless trench coat",
        "wrong": ["Inventing the wrinkle-free cotton dress shirt collar", "Designing the reversible lightweight rain jacket", "Patent-holding the concealed elastic waistband trouser"],
        "d": 1
    },
    {
        "q": "What luxury automobile does Jerry buy for his father that causes huge political uproar in Del Boca Vista?",
        "correct": "A brand-new Cadillac Fleetwood sedan",
        "wrong": ["A top-of-the-line Lincoln Continental town car", "A luxury Mercedes-Benz 300-class sedan", "A premium Lexus LS400 luxury sedan"],
        "d": 1
    },
    {
        "q": "Who is Morty Seinfeld's bitter political rival on the Del Boca Vista condominium board?",
        "correct": "Jack Klompus",
        "wrong": ["Arthur Blank", "Izzy Mandelbaum", "Lou Forestor"],
        "d": 1
    },
    {
        "q": "Why is Morty Seinfeld impeached from the presidency of the Del Boca Vista condo board?",
        "correct": "Accused of embezzling condo association funds to buy his Cadillac",
        "wrong": ["Violating strict community quiet hours with late-night pool games", "Failing to conduct open competitive bidding on private lawn maintenance contracts", "Allowing unregistered out-of-state guests to stay long-term"],
        "d": 2
    },
    {
        "q": "What missing personal item causes Morty to suspect everyone at Dr. Wexler's office of theft?",
        "correct": "His leather wallet filled with cash and cards",
        "wrong": ["His solid gold retirement wristwatch from the garment district", "His designer bifocal reading glasses in a leather case", "His official Del Boca Vista presidential election certificate"],
        "d": 2
    },
    {
        "q": "What financial gesture do Morty and Helen insist on making after Jerry buys them the Cadillac?",
        "correct": "Giving Jerry fifty dollars every time they see him to help his career",
        "wrong": ["Opening a secret trust fund bank account in his name in Miami", "Paying for his monthly health insurance premium in New York", "Sending him weekly commercial shipments of fresh Florida citrus fruit gift baskets"],
        "d": 2
    },
    {
        "q": "What was Morty Seinfeld's famous rule about never paying for anything when visiting restaurants?",
        "correct": "He insisted on fighting aggressively to pay the entire dinner check himself",
        "wrong": ["He calculated tips down to the exact mathematical percentage penny", "He demanded a senior citizen discount before ordering any beverage", "He refused to patronize any commercial dining establishment that required advance reservations"],
        "d": 2
    },
    {
        "q": "Who played Morty Seinfeld in his very first appearance in Season 1's 'The Stake Out'?",
        "correct": "Phil Bruns",
        "wrong": ["Barney Martin", "Jack Carter", "Herb Edelman"],
        "d": 3
    },
    {
        "q": "What Florida condominium development do the Seinfelds move to after leaving Del Boca Vista Phase 1?",
        "correct": "Del Boca Vista Phase 2",
        "wrong": ["Pines of Boca Raton Phase 4", "Century Village Gardens Phase 3", "Boca Del Mar Estates Phase 1"],
        "d": 3
    },
    {
        "q": "What gadget does Jack Klompus use to break the window of Jerry's Cadillac in Florida?",
        "correct": "A heavy rock thrown through the driver's side glass",
        "wrong": ["A crowbar pried against the door frame seam", "A golf club swung directly at the laminated windshield glass", "A tire iron from the trunk of his own vehicle"],
        "d": 3
    },
    {
        "q": "How much does Jack Klompus pay Morty for the Cadillac Fleetwood when Morty sells it in disgust?",
        "correct": "Six thousand dollars",
        "wrong": ["Four thousand dollars", "Ten thousand dollars", "Eight thousand dollars"],
        "d": 3
    },
    {
        "q": "What does Helen Seinfeld always warn Jerry about regarding his hygiene and health?",
        "correct": "Wearing a heavy jacket so he doesn't catch a cold",
        "wrong": ["Never eating seafood prepared in diners during summer months", "Always boiling tap water before drinking it in Manhattan", "Avoiding public restrooms in underground subway stations"],
        "d": 2
    },

    # --- UNCLE LEO & NEWMAN (36-55) ---
    {
        "q": "What famous greeting does Jerry's eccentric Uncle Leo shout whenever he spots Jerry in public?",
        "correct": "\"Jerry! Hello!\"",
        "wrong": ["\"Look who it is!\"", "\"My favorite nephew!\"", "\"Jerry, my boy!\""],
        "d": 1
    },
    {
        "q": "Which actor portrayed the unforgettable, loud-talking Uncle Leo throughout the series?",
        "correct": "Len Lesser",
        "wrong": ["Jack Gilford", "Al Lewis", "Character actor Harold Gould"],
        "d": 1
    },
    {
        "q": "What prestigious New York City employer does Uncle Leo constantly brag that his son Jeffrey works for?",
        "correct": "The New York City Parks and Recreation Department",
        "wrong": ["The Metropolitan Transportation Authority transit system", "The New York City Department of Environmental Protection", "The Manhattan Borough President's administrative council"],
        "d": 1
    },
    {
        "q": "What animal print obsession did Uncle Leo's son Jeffrey praise in Central Park?",
        "correct": "The leopard's natural spots at the Central Park Zoo",
        "wrong": ["The Bengal tiger's stripes at the Bronx Zoo enclosure", "The plumage of the snowy owls in the conservatory garden", "The agility of the river otters in the outdoor pool"],
        "d": 2
    },
    {
        "q": "What dark legal secret does Uncle Leo confess to Jerry that occurred in his distant past?",
        "correct": "He was convicted of a 'crime of passion' in his youth",
        "wrong": ["He served eighteen months for running an illegal bookmaking parlor", "He was arrested for smuggling counterfeit Cuban cigars through customs", "He was involved in a high-stakes jewelry heist in Atlantic City"],
        "d": 2
    },
    {
        "q": "Why does Uncle Leo look permanently enraged after a kitchen mishap with his gas oven?",
        "correct": "His eyebrows were burned off and Elaine drew new ones with marker",
        "wrong": ["His facial muscles locked from a severe allergic reaction to shellfish", "A botched cosmetic chemical peel left his forehead skin tightly stretched", "He was wearing ill-fitting prescription bifocals that pinched his nose"],
        "d": 1
    },
    {
        "q": "What is Newman's official civil service occupation in the city of New York?",
        "correct": "A United States Postal Service mail carrier",
        "wrong": ["A municipal sanitation department route inspector", "A parking enforcement traffic agent with the NYPD", "A commercial health inspector with the sanitation board"],
        "d": 1
    },
    {
        "q": "Which actor played Jerry's nefarious, scheming arch-nemesis Newman?",
        "correct": "Wayne Knight",
        "wrong": ["George Wendt", "Character actor Jon Polito", "John Goodman"],
        "d": 1
    },
    {
        "q": "What dream assignment does Newman desperately seek to transfer to within the Postal Service?",
        "correct": "Transferring to a mail route in Hawaii (where it rains constantly)",
        "wrong": ["A desk job in the postal inspection division in Washington", "A quiet rural mail delivery route through the scenic mountains of Vermont", "A supervisory role at the central air mail facility in Chicago"],
        "d": 2
    },
    {
        "q": "What famous statement does Newman utter regarding the immense power of the postal system?",
        "correct": "\"Because the mail never stops! It just keeps coming and coming and coming!\"",
        "wrong": ["\"When you control the letters, you hold the keys to the entire nation!\"", "\"The postal worker is the backbone of the American constitutional republic!\"", "\"Nobody defies the United States Postal Service and survives unscathed!\""],
        "d": 2
    },
    {
        "q": "What regional Southern dish does Newman passionately adore and cook in his apartment?",
        "correct": "Spicy authentic Louisiana jambalaya",
        "wrong": ["Low-country shrimp and stone-ground cheese grits", "Slow-cooked Texas barbecued beef brisket platter", "Deep-fried Mississippi catfish with hush puppies"],
        "d": 1
    },
    {
        "q": "What square-shaped chocolate candy bar is Newman famously obsessed with eating?",
        "correct": "A Chunky chocolate and raisin candy bar",
        "wrong": ["A Nestlé Crunch crisped rice chocolate bar", "A Hershey's Special Dark chocolate almond bar", "A Cadbury Dairy Milk fruit and nut bar"],
        "d": 2
    },
    {
        "q": "What apartment number does Newman reside in inside Jerry's apartment building?",
        "correct": "Apartment 5E",
        "wrong": ["Apartment 4B", "Apartment 3F on the third floor", "Apartment 5C"],
        "d": 3
    },
    {
        "q": "Who originally provided the uncredited off-screen voice of Newman in 'The Revenge' before Wayne Knight was cast?",
        "correct": "Series co-creator Larry David",
        "wrong": ["Executive producer Jerry Seinfeld", "Actor and comedian Larry Hankin", "Director and producer Tom Cherones"],
        "d": 3
    },
    {
        "q": "What pest infestation plagues Newman and Kramer's apartments, forcing them to flea-bomb their units?",
        "correct": "A severe flea infestation carried by a dog",
        "wrong": ["A colony of aggressive bedbugs in their mattress seams", "A swarm of German cockroaches behind their refrigerators", "A nesting family of urban rodents inside the wall cavities"],
        "d": 2
    },
    {
        "q": "What famous greeting do Jerry and Newman exchange with mutual dripping venom whenever they meet?",
        "correct": "\"Hello, Newman.\" / \"Hello, Jerry.\"",
        "wrong": ["\"What do you want, Newman?\" / \"Nothing from you, Seinfeld.\"", "\"We meet again, Newman.\" / \"Unfortunately, Seinfeld.\"", "\"Step aside, Newman.\" / \"Make me move, Jerry.\""],
        "d": 1
    },
    {
        "q": "What does Newman do during severe rainstorms when assigned to deliver his postal route?",
        "correct": "He refuses to deliver mail in the rain because he doesn't work in bad weather",
        "wrong": ["He dumps all commercial junk circulars into a neighborhood dumpster behind a grocery store", "He hires local neighborhood teenagers to carry his satchel for five dollars", "He leaves all packages sitting in the post office sorting lobby"],
        "d": 2
    },
    {
        "q": "What is Newman's first name, which is famously never revealed throughout the entire nine-season run?",
        "correct": "It is never revealed (he is only ever called Newman)",
        "wrong": ["Norman Clarence Newman (revealed on an official postal certificate)", "Norman Newman", "Clarence Newman"],
        "d": 2
    },
    {
        "q": "In 'The Calzone', how does Newman become essential to George's scheme to feed George Steinbrenner?",
        "correct": "Newman delivers the calzones inside his official postal route bag",
        "wrong": ["Newman distracts the security guards at the Yankee Stadium VIP gate", "Newman uses his postal vehicle to speed through red lights across town", "Newman bakes replica calzones in his apartment oven using Italian cheese"],
        "d": 2
    },
    {
        "q": "In 'The Andrea Doria', what does Jerry discover hidden inside Newman's basement storage locker?",
        "correct": "Bags of un-delivered mail that Newman hid to avoid work",
        "wrong": ["Boxes of stolen postal money orders and certified cashiers checks", "A stash of contraband imported Cuban cigars hidden in hollow books", "Counterfeit postage meter stamping machines and ink rollers"],
        "d": 2
    },

    # --- DAVID PUDDY & JACKIE CHILES (56-75) ---
    {
        "q": "Which actor portrayed Elaine's on-again, off-again boyfriend David Puddy?",
        "correct": "Patrick Warburton",
        "wrong": ["Ted McGinley", "Diedrich Bader", "Thomas Haden Church"],
        "d": 1
    },
    {
        "q": "What is David Puddy's primary initial profession before transitioning into auto sales?",
        "correct": "A certified professional automotive mechanic",
        "wrong": ["A commercial HVAC refrigeration technician", "A union construction structural ironworker", "A certified residential electrical contractor"],
        "d": 2
    },
    {
        "q": "What is David Puddy's trademark laconic catchphrase, delivered with a deadpan stare?",
        "correct": "\"Yeah, that's right.\"",
        "wrong": ["\"No question about it.\"", "\"You know how it is.\"", "\"That's the way she goes.\""],
        "d": 1
    },
    {
        "q": "What bizarre behavior does Puddy display on long commercial airline flights that drives Elaine crazy?",
        "correct": "Sitting completely still and staring blankly at the seat back ahead",
        "wrong": ["Chewing ice cubes loudly without stopping for hours", "Constantly adjusting the overhead air nozzle every two minutes", "Reading the emergency laminated safety instruction placard twenty consecutive times"],
        "d": 2
    },
    {
        "q": "What food philosophy does David Puddy vigorously defend when taking Elaine to dinner?",
        "correct": "Chip dip can serve as a complete, legitimate dinner meal",
        "wrong": ["Hamburgers must never be eaten with standard hamburger buns", "Pizza is mathematically superior when consumed cold for breakfast", "Steak should only be seasoned with coarse industrial sea salt"],
        "d": 2
    },
    {
        "q": "What does Puddy paint on his chest alongside other hockey fans at the playoff game?",
        "correct": "Letters spelling out 'D-E-V-I-L-S'",
        "wrong": ["A giant red devil pitchfork across his torso", "The state outline of New Jersey in bright red ink", "The championship Stanley Cup trophy outline in silver"],
        "d": 2
    },
    {
        "q": "Which real-life celebrity defense attorney is Jackie Chiles an overt parody of?",
        "correct": "Johnnie Cochran (defense attorney for O.J. Simpson)",
        "wrong": ["F. Lee Bailey", "Robert Shapiro", "High-profile criminal appellate defense attorney Alan Dershowitz"],
        "d": 1
    },
    {
        "q": "Which actor played the flamboyant, rhythmically speaking attorney Jackie Chiles?",
        "correct": "Phil Morris",
        "wrong": ["Carl Weathers", "Bernie Casey", "Kadeem Hardison"],
        "d": 1
    },
    {
        "q": "What series of rhyming adjectives does Jackie Chiles famously use to describe outrageous situations?",
        "correct": "\"It's outrageous, egregious, preposterous!\"",
        "wrong": ["\"It's scandalous, treacherous, blasphemous!\"", "\"It's ridiculous, calamitous, hazardous!\"", "\"It's monstrous, nefarious, venomous!\""],
        "d": 1
    },
    {
        "q": "What commercial establishment does Kramer hire Jackie Chiles to sue after suffering coffee burns?",
        "correct": "Java World coffee shop",
        "wrong": ["Starbucks Coffee Company", "Manhattan Roast Cafe", "Central Bean Emporium"],
        "d": 2
    },
    {
        "q": "Why does Kramer settle the high-stakes Java World coffee lawsuit without Jackie's consent?",
        "correct": "He accepted a lifetime supply of free cafe coffee and a cafe mocha",
        "wrong": ["He was intimidated by corporate defense lawyers in the courtroom", "He forgot to show up for the final deposition hearing on Monday", "He accepted a cash settlement of fifty dollars and a branded ceramic travel mug"],
        "d": 2
    },
    {
        "q": "In 'The Abstinence', what major industry does Jackie Chiles sue over Kramer's tobacco-weathered face?",
        "correct": "The major American tobacco cigarette corporations",
        "wrong": ["A luxury tanning salon chain in midtown Manhattan", "A commercial cosmetics chemical peel manufacturer", "An outdoor billboard advertising agency with bright lamps"],
        "d": 2
    },
    {
        "q": "What does Jackie Chiles proclaim when looking at Kramer's tobacco-ravaged face in 'The Abstinence'?",
        "correct": "\"Your face is a magnificent tapestry of rugged urban experience!\"",
        "wrong": ["\"Your visage has suffered irreparable epidermal trauma!\"", "\"You have been transformed into a walking biological disaster!\"", "\"No jury in New York could look upon that skin and deny compensation!\""],
        "d": 3
    },
    {
        "q": "What phrase does Jackie Chiles repeat when representing the group during the finale trial in Latham?",
        "correct": "\"It's lewd, lascivious, salacious, outrageous!\"",
        "wrong": ["\"It's unethical, untenable, intolerable, unbelievable!\"", "\"It's shocking, deplorable, disgraceful, indefensible!\"", "\"It's malicious, capricious, fictitious, pretentious!\""],
        "d": 3
    },
    {
        "q": "What happens to Jackie Chiles at the conclusion of the series finale in Massachusetts?",
        "correct": "He loses the case and the four main characters are sentenced to prison",
        "wrong": ["He gets disbarred for contempt of court by the presiding judge", "He wins an enormous multi-million dollar settlement verdict against the municipal district", "He quits the legal profession to pursue stand-up comedy with Jerry"],
        "d": 2
    },
    {
        "q": "What religious conflict occurs between Elaine and David Puddy in 'The Burning'?",
        "correct": "Puddy is a devout Christian who believes Elaine is going to hell",
        "wrong": ["Puddy refuses to eat meat on Fridays during the season of Lent", "Elaine refuses to attend his church choir's weekend performances", "Puddy demands they consult a spiritual elder before moving forward"],
        "d": 2
    },
    {
        "q": "What car salesman tactic does Puddy use on George when George tries to buy a new car?",
        "correct": "Insisting on high-markup add-ons like rust-proofing and keys",
        "wrong": ["Falsifying official credit application scores to artificially raise loan interest rates", "Pretending another buyer is on the phone ready to wire cash", "Swapping the vehicle's alloy rims for standard hubcaps"],
        "d": 2
    },
    {
        "q": "What nickname does Elaine give to David Puddy's heavy sheepskin coat?",
        "correct": "The \"caveman coat\"",
        "wrong": ["The \"wooly mammoth robe\"", "The \"grizzly bear parka\"", "The \"Neanderthal wrapper\""],
        "d": 2
    },
    {
        "q": "Why does Jackie Chiles warn Kramer never to put a balm on his coffee burn?",
        "correct": "\"Who told you to put the balm on?! Did the doctor tell you to put the balm on?!\"",
        "wrong": ["\"A balm compromises the physical integrity of legal courtroom evidence!\"", "\"Commercial balms contain synthetic chemicals that invalidate liability!\"", "\"Never soothe an injury that is worth half a million dollars in court!\""],
        "d": 3
    },
    {
        "q": "Who is Jackie Chiles' legal assistant who helps him research cases in his office?",
        "correct": "Suzie",
        "wrong": ["Rachel", "Brenda", "Carmen"],
        "d": 3
    },

    # --- KENNY BANIA, MICKEY ABBOTT, J. PETERMAN & RECURRING ICONS (76-100) ---
    {
        "q": "Which actor played Jerry's hack comic peer, Kenny Bania?",
        "correct": "Steve Hytner",
        "wrong": ["Kevin Pollak", "Richard Kind", "Mark Linn-Baker"],
        "d": 2
    },
    {
        "q": "What routine about a powdered beverage does Kenny Bania consider pure comedic genius?",
        "correct": "His bit about Ovaltine (\"Why do they call it Ovaltine?\")",
        "wrong": ["His joke about Carnation Instant Breakfast packets", "His routine about Tang breakfast drink flown to space", "His observation about Swiss Miss instant cocoa marshmallows"],
        "d": 1
    },
    {
        "q": "What favorite phrase does Kenny Bania declare whenever he loves an idea or joke?",
        "correct": "\"That's gold, Jerry! Gold!\"",
        "wrong": ["\"That's money in the bank!\"", "\"You knocked it out of the park!\"", "\"That's top-tier comedy genius!\""],
        "d": 1
    },
    {
        "q": "What seafood dish does Kenny Bania insist Jerry must try at Mendy's restaurant?",
        "correct": "The swordfish (\"The swordfish is the best, Jerry! The best!\")",
        "wrong": ["The Chilean sea bass with lemon herb butter", "The jumbo pan-seared sea scallops on wild rice", "The fresh broiled jumbo Maine lobster tail platter served with clarified herb butter"],
        "d": 2
    },
    {
        "q": "Which actor portrayed Kramer's fiery little person friend, Mickey Abbott?",
        "correct": "Danny Woodburn",
        "wrong": ["Award-winning actor Peter Dinklage", "Warwick Davis", "Verne Troyer"],
        "d": 2
    },
    {
        "q": "What medical symptom does Mickey Abbott get hired to portray for medical students in 'The Burning'?",
        "correct": "Cirrhosis of the liver",
        "wrong": ["Acute appendicitis with fever", "Bacterial meningitis with neck stiffness", "Double pneumonia with bronchial cough"],
        "d": 2
    },
    {
        "q": "What holiday job do Kramer and Mickey take at a department store in 'The Race'?",
        "correct": "Santa Claus and his helper elf",
        "wrong": ["Toy soldiers greeting children at the main revolving doors", "Holiday gift wrappers in the executive department", "Window mannequins displaying winter ski clothing"],
        "d": 2
    },
    {
        "q": "Why does Mickey get into a physical brawl with Kramer during the department store gig?",
        "correct": "Kramer spreads communist propaganda to children waiting in line",
        "wrong": ["Kramer stole tips from the charity donation kettle", "Kramer forgot the names of all eight Santa reindeer on live department store camera", "Kramer refused to let Mickey take a scheduled lunch break"],
        "d": 2
    },
    {
        "q": "Which actor played the eccentric, globe-trotting catalog mogul J. Peterman?",
        "correct": "John O'Hurley",
        "wrong": ["Christopher Walken", "Ted Danson", "Corbin Bernsen"],
        "d": 2
    },
    {
        "q": "What Asian country does J. Peterman flee to when suffering from severe executive burnout?",
        "correct": "Burma (Myanmar)",
        "wrong": ["Thailand (Siam)", "Cambodia (Kampuchea)", "Laos"],
        "d": 2
    },
    {
        "q": "What disastrous fashion product does Elaine greenlight while running J. Peterman in his absence?",
        "correct": "\"The Urban Sombrero\"",
        "wrong": ["\"The Outback Poncho\"", "\"The Safari Ascot\"", "\"The Metro Fez\""],
        "d": 1
    },
    {
        "q": "How much does J. Peterman pay at an auction for a vintage slice of Duke of Windsor's wedding cake?",
        "correct": "$29,000",
        "wrong": ["$15,000", "$50,000", "$10,000"],
        "d": 3
    },
    {
        "q": "What does Elaine do to J. Peterman's $29,000 antique royal wedding cake slice?",
        "correct": "She eats it during a mid-afternoon sugar craving",
        "wrong": ["She drops it down the office garbage disposal", "She leaves it out in the sun where mold covers the icing", "She accidentally tosses it into the executive recycling bin"],
        "d": 2
    },
    {
        "q": "What narcotic addiction does J. Peterman succumb to while residing in the jungles of Burma?",
        "correct": "Opium addiction (\"The white lotus... the dark cloud\")",
        "wrong": ["Pure liquid morphine extracts", "Addiction to South American herbal coca leaf tea paste mixed with natural tree bark extracts", "Hallucinogenic wild jungle mushrooms"],
        "d": 3
    },
    {
        "q": "Which actor portrayed Elaine's eccentric, hyper-demanding employer Mr. Pitt?",
        "correct": "Ian Abercrombie",
        "wrong": ["Edward Winter", "Richard Venture", "British character actor Bernard Fox"],
        "d": 3
    },
    {
        "q": "What brand of bottled mineral water does Mr. Pitt obsessively demand Elaine locate for him?",
        "correct": "Poland Spring water",
        "wrong": ["Evian natural spring water", "Perrier sparkling mineral water", "San Pellegrino imported spring water"],
        "d": 2
    },
    {
        "q": "What optical illusion image does Mr. Pitt become hopelessly transfixed by, neglecting his work?",
        "correct": "A 3D Magic Eye stereogram poster (trying to see a spaceship)",
        "wrong": ["An Escher impossible architectural staircase perspective lithograph print", "A holographic laser portrait of the Manhattan skyline", "A kaleidoscope optical refraction glass sculpture"],
        "d": 3
    },
    {
        "q": "What historical candy company is Sue Ellen Mischke the sole wealthy heiress to?",
        "correct": "The O'Henry! candy bar fortune",
        "wrong": ["The Baby Ruth candy bar estate", "The Clark Bar confectionery empire", "The Charleston Chew confectionery trust"],
        "d": 3
    },
    {
        "q": "What legendary comic actor played hyper-competitive 80-year-old fitness guru Izzy Mandelbaum?",
        "correct": "Lloyd Bridges",
        "wrong": ["Jack Albertson", "Red Buttons", "Buddy Ebsen"],
        "d": 3
    },
    {
        "q": "What battle cry does Izzy Mandelbaum shout before challenging anyone to physical tests of strength?",
        "correct": "\"It's go time!\"",
        "wrong": ["\"Show me what you got!\"", "\"Mandelbaum rules!\"", "\"Step up to the plate!\""],
        "d": 3
    },
    {
        "q": "What happens to Izzy Mandelbaum, his son, and his grandson when they try to out-lift Jerry?",
        "correct": "All three generations severely throw out their backs lifting heavy objects",
        "wrong": ["They all pull their hamstring muscles sprinting around the track", "They drop a heavy iron barbell through the gymnasium floorboards", "They collapse from severe heat exhaustion and dehydration inside the outdoor luxury sauna"],
        "d": 3
    },
    {
        "q": "What unseen, mythical friend of Kramer's allegedly lives in New Jersey and contracted rabies?",
        "correct": "Bob Sacamano",
        "wrong": ["Lobert", "Corky Ramirez", "Jay Reimenschneider"],
        "d": 3
    },
    {
        "q": "According to Kramer, what medical complication occurred during Bob Sacamano's routine hernia operation?",
        "correct": "The surgeon severed a nerve and he now speaks in a high-pitched squeak",
        "wrong": ["His appendix was mistakenly removed and his stitches ripped", "He developed a permanent dermatological allergy to synthetic cotton hospital bed linens", "He woke up during anesthesia and walked out into the corridor"],
        "d": 3
    },
    {
        "q": "What merchandise did Bob Sacamano sell on the street in Battery Park for forty dollars apiece?",
        "correct": "Faux Russian sable hats made from nutria fur",
        "wrong": ["Counterfeit Rolex chronometer watches with brass plating", "Imported cashmere pashmina scarves made of synthetic nylon", "Reconditioned police radar detectors with missing cords"],
        "d": 3
    },
    {
        "q": "What bizarre dietary habit does Kramer attribute to his unseen friend Jay Reimenschneider?",
        "correct": "He eats horse meat regularly from a specialized butcher",
        "wrong": ["He consumes exclusively raw organ meats and unpasteurized milk", "He eats four pounds of raw onions every single morning", "He survives on discarded bakery dough and commercial yeast"],
        "d": 3
    }
]

if __name__ == "__main__":
    out = assemble_batch(raw_questions, 5)
    save_json(out, "tools/staging/seinfeld_batch5.json")
