import sys
from make_batch import build_batch

# Batch 1: Cheers & Night Court (Sitcom Giants: Boston bar & Manhattan night courtroom)
# 100 questions: 30 d1, 40 d2, 30 d3

questions = [
    # Cheers - Textual / Character / Plot
    (
        "Who was the former Boston Red Sox relief pitcher and owner of the bar in Cheers?",
        "Sam Malone",
        ["Cliff Clavin", "Woody Boyd", "Frasier Crane"],
        1
    ),
    (
        "What was Sam Malone's baseball nickname during his pitching days on Cheers?",
        "Mayday",
        ["Bullseye", "Rocket", "Slapshot"],
        1
    ),
    (
        "Which graduate student walked into Cheers in the pilot episode and became a cocktail waitress after her fiancé abandoned her?",
        "Diane Chambers",
        ["Rebecca Howe", "Carla Tortelli", "Lilith Sternin"],
        1
    ),
    (
        "What was the title of the acclaimed 1982 pilot episode of Cheers?",
        "Give Me a Ring Sometime",
        ["Where Everybody Knows Your Name", "Sam's Women", "The Tortelli Affair"],
        2
    ),
    (
        "What was the name of Diane Chambers' professor fiancé who abandoned her in the Cheers pilot?",
        "Sumner Sloane",
        ["Derek Drake", "Robin Colcord", "Simon Finch-Royce"],
        2
    ),
    (
        "Which actor played the beloved, absent-minded former coach Ernie Pantusso on Cheers until his death in 1985?",
        "Nicholas Colasanto",
        ["Woody Harrelson", "George Wendt", "John Ratzenberger"],
        1
    ),
    (
        "What was Ernie Pantusso's coaching specialty before working at Cheers?",
        "Baseball coach",
        ["Boxing trainer", "Football coach", "Basketball coach"],
        1
    ),
    (
        "What Indiana hometown did farm boy Woody Boyd hail from when he arrived at Cheers?",
        "Hanover",
        ["Terre Haute", "Pawnee", "South Bend"],
        2
    ),
    (
        "What greeting did the patrons of Cheers shout in unison whenever George Wendt's character entered?",
        "Norm!",
        ["Sammy!", "Cliffie!", "Coach!"],
        1
    ),
    (
        "What was the name of Norm Peterson's wife on Cheers, who was rarely seen on screen?",
        "Vera",
        ["Esther", "Loretta", "Kelly"],
        1
    ),
    (
        "What was Cliff Clavin's day job on Cheers?",
        "U.S. Postal Service mail carrier",
        ["Transit bus driver", "IRS auditor", "Plumbing contractor"],
        1
    ),
    (
        "On which game show did Cliff Clavin famously compete and lose all his money in Final Jeopardy?",
        "Jeopardy!",
        ["Wheel of Fortune", "The Price Is Right", "Family Feud"],
        1
    ),
    (
        "What was Cliff Clavin's infamous Final Jeopardy category that led to his downfall on Cheers?",
        "Celebrities Who've Never Been in My Kitchen",
        ["Postal Codes of Western Europe", "Famous Postage Stamps", "U.S. Presidents' Dogs"],
        2
    ),
    (
        "Which actress played the sharp-tongued, superstitious waitress Carla Tortelli on Cheers?",
        "Rhea Perlman",
        ["Shelley Long", "Kirstie Alley", "Bebe Neuwirth"],
        1
    ),
    (
        "What was the name of Carla's hockey-player husband who was killed by a Zamboni in season 8?",
        "Eddie LeBec",
        ["Nick Tortelli", "Ludlow Fowler", "Benny Kelly"],
        2
    ),
    (
        "Which actor played the superstitious French-Canadian goalie Eddie LeBec on Cheers?",
        "Jay Thomas",
        ["Dan Hedaya", "Tom Berenger", "Harry Anderson"],
        2
    ),
    (
        "Who replaced Diane Chambers as the manager of Cheers starting in season 6?",
        "Rebecca Howe",
        ["Lilith Sternin", "Kelly Gaines", "Maggie O'Keefe"],
        1
    ),
    (
        "Which actress joined Cheers in season 6 as corporate manager Rebecca Howe?",
        "Kirstie Alley",
        ["Kim Cattrall", "JoBeth Williams", "Heather Locklear"],
        1
    ),
    (
        "What British corporate executive did Rebecca Howe obsessively pursue during seasons 6 through 8 of Cheers?",
        "Robin Colcord",
        ["Evan Drake", "Julian Crane", "Charles Winchester"],
        2
    ),
    (
        "Which Tony-winning Welsh-born actor played tycoon Robin Colcord on Cheers?",
        "Roger Rees",
        ["John Cleese", "Timothy Dalton", "Ian McKellen"],
        2
    ),
    (
        "Which psychiatrist character was introduced in season 3 of Cheers as Diane's fiancé before becoming a bar regular?",
        "Frasier Crane",
        ["Niles Crane", "Lilith Sternin", "Simon Finch-Royce"],
        1
    ),
    (
        "Which actress played Frasier Crane's stern, analytical psychiatrist wife Dr. Lilith Sternin?",
        "Bebe Neuwirth",
        ["Jane Leeves", "Peri Gilpin", "Judith Light"],
        1
    ),
    (
        "What was the name of the upscale seafood restaurant located directly above Cheers?",
        "Melville's",
        ["The Hampshire House", "The Ritz Tavern", "Captain's Catch"],
        2
    ),
    (
        "Who was the snooty, abrasive owner of Melville's restaurant who frequently feuded with Sam Malone?",
        "John Allen Hill",
        ["Robin Colcord", "Sumner Sloane", "Gary of Olde Towne Tavern"],
        3
    ),
    (
        "Which rival Boston drinking establishment constantly engaged in pranks and competitions with Cheers in the 'Bar Wars' episodes?",
        "Gary's Olde Towne Tavern",
        ["McNally's Irish Pub", "The Bull & Finch", "The King's Arms"],
        2
    ),
    (
        "Who sang the iconic Cheers theme song 'Where Everybody Knows Your Name'?",
        "Gary Portnoy",
        ["Randy Newman", "BJ Thomas", "Kenny Loggins"],
        2
    ),
    (
        "Who co-wrote the lyrics and music for the Cheers theme song with Gary Portnoy?",
        "Judy Hart Angelo",
        ["Alan Thicke", "Mike Post", "Allee Willis"],
        3
    ),
    (
        "Where did Cheers finish in the Nielsen ratings for its first season (1982-1983)?",
        "74th out of 77 prime-time programs",
        ["45th out of 77 prime-time programs", "12th out of 77 prime-time programs", "Last place out of 102 programs"],
        2
    ),
    (
        "Which NBC entertainment president championed Cheers and kept it on the air despite dismal first-season ratings?",
        "Brandon Tartikoff",
        ["Fred Silverman", "Grant Tinker", "Warren Littlefield"],
        2
    ),
    (
        "How many Primetime Emmy Awards did Cheers win across its 11-season run?",
        "28",
        ["14", "37", "42"],
        2
    ),
    (
        "Who was the only actor to receive an Emmy nomination in all 11 seasons of Cheers?",
        "Ted Danson",
        ["Rhea Perlman", "George Wendt", "Kelsey Grammer"],
        2
    ),
    (
        "At the end of which season did Shelley Long depart Cheers to pursue a film career?",
        "Season 5",
        ["Season 3", "Season 4", "Season 6"],
        2
    ),
    (
        "In the season 5 finale of Cheers, what career aspiration prompted Diane Chambers to leave Boston?",
        "Finishing her novel in Los Angeles",
        ["Joining a ballet company in New York", "Accepting a professorship at Oxford", "Attending law school at Harvard"],
        2
    ),
    (
        "What was the name of Woody Boyd's naive, wealthy socialite wife on Cheers?",
        "Kelly Gaines",
        ["Candi Pearson", "Corinne Flavin", "Amanda Swafford"],
        2
    ),
    (
        "Which actress played Woody Boyd's sweetheart and eventual wife Kelly Gaines on Cheers?",
        "Jackie Swanson",
        ["Amy Yasbeck", "Virginia Madsen", "Lori Loughlin"],
        3
    ),
    (
        "What real-life Boston establishment served as the exterior location for Cheers?",
        "The Bull & Finch Pub",
        ["The Black Rose", "The Green Dragon Tavern", "Bell in Hand Tavern"],
        1
    ),
    (
        "What was the name of Carla's smarmy ex-husband, played by Dan Hedaya on Cheers?",
        "Nick Tortelli",
        ["Vinnie Tortelli", "Gino Tortelli", "Tony Tortelli"],
        2
    ),
    (
        "Which short-lived 1987 NBC spin-off centered on Carla's ex-husband and his blonde trophy wife Loretta?",
        "The Tortellis",
        ["Nick's Place", "Boston Legal", "The Vegas Life"],
        2
    ),
    (
        "Which veteran actress played Cliff Clavin's overbearing mother, Esther Clavin, on Cheers?",
        "Frances Sternhagen",
        ["Marion Ross", "Audrey Meadows", "Doris Roberts"],
        2
    ),
    (
        "What was the name of Frasier Crane and Lilith Sternin's son born during season 8 of Cheers?",
        "Frederick",
        ["Martin", "David", "Niles"],
        2
    ),
    (
        "Which Monty Python member won an Emmy for Outstanding Guest Performer on Cheers playing Dr. Simon Finch-Royce?",
        "John Cleese",
        ["Eric Idle", "Michael Palin", "Terry Gilliam"],
        2
    ),
    (
        "What trio created and executive produced Cheers for Charles/Burrows/Charles Productions?",
        "Glen Charles, Les Charles, and James Burrows",
        ["David Angell, Peter Casey, and David Lee", "Garry Marshall, Jerry Belson, and Bob Brunner", "Susan Harris, Paul Junger Witt, and Tony Thomas"],
        3
    ),
    (
        "Before creating Cheers, Glen Charles, Les Charles, and James Burrows all worked extensively on which hit comedy series?",
        "Taxi",
        ["M*A*S*H", "The Bob Newhart Show", "WKRP in Cincinnati"],
        3
    ),
    (
        "Which real-life Boston politician made a famous cameo on Cheers in the season 2 episode 'Someone Single in Mayfair'?",
        "Tip O'Neill",
        ["Ted Kennedy", "Michael Dukakis", "Ray Flynn"],
        2
    ),
    (
        "What was Norm Peterson's profession on Cheers when he was actually working?",
        "Accountant",
        ["Architect", "Stockbroker", "Insurance salesman"],
        1
    ),
    (
        "What breed of dog was the painting that Norm gave to Sam in the Cheers episode 'Paint Your Office'?",
        "Dogs playing poker",
        ["A Golden Retriever fetching a ball", "A Basset Hound wearing glasses", "A Bulldog sitting at a desk"],
        3
    ),
    (
        "In the season 1 finale of Cheers, what former baseball rival arrived at the bar, prompting Sam to admit his alcoholism?",
        "Kevin Dyson",
        ["Rick Walker", "Glenn Miller", "Dave Richards"],
        3
    ),
    (
        "Which actor originally auditioned for the role of Sam Malone alongside Shelley Long before Ted Danson was cast?",
        "Fred Dryer",
        ["Tom Selleck", "Patrick Duffy", "Robert Urich"],
        3
    ),
    (
        "What was the final line spoken by Sam Malone in the 1993 series finale of Cheers?",
        "Sorry, we're closed.",
        ["Have a good night, Boston.", "Here's to the good times.", "Norm, pay your tab."],
        1
    ),
    (
        "How many times did Rhea Perlman win the Primetime Emmy Award for Outstanding Supporting Actress in a Comedy Series for Cheers?",
        "4",
        ["2", "6", "1"],
        3
    ),

    # Night Court - Textual / Character / Plot
    (
        "Who was the quirky, young magic-loving judge appointed to Manhattan Criminal Court, Part 9, on Night Court?",
        "Harry T. Stone",
        ["Dan Fielding", "Bull Shannon", "Mac Robinson"],
        1
    ),
    (
        "Which comedian and magician starred as Judge Harry T. Stone on Night Court?",
        "Harry Anderson",
        ["John Larroquette", "Richard Moll", "Charles Robinson"],
        1
    ),
    (
        "What jazz singer and crooner was Judge Harry Stone completely obsessed with on Night Court?",
        "Mel Tormé",
        ["Frank Sinatra", "Tony Bennett", "Perry Como"],
        1
    ),
    (
        "What was the name of the narcissistic, sex-obsessed prosecutor on Night Court?",
        "Dan Fielding",
        ["Phil Sanders", "Buddy Ryan", "Vincent Daniels"],
        1
    ),
    (
        "Which actor won four consecutive Primetime Emmy Awards for his portrayal of Dan Fielding on Night Court?",
        "John Larroquette",
        ["Harry Anderson", "Richard Moll", "Charles Robinson"],
        1
    ),
    (
        "Why was John Larroquette not nominated for an Emmy for Night Court in 1989 after four straight wins?",
        "He requested that his name not be submitted for consideration",
        ["He left the series for a feature film", "The academy banned consecutive nominations", "The series was temporarily canceled"],
        2
    ),
    (
        "What was Dan Fielding's embarrassing real first name on Night Court, which he kept secret?",
        "Reinhold",
        ["Mortimer", "Aloysius", "Cornelius"],
        2
    ),
    (
        "What was Dan Fielding's impoverished southern home state that he tried to hide?",
        "Louisiana",
        ["Alabama", "Mississippi", "Arkansas"],
        3
    ),
    (
        "What was the canonical first name of the towering bailiff Bull Shannon on Night Court?",
        "Nostradamus",
        ["Bartholomew", "Barnaby", "Napoleon"],
        2
    ),
    (
        "Which 6-foot-8 actor played the bald, good-hearted bailiff Bull Shannon on Night Court?",
        "Richard Moll",
        ["Ted Cassidy", "Carel Struycken", "Kevin Peter Hall"],
        1
    ),
    (
        "Which actress played the idealistic public defender Christine Sullivan starting in season 3 of Night Court?",
        "Markie Post",
        ["Ellen Foley", "Paula Kelly", "Marsha Warfield"],
        1
    ),
    (
        "Before Markie Post joined the cast permanently, who played public defender Billie Young in season 2 of Night Court?",
        "Ellen Foley",
        ["Paula Kelly", "Gail Strickland", "Karen Austin"],
        3
    ),
    (
        "Which actress played public defender Liz Donnelly during the first season of Night Court?",
        "Paula Kelly",
        ["Marsha Warfield", "Denice Kumagai", "Florence Halop"],
        3
    ),
    (
        "Which actor played the sensible, Vietnam-veteran court clerk Mac Robinson on Night Court?",
        "Charles Robinson",
        ["Richard Moll", "Terry Kiser", "William Utay"],
        1
    ),
    (
        "What was court clerk Mac Robinson's full first name on Night Court?",
        "Mackenzie",
        ["Malcolm", "Marcus", "Maurice"],
        3
    ),
    (
        "Which actress played Quon Le Duc Robinson, Mac's Vietnamese bride on Night Court?",
        "Denice Kumagai",
        ["Ming-Na Wen", "Tia Carrere", "Lauren Tom"],
        2
    ),
    (
        "Which raspy-voiced actress and former comedy writer played bailiff Selma Hacker in seasons 1 and 2 of Night Court?",
        "Selma Diamond",
        ["Florence Halop", "Marsha Warfield", "Marion Lorne"],
        2
    ),
    (
        "Following Selma Diamond's death, which veteran actress took over as bailiff Florence Kleiner for season 3?",
        "Florence Halop",
        ["Alice Ghostley", "Ruth Gordon", "Estelle Getty"],
        3
    ),
    (
        "After the tragic deaths of two cast members, which stand-up comedian joined Night Court in season 4 as bailiff Roz Russell?",
        "Marsha Warfield",
        ["Wanda Sykes", "Whoopi Goldberg", "Kym Whitley"],
        1
    ),
    (
        "What was bailiff Roz Russell's full first name on Night Court?",
        "Rosalind",
        ["Rosemary", "Rochelle", "Roxanne"],
        3
    ),
    (
        "Who created the comedy series Night Court for NBC?",
        "Reinhold Weege",
        ["Gary David Goldberg", "James L. Brooks", "Steven Bochco"],
        3
    ),
    (
        "Before creating Night Court, on which classic 1970s police sitcom did Reinhold Weege serve as writer and producer?",
        "Barney Miller",
        ["The Odd Couple", "Police Story", "All in the Family"],
        3
    ),
    (
        "How old was Harry Stone when he was appointed judge in the pilot episode of Night Court?",
        "34",
        ["28", "39", "42"],
        3
    ),
    (
        "Why was Harry Stone appointed as a criminal court judge on the last day of the mayor's term?",
        "He was at the bottom of the list and all other candidates were unavailable",
        ["He won a mayoral raffle contest", "He was the mayor's secret illegitimate son", "He saved the mayor from a mugging"],
        2
    ),
    (
        "Which pair of eccentric hillbilly squatters made frequent recurring appearances before Judge Harry Stone on Night Court?",
        "Bob and June Wheeler",
        ["Clem and Daisy Duke", "Otis and Mayberry Smith", "Zeke and Martha Higgins"],
        2
    ),
    (
        "Which actor, famous for playing Bob Wheeler on Night Court, later gained worldwide sci-fi fame as Data on Star Trek: TNG?",
        "Brent Spiner",
        ["Jonathan Frakes", "LeVar Burton", "Michael Dorn"],
        1
    ),
    (
        "What iconic musical instrument leads the driving funk rhythm of the Night Court theme song?",
        "Slap bass",
        ["Synthesizer keyboard", "Electric organ", "Harmonica"],
        1
    ),
    (
        "Which acclaimed jazz saxophonist played the blistering alto saxophone solos on the Night Court theme?",
        "Ernie Watts",
        ["David Sanborn", "Clarence Clemons", "Wayne Shorter"],
        3
    ),
    (
        "Who composed the memorable theme music for Night Court?",
        "Jack Elliott",
        ["Mike Post", "Jan Hammer", "Stu Gardner"],
        3
    ),
    (
        "Which iconic jazz singer made actual guest appearances on Night Court as Harry Stone's guardian angel / musical idol?",
        "Mel Tormé",
        ["Chet Baker", "Tony Bennett", "Cab Calloway"],
        2
    ),
    (
        "Which veteran Addams Family actor played Harry Stone's eccentric, globetrotting biological father, Buddy Ryan, on Night Court?",
        "John Astin",
        ["Jackie Coogan", "Ted Cassidy", "Al Lewis"],
        2
    ),
    (
        "What was Buddy Ryan's signature catchphrase on Night Court whenever discussing his stays in mental hospitals?",
        "But I'm feeling much better now!",
        ["And that was just Tuesday!", "Never trust the orderly!", "Good thing I had my spoon!"],
        2
    ),
    (
        "Which actor played Dan Fielding's homeless sycophant Phil Sanders, and later Phil's evil twin brother Will?",
        "William Utay",
        ["Terry Kiser", "Mike Finneran", "Ray Walston"],
        3
    ),
    (
        "How was Dan Fielding's sycophantic lackey Phil Sanders killed off on Night Court?",
        "Crushed by a falling piano",
        ["Fell down an open elevator shaft", "Eaten by an alligator in the sewers", "Struck by lightning while golfing"],
        2
    ),
    (
        "In the final season of Night Court, Bull Shannon is beamed aboard an alien spaceship because the aliens need what?",
        "Someone tall to reach the top shelves",
        ["A human with no hair for energy", "A courtroom judge for planetary disputes", "A gentle heart to fuel their engine"],
        3
    ),
    (
        "What was the recurring character Harry the Hat's primary specialty when appearing on Cheers before Night Court debuted?",
        "Con games and bar bets",
        ["Selling stolen jewelry", "Phony stock tips", "Card counting"],
        2
    ),
    (
        "How many seasons did Night Court air on NBC between 1984 and 1992?",
        "9",
        ["7", "8", "11"],
        3
    ),
    (
        "In what prime-time slot did Night Court typically air during NBC's dominant mid-1980s Thursday lineup?",
        "9:30 PM (following Cheers)",
        ["8:00 PM (opening the night)", "8:30 PM (following The Cosby Show)", "10:00 PM (closing the night)"],
        2
    ),
    (
        "What four hit comedies formed NBC's legendary fall 1984 Thursday night comedy juggernaut?",
        "The Cosby Show, Family Ties, Cheers, Night Court",
        ["Diff'rent Strokes, Silver Spoons, Cheers, Night Court", "Taxi, Cheers, Night Court, Hill Street Blues", "The Facts of Life, Cheers, Family Ties, Night Court"],
        2
    ),
    (
        "Which recurring Night Court character was an inept court maintenance man and handyman played by Mike Finneran?",
        "Art Hendricks",
        ["Phil Sanders", "Al Craven", "Gino Maretti"],
        3
    ),
    (
        "What prop did Judge Harry Stone frequently carry or use in court to defuse tense arguments?",
        "Magic handcuffs or trick gags",
        ["A baseball bat", "A wooden whistle", "A bullhorn"],
        2
    ),
    (
        "Which actor played district attorney Vincent Daniels, Dan Fielding's perpetually irritated boss on Night Court?",
        "Daniel Frishman",
        ["Bumper Robinson", "John Randolph", "Jason Bernard"],
        3
    ),
    (
        "What actress played Dan Fielding's sister Donna, who visited from Louisiana and surprised him with her southern accent?",
        "Elayne Boosler",
        ["Delta Burke", "Dixie Carter", "Annie Potts"],
        3
    ),
    (
        "What did Judge Harry Stone keep behind the secret door in his chambers on Night Court?",
        "A billiard pool table",
        ["A bowling lane", "A wine cellar", "A soundproof drum kit"],
        2
    ),
    (
        "What was Dan Fielding's official title in the courtroom throughout most of Night Court?",
        "Assistant District Attorney",
        ["Public Defender", "Senior Bailiff", "Court Stenographer"],
        1
    ),
    (
        "What prestigious theatrical award did John Larroquette win in 2011 for How to Succeed in Business Without Really Trying?",
        "Tony Award for Best Featured Actor in a Musical",
        ["Drama Desk Award for Lead Actor", "Olivier Award for Musical Performance", "Pulitzer Prize for Drama"],
        3
    ),
    (
        "Which episode of Night Court featured Michael J. Fox as an angry teenage delinquent named Eddie Simms before Family Ties took off?",
        "Santa Goes Pop (season 1)",
        ["The Eye of the Beholder", "Some Like It Hot", "Welcome Back, Momma"],
        3
    ),
    (
        "What stuffed animal did Dan Fielding win at a carnival that became a recurring source of emotional attachment in season 5?",
        "A giant stuffed gorilla",
        ["A pink teddy bear", "A giant stuffed flamingo", "A stuffed bulldog"],
        3
    ),
    (
        "Which veteran actress voiced the talking computer system introduced into the courtroom in Night Court's season 8 episode 'A Guy Named Darryl'?",
        "Majel Barrett",
        ["June Foray", "Lucille Bliss", "Bea Arthur"],
        3
    ),
    (
        "What network broadcast both Cheers and Night Court as part of its Thursday night powerhouse in the 1980s?",
        "NBC",
        ["CBS", "ABC", "Fox"],
        1
    )
]

if __name__ == "__main__":
    build_batch(questions, 1, "tools/staging/80s_tv_shows_batch1.json")
