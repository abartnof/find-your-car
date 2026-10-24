import sys
from make_batch import build_batch

# Batch 8: Hill Street Blues, St. Elsewhere, L.A. Law & Cagney & Lacey (Quality Ensembles & Gritty Drama)
# 100 questions: 30 d1, 40 d2, 30 d3

questions = [
    # Hill Street Blues - Textual / Plot / Characters
    (
        "Who created the groundbreaking, realistic police drama Hill Street Blues with Michael Kozoll?",
        "Steven Bochco",
        ["Donald P. Bellisario", "Stephen J. Cannell", "Dick Wolf"],
        1
    ),
    (
        "What was the signature morning roll-call catchphrase of Sgt. Phil Esterhaus on Hill Street Blues?",
        "Let's be careful out there",
        ["Keep your heads down", "Watch your six", "Stay sharp, people"],
        1
    ),
    (
        "Which actor portrayed the dignified, Latin-quoting Sgt. Phil Esterhaus until his death in 1983?",
        "Michael Conrad",
        ["Daniel J. Travanti", "Bruce Weitz", "Charles Haid"],
        1
    ),
    (
        "Who played the recovering alcoholic and respected precinct commander Captain Frank Furillo?",
        "Daniel J. Travanti",
        ["Michael Conrad", "James B. Sikking", "Taurean Blacque"],
        3
    ),
    (
        "Which actress played public defender Joyce Davenport, Frank Furillo's secret lover and eventual wife?",
        "Veronica Hamel",
        ["Barbara Bosson", "Betty Thomas", "Sharon Gless"],
        1
    ),
    (
        "What pet name did Frank Furillo and Joyce Davenport use for their private late-night bathtub encounters?",
        "Pizza man",
        ["Coffee break", "Midnight court", "Case review"],
        2
    ),
    (
        "Which scruffy, growling undercover detective on Hill Street Blues was notorious for biting suspects?",
        "Mick Belker",
        ["Johnny LaRue", "Neal Washington", "Andy Renko"],
        1
    ),
    (
        "Which actor played the eccentric, canine-growling detective Mick Belker on Hill Street Blues?",
        "Bruce Weitz",
        ["Charles Haid", "Kiel Martin", "Rene Enriquez"],
        1
    ),
    (
        "What insulting term did Detective Mick Belker routinely scream at criminals he wrestled to the ground?",
        "Dog breath! / Hairbag!",
        ["Dirtbag! / Scumbag!", "Punks! / Clowns!", "Lowlifes! / Vermin!"],
        2
    ),
    (
        "What two street patrol partners were ambushed and shot in the climactic cliffhanger of the pilot episode?",
        "Andy Renko and Bobby Hill",
        ["Frank Furillo and Phil Esterhaus", "Mick Belker and Johnny LaRue", "Neal Washington and Ray Calletano"],
        2
    ),
    (
        "Which actor played Officer Andy Renko, the cowboy-hat-wearing patrol cop from the South?",
        "Charles Haid",
        ["Michael Warren", "Kiel Martin", "James B. Sikking"],
        2
    ),
    (
        "Which former college basketball star played Officer Bobby Hill, Renko's level-headed African-American partner?",
        "Michael Warren",
        ["Taurean Blacque", "Carl Weathers", "Robert Guillaume"],
        2
    ),
    (
        "Who played the pipe-smoking, militaristic SWAT Emergency Action Team commander Lieutenant Howard Hunter?",
        "James B. Sikking",
        ["Michael Conrad", "Charles Haid", "Ed Flanders"],
        2
    ),
    (
        "Which actress played the tough, competent patrol officer (and later sergeant) Lucille Bates?",
        "Betty Thomas",
        ["Veronica Hamel", "Barbara Bosson", "Tyne Daly"],
        2
    ),
    (
        "Which actress played Frank Furillo's neurotic, demanding ex-wife Fay Furillo on Hill Street Blues?",
        "Barbara Bosson",
        ["Veronica Hamel", "Betty Thomas", "Alfre Woodard"],
        2
    ),
    (
        "What real-life relationship existed between actress Barbara Bosson and co-creator Steven Bochco?",
        "They were married",
        ["They were brother and sister", "They were first cousins", "They were former high school sweethearts"],
        2
    ),
    (
        "How did Sgt. Phil Esterhaus die on the show following actor Michael Conrad's real-life passing?",
        "He suffered a fatal heart attack while making love to his partner Grace Gardner",
        ["He was shot during a bank hostage crisis", "He died in a routine traffic accident", "He passed away quietly in his sleep at home"],
        3
    ),
    (
        "How many Primetime Emmy Awards did Hill Street Blues win for its rookie season in 1981, setting a drama record?",
        "8 Emmys",
        ["4 Emmys", "12 Emmys", "16 Emmys"],
        3
    ),
    (
        "How many consecutive years did Hill Street Blues win the Primetime Emmy for Outstanding Drama Series (1981-1984)?",
        "4 consecutive years",
        ["2 consecutive years", "3 consecutive years", "5 consecutive years"],
        2
    ),
    (
        "Who composed the melancholy piano-and-guitar instrumental theme song for Hill Street Blues?",
        "Mike Post (featuring Larry Carlton)",
        ["Jan Hammer", "Bill Conti", "Henry Mancini"],
        2
    ),
    (
        "In what fictional or unnamed metropolitan setting was Hill Street Blues located?",
        "An unnamed gritty northern rust-belt metropolis",
        ["New York City", "Los Angeles", "Philadelphia"],
        2
    ),
    (
        "What legendary production studio founded by Mary Tyler Moore and Grant Tinker produced Hill Street Blues?",
        "MTM Enterprises",
        ["Universal Television", "Stephen J. Cannell Productions", "Lorimar Television"],
        1
    ),
    (
        "Which veteran actor played Lieutenant Ray Calletano, the precinct's proud Hispanic division coordinator?",
        "Rene Enriquez",
        ["Edward James Olmos", "Henry Darrow", "A Martinez"],
        3
    ),
    (
        "Which character was the precinct's smarmy, alcoholic, camera-craving undercover vice cop?",
        "Johnny LaRue",
        ["Mick Belker", "Neal Washington", "Stan Jablonski"],
        2
    ),
    (
        "Which actor played the troubled detective Johnny LaRue on Hill Street Blues?",
        "Kiel Martin",
        ["Bruce Weitz", "Charles Haid", "Ken Olin"],
        3
    ),

    # St. Elsewhere - Textual / Plot / Characters
    (
        "What was the real name of the deteriorating South Boston public teaching hospital in St. Elsewhere?",
        "St. Eligius Hospital",
        ["Mercy General", "Boston Metropolitan", "County General"],
        1
    ),
    (
        "Who played Dr. Donald Westphall, the compassionate Director of Medicine at St. Eligius?",
        "Ed Flanders",
        ["William Daniels", "Norman Lloyd", "Ed Begley Jr."],
        3
    ),
    (
        "Who played the pompous, abrasive Chief of Surgery Dr. Mark Craig on St. Elsewhere?",
        "William Daniels",
        ["Ed Flanders", "David Morse", "Howie Mandel"],
        1
    ),
    (
        "Which real-life wife of William Daniels played his on-screen wife Ellen Craig on St. Elsewhere?",
        "Bonnie Bartlett",
        ["Marian Mercer", "Doris Roberts", "Swoosie Kurtz"],
        2
    ),
    (
        "What historic Emmy milestone did William Daniels and Bonnie Bartlett achieve in 1986 for St. Elsewhere?",
        "They became the first real-life married couple to win Emmys on the same night since 1965",
        ["They swept all comedy and drama guest categories", "They both won for writing and acting", "They were the oldest acting winners in Emmy history"],
        3
    ),
    (
        "Which actor played Dr. Victor Ehrlich, Dr. Craig's sycophantic and bumbling surgical protégé?",
        "Ed Begley Jr.",
        ["Howie Mandel", "David Morse", "Denzel Washington"],
        1
    ),
    (
        "Which future two-time Academy Award winner starred as young resident physician Dr. Philip Chandler on St. Elsewhere?",
        "Denzel Washington",
        ["Morgan Freeman", "Samuel L. Jackson", "Forest Whitaker"],
        1
    ),
    (
        "Which stand-up comedian and future game show host played ER resident Dr. Wayne Fiscus on St. Elsewhere?",
        "Howie Mandel",
        ["Bob Saget", "Drew Carey", "Ray Romano"],
        1
    ),
    (
        "Which tall dramatic actor played Dr. Jack 'Boomer' Morrison, an earnest resident who suffered numerous personal tragedies?",
        "David Morse",
        ["Mark Harmon", "Bruce Greenwood", "Ed Begley Jr."],
        2
    ),
    (
        "Which Hollywood heartthrob played plastic surgeon Dr. Robert Caldwell, who contracted HIV in season 4?",
        "Mark Harmon",
        ["Patrick Dempsey", "Pierce Brosnan", "Harry Hamlin"],
        1
    ),
    (
        "What landmark television storyline in 1986 featured Mark Harmon's character Dr. Robert Caldwell?",
        "He contracted HIV from heterosexual promiscuity and later died of AIDS",
        ["He became the first doctor to perform an artificial heart transplant", "He was convicted of medical malpractice in a criminal trial", "He survived a lethal hospital bombing"],
        2
    ),
    (
        "Which legendary stage and screen veteran played hospital administrator Dr. Peter Auschlander?",
        "Norman Lloyd",
        ["Ed Flanders", "John Huston", "E.G. Marshall"],
        2
    ),
    (
        "Who composed the gentle, melodic synthesizer theme music for St. Elsewhere?",
        "Dave Grusin",
        ["Mike Post", "Jan Hammer", "John Addison"],
        3
    ),
    (
        "What was the title of the famous, mind-bending series finale of St. Elsewhere broadcast in May 1988?",
        "The Last One",
        ["Fade to Black", "A Snowball's Chance", "Eligius Farewell"],
        3
    ),
    (
        "What shocking final reveal occurred in the closing scene of St. Elsewhere's series finale?",
        "The entire series was revealed to be a daydream inside the mind of autistic child Tommy Westphall",
        ["The hospital was demolished to build a high-rise shopping mall", "All the doctors were revealed to be patients in a psychiatric asylum", "Donald Westphall woke up from a coma after being shot in the pilot"],
        1
    ),
    (
        "What object was Tommy Westphall holding in the final scene of St. Elsewhere containing a miniature of the hospital?",
        "A snow globe",
        ["A kaleidoscope", "A music box", "A glass paperweight"],
        1
    ),
    (
        "What cultural and media theory grew out of St. Elsewhere's snow globe finale regarding hundreds of interconnected shows?",
        "The Tommy Westphall Universe Hypothesis",
        ["The MTM Crossover Matrix", "The Boston Canon Paradox", "The Bochco Multiverse"],
        3
    ),
    (
        "Who played the autistic child Tommy Westphall on St. Elsewhere?",
        "Chad Allen",
        ["Fred Savage", "Danny Pintauro", "Jeremy Miller"],
        3
    ),
    (
        "Which acclaimed creators developed St. Elsewhere before going on to create Northern Exposure?",
        "Joshua Brand and John Falsey",
        ["Steven Bochco and Terry Louise Fisher", "David E. Kelley and Mark Tinker", "Marshall Herskovitz and Edward Zwick"],
        3
    ),
    (
        "Which classic bar sitcom characters made a famous crossover appearance in a St. Elsewhere episode at a local tavern?",
        "Cheers patrons (Norm, Cliff, and Carla appeared in an episode)",
        ["Taxi drivers from the Sunshine Cab Company", "Night Court bailiffs", "Barney Miller detectives"],
        2
    ),

    # L.A. Law - Textual / Plot / Characters
    (
        "Who co-created the glossy legal drama L.A. Law alongside Steven Bochco?",
        "Terry Louise Fisher",
        ["David E. Kelley", "Dick Wolf", "John Masius"],
        2
    ),
    (
        "What was the name of the prestigious Century City law firm in L.A. Law?",
        "McKenzie, Brackman, Chaney and Kuzak",
        ["Cage & Fish", "Hamlin, Hamlin & McGill", "Florrick & Agos"],
        1
    ),
    (
        "Who played the dignified senior founding partner Leland McKenzie on L.A. Law?",
        "Richard Dysart",
        ["Alan Rachins", "Corbin Bernsen", "Harry Hamlin"],
        1
    ),
    (
        "Who played the dashing, idealistic lead trial attorney Michael Kuzak on L.A. Law?",
        "Harry Hamlin",
        ["Jimmy Smits", "Corbin Bernsen", "Blair Underwood"],
        1
    ),
    (
        "Which former Partridge Family star played Deputy DA Grace Van Owen on L.A. Law?",
        "Susan Dey",
        ["Jill Eikenberry", "Michele Greene", "Patricia Wettig"],
        3
    ),
    (
        "Who played the slick, womanizing divorce attorney Arnie Becker on L.A. Law?",
        "Corbin Bernsen",
        ["Harry Hamlin", "Jimmy Smits", "Alan Rachins"],
        1
    ),
    (
        "Which actor played the fiery, principled young litigator Victor Sifuentes on L.A. Law?",
        "Jimmy Smits",
        ["Esai Morales", "Edward James Olmos", "Blair Underwood"],
        1
    ),
    (
        "Which real-life married couple portrayed attorneys Ann Kelsey and Stuart Markowitz on L.A. Law?",
        "Jill Eikenberry and Michael Tucker",
        ["Susan Dey and Harry Hamlin", "Bonnie Bartlett and William Daniels", "Joanna Kerns and Alan Thicke"],
        1
    ),
    (
        "What mysterious intimate intimacy technique became a national pop-culture craze after Stuart shared it with Ann?",
        "The Venus Butterfly",
        ["The Velvet Whisper", "The Midnight Sonata", "The California Squeeze"],
        1
    ),
    (
        "Who played the penny-pinching, fastidious managing partner Douglas Brackman Jr.?",
        "Alan Rachins",
        ["Richard Dysart", "Larry Drake", "Michael Tucker"],
        3
    ),
    (
        "Which actor won two Primetime Emmy Awards playing the gentle, developmentally disabled clerk Benny Stulwicz?",
        "Larry Drake",
        ["Richard Dysart", "Jimmy Smits", "Blair Underwood"],
        1
    ),
    (
        "Which handsome actor joined the firm in season 2 as ambitious Ivy League associate Jonathan Rollins?",
        "Blair Underwood",
        ["Jimmy Smits", "Denzel Washington", "Courtney B. Vance"],
        3
    ),
    (
        "Which ruthless, manipulative female corporate partner was played by Diana Muldaur in seasons 4 and 5?",
        "Rosalind Shays",
        ["Cara Jean Lott", "Gwen Taylor", "Corrinne Hammond"],
        2
    ),
    (
        "What shocking, surreal death befell villainous attorney Rosalind Shays in season 5 of L.A. Law?",
        "She stepped into an open elevator shaft and plunged to her death",
        ["She was crushed by a falling marble statue in the courthouse", "She was poisoned by contaminated sushi during a merger", "Her brakes were cut on Mulholland Drive"],
        1
    ),
    (
        "How many times did L.A. Law win the Primetime Emmy Award for Outstanding Drama Series (1987, 1989, 1990, 1991)?",
        "4 times",
        ["2 times", "3 times", "6 times"],
        2
    ),
    (
        "Who composed the upbeat, saxophone-laced theme song for L.A. Law featuring a car trunk slamming shut?",
        "Mike Post",
        ["Jan Hammer", "Dave Grusin", "Bill Conti"],
        2
    ),
    (
        "What car trunk slammed shut in rhythm with the final chord of the L.A. Law opening title sequence?",
        "A customized Jaguar trunk bearing the personalized California plate 'LA LAW'",
        ["A Mercedes-Benz 560SL", "A BMW 735i", "A Rolls-Royce Corniche"],
        3
    ),
    (
        "Which young former Boston attorney joined L.A. Law as a writer and producer, later creating Ally McBeal and Boston Legal?",
        "David E. Kelley",
        ["Aaron Sorkin", "Dick Wolf", "Shawn Ryan"],
        2
    ),
    (
        "What network broadcast L.A. Law on Thursday nights at 10:00 PM throughout its peak years?",
        "NBC",
        ["CBS", "ABC", "Fox"],
        1
    ),
    (
        "Which actress played Abby Perkins, the timid associate who gradually grew into a formidable litigator?",
        "Michele Greene",
        ["Susan Dey", "Jill Eikenberry", "Amanda Donohoe"],
        3
    ),
    (
        "Which British actress played C.J. Lamb, who shared television's first prime-time lesbian kiss with Abby Perkins in 1991?",
        "Amanda Donohoe",
        ["Emma Samms", "Stephanie Beacham", "Jane Leeves"],
        2
    ),
    (
        "What was the name of the receptionist who worked the front desk of the firm across all eight seasons?",
        "Roxanne Melman",
        ["Gwen Taylor", "Corinne Flavin", "Debbie Meyers"],
        2
    ),
    (
        "Which actress portrayed Arnie Becker's devoted, long-suffering secretary Roxanne Melman?",
        "Susan Ruttan",
        ["Michele Greene", "Conchata Ferrell", "Doris Roberts"],
        2
    ),
    (
        "How many total seasons did L.A. Law run on NBC between 1986 and 1994?",
        "8 seasons",
        ["6 seasons", "7 seasons", "10 seasons"],
        2
    ),

    # Cagney & Lacey - Textual / Plot / Characters / Metatextual
    (
        "Who were the two female New York City police detectives who headlined the groundbreaking drama Cagney & Lacey?",
        "Christine Cagney and Mary Beth Lacey",
        ["Jane Tennison and Kate Longoria", "Laura Holt and Mildred Krebs", "Gina Calabrese and Trudy Joplin"],
        1
    ),
    (
        "Which actress played the single, career-driven detective Christine Cagney for the vast majority of the series?",
        "Sharon Gless",
        ["Tyne Daly", "Meg Foster", "Loretta Swit"],
        1
    ),
    (
        "Which actress played the working-class mother and married detective Mary Beth Lacey?",
        "Tyne Daly",
        ["Sharon Gless", "Alfre Woodard", "Barbara Bosson"],
        1
    ),
    (
        "Which M*A*S*H star originally played Christine Cagney in the 1981 made-for-television movie pilot?",
        "Loretta Swit",
        ["Sharon Gless", "Meg Foster", "Dixie Carter"],
        2
    ),
    (
        "Which actress played Christine Cagney in the first six-episode season before CBS insisted on recasting her?",
        "Meg Foster",
        ["Loretta Swit", "Sharon Gless", "Lee Grant"],
        2
    ),
    (
        "Why did CBS executives initially demand that Meg Foster be replaced as Christine Cagney after season 1?",
        "They felt she came across as too aggressive and non-traditional for mainstream viewers",
        ["She suffered a vocal cord injury", "She was arrested for protesting", "She demanded a higher salary than Tyne Daly"],
        3
    ),
    (
        "What unprecedented Emmy dominance did Tyne Daly and Sharon Gless achieve between 1983 and 1988?",
        "They won the Primetime Emmy for Lead Actress in a Drama Series for 6 consecutive years",
        ["They co-won the award as a tie three times", "They swept both Lead and Supporting categories", "They were the only two nominees in their category"],
        2
    ),
    (
        "How many times did Tyne Daly win the Primetime Emmy Award for Outstanding Lead Actress in a Drama for Cagney & Lacey?",
        "4 times",
        ["2 times", "3 times", "5 times"],
        2
    ),
    (
        "How many times did Sharon Gless win the Primetime Emmy Award for Outstanding Lead Actress in a Drama for Cagney & Lacey?",
        "2 times",
        ["1 time", "3 times", "4 times"],
        2
    ),
    (
        "In what Manhattan police precinct was Cagney & Lacey set?",
        "14th Precinct (Midtown South)",
        ["9th Precinct", "5th Precinct", "20th Precinct"],
        3
    ),
    (
        "Who played Mary Beth Lacey's supportive, stay-at-home construction contractor husband Harvey Lacey?",
        "John Karlen",
        ["Al Waxman", "Martin Kove", "Carl Weathers"],
        3
    ),
    (
        "Who played Lieutenant Bert Samuels, the blustery but fair precinct commander on Cagney & Lacey?",
        "Al Waxman",
        ["John Karlen", "Martin Kove", "Sidney Clute"],
        2
    ),
    (
        "Which actor, who later played Sensei John Kreese in The Karate Kid, portrayed Detective Victor Isbecki on Cagney & Lacey?",
        "Martin Kove",
        ["John Karlen", "Al Waxman", "Carl Weathers"],
        2
    ),
    (
        "What major personal health issue did Christine Cagney battle in a landmark season 6 storyline?",
        "Severe alcoholism and substance abuse",
        ["Breast cancer", "Depression and bipolar disorder", "Prescription opioid addiction"],
        2
    ),
    (
        "In what room did Christine Cagney and Mary Beth Lacey frequently hold their most intimate, confidential conversations?",
        "The women's restroom at the precinct",
        ["The squad car front seats", "The rooftop fire escape", "The basement evidence locker"],
        1
    ),
    (
        "Who created Cagney & Lacey as one of the first feminist police dramas in American television history?",
        "Barbara Avedon and Barbara Corday",
        ["Steven Bochco and Terry Louise Fisher", "Susan Harris and Paul Junger Witt", "Linda Bloodworth-Thomason"],
        3
    ),
    (
        "What television network broadcast Cagney & Lacey throughout its 1982 to 1988 run?",
        "CBS",
        ["NBC", "ABC", "Fox"],
        1
    ),
    (
        "How was Cagney & Lacey rescued from cancellation in 1983 after CBS initially dropped the series?",
        "A massive viewer letter-writing campaign spearheaded by feminist groups and fans",
        ["An executive order from the FCC", "A grant from the National Endowment for the Arts", "A major endorsement by President Ronald Reagan"],
        2
    ),
    (
        "Who composed the energetic brass-and-strings theme song used for Cagney & Lacey from season 2 onward?",
        "Bill Conti",
        ["Mike Post", "Dave Grusin", "Lalo Schifrin"],
        2
    ),
    (
        "Which veteran actor portrayed Christine Cagney's father, former police officer Charlie Cagney?",
        "Dick O'Neill",
        ["John McIntire", "Charles Durning", "Denver Pyle"],
        3
    ),
    (
        "How many total seasons of Cagney & Lacey aired on CBS?",
        "7 seasons",
        ["5 seasons", "6 seasons", "8 seasons"],
        2
    ),
    (
        "What prestigious honor did Cagney & Lacey win in 1985 and 1986 for Outstanding Drama Series?",
        "Primetime Emmy Award for Outstanding Drama Series",
        ["Peabody Institutional Award", "Golden Globe for Best Miniseries", "Directors Guild Grand Prix"],
        2
    ),
    (
        "Which actress played veteran desk officer Detective Paul La Guardia on Cagney & Lacey?",
        "Sidney Clute",
        ["Al Waxman", "John Karlen", "Dick O'Neill"],
        3
    ),
    (
        "How was veteran actor Sidney Clute honored in every episode of Cagney & Lacey following his death in 1985?",
        "His name and billing remained in the opening credits for the rest of the show's run",
        ["A dedication card appeared before every commercial break", "A bronze plaque was placed on the stationhouse set", "His character was said to be on permanent undercover duty"],
        3
    ),
    (
        "What was the title of the season 4 episode that directly tackled breast cancer examination and awareness?",
        "Mary Beth's Dilemma / Breast Cancer diagnosis storyline",
        ["A Matter of Life", "The Pink Ribbon", "Lacey's Courage"],
        3
    ),
    (
        "What was Christine Cagney's career ambition that caused frequent tension with her peers?",
        "Becoming the youngest female lieutenant and precinct commander",
        ["Earning a law degree to become District Attorney", "Transferring to the FBI Behavioral Analysis Unit", "Retiring early to write true-crime novels"],
        2
    ),
    (
        "Which acclaimed television director directed the groundbreaking pilot episode of Hill Street Blues in 1980?",
        "Robert Butler",
        ["Gregory Hoblit", "Mark Tinker", "Steven Bochco"],
        3
    ),
    (
        "Which actor portrayed the duplicitous resident Dr. Peter White, unmasked as a serial sexual predator on St. Elsewhere?",
        "Terence Knox",
        ["David Morse", "Ed Begley Jr.", "Mark Harmon"],
        3
    ),
    (
        "What was the name of the eccentric dwarf litigator played by David Rappaport in multiple episodes of L.A. Law?",
        "Hamilton Schuyler",
        ["Arthur Gold", "Murray Stone", "Oliver Wright"],
        3
    ),
    (
        "Which actor played Detective Jonah Newman, who was tragically shot and killed on Cagney & Lacey?",
        "Dan Shor",
        ["Sidney Clute", "Stephen Macht", "Robert Hegyes"],
        3
    ),
    (
        "What famous classical opera aria echoed in the background as Donald Westphall packed his office in the St. Elsewhere finale?",
        "Casta Diva from Bellini's Norma",
        ["Nessun Dorma from Turandot", "O Mio Babbino Caro from Gianni Schicchi", "La Donna e Mobile from Rigoletto"],
        3
    )
]

if __name__ == "__main__":
    build_batch(questions, 8, "tools/staging/80s_tv_shows_batch8.json")
