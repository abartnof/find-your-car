import sys
from make_batch import build_batch

# Batch 9: MacGyver, Murder She Wrote, 21 Jump Street & The Wonder Years (Icons of Craft, Mystery & Youth)
# 100 questions: 30 d1, 40 d2, 30 d3

questions = [
    # MacGyver - Textual / Plot / Gadgets / Characters
    (
        "Who played the resourceful, gun-eschewing secret agent Angus MacGyver on MacGyver?",
        "Richard Dean Anderson",
        ["Bruce McGill", "Michael Des Barres", "Dana Elcar"],
        1
    ),
    (
        "What brand of multi-tool pocketknife did MacGyver carry in almost every single episode?",
        "Swiss Army Knife (Victorinox)",
        ["Leatherman Wave", "Buck Hunting Knife", "Gerber Multi-Plier"],
        1
    ),
    (
        "What common adhesive material was MacGyver's most famous improvised problem-solving tool?",
        "Duct tape",
        ["Electrical tape", "Gorilla tape", "Masking tape"],
        1
    ),
    (
        "What non-profit think tank and government contractor employed MacGyver from season 2 onward?",
        "The Phoenix Foundation",
        ["The Vanguard Institute", "The Faraday Council", "The Horizon Corporation"],
        1
    ),
    (
        "Who played Peter Thornton, MacGyver's loyal director and closest friend at the Phoenix Foundation?",
        "Dana Elcar",
        ["John Anderson", "Bruce McGill", "Michael Des Barres"],
        1
    ),
    (
        "What real-life medical condition did actor Dana Elcar develop that was written into Peter Thornton's storyline?",
        "Glaucoma resulting in blindness",
        ["Parkinson's disease", "Multiple sclerosis", "Coronary artery disease"],
        2
    ),
    (
        "Why did MacGyver strictly refuse to carry or use a handgun?",
        "A childhood revolver accident accidentally killed his close friend Jesse",
        ["He swore a pacifist vow as a Buddhist monk", "He was court-martialed for firing on civilians", "He failed the government firearms exam"],
        1
    ),
    (
        "What was MacGyver's first name, which remained a closely guarded secret until season 7?",
        "Angus",
        ["Archibald", "Aloysius", "Atticus"],
        1
    ),
    (
        "Who was MacGyver's arch-nemesis, an unkillable master of disguise who worked for the assassination syndicate HIT?",
        "Murdoc",
        ["Jack Dalton", "Pete Thornton", "Harry Jackson"],
        3
    ),
    (
        "Which British rock singer and actor played the theatrical assassin Murdoc on MacGyver?",
        "Michael Des Barres",
        ["Bruce McGill", "Roger Daltrey", "John Glover"],
        2
    ),
    (
        "What was Murdoc's trademark death cry whenever he seemingly plunged into an explosion or ravine?",
        "MACGYVEEER!",
        ["I will be back!", "Curse you, MacGyver!", "Never again!"],
        1
    ),
    (
        "Who played Jack Dalton, MacGyver's bumbling aviator friend who twitched his eye when lying?",
        "Bruce McGill",
        ["Dana Elcar", "John Anderson", "Michael Des Barres"],
        2
    ),
    (
        "Which future Desperate Housewives star played MacGyver's ditzy, aspiring-actress friend Penny Parker?",
        "Teri Hatcher",
        ["Felicity Huffman", "Marcia Cross", "Nicollette Sheridan"],
        2
    ),
    (
        "Which iconic 1970s TV star co-executive produced MacGyver through Winkler/Rich Productions?",
        "Henry Winkler (The Fonz)",
        ["Ron Howard", "Tom Selleck", "Garry Marshall"],
        2
    ),
    (
        "Who created the action-adventure series MacGyver?",
        "Lee David Zlotoff",
        ["Stephen J. Cannell", "Glen A. Larson", "Steven Bochco"],
        3
    ),
    (
        "Who composed the iconic, driving brass-and-synthesizer theme music for MacGyver?",
        "Randy Edelman",
        ["Mike Post", "Jan Hammer", "John Addison"],
        2
    ),
    (
        "What household food item did MacGyver use in the pilot episode to plug a sulfuric acid leak?",
        "Chocolate candy bars (sugars react with the acid to form a carbon plug)",
        ["Peanut butter", "Mashed potatoes", "Baking flour"],
        2
    ),
    (
        "What sport did MacGyver play in college, occasionally coaching youth teams on the series?",
        "Ice hockey",
        ["Baseball", "Basketball", "Soccer"],
        2
    ),
    (
        "Who played Harry Jackson, MacGyver's crusty, beloved grandfather who lived in Minnesota?",
        "John Anderson",
        ["Denver Pyle", "Will Geer", "Jack Elam"],
        3
    ),
    (
        "How was MacGyver's grandfather Harry Jackson killed off in season 5?",
        "Suffered a fatal heart attack during an attack by Murdoc",
        ["Shot by a foreign sniper in Minneapolis", "Died peacefully in his cabin bed", "Killed in an explosion at a lumber yard"],
        3
    ),
    (
        "In the final season, what son did MacGyver discover he had fathered with his past love Ellen?",
        "Sean Angus Malloy (S.A.M.)",
        ["Jack Dalton Jr.", "David Thornton", "Michael Jackson"],
        3
    ),
    (
        "Which actor played MacGyver's adult son Sean Malloy in the series finale?",
        "Dirk Blocker",
        ["Ricky Paull Goldin", "Jason Priestley", "Brian Austin Green"],
        3
    ),
    (
        "What network broadcast MacGyver on Monday nights from 1985 to 1992?",
        "ABC",
        ["NBC", "CBS", "Fox"],
        1
    ),
    (
        "What popular dictionary verb was officially added to Oxford and Merriam-Webster inspired by MacGyver?",
        "To MacGyver (to make or repair in an improvised or inventive way)",
        ["To Phoenix", "To Zlotoff", "To Swiss-army"],
        3
    ),
    (
        "In what season 7 time-travel dream episode was MacGyver's first name 'Angus' finally revealed?",
        "Good Knight MacGyver",
        ["The Stringer", "Deadly Silents", "Gunz 'N' Boyz"],
        3
    ),

    # Murder, She Wrote - Textual / Plot / Characters
    (
        "Who starred as the mystery novelist and amateur sleuth Jessica Fletcher on Murder, She Wrote?",
        "Angela Lansbury",
        ["Bea Arthur", "Barbara Bel Geddes", "Jane Wyman"],
        1
    ),
    (
        "What was the name of the fictional, murder-prone Maine coastal town where Jessica Fletcher resided?",
        "Cabot Cove",
        ["Rockport Harbor", "Camden Bay", "Kennebunkport"],
        1
    ),
    (
        "What pen name did Jessica Beatrice Fletcher use on her bestselling mystery novels?",
        "J.B. Fletcher",
        ["J.F. Cabot", "BJ Fletcher", "Jessica Lansbury"],
        3
    ),
    (
        "What was Jessica Fletcher's primary mode of transportation around Cabot Cove during the early seasons?",
        "A black English three-speed bicycle",
        ["A red Volkswagen Beetle", "A wood-paneled station wagon", "A yellow motor scooter"],
        1
    ),
    (
        "What tool did Jessica Fletcher use to write all her novels until finally buying a computer in season 8?",
        "A manual Royal typewriter",
        ["An electric IBM Selectric", "Handwritten legal pads", "A voice dictaphone tape recorder"],
        3
    ),
    (
        "Who played the bumbling Cabot Cove sheriff Amos Tupper in seasons 1 through 4?",
        "Tom Bosley",
        ["Ron Masak", "William Windom", "Claude Akins"],
        1
    ),
    (
        "What iconic 1970s sitcom had Tom Bosley starred on before joining Murder, She Wrote?",
        "Happy Days (as Howard Cunningham)",
        ["The Brady Bunch", "All in the Family", "Sanford and Son"],
        1
    ),
    (
        "Who replaced Amos Tupper as the Cabot Cove sheriff, playing former NYPD officer Mort Metzger?",
        "Ron Masak",
        ["Tom Bosley", "William Windom", "Ken Swofford"],
        2
    ),
    (
        "Which veteran actor played Dr. Seth Hazlitt, the curmudgeonly Cabot Cove physician and Jessica's best friend?",
        "William Windom",
        ["Tom Bosley", "Ron Masak", "Arthur Hill"],
        1
    ),
    (
        "What was the name of Jessica's hapless accountant nephew who was repeatedly framed for murder?",
        "Grady Fletcher",
        ["Johnny Fletcher", "Michael Fletcher", "Tommy Fletcher"],
        2
    ),
    (
        "Which actor played Jessica's perennial murder-suspect nephew Grady Fletcher?",
        "Michael Horton",
        ["Keith Andes", "Richard Paul", "Bruce Jenner"],
        3
    ),
    (
        "What historic Emmy Awards record does Angela Lansbury hold for Murder, She Wrote?",
        "Nominated 12 consecutive times for Lead Actress in a Drama without ever winning",
        ["Most Emmy wins for a senior actress", "Only actress to win for acting and directing in the same year", "Most consecutive guest-star Emmy wins"],
        1
    ),
    (
        "On which television network did Murder, She Wrote anchor Sunday nights at 8:00 PM for over a decade?",
        "CBS",
        ["NBC", "ABC", "Fox"],
        1
    ),
    (
        "Who co-created Murder, She Wrote after previously creating Columbo and Ellery Queen?",
        "Richard Levinson, William Link, and Peter S. Fischer",
        ["Steven Bochco and Terry Louise Fisher", "Stephen J. Cannell and Frank Lupo", "Donald P. Bellisario and Glen A. Larson"],
        2
    ),
    (
        "What real-life northern California coastal town was used for exterior shots of Cabot Cove, Maine?",
        "Mendocino, California",
        ["Carmel-by-the-Sea", "Bodega Bay", "Eureka"],
        2
    ),
    (
        "Who composed the light, harpsichord-and-orchestra theme music for Murder, She Wrote?",
        "John Addison",
        ["Mike Post", "Jan Hammer", "Henry Mancini"],
        3
    ),
    (
        "What was the name of Jessica Fletcher's deceased husband, whom she frequently spoke of with deep affection?",
        "Frank Fletcher",
        ["Arthur Fletcher", "George Fletcher", "Robert Fletcher"],
        2
    ),
    (
        "In season 8, to which major city did Jessica Fletcher move part-time to teach criminological literature at Manhattan University?",
        "New York City",
        ["Boston", "Chicago", "London"],
        2
    ),
    (
        "What was the title of Jessica Fletcher's first published mystery novel in the pilot episode?",
        "The Corpse Danced at Midnight",
        ["Murder at the Inn", "A Deadly Affair in Cabot Cove", "Blood on the Typewriter"],
        2
    ),
    (
        "How many total seasons did Murder, She Wrote air on CBS between 1984 and 1996?",
        "12 seasons",
        ["10 seasons", "11 seasons", "14 seasons"],
        2
    ),
    (
        "What was Jessica Fletcher's former profession before she became a worldwide bestselling novelist?",
        "High school English teacher",
        ["Librarian", "Court reporter", "Newspaper typesetter"],
        3
    ),
    (
        "Which British secret agent buddy of Jessica was played recurringly by Len Cariou?",
        "Michael Hagarty (MI6 agent)",
        ["Dennis Stanton", "Harry McGraw", "Charlie Garrett"],
        3
    ),
    (
        "Which veteran actor played Boston private eye Harry McGraw, spun off into The Law & Harry McGraw?",
        "Jerry Orbach",
        ["Keith Andes", "Ken Swofford", "George Clooneey"],
        2
    ),
    (
        "Which future ER superstar guest-starred in season 3 of Murder, She Wrote as Jessica's nephew Kip?",
        "George Clooney",
        ["Noah Wyle", "Julianna Margulies", "Anthony Edwards"],
        2
    ),
    (
        "What mathematical anomaly did epidemiologists humorously calculate regarding Cabot Cove, Maine?",
        "It had the highest per-capita murder rate in the world (higher than any real city)",
        ["Its population never changed across 12 seasons", "More people drowned than died of natural causes", "Every resident was related to Frank Fletcher"],
        3
    ),

    # 21 Jump Street - Textual / Plot / Characters
    (
        "Which future Hollywood superstar rose to fame as undercover officer Tom Hanson on 21 Jump Street?",
        "Johnny Depp",
        ["Brad Pitt", "Keanu Reeves", "Tom Cruise"],
        1
    ),
    (
        "What was the specialized premise of the police squad in 21 Jump Street?",
        "Young-looking police officers going undercover in high schools and colleges",
        ["Undercover agents posing as rock musicians", "Detectives investigating white-collar Wall Street crimes", "Border patrol agents investigating smuggling"],
        1
    ),
    (
        "What building served as the squad's covert headquarters on 21 Jump Street?",
        "An abandoned chapel",
        ["An old fire station", "A closed bowling alley", "A dockside warehouse"],
        2
    ),
    (
        "Who played Officer Doug Penhall, Tom Hanson's wisecracking best friend and partner?",
        "Peter DeLuise",
        ["Dustin Nguyen", "Steven Williams", "Frederic Forrest"],
        2
    ),
    (
        "Who was the famous father of actor Peter DeLuise?",
        "Dom DeLuise",
        ["Ernest Borgnine", "Jack Lemmon", "Walter Matthau"],
        2
    ),
    (
        "Which actress played Officer Judy Hoffs and sang the show's memorable theme song?",
        "Holly Robinson Peete",
        ["Robin Givens", "Pam Grier", "Karyn Parsons"],
        3
    ),
    (
        "Who played Officer Harry Truman Ioki, who was secretly a Vietnamese refugee named Vinh Van Tran?",
        "Dustin Nguyen",
        ["BD Wong", "Russell Wong", "Phillip Rhee"],
        2
    ),
    (
        "Which eccentric actor played the squad's first commander, Captain Richard Jenko, in early season 1?",
        "Frederic Forrest",
        ["Steven Williams", "Lance LeGault", "Robert Vaughn"],
        3
    ),
    (
        "Who replaced Captain Jenko as the commanding officer, playing the stern Captain Adam Fuller?",
        "Steven Williams",
        ["Frederic Forrest", "Carl Weathers", "Taurean Blacque"],
        2
    ),
    (
        "Which major TV executive and producer co-created 21 Jump Street with Patrick Hasburgh?",
        "Stephen J. Cannell",
        ["Steven Bochco", "Donald P. Bellisario", "Aaron Spelling"],
        3
    ),
    (
        "On which newly launched broadcast network did 21 Jump Street premiere in April 1987 as a flagship hit?",
        "Fox",
        ["The WB", "UPN", "NBC"],
        1
    ),
    (
        "What real-life Canadian city stood in for the series' American setting throughout filming?",
        "Vancouver, British Columbia",
        ["Toronto, Ontario", "Montreal, Quebec", "Calgary, Alberta"],
        2
    ),
    (
        "Why was Johnny Depp reportedly desperate to leave 21 Jump Street by season 4?",
        "He resented being marketed as a teen-idol pinup and wanted serious film roles",
        ["He had a severe contract dispute over syndication residuals", "He refused to film in Canada due to winter weather", "He was fired after clashing with Fox executives"],
        3
    ),
    (
        "What Tim Burton film did Johnny Depp star in immediately after departing 21 Jump Street in 1990?",
        "Edward Scissorhands",
        ["Beetlejuice", "Sleepy Hollow", "Ed Wood"],
        1
    ),
    (
        "Which future Oscar winner guest-starred in season 2 as a high school student named Peter McCall?",
        "Brad Pitt",
        ["Leonardo DiCaprio", "Christian Bale", "Matthew McConaughey"],
        2
    ),
    (
        "How was Captain Richard Jenko killed off early in season 1 to facilitate Steven Williams taking command?",
        "Hit by a drunk driver",
        ["Shot during an undercover drug sting", "Plane crash en route to Seattle", "Heart attack in his office"],
        3
    ),
    (
        "Which actor played Officer Dennis Booker, who was spun off into his own 1989 series Booker?",
        "Richard Grieco",
        ["Peter DeLuise", "Dustin Nguyen", "Michael Bendetti"],
        2
    ),
    (
        "What PSA (Public Service Announcement) feature famously concluded several heavy episodes of 21 Jump Street?",
        "Cast members speaking directly to viewers with toll-free crisis hotline numbers",
        ["Blooper reels showing humorous mistakes", "Interviews with real high school principals", "Documentary footage from local police archives"],
        2
    ),
    (
        "How many seasons did 21 Jump Street air between 1987 and 1991?",
        "5 seasons",
        ["4 seasons", "6 seasons", "7 seasons"],
        2
    ),
    (
        "Which movie remake in 2012 featured Johnny Depp and Peter DeLuise in a surprise cameo as their original characters?",
        "21 Jump Street (starring Jonah Hill and Channing Tatum)",
        ["The A-Team", "Miami Vice", "Starsky & Hutch"],
        1
    ),

    # The Wonder Years - Textual / Plot / Characters
    (
        "Who starred as the adolescent protagonist Kevin Arnold on The Wonder Years?",
        "Fred Savage",
        ["Josh Saviano", "Jason Hervey", "Brian Bonsall"],
        1
    ),
    (
        "What was the name of Kevin Arnold's longtime neighbor, childhood friend, and romantic love interest?",
        "Gwendolyn 'Winnie' Cooper",
        ["Becky Slater", "Madeline Adams", "Lisa Berlini"],
        1
    ),
    (
        "Which actress played Winnie Cooper on The Wonder Years?",
        "Danica McKellar",
        ["Tracey Gold", "Tina Yothers", "Candace Cameron"],
        1
    ),
    (
        "Who played Kevin's brainy, bespectacled, allergic best friend Paul Joshua Pfeiffer?",
        "Josh Saviano",
        ["Jason Hervey", "Fred Savage", "Marc Price"],
        1
    ),
    (
        "What bizarre, persistent 1990s urban legend circulated regarding child actor Josh Saviano?",
        "That he grew up to become shock rocker Marilyn Manson",
        ["That he was the voice of Bart Simpson", "That he founded Netscape communications", "That he died in an allergy experiment"],
        3
    ),
    (
        "Who played Kevin's obnoxious, tormenting older brother Wayne Arnold on The Wonder Years?",
        "Jason Hervey",
        ["Josh Saviano", "Jeremy Miller", "David Faustino"],
        3
    ),
    (
        "What insult did older brother Wayne constantly direct at Kevin throughout the series?",
        "Butthead",
        ["Dork", "Loser", "Shrimp"],
        1
    ),
    (
        "Which gravelly voiced actor played Kevin's stern, Korean War veteran father Jack Arnold?",
        "Dan Lauria",
        ["Alan Thicke", "Michael Gross", "Bob Saget"],
        1
    ),
    (
        "Which actress played Kevin's gentle, nurturing 1960s suburban mother Norma Arnold?",
        "Alley Mills",
        ["Meredith Baxter", "Joanna Kerns", "Marion Ross"],
        3
    ),
    (
        "Which acclaimed actor provided the uncredited, nostalgic adult voiceover narration for Kevin Arnold?",
        "Daniel Stern",
        ["Fred Savage", "Ron Howard", "Richard Dreyfuss"],
        1
    ),
    (
        "What classic Beatles song, performed in a gritty soul cover by Joe Cocker, served as the theme song?",
        "With a Little Help from My Friends",
        ["In My Life", "Yesterday", "Help!"],
        1
    ),
    (
        "In what turbulent historical year did the pilot episode of The Wonder Years take place?",
        "1968",
        ["1965", "1972", "1975"],
        2
    ),
    (
        "What tragic event in the pilot episode prompted Kevin and Winnie's first kiss in the woods?",
        "Winnie's older brother Brian Cooper was killed in the Vietnam War",
        ["Kevin's family dog was struck by a car", "Martin Luther King Jr. was assassinated", "Winnie's parents announced their divorce"],
        2
    ),
    (
        "Which junior high school did Kevin, Paul, and Winnie attend in the early seasons?",
        "Robert F. Kennedy Junior High",
        ["John F. Kennedy Middle School", "Thomas Jefferson Junior High", "Lincoln High School"],
        3
    ),
    (
        "Which sadistic physical education teacher was played by Robert Picardo on The Wonder Years?",
        "Coach Cutlip",
        ["Coach Lubbock", "Coach White", "Coach Stern"],
        3
    ),
    (
        "What historic Emmy milestone did 13-year-old Fred Savage achieve in 1989?",
        "Youngest actor ever nominated for Outstanding Lead Actor in a Comedy Series",
        ["Youngest actor to host the Emmy broadcast", "Youngest winner of the Peabody Award", "First child actor to direct an Emmy-nominated episode"],
        2
    ),
    (
        "Following what mega-event did the pilot episode of The Wonder Years premiere in January 1988?",
        "Super Bowl XXII",
        ["The World Series Game 7", "The Academy Awards", "The 1988 Winter Olympics Opening Ceremony"],
        2
    ),
    (
        "What major Emmy victory did The Wonder Years achieve after airing only six episodes of its debut season?",
        "Won the Primetime Emmy Award for Outstanding Comedy Series",
        ["Won Outstanding Drama Series", "Swept all acting categories", "Won the Governors Award"],
        2
    ),
    (
        "Who created The Wonder Years, capturing baby-boomer suburban nostalgia?",
        "Neal Marlens and Carol Black",
        ["Steven Bochco and Terry Louise Fisher", "Gary David Goldberg", "Glenn Gordon Caron"],
        2
    ),
    (
        "Which future Friends star guest-starred in season 2 as a popular girl who goes on a date with Kevin?",
        "Alicia Silverstone",
        ["Lisa Kudrow", "Jennifer Aniston", "Courteney Cox"],
        3
    ),
    (
        "Which future Clueless superstar made her screen acting debut in season 6 as Kevin's dream girl Shannon?",
        "Alicia Silverstone",
        ["Reese Witherspoon", "Sarah Michelle Gellar", "Claire Danes"],
        2
    ),
    (
        "Which future Spider-Man star guest-starred in season 5 as Kevin's friend Doug Newcross?",
        "Tobey Maguire",
        ["Leonardo DiCaprio", "James Franco", "Kirsten Dunst"],
        3
    ),
    (
        "In the series finale epilogue, what adult fate is revealed for Kevin's father Jack Arnold?",
        "He passed away two years after Kevin graduated high school",
        ["He was elected mayor of their suburban town", "He retired to Florida to fish", "He founded his own defense contracting firm"],
        2
    ),
    (
        "In the series finale epilogue, what relationship status is revealed between Kevin and Winnie?",
        "They stayed lifelong pen pals and friends, each marrying other people",
        ["They married in a lavish church ceremony in 1982", "They became business partners in California", "They lost touch completely after high school"],
        2
    ),
    (
        "What company did Kevin's father Jack Arnold work for as an office manager?",
        "NORCOM",
        ["General Electric", "Westinghouse", "Grumman Aerospace"],
        3
    ),
    (
        "What car did Kevin Arnold purchase for himself in high school, which constantly broke down?",
        "A beat-up 1963 Dodge Dart",
        ["A rusty 1967 Ford Mustang", "A 1960 Volkswagen Beetle", "A Chevrolet Corvair"],
        3
    ),
    (
        "What instrument did Kevin attempt to learn in season 1 before giving up?",
        "Electric guitar",
        ["Piano", "Drums", "Saxophone"],
        3
    ),
    (
        "How many seasons did The Wonder Years run on ABC between 1988 and 1993?",
        "6 seasons",
        ["5 seasons", "7 seasons", "8 seasons"],
        2
    ),
    (
        "What was the name of Kevin's hippie older sister who frequently clashed with her conservative father?",
        "Karen Arnold",
        ["Kathy Arnold", "Kristin Arnold", "Kelly Arnold"],
        2
    ),
    (
        "Which actress played Kevin's counterculture older sister Karen Arnold?",
        "Olivia d'Abo",
        ["Tracey Gold", "Danica McKellar", "Alley Mills"],
        2
    )
]

if __name__ == "__main__":
    build_batch(questions, 9, "tools/staging/80s_tv_shows_batch9.json")
