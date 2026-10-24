import sys
from make_batch import build_batch

# Batch 5: The A-Team & Magnum, P.I. (Action Adventure & Veteran Heroes)
# 100 questions: 30 d1, 40 d2, 30 d3

questions = [
    # The A-Team - Textual / Plot / Vehicles / Characters
    (
        "Who played the cigar-chomping leader Colonel John 'Hannibal' Smith on The A-Team?",
        "George Peppard",
        ["Dirk Benedict", "Dwight Schultz", "Robert Vaughn"],
        1
    ),
    (
        "What was Hannibal Smith's famous signature catchphrase on The A-Team?",
        "I love it when a plan comes together",
        ["I pity the fool!", "Let's be careful out there", "Book 'em, Danno"],
        1
    ),
    (
        "Which pop-culture icon played the muscle-bound mechanic Sergeant B.A. Baracus on The A-Team?",
        "Mr. T",
        ["Carl Weathers", "Hulk Hogan", "Ernie Hudson"],
        1
    ),
    (
        "What did the initials 'B.A.' stand for in B.A. Baracus's nickname?",
        "Bad Attitude",
        ["Big Action", "Battle Armor", "Brave Assault"],
        1
    ),
    (
        "What was B.A. Baracus's canonical full first and middle name on The A-Team?",
        "Bosco Albert",
        ["Benjamin Arthur", "Barnaby Alexander", "Boris Anthony"],
        2
    ),
    (
        "What major phobia did B.A. Baracus suffer from throughout the entire run of The A-Team?",
        "Extreme fear of flying",
        ["Claustrophobia in elevators", "Fear of open water and sharks", "Fear of heights and bridges"],
        1
    ),
    (
        "How did the A-Team routinely get B.A. Baracus onto airplanes against his will?",
        "Tricking him into drinking drugged milk or knocking him unconscious",
        ["Hypnotizing him with a gold watch", "Handcuffing him inside a shipping crate", "Disguising the plane as a train car"],
        1
    ),
    (
        "What was B.A. Baracus's favorite non-alcoholic beverage on The A-Team?",
        "A glass of milk",
        ["Root beer", "Lemonade", "Orange juice"],
        1
    ),
    (
        "What make and model of vehicle was the iconic black and metallic gray A-Team van?",
        "1983 GMC Vandura",
        ["1982 Chevrolet Beauville", "1984 Ford Econoline", "1983 Dodge Ram Van"],
        1
    ),
    (
        "What color stripe ran along the sides and over the rear spoiler of the A-Team van?",
        "Red",
        ["Yellow", "White", "Silver"],
        1
    ),
    (
        "Who played the handsome, smooth-talking con artist Lieutenant Templeton 'Faceman' Peck?",
        "Dirk Benedict",
        ["Tim Dunigan", "George Peppard", "Richard Hatch"],
        1
    ),
    (
        "Which actor originally played Face in the pilot episode before Dirk Benedict took over the role?",
        "Tim Dunigan",
        ["Dwight Schultz", "William Lucking", "Lance LeGault"],
        3
    ),
    (
        "Why was Tim Dunigan replaced by Dirk Benedict after The A-Team pilot?",
        "Producers felt Dunigan was too tall and looked too young to be a Vietnam veteran",
        ["Dunigan broke his leg during a stunt", "Dunigan refused to sign a five-year contract", "Dunigan could not perform comedic scenes"],
        3
    ),
    (
        "Who played the eccentric, supposedly insane helicopter pilot Captain H.M. 'Howling Mad' Murdock?",
        "Dwight Schultz",
        ["Dirk Benedict", "George Peppard", "Eddie Velez"],
        1
    ),
    (
        "Where did Murdock reside when not on missions with the A-Team?",
        "A Veterans Administration psychiatric hospital",
        ["A military prison stockade in Utah", "A private beach house in Malibu", "A monastery in northern California"],
        1
    ),
    (
        "What was the name of Murdock's imaginary canine friend in the psychiatric hospital?",
        "Billy",
        ["Sammy", "Buster", "Barney"],
        2
    ),
    (
        "Which newspaper reporter helped the A-Team during seasons 1 and 2?",
        "Amy Amanda Allen",
        ["Tawnia Baker", "Maggie Malone", "Christine Sullivan"],
        2
    ),
    (
        "Which actress played investigative reporter Amy Allen on The A-Team?",
        "Melinda Culea",
        ["Marla Heasley", "Stephanie Zimbalist", "Erin Gray"],
        3
    ),
    (
        "Why was actress Melinda Culea written off The A-Team during season 2?",
        "She pushed for her character to participate in action sequences and shoot weapons",
        ["She signed a film contract with Warner Bros.", "She had an off-screen feud with Mr. T", "The network mandated an all-male cast"],
        3
    ),
    (
        "Which ruthless military officer pursued the A-Team relentlessly through seasons 2, 3, and 4?",
        "Colonel Roderick Decker",
        ["Colonel Derryck Lynch", "General Hunt Stockwell", "Colonel Samuel Briggs"],
        2
    ),
    (
        "Which deep-voiced actor played the A-Team's nemesis Colonel Roderick Decker?",
        "Lance LeGault",
        ["William Lucking", "Robert Vaughn", "Charles Napier"],
        2
    ),
    (
        "What legendary Hollywood actor joined The A-Team in season 5 as General Hunt Stockwell?",
        "Robert Vaughn",
        ["David McCallum", "Robert Culp", "Patrick Macnee"],
        2
    ),
    (
        "Which special effects technician joined the A-Team in season 5 to help with undercover operations?",
        "Frankie 'Dishpan' Santana",
        ["Carlos 'Gadget' Mendez", "Tony 'Sparky' Rivera", "Manny 'Dynamite' Ortiz"],
        3
    ),
    (
        "Which actor played Frankie Santana in the final season of The A-Team?",
        "Eddie Velez",
        ["Jesse Borrego", "Paul Rodriguez", "Esai Morales"],
        3
    ),
    (
        "Who co-created The A-Team alongside Frank Lupo?",
        "Stephen J. Cannell",
        ["Donald P. Bellisario", "Glen A. Larson", "Steven Bochco"],
        3
    ),
    (
        "Which legendary TV theme composers wrote the triumphant brass-and-synthesizer theme for The A-Team?",
        "Mike Post and Pete Carpenter",
        ["Jan Hammer and Harold Faltermeyer", "Stu Phillips and Glen A. Larson", "Bill Conti and Jack Elliott"],
        2
    ),
    (
        "What distinct stylistic convention was famous in nearly every A-Team action sequence?",
        "Villains survived massive explosions and car flips without a single fatality",
        ["Every fight scene was filmed in slow motion", "Characters spoke directly to the camera during brawls", "All weapons fired paintballs instead of live ammunition"],
        1
    ),
    (
        "What brand of semi-automatic rifle with a stainless steel folding stock was the A-Team's weapon of choice?",
        "Ruger Mini-14",
        ["Colt AR-15", "Steyr AUG", "Heckler & Koch MP5"],
        2
    ),
    (
        "In the opening narration, in what year was the crack commando unit sent to prison for a crime they didn't commit?",
        "1972",
        ["1968", "1975", "1979"],
        3
    ),
    (
        "What was the fictional bank in Hanoi that the A-Team was ordered to rob, leading to their court-martial?",
        "The Bank of Hanoi",
        ["The Saigon National Treasury", "The French Indochina Vault", "The Tonkin Reserve"],
        3
    ),
    (
        "What disguise did Hannibal Smith regularly assume to vet potential clients seeking the A-Team's help?",
        "Mr. Lee, the Chinese laundry owner",
        ["Father O'Malley, the parish priest", "Professor Higgins, the botanist", "Captain Jack, the harbor fisherman"],
        2
    ),
    (
        "Which professional wrestling superstar guest-starred in two episodes of The A-Team as an old friend of B.A. Baracus?",
        "Hulk Hogan",
        ["Rowdy Roddy Piper", "Andre the Giant", "Randy Savage"],
        1
    ),
    (
        "Which singer and pop star guest-starred in the season 4 episode 'Cowboy George'?",
        "Boy George",
        ["Billy Idol", "Cyndi Lauper", "Adam Ant"],
        2
    ),
    (
        "What was the original broadcast network for The A-Team from 1983 to 1987?",
        "NBC",
        ["CBS", "ABC", "Fox"],
        1
    ),
    (
        "In which prime-time time slot did The A-Team dominate on Tuesday nights for NBC?",
        "8:00 PM Eastern",
        ["9:00 PM Eastern", "10:00 PM Eastern", "7:00 PM Eastern"],
        2
    ),
    (
        "What cereal featured Mr. T on the box following the massive popularity of The A-Team?",
        "Mr. T Cereal",
        ["A-Team Crunch", "Gold Chain Crisps", "Commando Flakes"],
        1
    ),
    (
        "Which actor played Dirk Benedict's character Starbuck in Battlestar Galactica before he was cast on The A-Team?",
        "Dirk Benedict himself",
        ["Richard Hatch", "Tim Dunigan", "George Peppard"],
        3
    ),
    (
        "In what season of The A-Team were the team members finally captured by the military and put on trial?",
        "Season 5",
        ["Season 3", "Season 4", "Season 2"],
        2
    ),
    (
        "What vehicle did Murdock frequently hotwire or commandeer during escapes?",
        "Military helicopters",
        ["Armored bank vans", "Speedboats", "Crop dusters"],
        1
    ),
    (
        "How many total episodes of The A-Team were produced across five seasons?",
        "98 episodes",
        ["112 episodes", "85 episodes", "124 episodes"],
        3
    ),

    # Magnum, P.I. - Textual / Plot / Characters / Vehicles
    (
        "Who starred as the Hawaiian private investigator Thomas Magnum on Magnum, P.I.?",
        "Tom Selleck",
        ["Lee Majors", "Robert Urich", "David Hasselhoff"],
        1
    ),
    (
        "What distinctive facial hair was Tom Selleck famous for sporting on Magnum, P.I.?",
        "A thick chevron mustache",
        ["A Van Dyke goatee", "Long sideburns", "A stubble five-o'clock shadow"],
        1
    ),
    (
        "What Major League Baseball team cap did Thomas Magnum wear in almost every episode?",
        "Detroit Tigers",
        ["Boston Red Sox", "New York Yankees", "Los Angeles Dodgers"],
        1
    ),
    (
        "What branch of the U.S. military did Thomas Magnum serve in before becoming a private investigator?",
        "U.S. Navy (SEAL and Naval Intelligence)",
        ["U.S. Marine Corps", "U.S. Army Special Forces", "U.S. Air Force Pararescue"],
        1
    ),
    (
        "What red exotic sports car did Thomas Magnum drive around Oahu?",
        "Ferrari 308 GTS",
        ["Porsche 911 Targa", "Ferrari Testarossa", "DeLorean DMC-12"],
        1
    ),
    (
        "What vanity license plate was on Robin Masters' red Ferrari driven by Magnum?",
        "ROBIN 1",
        ["MAGNUM", "ALOHA 1", "HAWAII 5"],
        1
    ),
    (
        "What was the name of Robin Masters' luxurious beachfront estate where Magnum lived in the guest house?",
        "Robin's Nest",
        ["Pahonu Manor", "Diamond Head Villa", "Waikiki Haven"],
        1
    ),
    (
        "Who played the stern, cultured British majordomo Jonathan Quayle Higgins III on Magnum, P.I.?",
        "John Hillerman",
        ["Edward Mulhare", "Bernard Fox", "David Hemmings"],
        1
    ),
    (
        "What state was actor John Hillerman actually born and raised in, despite his flawless British accent?",
        "Texas",
        ["Kansas", "Ohio", "New York"],
        2
    ),
    (
        "What breed of dogs were Zeus and Apollo, Higgins' highly trained guard dogs referred to as 'the lads'?",
        "Doberman Pinschers",
        ["Rottweilers", "German Shepherds", "Boxers"],
        1
    ),
    (
        "Who was the unseen, wealthy mystery novelist who owned the estate and allowed Magnum to stay for free?",
        "Robin Masters",
        ["Arthur Cabot", "Jonathan Vance", "Alistair Finch"],
        1
    ),
    (
        "Which cinema legend provided the booming, uncredited voice of Robin Masters in several early episodes?",
        "Orson Welles",
        ["John Huston", "Vincent Price", "James Earl Jones"],
        2
    ),
    (
        "What long-running fan theory regarding Robin Masters was teased and debated throughout the series?",
        "That Higgins was secretly Robin Masters all along",
        ["That Magnum was Robin Masters' illegitimate son", "That Robin Masters was an undercover CIA director", "That Robin Masters never existed and was an insurance scam"],
        2
    ),
    (
        "Who played Theodore 'T.C.' Calvin, Magnum's helicopter-pilot friend who ran Island Hoppers?",
        "Roger E. Mosley",
        ["Carl Weathers", "Taurean Blacque", "Meshach Taylor"],
        1
    ),
    (
        "What model of commercial helicopter with a colorful striped pattern did T.C. fly for Island Hoppers?",
        "Hughes 500D",
        ["Bell 206 JetRanger", "Aérospatiale Gazelle", "Sikorsky S-76"],
        2
    ),
    (
        "Who played Magnum's friend Orville Wilbur Richard 'Rick' Wright, manager of the King Kamehameha Club?",
        "Larry Manetti",
        ["Roger E. Mosley", "John Hillerman", "Jeff MacKay"],
        1
    ),
    (
        "What was the name of the exclusive private beach club managed by Rick Wright on Magnum, P.I.?",
        "The King Kamehameha Club",
        ["The Honolulu Surf Society", "The Pacific Yacht Haven", "The Aloha Palms Club"],
        2
    ),
    (
        "Who was Rick Wright's shadowy underworld father-figure and mob connection in Honolulu?",
        "Francis 'Icepick' Hofstetler",
        ["Big Mike Varner", "Sal Donatelli", "Lucky Luciano"],
        2
    ),
    (
        "Which veteran character actor played mob boss Francis 'Icepick' Hofstetler?",
        "Elisha Cook Jr.",
        ["Charles Durning", "Jack Elam", "Ray Walston"],
        3
    ),
    (
        "Who created Magnum, P.I. along with Glen A. Larson?",
        "Donald P. Bellisario",
        ["Stephen J. Cannell", "Steven Bochco", "Anthony Yerkovich"],
        2
    ),
    (
        "What iconic blockbuster movie role did Tom Selleck have to turn down because CBS refused to release him from Magnum?",
        "Indiana Jones in Raiders of the Lost Ark",
        ["John McClane in Die Hard", "Han Solo in The Empire Strikes Back", "Axel Foley in Beverly Hills Cop"],
        1
    ),
    (
        "Why could Tom Selleck have actually filmed Raiders of the Lost Ark despite the network's initial refusal?",
        "The Magnum pilot shooting was delayed by a writers' and actors' strike",
        ["Spielberg agreed to film Raiders on Oahu", "CBS bought the television broadcast rights to Raiders", "Lucasfilm paid off Selleck's CBS contract"],
        2
    ),
    (
        "In which year did Tom Selleck win the Primetime Emmy Award for Outstanding Lead Actor in a Drama Series?",
        "1984",
        ["1981", "1987", "1989"],
        2
    ),
    (
        "In which year did John Hillerman win the Primetime Emmy Award for Outstanding Supporting Actor in a Drama Series?",
        "1987",
        ["1983", "1985", "1989"],
        3
    ),
    (
        "Who composed the famous guitar-and-bass Magnum, P.I. theme that replaced the original jazz theme in mid-season 1?",
        "Mike Post and Pete Carpenter",
        ["Jan Hammer", "Lalo Schifrin", "Henry Mancini"],
        2
    ),
    (
        "What luxury watch did Thomas Magnum inherit from his father and wear throughout the series?",
        "Rolex Submariner / GMT-Master",
        ["Omega Speedmaster", "TAG Heuer Monaco", "Breitling Navitimer"],
        3
    ),
    (
        "What was the name of Magnum's naval intelligence buddy who constantly fed him classified information?",
        "Lieutenant 'Mac' MacReynolds",
        ["Commander Higgins", "Captain Maggie Poole", "Lieutenant Tanaka"],
        2
    ),
    (
        "Which actor played Lieutenant Mac MacReynolds, and later returned as look-alike con man Jim Bonnick?",
        "Jeff MacKay",
        ["Lance LeGault", "James Whitmore Jr.", "Glenn Cannon"],
        3
    ),
    (
        "How was Lieutenant Mac MacReynolds killed off in the season 3 episode 'Did You See the Sunrise?'?",
        "A car bomb meant for Magnum planted in the Ferrari",
        ["Shot by a sniper at the naval base", "Drowned in a scuba diving sabotage", "Killed in a helicopter sabotage"],
        2
    ),
    (
        "In the acclaimed episode 'Did You See the Sunrise?', which Soviet assassin did Magnum execute in cold blood?",
        "Ivan",
        ["Vassily", "Dmitri", "Boris"],
        2
    ),
    (
        "What cold, chilling line did Magnum speak before shooting Ivan in 'Did You See the Sunrise?'?",
        "Ivan, did you see the sunrise?",
        ["This is for Mac.", "No more games, Ivan.", "Welcome to America."],
        2
    ),
    (
        "What was the name of Magnum's beautiful French-Eurasian wife whom he believed was killed in Vietnam?",
        "Michelle Hue",
        ["Mai Ling", "Kieu Chinh", "Suzy Nakamura"],
        2
    ),
    (
        "Which actress played Magnum's lost love and wife Michelle Hue?",
        "Marta DuBois",
        ["Tia Carrere", "France Nuyen", "Kieu Chinh"],
        3
    ),
    (
        "What was the name of the daughter Magnum discovered he had fathered with Michelle?",
        "Lily Catherine",
        ["Chloe Marie", "Samantha Anne", "Victoria Lynn"],
        3
    ),
    (
        "What was the title of the season 7 finale where Magnum was shot, drifted in limbo as a ghost, and was meant to die?",
        "Limbo",
        ["Aloha, Magnum", "The Last Case", "Ghost of Hawaii"],
        2
    ),
    (
        "Why was Magnum, P.I. renewed for an eighth and final season after Magnum seemingly died in 'Limbo'?",
        "Overwhelming viewer outrage and fan letters protesting his death",
        ["A contract breach lawsuit by CBS shareholders", "Tom Selleck had a multi-million-dollar movie fail at the box office", "CBS had an empty Friday night time slot"],
        2
    ),
    (
        "In the final episode of Magnum, P.I. ('Resolutions'), what does Magnum decide to do with his life?",
        "Re-enlist in the U.S. Navy as a Commander to raise his daughter",
        ["Marry a wealthy heiress and buy Robin's Nest", "Open a detective agency in New York City", "Retire completely and become a professional surfer"],
        2
    ),
    (
        "Which television series shared a famous 1982 two-part crossover episode with Magnum, P.I.?",
        "Simon & Simon",
        ["The A-Team", "Knight Rider", "Murder, She Wrote"],
        2
    ),
    (
        "Which other long-running CBS mystery series featured a 1986 crossover where Jessica Fletcher visited Magnum on Oahu?",
        "Murder, She Wrote",
        ["Cagney & Lacey", "Remington Steele", "Crazy Like a Fox"],
        2
    ),
    (
        "Which actor played Honolulu police lieutenant Gordon Katsumoto in the 2018 reboot, and lieutenant Tanaka in the original series?",
        "Kwan Hi Lim played Tanaka in the original series",
        ["Clyde Kusatsu", "Mako", "George Takei"],
        3
    ),
    (
        "What was the real-life Hawaii location of the beachfront estate used for Robin's Nest?",
        "Pahonu in Waimanalo, Oahu",
        ["Kailua Beach Park", "Makaha Valley Ranch", "Sunset Beach Preserve"],
        3
    ),
    (
        "How many seasons did Magnum, P.I. broadcast on CBS between 1980 and 1988?",
        "8 seasons",
        ["6 seasons", "7 seasons", "9 seasons"],
        2
    ),
    (
        "Which famous pop song by John Denver was featured prominently in the series finale 'Resolutions'?",
        "Looking for Space",
        ["Annie's Song", "Take Me Home, Country Roads", "Rocky Mountain High"],
        3
    ),
    (
        "What branch of the service did Higgins claim to have served with during his extensive military career?",
        "British Army (Sergeant Major)",
        ["Royal Navy (Commander)", "Royal Air Force (Squadron Leader)", "Royal Marines (Captain)"],
        2
    ),
    (
        "What sport did Higgins regularly play and referee on the grounds of Robin's Nest?",
        "Polo and cricket",
        ["Tennis and golf", "Badminton and croquet", "Rugby and squash"],
        3
    ),
    (
        "Which actress guest-starred as a young singer in season 7 before starring in Star Trek: The Next Generation as Deanna Troi?",
        "Marina Sirtis",
        ["Gates McFadden", "Denise Crosby", "Terry Farrell"],
        3
    ),
    (
        "Which legendary Hollywood leading woman guest-starred in season 8 as an aging screen icon who hires Magnum?",
        "Phyllis Davis",
        ["Lauren Bacall", "Angela Lansbury", "Kim Novak"],
        3
    ),
    (
        "What was the name of the recurring Navy Commander who had feelings for Magnum, played by Jean Bruce Scott?",
        "Maggie Poole",
        ["Karen West", "Laura Holt", "Kate Sullivan"],
        3
    ),
    (
        "What water sport was Magnum passionate about, often paddling out in the early morning off the estate?",
        "Surf ski / surf paddleboard",
        ["Windsurfing", "Scuba diving", "Kite surfing"],
        2
    ),
    (
        "In the final scene of Magnum, P.I., what did Higgins confess to Magnum regarding Robin Masters?",
        "He told Magnum he lied earlier and wasn't Robin Masters, smiling as Magnum stared in disbelief",
        ["He admitted he was Robin Masters and signed over the deed", "He revealed Robin Masters had died years ago", "He confirmed Robin Masters was his twin brother"],
        2
    ),
    (
        "What was the title of the two-hour pilot episode of The A-Team that aired following Super Bowl XVII in January 1983?",
        "Mexican Slayride",
        ["The Los Angeles Underground", "A Crack Commando Unit", "Escape from Fort Bragg"],
        2
    ),
    (
        "In what fictional Mexican town did the A-Team rescue a captured journalist in the pilot episode 'Mexican Slayride'?",
        "San Carango",
        ["Santa Rosalia", "San Miguel", "Puerto Vallarta"],
        3
    ),
    (
        "What military maximum-security prison stockade did the A-Team escape from in 1972 according to show lore?",
        "Fort Bragg stockade",
        ["Fort Leavenworth", "Camp Pendleton", "Fort Dix"],
        3
    ),
    (
        "Which iconic 1960s TV Batman actor guest-starred in season 4 of The A-Team as a corrupt art dealer?",
        "Adam West",
        ["Burt Ward", "Cesar Romero", "Burgess Meredith"],
        2
    ),
    (
        "Which veteran actor played Colonel Derryck Lynch, the first military officer who pursued the A-Team in season 1?",
        "William Lucking",
        ["Lance LeGault", "Charles Napier", "Robert Vaughn"],
        3
    ),
    (
        "What brand of longneck bottled beer did Thomas Magnum obsessively drink on Magnum, P.I.?",
        "Old Dusseldorf",
        ["Lone Star", "Coors Banquet", "Primo Beer"],
        2
    ),
    (
        "What branch of the U.S. military did series creator Donald P. Bellisario serve in before creating Magnum, P.I. and JAG?",
        "U.S. Marine Corps",
        ["U.S. Navy", "U.S. Army", "U.S. Air Force"],
        2
    ),
    (
        "What was the name of Thomas Magnum's mother, who visited him in Hawaii in season 6?",
        "Katherine Magnum",
        ["Martha Magnum", "Dorothy Magnum", "Eleanor Magnum"],
        3
    ),
    (
        "Which veteran actress played Thomas Magnum's mother Katherine in several emotional episodes?",
        "Gwen Verdon",
        ["Barbara Rush", "Celeste Holm", "Jeanette Nolan"],
        3
    ),
    (
        "In what Hawaiian valley was the fictional Robin's Nest estate set according to dialogue in Magnum, P.I.?",
        "Kalama Valley / southeast Oahu",
        ["Waimea Valley", "Manoa Valley", "Hanakapiai Valley"],
        3
    )
]

if __name__ == "__main__":
    build_batch(questions, 5, "tools/staging/80s_tv_shows_batch5.json")
