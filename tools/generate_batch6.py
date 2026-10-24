import sys
from make_batch import build_batch

# Batch 6: Dallas, Dynasty & Falcon Crest (Prime-Time Soap Operas & Cliffhangers)
# 100 questions: 30 d1, 40 d2, 30 d3

questions = [
    # Dallas - Textual / Plot / Characters
    (
        "Who played the ruthless oil baron J.R. Ewing on Dallas?",
        "Larry Hagman",
        ["Patrick Duffy", "Ken Kercheval", "Jim Davis"],
        1
    ),
    (
        "What was the name of the sprawling Texas ranch home of the Ewing family in Dallas?",
        "Southfork Ranch",
        ["Circle T Ranch", "Barrington Manor", "Ponderosa Ranch"],
        1
    ),
    (
        "What was the name of the independent oil company founded by Jock Ewing and fought over by his sons?",
        "Ewing Oil",
        ["Carrington Oil", "WestStar Oil", "Barnes Enterprises"],
        1
    ),
    (
        "Who played J.R.'s moral, upstanding younger brother Bobby Ewing?",
        "Patrick Duffy",
        ["Larry Hagman", "Steve Kanaly", "Ken Kercheval"],
        1
    ),
    (
        "Which actress played Bobby Ewing's wife Pamela Barnes Ewing, daughter of Digger Barnes?",
        "Victoria Principal",
        ["Linda Gray", "Charlene Tilton", "Donna Reed"],
        1
    ),
    (
        "Which actress portrayed J.R.'s long-suffering, alcoholic wife Sue Ellen Ewing?",
        "Linda Gray",
        ["Victoria Principal", "Priscilla Presley", "Mary Crosby"],
        1
    ),
    (
        "What title had Sue Ellen held prior to marrying J.R. Ewing?",
        "Miss Texas",
        ["Miss America", "Miss Dallas", "Miss Lone Star"],
        3
    ),
    (
        "Who played Miss Ellie Ewing, the matriarch of Southfork Ranch, for most of the series?",
        "Barbara Bel Geddes",
        ["Donna Reed", "Jane Wyman", "Alexis Smith"],
        1
    ),
    (
        "Which Oscar-winning actress temporarily replaced Barbara Bel Geddes as Miss Ellie during season 8?",
        "Donna Reed",
        ["Jane Wyman", "Lauren Bacall", "Olivia de Havilland"],
        3
    ),
    (
        "Which veteran actor played Ewing family patriarch Jock Ewing until his death in 1981?",
        "Jim Davis",
        ["Howard Keel", "John McIntire", "Denver Pyle"],
        2
    ),
    (
        "How was patriarch Jock Ewing written out of Dallas following actor Jim Davis's death?",
        "Killed in a helicopter crash while exploring oil fields in South America",
        ["Suffered a fatal heart attack at Southfork", "Died in an offshore drilling rig explosion", "Shot by a rival oil baron"],
        2
    ),
    (
        "Who was J.R. Ewing's neurotic, perpetually defeated rival at Barnes-Wentworth Oil?",
        "Cliff Barnes",
        ["Ray Krebbs", "Clayton Farlow", "Carter McKay"],
        1
    ),
    (
        "Which actor played Cliff Barnes in all 14 seasons of Dallas?",
        "Ken Kercheval",
        ["Steve Kanaly", "Patrick Duffy", "Howard Keel"],
        2
    ),
    (
        "What was the relationship between the Barnes and Ewing families intended to evoke?",
        "Romeo and Juliet (Hatfield and McCoy feuding families)",
        ["The Count of Monte Cristo", "The Great Gatsby", "War and Peace"],
        1
    ),
    (
        "What character was the Southfork ranch foreman, later revealed to be Jock Ewing's illegitimate son?",
        "Ray Krebbs",
        ["Mitch Cooper", "Jack Ewing", "Clayton Farlow"],
        2
    ),
    (
        "Which actor played ranch foreman Ray Krebbs throughout Dallas?",
        "Steve Kanaly",
        ["Ken Kercheval", "Howard Keel", "Morgan Woodward"],
        2
    ),
    (
        "What was the name of Lucy Ewing's character, J.R.'s petite niece played by Charlene Tilton?",
        "Lucy Ewing",
        ["Afton Cooper", "Kristin Shepard", "Jamie Ewing"],
        1
    ),
    (
        "What unflattering nickname did British broadcaster Terry Wogan coin for Charlene Tilton's character Lucy Ewing?",
        "The Poison Dwarf",
        ["The Pint-Sized Menace", "The Pocket Viper", "The Southfork Brat"],
        3
    ),
    (
        "In the epic March 1980 season 3 finale 'A House Divided', what global cliffhanger occurred?",
        "J.R. Ewing was shot twice by an unseen assailant in his office",
        ["Southfork Ranch burned to the ground", "Bobby Ewing was killed in an explosion", "Ewing Oil went bankrupt"],
        1
    ),
    (
        "On what date in November 1980 was the shooter of J.R. Ewing finally revealed in 'Who Done It?'?",
        "November 21, 1980",
        ["October 14, 1980", "December 25, 1980", "January 1, 1981"],
        3
    ),
    (
        "Who was revealed as the person who shot J.R. Ewing in 'Who Done It?'?",
        "Kristin Shepard (J.R.'s mistress and sister-in-law)",
        ["Sue Ellen Ewing", "Cliff Barnes", "Alan Beam"],
        1
    ),
    (
        "Which actress played Kristin Shepard, the shooter of J.R. Ewing, and was the daughter of singer Bing Crosby?",
        "Mary Crosby",
        ["Cathy Crosby", "Denise Crosby", "Kathryn Crosby"],
        2
    ),
    (
        "Approximately how many viewers in the United States watched the 'Who Done It?' episode revealing J.R.'s shooter?",
        "Over 83 million viewers",
        ["Roughly 45 million viewers", "Roughly 60 million viewers", "Over 120 million viewers"],
        2
    ),
    (
        "What market share did the 'Who Shot J.R.?' resolution episode achieve on CBS on November 21, 1980?",
        "76 share (53.3 Nielsen rating)",
        ["55 share (38.0 rating)", "92 share (68.0 rating)", "42 share (31.0 rating)"],
        3
    ),
    (
        "How was Bobby Ewing killed off at the end of season 8 in May 1985 when Patrick Duffy wanted to leave?",
        "Run down by a speeding car driven by Katherine Wentworth",
        ["Shot in the chest by J.R. in an argument", "Trapped in a burning oil well blowout", "Plane crash en route to Houston"],
        2
    ),
    (
        "How was Bobby Ewing's death completely retconned in the famous season 9 finale in May 1986?",
        "Pamela woke up and found Bobby showering, revealing the entire season was her dream",
        ["Bobby was revealed to have been in a CIA coma under an alias", "Bobby had an evil identical twin who died instead", "A cloned synthetic replica had been killed"],
        1
    ),
    (
        "What were Bobby Ewing's famous first words when Pamela opened the shower door in the season 9 finale?",
        "Good morning",
        ["Surprise, honey", "Did you miss me?", "I'm back"],
        1
    ),
    (
        "Which actress played Jenna Wade, Bobby's former girlfriend who was played by Priscilla Presley from 1983 to 1988?",
        "Priscilla Presley",
        ["Morgan Fairchild", "Francine Tacker", "Victoria Principal"],
        3
    ),
    (
        "Which legendary musical theater star played oilman Clayton Farlow, who married Miss Ellie?",
        "Howard Keel",
        ["Gordon MacRae", "John Raitt", "Robert Goulet"],
        2
    ),
    (
        "What was J.R. Ewing's drink of choice throughout Dallas?",
        "Bourbon and branch water",
        ["Scotch on the rocks", "Gin and tonic", "Dry martini with olives"],
        2
    ),
    (
        "Who created the prime-time soap opera Dallas for CBS?",
        "David Jacobs",
        ["Richard Shapiro", "Aaron Spelling", "Earl Hamner Jr."],
        2
    ),
    (
        "Which successful spin-off drama was also created by David Jacobs, focusing on Gary and Valene Ewing in California?",
        "Knots Landing",
        ["Falcon Crest", "Dynasty", "Hotel"],
        1
    ),
    (
        "How many total seasons did Dallas air in its original CBS run (1978-1991)?",
        "14 seasons",
        ["10 seasons", "12 seasons", "16 seasons"],
        2
    ),
    (
        "What real-life estate near Plano, Texas served as the famous exterior for Southfork Ranch?",
        "Duncan Acres / Southfork Ranch in Parker, Texas",
        ["King Ranch in Kingsville", "Waggoner Ranch in Vernon", "Y.O. Ranch in Mountain Home"],
        3
    ),
    (
        "What award did Larry Hagman earn multiple Emmy nominations for playing J.R. Ewing without ever winning?",
        "Primetime Emmy for Outstanding Lead Actor in a Drama Series",
        ["Golden Globe for Best Actor", "People's Choice Award", "Screen Actors Guild Award"],
        2
    ),

    # Dynasty - Textual / Plot / Characters
    (
        "Who played the suave Denver oil tycoon Blake Carrington on Dynasty?",
        "John Forsythe",
        ["Rock Hudson", "Larry Hagman", "Charlton Heston"],
        1
    ),
    (
        "Which actress played Blake's kind-hearted, blonde former-secretary wife Krystle Carrington?",
        "Linda Evans",
        ["Joan Collins", "Pamela Sue Martin", "Heather Locklear"],
        1
    ),
    (
        "Which British actress joined Dynasty in season 2 as the scheming, glamorous Alexis Carrington Colby?",
        "Joan Collins",
        ["Linda Evans", "Stephanie Beacham", "Jane Wyman"],
        1
    ),
    (
        "What was the name of Blake Carrington's Denver-based global oil conglomerate?",
        "Denver-Carrington",
        ["ColbyCo", "Ewing Oil", "Rocky Mountain Energy"],
        1
    ),
    (
        "What rival corporation was operated by Alexis Carrington Colby to destroy Blake?",
        "ColbyCo",
        ["Denver-Carrington", "Ewing Global", "Tuscany Enterprises"],
        2
    ),
    (
        "What trademark physical confrontation became a recurring signature between Krystle and Alexis on Dynasty?",
        "Vicious slap-fights and brawls in water fountains and lily ponds",
        ["Western-style gun duels at high noon", "Karate kickboxing matches", "Sword duels with antique rapiers"],
        1
    ),
    (
        "Which actress played Blake and Alexis's rebellious older daughter Fallon Carrington in seasons 1 through 4?",
        "Pamela Sue Martin",
        ["Emma Samms", "Heather Locklear", "Catherine Oxenberg"],
        2
    ),
    (
        "Which British actress took over the role of Fallon Carrington starting in season 6 of Dynasty and on The Colbys?",
        "Emma Samms",
        ["Pamela Sue Martin", "Stephanie Beacham", "Tracy Scoggins"],
        2
    ),
    (
        "Which character was one of network television's first openly gay/bisexual regular lead characters on Dynasty?",
        "Steven Carrington",
        ["Adam Carrington", "Jeff Colby", "Prince Michael"],
        1
    ),
    (
        "Which actor originally portrayed Steven Carrington in seasons 1 and 2 before Jack Coleman replaced him?",
        "Al Corley",
        ["Jack Coleman", "John James", "Gordon Thomson"],
        3
    ),
    (
        "How did Dynasty explain Steven Carrington's change in physical appearance when Jack Coleman took over?",
        "Extensive plastic surgery following an offshore oil rig explosion in the Java Sea",
        ["Facial burns suffered in a skiing accident in Aspen", "Experimental gene therapy in Switzerland", "He wore a silicon disguise for three episodes"],
        2
    ),
    (
        "Which actress played Krystle's scheming niece Sammy Jo, who married Steven Carrington?",
        "Heather Locklear",
        ["Catherine Oxenberg", "Pamela Bellwood", "Terri Garber"],
        1
    ),
    (
        "What other hit 1980s Aaron Spelling show was Heather Locklear starring on while simultaneously filming Dynasty?",
        "T.J. Hooker",
        ["The Love Boat", "Charlie's Angels", "Beverly Hills, 90210"],
        2
    ),
    (
        "What was the name of the ruthless long-lost oldest Carrington son who poisoned Jeff Colby with toxic paint?",
        "Adam Carrington",
        ["Steven Carrington", "Clay Fallon", "Miles Colby"],
        2
    ),
    (
        "Which actor played the devious Adam Carrington on Dynasty?",
        "Gordon Thomson",
        ["John James", "Michael Nader", "Dack Rambo"],
        3
    ),
    (
        "Who played the dashing, athletic Jeff Colby, who repeatedly married Fallon Carrington?",
        "John James",
        ["Michael Nader", "Gordon Thomson", "Ted McGinley"],
        2
    ),
    (
        "Who played Alexis's charming Hungarian playboy husband Dex Dexter starting in season 4?",
        "Michael Nader",
        ["Christopher Cazenove", "Rock Hudson", "Maxwell Caulfield"],
        2
    ),
    (
        "What devastating cliffhanger ended Dynasty's season 5 in May 1985?",
        "The Moldavian Massacre (terrorists machine-gunned Amanda's royal wedding)",
        ["Southfork Manor was bombed by foreign mercenaries", "The Carrington mansion collapsed into an underground mine", "Alexis and Krystle drove off a cliff into the ocean"],
        1
    ),
    (
        "Whose royal wedding to Prince Michael of Moldavia was the target of the Moldavian Massacre?",
        "Amanda Carrington",
        ["Fallon Carrington", "Sammy Jo Carrington", "Kirby Anders"],
        2
    ),
    (
        "Which European royal and actress played Amanda Carrington during the Moldavian Massacre?",
        "Catherine Oxenberg (daughter of Princess Elizabeth of Yugoslavia)",
        ["Emma Samms", "Stephanie Beacham", "Maryam d'Abo"],
        3
    ),
    (
        "Despite dozens of guests and main characters being gunned down, how many regular characters died in the Moldavian Massacre?",
        "Only two minor characters (Luke Fuller and Lady Ashley Mitchell)",
        ["Every main character except Blake survived", "Half of the main cast members were killed off", "None died; all bullets were tranquilizers"],
        2
    ),
    (
        "Which screen icon made his final acting appearance on Dynasty in 1985 as Krystle's lover Daniel Reece?",
        "Rock Hudson",
        ["Cary Grant", "Burt Lancaster", "Kirk Douglas"],
        2
    ),
    (
        "What public health panic arose in 1985 following Rock Hudson's romantic on-screen kiss with Linda Evans on Dynasty?",
        "Misinformation and fear about AIDS transmission through kissing",
        ["Hepatitis outbreaks on television production stages", "Strict union guidelines requiring plastic shields during love scenes", "A national boycott of nighttime soap operas"],
        2
    ),
    (
        "Who created Dynasty alongside her husband Richard Shapiro?",
        "Esther Shapiro",
        ["Susan Harris", "Linda Bloodworth-Thomason", "Diane English"],
        3
    ),
    (
        "Which prolific television producer executive produced Dynasty for ABC?",
        "Aaron Spelling",
        ["Stephen J. Cannell", "Glen A. Larson", "Steven Bochco"],
        1
    ),
    (
        "Who composed the regal, fanfare-heavy instrumental theme song for Dynasty?",
        "Bill Conti",
        ["Mike Post", "Jan Hammer", "John Williams"],
        2
    ),
    (
        "What ratings milestone did Dynasty achieve in the 1984-1985 Nielsen season?",
        "Hit Number 1 in all of U.S. prime-time television, dethroning Dallas",
        ["Drew the highest rating for any sitcom finale", "Became the first show with 100 million weekly viewers", "Swept all top 10 positions in sweeps month"],
        2
    ),
    (
        "Which actress played Dominique Deveraux, Blake's wealthy African-American half-sister and nightclub singer?",
        "Diahann Carroll",
        ["Eartha Kitt", "Leslie Uggams", "Pam Grier"],
        2
    ),
    (
        "What lavish spin-off series followed the Colby family to Los Angeles in 1985?",
        "The Colbys",
        ["Dynasty: The Next Generation", "California Carringtons", "Pacific Dynasty"],
        1
    ),
    (
        "Which legendary Oscar-winning actor starred as patriarch Jason Colby on The Colbys?",
        "Charlton Heston",
        ["Gregory Peck", "Kirk Douglas", "Burt Lancaster"],
        2
    ),
    (
        "What bizarre science-fiction event happened to Fallon Carrington in the final episode of The Colbys?",
        "She was abducted by an alien UFO in the desert",
        ["She traveled back in time to the 1920s", "She discovered she was an android replica", "She was struck by a meteor and gained clairvoyance"],
        2
    ),

    # Falcon Crest - Textual / Plot / Characters
    (
        "Who played the ruthless, iron-fisted winery matriarch Angela Channing on Falcon Crest?",
        "Jane Wyman",
        ["Barbara Bel Geddes", "Joan Collins", "Alexis Smith"],
        1
    ),
    (
        "What notable historical connection did actress Jane Wyman have to U.S. presidential history?",
        "She was the first wife of President Ronald Reagan",
        ["She was the daughter of President Herbert Hoover", "She was married to President Gerald Ford's brother", "She was the godmother of George H.W. Bush"],
        2
    ),
    (
        "In what fictional California wine region was Falcon Crest set?",
        "Tuscany Valley",
        ["Napa Ridge", "Sonoma Hills", "Chardonnay Valley"],
        2
    ),
    (
        "What agricultural empire did Angela Channing ruthlessly fight to control on Falcon Crest?",
        "Falcon Crest winery and vineyards",
        ["Tuscany Cattle Ranch", "Napa Valley Citrus Orchards", "Pacific Timber Mills"],
        1
    ),
    (
        "Who was Angela Channing's upright nephew who arrived from New York after inheriting 50 acres of the vineyard?",
        "Chase Gioberti",
        ["Richard Channing", "Lance Cumson", "Cole Gioberti"],
        2
    ),
    (
        "Which actor played Chase Gioberti in the first six seasons of Falcon Crest?",
        "Robert Foxworth",
        ["David Selby", "Lorenzo Lamas", "William Moses"],
        2
    ),
    (
        "Who played Angela Channing's handsome, irresponsible playboy grandson and henchman Lance Cumson?",
        "Lorenzo Lamas",
        ["William Moses", "Billy Moses", "John James"],
        1
    ),
    (
        "Who was Lorenzo Lamas's famous real-life mother, who also guest-starred on Falcon Crest as Francesca Gioberti?",
        "Arlene Dahl",
        ["Esther Williams", "Lana Turner", "Rita Hayworth"],
        3
    ),
    (
        "Which Hollywood glamour queen guest-starred in season 1 as Jacqueline Perrault, Chase's European mother?",
        "Lana Turner",
        ["Lauren Bacall", "Ava Gardner", "Rita Hayworth"],
        3
    ),
    (
        "Who was Angela's illegitimate half-brother / son and ruthless newspaper owner Richard Channing?",
        "David Selby",
        ["Robert Foxworth", "Simon MacCorkindale", "Rod Taylor"],
        2
    ),
    (
        "Which actress played Maggie Gioberti, Chase's freelance-writer wife, who drowned in a pool in season 9?",
        "Susan Sullivan",
        ["Ana Alicia", "Margaret Ladd", "Abby Dalton"],
        2
    ),
    (
        "Which actress played the passionate, manipulative Melissa Agretti on Falcon Crest?",
        "Ana Alicia",
        ["Laura Johnson", "Kristian Alfonso", "Apollonia Kotero"],
        2
    ),
    (
        "Who created Falcon Crest, drawing on his own rural background after creating The Waltons?",
        "Earl Hamner Jr.",
        ["David Jacobs", "Richard Shapiro", "Aaron Spelling"],
        2
    ),
    (
        "What night of the week and lead-in show gave Falcon Crest its massive ratings success for CBS?",
        "Friday nights at 10:00 PM, airing immediately after Dallas",
        ["Thursday nights at 9:00 PM after Magnum, P.I.", "Sunday nights at 10:00 PM after Murder, She Wrote", "Wednesday nights at 9:00 PM after Dynasty"],
        1
    ),
    (
        "What real-life Napa Valley stone winery served as the grand Victorian mansion exterior for Falcon Crest?",
        "Spring Mountain Vineyard in St. Helena, California",
        ["Robert Mondavi Winery", "Beringer Vineyards", "Inglenook Estate"],
        3
    ),
    (
        "Who composed the dramatic, sweeping classical theme music for Falcon Crest?",
        "Bill Conti",
        ["Mike Post", "Jan Hammer", "Lalo Schifrin"],
        3
    ),
    (
        "What was the name of Angela Channing's mentally unstable daughter who murdered her father in season 1?",
        "Emma Channing",
        ["Julia Cumson", "Terry Hartford", "Vickie Gioberti"],
        3
    ),
    (
        "Which actress played the eccentric, poetry-writing Emma Channing on Falcon Crest?",
        "Margaret Ladd",
        ["Abby Dalton", "Susan Sullivan", "Ana Alicia"],
        3
    ),
    (
        "Which daughter of Angela was revealed to be a nun turned serial murderer in the dramatic season 2 cliffhanger?",
        "Julia Cumson",
        ["Emma Channing", "Francesca Gioberti", "Melissa Agretti"],
        3
    ),
    (
        "Which actress portrayed Angela's troubled daughter Julia Cumson?",
        "Abby Dalton",
        ["Margaret Ladd", "Susan Sullivan", "Laura Johnson"],
        3
    ),
    (
        "What natural disaster struck the Tuscany Valley in the climactic season 3 cliffhanger of Falcon Crest?",
        "A devastating earthquake",
        ["A catastrophic vineyard fire", "A massive flood and dam collapse", "A volcanic eruption"],
        2
    ),
    (
        "How many seasons did Falcon Crest air on CBS between 1981 and 1990?",
        "9 seasons",
        ["7 seasons", "8 seasons", "11 seasons"],
        2
    ),
    (
        "In the final episode of Falcon Crest in 1990, what was Angela Channing's closing toast to the vineyard?",
        "A toast to Falcon Crest and family endurance: 'A toast to you, Falcon Crest, and may you live forever'",
        ["'To the land, which forgives all sins'", "'May the wine never turn to vinegar'", "'To the grapes of tomorrow'"],
        3
    ),
    (
        "Which Australian actor played the rugged vineyard manager Peter Stavros who married Angela in season 5?",
        "Cesar Romero",
        ["Rod Taylor", "Michael York", "David Hedison"],
        3
    ),
    (
        "Which suave 1960s Joker actor played billionaire Greek industrialist Peter Stavros's cousin on Falcon Crest?",
        "Cesar Romero played Peter Stavros himself",
        ["Burgess Meredith", "Frank Gorshin", "Vincent Price"],
        3
    ),
    (
        "What vehicle explosion marked the shocking cliffhanger of season 5 of Falcon Crest?",
        "An explosion in a Tuscany Valley mansion that trapped the entire family",
        ["A helicopter crash into the San Francisco Bay", "A limousine bombing carrying Angela and Chase", "A yacht explosion off Catalina"],
        3
    ),
    (
        "Which pop star and Prince protegee guest-starred in season 5 as singer Sophia Wayne?",
        "Apollonia Kotero",
        ["Sheila E.", "Vanity", "Wendy Melvoin"],
        3
    ),
    (
        "What major health issue kept star Jane Wyman absent for most of the final season of Falcon Crest?",
        "Severe diabetes and respiratory complications",
        ["A fractured hip requiring multiple surgeries", "A vocal paralysis disorder", "A broken collarbone from a horse riding stunt"],
        3
    ),
    (
        "What was the name of the Italian restaurant and hotel that was a frequent gathering spot in the Tuscany Valley?",
        "Del Oro Spa and Resort",
        ["Tuscany Inn", "The Gioberti Tavern", "Villa Miraflores"],
        3
    ),
    (
        "What network broadcast all nine seasons of Falcon Crest from 1981 to 1990?",
        "CBS",
        ["NBC", "ABC", "Fox"],
        1
    ),
    (
        "In the final episode of Dallas ('Conundrum'), which supernatural guide played by Joel Grey visits J.R. to show him what Ewing lives would be without him?",
        "Adam",
        ["Lucifer", "Gabriel", "Clarence"],
        3
    ),
    (
        "What was the name of the loyal Ewing Oil secretary who worked for J.R. Ewing across all 14 seasons, played by Deborah Rennard?",
        "Sly Lovegren",
        ["Phyllis Wapner", "Louella Caraway", "Connie Brasher"],
        3
    ),
    (
        "In the ninth and final season of Dynasty, what shocking mystery was uncovered at the bottom of the lake on the Carrington estate?",
        "The skeletal body of Roger Grimes",
        ["A crate of stolen European diamonds", "An unexploded wartime naval mine", "Blake's father's original handwritten will"],
        3
    ),
    (
        "What was the name of the influential metropolitan daily newspaper owned and published by Richard Channing on Falcon Crest?",
        "The San Francisco Globe",
        ["The Daily Chronicle", "The Bay Area Post", "The California Sun"],
        3
    )
]

if __name__ == "__main__":
    build_batch(questions, 6, "tools/staging/80s_tv_shows_batch6.json")
