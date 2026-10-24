#!/usr/bin/env python3
"""
Generate Batch 2: ABC 'TGIF' Golden Era (100 questions)
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from sitcom_builder import make_batch

q_batch2 = [
    # Full House (20 questions)
    {
        "q": "What morning talk show in San Francisco does Danny Tanner co-host alongside Rebecca Donaldson?",
        "correct": "Wake Up, San Francisco",
        "distractors": ["Good Morning Bay Area", "Rise and Shine SF", "Bay City Morning"],
        "d": 1
    },
    {
        "q": "What was the name of Uncle Jesse's rock band that played gigs around the Bay Area?",
        "correct": "Jesse and the Rippers",
        "distractors": ["The Katsopolis Kings", "Jesse & The Rockers", "The Sunset Strummers"],
        "d": 1
    },
    {
        "q": "What was Uncle Jesse's trademark exclamation whenever he saw an attractive woman or was overwhelmed by excitement?",
        "correct": "Have mercy!",
        "distractors": ["Mercy me!", "Oh baby!", "Lord have mercy!"],
        "d": 1
    },
    {
        "q": "What was the name of Joey Gladstone's beaver-like wooden puppet used in his stand-up comedy and kids' TV acts?",
        "correct": "Mr. Woodchuck",
        "distractors": ["Beaver Bob", "Woody Beaver", "Chucky Chipmunk"],
        "d": 1
    },
    {
        "q": "What physical hand gesture accompanied Joey Gladstone's signature catchphrase 'Cut it out'?",
        "correct": "Scissor fingers snipping across his chest, followed by pointing over his shoulder",
        "distractors": ["Slapping both knees and pointing forward", "Spinning a finger around his ear and winking", "Throwing two thumbs up and clicking his tongue"],
        "d": 1
    },
    {
        "q": "Which of the following was NOT one of Michelle Tanner's famous recurring catchphrases?",
        "correct": "Whoa, baby!",
        "distractors": ["You got it, dude!", "You're in big trouble, mister!", "No way, José!"],
        "d": 1
    },
    {
        "q": "What was Stephanie Tanner's signature indignation catchphrase whenever someone offended or interrupted her?",
        "correct": "How rude!",
        "distractors": ["That is bogus!", "Get real!", "Not cool!"],
        "d": 1
    },
    {
        "q": "What was the name of DJ Tanner's eccentric, foul-footed, obnoxious best friend who lived next door?",
        "correct": "Kimmy Gibbler",
        "distractors": ["Kathy Santoni", "Gia Mahan", "Viper"],
        "d": 1
    },
    {
        "q": "What was the name and breed of the Tanner family dog brought home in Season 3?",
        "correct": "Comet, a Golden Retriever",
        "distractors": ["Buddy, a Labrador Retriever", "Rover, a Sheepdog", "Sunny, a Cocker Spaniel"],
        "d": 1
    },
    {
        "q": "What were the names of Uncle Jesse and Aunt Becky's identical twin sons born in Season 5?",
        "correct": "Nicky and Alex",
        "distractors": ["Tommy and Bobby", "Luke and Jesse Jr.", "Joey and Danny"],
        "d": 1
    },
    {
        "q": "Which identical twin sisters famously alternated playing toddler Michelle Tanner across all eight seasons?",
        "correct": "Mary-Kate and Ashley Olsen",
        "distractors": ["Tia and Tamera Mowry", "Camilla and Rebecca Rosso", "Brittany and Cynthia Daniel"],
        "d": 1
    },
    {
        "q": "Who was originally cast and shot the unaired pilot of Full House as Danny Tanner before Bob Saget took over the role?",
        "correct": "John Posey",
        "distractors": ["Paul Reiser", "David Coulier", "Alan Thicke"],
        "d": 3
    },
    {
        "q": "At John Stamos' request after Season 1, Jesse's original surname 'Cochran' was changed to Katsopolis to reflect what heritage?",
        "correct": "Greek",
        "distractors": ["Italian", "Armenian", "Portuguese"],
        "d": 2
    },
    {
        "q": "DJ Tanner's high school boyfriend Steve Hale was voiced and portrayed by Scott Weinger, who famously voiced which Disney hero?",
        "correct": "Aladdin",
        "distractors": ["Hercules", "Tarzan", "Prince Eric"],
        "d": 1
    },
    {
        "q": "In Season 5, Uncle Jesse records a cover of The Beach Boys song 'Forever', which unexpectedly becomes a number-one hit in which country?",
        "correct": "Japan",
        "distractors": ["Germany", "Australia", "Brazil"],
        "d": 2
    },
    {
        "q": "What medical crisis affects Michelle Tanner in the two-part Full House series finale 'Michelle Rides Again'?",
        "correct": "A horseback riding accident causes temporary retrograde amnesia",
        "distractors": ["She swallows a coin and requires emergency throat surgery", "She contracts chickenpox during graduation day", "She breaks both legs falling out of the treehouse"],
        "d": 2
    },
    {
        "q": "Who composed and performed the Full House theme song 'Everywhere You Look'?",
        "correct": "Jesse Frederick",
        "distractors": ["Gary Portnoy", "Randy Newman", "Bill Bickford"],
        "d": 2
    },
    {
        "q": "What was the name of the San Francisco advertising agency where Danny Tanner's brother-in-law Jesse and friend Joey worked writing commercial jingles?",
        "correct": "Double J Creative Services",
        "distractors": ["Bay Jingle Masters", "Katsopolis & Gladstone Ads", "Golden Gate Jingles"],
        "d": 3
    },
    {
        "q": "What musical instrument did Stephanie Tanner briefly practice, driving the entire household crazy, before quitting in Season 2?",
        "correct": "Honeycomb drum set",
        "distractors": ["The clarinet", "The accordion", "The trombone"],
        "d": 3
    },
    {
        "q": "What street in San Francisco features the iconic Victorian row houses shown in the Full House opening picnic credits?",
        "correct": "Steiner Street at Alamo Square (The Painted Ladies)",
        "distractors": ["Lombard Street", "Haight Street", "Castro Street"],
        "d": 1
    },

    # Family Matters (20 questions)
    {
        "q": "What was the name of Steve Urkel's suave, debonair alter ego produced by his Transformation Chamber?",
        "correct": "Stefan Urquelle",
        "distractors": ["Pierre Urkel", "Sebastian Urquelle", "Julian Urkel"],
        "d": 1
    },
    {
        "q": "What is Steve Urkel's most ubiquitous catchphrase whenever he accidentally destroys property or knocks over furniture?",
        "correct": "Did I do that?",
        "distractors": ["Whoopsie daisy!", "That wasn't me!", "Look what happened!"],
        "d": 1
    },
    {
        "q": "What was Carl Winslow's rank and profession throughout Family Matters?",
        "correct": "Chicago Police Department officer, rising to Lieutenant",
        "distractors": ["Cook County Sheriff Detective", "Chicago Fire Department Captain", "Illinois State Police Inspector"],
        "d": 1
    },
    {
        "q": "Which Winslow family member was the unrequited romantic obsession of Steve Urkel throughout almost the entire series?",
        "correct": "Laura Winslow",
        "distractors": ["Rachel Crawford", "Judy Winslow", "Maxine Johnson"],
        "d": 1
    },
    {
        "q": "Actor Jaleel White was originally hired on Family Matters under what contractual terms?",
        "correct": "As a one-time guest star in Season 1 episode 'Laura's First Date'",
        "distractors": ["As a recurring bully for Eddie Winslow", "As an audition for a separate Saturday morning pilot", "As a permanent co-star from the series pilot"],
        "d": 2
    },
    {
        "q": "In addition to Steve Urkel and Stefan Urquelle, which flamboyant female cousin from Biloxi, Mississippi did Jaleel White also portray?",
        "correct": "Myrtle Urkel",
        "distractors": ["Bernice Urkel", "Latoya Urkel", "Bertha Urkel"],
        "d": 1
    },
    {
        "q": "What famously happened to Judy Winslow (played by Jaimee Foxworth) after Season 4 of Family Matters?",
        "correct": "She walked upstairs in a routine scene and was completely erased from the show without explanation",
        "distractors": ["She went to boarding school in Switzerland in a special episode", "She was recast with a younger actress who lasted two episodes", "She died in an off-screen accident during summer break"],
        "d": 2
    },
    {
        "q": "What was the name of the teen diner and hangout opened by Carl's sister-in-law Rachel Crawford in Season 2?",
        "correct": "Rachel's Place",
        "distractors": ["The Winslow Grill", "The Chicago Chill", "The Corner Booth"],
        "d": 2
    },
    {
        "q": "What was the full name of Eddie Winslow's lovable, extremely slow-witted best friend played by Orlando Brown?",
        "correct": "Waldo Geraldo Faldo",
        "distractors": ["Roland Bartholomew Faldo", "Ricardo Alberto Faldo", "Guillermo Antonio Faldo"],
        "d": 2
    },
    {
        "q": "What distinctive microcar did Steve Urkel drive around Chicago, featuring a single front door that opened outward?",
        "correct": "BMW Isetta",
        "distractors": ["Messerschmitt KR200", "Peel P50", "Subaru 360"],
        "d": 2
    },
    {
        "q": "Family Matters was a direct spin-off of which popular ABC sitcom where Harriette Winslow worked as an elevator operator?",
        "correct": "Perfect Strangers",
        "distractors": ["Full House", "Growing Pains", "Head of the Class"],
        "d": 1
    },
    {
        "q": "In 1997, after eight seasons on ABC's TGIF, which competing network bought the rights to broadcast Family Matters for Season 9?",
        "correct": "CBS",
        "distractors": ["NBC", "FOX", "The WB"],
        "d": 2
    },
    {
        "q": "Who portrayed Myra Monkhouse, the obsessive, possessive girl who passionately adored Steve Urkel and hated Laura Winslow?",
        "correct": "Michelle Thomas",
        "distractors": ["Cherie Johnson", "Countess Vaughn", "Kellie Shanygne Williams"],
        "d": 2
    },
    {
        "q": "Before starring as Officer Carl Winslow, Reginald VelJohnson played Sgt. Al Powell in which iconic 1988 action film?",
        "correct": "Die Hard",
        "distractors": ["Lethal Weapon", "RoboCop", "Beverly Hills Cop"],
        "d": 1
    },
    {
        "q": "What musical instrument was Steve Urkel shown to be a virtuoso at playing throughout the series?",
        "correct": "Accordion",
        "distractors": ["Saxophone", "Violin", "Bagpipes"],
        "d": 1
    },
    {
        "q": "What was the title of the energetic novelty dance song that Steve Urkel introduced in Season 2?",
        "correct": "The Urkel Dance ('Do the Urkel')",
        "distractors": ["The Suspenders Shake", "The Pocket Protector Hop", "The Chicago Urkel Strut"],
        "d": 1
    },
    {
        "q": "What was Carl Winslow's favorite food indulgence that Steve frequently ruined or that Carl hid around the house?",
        "correct": "Powdered sugar donuts",
        "distractors": ["Deep dish sausage pizza", "Chocolate fudge cupcakes", "Glazed crullers"],
        "d": 2
    },
    {
        "q": "What was the name of the elderly grandmother who lived with the Winslows and had a sassy, modern outlook on life?",
        "correct": "Estelle 'Mother' Winslow",
        "distractors": ["Edna Winslow", "Mildred Winslow", "Beatrice Winslow"],
        "d": 1
    },
    {
        "q": "In the Family Matters Season 9 finale, where do Steve Urkel and Carl Winslow get stranded after a NASA launch accident?",
        "correct": "Outer space orbiting Earth",
        "distractors": ["A deserted Pacific atoll", "The Russian Siberian tundra", "An underground missile silo"],
        "d": 3
    },
    {
        "q": "In a 1991 TGIF crossover event, Steve Urkel appeared on Full House to teach Michelle Tanner how to handle what life milestone?",
        "correct": "Wearing eyeglasses for the first time without being embarrassed",
        "distractors": ["Riding a bicycle without training wheels", "Dealing with a bully at preschool", "Learning how to tie her shoelaces"],
        "d": 2
    },

    # Step by Step (15 questions)
    {
        "q": "On Step by Step, what were the respective professions of Frank Lambert and Carol Foster when they impulsively married in Jamaica?",
        "correct": "Frank was a home construction contractor and Carol was a beauty salon owner",
        "distractors": ["Frank was an auto mechanic and Carol was a real estate broker", "Frank was an architect and Carol was a boutique clothing owner", "Frank was an electrician and Carol was a florist"],
        "d": 2
    },
    {
        "q": "Which two veteran 1970s TV superstars headlined the blended-family sitcom Step by Step?",
        "correct": "Patrick Duffy (Dallas) and Suzanne Somers (Three's Company)",
        "distractors": ["John Ritter and Joyce DeWitt", "Tom Selleck and Jaclyn Smith", "Ted Danson and Shelley Long"],
        "d": 1
    },
    {
        "q": "What was the name of Frank's dim-witted, surfer-dude nephew who lived in a customized van in the Lambert driveway?",
        "correct": "Cody Lambert",
        "distractors": ["JT Lambert", "Mark Foster", "Rich Halke"],
        "d": 1
    },
    {
        "q": "What was Cody Lambert's iconic catchphrase accompanied by a slow shake of his head?",
        "correct": "Whoa, dude!",
        "distractors": ["Totally tubular, man!", "Radical times!", "Far out, uncle Frank!"],
        "d": 1
    },
    {
        "q": "What Wisconsin town provided the setting for the Lambert-Foster household on Step by Step?",
        "correct": "Port Washington",
        "distractors": ["Green Bay", "Kenosha", "Sheboygan"],
        "d": 2
    },
    {
        "q": "Which of the Foster children was the outspoken, hyper-feminist intellectual who constantly clashed with J.T. Lambert?",
        "correct": "Dana Foster",
        "distractors": ["Karen Foster", "Al Lambert", "Lily Foster-Lambert"],
        "d": 1
    },
    {
        "q": "What amusement park roller coaster was shown in the opening theme sequence of Step by Step?",
        "correct": "Six Flags Great America in Gurnee, Illinois",
        "distractors": ["Cedar Point in Sandusky, Ohio", "Kings Island in Mason, Ohio", "Knott's Berry Farm in Buena Park, California"],
        "d": 2
    },
    {
        "q": "Why was Sasha Mitchell (Cody Lambert) abruptly written off Step by Step in Season 5?",
        "correct": "Personal domestic legal issues led producers to drop him from the cast",
        "distractors": ["He accepted a starring role in Kickboxer movie sequels", "He walked out during a contractual salary dispute", "He relocated to Europe to pursue competitive martial arts"],
        "d": 3
    },
    {
        "q": "What was the name of the baby girl born to Frank and Carol in Season 4 of Step by Step?",
        "correct": "Lily Foster-Lambert",
        "distractors": ["Chloe Foster-Lambert", "Emma Foster-Lambert", "Rose Foster-Lambert"],
        "d": 2
    },
    {
        "q": "What was J.T. Lambert's given first and middle name?",
        "correct": "John Thomas",
        "distractors": ["James Timothy", "Joseph Tyler", "Jason Troy"],
        "d": 2
    },
    {
        "q": "What sport does tomboy Alicia 'Al' Lambert initially excel at in early seasons of Step by Step?",
        "correct": "Little League Baseball",
        "distractors": ["Soccer", "Ice Hockey", "Gymnastics"],
        "d": 2
    },
    {
        "q": "Who portrayed J.T.'s dim-witted best friend Rich Halke, who later became Dana Foster's unlikely boyfriend?",
        "correct": "Jason Marsden",
        "distractors": ["Brandon Call", "Josh Byrne", "Danny Pintauro"],
        "d": 2
    },
    {
        "q": "Which member of the Lambert children mysteriously vanished from the series in Season 6 without an explanation?",
        "correct": "Brendan Lambert (Josh Byrne)",
        "distractors": ["Mark Foster (Christopher Castile)", "J.T. Lambert (Brandon Call)", "Al Lambert (Christine Lakin)"],
        "d": 3
    },
    {
        "q": "What was the title of the Step by Step theme song performed by Jesse Frederick and Teresa James?",
        "correct": "Second Time Around",
        "distractors": ["Step by Step We Grow", "Two Worlds Combined", "One Big Happy Family"],
        "d": 2
    },
    {
        "q": "What was the profession of Carol's vain, narcissistic daughter Karen Foster?",
        "correct": "Aspiring fashion model and country singer",
        "distractors": ["Aerobics instructor and cheerleader", "Cosmetologist and pageant coach", "TV weather forecaster"],
        "d": 2
    },

    # Boy Meets World (15 questions)
    {
        "q": "What was the full name of the eccentric middle-school teacher, high-school principal, and neighbor on Boy Meets World?",
        "correct": "George Hamilton Feeny",
        "distractors": ["Arthur Edward Feeny", "Thomas Richard Feeny", "Walter James Feeny"],
        "d": 2
    },
    {
        "q": "What theatrical nickname and melodramatic vocal call did Eric Matthews invent to summon Mr. Feeny across the yard?",
        "correct": "The Feeny Call ('Fee-fee-fee-feeny!')",
        "distractors": ["The Feeny Howl ('Feeny-weeny!')", "The Professor Yell ('Mister Fee-nay!')", "The Neighbor Shout ('Yo, Feeny!')"],
        "d": 1
    },
    {
        "q": "In the series finale 'Brave New World', what are Mr. Feeny's poignant final words to Cory, Topanga, Shawn, and Eric after they leave the classroom?",
        "correct": "I love you all. Class dismissed.",
        "distractors": ["Do good in this world. Class dismissed.", "Never stop learning. Class dismissed.", "You were my greatest students. Goodbye."],
        "d": 2
    },
    {
        "q": "What was the name of Shawn Hunter's cool, motorcycle-riding English teacher who took Shawn into his home as a foster guardian?",
        "correct": "Jonathan Turner",
        "distractors": ["Eli Williams", "Stuart Collins", "Alan Matthews"],
        "d": 2
    },
    {
        "q": "In later seasons, what hilarious hermit alter-ego does Eric Matthews adopt when envisioning his future life?",
        "correct": "Plays With Squirrels",
        "distractors": ["Speaks With Pigeons", "Hangs With Badgers", "Lives In Tree-Hollow"],
        "d": 2
    },
    {
        "q": "What city and high school provide the primary setting for Boy Meets World?",
        "correct": "Philadelphia, Pennsylvania (John Adams High School)",
        "distractors": ["Pittsburgh, Pennsylvania (George Washington High)", "Boston, Massachusetts (Benjamin Franklin High)", "Chicago, Illinois (Abraham Lincoln High)"],
        "d": 1
    },
    {
        "q": "What was Topanga Lawrence named after when she was introduced in Season 1 as a free-spirited, eccentric classmate?",
        "correct": "Topanga Canyon in California",
        "distractors": ["A Native American goddess of wisdom", "A wildflower native to the Allegheny mountains", "A bohemian music festival attended by her parents"],
        "d": 2
    },
    {
        "q": "What was the name of Shawn Hunter's biological older half-brother who re-enters his life at college?",
        "correct": "Jack Hunter",
        "distractors": ["Chet Hunter", "Eddie Hunter", "Virgil Hunter"],
        "d": 1
    },
    {
        "q": "Which actor, who played cool older brother Jack Hunter, was the real-life sibling of Joey and Andrew Lawrence?",
        "correct": "Matthew Lawrence",
        "distractors": ["Joey Lawrence", "Ben Savage", "Will Friedle"],
        "d": 1
    },
    {
        "q": "What was the profession of Cory and Eric's father Alan Matthews before he bought an outdoor wilderness store?",
        "correct": "Grocer / Supermarket manager",
        "distractors": ["Postal worker", "Plumbing contractor", "High school baseball coach"],
        "d": 2
    },
    {
        "q": "In Season 5, what ski lodge employee creates a major romantic wedge between Cory and Topanga after an all-night conversation?",
        "correct": "Lauren",
        "distractors": ["Wendy", "Trini", "Kelly"],
        "d": 2
    },
    {
        "q": "What is Cory Matthews' middle name?",
        "correct": "Israel",
        "distractors": ["David", "Isaac", "Michael"],
        "d": 3
    },
    {
        "q": "What cult-favorite Season 5 Halloween episode parody of Scream and horror films features a masked killer stalking the school?",
        "correct": "And Then There Was Shawn",
        "distractors": ["I Was a Teenage Feeny", "The Slasher of John Adams High", "Bloody Locker Horror"],
        "d": 2
    },
    {
        "q": "What actress played Cory and Eric's younger sister Morgan Matthews starting in Season 3 after the original actress left?",
        "correct": "Lindsay Ridgeway",
        "distractors": ["Lily Nicksay", "Danielle Fishel", "Maitland Ward"],
        "d": 3
    },
    {
        "q": "William Daniels, who played Mr. Feeny, was also the iconic 1980s voice of which famous sci-fi automobile?",
        "correct": "KITT in Knight Rider",
        "distractors": ["The General Lee in Dukes of Hazzard", "Herbie the Love Bug", "Bumblebee in Transformers"],
        "d": 2
    },

    # Hangin' with Mr. Cooper (10 questions)
    {
        "q": "On Hangin' with Mr. Cooper, what professional sport did Mark Cooper play before becoming a high school gym teacher and coach?",
        "correct": "NBA Basketball (briefly with the Golden State Warriors)",
        "distractors": ["NFL Football (with the Oakland Raiders)", "MLB Baseball (with the Oakland Athletics)", "European Professional Basketball (in Greece)"],
        "d": 1
    },
    {
        "q": "What California city served as the setting for Hangin' with Mr. Cooper?",
        "correct": "Oakland",
        "distractors": ["San Francisco", "San Jose", "Sacramento"],
        "d": 1
    },
    {
        "q": "Which future Disney Channel superstar joined the cast of Hangin' with Mr. Cooper in Season 2 as Mark's cute young cousin Nicole Lee?",
        "correct": "Raven-Symoné",
        "distractors": ["Keke Palmer", "Tia Mowry", "Kyla Pratt"],
        "d": 1
    },
    {
        "q": "Which actress played Mark's gorgeous roommate Vanessa Russell, whom he eventually fell in love with and proposed to?",
        "correct": "Holly Robinson Peete",
        "distractors": ["Dawnn Lewis", "Lela Rochon", "Garcelle Beauvais"],
        "d": 1
    },
    {
        "q": "What was Dawnn Lewis's character Robin Dumars' primary occupation during Season 1 of Hangin' with Mr. Cooper?",
        "correct": "Music teacher at Oakbridge High School",
        "distractors": ["Oakland city council aide", "Nurse at Highland Hospital", "Flight attendant for United Airlines"],
        "d": 2
    },
    {
        "q": "Which R&B vocal group performed the upbeat theme song for Season 1 of Hangin' with Mr. Cooper along with Dawnn Lewis and Mark Curry?",
        "correct": "En Vogue",
        "distractors": ["TLC", "SWV", "Jade"],
        "d": 2
    },
    {
        "q": "In the pilot episode, how does Mark Cooper afford the mortgage on his spacious Oakland rental home?",
        "correct": "By taking in two female roommates, Vanessa and Robin",
        "distractors": ["By renting out his garage to a recording studio", "By running an illegal sports betting pool from his kitchen", "By taking a second job delivering pizzas at night"],
        "d": 2
    },
    {
        "q": "What broadway legend and 'Gimme a Break!' star joined the cast in Season 4 as principal P.J. Moore?",
        "correct": "Nell Carter",
        "distractors": ["Sheryl Lee Ralph", "Telma Hopkins", "Patti LaBelle"],
        "d": 2
    },
    {
        "q": "What high school did Mark Cooper attend as a teenager and later return to as a physical education teacher and coach?",
        "correct": "Oakbridge High School",
        "distractors": ["Oakland Technical High", "Bay Area Prep", "East Bay Central High"],
        "d": 3
    },
    {
        "q": "What was Mark Cooper's eccentric elderly neighbor's name, played by character actor Ron Glass in guest appearances?",
        "correct": "Donnie Long",
        "distractors": ["Mr. Foster", "Mr. Toplyn", "Russell Tyler"],
        "d": 3
    },

    # Dinosaurs (10 questions)
    {
        "q": "What was the family surname of the prehistoric animatronic dinosaur family featured in Jim Henson Productions' sitcom Dinosaurs?",
        "correct": "Sinclair",
        "distractors": ["Flintstone", "Pangea", "Saurian"],
        "d": 1
    },
    {
        "q": "What was patriarch Earl Sinclair's blue-collar job at the Wesayso Development Corporation?",
        "correct": "Tree Pusher",
        "distractors": ["Rock Crusher", "Tar Pit Dredger", "Cave Blaster"],
        "d": 1
    },
    {
        "q": "What was the tyrannical, cigar-smoking boss of the Wesayso Corporation, B.P. Richfield's dinosaur species?",
        "correct": "Styracosaurus",
        "distractors": ["Tyrannosaurus Rex", "Triceratops", "Brachiosaurus"],
        "d": 2
    },
    {
        "q": "What violent object did Baby Sinclair constantly hit his father Earl with while yelling 'Not the mama!'?",
        "correct": "A frying pan",
        "distractors": ["A wooden club", "A stone hammer", "A heavy rolling pin"],
        "d": 1
    },
    {
        "q": "What was Baby Sinclair's smug second catchphrase directed at the audience whenever he got away with misbehavior?",
        "correct": "Gotta love me!",
        "distractors": ["I'm the cutest!", "Look at my cheeks!", "Bow before the baby!"],
        "d": 1
    },
    {
        "q": "Why is the 1994 series finale of Dinosaurs, titled 'Changing Nature', considered one of the darkest sitcom finales in TV history?",
        "correct": "Earl inadvertently causes an ecological nuclear winter, bringing about the impending extinction and death of the entire family",
        "distractors": ["A giant meteor strikes Pangea on live TV during dinner", "A volcanic eruption buries their suburban subdivision in lava", "The Wesayso Corporation bulldozes their home and forces them into a zoo"],
        "d": 2
    },
    {
        "q": "What dinosaur species was Earl Sinclair?",
        "correct": "Megalosaurus",
        "distractors": ["Allosaurus", "Carnotaurus", "Velociraptor"],
        "d": 2
    },
    {
        "q": "Who was Earl Sinclair's dim-witted best friend and co-worker at the Wesayso Corporation?",
        "correct": "Roy Hess, a Tyrannosaurus Rex",
        "distractors": ["Ralph Steg, a Stegosaurus", "Barney Vance, a Brontosaurus", "Gary Horn, a Triceratops"],
        "d": 2
    },
    {
        "q": "What was the name of Fran Sinclair's sarcastic, wheelchair-bound mother who took malicious joy in tormenting Earl?",
        "correct": "Ethyl Phillips",
        "distractors": ["Mildred Sinclair", "Gladys Richfield", "Agnes Saur"],
        "d": 2
    },
    {
        "q": "Who provided the iconic, high-pitched voice for Baby Sinclair throughout Dinosaurs?",
        "correct": "Kevin Clash (the original puppeteer and voice of Elmo)",
        "distractors": ["Frank Oz", "Jim Henson", "Carroll Spinney"],
        "d": 2
    },

    # Sabrina the Teenage Witch & Perfect Strangers (10 questions)
    {
        "q": "On Sabrina the Teenage Witch, what are the names of Sabrina Spellman's two eccentric 500-year-old witch aunts?",
        "correct": "Hilda and Zelda",
        "distractors": ["Agatha and Beatrice", "Clara and Tabitha", "Rowena and Helga"],
        "d": 1
    },
    {
        "q": "What was the crime that caused Salem Saberhagen to be sentenced to spend 100 years as an ordinary house cat?",
        "correct": "Attempting to take over the world with a mortal army",
        "distractors": ["Stealing the Sacred Witches' Council spellbook", "Turning the High Warlock into a toad", "Revealing magic secrets on mortal public access television"],
        "d": 2
    },
    {
        "q": "Who voiced Salem the cat on Sabrina the Teenage Witch and served as a producer/writer on the show?",
        "correct": "Nick Bakay",
        "distractors": ["Tom Kenny", "Billy West", "Rob Paulsen"],
        "d": 2
    },
    {
        "q": "What was the name of Sabrina Spellman's sweet, slightly clueless high school boyfriend throughout the early seasons?",
        "correct": "Harvey Kinkle",
        "distractors": ["Josh Blackhart", "Aaron Jacobs", "Miles Goodman"],
        "d": 1
    },
    {
        "q": "What fictional suburban Massachusetts town served as the primary setting for Sabrina the Teenage Witch?",
        "correct": "Westbridge",
        "distractors": ["Salem Falls", "Greendale", "Marblehead"],
        "d": 2
    },
    {
        "q": "What snobbish, wealthy high school cheerleader was Sabrina's main mortal rival in the first three seasons?",
        "correct": "Libby Chessler",
        "distractors": ["Morgan Cavanaugh", "Valerie Birkhead", "Roxie King"],
        "d": 2
    },
    {
        "q": "On Perfect Strangers, what fictional Greek-like Mediterranean island nation did shepherd Balki Bartokomous emigrate from?",
        "correct": "Mypos",
        "distractors": ["Olympos", "Santorini Minor", "Kefalonia"],
        "d": 1
    },
    {
        "q": "What jubilant, leaping folk dance did Balki and Larry Appleton perform whenever they had cause to celebrate?",
        "correct": "The Dance of Joy",
        "distractors": ["The Myposian Jig", "The Sheep Shearing Hop", "The Appleton Polka"],
        "d": 1
    },
    {
        "q": "What was Balki Bartokomous's most famous recurring catchphrase when Cousin Larry asked him an obvious question?",
        "correct": "Well, of course not, don't be ridiculous!",
        "distractors": ["Why you say such silly things!", "No way, cousin Larry!", "That is crazy talk in Mypos!"],
        "d": 1
    },
    {
        "q": "At what Chicago newspaper did Cousin Larry and Balki work in the basement mailroom and later as photojournalists?",
        "correct": "The Chicago Chronicle",
        "distractors": ["The Chicago Tribune", "The Chicago Sun-Times", "The Daily Chicagoan"],
        "d": 2
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "staging", "90s_sitcoms_batch2.json")
    make_batch(q_batch2, 2, out)
