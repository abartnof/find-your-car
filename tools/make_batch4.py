#!/usr/bin/env python3
"""
Generate Batch 4: 90s Black Sitcom Renaissance (100 questions)
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from sitcom_builder import make_batch

q_batch4 = [
    # The Fresh Prince of Bel-Air (25 questions)
    {
        "q": "What city and neighborhood did Will Smith's character move from before arriving in affluent Bel-Air, California?",
        "correct": "West Philadelphia, Pennsylvania",
        "distractors": ["South Bronx, New York", "South Side Chicago, Illinois", "East Baltimore, Maryland"],
        "d": 1
    },
    {
        "q": "What song by Tom Jones famously accompanied Alfonso Ribeiro's arm-swinging, hip-swaying 'Carlton Dance'?",
        "correct": "It's Not Unusual",
        "distractors": ["What's New Pussycat?", "She's a Lady", "Delilah"],
        "d": 1
    },
    {
        "q": "What was Uncle Phil's official judicial and legal title on The Fresh Prince of Bel-Air?",
        "correct": "Superior Court Judge (Philip Banks)",
        "distractors": ["Appellate Court Justice", "District Attorney of Los Angeles", "Chief Magistrate Judge"],
        "d": 1
    },
    {
        "q": "Why was the famous clip of Uncle Phil physically hurling Jazz out the front doors reused across dozens of episodes?",
        "correct": "DJ Jazzy Jeff refused to keep taking painful falls, so producers filmed one take wearing a specific shirt and reused it",
        "distractors": ["The front entrance set was damaged during an earthquake in Season 2", "James Avery injured his rotator cuff throwing him in the pilot", "The director wanted a cartoonish running visual gag that looked identical every time"],
        "d": 2
    },
    {
        "q": "What was the full name and former athletic background of the Banks family's dry-witted English butler Geoffrey?",
        "correct": "Geoffrey Barbara Butler, former Olympic track runner",
        "distractors": ["Geoffrey Arthur Higgins, former Royal Navy boxer", "Geoffrey Charles Sterling, former Wimbledon tennis coach", "Geoffrey Edward Vance, former cricket champion"],
        "d": 2
    },
    {
        "q": "What real-life financial emergency led 21-year-old rapper Will Smith to accept Quincy Jones' offer to star in the sitcom?",
        "correct": "He owed $2.8 million to the IRS in unpaid back taxes after reckless spending",
        "distractors": ["He was sued for copyright infringement over 'Parents Just Don't Understand'", "His record label went bankrupt and withheld all album royalties", "He lost his recording studio in a bad real estate investment"],
        "d": 2
    },
    {
        "q": "Which actress originated the role of Aunt Vivian Banks for the first three seasons before being replaced by Daphne Maxwell Reid?",
        "correct": "Janet Hubert-Whitten",
        "distractors": ["Jackée Harry", "Phylicia Rashad", "Lynn Whitfield"],
        "d": 1
    },
    {
        "q": "In the acclaimed dramatic Season 4 episode 'Papa's Got a Brand New Excuse', who plays Will's deadbeat father Lou who abandons him again?",
        "correct": "Ben Vereen",
        "distractors": ["Ron Glass", "Glynn Turman", "Richard Roundtree"],
        "d": 1
    },
    {
        "q": "What iconic tearful line does Will deliver to Uncle Phil at the end of 'Papa's Got a Brand New Excuse' before breaking down in tears?",
        "correct": "How come he don't want me, man?",
        "distractors": ["Why didn't he love me, Uncle Phil?", "I don't need him anyway, do I?", "He was never my real father!"],
        "d": 1
    },
    {
        "q": "What tragic and absurd accident claims the life of Hilary Banks' fiancé Trevor in Season 4?",
        "correct": "He proposes to Hilary while bungee jumping on live television and his cord snaps",
        "distractors": ["He is hit by a helicopter propeller while skydiving into a stadium", "His hot air balloon drifts into high-voltage power lines", "He crashes an experimental speed boat off Malibu"],
        "d": 2
    },
    {
        "q": "What R&B vocal group was baby Nicky Banks (Nicholas Andrew Michael Shawn Nathan Wanya Banks) named after?",
        "correct": "Boyz II Men",
        "distractors": ["Jodeci", "New Edition", "Color Me Badd"],
        "d": 1
    },
    {
        "q": "How did Will Smith customize his strict Bel-Air Academy prep school uniform jacket?",
        "correct": "He turned it completely inside-out to reveal the bright paisley lining",
        "distractors": ["He cut off the sleeves and replaced them with leather", "He spray-painted graffiti tags on the lapels", "He wore it backwards with neon yellow buttons"],
        "d": 1
    },
    {
        "q": "What real-life sources did Alfonso Ribeiro credit for inspiring the famous 'Carlton Dance'?",
        "correct": "Courteney Cox in Bruce Springsteen's 'Dancing in the Dark' video and Eddie Murphy's 'white man dance'",
        "distractors": ["Carlton Fisk's 1975 World Series home run wave and Michael Jackson's 'Thriller'", "Fred Astaire's tap solos and David Byrne's Talking Heads choreography", "John Travolta in Saturday Night Fever and Axl Rose's snake dance"],
        "d": 2
    },
    {
        "q": "In the series finale 'I, Done', which classic 1970s TV sitcom couple makes a cameo appearance as the buyers purchasing the Banks mansion?",
        "correct": "George and Louise Jefferson (The Jeffersons)",
        "distractors": ["Fred and Lamont Sanford (Sanford and Son)", "James and Florida Evans (Good Times)", "Cliff and Clair Huxtable (The Cosby Show)"],
        "d": 2
    },
    {
        "q": "What supermodel made a recurring appearance in Season 4 as Will's sharp-tongued childhood friend and college rival Jackie Ames?",
        "correct": "Tyra Banks",
        "distractors": ["Naomi Campbell", "Cindy Crawford", "Beverly Peele"],
        "d": 2
    },
    {
        "q": "Which actress played Lisa Wilkes, Will's serious college fiancée who leaves him at the altar twice?",
        "correct": "Nia Long",
        "distractors": ["Lela Rochon", "Vivica A. Fox", "Garcelle Beauvais"],
        "d": 2
    },
    {
        "q": "Which acclaimed actor guest starred in Season 1 as Will's rough-around-the-edges Philadelphia buddy 'Ice Tray'?",
        "correct": "Don Cheadle",
        "distractors": ["Cuba Gooding Jr.", "Forest Whitaker", "Terrence Howard"],
        "d": 2
    },
    {
        "q": "What prestigious dance studio scene in Season 3 showcased Janet Hubert's incredible professional dancing talent?",
        "correct": "Her Broadway dance audition performing to C+C Music Factory's 'Gonna Make You Sweat'",
        "distractors": ["Her tap battle against Carlton at the country club", "Her ballet solo during the Bel-Air Academy charity recital", "Her salsa routine with Uncle Phil at their anniversary gala"],
        "d": 2
    },
    {
        "q": "In Season 5's dramatic episode 'Bullets Over Bel-Air', what traumatic event lands Will in the hospital?",
        "correct": "He is shot by an armed robber at an ATM while Carlton watches helplessly",
        "distractors": ["He is caught in a drive-by shooting outside a bowling alley", "He is assaulted during a carjacking on the freeway", "He falls from a second-story balcony chasing a burglar"],
        "d": 2
    },
    {
        "q": "In which Los Angeles neighborhood is the real-life stately mansion used for the exterior shots of the Banks residence actually located?",
        "correct": "Brentwood",
        "distractors": ["Bel-Air", "Beverly Hills", "Holmby Hills"],
        "d": 3
    },
    {
        "q": "What hit single did Tatyana Ali (Ashley Banks) release in 1998, produced by Will Smith?",
        "correct": "Daydreamin'",
        "distractors": ["Make Up Your Mind", "Boy You Knock Me Out", "Everytime"],
        "d": 2
    },
    {
        "q": "In Season 3, who is Uncle Phil's corrupt political mentor who unexpectedly dies of a heart attack during an election debate?",
        "correct": "Judge Carl Robertson",
        "distractors": ["Judge Harrison Ross", "Senator Malcolm Davis", "Councilman Arthur Vance"],
        "d": 3
    },
    {
        "q": "What was the name of Carlton's cherished stuffed childhood toy that he hid from everyone?",
        "correct": "Captain Ted",
        "distractors": ["Baron Bear", "Sir Cuddles", "General Snuggles"],
        "d": 2
    },
    {
        "q": "Who wrote and executive produced The Fresh Prince of Bel-Air alongside Quincy Jones, having previously produced The Cosby Show?",
        "correct": "Andy and Susan Borowitz",
        "distractors": ["David Crane and Marta Kauffman", "Yvette Lee Bowser and Matt Williams", "Warren Littlefield and Brandon Tartikoff"],
        "d": 2
    },
    {
        "q": "In Season 6, where does Carlton Banks gain acceptance to pursue his dream college education?",
        "correct": "Princeton University",
        "distractors": ["Harvard University", "Yale University", "Columbia University"],
        "d": 1
    },

    # Martin (20 questions)
    {
        "q": "What Detroit radio station employed Martin Payne as a morning talk show host in the early seasons?",
        "correct": "WZUP 'Lover's Radio'",
        "distractors": ["WXYZ Detroit", "KDET Talk Radio", "WROC Power 98"],
        "d": 1
    },
    {
        "q": "Who played Martin's sweet, stylish girlfriend and later wife, Gina Waters?",
        "correct": "Tisha Campbell",
        "distractors": ["Tichina Arnold", "Vivica A. Fox", "Erika Alexander"],
        "d": 1
    },
    {
        "q": "What was the name of Gina's fiercely loyal, sharp-tongued best friend who constantly exchanged savage insults with Martin?",
        "correct": "Pamela 'Pam' James",
        "distractors": ["Sheneneh Jenkins", "Maxine Shaw", "Regine Hunter"],
        "d": 1
    },
    {
        "q": "What running joke regarding Martin's best friend Tommy Strawn (Thomas Mikal Ford) persisted throughout the entire series?",
        "correct": "Nobody had any idea what his actual job was, prompting the phrase 'Tommy, you ain't got no job!'",
        "distractors": ["He was secretly a multimillionaire lottery winner who pretended to be broke", "He had been engaged to seven different women without ever getting married", "He claimed to be a former professional athlete but couldn't dribble a basketball"],
        "d": 1
    },
    {
        "q": "What was the name of Martin's slow-witted, towering friend who still lived with his mother Big Shirley and worked at Men on the Move?",
        "correct": "Cole Brown",
        "distractors": ["Bruh-Man", "Stan Winters", "Jerome"],
        "d": 1
    },
    {
        "q": "Which of the following was NOT one of the many alter egos portrayed by Martin Lawrence on Martin?",
        "correct": "Stefan Urquelle",
        "distractors": ["Sheneneh Jenkins", "Jerome the Pimp", "Dragonfly Jones"],
        "d": 1
    },
    {
        "q": "What was the name of Sheneneh Jenkins' neighborhood hair salon across the street?",
        "correct": "Sho' Nuff Hair Salon",
        "distractors": ["Weave World", "Classy Cuts by Sheneneh", "Diva Locks"],
        "d": 1
    },
    {
        "q": "What was the catchphrase of Jerome, the 1970s gold-toothed, velvet-wearing playa from Detroit?",
        "correct": "Jerome's in the house, watch your mouth!",
        "distractors": ["Can you dig it, baby!", "Keep it smooth, keep it real!", "Ain't no playa like me!"],
        "d": 1
    },
    {
        "q": "What was the trademark greeting and entry habit of Bruh-Man 'from the fifth floor' (Reginald Ballard)?",
        "correct": "Climbing through Martin's fire escape window, holding up four fingers, and stealing food while saying 'Just chillin'!'",
        "distractors": ["Banging on the front door with a wrench and asking for change", "Crawling out of the laundry chute wearing Martin's bathrobes", "Dropping through the roof skylight to borrow cable TV"],
        "d": 1
    },
    {
        "q": "What martial arts discipline did Martin Lawrence's inept fighter alter ego Dragonfly Jones claim to master?",
        "correct": "Kenpo Karate (taught by Sifu Cliff St. Croix)",
        "distractors": ["Tae Kwon Do", "Judo Jujitsu", "Drunken Boxing"],
        "d": 2
    },
    {
        "q": "Why was Tisha Campbell notably absent from multiple episodes of Season 5 and barred from appearing in scenes with Martin Lawrence?",
        "correct": "She filed a lawsuit alleging sexual harassment and hostile working conditions against Lawrence",
        "distractors": ["She took a leave of absence to star in the Broadway musical Chicago", "A contract renegotiation dispute over syndication rights stalled production", "She suffered severe injuries in an automobile accident in Atlanta"],
        "d": 2
    },
    {
        "q": "What was Martin's go-to dismissal phrase whenever an unwelcome visitor overstayed their welcome in his apartment?",
        "correct": "Get ta steppin'!",
        "distractors": ["Hit the bricks!", "Take a hike!", "Bounce out of here!"],
        "d": 1
    },
    {
        "q": "What was the physical appearance and demeanor of Martin's overbearing mother, Mama Payne?",
        "correct": "She wore house dresses, had a faint mustache, and harbored intense hatred toward Gina",
        "distractors": ["She was a glamorous church choir soloist who refused to eat meat", "She wore aviator sunglasses and communicated through megaphone sirens", "She was a wealthy socialite who owned three Detroit bowling alleys"],
        "d": 2
    },
    {
        "q": "What television public access and local talk show did Martin host after losing his radio job at WZUP?",
        "correct": "Word on the Street",
        "distractors": ["Detroit Live with Martin", "The Payne Truth Hour", "Urban Voices"],
        "d": 2
    },
    {
        "q": "What was the name of the elderly security guard alter ego played by Martin Lawrence who spoke in incoherent, wheezing murmurs?",
        "correct": "Ol' Otis",
        "distractors": ["Pops", "Old Man Jenkins", "Deacon Harris"],
        "d": 2
    },
    {
        "q": "In the Season 5 series finale 'California, Here We Come', why do Martin and Gina pack up their Detroit life and move to California?",
        "correct": "Martin gets hired to host a nationally syndicated television talk show and Gina gets promoted",
        "distractors": ["Gina is accepted into Stanford Law School and Martin opens a comedy club", "They win a Beverly Hills mansion in a charity sweepstakes", "Martin signs a recording contract with Quincy Jones"],
        "d": 2
    },
    {
        "q": "Who portrayed Stan Winters, the sleazy, track-suit-wearing station manager of WZUP in the first two seasons?",
        "correct": "Garrett Morris (original SNL cast member)",
        "distractors": ["John Witherspoon", "Bernie Mac", "Clifton Powell"],
        "d": 2
    },
    {
        "q": "What was the name of Pam's corporate public relations firm employer where Gina also worked as an executive?",
        "correct": "The Anderson Group (headed by Mr. Anderson)",
        "distractors": ["Omni Media Relations", "Detroit Marketing Partners", "Sterling Advertising"],
        "d": 3
    },
    {
        "q": "What iconic line did Martin deliver whenever he apologized to Gina and softened his arrogant bravado?",
        "correct": "You go, girl! / My bad!",
        "distractors": ["I hear you, baby!", "Forgive the kid!", "Peace and love, honey!"],
        "d": 2
    },
    {
        "q": "What was the name of Sheneneh's equally loud and obnoxious best friend played by Yo-Yo?",
        "correct": "Keylolo",
        "distractors": ["Bonquisha", "Rochelle", "Tamika"],
        "d": 2
    },

    # Living Single (20 questions)
    {
        "q": "In what New York City borough and neighborhood did the four female friends share a brownstone on Living Single?",
        "correct": "Park Slope, Brooklyn",
        "distractors": ["Harlem, Manhattan", "Astoria, Queens", "South Bronx"],
        "d": 1
    },
    {
        "q": "What urban lifestyle and culture publication was founded and edited by Khadijah James (Queen Latifah)?",
        "correct": "Flavor Magazine",
        "distractors": ["Vibe City", "Urban Edge", "New York Beat"],
        "d": 1
    },
    {
        "q": "What was the high-powered legal profession of Maxine 'Max' Shaw, played by Erika Alexander?",
        "correct": "Corporate litigator and public defense attorney",
        "distractors": ["District Attorney prosecutor", "Entertainment contracts agent", "Real estate patent attorney"],
        "d": 1
    },
    {
        "q": "What was Maxine Shaw's shameless daily habit whenever she entered Khadijah and Regine's apartment?",
        "correct": "Immediately opening their refrigerator and eating their food without asking",
        "distractors": ["Stealing Regine's designer shoes from the front hallway", "Taking naps on their couch with her shoes on", "Borrowing Khadijah's car without leaving gas money"],
        "d": 1
    },
    {
        "q": "What was Synclaire James' bubbly, upbeat vocal trademark used to express excitement or confusion?",
        "correct": "Woo woo woo!",
        "distractors": ["Yay yay yay!", "Oh boy oh boy!", "Cha-ching!"],
        "d": 1
    },
    {
        "q": "What was the occupation of the debonair, baritone-voiced neighbor Kyle Barker (T.C. Carson)?",
        "correct": "Wall Street stockbroker and investment analyst",
        "distractors": ["Architectural interior designer", "Fashion photographer", "High school literature professor"],
        "d": 1
    },
    {
        "q": "Who portrayed the vain, boutique-shopping buyer Regine Hunter, known for her massive wig collection?",
        "correct": "Kim Fields (previously Tootie on The Facts of Life)",
        "distractors": ["Kim Coles", "Jackée Harry", "T'Keyah Crystal Keymáh"],
        "d": 1
    },
    {
        "q": "What was the Midwestern hometown of lovable building handyman Overton Wakefield Jones?",
        "correct": "Cleveland, Ohio",
        "distractors": ["Detroit, Michigan", "Gary, Indiana", "Milwaukee, Wisconsin"],
        "d": 2
    },
    {
        "q": "Why is Living Single recognized as a historic milestone for African American women in television production?",
        "correct": "Creator Yvette Lee Bowser became the first African American woman to develop and showrun her own prime-time series",
        "distractors": ["It was the first television series directed entirely by Black women", "It was the first sitcom produced without network executives in the studio", "It was the first broadcast sitcom funded exclusively by Black-owned investors"],
        "d": 2
    },
    {
        "q": "Which later mega-hit NBC sitcom debuted one year after Living Single with an almost identical premise and friend dynamic?",
        "correct": "Friends",
        "distractors": ["Will & Grace", "Seinfeld", "Coupling"],
        "d": 1
    },
    {
        "q": "Who wrote and performed the opening theme song for Living Single?",
        "correct": "Queen Latifah",
        "distractors": ["Mary J. Blige", "MC Lyte", "Salt-N-Pepa"],
        "d": 1
    },
    {
        "q": "What complex relationship dynamic defined Maxine Shaw and Kyle Barker throughout four seasons?",
        "correct": "A bitter, sarcastic rivalry masking passionate, volatile romantic and sexual attraction",
        "distractors": ["A secret childhood sibling relationship revealed via adoption records", "A failed high school engagement that made them sworn enemies", "A business partnership that dissolved over stolen intellectual property"],
        "d": 1
    },
    {
        "q": "Why did T.C. Carson (Kyle Barker) leave Living Single prior to Season 5?",
        "correct": "He was fired following clashes with network executives and producers over writing quality and character direction",
        "distractors": ["He accepted a role voicing Kratos in the God of War video game series", "He left to release a jazz album and tour internationally", "He walked out over salary disputes regarding Queen Latifah's pay"],
        "d": 2
    },
    {
        "q": "Which two characters got married in an emotional ceremony at the conclusion of Season 4?",
        "correct": "Synclaire James and Overton Wakefield Jones",
        "distractors": ["Khadijah James and Scooter", "Maxine Shaw and Kyle Barker", "Regine Hunter and Dexter Knight"],
        "d": 1
    },
    {
        "q": "What was the name of Khadijah's childhood sweetheart and recurring music executive boyfriend played by Cress Williams?",
        "correct": "Terrence 'Scooter' Williams",
        "distractors": ["Alonzo Evans", "Charles Phillips", "Russell Montego"],
        "d": 2
    },
    {
        "q": "What political office did Maxine Shaw successfully campaign for and win in Season 4?",
        "correct": "New York City Alderwoman / City Council",
        "distractors": ["State Assembly Representative", "Borough President of Brooklyn", "District Court Judge"],
        "d": 2
    },
    {
        "q": "What was the name of Flavor Magazine's clumsy, reggae-loving music and arts compositor played by Shaun Baker?",
        "correct": "Russell Montego",
        "distractors": ["Ivan Campbell", "Franklin Dell", "Tripp Hamilton"],
        "d": 2
    },
    {
        "q": "Who joined the living room cast in Season 5 as Ira Lee 'Tripp' Hamilton, a songwriter subletting Kyle's old apartment?",
        "correct": "Mel Jackson",
        "distractors": ["Morris Chestnut", "Blair Underwood", "Isaiah Washington"],
        "d": 3
    },
    {
        "q": "What was the name of the upscale boutique where Regine worked as a fashion consultant and buyer in early seasons?",
        "correct": "Pache",
        "distractors": ["Vogue Chic", "Manhattan Threads", "Fifth Avenue Elegance"],
        "d": 3
    },
    {
        "q": "What surprise life milestone does Maxine Shaw experience in the fifth and final season through an anonymous sperm donor?",
        "correct": "She becomes pregnant with a baby that turns out to be fathered by Kyle Barker",
        "distractors": ["She adopts twin boys from an orphanage in Chicago", "She gives birth to triplets fathered by a French diplomat", "She undergoes IVF with her law partner"],
        "d": 2
    },

    # Sister, Sister (15 questions)
    {
        "q": "How do identical twin sisters Tia Landry and Tamera Campbell first meet after being separated at birth on Sister, Sister?",
        "correct": "They bump into each other while browsing in a Detroit shopping mall clothing store",
        "distractors": ["They are assigned as college dormitory roommates at Michigan", "They attend the same summer cheerleading camp in Chicago", "They both audition for the lead in a local high school musical"],
        "d": 1
    },
    {
        "q": "What was the occupation of Tia's adopted mother Lisa Landry, played by Jackée Harry?",
        "correct": "An outspoken seamstress and clothing designer",
        "distractors": ["A school nurse", "A real estate agent", "A jazz lounge singer"],
        "d": 1
    },
    {
        "q": "What business was owned and operated by Tamera's conservative, dignified adopted father Ray Campbell (Tim Reid)?",
        "correct": "A luxury limousine service",
        "distractors": ["A commercial dry cleaners", "An independent bookstore", "An accounting and tax firm"],
        "d": 1
    },
    {
        "q": "What was the universal dismissive catchphrase yelled at pesky, infatuated neighbor Roger Evans (Marques Houston)?",
        "correct": "Go home, Roger!",
        "distractors": ["Get lost, Roger!", "Bye bye, Roger!", "Out the door, Roger!"],
        "d": 1
    },
    {
        "q": "What historic Emmy milestone had Jackée Harry achieved prior to starring on Sister, Sister?",
        "correct": "She was the first African American actress to win the Primetime Emmy for Outstanding Supporting Actress in a Comedy Series (for 227)",
        "distractors": ["She was the first Black woman to win Lead Actress in a Comedy", "She was the youngest female performer ever nominated for an Emmy", "She was the first person to win Emmys for both acting and writing in the same year"],
        "d": 2
    },
    {
        "q": "Which network rescued Sister, Sister from cancellation after ABC dropped it following its second season?",
        "correct": "The WB",
        "distractors": ["FOX", "UPN", "CBS"],
        "d": 1
    },
    {
        "q": "What Michigan university do Tia and Tamera attend together in the college seasons of Sister, Sister?",
        "correct": "University of Michigan (Ann Arbor)",
        "distractors": ["Michigan State University", "Detroit Mercy", "Wayne State University"],
        "d": 2
    },
    {
        "q": "Which real-life R&B boy band did Marques Houston (Roger Evans) front during the run of Sister, Sister?",
        "correct": "Immature (later IMx)",
        "distractors": ["B2K", "Soul 4 Real", "Another Bad Creation"],
        "d": 1
    },
    {
        "q": "What contrasting personality traits distinguished twins Tia and Tamera on the show?",
        "correct": "Tia was the studious, serious intellectual; Tamera was the impulsive, boy-crazy free spirit",
        "distractors": ["Tia was a rebellious rock musician; Tamera was a devout church choir singer", "Tia was an aspiring supermodel; Tamera was a competitive chess champion", "Tia was an athletic tomboy; Tamera was a quiet bookworm"],
        "d": 1
    },
    {
        "q": "What was the name of the suburban Detroit high school attended by the twins and Roger?",
        "correct": "Roosevelt High School",
        "distractors": ["Lincoln High School", "Oakridge Prep", "Detroit Central High"],
        "d": 2
    },
    {
        "q": "What was the brand name of Lisa Landry's home-based fashion design business?",
        "correct": "Fashions by Lisa",
        "distractors": ["Landry Threads", "Lisa's Looks", "Detroit Chic by Lisa"],
        "d": 2
    },
    {
        "q": "Who portrayed Tia's steady college boyfriend Tyreke Scott, a mechanic turned student?",
        "correct": "RonReaco Lee",
        "distractors": ["Deon Richmond", "Kel Mitchell", "Merlin Santana"],
        "d": 2
    },
    {
        "q": "Who portrayed Tamera's college boyfriend Jordan Bennett, who wrote for the campus paper?",
        "correct": "Deon Richmond",
        "distractors": ["Donald Faison", "Jason Weaver", "Kenan Thompson"],
        "d": 2
    },
    {
        "q": "In the series finale, which romantic milestone do Lisa Landry and Victor Sims celebrate?",
        "correct": "Their wedding ceremony in Hawaii",
        "distractors": ["The launch of their Paris fashion boutique", "The birth of their newborn daughter", "Their renewal of vows at Ray's house"],
        "d": 2
    },
    {
        "q": "What real-life sibling of Tia and Tamera guest starred on Sister, Sister as a kid named Stevie?",
        "correct": "Tahj Mowry (star of Smart Guy)",
        "distractors": ["Tavior Mowry", "Marcus Mowry", "Darius Mowry"],
        "d": 1
    },

    # Moesha, The Wayans Bros., The Jamie Foxx Show, Roc (20 questions)
    {
        "q": "Which chart-topping R&B teenage singing sensation starred as Moesha Mitchell on UPN's flagship sitcom Moesha?",
        "correct": "Brandy Norwood",
        "distractors": ["Monica", "Aaliyah", "Mya"],
        "d": 1
    },
    {
        "q": "What Los Angeles neighborhood served as the home base for the Mitchell family on Moesha?",
        "correct": "Leimert Park",
        "distractors": ["Inglewood", "Compton", "Baldwin Hills"],
        "d": 2
    },
    {
        "q": "What car dealership profession was held by Moesha's father Frank Mitchell (William Allen Young)?",
        "correct": "Saturn automobile dealership sales manager",
        "distractors": ["Ford dealership general manager", "Chevrolet franchise owner", "Cadillac fleet supervisor"],
        "d": 2
    },
    {
        "q": "Which Dreamgirls Broadway legend played Moesha's high school vice-principal and new stepmother Dee Mitchell?",
        "correct": "Sheryl Lee Ralph",
        "distractors": ["Jennifer Holliday", "Patti LaBelle", "Loretta Devine"],
        "d": 1
    },
    {
        "q": "What spinoff series was created centered around Moesha's boy-crazy best friend Kim Parker (Countess Vaughn)?",
        "correct": "The Parkers",
        "distractors": ["Kim's World", "Girlfriends", "College Life"],
        "d": 1
    },
    {
        "q": "What tragic real-life event befell actor Lamont Bentley, who played Moesha's loyal friend and neighbor Hakeem Campbell?",
        "correct": "He died in a tragic car crash in southern California in 2005",
        "distractors": ["He passed away from leukemia shortly after the finale", "He was fatally wounded in a robbery in Chicago", "He drowned during a vacation in Mexico"],
        "d": 3
    },
    {
        "q": "On The WB's hit comedy The Wayans Bros., what business did brothers Shawn and Marlon Williams run in Manhattan?",
        "correct": "A newsstand inside the lobby of the Neidermeyer Building",
        "distractors": ["A courier delivery service", "A customized t-shirt printing shop", "A shoe shine and hat cleaning parlor"],
        "d": 1
    },
    {
        "q": "Which beloved character actor played Shawn and Marlon's eccentric diner-owner father John 'Pops' Williams?",
        "correct": "John Witherspoon",
        "distractors": ["Bernie Mac", "Paul Winfield", "Clifton Davis"],
        "d": 1
    },
    {
        "q": "What unappetizing soul-food specialty dish did Pops constantly push on customers at his diner?",
        "correct": "Deep-fried pig feet and chili",
        "distractors": ["Pickled possum tails", "Boiled chicken gizzards in chocolate sauce", "Smoked raccoon ribs"],
        "d": 2
    },
    {
        "q": "Who played Dee Baxter, the tough-talking, gun-toting building security guard on The Wayans Bros.?",
        "correct": "Anna Maria Horsford",
        "distractors": ["Kym Whitley", "Marsha Warfield", "Roz Ryan"],
        "d": 2
    },
    {
        "q": "What was the setting and business in Los Angeles where Jamie King worked on The Jamie Foxx Show?",
        "correct": "The King's Tower, a boutique family hotel owned by his Aunt Helen and Uncle Junior",
        "distractors": ["The Sunset Regency, a luxury Hollywood resort", "The Foxx Den, a downtown jazz and blues supper club", "King's Records, an independent studio in Burbank"],
        "d": 1
    },
    {
        "q": "Who portrayed Francesca 'Fancy' Monroe, the gorgeous hotel desk clerk who was Jamie's dream love interest?",
        "correct": "Garcelle Beauvais",
        "distractors": ["Lela Rochon", "LisaRaye McCoy", "Nia Long"],
        "d": 1
    },
    {
        "q": "What was the name of the pretentious, Harvard-obsessed hotel accountant who served as Jamie King's hilarious foil?",
        "correct": "Braxton P. Hartnabrig (Christopher B. Duncan)",
        "distractors": ["Carlton Banks", "Eugene Young", "Miles Silverberg"],
        "d": 1
    },
    {
        "q": "What city in Texas was Jamie King from before moving to Hollywood to pursue his entertainment career?",
        "correct": "Terrell",
        "distractors": ["Dallas", "Houston", "San Antonio"],
        "d": 2
    },
    {
        "q": "What historic technical feat did Fox's blue-collar sitcom Roc accomplish during its entire second season in 1992-1993?",
        "correct": "Every single episode of the entire season was broadcast completely live to the nation",
        "distractors": ["It was the first sitcom broadcast in full high-definition digital sound", "It was shot without any artificial lighting on actual Baltimore streets", "It was filmed in front of an audience composed exclusively of sanitation workers"],
        "d": 2
    },
    {
        "q": "What was Roc Emerson's (Charles S. Dutton) blue-collar occupation in Baltimore, Maryland?",
        "correct": "Sanitation worker / garbage collector",
        "distractors": ["Dockworker / stevedore", "Steel mill blast furnace operator", "City bus driver"],
        "d": 1
    },
    {
        "q": "Who played Roc's freeloading, trumpet-playing brother Joey Emerson on Roc?",
        "correct": "Rocky Carroll (later Director Leon Vance on NCIS)",
        "distractors": ["Courtney B. Vance", "Joe Morton", "Delroy Lindo"],
        "d": 2
    },
    {
        "q": "Which hip-hop superstar headlined the UPN sitcom In the House as former professional football star Marion Hill?",
        "correct": "LL Cool J",
        "distractors": ["Heavy D", "Ice-T", "Big Daddy Kane"],
        "d": 1
    },
    {
        "q": "Which legendary dancer, director, and Fame actress co-starred on In the House as single mother Jackie Warren?",
        "correct": "Debbie Allen",
        "distractors": ["Phylicia Rashad", "Diahann Carroll", "Telma Hopkins"],
        "d": 2
    },
    {
        "q": "What business venture did Malcolm McGee and Eddie Sherman operate together on the UPN sitcom Malcolm & Eddie?",
        "correct": "A Kansas City sports bar called McGee's (later a jazz club)",
        "distractors": ["A record store and DJ studio in St. Louis", "A customized limousine rental fleet in Chicago", "An auto repair and restoration garage in Cleveland"],
        "d": 2
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "staging", "90s_sitcoms_batch4.json")
    make_batch(q_batch4, 4, out)
