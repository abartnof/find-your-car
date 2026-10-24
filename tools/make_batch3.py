#!/usr/bin/env python3
"""
Generate Batch 3: Blue-Collar & Family Classics (100 questions)
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from sitcom_builder import make_batch

q_batch3 = [
    # Roseanne (20 questions)
    {
        "q": "What fictional blue-collar Illinois town served as the primary setting for the Conner family in Roseanne?",
        "correct": "Lanford",
        "distractors": ["Springfield", "Peoria", "Elgin"],
        "d": 1
    },
    {
        "q": "What was the specialty menu item at The Lanford Lunch Box, the diner opened by Roseanne, Jackie, Nancy, and Bev?",
        "correct": "Loose-meat sandwiches",
        "distractors": ["Deep dish chili dogs", "Corned beef reubens", "Fried catfish baskets"],
        "d": 1
    },
    {
        "q": "Which actress originally played older daughter Becky Conner before leaving for college and being replaced by Sarah Chalke?",
        "correct": "Lecy Goranson",
        "distractors": ["Sara Gilbert", "Natalie Portman", "Alicia Silverstone"],
        "d": 1
    },
    {
        "q": "What shocking plot twist is revealed in the final moments of the Season 9 series finale of Roseanne?",
        "correct": "Dan actually died from his heart attack a year earlier, and the lottery win was Roseanne's fictional coping mechanism",
        "distractors": ["The entire series was a manuscript written by Darlene for her high school creative writing class", "Roseanne was committed to a psychiatric hospital after Wellman Plastics closed", "Dan had left the family to start a new life in California with another woman"],
        "d": 2
    },
    {
        "q": "How many Primetime Emmy Awards for Outstanding Supporting Actress in a Comedy Series did Laurie Metcalf win as Jackie Harris?",
        "correct": "Three",
        "distractors": ["One", "Two", "Four"],
        "d": 2
    },
    {
        "q": "What was the name of Darlene Conner's artistic, soft-spoken boyfriend turned husband played by Johnny Galecki?",
        "correct": "David Healy",
        "distractors": ["Mark Healy", "Kevin Healy", "Jimmy Healy"],
        "d": 1
    },
    {
        "q": "Which future Hollywood megastar played Roseanne's suave factory supervisor Booker Brooks at Wellman Plastics in Season 1?",
        "correct": "George Clooney",
        "distractors": ["Brad Pitt", "Kevin Bacon", "Bruce Willis"],
        "d": 1
    },
    {
        "q": "What notorious real-life incident in July 1990 brought intense national media backlash upon Roseanne Barr?",
        "correct": "Her screeching rendition of the Star-Spangled Banner and crotch grab at a San Diego Padres baseball game",
        "distractors": ["Her profanity-laced acceptance speech at the People's Choice Awards", "Her arrest for protesting outside the network upfronts in New York", "Her walkout during an interview with Barbara Walters on 20/20"],
        "d": 2
    },
    {
        "q": "What iconic household object with a multicolored granny square crochet blanket sat in the center of the Conner living room?",
        "correct": "The battered floral print sofa",
        "distractors": ["The faux-leather recliner", "The maple rocking chair", "The plaid love seat"],
        "d": 1
    },
    {
        "q": "Why was original Roseanne creator and showrunner Matt Williams fired after just 13 episodes of Season 1?",
        "correct": "A bitter power struggle erupted when Roseanne felt he refused to credit her comedic voice and vision",
        "distractors": ["ABC executives were unhappy with the show's low initial Nielsen ratings", "He was hired away by NBC to produce The Fresh Prince of Bel-Air", "Budget overruns on set caused major friction with the network"],
        "d": 3
    },
    {
        "q": "Which celebrated television creator worked as a staff writer on Roseanne before creating Gilmore Girls?",
        "correct": "Amy Sherman-Palladino",
        "distractors": ["Mindy Kaling", "Marta Kauffman", "Jenji Kohan"],
        "d": 2
    },
    {
        "q": "What holiday became the centerpiece of an elaborate annual tradition on Roseanne, renowned for terrifying practical jokes?",
        "correct": "Halloween",
        "distractors": ["Thanksgiving", "Christmas", "April Fools' Day"],
        "d": 1
    },
    {
        "q": "What was the name of Roseanne and Dan's fourth child, born in Season 8 and named after a legendary Grateful Dead musician?",
        "correct": "Jerry Garcia Conner",
        "distractors": ["Bob Weir Conner", "Phil Lesh Conner", "Mickey Hart Conner"],
        "d": 2
    },
    {
        "q": "Who portrayed Becky's rebellious, motorcycle-riding bad-boy boyfriend turned husband Mark Healy?",
        "correct": "Glenn Quinn",
        "distractors": ["Stephen Dorff", "Brian Austin Green", "Skeet Ulrich"],
        "d": 2
    },
    {
        "q": "What motorcycle shop did Dan Conner open with his buddies that eventually went out of business, devastating the family finances?",
        "correct": "Lanford Custom Cycle",
        "distractors": ["Conner Choppers", "Prairie State Motors", "Route 66 Bikes"],
        "d": 2
    },
    {
        "q": "What was the name of Roseanne and Jackie's manipulative, hyper-critical mother played by Estelle Parsons?",
        "correct": "Beverly Harris",
        "distractors": ["Audrey Harris", "Evelyn Harris", "Gladys Harris"],
        "d": 2
    },
    {
        "q": "What medical crisis did Dan Conner suffer at Darlene and David's wedding near the end of Season 8?",
        "correct": "A severe heart attack",
        "distractors": ["A ruptured appendix", "A stroke", "A diabetic coma"],
        "d": 1
    },
    {
        "q": "Who was Roseanne's flamboyant business partner and friend who came out as a lesbian in Season 5, played by Sandra Bernhard?",
        "correct": "Nancy Bartlett",
        "distractors": ["Leon Carp", "Arnie Thomas", "Anne-Marie McCoy"],
        "d": 2
    },
    {
        "q": "What job did Jackie Harris hold in early seasons before becoming a Lanford police officer and later a truck driver?",
        "correct": "Assembly line worker at Wellman Plastics",
        "distractors": ["Waitress at Lobo Lounge", "Beautician at Lanford Hair", "Cashier at the Buy & Bag"],
        "d": 2
    },
    {
        "q": "What prestigious broadcasting award did Roseanne win in 1992 for its unrelenting realism regarding working-class struggles?",
        "correct": "The Peabody Award",
        "distractors": ["The Pulitzer Citation", "The DuPont-Columbia Silver Baton", "The George Polk Award"],
        "d": 3
    },

    # Home Improvement (20 questions)
    {
        "q": "What was the name of the local cable home improvement show hosted by Tim 'The Tool Man' Taylor?",
        "correct": "Tool Time",
        "distractors": ["Hammer Time", "Power Tool Hour", "The Handyman Workshop"],
        "d": 1
    },
    {
        "q": "What fictional hardware and power tool manufacturer sponsored Tool Time throughout the series?",
        "correct": "Binford Tools",
        "distractors": ["Apex Hardware", "Titan Power Supplies", "Detroit Toolworks"],
        "d": 1
    },
    {
        "q": "What was Tim Taylor's guttural catchphrase whenever he added excessive horsepower or modified equipment?",
        "correct": "More Power! (accompanied by chimpanzee-like grunts: Arrgh, arrgh, arrgh!)",
        "distractors": ["Rev it up! (with car engine roars)", "Bigger is better! (with double fist pumps)", "Power to the max! (with loud stomps)"],
        "d": 1
    },
    {
        "q": "What was Al Borland's signature deadpan catchphrase whenever Tim proposed a hazardous or nonsensical idea?",
        "correct": "I don't think so, Tim",
        "distractors": ["That's not code, Tim", "Hold on a minute, Tim", "Please step back, Tim"],
        "d": 1
    },
    {
        "q": "What unusual visual convention was always maintained with the Taylors' wise next-door neighbor Wilson W. Wilson Jr.?",
        "correct": "The lower half of his face was always obscured by the privacy fence or random household objects",
        "distractors": ["He was only ever heard speaking through an old intercom system", "He only appeared in shadow silhouettes through his window blinds", "He wore a welding mask in every single scene"],
        "d": 1
    },
    {
        "q": "Who portrayed Tim's flannel-shirted, ever-patient Tool Time assistant Al Borland?",
        "correct": "Richard Karn",
        "distractors": ["Earl Hindman", "Stephen Tobolowsky", "Zachery Ty Bryan"],
        "d": 1
    },
    {
        "q": "Which teen heartthrob actor played middle brother Randy Taylor, renowned for his sharp wit and sarcastic barbs?",
        "correct": "Jonathan Taylor Thomas",
        "distractors": ["Rider Strong", "Devon Sawa", "Jared Leto"],
        "d": 1
    },
    {
        "q": "Which future Baywatch superstar originally played the Tool Time girl Lisa in the first two seasons before Debbe Dunning took over as Heidi?",
        "correct": "Pamela Anderson",
        "distractors": ["Carmen Electra", "Jenny McCarthy", "Yasmine Bleeth"],
        "d": 1
    },
    {
        "q": "What Michigan metropolitan area served as the setting for the Taylor family on Home Improvement?",
        "correct": "Suburban Detroit",
        "distractors": ["Grand Rapids", "Ann Arbor", "Lansing"],
        "d": 1
    },
    {
        "q": "What rare entertainment triple crown did Tim Allen achieve during a single week in November 1994?",
        "correct": "He starred in the #1 TV show (Home Improvement), the #1 box office film (The Santa Clause), and authored the #1 NYT bestseller (Don't Stand Too Close to a Naked Man)",
        "distractors": ["He won an Oscar, an Emmy, and a Grammy within 48 hours", "He hosted the Oscars, the Emmys, and Saturday Night Live in the same month", "He had the top-rated sitcom, top-selling comedy album, and headlined Caesars Palace"],
        "d": 2
    },
    {
        "q": "Why did Jonathan Taylor Thomas leave Home Improvement during Season 8 before the series concluded?",
        "correct": "To step away from acting and concentrate on his academic studies and college preparation",
        "distractors": ["He was cast as the lead in a major Harry Potter film adaptation", "Contract disputes over salary parity with Tim Allen", "Severe health complications stemming from childhood diabetes"],
        "d": 2
    },
    {
        "q": "What field of study does Jill Taylor pursue when she decides to return to college in the later seasons?",
        "correct": "Psychology",
        "distractors": ["Architecture", "Social Work", "Art History"],
        "d": 2
    },
    {
        "q": "What vintage hot rod did Tim Taylor lovingly build from bare parts inside his home garage throughout the series?",
        "correct": "A 1933 Ford Roadster",
        "distractors": ["A 1957 Chevy Bel Air", "A 1969 Dodge Charger", "A 1932 Plymouth Coupe"],
        "d": 2
    },
    {
        "q": "Which character actor was originally cast as Tim's Tool Time assistant Glen before dropping out to film Groundhog Day, allowing Richard Karn to audition?",
        "correct": "Stephen Tobolowsky",
        "distractors": ["Stephen Root", "Kurt Fuller", "John Kapelos"],
        "d": 3
    },
    {
        "q": "What subculture style did youngest son Mark Taylor (Taran Noah Smith) shockingly adopt during Season 7?",
        "correct": "Goth, dressing exclusively in black with dark makeup and trench coats",
        "distractors": ["Grunge rocker with bleached blonde hair", "Hip-hop skater with oversized jeans", "Preppy yacht-club style with sweater vests"],
        "d": 2
    },
    {
        "q": "What was the name of Al Borland's domineering, unseen mother whose immense size and appetite were frequent punchlines?",
        "correct": "Alma Borland",
        "distractors": ["Bertha Borland", "Mildred Borland", "Agnes Borland"],
        "d": 2
    },
    {
        "q": "In the series finale 'The Long and Winding Road', what job offer does Jill accept that prompts the family's relocation?",
        "correct": "A psychology clinical fellowship in Bloomington, Indiana",
        "distractors": ["A professorship at Columbia University in New York", "A hospital administration post in Chicago, Illinois", "A counseling directorship in Denver, Colorado"],
        "d": 2
    },
    {
        "q": "What athletic sport was eldest son Brad Taylor (Zachery Ty Bryan) poised to play at the collegiate level before a knee injury?",
        "correct": "Soccer",
        "distractors": ["Football", "Baseball", "Ice Hockey"],
        "d": 2
    },
    {
        "q": "What was the name of the eccentric, elderly owner of Binford Tools who frequently appeared on Tool Time?",
        "correct": "John Binford",
        "distractors": ["Arthur Binford", "Walter Binford", "Charles Binford"],
        "d": 3
    },
    {
        "q": "What was the real-life childhood origin of Wilson's face being permanently obscured?",
        "correct": "Tim Allen remembered being a small child and only ever seeing the top half of his neighbor's head over the tall fence",
        "distractors": ["Earl Hindman had a contract clause forbidding facial photography due to theatrical roles", "The creators wanted to hide the fact that multiple actors played Wilson", "The character was originally conceived as a mythical garden gnome"],
        "d": 2
    },

    # The Drew Carey Show (15 questions)
    {
        "q": "What department store in Cleveland, Ohio served as the primary workplace for Drew Carey as Assistant Director of Personnel?",
        "correct": "Winfred-Louder",
        "distractors": ["Halle Brothers", "Higbee's", "May Company"],
        "d": 1
    },
    {
        "q": "What was the name of Drew's garishly dressed, heavy-blue-eyeshadow-wearing cosmetic counter nemesis played by Kathy Kinney?",
        "correct": "Mimi Bobeck",
        "distractors": ["Nora O'Dougherty", "Penny Peters", "Darcy Fontaine"],
        "d": 1
    },
    {
        "q": "What home-brewed, coffee-infused alcoholic beverage did Drew and his friends produce and sell out of his garage?",
        "correct": "Buzz Beer",
        "distractors": ["Turbo Stout", "Rocket Ale", "Cleveland Caffeinated Lager"],
        "d": 1
    },
    {
        "q": "What was the name of Drew Carey's pompous, tyrannical British boss played by Scottish comedian Craig Ferguson?",
        "correct": "Mr. Nigel Wick",
        "distractors": ["Mr. Julian Mercer", "Mr. Colin Bell", "Mr. Rupert Giles"],
        "d": 1
    },
    {
        "q": "What high-energy rock song by The Presidents of the United States of America served as the iconic opening theme for later seasons?",
        "correct": "Cleveland Rocks",
        "distractors": ["Five O'Clock World", "Moon Over Parma", "Rock and Roll All Nite"],
        "d": 1
    },
    {
        "q": "What delivery company did Drew's perpetually scatterbrained friend Oswald Lee Harvey drive a truck for?",
        "correct": "Global Parcel",
        "distractors": ["QuickShip Express", "Buckeye Logistics", "Speedy Delivery"],
        "d": 2
    },
    {
        "q": "What medical testing facility and research laboratory employed Drew's neurotic, super-genius friend Lewis Kiniski as a janitor and test subject?",
        "correct": "DrugCo",
        "distractors": ["OmniPharm", "BioHealth Labs", "Pharmatech"],
        "d": 2
    },
    {
        "q": "What annual holiday tradition on The Drew Carey Show challenged viewers to spot dozens of deliberate continuity blunders for prizes?",
        "correct": "The April Fools' Day Contest episodes ('Drew's Poop Episodes')",
        "distractors": ["The Super Bowl Stunt episodes", "The Halloween Horror specials", "The New Year's Resolution crossovers"],
        "d": 2
    },
    {
        "q": "Who portrayed Kate O'Brien, Drew's lifelong tomboy friend and romantic interest, before departing to star in Scrubs?",
        "correct": "Christa Miller",
        "distractors": ["Cynthia Watros", "Kelly Perine", "Nan Martin"],
        "d": 2
    },
    {
        "q": "Which family member of Drew's unexpectedly entered a passionate romance with his arch-enemy Mimi Bobeck and eventually married her?",
        "correct": "His cross-dressing brother Steve Carey (John Carroll Lynch)",
        "distractors": ["His uncle Cecil Carey", "His estranged cousin Randy Carey", "His father George Carey"],
        "d": 2
    },
    {
        "q": "What physical comedic calling card did Mimi routinely leave in Drew's office as an insult?",
        "correct": "Inflatable trolls and pigs, or defacing his desk with pink paint",
        "distractors": ["Dead fish wrapped in newspapers", "Scented love letters to mock his loneliness", "Piles of rotten bananas"],
        "d": 2
    },
    {
        "q": "Which major improvisational comedy show did Drew Carey host simultaneously with The Drew Carey Show on ABC?",
        "correct": "Whose Line Is It Anyway?",
        "distractors": ["Wild 'N Out", "Improv-A-Ganza", "Curb Your Enthusiasm"],
        "d": 1
    },
    {
        "q": "What popular 1960s pop song by The Vogues was used with elaborate Broadway-style street dancing as the show's theme song in Season 2?",
        "correct": "Five O'Clock World",
        "distractors": ["You Really Got Me", "Downtown", "Time of the Season"],
        "d": 2
    },
    {
        "q": "What instrument did Drew Carey frequently play during musical numbers and credits sequences on the show?",
        "correct": "Accordion",
        "distractors": ["Electric Bass", "Banjo", "Trumpet"],
        "d": 2
    },
    {
        "q": "In Season 5, what did Mr. Wick force Drew to do to prevent Wick from being deported back to the United Kingdom?",
        "correct": "Enter into a sham same-sex domestic partnership/marriage with him",
        "distractors": ["Falsify immigration papers claiming Wick was an American Indian", "Smuggle him across the Canadian border in a Buzz Beer delivery truck", "Adopt him as his legal dependent son"],
        "d": 3
    },

    # Coach (10 questions)
    {
        "q": "What was the name of the fictional university football team coached by Hayden Fox on Coach?",
        "correct": "The Minnesota State University Screaming Eagles",
        "distractors": ["The Minneapolis Vikings", "The North Star Badgers", "The Great Lakes Lumberjacks"],
        "d": 1
    },
    {
        "q": "Who portrayed Coach Hayden Fox, earning three consecutive Emmy nominations and winning in 1992?",
        "correct": "Craig T. Nelson",
        "distractors": ["Jerry Van Dyke", "Barry Bostwick", "Tom Skerritt"],
        "d": 1
    },
    {
        "q": "What was the name of Hayden's lovable, highly superstitious defensive coordinator played by Jerry Van Dyke?",
        "correct": "Luther Horatio Van Dam",
        "distractors": ["Michael Dybinski", "Fred O'Neall", "Art Armstrong"],
        "d": 1
    },
    {
        "q": "Which actor, who famously voiced Patrick Star on SpongeBob SquarePants, played dim-witted special teams coach Michael 'Dauber' Dybinski?",
        "correct": "Bill Fagerbakke",
        "distractors": ["Tom Kenny", "Clancy Brown", "Rodger Bumpass"],
        "d": 1
    },
    {
        "q": "What was the profession of Hayden's glamorous longtime girlfriend and later wife, Christine Armstrong?",
        "correct": "Television news anchor in Minneapolis",
        "distractors": ["Dean of admissions at Minnesota State", "Sports agent representing NFL players", "Owner of a lakeside lodge resort"],
        "d": 1
    },
    {
        "q": "In Season 8, Hayden Fox leaves college athletics to take the head coaching job with which fictional NFL expansion franchise?",
        "correct": "The Orlando Breakers",
        "distractors": ["The Florida Sharks", "The Tampa Bay Vipers", "The Miami Mavericks"],
        "d": 2
    },
    {
        "q": "Who created Coach and named protagonist Hayden Fox after legendary real-life Iowa Hawkeyes coach Hayden Fry?",
        "correct": "Barry Kemp",
        "distractors": ["Ken Levine", "Steven Bochco", "Donald P. Bellisario"],
        "d": 3
    },
    {
        "q": "What was the name of Luther Van Dam's prized pet basset hound who accompanied him everywhere?",
        "correct": "Quincy",
        "distractors": ["Barney", "Buster", "Winston"],
        "d": 2
    },
    {
        "q": "What college football bowl game did the Screaming Eagles win to secure the national championship in Season 5?",
        "correct": "The Pioneer Bowl",
        "distractors": ["The Rose Bowl", "The Citrus Bowl", "The Alamo Bowl"],
        "d": 3
    },
    {
        "q": "Who portrayed Hayden's bright, ambitious college student daughter Kelly Fox?",
        "correct": "Clare Carey",
        "distractors": ["Pam Dawber", "Georgia Engel", "Katherine Helmond"],
        "d": 2
    },

    # Murphy Brown (15 questions)
    {
        "q": "What was the title of the elite Washington D.C. television newsmagazine anchored by Murphy Brown?",
        "correct": "FYI",
        "distractors": ["60 Minutes D.C.", "Capitol Report", "The Weekly Insider"],
        "d": 1
    },
    {
        "q": "How many Primetime Emmy Awards for Outstanding Lead Actress in a Comedy Series did Candice Bergen win playing Murphy Brown?",
        "correct": "Five",
        "distractors": ["Three", "Four", "Six"],
        "d": 2
    },
    {
        "q": "Which U.S. Vice President ignited a fiery 1992 cultural debate by publicly condemning Murphy Brown for choosing to have a baby out of wedlock?",
        "correct": "Dan Quayle",
        "distractors": ["George H.W. Bush", "Al Gore", "Dick Cheney"],
        "d": 1
    },
    {
        "q": "What was the long-running gag regarding Murphy Brown's home and her house painter Eldin Bernecky (Robert Pastorelli)?",
        "correct": "He lived in her townhouse for seasons constantly stripping and painting wallpaper without ever finishing",
        "distractors": ["He refused to paint in any color other than neon chartreuse", "He was secretly an undercover FBI operative watching her house", "He accidentally demolished three different load-bearing walls"],
        "d": 2
    },
    {
        "q": "What was the recurring running joke regarding Murphy Brown's executive secretaries at FYI?",
        "correct": "She fired or terrified a new bizarre secretary every single week, going through nearly 100 over the series",
        "distractors": ["None of them spoke English, communicating only through written notes", "They were all relatives of the network president who couldn't type", "They were all convicted felons on work-release programs"],
        "d": 1
    },
    {
        "q": "What was the name of the neurotic, hyper-stressed young executive producer of FYI played by Grant Shaud?",
        "correct": "Miles Silverberg",
        "distractors": ["Jim Dial", "Frank Fontana", "Phil Corley"],
        "d": 2
    },
    {
        "q": "What former beauty pageant winner joined FYI as an anchor, struggling to be taken seriously as a real journalist?",
        "correct": "Corky Sherwood (Faith Ford)",
        "distractors": ["Audrey Cohen", "Kay Carter-Shepley", "Tara West"],
        "d": 1
    },
    {
        "q": "What was the name of the dignified, legendary veteran news anchor who served as Murphy's old-school mentor on FYI?",
        "correct": "Jim Dial (Charles Kimbrough)",
        "distractors": ["Frank Fontana", "Walter Miller", "Peter Thomas"],
        "d": 2
    },
    {
        "q": "What musical genre provided Murphy Brown with her personal therapy, theme songs, and shower-singing anthems?",
        "correct": "Motown and 1960s Soul",
        "distractors": ["1940s Big Band Jazz", "Delta Blues", "Classic Punk Rock"],
        "d": 2
    },
    {
        "q": "What name did Murphy Brown give to her son born at the end of Season 4, honoring her mother?",
        "correct": "Avery",
        "distractors": ["Benjamin", "Alexander", "Julian"],
        "d": 2
    },
    {
        "q": "What legendary Soul icon made a cameo appearance on Murphy Brown, harmonizing with Murphy to 'Natural Woman'?",
        "correct": "Aretha Franklin",
        "distractors": ["Diana Ross", "Gladys Knight", "Tina Turner"],
        "d": 2
    },
    {
        "q": "Who created Murphy Brown and famously drafted the fiery Season 5 response episode to Dan Quayle's family values speech?",
        "correct": "Diane English",
        "distractors": ["Linda Bloodworth-Thomason", "Susan Harris", "Marta Kauffman"],
        "d": 2
    },
    {
        "q": "What was the name of the cozy Washington tavern where the FYI news team gathered to drink, gossip, and celebrate?",
        "correct": "Phil's Bar",
        "distractors": ["The Press Club Pub", "The Capitol Lounge", "Off the Record"],
        "d": 2
    },
    {
        "q": "Why did Candice Bergen withdraw her name from Emmy consideration after her fifth win in 1995?",
        "correct": "She felt winning more awards would be unfair to other deserving comedic actresses",
        "distractors": ["A contract dispute with CBS over her syndication residuals", "Her public feud with the Television Academy over category definitions", "She wanted to focus exclusively on directing"],
        "d": 3
    },
    {
        "q": "What medical storyline in Murphy Brown's tenth season sparked national awareness and congressional discussions on medical marijuana?",
        "correct": "Her diagnosis and treatment for breast cancer",
        "distractors": ["Her recovery from emergency open-heart surgery", "Her battle with clinical postpartum depression", "Her experimental treatment for multiple sclerosis"],
        "d": 2
    },

    # Grace Under Fire, Cybill, The King of Queens, Everybody Loves Raymond (20 questions)
    {
        "q": "Stand-up comedian Brett Butler starred in Grace Under Fire as Grace Kelly, who worked at which industrial workplace in Missouri?",
        "correct": "An oil refinery",
        "distractors": ["An auto assembly plant", "A coal preparation facility", "A commercial chemical warehouse"],
        "d": 2
    },
    {
        "q": "Which prolific television powerhouse created Grace Under Fire before creating Dharma & Greg, Two and a Half Men, and The Big Bang Theory?",
        "correct": "Chuck Lorre",
        "distractors": ["Bill Lawrence", "Steven Levitan", "Greg Daniels"],
        "d": 2
    },
    {
        "q": "On the sitcom Cybill, which Broadway powerhouse won an Emmy Award in 1995 playing Cybill's martini-swilling, caustic best friend Maryann Thorpe?",
        "correct": "Christine Baranski",
        "distractors": ["Jane Lynch", "Holland Taylor", "Allison Janney"],
        "d": 1
    },
    {
        "q": "What was Maryann Thorpe's hilarious recurring obsession throughout the run of Cybill?",
        "correct": "Executing elaborate, vengeful practical jokes against her wealthy plastic-surgeon ex-husband 'Dr. Dick'",
        "distractors": ["Auditioning for daytime soap operas to humiliate her daughter", "Writing an anonymous tell-all memoir about Hollywood producers", "Trying to seduce every tennis instructor at the Beverly Hills club"],
        "d": 2
    },
    {
        "q": "Premiering in 1998, The King of Queens starred Kevin James as Doug Heffernan, who held what occupation?",
        "correct": "Delivery driver for the International Parcel Service (IPS)",
        "distractors": ["Subway conductor for the MTA", "Sanitation worker for the City of New York", "Warehouse forklift operator for Sears"],
        "d": 1
    },
    {
        "q": "Who played Doug Heffernan's glamorous, quick-tempered wife Carrie on The King of Queens?",
        "correct": "Leah Remini",
        "distractors": ["Marisa Tomei", "Debra Messing", "Sarah Silverman"],
        "d": 1
    },
    {
        "q": "Which comedy legend played Carrie Heffernan's eccentric, loud-mouthed father Arthur Spooner who lived in their basement?",
        "correct": "Jerry Stiller",
        "distractors": ["Jack Carter", "Frank Gorshin", "Don Rickles"],
        "d": 1
    },
    {
        "q": "What stand-up comedian and actor played Doug's nerdy, comic-book-obsessed subway-token clerk friend Spence Olchin?",
        "correct": "Patton Oswalt",
        "distractors": ["Paul Rudd", "David Cross", "Brian Posehn"],
        "d": 1
    },
    {
        "q": "What New York City borough serves as the setting for Doug and Carrie's home on The King of Queens?",
        "correct": "Queens",
        "distractors": ["Brooklyn", "Staten Island", "The Bronx"],
        "d": 1
    },
    {
        "q": "On Everybody Loves Raymond, what professional occupation does Ray Barone hold at Newsday?",
        "correct": "Sports columnist",
        "distractors": ["Investigative crime reporter", "Political cartoonist", "Advertising copy editor"],
        "d": 1
    },
    {
        "q": "Who portrayed Ray Barone's suffocating, passive-aggressive mother Marie Barone across all nine seasons?",
        "correct": "Doris Roberts",
        "distractors": ["Georgia Engel", "Estelle Harris", "Marion Ross"],
        "d": 1
    },
    {
        "q": "What was the iconic grunted catchphrase of Ray's cynical, armchair-sitting father Frank Barone, played by Peter Boyle?",
        "correct": "Holy crap!",
        "distractors": ["Give me a break!", "What a bunch of bologna!", "Shut your trap!"],
        "d": 1
    },
    {
        "q": "What was the law enforcement profession of Ray's towering, deeply insecure older brother Robert Barone (Brad Garrett)?",
        "correct": "NYPD patrol officer, later promoted to Lieutenant",
        "distractors": ["Nassau County sheriff's deputy", "Port Authority security officer", "New York State Trooper"],
        "d": 1
    },
    {
        "q": "What peculiar nervous physical habit did Robert Barone display before eating any food?",
        "correct": "Touching the food to his chin",
        "distractors": ["Sniffing the fork three times", "Tapping the plate with both thumbs", "Blowing on his knuckles"],
        "d": 1
    },
    {
        "q": "Which actress portrayed Ray's exhausted, sharp-witted wife Debra Barone, winning two Primetime Emmy Awards?",
        "correct": "Patricia Heaton",
        "distractors": ["Laurie Metcalf", "Jane Kaczmarek", "Felicity Huffman"],
        "d": 1
    },
    {
        "q": "What Long Island town do the Barone families live in, directly across the street from one another?",
        "correct": "Lynbrook",
        "distractors": ["Garden City", "Massapequa", "Mineola"],
        "d": 2
    },
    {
        "q": "Who created Everybody Loves Raymond, basing the show's dysfunctional family dynamic on his own parents Max and Helen?",
        "correct": "Phil Rosenthal",
        "distractors": ["David Letterman", "Chuck Lorre", "Bill Lawrence"],
        "d": 2
    },
    {
        "q": "In the famous Season 2 episode 'The Letter', why is Debra furious at Ray regarding his mother Marie?",
        "correct": "Ray cowardly gave Debra's heartfelt letter to Marie and pretended he had nothing to do with it",
        "distractors": ["Ray threw away Marie's secret manicotti recipe", "Ray forgot Marie's 70th birthday party to watch the Jets", "Ray secretly gave Marie a spare key to their bedroom"],
        "d": 2
    },
    {
        "q": "What was the name of Robert Barone's eccentric, Amy-obsessed in-laws played by Fred Willard and Georgia Engel?",
        "correct": "Hank and Pat MacDougall",
        "distractors": ["Howard and Millie Henderson", "Richard and Evelyn Parker", "Arthur and Grace Cunningham"],
        "d": 2
    },
    {
        "q": "Which late-night talk show host produced Everybody Loves Raymond through his production company Worldwide Pants?",
        "correct": "David Letterman",
        "distractors": ["Jay Leno", "Conan O'Brien", "Arsenio Hall"],
        "d": 2
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "staging", "90s_sitcoms_batch3.json")
    make_batch(q_batch3, 3, out)
