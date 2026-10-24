import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from utils import assemble_batch, save_json

raw_questions = [
    # --- KRAMER'S INVENTIONS & VENTURES (1-20) ---
    {
        "q": "What special physical feature does Kramer's coffee table book about coffee tables have?",
        "correct": "It has four fold-out wooden legs, turning into a coffee table itself",
        "wrong": ["It includes a built-in electric cup-warmer heating pad", "It features an expandable pop-up wooden chessboard surface", "It contains an insulated hidden storage compartment for coasters and cups"],
        "d": 1
    },
    {
        "q": "What scent does Kramer invent for a men's cologne that Calvin Klein allegedly steals as 'Ocean'?",
        "correct": "The fresh scent of the ocean beach",
        "wrong": ["The crisp aroma of autumn pine needles", "The musky fragrance of aged leather book bindings", "The sweet scent of freshly mowed lawn grass"],
        "d": 1
    },
    {
        "q": "What automotive periscope invention does Kramer propose to see past traffic jams?",
        "correct": "A roof-mounted periscope providing panoramic views over vehicles",
        "wrong": ["A front-bumper optical laser sensor detecting slow cars", "An elevated drone camera linked to dashboard screens", "A hydraulic pneumatic cabin lift hoisting cars two feet above surrounding vehicles"],
        "d": 2
    },
    {
        "q": "What restaurant concept does Kramer pitch where customers prepare their own food?",
        "correct": "A make-your-own pizza parlor with customized ingredients",
        "wrong": ["A roll-your-own sushi bar with imported Japanese seaweed", "A grill-your-own burger steakhouse with charcoal pits", "A toss-your-own pasta station with simmering gourmet sauces and garlic bread"],
        "d": 1
    },
    {
        "q": "What nationality are the 'Cuban' cigar rollers Kramer hires, who turn out to be posers?",
        "correct": "Dominican Republic citizens",
        "wrong": ["Puerto Rican tobacco workers", "Costa Rican agricultural laborers", "Colombian coffee bean farmers"],
        "d": 3
    },
    {
        "q": "What pasta statue does Kramer sculpt for Bette Midler in 'The Understudy'?",
        "correct": "\"Macaroni Midler\"",
        "wrong": ["\"Linguine Liza\"", "\"Rigatoni Rosemary\"", "\"Spaghetti Streisand\""],
        "d": 3
    },
    {
        "q": "What heavy office furniture piece does Kramer place in the hallway of his apartment building?",
        "correct": "A massive antique wooden executive desk",
        "wrong": ["A four-drawer fireproof metal filing cabinet", "A mahogany conference table with eight leather chairs", "A vintage leather high-back swivel reading armchair"],
        "d": 2
    },
    {
        "q": "What accessory does Kramer invent that dispenses neckties from a roll like paper towels?",
        "correct": "A roll-out necktie dispenser cartridge",
        "wrong": ["A clip-on magnetic silk bowtie fastener", "A motorized revolving necktie carousel rack", "A pre-knotted necktie collar extension strap"],
        "d": 3
    },
    {
        "q": "What beverage does Kramer claim he invented during a hot summer day in his apartment?",
        "correct": "Coffee tea (steeping roasted coffee beans like tea)",
        "wrong": ["Carbonated iced espresso with citrus peel", "Cucumber-infused cold brew concentrate", "Electrolyte-charged chilled herbal mocha espresso blend"],
        "d": 3
    },
    {
        "q": "What pet ownership innovation does Kramer suggest to prevent city streets from getting messy?",
        "correct": "A diaper attachment harness designed for carriage horses",
        "wrong": ["A motorized suction street sweeper for dog walkers", "Biodegradable scented footwear booties for pets", "A mechanical waste-collection belt for urban domestic dogs"],
        "d": 2
    },
    {
        "q": "What does Kramer install in his apartment living room that shorts out the building's power grid?",
        "correct": "A heavy two-person outdoor wooden hot tub",
        "wrong": ["A commercial tanning bed with high-intensity ultraviolet bulbs", "An authentic Scandinavian cedar dry sauna chamber", "A restaurant-grade walk-in meat refrigeration freezer"],
        "d": 2
    },
    {
        "q": "What business name does Kramer give to his umbrella corporate enterprise?",
        "correct": "Kramerica Industries",
        "wrong": ["Cosmo Enterprises", "Vandelay Global", "Pennypacker Consolidated"],
        "d": 1
    },
    {
        "q": "What nickname does Kramer give to his signature exuberant physical entrance through Jerry's door?",
        "correct": "The sliding entrance",
        "wrong": ["The hip-hop tumble", "The tornado burst", "The lightning slide across the room"],
        "d": 2
    },
    {
        "q": "What does Kramer confess is his actual first name in Season 6's 'The Switch'?",
        "correct": "Cosmo",
        "wrong": ["Casimir", "Conrad", "Constantine"],
        "d": 1
    },
    {
        "q": "Who reveals Kramer's long-secret first name 'Cosmo' to Jerry and George on the street?",
        "correct": "Kramer's estranged mother, Babs Kramer",
        "wrong": ["His childhood friend Bob Sacamano", "Newman during a heated hallway argument", "A postal inspector reading official government records"],
        "d": 1
    },
    {
        "q": "What was Babs Kramer's occupation when she reappeared in Season 6?",
        "correct": "A luxury restaurant restroom attendant",
        "wrong": ["A hotel housekeeping maid at the Plaza", "A night-shift dispatcher for yellow taxicabs", "A commercial seamstress in the garment district"],
        "d": 3
    },
    {
        "q": "What high-stakes horse race gamble does Kramer celebrate winning by jumping up and down?",
        "correct": "His mudder horse 'Papanick' winning on a rainy track",
        "wrong": ["\"Blue Streak\" winning the third race at Belmont", "\"Captain Nemo\" coming from behind at Saratoga", "\"Prickly Pete\" setting a new track speed record"],
        "d": 2
    },
    {
        "q": "What does Kramer claim is a mudder horse's greatest genetic advantage?",
        "correct": "\"His mother was a mudder, his father was a mudder!\"",
        "wrong": ["\"His hooves were engineered for wet marshland clay!\"", "\"He runs with double the stamina when the track turns to soup!\"", "\"Rain brings out the pure wild predatory instinct in him!\""],
        "d": 2
    },
    {
        "q": "What does Kramer do when a bank promises a hundred dollars if a teller doesn't say 'hello'?",
        "correct": "He demands the reward when the teller only says 'Hey'",
        "wrong": ["He stages a silent twenty-minute sit-in at the teller window", "He calls the corporate customer service line from the lobby", "He hires Jackie Chiles to file a false advertising lawsuit"],
        "d": 2
    },
    {
        "q": "What character does Kramer portray in medical simulations with Mickey Abbott in 'The Burning'?",
        "correct": "A patient suffering from acute gonorrheal symptoms",
        "wrong": ["A senior executive recovering from heat stroke", "A construction worker with a fractured femur", "A sailor suffering from severe tropical dengue bonebreak fever"],
        "d": 3
    },

    # --- GEORGE'S ALIASES, JOBS & NEUROSES (21-45) ---
    {
        "q": "What products does George claim Art Vandelay manufactures, imports, and exports?",
        "correct": "Latex, potato chips, and diapers",
        "wrong": ["Corrugated cardboard boxes and industrial glue", "Fine imported crystal and porcelain dinnerware", "Synthetic plastics and hydraulic engine valves"],
        "d": 1
    },
    {
        "q": "What porn star alias does George dream of adopting if he entered the adult film industry?",
        "correct": "Buck Naked",
        "wrong": ["Dirk Diggler", "Lance Sterling", "Rex Steel"],
        "d": 1
    },
    {
        "q": "What revolutionary material does George convince the New York Yankees to use for their uniforms?",
        "correct": "One hundred percent pure breathable cotton",
        "wrong": ["Ultra-lightweight micro-mesh synthetic polyester", "Imported Egyptian combed silk-cotton blend", "High-performance moisture-wicking nylon weave"],
        "d": 1
    },
    {
        "q": "What disaster occurs when the Yankees play in their new all-cotton uniforms in the heat?",
        "correct": "The uniforms shrink dramatically and rip along the seams",
        "wrong": ["The dark dye bleeds onto the players' skin in the rain", "The fabric absorbs heavy sweat and weighs fifteen pounds", "The players develop severe friction heat blisters in games"],
        "d": 1
    },
    {
        "q": "What legendary Yankees artifact does George accidentally ruin while driving Steinbrenner's car?",
        "correct": "Dragging the World Series championship trophy behind the car",
        "wrong": ["Crashing into the iconic monuments in center field", "Running over the home plate dirt with a motorized cart", "Denting Babe Ruth's original game-worn wooden locker door frame"],
        "d": 3
    },
    {
        "q": "What handicap does George pretend to suffer from while working at the Play Now sports company?",
        "correct": "A permanent walking disability requiring a mobility cane",
        "wrong": ["Severe chronic lower spine degenerative disk disease causing pain", "Acute vertigo that prevents him from climbing stairs", "A neurological tremor that limits his physical balance"],
        "d": 1
    },
    {
        "q": "What exclusive executive luxury does George receive at Play Now due to his fake disability?",
        "correct": "A private, fully accessible executive bathroom suite",
        "wrong": ["A private corporate limousine with dedicated driver", "A chauffeured golf cart navigating the office corridors", "A first-floor corner office with a private terrace"],
        "d": 1
    },
    {
        "q": "How is George's fake disability scheme at Play Now finally exposed to the entire staff?",
        "correct": "Coworkers catch him carrying his electric cart up a flight of stairs",
        "wrong": ["He is spotted sprinting across the street to catch an express commuter bus", "Security cameras capture him dancing at a colleague's wedding", "He kicks a vending machine vigorously after losing his dollar"],
        "d": 2
    },
    {
        "q": "What photograph does George go to absurd lengths to steal from Mr. Kruger's office in 'The Slicer'?",
        "correct": "A beach photograph showing George photobombing Kruger's family",
        "wrong": ["A snapshot showing George fast asleep during an executive review", "A picture of George eating pastries out of an office garbage can", "A photograph of George posing in his boudoir underwear shoot"],
        "d": 2
    },
    {
        "q": "What cartoon character does George look like when Kruger has his family photo airbrushed?",
        "correct": "A generic drawing resembling a round bald cartoon character",
        "wrong": ["A caricature resembling Charlie Brown with glasses", "A hand-drawn figure of Elmer Fudd in bright yellow swimming trunks", "A cartoon portrait resembling Mr. Magoo with no hair"],
        "d": 3
    },
    {
        "q": "What architectural project does George claim he designed when boasting to Diane in 'The Marine Biologist'?",
        "correct": "The new addition to the Guggenheim Museum in Manhattan",
        "wrong": ["The expansion wing of the Metropolitan Museum of Art", "The glass pyramid entrance of the New York Public Library", "The executive observation deck of the Chrysler Building"],
        "d": 2
    },
    {
        "q": "What toilet observation does George passionately share that he claims qualifies him as a restroom expert?",
        "correct": "He knows the location of the best public restroom in every NYC neighborhood",
        "wrong": ["He can calculate the acoustic privacy rating of any public commercial stall", "He knows the water pressure specifications of commercial pipes", "He can predict the optimal door gap width to prevent eye contact"],
        "d": 2
    },
    {
        "q": "What candy does George leave on his boss's desk as a subtle hint to secure a promotion?",
        "correct": "A box of gourmet chocolate-covered raisins",
        "wrong": ["A jar of expensive imported Swiss hazelnut truffles", "A tin of dark chocolate espresso beans from Italy", "A selection of artisanal almond bark from Bloomingdale's"],
        "d": 3
    },
    {
        "q": "What board game does George play with 'The Bubble Boy' that ends in a violent physical brawl?",
        "correct": "Trivial Pursuit",
        "wrong": ["Scrabble", "Parker Brothers Monopoly Board Game", "Risk"],
        "d": 1
    },
    {
        "q": "What misprinted Trivial Pursuit card answer sparks George's fight with the Bubble Boy?",
        "correct": "\"Moops\" (instead of \"Moors\")",
        "wrong": ["\"Turks\" (instead of \"Greeks\")", "\"Huns\" (instead of \"Goths\")", "\"Celts\" (instead of \"Gauls\")"],
        "d": 1
    },
    {
        "q": "What is the name of the cantankerous Bubble Boy in Season 4's 'The Bubble Boy'?",
        "correct": "Donald Sanger",
        "wrong": ["David Miller", "Danny Cooper", "Dennis Clark from Upstate New York"],
        "d": 3
    },
    {
        "q": "What luxury leisure garment does George wear in 'The Doodle' that Jerry compares to a diaper?",
        "correct": "A full-body velvet leisure sweat suit",
        "wrong": ["A silk kimono dressing robe with dragons", "A terrycloth hooded sauna jumpsuit", "A cashmere thermal union suit with buttons"],
        "d": 2
    },
    {
        "q": "What declaration does George make about wearing velvet in 'The Doodle'?",
        "correct": "\"I would drape myself in velvet for the rest of my life if it were socially acceptable!\"",
        "wrong": ["\"Velvet is the ultimate fabric of refined masculine elegance!\"", "\"Nothing in this world feels more luxurious against the human epidermis!\"", "\"If kings wore velvet every day, why should modern men settle for cotton!\""],
        "d": 2
    },
    {
        "q": "What baseball team does George Costanza claim to have had an audition with as a young prospect?",
        "correct": "A tryout scout meeting with the Texas Rangers",
        "wrong": ["A regional workout with the Kansas City Royals", "A high school showcase with the Pittsburgh Pirates", "A pitching exhibition for the Cincinnati Reds"],
        "d": 3
    },
    {
        "q": "What food obsession does George incorporate into his intimate encounters in 'The Blood'?",
        "correct": "Eating pastrami sandwiches while engaged in romantic intimacy",
        "wrong": ["Drinking chocolate milkshakes during bedroom encounters", "Savoring hot slices of pepperoni pizza between kisses", "Snacking on cold cocktail shrimp with extra spicy cocktail sauce"],
        "d": 2
    },
    {
        "q": "What does George call the combination of food, sex, and television in 'The Blood'?",
        "correct": "\"The trifecta\"",
        "wrong": ["\"The holy trinity\"", "\"The ultimate summit\"", "\"The grand slam\""],
        "d": 2
    },
    {
        "q": "What high school gym teacher gave George the humiliating wedgie nicknamed the 'atomic wedgie'?",
        "correct": "Mr. Heyman (who couldn't pronounce George's name)",
        "wrong": ["Coach Ross", "Mr. Fitzpatrick", "Coach Miller from the athletic department"],
        "d": 3
    },
    {
        "q": "What nickname did Mr. Heyman give George during high school physical education class?",
        "correct": "\"Can'tstandya!\"",
        "wrong": ["\"Costanza-the-loser!\"", "\"Short-stuff!\"", "\"Baldy-boy!\""],
        "d": 2
    },
    {
        "q": "Where does George find his long-lost high school nemesis Mr. Heyman in Season 3?",
        "correct": "Living as a homeless man on a Manhattan street corner",
        "wrong": ["Working as a security guard at an off-track betting parlor", "Managing a dilapidated bowling alley in the Bronx", "Sweeping the floors at a Queens public high school"],
        "d": 2
    },
    {
        "q": "What does George discover Mr. Heyman is still chewing decades after high school?",
        "correct": "The exact same brand of pungent tobacco",
        "wrong": ["Slices of raw ginger root", "Sticks of natural cinnamon bark chewing gum", "Clove and anise seeds"],
        "d": 3
    },

    # --- ELAINE, JERRY & SETTING DETAILS (46-75) ---
    {
        "q": "What physical aggressive gesture does Elaine perform whenever she hears shocking good news?",
        "correct": "Shoving the person forcefully while screaming \"GET OUT!\"",
        "wrong": ["Slapping both hands against the table while screaming \"NO WAY!\"", "Grabbing the person's lapels and shaking them vigorously", "Spinning around in a complete circle with hands in the air"],
        "d": 1
    },
    {
        "q": "What publishing house does Elaine work for as an assistant editor in the early seasons?",
        "correct": "Pendant Publishing",
        "wrong": ["Vanguard Books", "Simon & Schuster", "Doubleday Publishing"],
        "d": 1
    },
    {
        "q": "Who is Elaine's high-strung, perpetually stressed boss at Pendant Publishing?",
        "correct": "Mr. Lippman",
        "wrong": ["Mr. Pitt", "Mr. Peterman", "Mr. Kruger"],
        "d": 1
    },
    {
        "q": "What country did Elaine grow up in before moving to New York City for college?",
        "correct": "The United States (born and raised in suburban Maryland)",
        "wrong": ["England (raised in a countryside boarding school in Surrey)", "Canada (raised in a French-speaking family in Montreal)", "France (spent childhood between Paris and Normandy)"],
        "d": 2
    },
    {
        "q": "What famous private liberal arts college did Elaine attend in Massachusetts?",
        "correct": "Tufts University",
        "wrong": ["Amherst College", "Williams College", "Boston University"],
        "d": 3
    },
    {
        "q": "What odd habit does Elaine discover her therapist Dr. Reston has during their sessions?",
        "correct": "He uses psychological manipulation to control her dating life",
        "wrong": ["He falls asleep for twenty minutes while taking sparse notes", "He charges her triple rates for appointments held on weekends", "He constantly compares her neuroses to classic literary heroines"],
        "d": 3
    },
    {
        "q": "What video store clerk's curated movie recommendations does Elaine become obsessed with?",
        "correct": "Vincent's staff picks at the local video rental shop",
        "wrong": ["Arthur's film recommendations at Blockbuster Video", "Marcus's foreign cinema picks at Manhattan Video", "Gene's art-house foreign cinema classics at Cinema World boutique"],
        "d": 3
    },
    {
        "q": "What is the street address of Jerry Seinfeld's Upper West Side apartment building?",
        "correct": "129 West 81st Street",
        "wrong": ["340 West 72nd Street Apartment Complex", "215 West 86th Street", "104 West 79th Street"],
        "d": 1
    },
    {
        "q": "What is Jerry's apartment unit number throughout the entire television series?",
        "correct": "Apartment 5A",
        "wrong": ["Apartment 4B on the fourth floor", "Apartment 3C", "Apartment 5B"],
        "d": 1
    },
    {
        "q": "What comic book superhero figurine is visibly displayed on the living room shelf in Jerry's apartment?",
        "correct": "Superman",
        "wrong": ["Batman", "Spider-Man", "The Flash"],
        "d": 1
    },
    {
        "q": "What brand and color of bicycle hangs vertically on the wall near Jerry's bathroom door?",
        "correct": "A green Klein mountain bicycle",
        "wrong": ["A red Trek road racing bicycle", "A blue Cannondale commuter bicycle", "A silver Specialized hybrid bicycle"],
        "d": 2
    },
    {
        "q": "What food item dominates the kitchen shelves inside Jerry's apartment cabinets?",
        "correct": "Dozens of boxes of various commercial breakfast cereals",
        "wrong": ["Jars of gourmet peanut butter and artisanal jams", "Cans of imported Italian tomato sauces and pastas", "Bottles of single-origin olive oils and balsamic vinegars"],
        "d": 1
    },
    {
        "q": "What high-performance sports car brand is Jerry Seinfeld personally obsessed with in real life and on the show?",
        "correct": "Porsche sports cars",
        "wrong": ["Ferrari sports cars", "Corvette sports cars", "Aston Martin sports cars"],
        "d": 2
    },
    {
        "q": "What is the name of the neighborhood coffee shop where Jerry, George, Elaine, and Kramer eat daily?",
        "correct": "Monk's Diner (Monk's Cafe)",
        "wrong": ["Tom's Restaurant Diner in Morningside Heights", "Reggie's Diner", "Mendy's Delicatessen"],
        "d": 1
    },
    {
        "q": "What diner do Jerry and George briefly patronize when alienated from Monk's, only to hate it?",
        "correct": "Reggie's Diner (which serves no Big Salad)",
        "wrong": ["Pete's Traditional Upper West Side Luncheonette", "The Broadway Luncheonette", "Max's Manhattan Grill"],
        "d": 2
    },
    {
        "q": "What does the waitress at Reggie's bluntly tell Elaine when Elaine tries to order a Big Salad?",
        "correct": "\"We don't have big bowls! If you want a salad, I can bring you two small ones.\"",
        "wrong": ["\"We serve real diner meals here, not giant bowls of raw rabbit food!\"", "\"Nobody in this neighborhood orders salad bowls that weigh three pounds!\"", "\"If you want luxury salads, you need to walk three blocks to Monk's!\""],
        "d": 2
    },
    {
        "q": "What food item does Jerry refuse to eat if it has been touched by someone's bare fingers?",
        "correct": "Practically anything—Jerry is a hyper-vigilant germaphobe",
        "wrong": ["Only poultry dishes and raw shellfish platters", "Exclusively baked pastries and unpeeled orchard fruits", "Only sushi rolls, fresh oysters, and raw sliced deli cold cuts"],
        "d": 1
    },
    {
        "q": "Why does Jerry throw away an expensive leather belt in 'The Puerto Rican Day'?",
        "correct": "The tip of the belt accidentally touched the floor of a public restroom",
        "wrong": ["He noticed a hairline crack in the stitching of the brass buckle", "A street vendor brushed against the leather with oily salted pretzel hands", "Kramer borrowed the belt to secure an overloaded postal package"],
        "d": 2
    },
    {
        "q": "What happens to Jerry's shoelaces in 'The Gymnast' that causes him to discard them immediately?",
        "correct": "The laces brushed the public restroom floor while tying his shoe",
        "wrong": ["A drop of gutter rainwater splashed across the synthetic fabric", "A stranger stepped on the trailing loop on a crowded subway platform", "They touched the exterior rim of a public metal trash can"],
        "d": 2
    },
    {
        "q": "What stand-up comic rival constantly annoys Jerry with unsolicited scripts and invitations to lunch?",
        "correct": "Pat Buckles",
        "wrong": ["Kenny Bania", "Ronnie Kaye", "Mickey Abbott"],
        "d": 3
    },
    {
        "q": "What gift does Pat Buckles ask Jerry for during a ride in Jerry's car in 'The Movie'?",
        "correct": "Jerry's trench coat from the back seat",
        "wrong": ["Jerry's spare car keys for an emergency", "A five-hundred-dollar loan for an Edinburgh festival trip", "An introduction to the talent booker for Jay Leno"],
        "d": 3
    },
    {
        "q": "What radio station call letters broadcast the classical music station Jerry listens to in his car?",
        "correct": "WQXR (New York's classical music radio station)",
        "wrong": ["WNYC (New York City Public Radio 93.9 FM broadcast)", "WFUV", "WINS"],
        "d": 3
    },
    {
        "q": "What color is the exterior entryway door of Jerry Seinfeld's apartment 5A?",
        "correct": "Standard institutional apartment brown",
        "wrong": ["Bright painted royal blue", "Dark forest green high-gloss exterior lacquer", "Industrial slate battleship gray"],
        "d": 3
    },
    {
        "q": "What appliance does Kramer borrow from Jerry so frequently that it essentially stays in Kramer's kitchen?",
        "correct": "Jerry's electric citrus juicer and blender",
        "wrong": ["Jerry's toaster oven appliance", "Jerry's microwave cooking turntable", "Jerry's electric countertop burr coffee grinder"],
        "d": 3
    },
    {
        "q": "What food does Kramer repeatedly raid from Jerry's refrigerator in almost every single episode?",
        "correct": "Fresh milk, cereal, fruit, and whatever is in the deli crisper",
        "wrong": ["Frozen microwaveable dinners and ice cream tubs", "Bottled beer and carbonated mineral waters", "Pre-packaged flavored yogurt cups and imported string cheese sticks"],
        "d": 2
    },

    # --- FAMOUS CATCHPHRASES & BEHIND-THE-SCENES LORE (76-100) ---
    {
        "q": "What party etiquette violation does George commit at a wake that causes Timmy to confront him angrily?",
        "correct": "\"Double dipping\" a chip into the communal bowl",
        "wrong": ["Taking four cocktail meatballs on a single toothpick", "Drinking directly from an open two-liter soda bottle", "Taking an entire sleeve of crackers without sharing"],
        "d": 2
    },
    {
        "q": "What line does Timmy scream when George dips a chip twice in 'The Implant'?",
        "correct": "\"That's like putting your whole mouth right in the dip!\"",
        "wrong": ["\"You just contaminated the entire bowl for everyone here!\"", "\"Nobody dips twice in this house without facing the consequences!\"", "\"Have some basic human respect for the deceased's family!\""],
        "d": 3
    },
    {
        "q": "What famous declaration does Teri Hatcher's character make about her physical attributes in 'The Implant'?",
        "correct": "\"They're real, and they're spectacular!\"",
        "wrong": ["\"They're all natural, and they're flawless!\"", "\"They're completely genuine, and they're glorious!\"", "\"They're unenhanced, and they're extraordinary!\""],
        "d": 2
    },
    {
        "q": "What communication trait does Judge Reinhold's character Aaron have in 'The Raincoats'?",
        "correct": "He is a \"close talker\" who stands inches from people's faces",
        "wrong": ["He is a \"high talker\" whose voice sounds like a child", "He is a \"low talker\" who whispers all of his thoughts", "He is a \"rapid talker\" who speaks two hundred words per minute"],
        "d": 2
    },
    {
        "q": "What communication trait does Elaine's boyfriend Dan possess in 'The Pledge Drive'?",
        "correct": "He is a \"high talker\" whose voice sounds identical to a woman's",
        "wrong": ["He is a \"loud talker\" who projects across entire dining rooms", "He is a \"mumble talker\" who swallows the endings of words", "He is a \"slow talker\" who pauses ten seconds between sentences"],
        "d": 3
    },
    {
        "q": "What four-word mantra did Larry David establish as the cardinal creative rule for all Seinfeld scripts?",
        "correct": "\"No hugging, no learning\"",
        "wrong": ["\"Keep it simple, stupid\"", "\"Always find the funny\"", "\"Characters never grow up\""],
        "d": 1
    },
    {
        "q": "What distinctive musical instrument sound effect separates scenes in every episode of Seinfeld?",
        "correct": "A slap-bass synthesizer riff composed by Jonathan Wolff",
        "wrong": ["An authentic acoustic fretless upright bass melody", "A brass trumpet fanfare recorded with a vintage mute", "A funk guitar riff played on an electric Fender Stratocaster"],
        "d": 1
    },
    {
        "q": "How did composer Jonathan Wolff customize the music for every single episode of Seinfeld?",
        "correct": "He adjusted the tempo and slap-bass rhythms to match Jerry's stand-up timing",
        "wrong": ["He re-recorded the theme song using guest vocalists from Broadway", "He modulated the key signature to reflect the subtle emotional tone of the plot", "He added ambient sound effects recorded in the New York subway system"],
        "d": 1
    },
    {
        "q": "Why did NBC studio directors have to ask live studio audiences to restrain their cheers for Michael Richards?",
        "correct": "His applause ovations were so long they threw off the comic timing of scenes",
        "wrong": ["The extreme audio decibel level blew out the sensitive boom microphones", "Jerry Seinfeld complained that Kramer was overshadowing his opening scene", "The broadcast network was forced to trim critical dialogue to fit commercial time"],
        "d": 3
    },
    {
        "q": "How was Julia Louis-Dreyfus's real-life pregnancy hidden from viewers during Season 3 and Season 8?",
        "correct": "She carried large cardboard boxes, laundry baskets, and hid behind furniture",
        "wrong": ["Digital visual effects artists removed her baby bump in post-production", "She was replaced by an uncredited body double for all wide camera angles", "Her character was sent on European travel assignments for twelve whole episodes"],
        "d": 2
    },
    {
        "q": "How many total episodes of Seinfeld were produced and broadcast across its historic nine-season run?",
        "correct": "180 episodes",
        "wrong": ["200 full episodes", "165 episodes", "220 episodes"],
        "d": 1
    },
    {
        "q": "In how many episodes across all nine seasons did the character of Cosmo Kramer NOT appear?",
        "correct": "Two episodes ('The Chinese Restaurant' and 'The Pen')",
        "wrong": ["Zero episodes (he appeared in every single episode)", "One episode ('The Chinese Restaurant' only)", "Four complete episodes throughout the entire series run"],
        "d": 2
    },
    {
        "q": "Which of the four core characters never appeared in Season 3's classic episode 'The Chinese Restaurant'?",
        "correct": "Kramer",
        "wrong": ["Elaine Benes", "George", "Jerry"],
        "d": 1
    },
    {
        "q": "Which two main characters did NOT appear in the Season 3 episode 'The Pen'?",
        "correct": "George and Kramer",
        "wrong": ["Elaine Benes and Cosmo Kramer", "Jerry and George", "George and Newman"],
        "d": 2
    },
    {
        "q": "Who provided the iconic, fast-talking off-screen voice of New York Yankees owner George Steinbrenner?",
        "correct": "Series co-creator Larry David",
        "wrong": ["Actor and voice artist Phil Hartman", "Executive producer Peter Mehlman", "Writer and director Spike Feresten"],
        "d": 1
    },
    {
        "q": "What physical feature of George Steinbrenner is the only part ever shown on camera in his office?",
        "correct": "The back of his head and his gesturing hands from behind his desk",
        "wrong": ["His polished wingtip shoes resting upon his mahogany desk", "His silhouette projected against the frosted glass of his door", "His reflection in the polished glass of his championship trophy cabinet"],
        "d": 2
    },
    {
        "q": "What was the original working title of the Seinfeld pilot episode when it was filmed in 1989?",
        "correct": "\"The Seinfeld Chronicles\"",
        "wrong": ["\"Stand-Up Life in New York\"", "\"The Jerry Seinfeld Show\"", "\"Nothing to Report\""],
        "d": 3
    },
    {
        "q": "What real-life neighbor of Larry David's was the direct inspiration for the character of Cosmo Kramer?",
        "correct": "Kenny Kramer (who later ran 'The Kramer Reality Tour' in New York)",
        "wrong": ["Cosmo DiGiacomo", "Arthur Sacamano", "Donald Newman (the eccentric building superintendent who lived across the hall)"],
        "d": 3
    },
    {
        "q": "What real-life tour did Kenny Kramer create to capitalize on the show's worldwide fame?",
        "correct": "\"The Kramer Reality Tour\" bus tour of Manhattan locations",
        "wrong": ["\"The Ultimate Seinfeld Pilgrimage\" walking tour", "\"The Real Cosmo Experience\" open-air trolley tour", "\"The Manhattan Sites of Nothing\" VIP limousine excursion"],
        "d": 2
    },
    {
        "q": "What dialogue do Jerry and George repeat in the final jail cell scene of 'The Finale'?",
        "correct": "The debate about the placement of the second button on a dress shirt from the 1989 pilot",
        "wrong": ["The argument regarding whether breakfast cereal qualifies as a midnight dessert snack item", "The debate over whether a public restroom stall door should reach the floor", "The discussion about why banks give complimentary pens that fail to write"],
        "d": 1
    },
    {
        "q": "What exact line does George say to Jerry in the final prison cell scene regarding their conversation?",
        "correct": "\"Haven't we had this conversation before?\"",
        "wrong": ["\"Does any of this sound remotely familiar to you?\"", "\"Are we doomed to repeat this dialogue forever?\"", "\"Why do we always return to the same trivial nonsense?\""],
        "d": 2
    },
    {
        "q": "What was the date of the historic broadcast of the Seinfeld series finale on NBC?",
        "correct": "May 14, 1998",
        "wrong": ["May 21, 1997", "June 4, 1999", "April 30, 1998"],
        "d": 3
    },
    {
        "q": "How many viewers tuned in to watch the May 14, 1998 series finale of Seinfeld in the United States?",
        "correct": "Approximately 76 million viewers",
        "wrong": ["Approximately 52 million viewers", "Approximately 95 million television viewers", "Approximately 63 million viewers"],
        "d": 3
    },
    {
        "q": "In what real-life diner exterior is Monk's Cafe filmed for establishing shots in Upper Manhattan?",
        "correct": "Tom's Restaurant (on Broadway and West 112th Street)",
        "wrong": ["The iconic Empire Diner on 10th Avenue in the Chelsea district", "Tick Tock Diner on 34th Street", "Veselka in the East Village"],
        "d": 2
    },
    {
        "q": "Which singer famously wrote the 1987 hit song 'Tom's Diner' inspired by the very same establishment?",
        "correct": "Suzanne Vega",
        "wrong": ["Tracy Chapman", "Rickie Lee Jones", "Shawn Colvin"],
        "d": 2
    },
    {
        "q": "In 'The Andrea Doria', what canine illness does Kramer contract that forces him to take dog medication?",
        "correct": "A chronic hacking cough from an unruly dog named Smuckers",
        "wrong": ["Canine heartworm infection from sleeping near an infected hound", "A parasitic kennel tick infection picked up at a public dog park", "Mange skin irritation contracted from handling stray puppies"],
        "d": 2
    },
    {
        "q": "In 'The Bizarro Jerry', what figurine is displayed in Kevin's apartment as the bizarro opposite of Jerry's Superman?",
        "correct": "A figurine of Bizarro (Superman's villainous imperfect clone)",
        "wrong": ["A miniature metal bust of Lex Luthor with green Kryptonite", "A miniature statue of General Zod from Planet Krypton", "A small metal figure of Batman guarding a miniature Gotham City skyline"],
        "d": 2
    },
    {
        "q": "In 'The Cartoon', what is the name of The New Yorker cartoon editor whom Elaine confronts in his office?",
        "correct": "Mr. Elinoff",
        "wrong": ["Mr. Henderson", "Mr. Wallace", "Mr. Sterling"],
        "d": 3
    },
    {
        "q": "In 'The Voice', what legal fate befalls Kramer's loyal intern Darren after the oil bladder accident?",
        "correct": "Darren is convicted and sentenced to federal prison time",
        "wrong": ["Darren is expelled from New York University with zero credits", "Darren is hired as a corporate risk analyst by ExxonMobil", "Darren sues Kramerica Industries for twenty million dollars"],
        "d": 2
    },
    {
        "q": "In 'The Rye', what fishing bait do Jerry and George use on the street to hoist the marble rye?",
        "correct": "A heavy three-pronged treble hook without bait",
        "wrong": ["A cluster of nightcrawler earthworms from a tackle box", "A piece of dried salt cod tied to forty-pound test line", "A metal spoon lure with artificial bright feathers"],
        "d": 3
    }
]

if __name__ == "__main__":
    out = assemble_batch(raw_questions, 6)
    save_json(out, "tools/staging/seinfeld_batch6.json")
