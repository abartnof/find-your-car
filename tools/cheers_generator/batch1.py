import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from utils import assemble_batch, save_json

raw_questions = [
    # --- SAM MALONE (1-20) ---
    {
        "q": "What was Sam Malone's jersey number when pitching for the Boston Red Sox?",
        "correct": "16",
        "wrong": ["24", "7", "33"],
        "d": 1
    },
    {
        "q": "What nickname did Sam Malone earn during his Major League Baseball pitching career?",
        "correct": "\"Mayday\" Malone",
        "wrong": ["\"Slaphappy\" Sam", "\"Fastball\" Malone", "\"The Boston Flamethrower\""],
        "d": 1
    },
    {
        "q": "Why did Sam Malone retire from professional baseball before opening Cheers?",
        "correct": "He struggled with severe alcoholism",
        "wrong": ["He suffered a career-ending torn rotator cuff", "He was banned for gambling on games", "He lost passion for the sport after winning the pennant"],
        "d": 1
    },
    {
        "q": "What classic sports car is Sam Malone's prized personal possession?",
        "correct": "1967 Chevrolet Corvette Stingray",
        "wrong": ["1965 Ford Mustang Fastback", "1969 Chevrolet Camaro SS", "1970 Dodge Challenger"],
        "d": 1
    },
    {
        "q": "What non-alcoholic beverage does Sam Malone typically drink while tending bar?",
        "correct": "Club soda with lime",
        "wrong": ["Diet cola", "Tomato juice", "Ginger ale"],
        "d": 1
    },
    {
        "q": "What was the name of Sam Malone's short-lived, self-absorbed agent who represented him during his baseball days?",
        "correct": "Dave Richards",
        "wrong": ["Rick Walker", "Brad Douglas", "Phil Cooper"],
        "d": 2
    },
    {
        "q": "In Season 1, what does Sam Malone discover in his office safe that had been left behind by a former customer?",
        "correct": "A lucky bottle cap from his first major league win",
        "wrong": ["A stash of Confederate currency", "An unsigned Babe Ruth baseball", "A stolen diamond ring"],
        "d": 3
    },
    {
        "q": "What good luck charm does Sam Malone temporarily lose, causing him to believe he has lost his mojo with women?",
        "correct": "His lucky bottle cap",
        "wrong": ["His Red Sox championship ring", "His silver belt buckle", "His vintage dice keychain"],
        "d": 2
    },
    {
        "q": "Who buys Cheers from Sam at the end of Season 5 when Sam sails around the world?",
        "correct": "The Lillian Corporation",
        "wrong": ["Gary from Olde Towne Tavern", "Melville's Restaurant Group", "The Boston Athletic Club"],
        "d": 1
    },
    {
        "q": "For how much money does Sam Malone buy Cheers back from the Lillian Corporation in Season 6?",
        "correct": "85 cents",
        "wrong": ["One dollar", "10,000 dollars", "500 dollars"],
        "d": 2
    },
    {
        "q": "What was Sam Malone's specific pitching role on the Boston Red Sox?",
        "correct": "Relief pitcher / closer",
        "wrong": ["Starting pitcher", "Middle reliever", "Knuckleball specialist"],
        "d": 1
    },
    {
        "q": "What was the name of the boat Sam purchased to sail around the world between Seasons 5 and 6?",
        "correct": "The Trudy",
        "wrong": ["The Flying Diane", "The Boston Lady", "The Mayday Mariner"],
        "d": 2
    },
    {
        "q": "What happened to Sam's sailboat 'The Trudy' during his voyage between Seasons 5 and 6?",
        "correct": "It sank in the Caribbean",
        "wrong": ["It was confiscated by the Coast Guard", "He sold it in Bermuda to pay bar debts", "It was stolen in Miami"],
        "d": 2
    },
    {
        "q": "Which rival pitcher and former teammate of Sam's wrote a tell-all autobiography mentioning Sam's exploits?",
        "correct": "Rick Walker",
        "wrong": ["Dutch Kincaid", "Lefty Hernandez", "Buzz Anderson"],
        "d": 3
    },
    {
        "q": "In the episode 'Showdown: Part 2', what do Sam and Diane do right before their famous first passionate kiss?",
        "correct": "Engage in a screaming match threatening physical violence",
        "wrong": ["Recite a romantic Shakespearean sonnet", "Spill a pitcher of beer across the mahogany bar", "Apologize tearfully in Sam's back office"],
        "d": 1
    },
    {
        "q": "What physical feature is Sam Malone famously insecure about as he begins aging?",
        "correct": "His thinning hair / hairline",
        "wrong": ["His emerging beer belly", "His crow's feet wrinkles", "His aching pitching elbow"],
        "d": 1
    },
    {
        "q": "In Season 3, what job does Sam take at a local Boston television station?",
        "correct": "Weekend sports anchor",
        "wrong": ["Morning talk show co-host", "Commercial pitchman for a car dealership", "Color commentator for Red Sox broadcasts"],
        "d": 2
    },
    {
        "q": "What made Sam Malone notoriously terrible during his audition as a television sports anchor?",
        "correct": "He could not read the Teleprompter naturally and froze on camera",
        "wrong": ["He insulted the Boston Celtics mascot live on air", "He repeatedly pronounced athlete names wrong", "He started drinking soda on camera during commercials"],
        "d": 3
    },
    {
        "q": "What sport does Sam play against rival bar owner Gary in an attempt to win back the Cheers sign?",
        "correct": "Bowling",
        "wrong": ["Softball", "Basketball", "Darts"],
        "d": 2
    },
    {
        "q": "What is the final line spoken by Sam Malone in the series finale 'One for the Road'?",
        "correct": "\"Sorry, we're closed.\"",
        "wrong": ["\"Goodnight, everybody.\"", "\"See you tomorrow, Norm.\"", "\"Have a good night, Boston.\""],
        "d": 1
    },

    # --- DIANE CHAMBERS (21-40) ---
    {
        "q": "In the pilot episode, what is Diane Chambers' initial profession or status when she enters Cheers?",
        "correct": "A literature student and teaching assistant engaged to her professor",
        "wrong": ["A cocktail waitress seeking a new shift", "A Boston globe journalist researching local pubs", "A lawyer celebrating passing the Massachusetts bar exam"],
        "d": 1
    },
    {
        "q": "What was the name of the snooty literature professor who abandoned Diane at Cheers in the pilot episode?",
        "correct": "Sumner Sloane",
        "wrong": ["Simon Finch-Royce", "Derek Underwood", "Elliott Randolph"],
        "d": 1
    },
    {
        "q": "Where were Sumner Sloane and Diane Chambers supposedly traveling before he abandoned her in the pilot?",
        "correct": "Barbados",
        "wrong": ["Paris", "Florence", "Bermuda"],
        "d": 3
    },
    {
        "q": "Why did Sumner Sloane leave Diane waiting at Cheers in the pilot episode?",
        "correct": "To retrieve his grandmother's wedding ring from his ex-wife",
        "wrong": ["To confirm his flight tickets at Logan Airport", "To grade his undergraduate midterm papers", "To cash an academic fellowship check"],
        "d": 2
    },
    {
        "q": "What breed of dog did Diane Chambers own, named Elizabeth Barrett Browning?",
        "correct": "Poodle",
        "wrong": ["Golden Retriever", "Cocker Spaniel", "Yorkshire Terrier"],
        "d": 3
    },
    {
        "q": "Which 19th-century English Romantic poet does Diane Chambers frequently quote to annoy Carla and Sam?",
        "correct": "John Keats",
        "wrong": ["Lord Byron", "Percy Bysshe Shelley", "William Wordsworth"],
        "d": 2
    },
    {
        "q": "What type of facility did Diane Chambers check into between Seasons 2 and 3 following her breakup with Sam?",
        "correct": "A psychiatric sanatorium / mental health clinic",
        "wrong": ["A French culinary academy in Paris", "A monastery retreat in Vermont", "An exclusive writing colony in Maine"],
        "d": 1
    },
    {
        "q": "Whom did Diane Chambers meet and begin dating while staying at the psychiatric sanatorium?",
        "correct": "Dr. Frasier Crane",
        "wrong": ["Dr. Simon Finch-Royce", "Dr. Robert Caplan", "Dr. Clinton Sternin"],
        "d": 1
    },
    {
        "q": "In Season 3, where does Frasier propose to Diane, only to be abandoned at the altar later in Europe?",
        "correct": "Italy",
        "wrong": ["France", "England", "Switzerland"],
        "d": 3
    },
    {
        "q": "What was the title of the epic novel Diane Chambers spent years attempting to write?",
        "correct": "A novel based on the lives and patrons of Cheers",
        "wrong": ["The Crimson Beacon", "The Ivy Leaves of Boston", "Echoes of New England"],
        "d": 2
    },
    {
        "q": "What high-culture art form did Diane Chambers obsessively practice, even auditioning for a local Boston company?",
        "correct": "Ballet",
        "wrong": ["Opera singing", "Modern dance", "Classical cello"],
        "d": 2
    },
    {
        "q": "What wealthy, eccentric intellectual did Diane date in Season 2 who challenged Sam to a high-stakes intellectual duel?",
        "correct": "Derek Drake",
        "wrong": ["Sumner Sloane", "Dr. Simon Finch-Royce", "Ludlow Fowler"],
        "d": 3
    },
    {
        "q": "What allergic reaction did Diane Chambers famously suffer from whenever she was around cats?",
        "correct": "Uncontrollable sneezing and watery eyes",
        "wrong": ["Hives across her face", "Severe asthma attacks", "Temporary loss of speech"],
        "d": 2
    },
    {
        "q": "In the Season 5 finale 'I Do, Adieu', why does Diane ultimately leave Boston and Sam Malone?",
        "correct": "To finish her manuscript in Los Angeles after getting a book deal",
        "wrong": ["To marry Frasier Crane in Seattle", "To take an endowed professorship at Oxford", "To open her own French cafe in Montreal"],
        "d": 1
    },
    {
        "q": "What gift does Sam Malone present to Diane in 'I Do, Adieu' that convinces her she must pursue her writing career?",
        "correct": "A typewriter",
        "wrong": ["A first edition of John Keats poetry", "A personalized fountain pen", "A round-trip ticket to Los Angeles"],
        "d": 2
    },
    {
        "q": "When Diane returns in the series finale 'One for the Road', what Hollywood award is she celebrating having won?",
        "correct": "A CableACE Award",
        "wrong": ["An Emmy Award", "A Golden Globe Award", "A Writers Guild of America Award"],
        "d": 3
    },
    {
        "q": "In 'One for the Road', what fictional movie project does Diane claim she wrote that turned into an embarrassing TV movie?",
        "correct": "A dramatic script that was butchered into a cheesy telefilm",
        "wrong": ["A high-concept romantic comedy with Tom Cruise", "A Broadway musical adaptation of Hamlet", "A historical biopic about Abigail Adams"],
        "d": 2
    },
    {
        "q": "In Season 1, what does Diane do when a customer pinches her rear while she is serving drinks?",
        "correct": "Slaps him across the face and demands an apology",
        "wrong": ["Pours a draft beer over his head", "Quietly informs Sam to throw him out", "Ignores it to keep her tips high"],
        "d": 2
    },
    {
        "q": "Which painter did Diane Chambers hire to paint a portrait of her and Sam, leading to endless arguments?",
        "correct": "Phillip Semenko",
        "wrong": ["Henri Rousseau", "Julian Martinez", "Claude Bennett"],
        "d": 3
    },
    {
        "q": "What was Diane Chambers' mother's name, who visited the bar threatening to disinherit Diane unless she married?",
        "correct": "Spencer Chambers",
        "wrong": ["Eleanor Chambers", "Victoria Chambers", "Cordelia Chambers"],
        "d": 3
    },

    # --- COACH ERNIE PANTUSSO (41-60) ---
    {
        "q": "What was Ernie Pantusso's primary role on the Boston Red Sox coaching staff under which he managed Sam Malone?",
        "correct": "Pitching coach",
        "wrong": ["Hitting coach", "Bench coach", "Bullpen catcher"],
        "d": 1
    },
    {
        "q": "What was Ernie Pantusso's universal nickname among all friends and patrons of Cheers?",
        "correct": "Coach",
        "wrong": ["Skip", "Pants", "Cap"],
        "d": 1
    },
    {
        "q": "What was the name of Coach's beloved, plain-looking daughter who visited the bar in Season 1?",
        "correct": "Lisa Pantusso",
        "wrong": ["Maria Pantusso", "Gina Pantusso", "Angela Pantusso"],
        "d": 2
    },
    {
        "q": "In the Season 1 episode 'Coach's Daughter', why was Coach initially devastated about Lisa's fiancé Roy?",
        "correct": "Roy was an arrogant jerk who treated Lisa poorly and openly demeaned her",
        "wrong": ["Roy was a passionate New York Yankees fan", "Roy refused to get married in the Catholic Church", "Roy wanted to move Lisa to Alaska permanently"],
        "d": 2
    },
    {
        "q": "What was Coach Ernie Pantusso's late wife's name, whom he frequently spoke of with deep love?",
        "correct": "Angela",
        "wrong": ["Rose", "Grace", "Lucille"],
        "d": 3
    },
    {
        "q": "What peculiar habit did Coach exhibit when answering the Cheers bar telephone?",
        "correct": "Shouting 'Cheers!' into the receiver or calling out the wrong person's name",
        "wrong": ["Whispering in fear of wiretaps", "Always hanging up after two seconds", "Singing the opening bar of a fight song"],
        "d": 1
    },
    {
        "q": "In Season 1, what second job did Coach take that involved coaching an all-girls Little League team?",
        "correct": "Managing a youth baseball team called the Red Sox",
        "wrong": ["Refereeing middle school basketball games", "Umpiring high school softball", "Directing youth bowling leagues"],
        "d": 3
    },
    {
        "q": "In the Season 2 episode 'Fortune and Men's Weights', what con game is Coach tricked into by a shady grifter?",
        "correct": "Investing in a fraudulent scales-and-vending-machine venture",
        "wrong": ["A counterfeit rare coin swap", "A phony real estate deed in Maine", "A rigged underground poker match"],
        "d": 3
    },
    {
        "q": "What was Coach's response whenever Sam or Diane asked him a complex philosophical question?",
        "correct": "A hilariously literal or completely backward misunderstanding of the premise",
        "wrong": ["Quoting Latin proverbs learned in parochial school", "Pretending to have severe sudden hearing loss", "Changing the subject to Red Sox batting averages"],
        "d": 1
    },
    {
        "q": "In Season 2, Coach attempts to earn his high school diploma by taking what evening class?",
        "correct": "Geography",
        "wrong": ["World History", "Basic Algebra", "American Government"],
        "d": 2
    },
    {
        "q": "Who was the strict evening school teacher who helped Coach study for his high school geography exam?",
        "correct": "George Gaines",
        "wrong": ["Mr. Higgins", "Professor Sumner Sloane", "Mr. Hedenberg"],
        "d": 3
    },
    {
        "q": "What mnemonic device did Coach Ernie Pantusso memorize to pass his geography exam about Albania?",
        "correct": "Albania, Albania, you border on the Adriatic...",
        "wrong": ["Tirana is the capital near the sea...", "The Balkan peaks are snowy and grand...", "Across from Italy lies the land..."],
        "d": 2
    },
    {
        "q": "Which grifter and street magician repeatedly tried to swindle Coach, only to be outwitted or beaten by the bar?",
        "correct": "Harry the Hat (Harry Gittes)",
        "wrong": ["Slick Willy", "Boston Benny", "Fast Eddie"],
        "d": 1
    },
    {
        "q": "What classic bar con does Harry the Hat pull on Coach involving a dollar bill under a glass of water?",
        "correct": "Taking the dollar without touching the inverted glass of water",
        "wrong": ["Guessing the serial number of the bill", "Balancing a quarter on the rim of the glass", "Turning a dollar bill into a ten-dollar bill"],
        "d": 2
    },
    {
        "q": "In Season 3, what romantic interest does Coach pursue who happens to be an older woman named Katherine?",
        "correct": "A woman he met at an adult night school class",
        "wrong": ["A regular customer at Melville's", "Carla's mother Mama Lozupone", "Norm's aunt Margaret"],
        "d": 3
    },
    {
        "q": "What was Coach's standard reaction whenever someone ordered an exotic or complicated cocktail at Cheers?",
        "correct": "Confused blinking followed by offering them a beer or pretzel",
        "wrong": ["Consulting a massive leather-bound bartending manual", "Calling Sam out from the back office in a panic", "Pretending the bar was out of the liquor"],
        "d": 2
    },
    {
        "q": "Why was Nicholas Colasanto's character Coach written off the show between Seasons 3 and 4?",
        "correct": "Nicholas Colasanto tragically passed away from heart disease in 1985",
        "wrong": ["He retired to live in Florida full-time", "He took a role on another television sitcom", "The character was written out to reduce the cast size"],
        "d": 1
    },
    {
        "q": "How was Coach's absence initially explained in early Season 4 dialogue before acknowledging his passing?",
        "correct": "He was traveling to visit relatives and friends",
        "wrong": ["He was managing a baseball winter league in Florida", "He was hospitalized for minor knee surgery", "He was scouting pitching prospects in Ohio"],
        "d": 2
    },
    {
        "q": "In the Season 3 episode 'Cheerio, Cheers', what does Coach do when an English gentleman challenges him to a drinking game?",
        "correct": "Drinks him under the table with polite modesty",
        "wrong": ["Passes out after the second glass of sherry", "Substitutes apple juice for dark ale", "Spills his drinks into an empty vase"],
        "d": 3
    },
    {
        "q": "What framed portrait in the bar was touched by the cast at the end of episodes in memory of Nicholas Colasanto?",
        "correct": "A photograph of Apache leader Geronimo",
        "wrong": ["A photograph of Babe Ruth", "A vintage black-and-white print of Fenway Park", "A painting of an American bald eagle"],
        "d": 2
    },

    # --- WOODY BOYD (61-80) ---
    {
        "q": "What was Woody Boyd's hometown in Indiana before moving to Boston?",
        "correct": "Hanover",
        "wrong": ["Muncie", "Terre Haute", "Kokomo"],
        "d": 1
    },
    {
        "q": "How did Woody Boyd first connect with Ernie 'Coach' Pantusso before arriving at Cheers?",
        "correct": "They were long-time pen pals who exchanged pens through the mail",
        "wrong": ["Woody played junior college baseball against Coach's team", "They were third cousins twice removed", "Coach had scouted Woody's high school baseball team"],
        "d": 3
    },
    {
        "q": "Why did Woody Boyd travel to Cheers in the Season 4 premiere 'Birth, Death, Love and Rice'?",
        "correct": "To meet Coach in person, unaware that Coach had passed away",
        "wrong": ["To audition for Sam's open assistant bartender position", "To attend Harvard University on an agricultural scholarship", "To escape a vengeful farming family in Indiana"],
        "d": 1
    },
    {
        "q": "What is Woody Boyd's full legal birth name?",
        "correct": "Huckleberry Edward Boyd",
        "wrong": ["Woodrow Wilson Boyd", "Woodrow Allen Boyd", "Huckleberry Thomas Boyd"],
        "d": 3
    },
    {
        "q": "What was the name of Woody Boyd's high school sweetheart from Hanover who visited him in Boston?",
        "correct": "Beth Marshall",
        "wrong": ["Kelly Gaines", "Daisy Sue Jenkins", "Mary Lou Miller"],
        "d": 2
    },
    {
        "q": "What was the peculiar shared habit Woody Boyd and his Indiana girlfriend Beth had when eating together?",
        "correct": "They both ate massive, gluttonous quantities of food in rapid succession",
        "wrong": ["They chewed exactly twenty times per bite in silence", "They only ate fried pork rinds dipping them in milk", "They refused to speak while food was on the table"],
        "d": 3
    },
    {
        "q": "What was the name of the wealthy Boston heiress Woody Boyd fell in love with and married?",
        "correct": "Kelly Gaines",
        "wrong": ["Victoria Drake", "Elizabeth Stone", "Penelope Wentworth"],
        "d": 1
    },
    {
        "q": "What was the name of Kelly Gaines' wealthy, snobbish father who looked down upon Woody?",
        "correct": "Walter Gaines",
        "wrong": ["Arthur Gaines", "Preston Gaines", "Randolph Gaines"],
        "d": 2
    },
    {
        "q": "In Season 8, Kelly Gaines leaves for a year of study abroad in which European country?",
        "correct": "France",
        "wrong": ["England", "Switzerland", "Italy"],
        "d": 3
    },
    {
        "q": "What song does Woody Boyd perform at Kelly Gaines' high-society birthday party that becomes a surprise crowd hit?",
        "correct": "\"Kelly, Kelly, Kelly, Kelly...\"",
        "wrong": ["\"The Hanover Corn Song\"", "\"Indiana Sweetheart\"", "\"My Girl From Boston\""],
        "d": 2
    },
    {
        "q": "In Season 11, what surprising public office does Woody Boyd successfully run for and win?",
        "correct": "Boston City Council",
        "wrong": ["Massachusetts State Senate", "Cambridge Mayor", "Suffolk County Commissioner"],
        "d": 1
    },
    {
        "q": "What political strategy does Woody's rival use that accidentally backfires and wins Woody the election?",
        "correct": "Highlighting Woody's complete lack of knowledge, making him look disarmingly honest",
        "wrong": ["Accusing Woody of financial corruption in Indiana", "Challenging Woody to an intellectual televised debate", "Exposing Woody's secret criminal past"],
        "d": 2
    },
    {
        "q": "What odd Hanover tradition did Woody insist upon when preparing for his wedding with Kelly?",
        "correct": "Ice carvings of farm animals and traditional pig-related folk customs",
        "wrong": ["A midnight corn-husking relay race for the groomsmen", "A mandatory square dance in boots before the altar", "Wrestling the bride's father in a mud pit"],
        "d": 2
    },
    {
        "q": "During Woody and Kelly's chaotic wedding ceremony in Season 10, what happened to the officiating minister?",
        "correct": "He collapsed and died right before the vows",
        "wrong": ["He got locked in the church cellar by Carla", "He was struck by lightning on the church steps", "He passed out from drinking sacramental wine"],
        "d": 2
    },
    {
        "q": "Who ended up performing Woody and Kelly's emergency marriage ceremony in the kitchen after the minister's collapse?",
        "correct": "A visiting foreign priest / German minister",
        "wrong": ["Sam Malone using his ship captain's license", "Dr. Frasier Crane via mail ordination", "Cliff Clavin as a justice of the peace"],
        "d": 3
    },
    {
        "q": "What theater role did Woody Boyd play in a local Boston avant-garde production of 'Hair'?",
        "correct": "Claude (in which he was required to perform nude)",
        "wrong": ["Berger", "Woof", "Hud"],
        "d": 3
    },
    {
        "q": "What odd snack food did Woody Boyd frequently invent or crave from his childhood in Hanover?",
        "correct": "Veg-a-Loo / deep-fried corn concoctions and bizarre casseroles",
        "wrong": ["Peanut butter and sardine toast", "Pickled hog ears in hot sauce", "Raw turnip sandwiches on sourdough"],
        "d": 3
    },
    {
        "q": "What pet pig did Woody Boyd fondly reminisce about from his family farm in Hanover?",
        "correct": "Arnold",
        "wrong": ["Barnaby", "Wilbur", "Pinky"],
        "d": 3
    },
    {
        "q": "In Season 6, what commercial did Woody Boyd film that aired on Boston local television?",
        "correct": "A commercial for 'Veg-a-Lax' laxative",
        "wrong": ["A commercial for a used pickup truck dealership", "A public service announcement for fire safety", "An advertisement for Boston baked beans"],
        "d": 2
    },
    {
        "q": "Why was Woody horrified by the Veg-a-Lax commercial after it aired on television?",
        "correct": "His lines were edited to make it sound like he personally suffered from chronic constipation",
        "wrong": ["His face was replaced by a cartoon illustration of a prune", "The company went bankrupt without paying him his acting fee", "The advertisement aired during his family's church service in Hanover"],
        "d": 2
    },

    # --- MELVILLE'S & GARY'S OLDE TOWNE TAVERN (81-100) ---
    {
        "q": "What is the name of the upscale seafood restaurant located directly above Cheers?",
        "correct": "Melville's Fine Sea Food",
        "wrong": ["Captain's Galley", "The Boston Chowder House", "Harbor View Grill"],
        "d": 1
    },
    {
        "q": "What is the name of the haughty, condescending owner of Melville's restaurant introduced in Season 9?",
        "correct": "John Allen Hill",
        "wrong": ["Sumner Sloane", "Derek Drake", "Sterling Hall"],
        "d": 1
    },
    {
        "q": "What financial dispute frequently erupts between John Allen Hill and Sam Malone regarding the building lease?",
        "correct": "Lease rights over the shared bathrooms and alleyway parking spots",
        "wrong": ["Shared heating oil and utility meter readings", "Fire escape maintenance fees", "The roof antenna installation fees"],
        "d": 2
    },
    {
        "q": "What romantic relationship involving John Allen Hill horrified Carla Tortelli in Season 10?",
        "correct": "John Allen Hill started dating Carla's mother Mama Lozupone",
        "wrong": ["Hill proposed marriage to Carla's daughter Serafina", "Hill had a brief passionate affair with Carla herself", "Hill secretly eloped with Carla's sister Annette"],
        "d": 2
    },
    {
        "q": "What is the name of Cheers' primary rival drinking establishment located across town in Boston?",
        "correct": "Gary's Olde Towne Tavern",
        "wrong": ["McGinty's Ale House", "The Boston Boathouse", "O'Malley's Irish Pub"],
        "d": 1
    },
    {
        "q": "What is the recurring series of multi-season prank wars between Cheers and Gary's Olde Towne Tavern called?",
        "correct": "Bar Wars",
        "wrong": ["The Tavern Feud", "Boston Pub Brawl", "The Keg Clash"],
        "d": 1
    },
    {
        "q": "In one of the most famous Bar Wars pranks, what animal did the Cheers gang place inside Gary's Olde Towne Tavern?",
        "correct": "A live sheep (or farm animal)",
        "wrong": ["A circus bear", "A swarm of pigeons", "A baby alligator"],
        "d": 1
    },
    {
        "q": "How did Gary retaliate against Cheers after the bar gang stole his prized bowling trophy?",
        "correct": "He had the entire Cheers interior completely stripped down to bare walls overnight",
        "wrong": ["He poured blue dye into the Cheers draft beer kegs", "He had the building condemned by fake city inspectors", "He sent a marching band to play in the bar at 3 AM"],
        "d": 2
    },
    {
        "q": "In 'Bar Wars V', what morbid prank does Gary appear to play on Cheers regarding his own life?",
        "correct": "Faking his own death and funeral to trick Cheers into public humiliation",
        "wrong": ["Faking a catastrophic fire at his own tavern", "Pretending he had lost his bar in a high-stakes poker game", "Staging a fake kidnapping by the Boston mob"],
        "d": 2
    },
    {
        "q": "What prank did the Cheers gang pull on Gary by posing as construction workers outside his tavern?",
        "correct": "Bricking up the front entrance of Gary's Olde Towne Tavern",
        "wrong": ["Digging a massive trench through his beer delivery chute", "Paving over his private parking lot with grass sod", "Painting his brick facade bright neon pink"],
        "d": 2
    },
    {
        "q": "What sporting event do Cheers and Gary's Olde Towne Tavern compete in during the Season 4 episode 'From Beer to Eternity'?",
        "correct": "A bowling tournament",
        "wrong": ["A softball championship", "A tug-of-war at Boston Common", "A championship dart tournament"],
        "d": 2
    },
    {
        "q": "In 'From Beer to Eternity', who turns out to be Cheers' secret weapon bowler despite her hatred of bowling?",
        "correct": "Diane Chambers",
        "wrong": ["Carla Tortelli", "Norm Peterson", "Cliff Clavin"],
        "d": 2
    },
    {
        "q": "In Season 10, how does John Allen Hill acquire legal ownership of the Cheers back room and pool room?",
        "correct": "He purchases the building property parcel that boundaries the back room",
        "wrong": ["He wins the back room in a game of craps with Sam", "He claims eminent domain through the Boston city council", "He discovers an 18th-century land grant in his name"],
        "d": 3
    },
    {
        "q": "What does Sam Malone do to John Allen Hill's expensive Mercedes sedan in retaliation for rent hikes?",
        "correct": "Carves up the parking lines or blocks it with trash bins",
        "wrong": ["Fills the sunroof with clam chowder", "Slashes all four tires with a bottle opener", "Has it towed to an impound lot in Providence"],
        "d": 3
    },
    {
        "q": "Which actor portrayed the pompous restaurant proprietor John Allen Hill across multiple seasons?",
        "correct": "Keene Curtis",
        "wrong": ["Max Wright", "Richard Venture", "George Gaynes"],
        "d": 3
    },
    {
        "q": "In the final installment of Bar Wars in Season 11, what does Harry the Hat reveal about the entire prank conflict?",
        "correct": "Harry orchestrated the war himself to con money out of both bars",
        "wrong": ["Gary had sold his tavern to a chain corporation two years earlier", "Gary was actually Sam's long-lost second cousin", "The Boston police department had been Gary's co-conspirators"],
        "d": 3
    },
    {
        "q": "What did the Cheers gang send to Gary disguised as a birthday present, which detonated in a cloud of glitter and flour?",
        "correct": "A booby-trapped fake champagne crate",
        "wrong": ["A spring-loaded cigar humidor", "A hollowed-out vintage jukebox", "A helium-inflated balloon bomb"],
        "d": 3
    },
    {
        "q": "In 'Bar Wars II', what did Gary steal from Cheers that served as the bar's beloved symbol of Boston pride?",
        "correct": "Sam's prized portrait or the bar's wooden Indian statue",
        "wrong": ["The authentic brass bar rail", "The brass bell behind the counter", "The neon beer sign in the front window"],
        "d": 2
    },
    {
        "q": "What was the name of the snooty French chef at Melville's who frequently complained about Cheers' grease fumes?",
        "correct": "Chef Henri",
        "wrong": ["Chef Pierre", "Chef Marcel", "Chef Jacques"],
        "d": 3
    },
    {
        "q": "What type of food did Melville's specialize in that caused seafood aromas to seep down into the Cheers barroom?",
        "correct": "Lobster, oysters, and fresh New England fish",
        "wrong": ["Spicy Creole seafood boils", "Fried calamari and oily sardines", "Steamed crabs and clam chowder exclusively"],
        "d": 2
    }
]

assert len(raw_questions) == 100, f"Expected 100, got {len(raw_questions)}"

d_counts = {1: 0, 2: 0, 3: 0}
for q in raw_questions:
    d_counts[q["d"]] += 1
print(f"DEBUG d_counts: {d_counts}")
assert d_counts[1] == 30, f"Expected 30 d1, got {d_counts[1]}"
assert d_counts[2] == 40, f"Expected 40 d2, got {d_counts[2]}"
assert d_counts[3] == 30, f"Expected 30 d3, got {d_counts[3]}"

formatted = assemble_batch(raw_questions, 1)
save_json(formatted, "tools/staging/cheers_batch1.json")
print("Saved tools/staging/cheers_batch1.json successfully!")
