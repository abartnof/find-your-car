import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from utils import assemble_batch, save_json

raw_questions = [
    # --- SEASON 4: THE LA TRIP & NBC PILOT PITCH (1-25) ---
    {
        "q": "In 'The Trip', what serial crime is Kramer falsely arrested for while living in Los Angeles?",
        "correct": "Being the 'Smog Strangler' serial killer",
        "wrong": ["Robbing a Beverly Hills luxury jewelry boutique", "Stealing a high-end luxury sports convertible", "Operating an illegal high-stakes poker gambling ring"],
        "d": 2
    },
    {
        "q": "What child television star does Kramer sit next to on a bench and share acting advice with in 'The Trip'?",
        "correct": "Fred Savage",
        "wrong": ["Macaulay Culkin", "Neil Patrick Harris", "Kirk Cameron"],
        "d": 3
    },
    {
        "q": "What late night talk show do Jerry and George appear on while in Los Angeles in 'The Trip'?",
        "correct": "The Tonight Show with Jay Leno",
        "wrong": ["Late Night with David Letterman", "The Arsenio Hall Show", "The Joan Rivers Show"],
        "d": 2
    },
    {
        "q": "Who is the lead LAPD detective who interrogates Kramer in 'The Trip'?",
        "correct": "Lieutenant Martel",
        "wrong": ["Detective Columbo", "Lieutenant Valenti", "Sergeant Callahan"],
        "d": 3
    },
    {
        "q": "In 'The Pitch', what is George's core artistic concept for the sitcom he and Jerry pitch to NBC?",
        "correct": "A show about absolutely nothing",
        "wrong": ["A satirical documentary about New York dating life", "A behind-the-scenes look at the stand-up comedy industry", "A workplace sitcom set in an architect firm"],
        "d": 1
    },
    {
        "q": "Who is the president of NBC whom Jerry and George pitch their pilot idea to in 'The Pitch'?",
        "correct": "Russell Dalrymple",
        "wrong": ["Warren Littlefield", "Michael Branden", "Donald Tartikoff"],
        "d": 1
    },
    {
        "q": "Why does George initially reject NBC's initial contract offer for the pilot script in 'The Ticket'?",
        "correct": "He demanded equal pay to Jerry's compensation",
        "wrong": ["He insisted on directing all thirteen episodes himself", "He refused to allow network censors to alter his jokes", "He wanted a guarantee of a prime-time Thursday night slot"],
        "d": 3
    },
    {
        "q": "In 'The Ticket', what is the name of the neurotic writer who threatens to break Jerry's thumbs over a joke?",
        "correct": "Crazy Joe Davola",
        "wrong": ["Kenny Bania", "Mike Moffitt", "Bob Cobb"],
        "d": 2
    },
    {
        "q": "In 'The Virgin', what is the name of the woman Jerry dates who reveals she is still a virgin?",
        "correct": "Marla",
        "wrong": ["Melanie", "Audrey", "Gillian"],
        "d": 2
    },
    {
        "q": "In 'The Virgin', what famous contest bet is first proposed among the four friends?",
        "correct": "Who can refrain from sexual self-gratification longest",
        "wrong": ["Who can go thirty full days without telling a single lie", "Who can survive an entire month without visiting Monk's diner", "Who can avoid drinking coffee for two consecutive weeks"],
        "d": 1
    },
    {
        "q": "In 'The Contest', what phrase do the characters repeat to signify they have not succumbed to temptation?",
        "correct": "\"Master of my domain\"",
        "wrong": ["\"Ruler of my kingdom\"", "\"Captain of my fate\"", "\"Keeper of the flame\""],
        "d": 1
    },
    {
        "q": "Who is the very first person to cave and lose the wager in 'The Contest' after seeing a naked neighbor?",
        "correct": "Kramer, after only twenty minutes",
        "wrong": ["George, after visiting his mother in the hospital", "Jerry, after watching late night television", "Elaine, after taking an aerobics exercise class"],
        "d": 1
    },
    {
        "q": "What political scion does Elaine encounter at her health club that tests her willpower in 'The Contest'?",
        "correct": "John F. Kennedy Jr.",
        "wrong": ["Andrew Cuomo", "Robert F. Kennedy Jr.", "Patrick Kennedy"],
        "d": 1
    },
    {
        "q": "What magazine was George reading in his mother's house that caused her to throw her back out upon walking in?",
        "correct": "Glamour magazine",
        "wrong": ["Vogue magazine", "Cosmopolitan magazine", "Vanity Fair magazine"],
        "d": 1
    },
    {
        "q": "In 'The Airport', what sweet treat does Jerry savor while flying in first class?",
        "correct": "A warm hot fudge sundae with whipped cream",
        "wrong": ["A fresh hot chocolate lava cake slice", "A chilled bowl of fresh exotic tropical fruit", "A warm fresh gourmet chocolate chip cookie"],
        "d": 2
    },
    {
        "q": "In 'The Airport', what passenger is George convinced is a high school classmate who owes him money?",
        "correct": "Grossbard",
        "wrong": ["Lippman", "Farbman", "Tiefenbrun"],
        "d": 3
    },
    {
        "q": "In 'The Visa', what catastrophic postal mistake happens to Babu Bhatt's immigration paperwork?",
        "correct": "Jerry held Babu's mail while he was away on vacation",
        "wrong": ["Newman accidentally dropped the envelope into a storm drain", "George mistakenly shredded the forms at his office", "Kramer used the official documents to line his bird cage"],
        "d": 2
    },
    {
        "q": "To which country is Babu Bhatt deported after his visa renewal deadline passes in 'The Visa'?",
        "correct": "Pakistan",
        "wrong": ["Bangladesh", "India", "Afghanistan"],
        "d": 1
    },
    {
        "q": "In 'The Movie', what fictional film does Jerry desperately try to see while George struggles to save seats?",
        "correct": "CheckMate",
        "wrong": ["Death Blow: The Action Blockbuster", "Rochelle, Rochelle: A Young Girl's Journey", "Prognosis Negative: The Final Verdict"],
        "d": 2
    },
    {
        "q": "In 'The Outing', what famous phrase does Jerry repeatedly assert when mistakenly identified as gay by a reporter?",
        "correct": "\"Not that there's anything wrong with that!\"",
        "wrong": ["\"To each his own personal lifestyle choice!\"", "\"We are entirely secure in our true masculinity!\"", "\"Love is love wherever you happen to find it!\""],
        "d": 1
    },
    {
        "q": "What is the name of the NYU university newspaper reporter who writes the outing article in 'The Outing'?",
        "correct": "Sharon Davis",
        "wrong": ["Allison Foster", "Rachel Goldstein", "Dana Hamilton"],
        "d": 2
    },
    {
        "q": "In 'The Shoes', what does NBC president Russell Dalrymple get caught staring at during a meeting with Elaine?",
        "correct": "Elaine's exposed cleavage",
        "wrong": ["Her expensive green designer leather shoes", "A chocolate stain on the front collar of her shirt", "The handwritten outline of the upcoming pilot episode"],
        "d": 1
    },
    {
        "q": "In 'The Handicap Spot', whose car does George park in a reserved handicapped space at the shopping center?",
        "correct": "His father Frank Costanza's car",
        "wrong": ["His friend Jerry Seinfeld's luxury sedan", "His mother Estelle's private convertible", "His uncle Leo's station wagon vehicle"],
        "d": 1
    },
    {
        "q": "What happens to the disabled woman, Lola, as a result of George parking in her designated handicap spot?",
        "correct": "Her wheelchair was smashed after rolling down an incline",
        "wrong": ["She missed her critical physical therapy appointment", "She was forced to roll three miles through heavy rain", "She fell and suffered a serious fractured collarbone"],
        "d": 3
    },
    {
        "q": "What cheap replacement item do George and Kramer purchase for Lola to make amends in 'The Handicap Spot'?",
        "correct": "A severely defective used motorized wheelchair",
        "wrong": ["A pair of lightweight aluminum walking crutches", "A discounted manual hospital mobility wheelchair", "An electric four-wheeled handicap mobility scooter"],
        "d": 3
    },

    # --- SEASON 4 FINALE & ICONIC SURGERIES (26-40) ---
    {
        "q": "In 'The Junior Mint', who is undergoing surgery while Jerry and Kramer observe from the surgical viewing balcony?",
        "correct": "Elaine's artist ex-boyfriend Roy",
        "wrong": ["George's childhood friend Lloyd Braun", "Jerry's longtime agent Vic Daniels", "Kramer's bowling teammate Mickey Abbott"],
        "d": 2
    },
    {
        "q": "What surgical operation is Roy undergoing when Kramer accidentally drops the Junior Mint candy into his body?",
        "correct": "A splenectomy procedure",
        "wrong": ["An emergency appendectomy procedure", "A triple heart bypass procedure", "A gallbladder removal procedure"],
        "d": 3
    },
    {
        "q": "According to the surgeon in 'The Junior Mint', why does Roy make a miraculous medical recovery?",
        "correct": "His recovery was beyond medical explanation",
        "wrong": ["The peppermint candy acted as an internal sterile barrier", "The sugar elevated his white blood cell count significantly", "The gelatin coating absorbed all post-operative toxins"],
        "d": 3
    },
    {
        "q": "In 'The Smelly Car', what causes an unbearable odor to cling permanently to Jerry's car and Elaine's hair?",
        "correct": "Severe body odor from a parking garage valet",
        "wrong": ["A rotten carton of milk hidden beneath the back seat", "A dead rodent decomposing inside the ventilation fan", "A punctured container of commercial seafood bait"],
        "d": 1
    },
    {
        "q": "What make and model of vehicle does Jerry own that is ruined by the valet's body odor in 'The Smelly Car'?",
        "correct": "BMW 5-Series convertible",
        "wrong": ["Saab 900 Turbo convertible", "Volvo 240 DL station wagon", "Mercedes-Benz 300E sedan"],
        "d": 3
    },
    {
        "q": "In 'The Pilot', which celebrated actor plays the television version of George Costanza in the NBC pilot?",
        "correct": "Jeremy Piven",
        "wrong": ["Stephen Tobolowsky", "Richard Fancy", "Bob Odenkirk"],
        "d": 3
    },
    {
        "q": "What radical life change does NBC president Russell Dalrymple make because of his obsession with Elaine?",
        "correct": "He joins Greenpeace to fight ocean whalers",
        "wrong": ["He resigns from television to write romantic poetry", "He moves into an apartment right across from her building", "He converts to Latvian Orthodox Christianity"],
        "d": 3
    },
    {
        "q": "Why is the 'Jerry' pilot abruptly cancelled after Russell Dalrymple leaves NBC in 'The Pilot'?",
        "correct": "Incoming NBC president Rita Kirson despised the show",
        "wrong": ["Network test audiences gave the pilot the lowest rating ever", "Jerry Seinfeld refused to sign a multi-year talent option", "Advertisers boycotted the pilot over offensive dialogue"],
        "d": 3
    },
    {
        "q": "What character does Crazy Joe Davola dress up as when stalking Jerry at the NBC studio taping?",
        "correct": "Pagliacci the tragic opera clown",
        "wrong": ["A terrifying medieval castle executioner", "A menacing silent film vampire monster", "An authentic Renaissance court jester"],
        "d": 1
    },
    {
        "q": "In 'The Mango', what fruit does Kramer purchase from Joe's Fruit Stand that revitalizes George's confidence?",
        "correct": "A ripe tropical mango",
        "wrong": ["A sweet Mackinaw peach", "A fresh honeydew melon", "A ripe South American papaya"],
        "d": 3
    },
    {
        "q": "Why is George banned from Joe's Fruit Stand in 'The Mango'?",
        "correct": "He squeezed fruit without intending to purchase it",
        "wrong": ["He argued aggressively over the price of organic plums", "He dropped an entire pyramid display of Florida oranges", "He tried to return a half-eaten cantaloupe for cash"],
        "d": 1
    },
    {
        "q": "In 'The Puffy Shirt', what communication quirk does Kramer's fashion designer girlfriend Leslie possess?",
        "correct": "She speaks in an almost inaudible low whisper",
        "wrong": ["She speaks extremely rapidly without taking any breaths", "She stands uncomfortably close to whoever she speaks to", "She speaks in an excessively loud, booming theatrical voice"],
        "d": 1
    },
    {
        "q": "On which national morning program does Jerry wear the ridiculous puffy pirate shirt?",
        "correct": "The Today Show with Bryant Gumbel",
        "wrong": ["Good Morning America with Charles Gibson", "CBS This Morning with Harry Smith", "Live with Regis and Kathie Lee"],
        "d": 2
    },
    {
        "q": "What does Bryant Gumbel say on live national television that deeply insults Jerry's puffy shirt?",
        "correct": "\"You look like a pirate!\"",
        "wrong": ["\"You look like an extra from a cheap period play!\"", "\"Did you lose a bet with a costume designer?!\"", "\"That is the most absurd shirt in television history!\""],
        "d": 3
    },
    {
        "q": "What happens to Leslie's pirate clothing line immediately following the disastrous Today Show appearance?",
        "correct": "Her boutique orders were canceled and homeless people wore them",
        "wrong": ["High fashion runways in Paris embraced the design overnight", "Every major department store demanded exclusive distribution", "The clothes were bought by a regional traveling theater company"],
        "d": 2
    },

    # --- SEASON 5 HIGHLIGHTS & CLASSICS (41-75) ---
    {
        "q": "In 'The Glasses', what does a squinting George believe he sees cousin Jeffrey doing in the street?",
        "correct": "Kissing Jerry's current girlfriend Amy",
        "wrong": ["Stealing an expensive leather jacket from a store", "Eating food discarded in a public trash receptacle", "Vandalizing a parked police patrol cruiser"],
        "d": 3
    },
    {
        "q": "What bizarre replacement frames does Kramer purchase for George at a specialized optical shop?",
        "correct": "Ladies' frames with tortoiseshell coloring",
        "wrong": ["Thick rimmed vintage horn-rimmed bifocals", "Wire-rimmed circular antique reading spectacles", "Heavy plastic prescription safety goggles"],
        "d": 3
    },
    {
        "q": "In 'The Sniffing Accountant', why are Jerry, Kramer, and Newman suspicious of Jerry's accountant Doug?",
        "correct": "He sniffs constantly, leading them to suspect cocaine use",
        "wrong": ["He drives an expensive sports car beyond his known income", "He keeps stacks of unmarked foreign banknotes in his safe", "He refused to show Jerry the original quarterly tax filings"],
        "d": 1
    },
    {
        "q": "What iconic bar stunt does Kramer perform at the lounge in 'The Sniffing Accountant'?",
        "correct": "Drinking a beer while simultaneously puffing a cigarette",
        "wrong": ["Balancing five pint glasses on his outstretched arm", "Swallowing a shot of tequila with a flaming lime peel", "Downing a mug of draft beer in under three seconds"],
        "d": 1
    },
    {
        "q": "What toast does Kramer deliver while drinking beer and smoking a cigarette in 'The Sniffing Accountant'?",
        "correct": "\"Here's to feeling good all the time!\"",
        "wrong": ["\"To the good life and easy money!\"", "\"May we never see tomorrow morning!\"", "\"Here's to staying lucky every single day!\""],
        "d": 1
    },
    {
        "q": "In 'The Bris', who is hired to perform the circumcision ceremony on Jerry and Elaine's friends' baby?",
        "correct": "An extremely neurotic, anxious mohel",
        "wrong": ["A traditional Orthodox rabbi from Brooklyn", "A pediatric surgeon from Mount Sinai Hospital", "A holistic religious elder recommended by Kramer"],
        "d": 2
    },
    {
        "q": "Which actor delivered the hysterical guest performance as the high-strung mohel in 'The Bris'?",
        "correct": "Charles Levin",
        "wrong": ["Larry Hankin", "Mark Metcalf", "Philip Baker Hall"],
        "d": 3
    },
    {
        "q": "What mythical creature does Kramer become obsessed with finding inside the hospital in 'The Bris'?",
        "correct": "A terrifying half-man, half-pig creature",
        "wrong": ["A lab-grown genetic clone of a hospital patient", "A feral hospital phantom residing inside the air vents", "An illegal alien test subject kept on the eighth floor"],
        "d": 3
    },
    {
        "q": "In 'The Lip Reader', what profession does Jerry's date Laura practice that George wants to exploit at a party?",
        "correct": "A deaf professional tennis lineswoman",
        "wrong": ["A certified courtroom stenographer reporter", "A professional lip-reading speech pathologist", "An acoustic technician for classical recording studios"],
        "d": 3
    },
    {
        "q": "What word does Laura mistakenly think George's ex-girlfriend says when reading her lips across the room?",
        "correct": "\"Sweeper\" instead of \"sleep with\"",
        "wrong": ["\"Never\" instead of \"forever\"", "\"Leave\" instead of \"love\"", "\"Crazy\" instead of \"lazy\""],
        "d": 1
    },
    {
        "q": "In 'The Non-Fat Yogurt', what surprising medical result do Jerry and Elaine receive from their blood tests?",
        "correct": "Their body weight and cholesterol increased unexpectedly",
        "wrong": ["Their blood sugar levels dropped to dangerous levels", "Their blood pressure spiked beyond safe parameters", "Their red blood cell count indicated acute fatigue"],
        "d": 2
    },
    {
        "q": "What prominent New York political candidate uses the non-fat yogurt controversy in his campaign platform?",
        "correct": "Rudy Giuliani",
        "wrong": ["David Dinkins", "Ed Koch", "Michael Bloomberg"],
        "d": 2
    },
    {
        "q": "In 'The Barber', why does Jerry dread having his hair cut by his longtime Italian barber Enzo?",
        "correct": "Enzo consistently gives him terrible, outdated haircuts",
        "wrong": ["Enzo charges outrageous prices for standard trims", "Enzo spends the entire session complaining about politics", "Enzo frequently knicks his neck with straight razors"],
        "d": 3
    },
    {
        "q": "What classical opera music plays dramatically throughout 'The Barber' as Jerry seeks a covert haircut?",
        "correct": "Gioachino Rossini's The Barber of Seville",
        "wrong": ["Giuseppe Verdi's Rigoletto", "Giacomo Puccini's La Bohème", "Wolfgang Mozart's The Marriage of Figaro"],
        "d": 3
    },
    {
        "q": "In 'The Masseuse', why is George utterly obsessed with Jerry's girlfriend Jodi?",
        "correct": "She is the only person on earth who genuinely dislikes him",
        "wrong": ["She refused to provide him a complimentary shoulder rub", "She commented critically on his personal posture", "She gave Jerry an hour-long massage right in front of him"],
        "d": 2
    },
    {
        "q": "In 'The Cigar Store Indian', what gift does Jerry bring to Elaine's apartment that offends his Native American date?",
        "correct": "A life-sized carved wooden cigar store Indian statue",
        "wrong": ["An authentic antique peace pipe from the southwest", "A handwoven traditional Navajo reservation blanket", "A framed vintage print of Chief Sitting Bull"],
        "d": 2
    },
    {
        "q": "What is the name of the Native American woman Jerry dates in 'The Cigar Store Indian'?",
        "correct": "Winona",
        "wrong": ["Sasha", "Patrice", "Cheryl"],
        "d": 3
    },
    {
        "q": "In 'The Conversion', why does George decide to convert to the Latvian Orthodox Church?",
        "correct": "To prevent his religious girlfriend Sasha from breaking up",
        "wrong": ["To qualify for an apartment owned by the diocese", "To impress a wealthy foreign philanthropist patron", "To participate in an exclusive private social club"],
        "d": 1
    },
    {
        "q": "What mythical mystical allure does a Latvian Orthodox nun claim Kramer possesses in 'The Conversion'?",
        "correct": "\"The Kavorka\" (the lure of the animal)",
        "wrong": ["\"The Charm of the Serpent\"", "\"The Magnetism of the Wolf\"", "\"The Spirit of the Wild Lynx\""],
        "d": 1
    },
    {
        "q": "In 'The Stall', what desperate plea does Elaine make to a neighboring patron in a public restroom?",
        "correct": "\"Can you spare a square?!\"",
        "wrong": ["\"Do you have any tissues to spare?!\"", "\"Could you pass some paper over the stall?!\"", "\"Is there any napkin under your door?!\""],
        "d": 2
    },
    {
        "q": "Who turns out to be the woman who refused Elaine toilet paper in 'The Stall'?",
        "correct": "Jerry's current girlfriend Jane",
        "wrong": ["George's coworker Ada", "Newman's postal supervisor", "Russell Dalrymple's sister"],
        "d": 2
    },
    {
        "q": "What handsome 'mimbo' rock-climbing enthusiast does Elaine date in 'The Stall'?",
        "correct": "Tony",
        "wrong": ["Brett", "Craig", "Keith"],
        "d": 3
    },
    {
        "q": "Which actor portrayed the rugged rock climber Tony in 'The Stall'?",
        "correct": "Dan Cortese",
        "wrong": ["Antonio Sabato Jr.", "Mark Valley", "Brian Austin Green"],
        "d": 3
    },
    {
        "q": "What accident happens to Tony's handsome face while rock climbing with George and Kramer?",
        "correct": "He falls down a steep rock face and injures his nose",
        "wrong": ["He gets severely stung by a swarm of mountain wasps", "He is struck in the forehead by falling loose shale", "He scrapes his cheek against a sharp granite cliff edge"],
        "d": 1
    },
    {
        "q": "In 'The Marine Biologist', what career does Jerry tell George's college crush Diane that George pursues?",
        "correct": "A marine biologist studying sea life",
        "wrong": ["A renowned architect specializing in skyscrapers", "A high-ranking foreign diplomat with the UN", "An executive vice president at a latex firm"],
        "d": 1
    },

    # --- CLIMACTIC SEASON 5 FINALE ARCS (76-100) ---
    {
        "q": "What famous opening line does George utter when recounting his beach heroics in 'The Marine Biologist'?",
        "correct": "\"The sea was angry that day, my friends!\"",
        "wrong": ["\"The ocean was raging with fury that afternoon!\"", "\"Waves were crashing violently against the shoreline!\"", "\"Nature was screaming at the top of its lungs!\""],
        "d": 1
    },
    {
        "q": "What lodged object does George dramatically pull from the blowhole of the beached whale in 'The Marine Biologist'?",
        "correct": "A Titleist golf ball hit by Kramer",
        "wrong": ["A plastic six-pack beverage ring holder", "A crumpled waterproof sailing navigation chart", "An aluminum beer can from a party boat"],
        "d": 2
    },
    {
        "q": "In 'The Dinner Party', what bakery treat do Jerry and Elaine fail to get when someone buys the last one?",
        "correct": "A fresh chocolate babka pastry",
        "wrong": ["A fresh braided almond kringle pastry", "A box of powdered raspberry jelly donuts", "A traditional cinnamon apple strudel loaf"],
        "d": 3
    },
    {
        "q": "What does Jerry declare to Elaine about the cinnamon babka when chocolate is sold out?",
        "correct": "Cinnamon is not a lesser babka",
        "wrong": ["Cinnamon babka is an insulting consolation prize", "Nobody in New York voluntarily orders cinnamon pastry", "Cinnamon was created for people who lack refinement"],
        "d": 1
    },
    {
        "q": "What baked good does Jerry hold up as an inspiring metaphor for racial harmony in 'The Dinner Party'?",
        "correct": "A black and white cookie",
        "wrong": ["A marbled chocolate cheesecake", "A half-vanilla, half-chocolate cupcake", "A layered checkerboard sponge cake"],
        "d": 2
    },
    {
        "q": "What heavy coat does George proudly wear to the dinner party that knocks over merchandise in the liquor store?",
        "correct": "A massive Gore-Tex winter coat",
        "wrong": ["A heavy full-length shearling fur coat", "An authentic down-filled Arctic exploration parka", "A double-breasted vintage wool trench coat"],
        "d": 1
    },
    {
        "q": "In 'The Pie', why does Jerry refuse to eat the pizza prepared by Italian restaurateur Poppie?",
        "correct": "He saw Poppie exit the restroom without washing his hands",
        "wrong": ["He noticed mold growing along the edges of the cheese", "He watched the kitchen chef drop the raw dough on the floor", "He learned Poppie imported expired tomato sauce from Naples"],
        "d": 1
    },
    {
        "q": "In 'The Stand-In', what is the name of Kramer's diminutive actor friend with whom he works as a television stand-in?",
        "correct": "Mickey Abbott",
        "wrong": ["Kenny Bania", "Phil Totola", "Russell Dalrymple"],
        "d": 3
    },
    {
        "q": "Why does Mickey Abbott become furious with Kramer during a television soap opera production?",
        "correct": "Kramer wore lifts in his shoes, making Mickey look shorter",
        "wrong": ["Kramer stole his spotlight during a crucial close-up scene", "Kramer forgot his blocking and knocked over a camera crane", "Kramer improvised lines that made the lead director laugh"],
        "d": 3
    },
    {
        "q": "In 'The Wife', which future Friends star plays Jerry's girlfriend Meryl, who poses as his wife for dry cleaning discounts?",
        "correct": "Courteney Cox",
        "wrong": ["Jennifer Aniston", "Lisa Kudrow", "Jane Sibbett"],
        "d": 2
    },
    {
        "q": "In 'The Raincoats', what vintage fashion item does Morty Seinfeld try to sell through a local boutique?",
        "correct": "\"The Executive\" beltless trench coat",
        "wrong": ["The reversible waterproof golf windbreaker", "The double-collared lightweight cabana shirt", "The crease-resistant leisure resort slacks"],
        "d": 3
    },
    {
        "q": "What serious historical film are Jerry and his girlfriend Rachel caught passionately making out during in 'The Raincoats'?",
        "correct": "Schindler's List",
        "wrong": ["The English Patient", "The Last Emperor", "Saving Private Ryan"],
        "d": 2
    },
    {
        "q": "Who catches Jerry making out during 'Schindler's List' and gleefully tattles to Jerry's parents?",
        "correct": "Newman",
        "wrong": ["Uncle Leo", "Jack Klompus", "George Costanza"],
        "d": 2
    },
    {
        "q": "In 'The Fire', what does George do when a small grease fire breaks out in the kitchen during a children's birthday party?",
        "correct": "He knocks down children and an old lady with a walker to escape",
        "wrong": ["He locks himself inside the bathroom until fire trucks arrive", "He grabs the entire birthday cake and runs out into the street", "He hides under the dining room table while screaming for help"],
        "d": 3
    },
    {
        "q": "Which celebrated future director and actor plays Eric the Clown at the birthday party in 'The Fire'?",
        "correct": "Jon Favreau",
        "wrong": ["Vince Vaughn", "Peter Berg", "Judd Apatow"],
        "d": 2
    },
    {
        "q": "What insult does George throw at Eric the Clown regarding the clown's professional knowledge?",
        "correct": "\"You're living in the past, man! You're hung up on some clown from the sixties, man!\"",
        "wrong": ["\"You wouldn't know a real circus routine if a trapeze hit you!\"", "\"Any amateur in makeup could twist balloon animals better than you!\"", "\"You belong in a carnival dunk tank, not at a private party!\""],
        "d": 2
    },
    {
        "q": "In 'The Hamptons', what reason does George give for the embarrassing appearance of his anatomy after swimming?",
        "correct": "\"Shrinkage\" caused by cold pool water",
        "wrong": ["\"Exhaustion\" from swimming twenty laps", "\"A reaction\" to heavy pool chlorination", "\"Muscle contraction\" from an early morning cramp"],
        "d": 2
    },
    {
        "q": "What famous three-word phrase does George repeatedly shout to defend himself in 'The Hamptons'?",
        "correct": "\"I was in the pool!\"",
        "wrong": ["\"It was freezing cold!\"", "\"Water does that to everyone!\"", "\"It expands later on!\""],
        "d": 2
    },
    {
        "q": "What dish does Jerry discover Kramer prepared with kosher eggs that deeply offends Jerry's date Rachel?",
        "correct": "Scrambled eggs cooked with poached lobster",
        "wrong": ["An omelette prepared with crispy bacon strips", "French toast dipped in pork sausage drippings", "Eggs benedict topped with commercial crab meat"],
        "d": 3
    },
    {
        "q": "How does Jerry describe the visual appearance of Dr. Ben and Carol's newborn baby in 'The Hamptons'?",
        "correct": "\"Breathtaking\"",
        "wrong": ["\"Magnificent\"", "\"Stunning\"", "\"Angelic\""],
        "d": 1
    },
    {
        "q": "In 'The Opposite', what life philosophy does George decide to adopt after realizing every instinct he has is wrong?",
        "correct": "Doing the exact opposite of every single natural instinct",
        "wrong": ["Consulting an astrologer before making any major life decision", "Relying purely on the flip of a silver dollar coin", "Letting Jerry Seinfeld make all his professional choices"],
        "d": 1
    },
    {
        "q": "What lunch order does George make at Monk's diner when demonstrating his new 'opposite' philosophy?",
        "correct": "Chicken salad on rye with untoasted bread and a cup of tea",
        "wrong": ["Tuna on toast with potato chips and a chocolate milkshake", "A hot pastrami sandwich with coleslaw and a black coffee", "A grilled cheese sandwich with tomato soup and ginger ale"],
        "d": 2
    },
    {
        "q": "What bold opening line does George say to an attractive woman sitting at the diner counter in 'The Opposite'?",
        "correct": "\"My name is George. I'm unemployed and I live with my parents.\"",
        "wrong": ["\"I have no money, no prospects, and completely zero self-esteem.\"", "\"I usually fail at everything I try, but I wanted to say hello.\"", "\"I am currently broke, bald, and living on my mother's couch.\""],
        "d": 1
    },
    {
        "q": "What major sports organization hires George Costanza as Assistant to the Traveling Secretary in 'The Opposite'?",
        "correct": "The New York Yankees baseball franchise",
        "wrong": ["The New York Mets baseball organization", "The New York Knicks basketball franchise", "The New York Rangers hockey organization"],
        "d": 2
    },
    {
        "q": "What eccentric team owner hires George after George aggressively berates his management decisions in 'The Opposite'?",
        "correct": "George Steinbrenner",
        "wrong": ["Fred Wilpon of the Mets", "James Dolan of the Knicks", "Leon Hess of the Jets"],
        "d": 2
    },
    {
        "q": "In 'The Ticket', why does Newman drag Jerry to traffic court as a character witness for his speeding ticket?",
        "correct": "He claimed he was rushing home to save his suicidal friend Martin",
        "wrong": ["He claimed his postal speedometer was completely broken", "He asserted he was delivering an urgent certified government dispatch", "He argued he was speeding away from an aggressive stray dog"],
        "d": 2
    },
    {
        "q": "In 'The Airport', what unfortunate meal does Elaine get stuck receiving in coach while Jerry enjoys first class?",
        "correct": "A stale kosher meal meant for another passenger",
        "wrong": ["A cold rubbery vegetarian pasta platter", "A dry turkey sandwich with expired mayonnaise", "An unseasoned boiled fish tray with limp broccoli"],
        "d": 2
    },
    {
        "q": "In 'The Outing', how does George attempt to exploit the false newspaper article about his sexuality?",
        "correct": "To break up with his clingy girlfriend Allison",
        "wrong": ["To get out of jury duty for a high-profile trial", "To win an apartment in a supportive community co-op", "To avoid paying back taxes to the internal revenue service"],
        "d": 2
    },
    {
        "q": "In 'The Mango', what shocking relationship truth does Elaine confess to Jerry that shatters his confidence?",
        "correct": "She faked all of her orgasms during their relationship",
        "wrong": ["She only dated him to get free tickets to comedy clubs", "She secretly dated his rival stand-up comic Kenny Bania", "She hated all of his friends from the very beginning"],
        "d": 2
    },
    {
        "q": "In 'The Non-Fat Yogurt', what does an impressionable neighborhood boy shout at Jerry after hearing him curse?",
        "correct": "\"You're a damn fool, Seinfeld!\"",
        "wrong": ["\"You ruined my ice cream, Seinfeld!\"", "\"You're full of it, funny man!\"", "\"Get out of here, you jerk!\""],
        "d": 2
    },
    {
        "q": "In 'The Barber', what is the name of Enzo's handsome nephew who gives Jerry secret high-fashion haircuts?",
        "correct": "Gino",
        "wrong": ["Marco", "Angelo", "Santino"],
        "d": 2
    },
    {
        "q": "In 'The Pitch', what is the name of the junior NBC executive who accompanies Russell Dalrymple in meetings?",
        "correct": "Stu Chermak",
        "wrong": ["Donald Rivers", "Arthur Sackler", "Craig Sterling"],
        "d": 2
    },
    {
        "q": "In 'The Smelly Car', what does the dry cleaner tell Jerry when Jerry brings his leather jacket in to remove the B.O.?",
        "correct": "The smell has embedded itself into the cellular structure of the leather",
        "wrong": ["They cannot accept garments that pose a hazardous biological risk", "It will require ten cycles of chemical solvent cleaning at triple price", "He should burn the jacket immediately to prevent contamination"],
        "d": 2
    },
    {
        "q": "In 'The Handicap Spot', what happens to Frank Costanza's car while parked in the reserved handicap spot?",
        "correct": "An enraged angry mob vandalizes and wrecks the vehicle",
        "wrong": ["It is towed away and impounded in an inaccessible lot", "A delivery truck backs directly over the front hood engine", "The tires are slashed and the windows are spray-painted"],
        "d": 2
    },
    {
        "q": "In 'The Opposite', what does Jerry realize about his own life balance while George's fortunes dramatically rise?",
        "correct": "He is 'Even Steven'—everything in his life always breaks even",
        "wrong": ["He is doomed to absorb all of George's former bad luck", "He is destined to remain a mediocre stand-up comedian forever", "He needs to move out of Manhattan to find true contentment"],
        "d": 2
    }
]

if __name__ == "__main__":
    out = assemble_batch(raw_questions, 2)
    save_json(out, "tools/staging/seinfeld_batch2.json")
