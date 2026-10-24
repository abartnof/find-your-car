from utils import build_golden_girls_batch

RAW_QUESTIONS = [
    # 1
    {
        "q": "What dessert do the four women most frequently eat late at night in the kitchen while discussing their problems?",
        "correct": "Cheesecake",
        "wrong": ["Key lime pie", "Tiramisu", "Apple strudel"],
        "d": 1
    },
    # 2
    {
        "q": "What is the street address of Blanche Devereaux's Miami home where the women live?",
        "correct": "6151 Richmond Street",
        "wrong": ["742 Evergreen Terrace", "124 Conch Street", "4321 Palm Boulevard"],
        "d": 1
    },
    # 3
    {
        "q": "What iconic phrase does Sophia Petrillo habitually use to begin her nostalgic anecdotes?",
        "correct": "Picture it: Sicily...",
        "wrong": ["Listen closely, children...", "Back in the old country...", "Remember Brooklyn in the thirties..."],
        "d": 1
    },
    # 4
    {
        "q": "What is the name of the Minnesota hometown where Rose Nylund grew up?",
        "correct": "St. Olaf",
        "wrong": ["Lake Wobegon", "Duluth Falls", "Little Norway"],
        "d": 1
    },
    # 5
    {
        "q": "Dorothy Zbornak works primarily in which profession throughout the series?",
        "correct": "Substitute teacher",
        "wrong": ["Museum curator", "Travel agent", "Real estate broker"],
        "d": 1
    },
    # 6
    {
        "q": "What retirement home did Sophia live in before it burned down, forcing her to move in with Dorothy?",
        "correct": "Shady Pines",
        "wrong": ["Whispering Palms", "Sunny Acres", "Golden Meadows"],
        "d": 1
    },
    # 7
    {
        "q": "What warning does Dorothy frequently utter to her mother whenever Sophia misbehaves or insults someone?",
        "correct": "Shady Pines, Ma!",
        "wrong": ["Back to Brooklyn, Ma!", "Quiet down, Sophia!", "To your room, Ma!"],
        "d": 1
    },
    # 8
    {
        "q": "What accessory does Sophia Petrillo carry with her everywhere, even inside the house?",
        "correct": "A woven wicker purse",
        "wrong": ["A silver locket", "A leather satchel", "A beaded clutch"],
        "d": 1
    },
    # 9
    {
        "q": "What was the name of Dorothy's ex-husband who left her after 38 years of marriage?",
        "correct": "Stan Zbornak",
        "wrong": ["Artie Levine", "Murray Guttman", "Dennis Douglas"],
        "d": 1
    },
    # 10
    {
        "q": "What was the profession of Chrissy, the young woman Stan left Dorothy for?",
        "correct": "Flight attendant",
        "wrong": ["Tennis instructor", "Dental hygienist", "Cocktail waitress"],
        "d": 1
    },
    # 11
    {
        "q": "What pet name does Stan repeatedly and annoying call Dorothy whenever he visits?",
        "correct": "Babe",
        "wrong": ["Sweetheart", "Doll", "Honeybun"],
        "d": 1
    },
    # 12
    {
        "q": "What novelty invention does Stan create that runs on a common vegetable?",
        "correct": "A potato clock",
        "wrong": ["A carrot flashlight", "A turnip radio", "An onion battery"],
        "d": 1
    },
    # 13
    {
        "q": "What is Blanche Devereaux's middle name?",
        "correct": "Elizabeth",
        "wrong": ["Ann", "Marie", "Lee"],
        "d": 1
    },
    # 14
    {
        "q": "What distinctive wallpaper design covers Blanche's bedroom walls throughout the series?",
        "correct": "Tropical banana palm leaves",
        "wrong": ["Pink flamingos", "Southern magnolia blossoms", "Blue damask silk"],
        "d": 1
    },
    # 15
    {
        "q": "How did Rose's late husband, Charlie Nylund, pass away?",
        "correct": "He had a heart attack while making love to Rose",
        "wrong": ["In a tractor accident on their farm", "During a blizzard in St. Olaf", "From food poisoning at a lutefisk dinner"],
        "d": 1
    },
    # 16
    {
        "q": "How did Blanche's late husband, George Devereaux, die according to the series backstory?",
        "correct": "In a car accident",
        "wrong": ["From a plane crash", "Of a heart attack on a golf course", "During an overseas sailing trip"],
        "d": 1
    },
    # 17
    {
        "q": "What medical event caused Sophia to lose her filter and speak whatever unfiltered thought comes to mind?",
        "correct": "A stroke",
        "wrong": ["A concussion", "A mild heart attack", "A fainting spell at church"],
        "d": 1
    },
    # 18
    {
        "q": "Where did Blanche first place the notice advertising for roommates for her house?",
        "correct": "A bulletin board at a local supermarket",
        "wrong": ["The classifieds in the Miami Herald", "A community board at the library", "A flyer at the senior center"],
        "d": 1
    },
    # 19
    {
        "q": "What fish is central to dozens of Rose Nylund's St. Olaf stories, folk traditions, and recipes?",
        "correct": "Herring",
        "wrong": ["Cod", "Trout", "Haddock"],
        "d": 1
    },
    # 20
    {
        "q": "What is the name of Blanche's beloved father, whom she affectionately calls 'Big Daddy'?",
        "correct": "Curtis Hollingsworth",
        "wrong": ["Beauregard Devereaux", "Jackson Hollingsworth", "Calhoun Montgomery"],
        "d": 1
    },
    # 21
    {
        "q": "What was the name of the Georgia estate where Blanche grew up as a southern belle?",
        "correct": "Twin Oaks",
        "wrong": ["Tara", "Twelve Oaks", "Belle Rive"],
        "d": 1
    },
    # 22
    {
        "q": "What physical feature of Stan Zbornak was a frequent target of Dorothy and Sophia's jokes?",
        "correct": "His baldness and terrible toupees",
        "wrong": ["His fake glass eye", "His oversized mustache", "His elevator shoes"],
        "d": 1
    },
    # 23
    {
        "q": "What is Sophia Petrillo's maiden name?",
        "correct": "Spirelli",
        "wrong": ["Castorini", "Grisanti", "Barone"],
        "d": 3
    },
    # 24
    {
        "q": "What was the name of Sophia's late husband and Dorothy's father?",
        "correct": "Salvadore",
        "wrong": ["Giuseppe", "Vito", "Antonio"],
        "d": 1
    },
    # 25
    {
        "q": "Why did Dorothy marry Stan Zbornak when they were teenagers?",
        "correct": "Dorothy got pregnant after high school prom",
        "wrong": ["Stan won a bet with her father", "They eloped to escape Brooklyn", "To combine their families' bakery businesses"],
        "d": 1
    },
    # 26
    {
        "q": "What subject does Dorothy most frequently mention teaching as a substitute high school teacher?",
        "correct": "English and American History",
        "wrong": ["Chemistry and Biology", "French and Spanish", "Home Economics and Art"],
        "d": 1
    },
    # 27
    {
        "q": "What college professor becomes Rose's steady, long-term romantic partner in later seasons?",
        "correct": "Miles Webber",
        "wrong": ["Arnie Peterson", "Jonathan Newman", "Lucas Hollingsworth"],
        "d": 1
    },
    # 28
    {
        "q": "What surprise true identity does Miles Webber reveal after being tracked down by a mobster?",
        "correct": "Nicholas Carbone, who entered witness protection",
        "wrong": ["Arthur Miller, a retired CIA operative", "Vincent Falcone, an undercover FBI agent", "Charles Lindstrom, Rose's distant cousin"],
        "d": 1
    },
    # 29
    {
        "q": "What is the alias of the mob hitman from whom Miles Webber is hiding in the federal witness protection program?",
        "correct": "The Cheese Man",
        "wrong": ["The Butcher", "The Claw", "The Ice Pick"],
        "d": 2
    },
    # 30
    {
        "q": "What is the name of Dorothy's musician son who frequently needs money and couch space?",
        "correct": "Michael",
        "wrong": ["David", "Tommy", "Anthony"],
        "d": 2
    },
    # 31
    {
        "q": "What instrument does Dorothy's slacker son Michael play?",
        "correct": "Drums",
        "wrong": ["Saxophone", "Bass guitar", "Trumpet"],
        "d": 2
    },
    # 32
    {
        "q": "What is the name of Dorothy's daughter whose wedding takes place early in the series?",
        "correct": "Kate",
        "wrong": ["Rebecca", "Janet", "Maria"],
        "d": 2
    },
    # 33
    {
        "q": "What profession does Kate's fiancé Dennis practice when they marry in Season 1?",
        "correct": "Podiatrist",
        "wrong": ["Accountant", "Chiropractor", "Architect"],
        "d": 3
    },
    # 34
    {
        "q": "What was the name of Sophia's son who was a cross-dresser and lived in Newark?",
        "correct": "Phil",
        "wrong": ["Gino", "Dominic", "Frankie"],
        "d": 2
    },
    # 35
    {
        "q": "How does Sophia's unseen son Phil die in the emotional Season 6 episode 'Ebbtide's Revenge'?",
        "correct": "A sudden heart attack",
        "wrong": ["A stroke", "A car accident", "Pneumonia"],
        "d": 3
    },
    # 36
    {
        "q": "What was Phil Petrillo's wife's name who clashed with Sophia at his funeral?",
        "correct": "Angela",
        "wrong": ["Carmela", "Lucia", "Theresa"],
        "d": 3
    },
    # 37
    {
        "q": "What was the name of Sophia's sister who moved from Sicily and frequently bickered with her?",
        "correct": "Angela",
        "wrong": ["Concetta", "Rosalia", "Gina"],
        "d": 2
    },
    # 38
    {
        "q": "What was the name of Sophia's brother who was a Catholic priest before leaving the priesthood?",
        "correct": "Angelo",
        "wrong": ["Giovanni", "Marco", "Pietro"],
        "d": 2
    },
    # 39
    {
        "q": "What Scandinavian exclamation does Rose frequently utter when startled, exasperated, or amazed?",
        "correct": "Uff-da!",
        "wrong": ["Mamma mia!", "Holy yutz!", "Gee whiz!"],
        "d": 1
    },
    # 40
    {
        "q": "What job did Rose hold in the early seasons before working at a local television station?",
        "correct": "Grief counselor at a counseling center",
        "wrong": ["Dental assistant", "Elementary school nurse", "Public library clerk"],
        "d": 2
    },
    # 41
    {
        "q": "What is the name of the eccentric TV consumer reporter Rose works for at the Miami news station?",
        "correct": "Enrique Mas",
        "wrong": ["Hector Alvarez", "Ricardo Gomez", "Carlos Ramos"],
        "d": 3
    },
    # 42
    {
        "q": "What is the name of Blanche's daughter who arrives in Miami visibly overweight, shocking Blanche?",
        "correct": "Rebecca",
        "wrong": ["Janet", "Virginia", "Charmaine"],
        "d": 2
    },
    # 43
    {
        "q": "What is the name of Rebecca's baby daughter born via artificial insemination?",
        "correct": "Aurora",
        "wrong": ["Scarlett", "Savannah", "Belle"],
        "d": 2
    },
    # 44
    {
        "q": "What is the name of Blanche's gay brother who visits Miami to come out to her?",
        "correct": "Clayton",
        "wrong": ["Tad", "Buford", "Sterling"],
        "d": 2
    },
    # 45
    {
        "q": "What is the name of Clayton's fiancé whom he plans to marry in Season 6?",
        "correct": "Doug",
        "wrong": ["Gary", "Brian", "Keith"],
        "d": 3
    },
    # 46
    {
        "q": "What is the name of Blanche's sister who comes to Miami needing a kidney transplant?",
        "correct": "Virginia",
        "wrong": ["Charmaine", "Magnolia", "Emmaline"],
        "d": 3
    },
    # 47
    {
        "q": "What is the name of Blanche's rivalrous sister who writes an erotic romance novel based on Blanche's life?",
        "correct": "Charmaine",
        "wrong": ["Virginia", "Lucinda", "Clementine"],
        "d": 3
    },
    # 48
    {
        "q": "What is the title of the steamy romance novel Charmaine publishes about Blanche's love life?",
        "correct": "Vixen: Story of a Woman",
        "wrong": ["Southern Heat", "Georgia Nights", "The Scent of Magnolias"],
        "d": 3
    },
    # 49
    {
        "q": "In St. Olaf folklore, what legendary leader was known as 'Olaf the Berserk'?",
        "correct": "A Viking chieftain with a terrible sense of direction",
        "wrong": ["A baker who invented the square pretzel", "A blacksmith who fought with giant spoons", "A farmer who married a snow yeti"],
        "d": 3
    },
    # 50
    {
        "q": "What St. Olaf competition involves tossing a heavy fish across a field for distance and accuracy?",
        "correct": "The Great Herring Toss",
        "wrong": ["The Flounder Fling", "The Salmon Slam", "The Cod Catapult"],
        "d": 2
    },
    # 51
    {
        "q": "What animal does Rose claim could tell fortunes in St. Olaf?",
        "correct": "A pig named Elmer",
        "wrong": ["A rooster named Thor", "A cow named Greta", "A goat named Sven"],
        "d": 3
    },
    # 52
    {
        "q": "What was the name of Rose's beloved childhood teddy bear that was held hostage by a Girl Scout?",
        "correct": "Fernando",
        "wrong": ["Barnaby", "Olaf", "Teddy Ruxpin"],
        "d": 2
    },
    # 53
    {
        "q": "What is the name of the ruthless Sunshine Cadet scout who refuses to return Rose's teddy bear Fernando?",
        "correct": "Daisy",
        "wrong": ["Amber", "Chloe", "Megan"],
        "d": 3
    },
    # 54
    {
        "q": "How does Dorothy get Rose's teddy bear back from Daisy the Sunshine Cadet?",
        "correct": "She snatches it out of Daisy's hands and kicks her out of the house",
        "wrong": ["She pays the 50-dollar ransom demand", "She calls Daisy's mother and troop leader", "She trades it for an autographed encyclopedia"],
        "d": 2
    },
    # 55
    {
        "q": "What Miami museum does Blanche work at as an assistant or administrator during the show?",
        "correct": "The Miami Museum of Art",
        "wrong": ["The Florida Natural History Museum", "The Coral Gables Cultural Center", "The Biscayne Historical Society"],
        "d": 2
    },
    # 56
    {
        "q": "What was the name of Sophia's elderly fiancé who married her in a Season 4 two-part premiere?",
        "correct": "Max Weinstock",
        "wrong": ["Murray Guttman", "Rocco", "Alvin"],
        "d": 2
    },
    # 57
    {
        "q": "What joint business venture did Sophia and her new husband Max open on the boardwalk?",
        "correct": "A pizza knish stand",
        "wrong": ["A gelato cart", "A pastrami and cannoli trailer", "An espresso kiosk"],
        "d": 2
    },
    # 58
    {
        "q": "What business did Dorothy's father Sal and Max Weinstock originally run together decades earlier?",
        "correct": "A novelty and catering company that burned down",
        "wrong": ["A dry-cleaning service in Queens", "A bowling alley in Brooklyn", "A tailor shop in Little Italy"],
        "d": 3
    },
    # 59
    {
        "q": "What was the name of the dog Rose briefly adopted that belonged to a deceased neighbor?",
        "correct": "Pepe",
        "wrong": ["Rusty", "Buster", "Bruno"],
        "d": 3
    },
    # 60
    {
        "q": "What musical production do the four women stage in order to save a local park or community center?",
        "correct": "The Henny Penny musical",
        "wrong": ["South Pacific revue", "The Wizard of Oz", "Fiddler on the Roof"],
        "d": 2
    },
    # 61
    {
        "q": "Which character dresses up as Henny Penny in the school play?",
        "correct": "Dorothy",
        "wrong": ["Rose", "Blanche", "Sophia"],
        "d": 2
    },
    # 62
    {
        "q": "Which bird does Rose portray in the Henny Penny play?",
        "correct": "Goosey Loosey",
        "wrong": ["Foxy Loxy", "Turkey Lurkey", "Ducky Lucky"],
        "d": 3
    },
    # 63
    {
        "q": "Which bird does Blanche portray in the Henny Penny musical?",
        "correct": "Foxy Loxy",
        "wrong": ["Goosey Loosey", "Chicken Little", "Turkey Lurkey"],
        "d": 3
    },
    # 64
    {
        "q": "What color hair does Dorothy's sister Gloria have, who arrives in town with financial problems?",
        "correct": "Blonde",
        "wrong": ["Red", "Jet black", "Brunette"],
        "d": 3
    },
    # 65
    {
        "q": "What shocking romantic betrayal does Gloria commit against Dorothy in Season 7?",
        "correct": "She sleeps with Dorothy's ex-husband Stan",
        "wrong": ["She steals Dorothy's fiancé Lucas", "She sells Dorothy's wedding ring", "She dates Dorothy's high school sweetheart"],
        "d": 2
    },
    # 66
    {
        "q": "What is the name of the hotel where the girls are mistaken for prostitutes while waiting to attend a Burt Reynolds taping?",
        "correct": "The Falcon Nest Hotel",
        "wrong": ["The Biltmore Miami", "The Fontainebleau", "The Biscayne Bay Towers"],
        "d": 3
    },
    # 67
    {
        "q": "What famous actor tells the girls 'Which one's the slut?' after Sophia meets him at the hotel?",
        "correct": "Burt Reynolds",
        "wrong": ["Tom Selleck", "Clint Eastwood", "Robert Redford"],
        "d": 1
    },
    # 68
    {
        "q": "What game show do Dorothy, Blanche, and Rose appear on together where they win absolutely nothing?",
        "correct": "Grab That Dough",
        "wrong": ["Jeopardy!", "Wheel of Fortune", "The Price is Right"],
        "d": 2
    },
    # 69
    {
        "q": "What contestant teammate do the girls get stuck with on 'Grab That Dough' who ruins their chances?",
        "correct": "An eccentric elderly man named Guy",
        "wrong": ["A competitive teenager named Kevin", "A sleepy tourist named Harold", "A nervous cab driver named Sal"],
        "d": 3
    },
    # 70
    {
        "q": "What prize do the women choose at the end of 'Grab That Dough' instead of taking the cash?",
        "correct": "The mystery envelope containing a skillet",
        "wrong": ["A lifetime supply of soup", "A set of patio luggage", "A trip to Milwaukee"],
        "d": 3
    },
    # 71
    {
        "q": "What illness does Dorothy struggle to get diagnosed in the acclaimed two-part episode 'Sick and Tired'?",
        "correct": "Chronic Fatigue Syndrome",
        "wrong": ["Fibromyalgia", "Lyme disease", "Mononucleosis"],
        "d": 2
    },
    # 72
    {
        "q": "What doctor finally takes Dorothy seriously and validates her Chronic Fatigue Syndrome diagnosis?",
        "correct": "Dr. Chang",
        "wrong": ["Dr. Newman", "Dr. Harris", "Dr. McDermott"],
        "d": 3
    },
    # 73
    {
        "q": "What dismissive medical practitioner does Dorothy confront at a restaurant after getting properly diagnosed?",
        "correct": "Dr. Budd",
        "wrong": ["Dr. Stevens", "Dr. Miller", "Dr. Warren"],
        "d": 3
    },
    # 74
    {
        "q": "What contest does Rose enter where she is mistakenly named St. Olaf's 'Woman of the Year'?",
        "correct": "St. Olaf Woman of the Year",
        "wrong": ["Butter Queen of Minnesota", "Lutefisk Princess of Crow Wing County", "Miss Dairy Days"],
        "d": 2
    },
    # 75
    {
        "q": "What St. Olaf award did Rose actually win when she was a young girl?",
        "correct": "Little Miss St. Olaf runner-up",
        "wrong": ["Best Milker at 4-H", "Fastest Herring Scaler", "Junior Yodeler"],
        "d": 3
    },
    # 76
    {
        "q": "What is the name of Blanche's childhood nanny who comes to visit her in Miami?",
        "correct": "Viola Watkins",
        "wrong": ["Mammy Lou", "Delilah Jackson", "Bernice Washington"],
        "d": 3
    },
    # 77
    {
        "q": "What shocking truth about Big Daddy does Viola Watkins reveal to Blanche?",
        "correct": "Big Daddy had a long-term secret affair with Viola",
        "wrong": ["Big Daddy was deeply in debt and lost Twin Oaks", "Big Daddy wasn't Blanche's biological father", "Big Daddy was secretly married to another woman"],
        "d": 3
    },
    # 78
    {
        "q": "What was the name of the wealthy older gentleman Blanche dated who turned out to have a secret heart condition?",
        "correct": "Harry",
        "wrong": ["Arthur", "Richard", "Edward"],
        "d": 3
    },
    # 79
    {
        "q": "What is the name of Sophia's friend who decides to end her own life due to terminal illness, sparking an ethical debate?",
        "correct": "Martha",
        "wrong": ["Clara", "Evelyn", "Gladys"],
        "d": 3
    },
    # 80
    {
        "q": "What dance contest do Blanche and Rose enter together where Blanche becomes obsessively competitive?",
        "correct": "A charity dance marathon",
        "wrong": ["A salsa competition", "A ballroom tango tournament", "A tap dancing showcase"],
        "d": 2
    },
    # 81
    {
        "q": "What St. Olaf holiday celebrates a legendary hero who drove all the flies out of town?",
        "correct": "St. Sigmund's Day",
        "wrong": ["St. Olaf Founder's Day", "The Feast of King Sven", "Herring Jubilee"],
        "d": 3
    },
    # 82
    {
        "q": "What was the name of Rose's biological father, whom she meets in Season 4?",
        "correct": "Brother Martin, a monk",
        "wrong": ["Sven Lindstrom, a dairy farmer", "Lars Peterson, a sailor", "Olaf Gunder, a carpenter"],
        "d": 3
    },
    # 83
    {
        "q": "What famous television personality does Rose convince herself is her biological father in 'You Gotta Have Hope'?",
        "correct": "Bob Hope",
        "wrong": ["Johnny Carson", "Milton Berle", "George Burns"],
        "d": 2
    },
    # 84
    {
        "q": "What was the name of the gay cook who appeared in the pilot episode but was subsequently dropped from the series?",
        "correct": "Coco",
        "wrong": ["Enzo", "Mateo", "Julio"],
        "d": 2
    },
    # 85
    {
        "q": "Why was the character of Coco the cook dropped after the pilot episode?",
        "correct": "Sophia was promoted to a main character and took over the cooking role",
        "wrong": ["The actor was cast in another series", "Test audiences complained about the kitchen size", "The network banned male roommate characters"],
        "d": 2
    },
    # 86
    {
        "q": "What Italian dish does Sophia claim can cure practically any ailment or broken heart?",
        "correct": "Her homemade marinara sauce with meatballs",
        "wrong": ["Spaghetti carbonara", "Baked ziti with ricotta", "Veal marsala"],
        "d": 2
    },
    # 87
    {
        "q": "In the pilot episode, Blanche plans to marry an affluent suitor named Harry, but what crime is he arrested for?",
        "correct": "Bigamy",
        "wrong": ["Embezzlement", "Art forgery", "Jewel theft"],
        "d": 2
    },
    # 88
    {
        "q": "What is the name of the high school where Dorothy frequently substitute-teaches and encounters troubled students?",
        "correct": "Southside High",
        "wrong": ["Biscayne Bay High", "Miami Central High", "Sunshine State Academy"],
        "d": 3
    },
    # 89
    {
        "q": "What musical instrument does Dorothy play whenever she wants to express deep melancholy or irritation?",
        "correct": "Piano",
        "wrong": ["Accordion", "Violin", "Flute"],
        "d": 2
    },
    # 90
    {
        "q": "What musical instrument does Rose play, including leading a band of local seniors?",
        "correct": "The tuba",
        "wrong": ["The clarinet", "The banjo", "The tambourine"],
        "d": 3
    },
    # 91
    {
        "q": "What was the name of the high school student Dorothy helps to stay in school despite him wanting to drop out to play baseball?",
        "correct": "Mario Lopez played him as Michael Gonzalez",
        "wrong": ["Tony Rodriguez", "Carlos Mendoza", "Ramon Sanchez"],
        "d": 3
    },
    # 92
    {
        "q": "What future teen star played Dorothy's undocumented student Mario Sanchez in Season 2?",
        "correct": "Mario Lopez",
        "wrong": ["Mark-Paul Gosselaar", "Ricky Martin", "Wilmer Valderrama"],
        "d": 2
    },
    # 93
    {
        "q": "What happens to the house roof in Season 3, forcing the girls to raise thousands of dollars?",
        "correct": "It collapses and needs total replacement",
        "wrong": ["It is destroyed by a hurricane", "Termites eat through the rafters", "A fallen palm tree crushes it"],
        "d": 2
    },
    # 94
    {
        "q": "What fundraiser performance do the girls put on to pay for their leaky roof?",
        "correct": "A vaudeville talent show",
        "wrong": ["A fashion show at the mall", "A bake sale and car wash", "A telethon on local cable"],
        "d": 2
    },
    # 95
    {
        "q": "What song do Blanche, Dorothy, and Rose perform in top hats and tails during their talent show act?",
        "correct": "Miami, You've Got Style",
        "wrong": ["Give My Regards to Broadway", "New York, New York", "There's No Business Like Show Business"],
        "d": 3
    },
    # 96
    {
        "q": "What is the name of Blanche's grandson who visits and exhibits rebellious, spoiled behavior?",
        "correct": "David",
        "wrong": ["Travis", "Hunter", "Cody"],
        "d": 3
    },
    # 97
    {
        "q": "Which daughter of Blanche is David's mother?",
        "correct": "Janet",
        "wrong": ["Rebecca", "Charmaine", "Virginia"],
        "d": 3
    },
    # 98
    {
        "q": "What St. Olaf dish does Rose make that smells so putrid the other women refuse to let it in the kitchen?",
        "correct": "Lefse with fermented herring and goat cheese",
        "wrong": ["Boiled rutabaga pudding", "Pickled pig snouts", "Smoked cod gelatin"],
        "d": 3
    },
    # 99
    {
        "q": "What kind of car did Stan drive that Dorothy frequently ridiculed?",
        "correct": "A cheap imported convertible that constantly broke down",
        "wrong": ["A rusty station wagon with wood paneling", "An oversized Cadillac with broken AC", "A yellow compact hatchback"],
        "d": 3
    },
    # 100
    {
        "q": "What is the outdoor patio called where the Golden Girls frequently have breakfast and morning coffee?",
        "correct": "The lanai",
        "wrong": ["The veranda", "The sunroom", "The courtyard"],
        "d": 1
    }
]

if __name__ == "__main__":
    build_golden_girls_batch(RAW_QUESTIONS, 1, "tools/staging/golden_girls_batch1.json")
