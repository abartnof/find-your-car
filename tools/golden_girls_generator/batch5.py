from utils import build_golden_girls_batch

RAW_QUESTIONS = [
    # 1
    {
        "q": "Which British royal family member personally requested that the cast of 'The Golden Girls' perform live at the Royal Variety Performance in London in 1988?",
        "correct": "Queen Elizabeth The Queen Mother",
        "wrong": ["Queen Elizabeth II", "Princess Margaret", "Diana, Princess of Wales"],
        "d": 1
    },
    # 2
    {
        "q": "At which iconic London venue did the cast perform their special live sketch for the Royal Family in November 1988?",
        "correct": "The London Palladium",
        "wrong": ["The Royal Albert Hall", "The Drury Lane Theatre", "The Savoy Theatre"],
        "d": 2
    },
    # 3
    {
        "q": "What question did the producers and cast face when preparing their sketch for the 1988 Royal Variety Performance?",
        "correct": "Whether to tone down Blanche's bawdy sexual innuendos for the Royal Family",
        "wrong": ["Whether to replace Estelle Getty with a British actress", "Whether to film the sketch on location in Miami beforehand", "Whether to sing the British national anthem instead of the theme"],
        "d": 2
    },
    # 4
    {
        "q": "Which character on 'The Golden Girls' was reportedly the Queen Mother's absolute favorite?",
        "correct": "Sophia Petrillo",
        "wrong": ["Rose Nylund", "Dorothy Zbornak", "Blanche Devereaux"],
        "d": 2
    },
    # 5
    {
        "q": "What did the Queen Mother tell the cast during the post-show receiving line at the London Palladium?",
        "correct": "She told them she watched the show religiously and found them utterly delightful",
        "wrong": ["She asked them to film an episode at Windsor Castle", "She questioned why they ate so much cheesecake", "She invited Betty White to care for her royal corgis"],
        "d": 2
    },
    # 6
    {
        "q": "Which future Hollywood superstar played Miami undercover vice cop Bobby Hopkins in the Season 2 episode 'To Catch a Neighbor'?",
        "correct": "George Clooney",
        "wrong": ["Brad Pitt", "Johnny Depp", "Tom Cruise"],
        "d": 1
    },
    # 7
    {
        "q": "How old was George Clooney approximately when he appeared as Officer Bobby Hopkins on 'The Golden Girls' in 1987?",
        "correct": "26 years old",
        "wrong": ["19 years old", "33 years old", "38 years old"],
        "d": 2
    },
    # 8
    {
        "q": "Which future Oscar-winning filmmaker appeared as an Elvis Presley impersonator in the 1988 episode 'Sophia's Wedding'?",
        "correct": "Quentin Tarantino",
        "wrong": ["David Fincher", "Spike Jonze", "Paul Thomas Anderson"],
        "d": 1
    },
    # 9
    {
        "q": "How did Quentin Tarantino's small cameo on 'The Golden Girls' critically impact his early filmmaking career?",
        "correct": "The SAG residual checks paid his living expenses while he wrote and pre-produced 'Reservoir Dogs'",
        "wrong": ["It introduced him to Harvey Keitel who was visiting the set", "It funded the camera rental for his debut short film", "It earned him an audition for 'Pulp Fiction'"],
        "d": 1
    },
    # 10
    {
        "q": "What iconic movie star made a memorable guest appearance in Season 2's 'Ladies of the Evening', delivering the punchline 'Which one's the slut?'?",
        "correct": "Burt Reynolds",
        "wrong": ["Clint Eastwood", "Paul Newman", "Robert Redford"],
        "d": 1
    },
    # 11
    {
        "q": "Which acclaimed comedy actor played Blanche's uncle Lucas Hollingsworth and married Dorothy in the series finale?",
        "correct": "Leslie Nielsen",
        "wrong": ["Lloyd Bridges", "Jack Lemmon", "Mel Brooks"],
        "d": 1
    },
    # 12
    {
        "q": "Which legendary Hollywood actress and singer played Trisha, a potential roommate who interviews with the girls in Season 5?",
        "correct": "Debbie Reynolds",
        "wrong": ["Shirley MacLaine", "Doris Day", "Lauren Bacall"],
        "d": 1
    },
    # 13
    {
        "q": "Which iconic entertainer guest-starred as himself in 'You Gotta Have Hope', where Rose believes he is her biological father?",
        "correct": "Bob Hope",
        "wrong": ["Bing Crosby", "Milton Berle", "Danny Kaye"],
        "d": 1
    },
    # 14
    {
        "q": "Which international pop singer guest-starred as Sophia's dream Valentine's Day date in Season 4?",
        "correct": "Julio Iglesias",
        "wrong": ["Plácido Domingo", "Enrique Iglesias", "Tom Jones"],
        "d": 1
    },
    # 15
    {
        "q": "Which future indie rock musician and lead singer of Rilo Kiley played the devious Sunshine Cadet Daisy who kidnapped Rose's teddy bear?",
        "correct": "Jenny Lewis",
        "wrong": ["Fiona Apple", "Chan Marshall", "Alanis Morissette"],
        "d": 2
    },
    # 16
    {
        "q": "Which 'Law & Order' icon played Glenn O'Brien, Dorothy's married lover who returns after his divorce in Season 5?",
        "correct": "Jerry Orbach",
        "wrong": ["Sam Waterston", "Fred Thompson", "Paul Sorvino"],
        "d": 2
    },
    # 17
    {
        "q": "Which TV veteran and 'Barney Miller' star played John Neretti, Dorothy's high school prom date who stood her up?",
        "correct": "Hal Linden",
        "wrong": ["Abe Vigoda", "Max Gail", "Ron Glass"],
        "d": 2
    },
    # 18
    {
        "q": "Which legendary 1960s TV Batman villain (The Joker) played Tony Delvecchio, a suitor who dates Sophia in Season 5?",
        "correct": "Cesar Romero",
        "wrong": ["Burgess Meredith", "Frank Gorshin", "Vincent Price"],
        "d": 2
    },
    # 19
    {
        "q": "Which Emmy-winning actor, famous for 'Arrested Development' and 'The Larry Sanders Show', played two different guest roles across the series?",
        "correct": "Jeffrey Tambor",
        "wrong": ["Garry Shandling", "Rip Torn", "Eugene Levy"],
        "d": 2
    },
    # 20
    {
        "q": "Which beloved comic actor played Sophia's bank-robbing boyfriend Rocco in Season 3?",
        "correct": "Mickey Rooney",
        "wrong": ["Red Buttons", "Don Knotts", "Jack Albertson"],
        "d": 1
    },
    # 21
    {
        "q": "Which long-time 'Jeopardy!' host played himself in Dorothy's nightmare audition in Season 7?",
        "correct": "Alex Trebek",
        "wrong": ["Art Fleming", "Pat Sajak", "Chuck Woolery"],
        "d": 1
    },
    # 22
    {
        "q": "Which media mogul and creator of 'Jeopardy!' and 'Wheel of Fortune' appeared alongside Alex Trebek in Dorothy's dream?",
        "correct": "Merv Griffin",
        "wrong": ["Mark Goodson", "Bill Todman", "Chuck Barris"],
        "d": 1
    },
    # 23
    {
        "q": "Which famous television star and singer appeared as himself in Blanche's romantic fantasy in 'Mrs. George Devereaux'?",
        "correct": "Sonny Bono",
        "wrong": ["Cher", "Gene Simmons", "Paul Anka"],
        "d": 2
    },
    # 24
    {
        "q": "Which 'Carol Burnett Show' regular appeared alongside Sonny Bono in Blanche's dream as a rival suitor?",
        "correct": "Lyle Waggoner",
        "wrong": ["Harvey Korman", "Tim Conway", "Dick Van Dyke"],
        "d": 2
    },
    # 25
    {
        "q": "Which 'Mission: Impossible' star played a suave doctor who takes Blanche out on his yacht in Season 5?",
        "correct": "Peter Graves",
        "wrong": ["Martin Landau", "Greg Morris", "Robert Conrad"],
        "d": 2
    },
    # 26
    {
        "q": "Which comedy legend played Ken, Dorothy's attorney beau who gave up the law to become a circus clown?",
        "correct": "Dick Van Dyke",
        "wrong": ["Jerry Lewis", "Carl Reiner", "Tim Conway"],
        "d": 1
    },
    # 27
    {
        "q": "Which 'Saved by the Bell' star made an early acting appearance as Mario Sanchez, Dorothy's star pupil facing deportation?",
        "correct": "Mario Lopez",
        "wrong": ["Mark-Paul Gosselaar", "Dustin Diamond", "Brian Austin Green"],
        "d": 1
    },
    # 28
    {
        "q": "Which actress played Dorothy's daughter Kate Zbornak in the Season 1 wedding episode?",
        "correct": "Lisa Jane Persky",
        "wrong": ["Deena Freeman", "Christine Ebersole", "Dinah Manoff"],
        "d": 3
    },
    # 29
    {
        "q": "Which actress replaced Lisa Jane Persky as Kate Zbornak in Season 2 when Dennis had an affair?",
        "correct": "Deena Freeman",
        "wrong": ["Lee Garlington", "Christine Ebersole", "Brenda Vaccaro"],
        "d": 3
    },
    # 30
    {
        "q": "Which Broadway star and Tony winner played Rose's suspicious daughter Kirsten in Season 8 / later episodes?",
        "correct": "Christine Ebersole",
        "wrong": ["Patti LuPone", "Bernadette Peters", "Audra McDonald"],
        "d": 3
    },
    # 31
    {
        "q": "Which actress originally played Rose's daughter Kirsten in Season 1 when Charlie's will was examined?",
        "correct": "Lee Garlington",
        "wrong": ["Christine Ebersole", "Lisa Jane Persky", "Melora Hardin"],
        "d": 3
    },
    # 32
    {
        "q": "Which character actor played Stan Zbornak in 26 episodes, earning two Primetime Emmy nominations?",
        "correct": "Herb Edelman",
        "wrong": ["Harold Gould", "Bill Dana", "Richard Libertini"],
        "d": 1
    },
    # 33
    {
        "q": "Which distinguished character actor played Rose's long-time beau Miles Webber (Nicholas Carbone)?",
        "correct": "Harold Gould",
        "wrong": ["Herb Edelman", "Edward Winter", "John Randolph"],
        "d": 1
    },
    # 34
    {
        "q": "Before playing Miles Webber, Harold Gould appeared in Season 1 of 'The Golden Girls' as which different suitor of Rose?",
        "correct": "Arnie Peterson",
        "wrong": ["Dr. Jonathan Newman", "Fidel Santiago", "Al Beatty"],
        "d": 2
    },
    # 35
    {
        "q": "Which veteran comedy actor played Sophia's Italian brother, Uncle Angelo Petrillo?",
        "correct": "Bill Dana",
        "wrong": ["Pat Cooper", "Frank Fontaine", "Jack Carter"],
        "d": 2
    },
    # 36
    {
        "q": "Which veteran TV actress played Sophia's feud-loving Sicilian sister Angela in Season 2?",
        "correct": "Nancy Walker",
        "wrong": ["Selma Diamond", "Ruth Gordon", "Alice Ghostley"],
        "d": 2
    },
    # 37
    {
        "q": "Besides playing sister Angela, what behind-the-scenes role did Nancy Walker perform on 'The Golden Girls' in Season 1?",
        "correct": "She directed four episodes of the series",
        "wrong": ["She wrote the musical score", "She was the lead casting director", "She was the head dialect coach"],
        "d": 3
    },
    # 38
    {
        "q": "Which actress played Dorothy's wealthy sister Gloria in Season 1 before the character returned in Season 7?",
        "correct": "Doris Belack",
        "wrong": ["Dena Dietrich", "Sheree North", "Barbara Babcock"],
        "d": 3
    },
    # 39
    {
        "q": "Which famous actress, known as Mother Nature in 1970s margarine commercials, played Gloria in Season 7?",
        "correct": "Dena Dietrich",
        "wrong": ["Doris Belack", "Rue McClanahan", "Charlotte Rae"],
        "d": 3
    },
    # 40
    {
        "q": "Which legendary Southern actor played Blanche's father 'Big Daddy' Hollingsworth in his first appearance in Season 1?",
        "correct": "Murray Hamilton",
        "wrong": ["David Wayne", "Denver Pyle", "Strother Martin"],
        "d": 2
    },
    # 41
    {
        "q": "Which veteran actor took over the role of 'Big Daddy' Hollingsworth in Season 2 after Murray Hamilton passed away?",
        "correct": "David Wayne",
        "wrong": ["Murray Hamilton", "Pat Hingle", "Arthur O'Connell"],
        "d": 2
    },
    # 42
    {
        "q": "Which actress played Blanche's sister Virginia in Season 1 when Virginia asked for a kidney?",
        "correct": "Sheree North",
        "wrong": ["Barbara Babcock", "Dixie Carter", "Delta Burke"],
        "d": 3
    },
    # 43
    {
        "q": "Which Emmy-winning actress played Blanche's rival sister Charmaine in Season 1?",
        "correct": "Barbara Babcock",
        "wrong": ["Sheree North", "Faye Dunaway", "Lee Grant"],
        "d": 3
    },
    # 44
    {
        "q": "Which actor played Blanche's gay brother Clayton in both Season 4 and Season 6?",
        "correct": "Monte Markham",
        "wrong": ["Richard Mulligan", "Robert Mandan", "Charles Frank"],
        "d": 2
    },
    # 45
    {
        "q": "Which actor played Dorothy's son Michael Zbornak in multiple episodes across the series?",
        "correct": "Scott Jacoby",
        "wrong": ["Rob Lowe", "Michael J. Fox", "Matthew Broderick"],
        "d": 2
    },
    # 46
    {
        "q": "What major acting honor had Scott Jacoby (Michael Zbornak) won before appearing on 'The Golden Girls'?",
        "correct": "A Primetime Emmy Award for Outstanding Supporting Actor (for 'That Certain Summer')",
        "wrong": ["A Tony Award for Best Actor", "An Academy Award for Best Supporting Actor", "A Golden Globe Award"],
        "d": 3
    },
    # 47
    {
        "q": "Which actor played Blanche's late husband George Devereaux in the dream episode 'Mrs. George Devereaux'?",
        "correct": "George Grizzard",
        "wrong": ["Richard Dysart", "Donald Moffat", "Philip Bosco"],
        "d": 3
    },
    # 48
    {
        "q": "What difference in working styles occasionally caused friction between Bea Arthur and Betty White on set?",
        "correct": "Bea was an introspective stage actress who valued quiet focus, while Betty was cheerful, chatty, and played with the audience",
        "wrong": ["Betty White constantly rewrote the scripts without telling the other actresses", "Bea Arthur refused to share dressing room hallways with Betty", "Betty White demanded top billing over Bea in the opening titles"],
        "d": 1
    },
    # 49
    {
        "q": "How did Rue McClanahan describe Bea Arthur's feelings toward Betty White in her autobiography?",
        "correct": "Bea admired Betty's talent but sometimes found her unrelenting perkiness exhausting",
        "wrong": ["They actively sabotaged each other's comedic scenes", "They refused to speak to each other unless through lawyers", "They were inseparable best friends who vacationed together every summer"],
        "d": 2
    },
    # 50
    {
        "q": "What was the title of Rue McClanahan's bestselling 2007 autobiography?",
        "correct": "My First Five Husbands... And the Ones Who Got Away",
        "wrong": ["Thank You for Being Blanche", "Golden Memories of a Southern Belle", "Life in the Lanai"],
        "d": 2
    },
    # 51
    {
        "q": "How many times was Rue McClanahan married in real life, a fact she frequently joked about in comparison to Blanche?",
        "correct": "Six times",
        "wrong": ["Three times", "Eight times", "Twice"],
        "d": 2
    },
    # 52
    {
        "q": "In what year did Estelle Getty pass away at the age of 84?",
        "correct": "2008",
        "wrong": ["2005", "2010", "2012"],
        "d": 2
    },
    # 53
    {
        "q": "What progressive neurological condition did Estelle Getty battle in the final decade of her life?",
        "correct": "Lewy body dementia",
        "wrong": ["Multiple sclerosis", "Amyotrophic lateral sclerosis (ALS)", "Huntington's disease"],
        "d": 2
    },
    # 54
    {
        "q": "In what year did Bea Arthur pass away from cancer at the age of 86?",
        "correct": "2009",
        "wrong": ["2006", "2011", "2013"],
        "d": 2
    },
    # 55
    {
        "q": "What substantial charitable bequest did Bea Arthur leave in her will to help homeless youth in New York City?",
        "correct": "$300,000 to the Ali Forney Center for homeless LGBT youth",
        "wrong": ["$1,000,000 to the Actors Fund of America", "$500,000 to the Juilliard School of Drama", "$250,000 to the ASPCA of New York"],
        "d": 2
    },
    # 56
    {
        "q": "What facility was opened in Manhattan in 2017 in honor of Bea Arthur's generous bequest to homeless LGBT youth?",
        "correct": "The Bea Arthur Residence",
        "wrong": ["The Dorothy Zbornak House", "The Arthur Memorial Shelter", "The Maude Center"],
        "d": 2
    },
    # 57
    {
        "q": "In what year did Rue McClanahan pass away from a brain hemorrhage at the age of 76?",
        "correct": "2010",
        "wrong": ["2008", "2012", "2014"],
        "d": 2
    },
    # 58
    {
        "q": "On what date did Betty White pass away, just 17 days shy of celebrating her 100th birthday?",
        "correct": "December 31, 2021",
        "wrong": ["January 17, 2022", "November 28, 2021", "February 14, 2022"],
        "d": 1
    },
    # 59
    {
        "q": "Which of the four Golden Girls actresses was the longest-surviving member of the main cast?",
        "correct": "Betty White",
        "wrong": ["Rue McClanahan", "Bea Arthur", "Estelle Getty"],
        "d": 1
    },
    # 60
    {
        "q": "In what city was the first official 'Golden-Con: Thank You for Being a Fan' convention held in April 2022?",
        "correct": "Chicago, Illinois",
        "wrong": ["Miami, Florida", "Los Angeles, California", "Atlanta, Georgia"],
        "d": 2
    },
    # 61
    {
        "q": "What unique culinary cafe dedicated to Rue McClanahan and 'The Golden Girls' opened in Manhattan's Washington Heights in 2017?",
        "correct": "Rue La Rue Cafe",
        "wrong": ["The Lanai Bakery", "Sophia's Kitchen Cafe", "Blanche's Southern Tea"],
        "d": 2
    },
    # 62
    {
        "q": "Who founded the Rue La Rue Cafe using personal memorabilia and costumes inherited from Rue McClanahan?",
        "correct": "Michael J. LaRue (Rue's close friend and executor)",
        "wrong": ["Marc Cherry", "Brandon Tartikoff", "Norman Lear"],
        "d": 3
    },
    # 63
    {
        "q": "What popular drag stage show touring major cities features all-male drag performers portraying the Golden Girls word-for-word?",
        "correct": "The Golden Girls Live! on Stage",
        "wrong": ["Queens in Miami", "Wicker Purses and Wigs", "Lanai Queens Revue"],
        "d": 2
    },
    # 64
    {
        "q": "Which major collectible toy brand released official stylized vinyl figures of Dorothy, Rose, Blanche, and Sophia in 2016?",
        "correct": "Funko (Pop! Vinyl)",
        "wrong": ["Hasbro Action Heroes", "Mattel Barbie Collector", "McFarlane Toys"],
        "d": 2
    },
    # 65
    {
        "q": "What novelty pottery plant brand produced popular Golden Girls ceramic planters that sprout green chia seeds as hair?",
        "correct": "Chia Pet",
        "wrong": ["Veg-O-Matic", "Pocket Planter", "Flora-Pot"],
        "d": 1
    },
    # 66
    {
        "q": "What popular board game company released official custom editions for 'The Golden Girls', including Clue and Monopoly?",
        "correct": "Hasbro / USAopoly",
        "wrong": ["Mattel Games", "Milton Bradley Classic", "Ravensburger"],
        "d": 2
    },
    # 67
    {
        "q": "In the custom 'Golden Girls Clue' board game, what crime are the players trying to solve?",
        "correct": "Who ate the last piece of cheesecake, with what weapon, and in what room",
        "wrong": ["Who stole Sophia's wicker purse", "Who dented Stan's car in the driveway", "Who tore Blanche's palm wallpaper"],
        "d": 1
    },
    # 68
    {
        "q": "What popular restaurant chain launched a pop-up dining experience called 'The Golden Girls Kitchen' in Beverly Hills, New York, and Chicago?",
        "correct": "Bucket Listers",
        "wrong": ["Hard Rock Cafe", "Planet Hollywood", "The Cheesecake Factory"],
        "d": 2
    },
    # 69
    {
        "q": "What food was naturally the centerpiece of the dessert menu at 'The Golden Girls Kitchen' pop-up restaurant?",
        "correct": "Cheesecake in assorted flavors",
        "wrong": ["Cannoli with powdered sugar", "Southern peach cobbler", "St. Olaf herring pie"],
        "d": 1
    },
    # 70
    {
        "q": "Which of the following actresses was offered the role of Dorothy Zbornak before Bea Arthur officially signed on?",
        "correct": "Lee Grant (who turned it down because she didn't want to play a grandmother)",
        "wrong": ["Angela Lansbury", "Lucille Ball", "Carol Burnett"],
        "d": 3
    },
    # 71
    {
        "q": "Which actress was Susan Harris's original template and ideal choice for Dorothy when writing the pilot script?",
        "correct": "Bea Arthur",
        "wrong": ["Elaine Stritch", "Maureen Stapleton", "Colleen Dewhurst"],
        "d": 2
    },
    # 72
    {
        "q": "Why was Bea Arthur initially hesitant to accept the role of Dorothy Zbornak when first approached?",
        "correct": "She worried the show would feel like an uninspired retread of 'Maude'",
        "wrong": ["She had retired from acting to live permanently in England", "She refused to work in comedy after winning a Tony for drama", "She wanted to play Blanche Devereaux instead"],
        "d": 2
    },
    # 73
    {
        "q": "Who personally called Bea Arthur and convinced her to read Susan Harris's script, assuring her it was brilliant and unique?",
        "correct": "Rue McClanahan",
        "wrong": ["Brandon Tartikoff", "Betty White", "Paul Junger Witt"],
        "d": 2
    },
    # 74
    {
        "q": "Which Broadway legend famously auditioned for the role of Dorothy Zbornak but blew the audition by cursing at creator Susan Harris?",
        "correct": "Elaine Stritch",
        "wrong": ["Patti LuPone", "Chita Rivera", "Carol Channing"],
        "d": 2
    },
    # 75
    {
        "q": "In what year did Elaine Stritch recount her disastrous Golden Girls audition in her one-woman Broadway show 'Elaine Stritch at Liberty'?",
        "correct": "2002",
        "wrong": ["1995", "2010", "1988"],
        "d": 3
    },
    # 76
    {
        "q": "What did Elaine Stritch do during her audition that she admitted cost her the role of Dorothy?",
        "correct": "She used vulgar expletives when improvising dialogue after her joke didn't land",
        "wrong": ["She walked out after three minutes saying the script was terrible", "She showed up two hours late smelling of gin", "She refused to read opposite Estelle Getty"],
        "d": 3
    },
    # 77
    {
        "q": "What did Estelle Getty wear to her final audition for Sophia to convince producers she could look like an 80-year-old woman?",
        "correct": "An oversized dowdy thrift-store dress, sensible orthotics, and unstyled graying hair",
        "wrong": ["A black Sicilian mourning veil and a cane", "Prosthetic latex wrinkles she bought at a costume shop", "A nurse's uniform from a retirement home"],
        "d": 2
    },
    # 78
    {
        "q": "Where did Estelle Getty find the signature wicker purse that became Sophia's trademark prop?",
        "correct": "She spotted it on a flea market stand during a shopping trip in Los Angeles",
        "wrong": ["It was custom-designed by the Disney prop department", "It was inherited from Bea Arthur's grandmother", "It was purchased from a high-end Beverly Hills boutique"],
        "d": 2
    },
    # 79
    {
        "q": "Which of the four Golden Girls was the only one born in California?",
        "correct": "None of them (Betty White was born in Illinois, Bea Arthur in New York, Rue McClanahan in Oklahoma, Estelle Getty in New York)",
        "wrong": ["Betty White", "Rue McClanahan", "Estelle Getty"],
        "d": 3
    },
    # 80
    {
        "q": "In which city and state was Betty White born on January 17, 1922?",
        "correct": "Oak Park, Illinois",
        "wrong": ["Chicago, Illinois", "Evanston, Illinois", "Springfield, Illinois"],
        "d": 2
    },
    # 81
    {
        "q": "In which New York borough was Estelle Getty born to Polish-Jewish immigrant parents?",
        "correct": "Manhattan (Lower East Side)",
        "wrong": ["Brooklyn (Flatbush)", "The Bronx", "Queens (Astoria)"],
        "d": 3
    },
    # 82
    {
        "q": "In which New York borough was Bea Arthur born before her family moved to Maryland?",
        "correct": "Brooklyn",
        "wrong": ["Manhattan", "Queens", "Staten Island"],
        "d": 2
    },
    # 83
    {
        "q": "In which Oklahoma town was Rue McClanahan born in 1934?",
        "correct": "Healdton, Oklahoma",
        "wrong": ["Tulsa, Oklahoma", "Oklahoma City, Oklahoma", "Norman, Oklahoma"],
        "d": 3
    },
    # 84
    {
        "q": "What Guinness World Record did Betty White earn in 2014 for her entertainment career?",
        "correct": "Longest TV career by an entertainer (female)",
        "wrong": ["Most television guest appearances in history", "Oldest person to win an Emmy Award", "Most game show appearances by a celebrity"],
        "d": 1
    },
    # 85
    {
        "q": "How many total decades did Betty White's television broadcasting career span before her death in 2021?",
        "correct": "Over eight decades (starting in 1939)",
        "wrong": ["Four decades", "Six decades", "Ten decades"],
        "d": 1
    },
    # 86
    {
        "q": "What popular sitcom did Betty White star in from 2010 to 2015 as feisty caretaker Elka Ostrovsky?",
        "correct": "Hot in Cleveland",
        "wrong": ["Mom", "Grace and Frankie", "The Cool Kids"],
        "d": 1
    },
    # 87
    {
        "q": "Which former 'Golden Girls' co-star made a guest appearance on Betty White's sitcom 'Hot in Cleveland' before passing away?",
        "correct": "None of them (all three co-stars had passed away before or around the premiere)",
        "wrong": ["Rue McClanahan", "Bea Arthur", "Estelle Getty"],
        "d": 3
    },
    # 88
    {
        "q": "What popular Disney animated film featured Estelle Getty as the voice of Mrs. Tweet, or did she voice characters in animation?",
        "correct": "She voiced characters in 'Stuart Little' and animated TV shows like 'Duckman' and 'Hercules'",
        "wrong": ["She voiced the Fairy Godmother in 'Cinderella II'", "She voiced Mama Odie in 'The Princess and the Frog'", "She voiced Mrs. Potts in 'Beauty and the Beast'"],
        "d": 3
    },
    # 89
    {
        "q": "What buddy-cop action comedy movie did Estelle Getty star in alongside Sylvester Stallone in 1992?",
        "correct": "Stop! Or My Mom Will Shoot",
        "wrong": ["Tango & Cash", "Kindergarten Cop", "Cop and a Half"],
        "d": 1
    },
    # 90
    {
        "q": "What iconic Golden Globe and Emmy award-winning role did Bea Arthur play in a Norman Lear 1970s sitcom before 'The Golden Girls'?",
        "correct": "Maude Findlay on 'Maude'",
        "wrong": ["Edith Bunker on 'All in the Family'", "Ann Romano on 'One Day at a Time'", "Florida Evans on 'Good Times'"],
        "d": 1
    },
    # 91
    {
        "q": "On which hit sitcom did Bea Arthur's character Maude first appear as Edith Bunker's outspoken, liberal cousin?",
        "correct": "All in the Family",
        "wrong": ["Sanford and Son", "The Jeffersons", "Mary Hartman, Mary Hartman"],
        "d": 1
    },
    # 92
    {
        "q": "What famous 1983 science fiction comedy film featured Rue McClanahan alongside John Candy and Dan Aykroyd?",
        "correct": "Doctor Detroit",
        "wrong": ["Ghostbusters", "Spaceballs", "The Blues Brothers"],
        "d": 3
    },
    # 93
    {
        "q": "Which Golden Girl was a licensed medical laboratory technician before she became a professional actress?",
        "correct": "Bea Arthur",
        "wrong": ["Betty White", "Rue McClanahan", "Estelle Getty"],
        "d": 2
    },
    # 94
    {
        "q": "In what branch of wartime clinical medicine was Bea Arthur certified during the 1940s?",
        "correct": "Medical technician specializing in blood and clinical lab work",
        "wrong": ["Surgical dental hygienist", "Radiological technician", "Physical therapy nurse"],
        "d": 3
    },
    # 95
    {
        "q": "What game show host did Betty White decline to marry multiple times before finally saying yes on the set of 'Password'?",
        "correct": "Allen Ludden",
        "wrong": ["Bert Convy", "Gene Rayburn", "Jack Barry"],
        "d": 2
    },
    # 96
    {
        "q": "What was the name of the pet poodle Betty White famously kept and brought onto production sets?",
        "correct": "Bandit",
        "wrong": ["Fifi", "Fernando", "Pepe"],
        "d": 3
    },
    # 97
    {
        "q": "Which Golden Girl received a posthumous star on the Hollywood Walk of Fame in November 2008?",
        "correct": "Estelle Getty",
        "wrong": ["Bea Arthur", "Rue McClanahan", "None of them"],
        "d": 3
    },
    # 98
    {
        "q": "Where is Betty White's star on the Hollywood Walk of Fame located relative to her husband Allen Ludden's star?",
        "correct": "Side-by-side right next to Allen Ludden's star on Hollywood Boulevard",
        "wrong": ["Three blocks apart across Vine Street", "In front of the Chinese Theatre while his is at Sunset", "Directly opposite each other across the street"],
        "d": 2
    },
    # 99
    {
        "q": "What prestigious television institution inducted all four Golden Girls into its Hall of Fame in 2009?",
        "correct": "The Television Academy Hall of Fame",
        "wrong": ["The National Broadcasters Hall of Fame", "The Hollywood Comedy Hall of Fame", "The Paley Center for Media Walk of Fame"],
        "d": 2
    },
    # 100
    {
        "q": "In what year was 'The Golden Girls' honored with the Pop Culture Award at the TV Land Awards, reunited on stage by Betty White and Rue McClanahan?",
        "correct": "2008",
        "wrong": ["2003", "2012", "2015"],
        "d": 2
    }
]

if __name__ == "__main__":
    build_golden_girls_batch(RAW_QUESTIONS, 5, "tools/staging/golden_girls_batch5.json")
