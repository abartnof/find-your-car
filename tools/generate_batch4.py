import sys
from make_batch import build_batch

# Batch 4: Family Ties & Growing Pains (80s Family Sitcoms & Teen Idols)
# 100 questions: 30 d1, 40 d2, 30 d3

questions = [
    # Family Ties - Textual / Plot / Characters
    (
        "Who played the young conservative, briefcase-carrying Alex P. Keaton on Family Ties?",
        "Michael J. Fox",
        ["Kirk Cameron", "Scott Valentine", "Marc Price"],
        1
    ),
    (
        "In what Ohio city was Family Ties set?",
        "Columbus",
        ["Cleveland", "Cincinnati", "Dayton"],
        1
    ),
    (
        "What were the names of Alex P. Keaton's former-hippie parents on Family Ties?",
        "Steven and Elyse Keaton",
        ["Jason and Maggie Seaver", "Dan and Roseanne Conner", "Cliff and Clair Huxtable"],
        1
    ),
    (
        "Which actor played patriarch Steven Keaton, manager of public television station WKS-TV?",
        "Michael Gross",
        ["Alan Thicke", "Bob Saget", "Reginald VelJohnson"],
        1
    ),
    (
        "Which actress played architect and mother Elyse Keaton on Family Ties?",
        "Meredith Baxter",
        ["Joanna Kerns", "Marion Ross", "Phylicia Rashad"],
        1
    ),
    (
        "Which actress portrayed Alex's fashion-obsessed older sister Mallory Keaton?",
        "Justine Bateman",
        ["Tracey Gold", "Alyssa Milano", "Candace Cameron"],
        1
    ),
    (
        "Which actress played the practical, tomboy younger sister Jennifer Keaton?",
        "Tina Yothers",
        ["Danica McKellar", "Sara Gilbert", "Mary-Kate Olsen"],
        1
    ),
    (
        "What was the name of the youngest Keaton child, born in season 3 and aged rapidly to preschool in season 5?",
        "Andrew",
        ["Ben", "Luke", "Toby"],
        2
    ),
    (
        "Which child actor portrayed little Andrew Keaton in seasons 5 through 7?",
        "Brian Bonsall",
        ["Jeremy Miller", "Danny Pintauro", "Fred Savage"],
        3
    ),
    (
        "What was the name of Mallory's scruffy, leather-jacketed artist boyfriend who famously grunted 'Aay'?",
        "Nick Moore",
        ["Skippy Handleman", "Boner Stabone", "Eddie Simms"],
        1
    ),
    (
        "Which actor played Mallory's well-meaning artist boyfriend Nick Moore?",
        "Scott Valentine",
        ["Marc Price", "Josh Andrew Koenig", "Sam Anderson"],
        2
    ),
    (
        "What was the name of the nerdy next-door neighbor who harbored an unrequited crush on Mallory Keaton?",
        "Irwin 'Skippy' Handleman",
        ["Boner Stabone", "Arvid Engen", "Bud Bundy"],
        1
    ),
    (
        "Which actor and stand-up comedian played Skippy Handleman on Family Ties?",
        "Marc Price",
        ["Dan Frischman", "Curtis Armstrong", "Scott Valentine"],
        2
    ),
    (
        "What political and financial publication did Alex P. Keaton treat with religious devotion?",
        "The Wall Street Journal",
        ["Forbes", "Barron's", "The Financial Times"],
        1
    ),
    (
        "Which U.S. President was Alex P. Keaton's ultimate political idol throughout the 1980s?",
        "Ronald Reagan",
        ["Richard Nixon", "Gerald Ford", "George H.W. Bush"],
        1
    ),
    (
        "Which real-life sitting U.S. President publicly declared Family Ties to be his favorite television program?",
        "Ronald Reagan",
        ["Jimmy Carter", "George H.W. Bush", "Bill Clinton"],
        1
    ),
    (
        "Which actress played Alex's feminist artist girlfriend Ellen Reed in season 4?",
        "Tracy Pollan",
        ["Courteney Cox", "Julie McCullough", "Meg Ryan"],
        2
    ),
    (
        "What real-life marriage resulted from the on-screen romance between Alex and Ellen on Family Ties?",
        "Michael J. Fox and Tracy Pollan married in 1988",
        ["Kirk Cameron and Chelsea Noble married in 1991", "Alan Thicke and Joanna Kerns married in 1987", "Scott Valentine and Justine Bateman married in 1989"],
        2
    ),
    (
        "Which future Friends star played Alex's psychology-major girlfriend Lauren Miller in seasons 6 and 7?",
        "Courteney Cox",
        ["Jennifer Aniston", "Lisa Kudrow", "Helen Hunt"],
        1
    ),
    (
        "What college did Alex P. Keaton attend after turning down an offer from Princeton to stay close to family?",
        "Leland University",
        ["Ohio State University", "Dartmouth College", "Northwestern University"],
        2
    ),
    (
        "Who created Family Ties, basing the dynamic on his own experience as a 1960s liberal raising conservative children?",
        "Gary David Goldberg",
        ["Neal Marlens", "Steven Bochco", "Reinhold Weege"],
        2
    ),
    (
        "Which acclaimed duo sang the opening theme song 'Without Us' for the vast majority of Family Ties episodes?",
        "Johnny Mathis and Deniece Williams",
        ["Kenny Rogers and Dolly Parton", "Peabo Bryson and Roberta Flack", "Billy Joe Thomas and Dusty Springfield"],
        2
    ),
    (
        "What grueling production schedule did Michael J. Fox maintain during late 1984 and early 1985?",
        "Filming Family Ties by day and Back to the Future by night",
        ["Rehearsing a Broadway play by morning and filming Family Ties at night", "Filming Teen Wolf and Back to the Future on alternating weekends", "Writing an autobiography while directing episodes of Family Ties"],
        1
    ),
    (
        "How many consecutive Primetime Emmy Awards did Michael J. Fox win for Family Ties (1986, 1987, 1988)?",
        "3 consecutive Emmys",
        ["2 consecutive Emmys", "4 consecutive Emmys", "5 consecutive Emmys"],
        2
    ),
    (
        "Which famous actor originally turned down the role of Alex P. Keaton because he did not want a long TV contract?",
        "Matthew Broderick",
        ["Rob Lowe", "Emilio Estevez", "Tom Cruise"],
        3
    ),
    (
        "Why did creator Gary David Goldberg initially reject Michael J. Fox during the casting process?",
        "He felt Fox was too short and couldn't picture his face on a lunchbox",
        ["He thought Fox had too thick of a Canadian accent", "Fox showed up late to the reading", "Fox had no previous television credits"],
        3
    ),
    (
        "What job did Alex P. Keaton accept in New York City in the two-part series finale of Family Ties?",
        "Investment banker on Wall Street",
        ["Speechwriter for the Republican National Committee", "Economics editor for The Wall Street Journal", "Professor of Finance at Columbia"],
        2
    ),
    (
        "Which famous guest star played Uncle Ned, Elyse's alcoholic brother who punches Alex in 'Say Uncle'?",
        "Tom Hanks",
        ["Robin Williams", "Dan Aykroyd", "John Candy"],
        2
    ),
    (
        "In the emotional two-part episode 'A, My Name Is Alex', why did Alex undergo psychiatric therapy?",
        "His friend Greg died in a car crash that Alex was supposed to be in",
        ["He failed his first college economics examination", "Lauren broke off their engagement unexpectedly", "Steven suffered a heart attack during Thanksgiving"],
        2
    ),
    (
        "Which future Oscar winner guest-starred in season 2 as a teenage babysitter who develops a crush on Alex?",
        "Geena Davis",
        ["Julia Roberts", "Jodie Foster", "Marisa Tomei"],
        3
    ),
    (
        "Which future superstar guest-starred in season 4 as a high school saxophone player who tutors Jennifer?",
        "River Phoenix",
        ["Christian Slater", "Corey Haim", "Wil Wheaton"],
        3
    ),
    (
        "Which actress played Skippy's sister and Mallory's friend Trudy on Family Ties?",
        "Julia Louis-Dreyfus",
        ["Christina Applegate", "Jane Krakowski", "Pam Dawber"],
        3
    ),
    (
        "What was the name of the PBS affiliate station where Steven Keaton worked?",
        "WKS-TV Channel 3",
        ["WGBH Channel 2", "WNET Channel 13", "KCET Channel 28"],
        3
    ),
    (
        "What instrument did Elyse Keaton play when singing folk songs with Steven?",
        "Acoustic guitar",
        ["Banjo", "Autoharp", "Harmonica"],
        2
    ),
    (
        "What award did Family Ties win at the 1987 Emmy Awards for writing the episode 'A, My Name Is Alex'?",
        "Outstanding Writing in a Comedy Series",
        ["Outstanding Directing in a Comedy Series", "Peabody Award for Drama", "Humanitas Prize in 30-Minute Category"],
        3
    ),
    (
        "How many seasons did Family Ties run on NBC between 1982 and 1989?",
        "7 seasons",
        ["6 seasons", "8 seasons", "9 seasons"],
        2
    ),
    (
        "What was the title of the spin-off pilot produced starring Scott Valentine as Nick Moore that NBC declined to pick up?",
        "The Art of Being Nick",
        ["Nick at Night", "Mallory and Nick", "Moore than Words"],
        3
    ),
    (
        "In what time slot did Family Ties anchor NBC's Thursday night block before Cheers?",
        "8:30 PM (following The Cosby Show)",
        ["8:00 PM (opening the evening)", "9:00 PM (replacing Cheers)", "9:30 PM (following Night Court)"],
        2
    ),
    (
        "What was the highest rank Family Ties reached in the end-of-year Nielsen ratings during the 1985-1986 and 1986-1987 seasons?",
        "Number 2 (behind only The Cosby Show)",
        ["Number 1 in all of television", "Number 4 (behind Dallas and Dynasty)", "Number 6 (behind 60 Minutes)"],
        2
    ),
    (
        "What greeting did Nick Moore always deliver when entering the Keaton living room?",
        "Aay!",
        ["Yo!", "Howdy!", "Greetings!"],
        1
    ),

    # Growing Pains - Textual / Plot / Characters
    (
        "Who played the easygoing psychiatrist father Dr. Jason Seaver on Growing Pains?",
        "Alan Thicke",
        ["Michael Gross", "Kirk Cameron", "Bob Saget"],
        1
    ),
    (
        "What was the name of the mother and journalist played by Joanna Kerns on Growing Pains?",
        "Maggie Malone Seaver",
        ["Elyse Keaton", "Jill Taylor", "Angela Bower"],
        1
    ),
    (
        "Who played the charming, troublemaking oldest son Mike Seaver on Growing Pains?",
        "Kirk Cameron",
        ["Fred Savage", "Michael J. Fox", "Jason Hervey"],
        1
    ),
    (
        "Which actress played the studious, straight-A middle daughter Carol Seaver on Growing Pains?",
        "Tracey Gold",
        ["Justine Bateman", "Candace Cameron", "Alyssa Milano"],
        1
    ),
    (
        "Which young actor played the mischievous younger brother Ben Seaver on Growing Pains?",
        "Jeremy Miller",
        ["Danny Pintauro", "Brian Bonsall", "Josh Saviano"],
        1
    ),
    (
        "On what town and island was Growing Pains primarily set?",
        "Huntington, Long Island, New York",
        ["Scarsdale, Westchester, New York", "Oyster Bay, Long Island, New York", "Stamford, Connecticut"],
        2
    ),
    (
        "Why did Dr. Jason Seaver move his psychiatry practice to an office inside his home?",
        "So his wife Maggie could resume her career as a journalist",
        ["Because he lost his hospital privileges", "To save on commercial rent costs", "To conduct psychiatric research on his own family"],
        2
    ),
    (
        "What was the name of the local newspaper where Maggie Seaver worked as a reporter?",
        "The Long Island Herald",
        ["The Newsday Dispatch", "The Huntington Chronicle", "The New York Post"],
        3
    ),
    (
        "What was the nickname of Mike Seaver's dim-witted best friend, played by Josh Andrew Koenig?",
        "Boner",
        ["Skippy", "Chunk", "Spud"],
        1
    ),
    (
        "What was the full canonical name of Mike's best friend 'Boner' on Growing Pains?",
        "Richard Stabone",
        ["Robert Henderson", "Raymond St. John", "Ronald Robinson"],
        2
    ),
    (
        "Who was the father of actor Josh Andrew Koenig (who played Boner Stabone)?",
        "Walter Koenig (Chekov from Star Trek)",
        ["William Shatner", "Leonard Nimoy", "George Takei"],
        2
    ),
    (
        "Which actor played high school principal Bob DeWitt, who constantly clashed with Mike Seaver?",
        "Sam Anderson",
        ["Howard Hesseman", "James Karen", "Richard Sanders"],
        3
    ),
    (
        "What high school gym coach and large-family father was spun off into the sitcom Just the Ten of Us?",
        "Coach Graham Lubbock",
        ["Coach Ernie Pantusso", "Coach White", "Coach Cutlip"],
        2
    ),
    (
        "Which actor played Coach Graham Lubbock on Growing Pains and Just the Ten of Us?",
        "Bill Kirchenbauer",
        ["Alan Thicke", "Sam Anderson", "Gordon Jump"],
        3
    ),
    (
        "Who joined the cast of Growing Pains in season 7 as homeless teen Luke Brower?",
        "Leonardo DiCaprio",
        ["Brad Pitt", "Tobey Maguire", "River Phoenix"],
        1
    ),
    (
        "How old was Leonardo DiCaprio when he joined Growing Pains in 1991?",
        "16 years old",
        ["12 years old", "19 years old", "21 years old"],
        3
    ),
    (
        "Which actress played the rapidly aged toddler Chrissy Seaver in seasons 6 and 7 of Growing Pains?",
        "Ashley Johnson",
        ["Tina Yothers", "Mary-Kate Olsen", "Thora Birch"],
        2
    ),
    (
        "Who created the ABC family sitcom Growing Pains?",
        "Neal Marlens",
        ["Gary David Goldberg", "Susan Harris", "David Jacobs"],
        3
    ),
    (
        "What singer recorded the Growing Pains theme song 'As Long as We Got Each Other' with Dusty Springfield and Jennifer Warnes?",
        "Billy Joe Thomas",
        ["Kenny Rogers", "Burt Bacharach", "Gary Portnoy"],
        2
    ),
    (
        "What was the title of the famous 1989 Growing Pains episode where Carol's boyfriend Sandy dies from drunk driving?",
        "Second Chance",
        ["One for the Road", "The Final Drive", "A Lesson for Carol"],
        2
    ),
    (
        "Which future Friends superstar played Carol's doomed college boyfriend Sandy in 'Second Chance'?",
        "Matthew Perry",
        ["Matt LeBlanc", "David Schwimmer", "George Clooney"],
        1
    ),
    (
        "Which Hollywood megastar guest-starred in season 4 as a rock star named Jonathan Keith who dates Carol?",
        "Brad Pitt",
        ["Tom Cruise", "Johnny Depp", "Christian Slater"],
        2
    ),
    (
        "What personal transformation in Kirk Cameron's life during season 4 created major friction on the set of Growing Pains?",
        "He became a devout born-again Christian",
        ["He converted to Scientology", "He refused to speak to female cast members", "He demanded to direct every episode"],
        1
    ),
    (
        "Which actress was fired from playing Mike's fiancée Julie Costello after Kirk Cameron objected to her previous appearance in Playboy?",
        "Julie McCullough",
        ["Chelsea Noble", "Tracey Gold", "Kelly Packett"],
        2
    ),
    (
        "Which actress played Mike Seaver's girlfriend Kate MacDonald and later married Kirk Cameron in real life?",
        "Chelsea Noble",
        ["Julie McCullough", "Tracey Gold", "Joanna Kerns"],
        2
    ),
    (
        "What serious health struggle caused Tracey Gold to be absent from most of Growing Pains' final season?",
        "Severe battle with anorexia nervosa",
        ["Mononucleosis and vocal cord polyps", "A career-threatening auto accident", "Lyme disease"],
        2
    ),
    (
        "What real-life relation is Kirk Cameron to Full House star Candace Cameron Bure?",
        "Older brother",
        ["First cousin", "Twin brother", "Uncle"],
        1
    ),
    (
        "What career did Mike Seaver pursue after struggling through high school, eventually becoming a teacher at a remedial clinic?",
        "Actor and high school drama teacher",
        ["Commercial real estate agent", "Pediatric nurse", "Police patrol officer"],
        2
    ),
    (
        "In the final scene of the Growing Pains series finale, what did the Seaver family do before leaving their home for Washington D.C.?",
        "Shared a pizza picnic on the bare floor of the empty living room",
        ["Carved their initials into the front porch post", "Took a final family photo by the front door", "Turned out the lights and locked the keys inside"],
        2
    ),
    (
        "On which television network did Growing Pains air throughout its seven-season run (1985-1992)?",
        "ABC",
        ["NBC", "CBS", "Fox"],
        1
    ),
    (
        "Which Canadian talk show and game show host had Alan Thicke hosted before starring in Growing Pains?",
        "The Alan Thicke Show",
        ["Jeopardy!", "Canada AM", "Front Page Challenge"],
        3
    ),
    (
        "What musical talent did Alan Thicke possess, co-writing the theme songs for Diff'rent Strokes and The Facts of Life?",
        "Composer and songwriter",
        ["Concert violinist", "Operatic tenor", "Heavy metal drummer"],
        2
    ),
    (
        "Who is Alan Thicke's famous singer-songwriter son who recorded the global hit 'Blurred Lines'?",
        "Robin Thicke",
        ["Brennan Thicke", "Carter Thicke", "Julian Thicke"],
        1
    ),
    (
        "What was the name of Mike Seaver's favorite jacket that he wore throughout the early seasons?",
        "A red member-style bomber jacket",
        ["A black leather motorcycle jacket", "A brown suede aviator jacket", "A denim sherpa jacket"],
        2
    ),
    (
        "In the season 2 episode 'Born Free', what prank did Mike pull on the school statue that got him suspended?",
        "Painted it and dressed it up in clothes",
        ["Glued a toilet seat around its neck", "Swapped its head with a watermelon", "Tied hundreds of balloons to lift it off the ground"],
        3
    ),
    (
        "What pet dog did the Seaver family adopt in season 3 of Growing Pains?",
        "A golden retriever named Stinky",
        ["A basset hound named Einstein", "A bulldog named Winston", "A beagle named Snoopy"],
        3
    ),
    (
        "What was the name of the recurring French exchange student who stayed with the Seaver family?",
        "Maurice",
        ["Pierre", "Francois", "Henri"],
        3
    ),
    (
        "Which actress played Cindy, Ben's awkward neighborhood girlfriend in season 5?",
        "Kirsten Dunst",
        ["Sarah Michelle Gellar", "Candace Hutson", "Danielle Fishel"],
        3
    ),
    (
        "How many total episodes of Growing Pains were broadcast on ABC?",
        "166 episodes",
        ["142 episodes", "185 episodes", "204 episodes"],
        3
    ),
    (
        "Which night of the week was Growing Pains' primary anchor broadcast night on ABC during its peak popularity?",
        "Wednesday night",
        ["Friday night", "Monday night", "Thursday night"],
        2
    ),
    (
        "What teen idol magazine frequently featured Kirk Cameron on its cover alongside Michael J. Fox during the late 1980s?",
        "Tiger Beat",
        ["Rolling Stone", "Seventeen", "People Weekly"],
        1
    ),
    (
        "Which actor played Jason Seaver's crusty, adventurous father Ed Seaver on Growing Pains?",
        "Gordon Jump",
        ["Dick O'Neill", "David Doyle", "Howard Duff"],
        3
    ),
    (
        "How was Jason's father Ed Seaver written out of the show in season 4?",
        "He passed away suddenly during a visit",
        ["He moved to Tahiti to run a marina", "He remarried and moved to Alaska", "He sailed around the world on a yacht"],
        3
    ),
    (
        "Which future star of Beverly Hills, 90210 guest-starred in season 3 as a girl who goes on a date with Mike?",
        "Jennie Garth",
        ["Tori Spelling", "Shannen Doherty", "Tiffani Thiessen"],
        3
    ),
    (
        "Which future Oscar winner auditioned for the role of Mike Seaver before Kirk Cameron won the part?",
        "Robert Downey Jr.",
        ["Nicolas Cage", "Sean Penn", "Christian Bale"],
        3
    ),
    (
        "In the episode where Ben wants to pierce his ear to look cool, who helps him do it with a potato and needle?",
        "Mike Seaver",
        ["Boner Stabone", "Carol Seaver", "Coach Lubbock"],
        2
    ),
    (
        "What was the name of Carol Seaver's high school boyfriend with whom she planned to attend Columbia?",
        "Bobby Wynn",
        ["Sandy", "Jeff", "David"],
        3
    ),
    (
        "Which actor played Bobby Wynn, Carol's clean-cut high school boyfriend?",
        "Kevin Wixted",
        ["Matthew Perry", "Brian Austin Green", "Josh Andrew Koenig"],
        3
    ),
    (
        "In the final season, why does the Seaver family pack up and move from Long Island to Washington D.C.?",
        "Maggie receives a prestigious job offer at the White House press office",
        ["Jason is appointed chief of psychiatry at Georgetown Medical", "Mike is admitted to law school in D.C.", "Ben is accepted to an elite music academy"],
        2
    ),
    (
        "What year did Growing Pains premiere on ABC?",
        "1985",
        ["1983", "1987", "1988"],
        2
    ),
    (
        "Which Nobel Prize-winning free-market economist was Alex P. Keaton's intellectual idol on Family Ties?",
        "Milton Friedman",
        ["John Maynard Keynes", "Paul Samuelson", "Alan Greenspan"],
        2
    ),
    (
        "Whose framed photograph did Alex P. Keaton keep prominently on his bedroom nightstand?",
        "Richard Nixon",
        ["Barry Goldwater", "George Bush", "William F. Buckley"],
        2
    ),
    (
        "What was the name of the high school that Alex, Mallory, and Jennifer attended in Columbus, Ohio?",
        "Leland High School",
        ["Grant High School", "Buckeye Central High", "Franklin High School"],
        3
    ),
    (
        "What was the name of the high school Mike and Carol Seaver attended on Growing Pains?",
        "Thomas Dewey High School",
        ["Long Island Academy", "Huntington Regional High", "Roosevelt High School"],
        3
    ),
    (
        "What was the name of the Seavers' eccentric, gossiping next-door neighbor played by K Callan?",
        "Mrs. Koosman",
        ["Mrs. Ochmonek", "Mrs. Kravitz", "Mrs. Poole"],
        3
    ),
    (
        "In season 3 of Growing Pains, what classic Thornton Wilder stage play did Mike audition for to impress a girl, winning the lead role of George Gibbs?",
        "Our Town",
        ["The Crucible", "Death of a Salesman", "The Glass Menagerie"],
        2
    ),
    (
        "What musical instrument was Ben Seaver forced to play in the school band on Growing Pains?",
        "The tuba",
        ["The triangle", "The trombone", "The snare drum"],
        3
    ),
    (
        "In the Growing Pains spin-off Just the Ten of Us, to which state did Coach Lubbock move his large family to teach at St. Augustine's Academy?",
        "California",
        ["Texas", "Florida", "Ohio"],
        2
    ),
    (
        "Which iconic late-night talk show host did Michael J. Fox repeatedly visit to share humorous updates about his meteoric 1980s stardom?",
        "Johnny Carson",
        ["David Letterman", "Merv Griffin", "Dick Cavett"],
        1
    ),
    (
        "What catchphrase did Steven Keaton often use when reacting with gentle exasperation to Alex's extreme capitalist schemes?",
        "Alex, please!",
        ["Not in this house!", "Turn off the ticker!", "Go to your room!"],
        1
    )
]

if __name__ == "__main__":
    build_batch(questions, 4, "tools/staging/80s_tv_shows_batch4.json")
