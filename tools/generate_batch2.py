import sys
from make_batch import build_batch

# Batch 2: Miami Vice & Knight Rider (80s Action/Style & High-Tech Vehicles)
# 100 questions: 30 d1, 40 d2, 30 d3

questions = [
    # Miami Vice - Textual / Plot / Characters
    (
        "Who played Detective James 'Sonny' Crockett on Miami Vice?",
        "Don Johnson",
        ["Philip Michael Thomas", "Edward James Olmos", "Michael Talbott"],
        1
    ),
    (
        "Who played Detective Ricardo 'Rico' Tubbs on Miami Vice?",
        "Philip Michael Thomas",
        ["Don Johnson", "Denzel Washington", "Carl Weathers"],
        1
    ),
    (
        "What was Sonny Crockett's undercover drug smuggler alias on Miami Vice?",
        "Sonny Burnett",
        ["Rico Cooper", "Jimmy Cole", "Johnny Staccato"],
        1
    ),
    (
        "What was Ricardo Tubbs' undercover persona when infiltrating criminal syndicates?",
        "Rico Cooper",
        ["Sonny Burnett", "Teddy Prentiss", "Ricky Ricardo"],
        1
    ),
    (
        "What kind of animal was Elvis, Sonny Crockett's pet living aboard his sailboat?",
        "Alligator",
        ["Pelican", "Boa constrictor", "Parrot"],
        1
    ),
    (
        "What was the name of Sonny Crockett's sailboat home docked in Miami?",
        "St. Vitus' Dance",
        ["The Lady Luck", "Biscayne Dream", "Key Largo Queen"],
        3
    ),
    (
        "Which stern, taciturn lieutenant led the Vice squad starting early in season 1?",
        "Martin Castillo",
        ["Lou Rodriguez", "Frank Hackett", "Stan Switek"],
        1
    ),
    (
        "Which actor won both an Emmy and a Golden Globe for his role as Lieutenant Martin Castillo on Miami Vice?",
        "Edward James Olmos",
        ["Jimmy Smits", "Hector Elizondo", "Raul Julia"],
        1
    ),
    (
        "In seasons 1 and 2 of Miami Vice, what vehicle did Sonny Crockett drive before it was destroyed?",
        "Black Ferrari Daytona Spyder replica",
        ["White Ferrari Testarossa", "Red Porsche 911 Turbo", "Silver DeLorean DMC-12"],
        2
    ),
    (
        "How was Sonny Crockett's black Daytona Spyder destroyed in the season 3 premiere?",
        "Hit by a Stinger missile",
        ["Blown up by a car bomb", "Driven into Biscayne Bay", "Crushed in a junkyard compactor"],
        2
    ),
    (
        "What iconic white sports car did Sonny Crockett drive starting in season 3 of Miami Vice?",
        "Ferrari Testarossa",
        ["Lamborghini Countach", "Porsche 928", "Aston Martin Vantage"],
        1
    ),
    (
        "Why did Ferrari provide two authentic Testarossas to the production of Miami Vice for season 3?",
        "To stop the show from using kit-car replicas built on Corvette chassis",
        ["As a sponsorship deal for Enzo Ferrari's retirement", "Because Don Johnson became a factory test driver", "In exchange for European syndication rights"],
        2
    ),
    (
        "What comedy-relief detective duo on Miami Vice often handled surveillance in a bug van?",
        "Stan Switek and Larry Zito",
        ["Gina Calabrese and Trudy Joplin", "Crockett and Tubbs", "Castillo and Rodriguez"],
        2
    ),
    (
        "Which actor played Detective Stan Switek on Miami Vice?",
        "Michael Talbott",
        ["John Diehl", "Bruce Willis", "Richard Jenkins"],
        2
    ),
    (
        "Which actor played Detective Larry Zito until his character was killed off in season 3?",
        "John Diehl",
        ["Michael Talbott", "Dennis Farina", "Ving Rhames"],
        3
    ),
    (
        "How was Detective Larry Zito killed off in the season 3 episode 'Down for the Count'?",
        "Forced drug overdose by a corrupt boxing promoter",
        ["Drive-by shooting outside police headquarters", "Helicopter crash in the Everglades", "Poisoned at a hotel banquet"],
        3
    ),
    (
        "Which female detective partners regularly backed up Crockett and Tubbs on undercover stings?",
        "Gina Calabrese and Trudy Joplin",
        ["Mary Beth Lacey and Chris Cagney", "Kate Russo and Julie Barnes", "Laura Holt and Mildred Krebs"],
        2
    ),
    (
        "Which actress played Detective Trudy Joplin on Miami Vice?",
        "Olivia Brown",
        ["Saundra Santiago", "Pam Grier", "Robin Givens"],
        3
    ),
    (
        "Which actress played Detective Gina Calabrese on Miami Vice?",
        "Saundra Santiago",
        ["Olivia Brown", "Talisa Soto", "Maria Conchita Alonso"],
        3
    ),
    (
        "What famous rock song soundtracked the iconic night driving sequence in the pilot episode of Miami Vice?",
        "In the Air Tonight by Phil Collins",
        ["Smuggler's Blues by Glenn Frey", "Bad to the Bone by George Thorogood", "Boys of Summer by Don Henley"],
        1
    ),
    (
        "Which musician scored Miami Vice with groundbreaking electronic synthesizer compositions?",
        "Jan Hammer",
        ["Harold Faltermeyer", "Giorgio Moroder", "Vangelis"],
        1
    ),
    (
        "What Billboard chart milestone did Jan Hammer's 'Miami Vice Theme' achieve in November 1985?",
        "Hit Number 1 on the Billboard Hot 100",
        ["Spent 20 weeks at Number 2", "Was the best-selling country crossover", "Sold one million vinyl 45s in 48 hours"],
        2
    ),
    (
        "How many consecutive weeks did the Miami Vice soundtrack album spend at Number 1 on the Billboard 200 album chart?",
        "11 weeks",
        ["3 weeks", "22 weeks", "40 weeks"],
        3
    ),
    (
        "Which Eagles member guest-starred in the episode 'Smuggler's Blues' as a bush pilot named Jimmy?",
        "Glenn Frey",
        ["Don Henley", "Joe Walsh", "Timothy B. Schmit"],
        2
    ),
    (
        "Which Glenn Frey song, written for Miami Vice, peaked at Number 2 on the Billboard Hot 100 in 1985?",
        "You Belong to the City",
        ["The Heat Is On", "Smuggler's Blues", "True Love"],
        2
    ),
    (
        "What signature fashion style did Don Johnson popularize worldwide through Miami Vice?",
        "Pastel jackets over T-shirts with slip-on loafers and no socks",
        ["Double-breasted navy suits with red power ties", "Leather trench coats with fedoras", "Denim jackets over flannel shirts"],
        1
    ),
    (
        "Which sunglasses style saw sales surge into the hundreds of thousands after being worn by Don Johnson on Miami Vice?",
        "Ray-Ban Wayfarer",
        ["Oakley Frogskins", "Aviator Teardrops", "Carrera Porche Design"],
        1
    ),
    (
        "Who created Miami Vice after a legendary two-word brainstorming memo reading 'MTV Cops'?",
        "Anthony Yerkovich",
        ["Steven Bochco", "Glen A. Larson", "Dick Wolf"],
        2
    ),
    (
        "Which legendary filmmaker served as executive producer, defining Miami Vice's visual aesthetic and pastel color palette?",
        "Michael Mann",
        ["Ridley Scott", "Brian De Palma", "Walter Hill"],
        1
    ),
    (
        "Which famous rule did Michael Mann strictly enforce regarding colors allowed on set in Miami Vice?",
        "No earth tones like brown, tan, or beige",
        ["No black clothing under any circumstances", "Only primary colors allowed in day scenes", "All neon signs had to be green"],
        2
    ),
    (
        "In season 5, what amnesia storyline did Sonny Crockett experience after surviving a boat explosion?",
        "He genuinely believed he was his drug-dealing alter ego Sonny Burnett",
        ["He forgot English and spoke only Spanish", "He joined the DEA under a false identity", "He believed he was a Catholic priest"],
        2
    ),
    (
        "What was the title of the two-hour series finale of Miami Vice broadcast in May 1989?",
        "Freefall",
        ["Miami Farewell", "End of the Line", "The Last Sting"],
        3
    ),
    (
        "Which future Oscar winner guest-starred in season 4 as a high-school mob informant named Sean McVeigh?",
        "Ben Stiller",
        ["Chris Rock", "Viggo Mortensen", "Brad Pitt"],
        3
    ),
    (
        "Which future Die Hard star guest-starred in season 1 as gunrunner Tony Amato?",
        "Bruce Willis",
        ["Mel Gibson", "Kurt Russell", "Arnold Schwarzenegger"],
        2
    ),
    (
        "Which legendary jazz trumpeter made a rare dramatic guest appearance on Miami Vice as ivory merchant Hank Weldon?",
        "Miles Davis",
        ["Dizzy Gillespie", "Herbie Hancock", "Wynton Marsalis"],
        3
    ),
    (
        "Which former Watergate burglar guest-starred in two episodes of Miami Vice as real estate conspirator William Maynard?",
        "G. Gordon Liddy",
        ["E. Howard Hunt", "John Dean", "Chuck Colson"],
        3
    ),
    (
        "Which firearms manufacturer provided Sonny Crockett's primary 10mm handgun in the early seasons?",
        "Bren Ten",
        ["Glock 17", "Beretta 92FS", "Colt Python"],
        3
    ),
    (
        "What breed of dog did Tubbs briefly look after in the episode 'The Great McCarthy'?",
        "A greyhound racer",
        ["A pit bull terrier", "A German shepherd", "A prize-winning poodle"],
        3
    ),
    (
        "What acronym did Philip Michael Thomas famously coin on talk shows to describe his career aspirations?",
        "EGOT (Emmy, Grammy, Oscar, Tony)",
        ["STAR (Screen, Television, Academy, Radio)", "GOLD (Grammy, Oscar, Laureate, Daytime)", "FAME (Film, Acting, Music, Excellence)"],
        3
    ),
    (
        "What broadcast network was home to Miami Vice throughout its 1984 to 1989 run?",
        "NBC",
        ["CBS", "ABC", "Fox"],
        1
    ),
    (
        "In what time slot did Miami Vice famously air on Friday nights, battling CBS's Falcon Crest?",
        "10:00 PM Eastern",
        ["8:00 PM Eastern", "9:00 PM Eastern", "11:30 PM Eastern"],
        2
    ),
    (
        "Who was the prime villain responsible for killing Tubbs' brother Rafael in the Miami Vice pilot?",
        "Calderone",
        ["Lombard", "Montoya", "Arroyo"],
        2
    ),
    (
        "Which Colombian drug lord did Crockett and Tubbs pursue across multiple episodes, culminating in 'Calderone's Demise'?",
        "Esteban Calderone",
        ["Orlando Montoya", "Juan Carlos Gomez", "Hector Fuentes"],
        2
    ),
    (
        "What singer played Calderone's daughter Angelina, who fell in love with Tubbs?",
        "Phanie Napoli",
        ["Irene Cara", "Gloria Estefan", "Maria Conchita Alonso"],
        3
    ),
    (
        "In season 4, Sonny Crockett impulsively married a pop star played by which real-life rock singer?",
        "Sheena Easton",
        ["Pat Benatar", "Debbie Harry", "Kim Carnes"],
        2
    ),
    (
        "What was the name of Sheena Easton's pop-star character who married Sonny Crockett on Miami Vice?",
        "Caitlin Davies",
        ["Laura Rollins", "Vanessa Cruz", "Brenda Fox"],
        3
    ),
    (
        "How was Sonny Crockett's pop-star wife Caitlin Davies killed in season 4?",
        "Shot by Crockett's nemesis Frank Hackman at a concert hall",
        ["Killed in a car bomb meant for Crockett", "Poisoned backstage at a recording studio", "Plane crash en route to Nassau"],
        3
    ),
    (
        "What iconic piece of surveillance technology did Switek and Zito operate from the back of their bug van?",
        "Audio eavesdropping antennas disguised in a pest control van",
        ["Thermal heat cameras disguised in an ice cream truck", "A satellite dish disguised as a TV antenna", "A periscope disguised as a plumber pipe"],
        2
    ),
    (
        "Which famous comedian played a scam artist and loan shark named Fast Eddie in season 4?",
        "Phil Hartman",
        ["Chris Rock", "Penn Jillette", "Gilbert Gottfried"],
        3
    ),
    (
        "How many seasons of Miami Vice were produced and broadcast by NBC?",
        "5 seasons",
        ["4 seasons", "6 seasons", "7 seasons"],
        2
    ),

    # Knight Rider - Textual / Plot / Vehicles / Gadgets
    (
        "Who starred as Michael Knight in the 1982 television series Knight Rider?",
        "David Hasselhoff",
        ["Tom Selleck", "Lee Majors", "Richard Dean Anderson"],
        1
    ),
    (
        "What was Michael Knight's original identity before undergoing facial reconstruction in the pilot?",
        "Michael Long",
        ["Michael Stone", "Michael Vance", "Michael Hunter"],
        2
    ),
    (
        "What did the acronym K.I.T.T. officially stand for on Knight Rider?",
        "Knight Industries Two Thousand",
        ["Knight Integrated Tactical Transport", "Kinetic Intelligent Tank Technology", "Knight Industrial Top Tracer"],
        1
    ),
    (
        "What make and model of car was customized to create KITT in Knight Rider?",
        "1982 Pontiac Firebird Trans Am",
        ["1981 Chevrolet Camaro Z28", "1982 Dodge Charger Daytona", "1983 Ford Mustang GT"],
        1
    ),
    (
        "Which acclaimed actor provided the voice of KITT throughout Knight Rider?",
        "William Daniels",
        ["Peter Cullen", "Paul Frees", "James Earl Jones"],
        1
    ),
    (
        "Why was William Daniels not credited on screen for voicing KITT during the original run of Knight Rider?",
        "He wanted the audience to believe the car was a genuine autonomous computer",
        ["A contract dispute with Universal Pictures", "He was exclusively under contract to CBS", "He recorded his lines under a pseudonym"],
        2
    ),
    (
        "What other classic 1980s drama series was William Daniels starring on while simultaneously voicing KITT?",
        "St. Elsewhere",
        ["Hill Street Blues", "Dallas", "L.A. Law"],
        2
    ),
    (
        "When did David Hasselhoff and William Daniels first meet in person during the production of Knight Rider?",
        "At the cast and crew Christmas party months into filming",
        ["During the initial table read for the pilot", "In a post-production audio dubbing room", "At the 1983 Emmy Awards ceremony"],
        2
    ),
    (
        "What organization employed Michael Knight and KITT on Knight Rider?",
        "FLAG (Foundation for Law and Government)",
        ["CUP (Citizens United for Protection)", "SHIELD (Strategic Hazard Intervention)", "PHOENIX (Phoenix Foundation)"],
        1
    ),
    (
        "Who was the dying billionaire philanthropist who founded FLAG and rescued Michael Long?",
        "Wilton Knight",
        ["Devon Miles", "Robin Masters", "Charles Townsend"],
        2
    ),
    (
        "Which veteran actor portrayed Wilton Knight and narrated the iconic opening sequence of Knight Rider?",
        "Richard Basehart",
        ["Edward Mulhare", "John Hillerman", "Lionel Stander"],
        2
    ),
    (
        "Who served as the dignified British director of FLAG and Michael Knight's mentor?",
        "Devon Miles",
        ["Jonathan Higgins", "Arthur Pringle", "Alistair Finch"],
        1
    ),
    (
        "Which Irish-born actor played Devon Miles on Knight Rider?",
        "Edward Mulhare",
        ["Bernard Fox", "Patrick Macnee", "John Gielgud"],
        2
    ),
    (
        "Who was KITT's primary mechanic and chief technician in seasons 1, 3, and 4?",
        "Dr. Bonnie Barstow",
        ["Dr. April Curtis", "Dr. Amanda Bentley", "Dr. Maggie O'Keefe"],
        1
    ),
    (
        "Which actress portrayed KITT's beloved engineer Dr. Bonnie Barstow?",
        "Patricia McPherson",
        ["Rebecca Holden", "Stephanie Zimbalist", "Dana Delany"],
        2
    ),
    (
        "Which technician replaced Bonnie Barstow as KITT's mechanic during season 2?",
        "April Curtis",
        ["Marta Simmons", "Robin West", "Diana Flavin"],
        3
    ),
    (
        "Which actress played April Curtis during season 2 of Knight Rider?",
        "Rebecca Holden",
        ["Patricia McPherson", "Connie Sellecca", "Erin Gray"],
        3
    ),
    (
        "What iconic visual feature sweeped side-to-side on the front nose cone of KITT?",
        "A red halogen scanner light bar",
        ["A green laser radar beam", "A rotating amber strobe light", "A blue neon strip"],
        1
    ),
    (
        "What button on KITT's dashboard allowed the car to leap over obstacles into the air?",
        "Turbo Boost",
        ["Super Rocket", "Hydro Jump", "Hyper Thrust"],
        1
    ),
    (
        "What mode was introduced in season 4 that deployed hydraulic air brakes and cowls to reach 300 mph?",
        "Super Pursuit Mode",
        ["Hyperdrive Velocity", "Overdrive Assault", "Max Thrust System"],
        2
    ),
    (
        "What new button was added to KITT's dashboard in season 4 that converted him into an open-top convertible?",
        "The C button",
        ["The T-Top switch", "The Open Sky lever", "The Aero button"],
        3
    ),
    (
        "What vehicle served as FLAG's mobile headquarters where KITT drove up an open ramp while cruising on the highway?",
        "A black and gold GMC semi-truck",
        ["A customized military cargo plane", "An armored train car", "A luxury yacht docked on the coast"],
        1
    ),
    (
        "What was the name of KITT's evil prototype predecessor whose CPU lacked the preservation-of-human-life directive?",
        "KARR (Knight Automated Roving Robot)",
        ["KRON (Knight Robotic Operative Network)", "KARM (Kinetic Autonomous Recon Machine)", "KLON (Knight Law Operative Nexus)"],
        1
    ),
    (
        "Which legendary voice actor, famous as Optimus Prime, originally voiced KARR in the season 1 episode 'Trust Doesn't Rust'?",
        "Peter Cullen",
        ["Frank Welker", "Paul Frees", "Casey Kasem"],
        2
    ),
    (
        "Which iconic voice actor voiced KARR when the evil vehicle returned in season 3's 'K.I.T.T. vs. K.A.R.R.'?",
        "Paul Frees",
        ["Peter Cullen", "Don Messick", "Mel Blanc"],
        3
    ),
    (
        "What was the name of Wilton Knight's evil biological son, also played by David Hasselhoff with a goatee?",
        "Garthe Knight",
        ["Devon Knight Jr.", "Victor Knight", "Damian Knight"],
        2
    ),
    (
        "What gargantuan armored vehicle did Garthe Knight drive against KITT in the two-part episode 'Goliath'?",
        "An 18-wheel semi-truck coated in KITT's molecular bonding shell",
        ["A surplus military tank with depleted uranium armor", "A missile-launching hovercraft", "A titanium bulldozer"],
        2
    ),
    (
        "Who created the television series Knight Rider?",
        "Glen A. Larson",
        ["Stephen J. Cannell", "Donald P. Bellisario", "Quinn Martin"],
        2
    ),
    (
        "Which classic TV producer also created Battlestar Galactica and Magnum, P.I. alongside Knight Rider?",
        "Glen A. Larson",
        ["Steven Bochco", "Garry Marshall", "Aaron Spelling"],
        2
    ),
    (
        "Who co-composed the synthesizer-driven theme music for Knight Rider with Glen A. Larson?",
        "Stu Phillips",
        ["Mike Post", "Jan Hammer", "John Addison"],
        3
    ),
    (
        "Which hip-hop artist famously sampled the Knight Rider theme for his 1998 hit song 'Fire It Up'?",
        "Busta Rhymes",
        ["LL Cool J", "Snoop Dogg", "Jay-Z"],
        2
    ),
    (
        "What chemical defense made KITT's exterior practically invulnerable to bullets and conventional explosives?",
        "Tri-Helical Molecular Bonded Shell",
        ["Kevlar Titanium Plating", "Depleted Uranium Alloy", "Carbon Fiber Ceramic Shield"],
        2
    ),
    (
        "What wearable gadget allowed Michael Knight to communicate with KITT from anywhere?",
        "A two-way radio wristwatch",
        ["A walkie-talkie belt buckle", "A sunglasses transceiver", "An earpiece lapel pin"],
        1
    ),
    (
        "What was the name of the woman who shot Michael Long in the face in the pilot episode of Knight Rider?",
        "Tanya Walker",
        ["Adriana Dupree", "Elena Salazar", "Vanessa Adams"],
        3
    ),
    (
        "Which actress played the treacherous Tanya Walker in the Knight Rider pilot?",
        "Phyllis Davis",
        ["Morgan Fairchild", "Joan Collins", "Barbi Benton"],
        3
    ),
    (
        "How many seasons did the original Knight Rider series run on NBC?",
        "4 seasons",
        ["3 seasons", "5 seasons", "6 seasons"],
        2
    ),
    (
        "In the season 4 premiere 'Knight of the Juggernaut', who created the Super Pursuit Mode after KITT was destroyed by an armored vehicle?",
        "Bonnie Barstow and street mechanic RC3 (Reginald Cornelius III)",
        ["Devon Miles and Wilton Knight", "NASA aerospace engineers", "A secret team in Stuttgart, Germany"],
        3
    ),
    (
        "Which actor played Reginald Cornelius III (RC3), who joined Michael and Bonnie in season 4?",
        "Peter Parros",
        ["Carl Weathers", "Taurean Blacque", "Kevin Hooks"],
        3
    ),
    (
        "What special ability did KITT utilize to balance on two side wheels to squeeze through narrow alleys?",
        "Ski Mode",
        ["Tilt Track", "Wedge Angle", "Bicycle Drive"],
        2
    ),
    (
        "What was KITT's primary fuel source according to the lore established in the series?",
        "Hydrogen / synthetic fuel turbine engine",
        ["Nuclear fission micro-reactor", "Solar battery cells", "Standard unleaded 93 gasoline"],
        3
    ),
    (
        "Which actor made an early career guest appearance in Knight Rider as an outlaw biker in the episode 'A Nice, Indecent Little Town'?",
        "Luke Askew",
        ["Patrick Swayze", "Kurt Russell", "Willem Dafoe"],
        3
    ),
    (
        "What television series did David Hasselhoff star in immediately after Knight Rider concluded?",
        "Baywatch",
        ["The Young and the Restless", "Airwolf", "V.I.P."],
        1
    ),
    (
        "In what German-speaking countries did David Hasselhoff become a massive pop-music sensation following Knight Rider?",
        "Germany and Austria",
        ["France and Belgium", "Sweden and Norway", "Italy and Spain"],
        1
    ),
    (
        "What famous song did David Hasselhoff perform atop the Berlin Wall on New Year's Eve 1989?",
        "Looking for Freedom",
        ["Hooked on a Feeling", "Crazy for You", "Night Rocker"],
        1
    ),
    (
        "What was the name of Wilton Knight's daughter who attempted to seize control of FLAG in season 2?",
        "Jennifer Knight",
        ["Stephanie Knight", "Victoria Knight", "Clarissa Knight"],
        3
    ),
    (
        "What was KITT's top cruising speed without engaging Super Pursuit Mode?",
        "Roughly 200 mph",
        ["120 mph", "90 mph", "350 mph"],
        2
    ),
    (
        "Which 1991 television reunion movie brought David Hasselhoff and William Daniels back to fight crime in the year 2000?",
        "Knight Rider 2000",
        ["Knight Rider: The Next Generation", "KITT Returns", "The New Knight Rider"],
        2
    ),
    (
        "What color was KITT's exterior throughout the run of Knight Rider?",
        "Gloss black",
        ["Midnight blue", "Metallic silver", "Charcoal gray"],
        1
    ),
    (
        "Which voice synthesizer computer company provided the electronic sound effects for KITT's cockpit voice box display?",
        "Universal Sound Dept. / electronic LED bars",
        ["Texas Instruments Speak & Spell", "Atari 800 sound chip", "Moog modular laboratory"],
        3
    ),
    (
        "In which year did Knight Rider premiere on NBC?",
        "1982",
        ["1980", "1984", "1986"],
        2
    )
]

if __name__ == "__main__":
    build_batch(questions, 2, "tools/staging/80s_tv_shows_batch2.json")
