import sys
from make_batch import build_batch

# Batch 7: Moonlighting & Remington Steele (Bickering Romantic Detectives & Screwball Drama)
# 100 questions: 30 d1, 40 d2, 30 d3

questions = [
    # Moonlighting - Textual / Plot / Characters
    (
        "Who played the cocky, wisecracking private detective David Addison Jr. on Moonlighting?",
        "Bruce Willis",
        ["Pierce Brosnan", "Don Johnson", "Ted Danson"],
        1
    ),
    (
        "Which actress played former high-fashion model Madelyn 'Maddie' Hayes on Moonlighting?",
        "Cybill Shepherd",
        ["Stephanie Zimbalist", "Linda Evans", "Kirstie Alley"],
        1
    ),
    (
        "What was the name of the Los Angeles private investigation agency in Moonlighting?",
        "Blue Moon Detective Agency",
        ["City of Angels Investigations", "Steele Investigations", "Argus Detective Bureau"],
        1
    ),
    (
        "Why did Maddie Hayes initially want to liquidate the Blue Moon Detective Agency in the pilot?",
        "Her accountant embezzled all her money, leaving the agency as a failed tax write-off",
        ["She wanted to open a restaurant in Paris", "She was framed for corporate espionage", "She received a multimillion-dollar modeling contract"],
        2
    ),
    (
        "What rhyming telephone greeting did receptionist Agnes DiPesto always recite when answering calls?",
        "Blue Moon Detective Agency, where the stars shine bright...",
        ["City of Angels, we watch your back...", "Who done it, we run it, Blue Moon's the one...", "Private eyes watching you, Blue Moon how do you do..."],
        1
    ),
    (
        "Which actress played the eccentric, rhyming receptionist Agnes DiPesto on Moonlighting?",
        "Allyce Beasley",
        ["Doris Roberts", "Annie Potts", "Marsha Warfield"],
        1
    ),
    (
        "Which actor joined Moonlighting in season 3 as clerk and junior detective Herbert Quentin Viola?",
        "Curtis Armstrong",
        ["Bronson Pinchot", "Marc Price", "Dan Frischman"],
        2
    ),
    (
        "What classic Hollywood film style heavily influenced Moonlighting's rapid-fire, overlapping banter?",
        "Screwball comedy (such as His Girl Friday)",
        ["Film noir melodrama", "Method acting cinema verite", "Spaghetti western minimalism"],
        1
    ),
    (
        "What stylistic device did David and Maddie constantly use, talking directly to the camera and crew?",
        "Breaking the fourth wall",
        ["Voiceover interior monologue", "Split-screen parallel narrative", "Silent pantomime"],
        1
    ),
    (
        "Which legendary filmmaker delivered a special filmed on-camera introduction for 'The Dream Sequence Always Rings Twice'?",
        "Orson Welles",
        ["Alfred Hitchcock", "John Huston", "Billy Wilder"],
        1
    ),
    (
        "In what visual format was 'The Dream Sequence Always Rings Twice' filmed to pay homage to classic noir?",
        "Black and white cinematography",
        ["Sepia tone tint", "Technicolor 3-strip", "Grainy 16mm handheld"],
        2
    ),
    (
        "What Shakespearean comedy was parodied in the acclaimed season 3 episode 'Atomic Shakespeare'?",
        "The Taming of the Shrew",
        ["A Midsummer Night's Dream", "Much Ado About Nothing", "The Comedy of Errors"],
        1
    ),
    (
        "What 1980s pop-rock hit was famously performed during the wedding feast in 'Atomic Shakespeare'?",
        "Good Lovin' by The Young Rascals",
        ["Every Breath You Take by The Police", "Bad by Michael Jackson", "Faith by George Michael"],
        3
    ),
    (
        "In which season 3 episode did David and Maddie finally consummate their romantic relationship?",
        "I Am Curious... Maddie",
        ["Atomic Shakespeare", "Brother, Can You Spare a Blonde?", "Big Man on Mulberry Street"],
        2
    ),
    (
        "What famous 1963 Ronettes song played during David and Maddie's climactic romantic encounter in season 3?",
        "Be My Baby",
        ["Baby, I Love You", "Walking in the Rain", "Then He Kissed Me"],
        2
    ),
    (
        "What critical television term was frequently applied to Moonlighting after David and Maddie became a couple?",
        "Jumping the shark (losing unresolved sexual tension)",
        ["Flanderization", "Retconning", "Bottle episode exhaustion"],
        2
    ),
    (
        "Who created and served as showrunner for Moonlighting?",
        "Glenn Gordon Caron",
        ["Steven Bochco", "Michael Gleason", "Gary David Goldberg"],
        2
    ),
    (
        "Who composed the music and sang the smooth jazz theme song 'Moonlighting'?",
        "Al Jarreau (music by Lee Holdridge)",
        ["George Benson", "Kenny G", "Bobby McFerrin"],
        1
    ),
    (
        "Why were Moonlighting script pages typically 90 to 100 pages instead of the standard 60 pages?",
        "The characters spoke at double-speed with rapid overlapping dialogue",
        ["They included extensive camera choreography instructions", "Every musical cue was written out in sheet music", "Network censors required triple documentation"],
        2
    ),
    (
        "What notorious problem plagued the broadcast schedule of Moonlighting throughout its run?",
        "Severe production delays causing frequent rerun broadcasts and pre-emptions",
        ["Constant time-slot shifts by ABC to battle Dallas", "Writer guild bans on the production", "Censorship battles over language"],
        1
    ),
    (
        "What real-life behind-the-scenes relationship dynamic existed between Cybill Shepherd and Bruce Willis?",
        "Intense personal friction, feuds, and screaming arguments on set",
        ["They were secretly engaged for two years", "They had been childhood friends in New Jersey", "They co-owned a restaurant chain together"],
        2
    ),
    (
        "Which Hollywood blockbuster film launched Bruce Willis into superstar status while he was starring on Moonlighting?",
        "Die Hard",
        ["Pulp Fiction", "Armageddon", "The Sixth Sense"],
        1
    ),
    (
        "What physical injury did Bruce Willis suffer during the hiatus of season 3 that delayed production?",
        "Broken clavicle (collarbone) from a skiing accident",
        ["Torn ACL playing basketball", "Severe concussion in a motorcycle crash", "Second-degree burns from a kitchen accident"],
        3
    ),
    (
        "What real-life personal milestone for Cybill Shepherd during season 4 forced writers to separate the leads?",
        "She was pregnant with twins",
        ["She was filming a feature film in Rome", "She contracted severe pneumonia", "She was serving on a presidential commission"],
        2
    ),
    (
        "Why was creator Glenn Gordon Caron fired by ABC during the fourth season of Moonlighting?",
        "Severe budget overruns and persistent failure to deliver episodes on time",
        ["A public disagreement with network president Brandon Stoddard over politics", "Accusations of script plagiarism", "A walkout staged by the technical crew"],
        3
    ),
    (
        "In which year did Bruce Willis win the Primetime Emmy Award for Outstanding Lead Actor in a Drama Series for Moonlighting?",
        "1987",
        ["1985", "1989", "1991"],
        2
    ),
    (
        "How many Emmy nominations did Moonlighting receive for its second season in 1986?",
        "16 nominations",
        ["8 nominations", "22 nominations", "27 nominations"],
        3
    ),
    (
        "Which singer and dance legend directed and choreographed the lavish musical dream in 'Big Man on Mulberry Street'?",
        "Stanley Donen",
        ["Gene Kelly", "Bob Fosse", "Paula Abdul"],
        3
    ),
    (
        "What Billy Joel song soundtracked David Addison's elaborate dance sequence in 'Big Man on Mulberry Street'?",
        "Big Man on Mulberry Street",
        ["Uptown Girl", "The Longest Time", "Matter of Trust"],
        2
    ),
    (
        "Who played David Addison's father, David Addison Sr., on Moonlighting?",
        "Paul Sorvino",
        ["Charles Durning", "John Goodman", "Brian Keith"],
        3
    ),
    (
        "Who played Maddie Hayes's mother, Virginia Hayes, on Moonlighting?",
        "Eva Marie Saint",
        ["Lauren Bacall", "Janet Leigh", "Angela Lansbury"],
        3
    ),
    (
        "Who played Maddie Hayes's father, Alexander Hayes, on Moonlighting?",
        "Robert Webber",
        ["John Hillerman", "Don Ameche", "Lloyd Bridges"],
        3
    ),
    (
        "What was the title of the surreal final episode of Moonlighting in May 1989 where the sets are dismantled around them?",
        "Lunar Eclipse",
        ["Blue Moon Farewell", "Case Closed", "Curtain Call"],
        3
    ),
    (
        "In the series finale 'Lunar Eclipse', what television executive character tells David and Maddie that the show is canceled?",
        "An ABC network executive who orders the sets struck",
        ["The head of the Federal Communications Commission", "Their former accountant who returns from prison", "A Hollywood studio producer"],
        2
    ),
    (
        "Which actress played Annie Charnock, Maddie's cousin who has an affair with David in season 5?",
        "Virginia Madsen",
        ["Demi Moore", "Brooke Adams", "Meg Ryan"],
        3
    ),
    (
        "Which famous guest star played a hitman who hunts David in the episode 'Brother, Can You Spare a Blonde?'?",
        "Charles Rocket",
        ["Dennis Farina", "Ray Liotta", "Michael Madsen"],
        3
    ),
    (
        "What make and color of car did David Addison drive on Moonlighting?",
        "A customized 1985 BMW 635CSi in silver",
        ["A red Chevrolet Corvette convertible", "A black Porsche 928", "A white Mercedes-Benz 560SL"],
        2
    ),
    (
        "On which major television network did Moonlighting air throughout its 1985-1989 run?",
        "ABC",
        ["NBC", "CBS", "Fox"],
        1
    ),
    (
        "What Tuesday night time slot did Moonlighting dominate during its peak seasons?",
        "9:00 PM Eastern",
        ["8:00 PM Eastern", "10:00 PM Eastern", "11:00 PM Eastern"],
        2
    ),
    (
        "What Claymation character famously appeared alongside Bruce Willis in a special 1986 holiday sequence?",
        "The California Raisins",
        ["Gumby", "Davey and Goliath", "Wallace and Gromit"],
        3
    ),
    (
        "In what year did Bruce Willis marry actress Demi Moore after meeting at a screening of Stakeout?",
        "1987",
        ["1985", "1989", "1991"],
        2
    ),
    (
        "What beverage did David Addison constantly drink from a coffee mug in the office?",
        "Diet Coke / Tab",
        ["Whiskey", "Black espresso", "Mountain Dew"],
        3
    ),
    (
        "What was the name of the detective agency before Maddie Hayes changed it to Blue Moon?",
        "City of Angels Investigations",
        ["Sunset Strip Detectives", "Pacific Coast Inquiries", "Apex Security"],
        3
    ),
    (
        "Which Motown hit did David Addison routinely sing while sliding down office hallways?",
        "Ain't No Mountain High Enough",
        ["My Girl", "I Heard It Through the Grapevine", "Signed, Sealed, Delivered"],
        2
    ),
    (
        "What was Herbert Viola's mother's profession as revealed in season 4?",
        "A probation officer",
        ["A high school librarian", "A bakery owner", "A seamstress"],
        3
    ),
    (
        "What was the title of the season 2 Christmas episode that ended with the cast singing 'The First Noel' to the camera?",
        "'Twas the Episode Before Christmas",
        ["Blue Moon Yule", "A Christmas Case", "Silent Night, Deadly Night"],
        3
    ),
    (
        "Which famous British rock group's song served as the title for the episode 'Every Daughter's Father Is a Virgin'?",
        "Elvis Costello / Nick Lowe (song allusion)",
        ["The Beatles", "The Rolling Stones", "The Who"],
        3
    ),
    (
        "How many total episodes of Moonlighting were produced across its five seasons?",
        "66 episodes",
        ["88 episodes", "102 episodes", "45 episodes"],
        3
    ),
    (
        "What phrase appeared on screen at the very end of the final Moonlighting episode?",
        "Blue Moon Investigations was never just a job... it was a love affair. Dedicated to the memory of our viewers.",
        ["That's all, folks!", "Tune in for the movie next summer.", "We apologize for the reruns."],
        3
    ),
    (
        "Which iconic comedy team's fast cross-talk did Glenn Gordon Caron explicitly cite as his structural model for Moonlighting?",
        "Spencer Tracy and Katharine Hepburn",
        ["Laurel and Hardy", "The Marx Brothers", "Burns and Allen"],
        2
    ),

    # Remington Steele - Textual / Plot / Characters
    (
        "Who starred as the suave, mysterious former thief who assumed the identity of Remington Steele?",
        "Pierce Brosnan",
        ["Timothy Dalton", "Roger Moore", "Bruce Willis"],
        1
    ),
    (
        "Which actress starred as licensed private investigator Laura Holt on Remington Steele?",
        "Stephanie Zimbalist",
        ["Cybill Shepherd", "Sharon Gless", "Tyne Daly"],
        1
    ),
    (
        "Why did Laura Holt invent the fictitious male detective Remington Steele to front her agency?",
        "Clients in the 1980s refused to hire a female private investigator",
        ["To evade an arrest warrant from the FBI", "To qualify for a corporate license", "To collect insurance money from a deceased partner"],
        1
    ),
    (
        "How did Pierce Brosnan's character come to assume the real-life persona of Remington Steele?",
        "He stumbled across Laura's deception while working a heist and stepped into the role",
        ["He was hired by Laura from an acting agency", "He was Laura's estranged ex-husband", "He won the identity in a poker game in Monaco"],
        1
    ),
    (
        "What was Remington Steele's signature method for solving baffling criminal cases?",
        "Drawing parallels to classic Hollywood movies and their plot twists",
        ["Analyzing microscopic soil samples", "Consulting an astrological horoscope", "Using electronic wiretapping gadgets"],
        1
    ),
    (
        "Which classic Hollywood screen idol was Pierce Brosnan's portrayal of Remington Steele heavily based upon?",
        "Cary Grant",
        ["Humphrey Bogart", "John Wayne", "Clark Gable"],
        1
    ),
    (
        "What was the real birth name of Pierce Brosnan's character on Remington Steele?",
        "His real name was never canonically revealed",
        ["Harry Trevor", "Paul Michaels", "Alistair Finch"],
        2
    ),
    (
        "Which veteran actress played Mildred Krebs, the former IRS auditor who became Steele's loyal associate in season 2?",
        "Doris Roberts",
        ["Estelle Getty", "Alice Ghostley", "Marion Ross"],
        1
    ),
    (
        "What was Mildred Krebs's profession before joining Remington Steele Investigations?",
        "IRS (Internal Revenue Service) field investigator",
        ["Bail bond agent", "Police homicide detective", "Customs inspector"],
        2
    ),
    (
        "Which actor played Laura Holt's detective partner and romantic rival Murphy Michaels in season 1?",
        "James Read",
        ["Curtis Armstrong", "Scott Valentine", "Jeff MacKay"],
        2
    ),
    (
        "Why did actor James Read leave Remington Steele after the first season?",
        "Producers wanted to focus entirely on the romantic chemistry between Laura and Steele",
        ["He signed a contract with Dallas", "He broke his leg filming a stunt", "He was fired for creative disputes"],
        3
    ),
    (
        "Who played Bernice Foxe, Laura's quirky receptionist during season 1 of Remington Steele?",
        "Janet DeMay",
        ["Allyce Beasley", "Doris Roberts", "Annie Potts"],
        3
    ),
    (
        "Who co-created Remington Steele alongside Robert Butler?",
        "Michael Gleason",
        ["Glenn Gordon Caron", "Steven Bochco", "Donald P. Bellisario"],
        2
    ),
    (
        "Which legendary Hollywood producer's company (MTM Enterprises) produced Remington Steele?",
        "Mary Tyler Moore (MTM Enterprises)",
        ["Aaron Spelling Productions", "Stephen J. Cannell Productions", "Universal Television"],
        2
    ),
    (
        "What high-profile cinematic role was Pierce Brosnan officially offered in 1986 following the apparent cancellation of Remington Steele?",
        "James Bond in The Living Daylights",
        ["Batman in Tim Burton's Batman", "Indiana Jones in The Last Crusade", "Sherlock Holmes in Young Sherlock Holmes"],
        1
    ),
    (
        "Why did Pierce Brosnan lose the role of James Bond in 1986 after it was announced in the press?",
        "NBC reversed its cancellation of Remington Steele due to the publicity, enforcing his contract",
        ["He failed a weapons training exam at Pinewood Studios", "He demanded more money than producer Cubby Broccoli offered", "He contracted mononucleosis during pre-production"],
        1
    ),
    (
        "Which producer refused to let Pierce Brosnan play James Bond while under contract to a weekly TV series?",
        "Albert R. 'Cubby' Broccoli",
        ["Harry Saltzman", "Irwin Allen", "Dino De Laurentiis"],
        2
    ),
    (
        "Who was cast as James Bond in The Living Daylights after Pierce Brosnan was forced back to Remington Steele?",
        "Timothy Dalton",
        ["Roger Moore", "Sean Connery", "Sam Neill"],
        1
    ),
    (
        "In what year did Pierce Brosnan finally make his debut as James Bond in GoldenEye?",
        "1995",
        ["1989", "1993", "1997"],
        1
    ),
    (
        "How did NBC resolve the contract dispute with Brosnan and Zimbalist for season 5?",
        "They produced a shortened final season of six two-hour television movies shot in Europe",
        ["They filmed a full 22-episode season in Canada", "They recast both lead roles with new actors", "They released a theatrical feature film"],
        2
    ),
    (
        "Which major film role did Stephanie Zimbalist reportedly lose because NBC renewed Remington Steele for season 5?",
        "Officer Anne Lewis in RoboCop",
        ["Vicky Vale in Batman", "Clarice Starling in The Silence of the Lambs", "Marion Ravenwood in Raiders"],
        3
    ),
    (
        "What was the title of the season 5 premiere episode filmed on location in Ireland?",
        "The Steele That Wouldn't Die",
        ["Steele in the Emerald Isle", "A Bond of Steele", "Steele Across the Atlantic"],
        3
    ),
    (
        "Who was revealed to be Remington Steele's con-artist mentor and possible biological father, played by Efrem Zimbalist Jr.?",
        "Daniel Chalmers",
        ["Arthur Cabot", "Jonathan Vance", "William Steele"],
        2
    ),
    (
        "What real-life family connection existed between Efrem Zimbalist Jr. and Stephanie Zimbalist?",
        "They were father and daughter in real life",
        ["They were uncle and niece", "They were first cousins", "They had no relation; it was a coincidence"],
        2
    ),
    (
        "What 1941 Humphrey Bogart film classic was referenced in the Remington Steele pilot 'License to Steele'?",
        "The Maltese Falcon",
        ["Casablanca", "The Big Sleep", "Key Largo"],
        2
    ),
    (
        "What make and model of classic convertible did Laura Holt drive in the early seasons of Remington Steele?",
        "1936 Auburn 851 Boattail Speedster replica",
        ["1957 Chevrolet Corvette", "1965 Ford Mustang convertible", "1955 Porsche 356 Speedster"],
        3
    ),
    (
        "Who composed the elegant, jazzy theme music for Remington Steele?",
        "Henry Mancini",
        ["Jan Hammer", "Mike Post", "Lalo Schifrin"],
        2
    ),
    (
        "What was the signature graphic feature of the MTM kitten at the end of Remington Steele credits?",
        "The MTM kitten wore a deerstalker detective hat like Sherlock Holmes",
        ["The kitten held a magnifying glass", "The kitten had a mustache like Tom Selleck", "The kitten was dressed in a tuxedo"],
        2
    ),
    (
        "Which network broadcast Remington Steele from 1982 to 1987?",
        "NBC",
        ["CBS", "ABC", "Fox"],
        1
    ),
    (
        "In what time slot did Remington Steele air during its peak ratings on Tuesday nights?",
        "10:00 PM Eastern (following The A-Team and Riptide)",
        ["8:00 PM Eastern", "9:00 PM Eastern", "11:30 PM Eastern"],
        2
    ),
    (
        "How many total seasons of Remington Steele were broadcast on NBC?",
        "5 seasons",
        ["4 seasons", "6 seasons", "7 seasons"],
        2
    ),
    (
        "What European countries served as glamorous backdrops for the fifth and final season of Remington Steele?",
        "Ireland, England, and Malta",
        ["France, Italy, and Switzerland", "Spain, Portugal, and Greece", "Germany, Austria, and Monaco"],
        3
    ),
    (
        "What was the name of Laura Holt's mother, played by Beverly Garland on Remington Steele?",
        "Abigail Holt",
        ["Margaret Holt", "Eleanor Holt", "Dorothy Holt"],
        3
    ),
    (
        "What was the title of the season 3 episode set at a Cannes film festival where Steele is framed for murder?",
        "Steele at It",
        ["Blue Movie Steele", "Steele in the Sun", "Cinematic Steele"],
        2
    ),
    (
        "Which famous British actor played Steele's former criminal associate Major Descoine?",
        "Peter Burton",
        ["David Warner", "Patrick Macnee", "John Hurt"],
        3
    ),
    (
        "What character did Geena Davis play in a season 3 episode of Remington Steele?",
        "A private investigator named Newton Crosby",
        ["A museum jewel curator", "Steele's former fiancée", "A high school classmate of Laura"],
        3
    ),
    (
        "What was the name of the white-collar security firm where Laura Holt worked before founding her own agency?",
        "Havenhurst Security",
        ["Pinkerton Agency", "Inter-Continental Protection", "National Inquiries"],
        3
    ),
    (
        "What weapon did Remington Steele famously dislike carrying or using, preferring his wits?",
        "Handguns / firearms",
        ["Pocket knives", "Tasers", "Brass knuckles"],
        2
    ),
    (
        "What was the primary filming studio lot for the interior offices of Remington Steele?",
        "CBS Studio Center (Radford) in Studio City, California",
        ["Universal Studios Hollywood", "Paramount Studios", "Burbank Warner Bros. Studios"],
        3
    ),
    (
        "In the final television movie of season 5, what did Laura and Steele finally agree to do?",
        "Commit to a genuine romantic partnership and marriage",
        ["Retire from private investigation and move to Ireland", "Sell the agency to Mildred Krebs", "Part ways forever at Heathrow Airport"],
        2
    ),
    (
        "What was Cybill Shepherd's character Maddie Hayes's lucrative career before discovering her embezzlement on Moonlighting?",
        "High-fashion runway and print model",
        ["Wall Street stockbroker", "Corporate attorney", "Opera soprano"],
        1
    ),
    (
        "What was the title of Bruce Willis's platinum-selling 1987 R&B musical album released during his Moonlighting fame?",
        "The Return of Bruno",
        ["Moonlight Serenade", "Under the Boardwalk", "Secret Agent Man"],
        1
    ),
    (
        "What signature formal attire did Pierce Brosnan's character wear almost constantly to project sophistication on Remington Steele?",
        "A tailored three-piece suit",
        ["A leather flight jacket", "A velvet tuxedo", "A trench coat with fedora"],
        1
    ),
    (
        "What was Laura Holt's profession throughout all five seasons of Remington Steele?",
        "Licensed private investigator",
        ["Criminal defense attorney", "Bounty hunter", "Forensic pathologist"],
        1
    ),
    (
        "What was the name of the glamorous shampoo brand that Maddie Hayes famously promoted in commercials before Moonlighting begins?",
        "Blue Moon Shampoo",
        ["Silk & Satin", "Golden Tresses", "Sunburst Shampoo"],
        1
    ),
    (
        "Which alcoholic beverage company signed Bruce Willis to a high-profile multi-million dollar commercial campaign in the mid-1980s?",
        "Seagram's Wine Coolers",
        ["Budweiser", "Bartles & Jaymes", "Miller Lite"],
        2
    ),
    (
        "What classic 1942 Humphrey Bogart and Ingrid Bergman wartime romance did Remington Steele repeatedly quote during romantic cases?",
        "Casablanca",
        ["The Maltese Falcon", "To Have and Have Not", "Sabrina"],
        2
    ),
    (
        "What concealed handgun did Laura Holt typically carry in her purse or holster on Remington Steele?",
        "A snub-nosed .38 Special revolver",
        ["A Glock 17", "A Beretta 92FS", "A Colt .45 semi-automatic"],
        2
    ),
    (
        "What was the title of the feature-length pilot movie that launched Moonlighting on ABC in March 1985?",
        "Moonlighting (The Pilot)",
        ["Pilot to Steele", "The First Case", "City of Angels"],
        2
    ),
    (
        "Which legendary Motown group's song 'Psychedelic Shack' was spoofed by David Addison in a season 4 hallway sequence?",
        "The Temptations",
        ["The Four Tops", "The Miracles", "The Jackson 5"],
        2
    )
]

if __name__ == "__main__":
    build_batch(questions, 7, "tools/staging/80s_tv_shows_batch7.json")
