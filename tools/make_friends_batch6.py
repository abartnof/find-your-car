#!/usr/bin/env python3
"""
Generate tools/staging/friends_batch6.json (100 questions, Metatextual: Awards, Directors, Writers, Theme Song).
"""
import sys
import os

from build_friends_batch import build_batch

questions = [
    {
        "q": "Which creative duo co-created Friends after developing the original concept in late 1993?",
        "correct": "David Crane and Marta Kauffman",
        "distractors": ["Chuck Lorre and Bill Prady", "Larry David and Jerry Seinfeld", "Steven Levitan and Christopher Lloyd"],
        "d": 1
    },
    {
        "q": "What university did co-creators David Crane and Marta Kauffman attend together as undergraduate students in the 1970s?",
        "correct": "Brandeis University",
        "distractors": ["New York University", "Columbia University", "Harvard University"],
        "d": 2
    },
    {
        "q": "What acclaimed adult cable comedy on HBO did David Crane and Marta Kauffman co-create prior to Friends?",
        "correct": "'Dream On'",
        "distractors": ["'The Larry Sanders Show'", "'Tales from the Crypt'", "'1st & Ten'"],
        "d": 2
    },
    {
        "q": "Who was the third key executive producer and primary director who partnered with Crane and Kauffman?",
        "correct": "Kevin S. Bright",
        "distractors": ["James Burrows", "Warren Littlefield", "David Nevins"],
        "d": 1
    },
    {
        "q": "What was the production company name formed by the three executive producers that produced Friends?",
        "correct": "Bright/Kauffman/Crane Productions",
        "distractors": ["Crane-Kauffman Television", "Bright Light Entertainment", "Manhattan Friends TV"],
        "d": 1
    },
    {
        "q": "What was the original working title used by Crane and Kauffman on their initial seven-page pitch treatment in December 1993?",
        "correct": "'Insomnia Cafe'",
        "distractors": ["'Across the Hall'", "'Six of One'", "'Friends Like Us'"],
        "d": 1
    },
    {
        "q": "Which of the following was also an early proposed working title before the network finalized 'Friends'?",
        "correct": "'Six of One'",
        "distractors": ["'Manhattan Brew'", "'The West Village Six'", "'Coffee and Companions'"],
        "d": 2
    },
    {
        "q": "What legendary television director helmed the Pilot episode and fifteen foundational episodes in the early seasons?",
        "correct": "James Burrows",
        "distractors": ["Michael Lembeck", "Kevin S. Bright", "Gail Mancuso"],
        "d": 1
    },
    {
        "q": "Where did director James Burrows take the six cast members in summer 1994, telling them it was their last shot at anonymity?",
        "correct": "Las Vegas, Nevada",
        "distractors": ["Cabo San Lucas, Mexico", "New York City", "Miami Beach, Florida"],
        "d": 1
    },
    {
        "q": "What American pop-rock duo recorded and performed the iconic theme song 'I'll Be There for You'?",
        "correct": "The Rembrandts",
        "distractors": ["Toad the Wet Sprocket", "The Goo Goo Dolls", "Gin Blossoms"],
        "d": 1
    },
    {
        "q": "Who were the two core members of The Rembrandts who sang 'I'll Be There for You'?",
        "correct": "Danny Wilde and Phil Solem",
        "distractors": ["Glen Phillips and Todd Nichols", "John Rzeznik and Robby Takac", "Robin Wilson and Jesse Valenzuela"],
        "d": 2
    },
    {
        "q": "Which celebrated songwriter co-wrote the lyrics to 'I'll Be There for You' along with Crane, Kauffman, and The Rembrandts?",
        "correct": "Allee Willis",
        "distractors": ["Diane Warren", "Carole King", "Cynthia Weil"],
        "d": 2
    },
    {
        "q": "Who composed the original musical theme for 'I'll Be There for You' and served as the show's music composer?",
        "correct": "Michael Skloff",
        "distractors": ["Mark Snow", "Mike Post", "Snuffy Walden"],
        "d": 2
    },
    {
        "q": "How many rapid rhythmic hand claps occur during the introductory chorus of 'I'll Be There for You'?",
        "correct": "Four claps",
        "distractors": ["Three claps", "Five claps", "Six claps"],
        "d": 1
    },
    {
        "q": "Who actually performed the four rhythmic hand claps during the recording of the theme song?",
        "correct": "The producers and composers (Crane, Kauffman, Bright, and Skloff)",
        "distractors": ["The six main actors in the studio", "Professional percussionists from the LA Philharmonic", "A machine drum synthesizer loop"],
        "d": 2
    },
    {
        "q": "Where did 'I'll Be There for You' peak on the Billboard Hot 100 Airplay chart in 1995?",
        "correct": "Number 1 (for eight consecutive weeks)",
        "distractors": ["Number 5", "Number 12", "Number 2"],
        "d": 2
    },
    {
        "q": "Where was the famous opening title sequence featuring the water fountain and umbrella sofa actually filmed?",
        "correct": "The Warner Bros. Ranch backlot in Burbank, California",
        "distractors": ["Central Park in New York City", "Prospect Park in Brooklyn", "Gramercy Park in Manhattan"],
        "d": 1
    },
    {
        "q": "At what time of day was the opening fountain title sequence filmed in chilly water?",
        "correct": "Around 4:00 AM",
        "distractors": ["Noon under bright sun", "At sunset around 7:00 PM", "At 10:00 AM after breakfast"],
        "d": 2
    },
    {
        "q": "In what year did Friends win the Primetime Emmy Award for Outstanding Comedy Series?",
        "correct": "2002 (for Season 8)",
        "distractors": ["1996 (for Season 2)", "1999 (for Season 5)", "2004 (for Season 10)"],
        "d": 1
    },
    {
        "q": "Which cast member was the first to win a Primetime Emmy Award for acting on the show, winning in 1998?",
        "correct": "Lisa Kudrow",
        "distractors": ["Jennifer Aniston", "David Schwimmer", "Matthew Perry"],
        "d": 1
    },
    {
        "q": "In which category did Lisa Kudrow win her Primetime Emmy Award in 1998?",
        "correct": "Outstanding Supporting Actress in a Comedy Series",
        "distractors": ["Outstanding Lead Actress in a Comedy Series", "Outstanding Guest Actress in a Comedy Series", "Outstanding Original Music and Lyrics"],
        "d": 1
    },
    {
        "q": "Which cast member won the Primetime Emmy Award for Outstanding Lead Actress in a Comedy Series in 2002?",
        "correct": "Jennifer Aniston",
        "distractors": ["Courteney Cox", "Lisa Kudrow", "Marlo Thomas"],
        "d": 1
    },
    {
        "q": "Which of the six main cast members was famously NEVER nominated for an acting Primetime Emmy Award for Friends?",
        "correct": "Courteney Cox",
        "distractors": ["Matthew Perry", "Matt LeBlanc", "David Schwimmer"],
        "d": 1
    },
    {
        "q": "How many Primetime Emmy Award nominations for Outstanding Lead Actor in a Comedy Series did Matt LeBlanc receive?",
        "correct": "Three nominations (2002, 2003, 2004)",
        "distractors": ["One nomination", "Five nominations", "Zero nominations"],
        "d": 2
    },
    {
        "q": "In what year was Matthew Perry nominated for a Primetime Emmy Award for Outstanding Lead Actor for playing Chandler?",
        "correct": "2002",
        "distractors": ["1996", "1999", "2004"],
        "d": 2
    },
    {
        "q": "Which actor earned a Primetime Emmy nomination in 1995 for Outstanding Supporting Actor in a Comedy Series?",
        "correct": "David Schwimmer",
        "distractors": ["Matthew Perry", "Matt LeBlanc", "Hank Azaria"],
        "d": 2
    },
    {
        "q": "Which Hollywood guest star won an Emmy for Outstanding Guest Actor in a Comedy Series in 2000 for playing Paul Stevens?",
        "correct": "Bruce Willis",
        "distractors": ["Brad Pitt", "Gary Oldman", "Danny DeVito"],
        "d": 1
    },
    {
        "q": "Which guest star won an Emmy Award for Outstanding Guest Actress in a Comedy Series in 2003 for playing Amy Green?",
        "correct": "Christina Applegate",
        "distractors": ["Reese Witherspoon", "Brooke Shields", "Susan Sarandon"],
        "d": 1
    },
    {
        "q": "Which director won the Primetime Emmy Award for Outstanding Directing for a Comedy Series for 'The One After the Superbowl'?",
        "correct": "Michael Lembeck",
        "distractors": ["James Burrows", "Kevin S. Bright", "David Schwimmer"],
        "d": 2
    },
    {
        "q": "How many episodes of Friends did cast member David Schwimmer personally direct during the series?",
        "correct": "10 episodes",
        "distractors": ["4 episodes", "16 episodes", "22 episodes"],
        "d": 1
    },
    {
        "q": "Which director directed the highest number of Friends episodes across the entire series (55 episodes)?",
        "correct": "Gary Halvorson",
        "distractors": ["Kevin S. Bright", "James Burrows", "Michael Lembeck"],
        "d": 2
    },
    {
        "q": "How many total episodes did executive producer Kevin S. Bright personally direct?",
        "correct": "54 episodes",
        "distractors": ["25 episodes", "38 episodes", "72 episodes"],
        "d": 2
    },
    {
        "q": "Who directed the emotional series finale 'The Last One' (Parts 1 & 2)?",
        "correct": "Kevin S. Bright",
        "distractors": ["James Burrows", "David Schwimmer", "Gary Halvorson"],
        "d": 1
    },
    {
        "q": "What Screen Actors Guild (SAG) Award did the entire ensemble cast win together in 1996?",
        "correct": "Outstanding Performance by an Ensemble in a Comedy Series",
        "distractors": ["SAG Lifetime Achievement Award", "Favorite Cast of the Decade Award", "Best Comedy Writing Ensemble"],
        "d": 1
    },
    {
        "q": "Which cast member won a Screen Actors Guild Award for Outstanding Performance by a Female Actor in a Comedy Series in 2000?",
        "correct": "Lisa Kudrow",
        "distractors": ["Jennifer Aniston", "Courteney Cox", "Teri Garr"],
        "d": 2
    },
    {
        "q": "Which cast member won the Golden Globe Award for Best Actress in a Television Series – Musical or Comedy in 2003?",
        "correct": "Jennifer Aniston",
        "distractors": ["Lisa Kudrow", "Courteney Cox", "Christina Applegate"],
        "d": 1
    },
    {
        "q": "How many times was Friends nominated for the Golden Globe for Best Television Series – Musical or Comedy?",
        "correct": "6 times",
        "distractors": ["2 times", "10 times", "Zero times"],
        "d": 2
    },
    {
        "q": "Which prolific female television director helmed 14 episodes of Friends including 'The One with Ross's Sandwich'?",
        "correct": "Gail Mancuso",
        "distractors": ["Pamela Fryman", "Bethany Rooney", "Mary Lou Belli"],
        "d": 2
    },
    {
        "q": "What award show presented Friends with the award for Favorite TV Comedy Series for five consecutive years from 2000 to 2004?",
        "correct": "The People's Choice Awards",
        "distractors": ["The TCA Awards", "The Critics' Choice Television Awards", "The TV Guide Awards"],
        "d": 2
    },
    {
        "q": "Who was the president of NBC Entertainment who championed and greenlit Friends in early 1994?",
        "correct": "Warren Littlefield",
        "distractors": ["Brandon Tartikoff", "Jeff Zucker", "Les Moonves"],
        "d": 2
    },
    {
        "q": "What Warner Bros. executive was instrumental in the production and syndication distribution of Friends?",
        "correct": "Peter Roth",
        "distractors": ["Barry Meyer", "Bob Daly", "Terry Semel"],
        "d": 3
    },
    {
        "q": "Which writer wrote the legendary bottle episode 'The One Where No One's Ready'?",
        "correct": "Ira Ungerleider",
        "distractors": ["David Crane", "Marta Kauffman", "Scott Silveri"],
        "d": 3
    },
    {
        "q": "Which writing duo penned the iconic Season 4 apartment trivia showdown 'The One with the Embryos'?",
        "correct": "Jill Condon and Amy Toomin",
        "distractors": ["David Crane and Marta Kauffman", "Scott Silveri and Shana Goldberg-Meehan", "Ted Cohen and Andrew Reich"],
        "d": 3
    },
    {
        "q": "Which longtime Friends writers became executive producers and co-showrunners in the later seasons?",
        "correct": "Scott Silveri and Shana Goldberg-Meehan",
        "distractors": ["Ted Cohen and Andrew Reich", "Adam Chase and Ira Ungerleider", "Greg Malins and Wil Calhoun"],
        "d": 2
    },
    {
        "q": "Who wrote the iconic Season 5 episode 'The One Where Everybody Finds Out'?",
        "correct": "Alexa Junge",
        "distractors": ["Marta Kauffman", "Greg Malins", "Scott Silveri"],
        "d": 2
    },
    {
        "q": "Which writer penned the emotional Season 2 episode 'The One with the Prom Video'?",
        "correct": "Alexa Junge",
        "distractors": ["David Crane", "Jeff Astrof", "Michael Borkow"],
        "d": 2
    },
    {
        "q": "Which writer created the famous running joke of Ross screaming 'We were on a break!' in Season 3?",
        "correct": "David Crane and Marta Kauffman",
        "distractors": ["Adam Chase", "Scott Silveri", "Jeff Greenstein"],
        "d": 2
    },
    {
        "q": "What television studio head at Warner Bros. Television initially negotiated the network deal with NBC?",
        "correct": "Leslie Moonves (then president of Warner Bros. Television)",
        "distractors": ["Peter Roth", "Garth Ancier", "Ted Harbert"],
        "d": 3
    },
    {
        "q": "What was the initial episode order NBC gave to Friends when picked up in May 1994?",
        "correct": "12 episodes plus the pilot",
        "distractors": ["6 episodes", "22 episodes", "Full 24-episode order"],
        "d": 2
    },
    {
        "q": "Which episode of Friends was the first one directed by David Schwimmer?",
        "correct": "\"The One on the Last Night\" (Season 6, Episode 6)",
        "distractors": ["\"The One with the Red Sweater\"", "\"The One with Rachel's Phone Number\"", "\"The One with the Truth About London\""],
        "d": 3
    },
    {
        "q": "What episode directed by David Schwimmer features Ross attempting to retrieve his red sweater in Season 8?",
        "correct": "\"The One with the Red Sweater\"",
        "distractors": ["\"The One After 'I Do'\"", "\"The One Where Rachel Tells...\"", "\"The One with the Videotape\""],
        "d": 2
    },
    {
        "q": "Which of these episodes was directed by David Schwimmer?",
        "correct": "\"The One with the Truth About London\"",
        "distractors": ["\"The One with the Prom Video\"", "\"The One Where No One's Ready\"", "\"The One with the Embryos\""],
        "d": 2
    },
    {
        "q": "How many total Primetime Emmy nominations did Friends receive for Outstanding Comedy Series?",
        "correct": "6 nominations",
        "distractors": ["10 nominations (every season)", "3 nominations", "8 nominations"],
        "d": 2
    },
    {
        "q": "Which HBO critical juggernaut defeated Friends for Outstanding Comedy Series at the 2001 Emmys?",
        "correct": "'Sex and the City'",
        "distractors": ["'Curb Your Enthusiasm'", "'The Sopranos'", "'The Larry Sanders Show'"],
        "d": 2
    },
    {
        "q": "Which NBC comedy rival defeated Friends for Outstanding Comedy Series multiple times in the late 1990s?",
        "correct": "'Frasier'",
        "distractors": ["'Seinfeld'", "'Will & Grace'", "'3rd Rock from the Sun'"],
        "d": 1
    },
    {
        "q": "How many consecutive Emmy wins for Outstanding Comedy Series did 'Frasier' win while competing with Friends?",
        "correct": "Five consecutive wins (1994–1998)",
        "distractors": ["Three consecutive wins", "Seven consecutive wins", "Two consecutive wins"],
        "d": 2
    },
    {
        "q": "Which fellow NBC Thursday night sitcom won Outstanding Comedy Series in 2000 over Friends?",
        "correct": "'Will & Grace'",
        "distractors": ["'Just Shoot Me!'", "'Scrubs'", "'NewsRadio'"],
        "d": 2
    },
    {
        "q": "What song by U2 was originally featured in the UK and European broadcast of Ross and Rachel's Season 2 prom video episode?",
        "correct": "\"With or Without You\"",
        "distractors": ["\"One\"", "\"Beautiful Day\"", "\"I Still Haven't Found What I'm Looking For\""],
        "d": 2
    },
    {
        "q": "What Chris Isaak song plays when Ross and Rachel share their planetarium date in Season 2?",
        "correct": "\"Wicked Game\"",
        "distractors": ["\"Somebody's Crying\"", "\"Baby Did a Bad Bad Thing\"", "\"Blue Hotel\""],
        "d": 2
    },
    {
        "q": "What Eric Clapton ballad plays during Chandler and Monica's engagement scene in Season 6?",
        "correct": "\"Wonderful Tonight\"",
        "distractors": ["\"Tears in Heaven\"", "\"Layla\"", "\"Change the World\""],
        "d": 1
    },
    {
        "q": "What Cyndi Lauper acoustic track plays at the conclusion of Monica and Chandler's wedding reception in Season 7?",
        "correct": "\"Time After Time\"",
        "distractors": ["\"True Colors\"", "\"Girls Just Want to Have Fun\"", "\"All Through the Night\""],
        "d": 2
    },
    {
        "q": "What British artist's song 'Trouble' plays over the somber montage at the end of the Season 7 premiere?",
        "correct": "Coldplay",
        "distractors": ["Radiohead", "Oasis", "The Verve"],
        "d": 2
    },
    {
        "q": "What rock band's song 'Semi-Charmed Life' is featured in the party background in Season 4?",
        "correct": "Third Eye Blind",
        "distractors": ["Smash Mouth", "Sugar Ray", "Matchbox 20"],
        "d": 3
    },
    {
        "q": "What Hootie & the Blowfish song is the subject of group concert tickets in Season 2?",
        "correct": "\"Hold My Hand\"",
        "distractors": ["\"Only Wanna Be with You\"", "\"Time\"", "\"Let Her Cry\""],
        "d": 2
    },
    {
        "q": "What Lionel Richie and Diana Ross duet do Ross and Phoebe sing while grieving in their apartments?",
        "correct": "\"Endless Love\"",
        "distractors": ["\"Truly\"", "\"Say You, Say Me\"", "\"Hello\""],
        "d": 2
    },
    {
        "q": "What Sir Mix-a-Lot rap song do Ross and Rachel sing to make baby Emma laugh for the first time?",
        "correct": "\"Baby Got Back\"",
        "distractors": ["\"Posse on Broadway\"", "\"Jump On It\"", "\"U Can't Touch This\""],
        "d": 1
    },
    {
        "q": "Who directed the two-part London episodes 'The One with Ross's Wedding' in Season 4?",
        "correct": "Michael Lembeck",
        "distractors": ["James Burrows", "Kevin S. Bright", "Gail Mancuso"],
        "d": 2
    },
    {
        "q": "Who directed the memorable Season 3 Thanksgiving football episode 'The One with the Football'?",
        "correct": "Michael Lembeck",
        "distractors": ["Kevin S. Bright", "James Burrows", "Peter Bonerz"],
        "d": 2
    },
    {
        "q": "Who directed 'The One with the Blackout' in Season 1?",
        "correct": "James Burrows",
        "distractors": ["Michael Lembeck", "Paul Lazarus", "Peter Bonerz"],
        "d": 2
    },
    {
        "q": "How many total Emmy nominations did director James Burrows receive specifically for directing episodes of Friends?",
        "correct": "Four nominations",
        "distractors": ["One nomination", "Eight nominations", "Ten nominations"],
        "d": 3
    },
    {
        "q": "In which category was Brad Pitt nominated for an Emmy Award for his guest appearance in Season 8?",
        "correct": "Outstanding Guest Actor in a Comedy Series",
        "distractors": ["Outstanding Supporting Actor in a Comedy Series", "Outstanding Lead Actor in a Comedy Series", "Outstanding Variety Performance"],
        "d": 1
    },
    {
        "q": "Which legendary comedic actor was nominated for an Emmy for guest starring as Dr. Richard Burke?",
        "correct": "Tom Selleck",
        "distractors": ["Elliott Gould", "Hank Azaria", "Gary Oldman"],
        "d": 1
    },
    {
        "q": "How many Emmy nominations for Outstanding Guest Actor did Hank Azaria receive for portraying David the Scientist Guy?",
        "correct": "Two nominations",
        "distractors": ["One nomination", "Three nominations", "Zero nominations"],
        "d": 3
    },
    {
        "q": "What British television comedy award did Friends win in 1999 for Best International Comedy Show?",
        "correct": "British Comedy Award",
        "distractors": ["BAFTA TV Award", "Royal Television Society Award", "National Television Award"],
        "d": 3
    },
    {
        "q": "How many Writers Guild of America (WGA) Award nominations did the writing staff of Friends receive?",
        "correct": "3 nominations",
        "distractors": ["10 nominations", "15 nominations", "Zero nominations"],
        "d": 3
    },
    {
        "q": "What prestigious recognition did the series receive from the American Film Institute (AFI) in 2002?",
        "correct": "AFI TV Program of the Year",
        "distractors": ["AFI Lifetime Achievement Award", "AFI Heritage Award", "AFI Top 10 International Series"],
        "d": 2
    },
    {
        "q": "Who wrote the series finale 'The Last One'?",
        "correct": "Marta Kauffman and David Crane",
        "distractors": ["Scott Silveri and Shana Goldberg-Meehan", "Ted Cohen and Andrew Reich", "Kevin S. Bright"],
        "d": 1
    },
    {
        "q": "Who composed the whimsical transitional guitar and acoustic musical stingers between scenes?",
        "correct": "Michael Skloff",
        "distractors": ["The Rembrandts", "Danny Elfman", "David Schwartz"],
        "d": 2
    },
    {
        "q": "What famous sound effect was created using a real human mouth to accompany scene cuts throughout the series?",
        "correct": "Scat vocal riffs and acoustic guitar strumming by Michael Skloff",
        "distractors": ["Snapping fingers", "A muted brass trumpet", "A slide whistle"],
        "d": 3
    },
    {
        "q": "Which editor won an American Cinema Editors (ACE Eddie) Award for editing 'The One with the Prom Video'?",
        "correct": "Andy Zall",
        "distractors": ["David Helfand", "Stephen Prime", "Janet Ashikaga"],
        "d": 3
    },
    {
        "q": "How many multi-camera setups were typically utilized to film an episode of Friends in front of the studio audience?",
        "correct": "Four cameras",
        "distractors": ["Two cameras", "Three cameras", "Six cameras"],
        "d": 2
    },
    {
        "q": "What production role did Lisa Kudrow's real-life husband Michel Stern work in?",
        "correct": "Advertising executive",
        "distractors": ["Television producer", "Cinematographer", "Talent manager"],
        "d": 3
    },
    {
        "q": "What costume designer was responsible for creating the iconic fashion wardrobes for Rachel, Monica, and Phoebe?",
        "correct": "Debra McGuire",
        "distractors": ["Patricia Field", "Mandi Line", "Janie Bryant"],
        "d": 2
    },
    {
        "q": "What set decorator was responsible for furnishing Monica's apartment and the Central Perk coffeehouse sets?",
        "correct": "Greg Grande",
        "distractors": ["John Shaffner", "Joe Stewart", "Thomas E. Azzari"],
        "d": 2
    },
    {
        "q": "Who was the primary production designer who conceived the layout of Monica's apartment and Central Perk?",
        "correct": "John Shaffner",
        "distractors": ["Greg Grande", "Roy Christopher", "Steve Olson"],
        "d": 2
    },
    {
        "q": "What distinct design rule did production designer John Shaffner break by painting Monica's apartment walls lilac purple?",
        "correct": "Producers initially opposed purple walls, but Shaffner argued it would make the show instantly identifiable when flipping channels",
        "distractors": ["Lilac was considered bad luck in theatrical tradition", "Purple absorbed too much studio lighting and required higher power", "The network mandated all comedy sets must be beige or cream"],
        "d": 2
    },
    {
        "q": "Where did set decorator Greg Grande originally find the famous burnt orange Central Perk velvet sofa?",
        "correct": "Stored in the basement of the Warner Bros. prop department",
        "distractors": ["At a flea market on Melrose Avenue", "In an antique thrift shop in Greenwich Village", "It was custom-built by an upholstery artisan in Burbank"],
        "d": 2
    },
    {
        "q": "What famous prop on Monica's purple door was originally a mirror that had its glass accidentally broken by a crew member?",
        "correct": "The yellow peephole picture frame",
        "distractors": ["The brass door knocker", "The chain latch", "The numbered apartment plaque"],
        "d": 1
    },
    {
        "q": "Why was the frame kept on the door after its mirror glass was shattered?",
        "correct": "Set decorator Greg Grande hung the empty frame around the peephole and loved how it looked",
        "distractors": ["The prop master forgot to order a replacement before taping", "Director James Burrows demanded it stay as a joke", "Jennifer Aniston requested it remain as a good luck charm"],
        "d": 2
    },
    {
        "q": "How long did a typical Friday night live studio audience taping of a Friends episode last?",
        "correct": "Around 5 to 6 hours",
        "distractors": ["Around 22 minutes", "Around 2 hours", "Around 8 to 10 hours"],
        "d": 2
    },
    {
        "q": "What live comedy warm-up comedian entertained the studio audience between scene takes for many seasons?",
        "correct": "Mark Cohen",
        "distractors": ["Brian Posehn", "Bill Burr", "Wayne Brady"],
        "d": 3
    },
    {
        "q": "What food was traditionally ordered and distributed to feed the studio audience during the long taping nights?",
        "correct": "Dozens of fresh delivery pizzas",
        "distractors": ["In-N-Out burgers", "Chinese takeout noodles", "Gourmet submarine sandwiches"],
        "d": 2
    },
    {
        "q": "Why were cliffhanger season finale endings (such as Ross saying Rachel's name) filmed without a studio audience?",
        "correct": "To maintain absolute plot secrecy and avoid leaks to the tabloids",
        "distractors": ["Because the sound stage was too small to fit the London set", "The cast was too nervous to perform the emotional beats in front of people", "Network regulations prohibited live audiences after midnight"],
        "d": 1
    },
    {
        "q": "What French title was given to Friends during its broadcast in France and French-speaking territories?",
        "correct": "Friends (retaining the English title)",
        "distractors": ["Les Amis", "Copains de Manhattan", "La Bande"],
        "d": 2
    },
    {
        "q": "What German title was given to Friends when broadcast in Germany and Austria?",
        "correct": "Friends (subtitled 'Freunde')",
        "distractors": ["Sechs in Manhattan", "Die Kumpel", "New Yorker Nächte"],
        "d": 3
    },
    {
        "q": "Which major television trade publication chronicled the weekly production and ratings data of Friends throughout the 1990s?",
        "correct": "Variety and The Hollywood Reporter",
        "distractors": ["Billboard and Rolling Stone", "Time and Newsweek", "Forbes and Fortune"],
        "d": 2
    },
    {
        "q": "What was the official name of the soundstage at Warner Bros. Studios where Friends was filmed from Season 2 through Season 10?",
        "correct": "Stage 24",
        "distractors": ["Stage 12", "Stage 18", "Stage 29"],
        "d": 1
    },
    {
        "q": "What ceremonial honor was bestowed upon Stage 24 by Warner Bros. immediately following the series finale wrap in 2004?",
        "correct": "It was officially renamed 'The Friends Stage'",
        "distractors": ["A bronze statue of the six actors was erected at the door", "The stage was permanently retired from television production", "A replica Central Perk was opened to the public inside"],
        "d": 1
    },
    {
        "q": "What was the only soundstage on the Warner Bros. lot previously renamed in honor of a single television production?",
        "correct": "Stage 11 was renamed 'The ER Stage' years later",
        "distractors": ["Stage 25 was renamed 'The Big Bang Theory Stage' years later", "Stage 14 was renamed 'The West Wing Stage'", "Stage 5 was renamed 'The Gilmore Girls Stage'"],
        "d": 3
    },
    {
        "q": "On what soundstage at Warner Bros. was Season 1 of Friends filmed before moving to Stage 24?",
        "correct": "Stage 5",
        "distractors": ["Stage 24", "Stage 12", "Stage 16"],
        "d": 3
    }
]

if __name__ == "__main__":
    out_path = os.path.join(os.path.dirname(__file__), "staging", "friends_batch6.json")
    build_batch(questions, out_path, batch_num=6)
