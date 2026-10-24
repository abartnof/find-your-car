from utils import build_golden_girls_batch

RAW_QUESTIONS = [
    # --- METATEXTUAL QUESTIONS (1-70: Questions 81-150 of Metatextual) ---
    # 1
    {
        "q": "What personal medical experience inspired creator Susan Harris to write Dorothy's battle with Chronic Fatigue Syndrome in 'Sick and Tired'?",
        "correct": "Susan Harris suffered from the illness and was dismissed and misdiagnosed by numerous doctors",
        "wrong": ["Susan Harris had a sister who contracted malaria in Africa", "Susan Harris suffered from mononucleosis while in college", "Susan Harris broke her back during a horseback riding accident"],
        "d": 1
    },
    # 2
    {
        "q": "In the acclaimed 1990 episode '72 Hours', what critical public health issue did 'The Golden Girls' tackle during the height of the epidemic?",
        "correct": "HIV and AIDS testing and social stigma",
        "wrong": ["Lyme disease tick infections", "Secondhand cigarette smoke exposure", "Breast cancer mammography screenings"],
        "d": 1
    },
    # 3
    {
        "q": "What groundbreaking social issue did 'The Golden Girls' address in the 1991 episode 'Sister of the Bride' over a decade before it became legal in the US?",
        "correct": "Same-sex marriage and legal equality",
        "wrong": ["Single-payer universal healthcare", "Decriminalization of recreational marijuana", "Banning smoking on domestic airplane flights"],
        "d": 1
    },
    # 4
    {
        "q": "In 'Isn't It Romantic?' (1986), what taboo topic for 1980s network television was handled with warmth and acceptance through Dorothy's friend Jean?",
        "correct": "Lesbian sexual orientation and coming out",
        "wrong": ["Interracial adoption of infants", "Divorce in the Catholic Church", "Living with physical paraplegia"],
        "d": 1
    },
    # 5
    {
        "q": "Which future 'Modern Family' co-creator wrote several acclaimed episodes of 'The Golden Girls' in its early seasons?",
        "correct": "Christopher Lloyd",
        "wrong": ["Steven Levitan", "Chuck Lorre", "Bill Lawrence"],
        "d": 3
    },
    # 6
    {
        "q": "What Emmy Award-winning costume designer created the signature pastel silks, stylish shoulder pads, and flowy loungewear for the cast?",
        "correct": "Judy Evans",
        "wrong": ["Bob Mackie", "Edith Head", "Patricia Field"],
        "d": 3
    },
    # 7
    {
        "q": "Approximately how many real cheesecakes were reportedly prepared and consumed by the cast and crew across the seven seasons of filming?",
        "correct": "Over 100 cheesecakes",
        "wrong": ["Fewer than 15 cheesecakes", "Exactly 25 cheesecakes", "Over 1,000 cheesecakes"],
        "d": 1
    },
    # 8
    {
        "q": "Which art director and production designer won a Primetime Emmy Award for creating the iconic sets of Blanche's Miami home?",
        "correct": "John C. Mula and Edward Stephenson",
        "wrong": ["Ken Adam and Cedric Gibbons", "Thomas E. Azzari and Roy Christopher", "Mary Ann Biddle and Rick Gentz"],
        "d": 3
    },
    # 9
    {
        "q": "What type of tropical furniture dominated the living room set, becoming a hallmark of 1980s South Florida chic?",
        "correct": "Rattan and wicker furniture with floral pastel cushions",
        "wrong": ["Dark mahogany Victorian parlor sets", "Mid-century modern chrome and leather", "Brutalist concrete and oak tables"],
        "d": 1
    },
    # 10
    {
        "q": "In the Season 5 episode 'Not Another Monday', what controversial and sensitive ethical dilemma did Sophia confront with her friend Martha?",
        "correct": "Assisted suicide and the right to die with dignity",
        "wrong": ["Undergoing experimental clinical drug trials", "Donating one's body to medical science", "Writing family members out of a will"],
        "d": 1
    },
    # 11
    {
        "q": "In the Season 4 episode 'Dorothy's New Friend', what form of discrimination does Dorothy discover her snooty intellectual friend Barbara practices?",
        "correct": "Anti-Semitism against Sophia and Jewish country club members",
        "wrong": ["Racial discrimination against African-American waitstaff", "Ageism against senior citizens", "Snobbery against non-college graduates"],
        "d": 1
    },
    # 12
    {
        "q": "What is the standard running time for a standard broadcast episode of 'The Golden Girls', excluding commercial breaks?",
        "correct": "Approximately 22 to 24 minutes",
        "wrong": ["Approximately 15 minutes", "Approximately 28 to 30 minutes", "Approximately 35 minutes"],
        "d": 1
    },
    # 13
    {
        "q": "Which prominent writing and executive producing duo wrote many of the show's sharpest rapid-fire comedic scripts in Seasons 1-4?",
        "correct": "Barry Fanaro and Mort Nathan",
        "wrong": ["David Angell and Peter Casey", "Garry Marshall and Jerry Belson", "Dick Clair and Jenna McMahon"],
        "d": 3
    },
    # 14
    {
        "q": "Which writer served as executive producer and showrunner for 'The Golden Girls' during its middle and later seasons?",
        "correct": "Marc Sotkin",
        "wrong": ["David Lee", "Glen Charles", "Les Charles"],
        "d": 3
    },
    # 15
    {
        "q": "What unique comedic visual motif was frequently used as a transition between scenes in 'The Golden Girls'?",
        "correct": "An exterior establishing shot of the Miami house set to bouncy woodwind music",
        "wrong": ["A spinning newspaper graphic", "A slide whistle with a wipe transition", "A fade to black with traffic noise"],
        "d": 1
    },
    # 16
    {
        "q": "In what year did TV Guide rank 'The Golden Girls' at Number 54 on its list of the 60 Best Series of All Time?",
        "correct": "2013",
        "wrong": ["2001", "2008", "2020"],
        "d": 3
    },
    # 17
    {
        "q": "How many Golden Globe Award nominations for Best Actress in a Television Comedy did the four stars accumulate collectively?",
        "correct": "19 nominations",
        "wrong": ["8 nominations", "12 nominations", "28 nominations"],
        "d": 3
    },
    # 18
    {
        "q": "Which of the four Golden Girls was the only one to win a Golden Globe Award for Best Actress in a Comedy for her role on the show?",
        "correct": "Estelle Getty (1986)",
        "wrong": ["Bea Arthur", "Betty White", "Rue McClanahan"],
        "d": 1
    },
    # 19
    {
        "q": "In what year did Estelle Getty tie with Cybill Shepherd for the Golden Globe for Best Actress in a Television Series - Musical or Comedy?",
        "correct": "1986",
        "wrong": ["1988", "1990", "1992"],
        "d": 3
    },
    # 20
    {
        "q": "What British television network bought the broadcast rights and aired 'The Golden Girls' to massive success in the United Kingdom starting in 1986?",
        "correct": "Channel 4",
        "wrong": ["BBC One", "ITV", "BBC Two"],
        "d": 1
    },
    # 21
    {
        "q": "In what German television network did 'The Golden Girls' become a legendary late-night cult phenomenon under the title 'Golden Girls'?",
        "correct": "RTL",
        "wrong": ["ZDF", "ARD", "Sat.1"],
        "d": 3
    },
    # 22
    {
        "q": "What major American television network attempted to create a remake or companion project titled 'Golden Girls' in numerous foreign markets?",
        "correct": "Touchstone / Disney Television International",
        "wrong": ["CBS Paramount International", "Sony Pictures International", "Universal Television Worldwide"],
        "d": 3
    },
    # 23
    {
        "q": "Which episode of 'The Golden Girls' served as the backdoor pilot for the spin-off 'Empty Nest' in Season 2?",
        "correct": "'Empty Nests' (featuring Rita Moreno and Paul Dooley)",
        "wrong": ["'The Neighbor Next Door'", "'Dr. Weston Moves In'", "'Miami Physicians'"],
        "d": 3
    },
    # 24
    {
        "q": "Why was the original backdoor pilot of 'Empty Nest' in Season 2 completely retooled before the series actually premiered in 1988?",
        "correct": "Test audiences disliked the original characters, so Susan Harris rewrote it around pediatrician Dr. Harry Weston and his daughters",
        "wrong": ["Rita Moreno had scheduling conflicts with a Broadway show", "NBC wanted the show set in New York instead of Miami", "The producers ran out of financing for the original concept"],
        "d": 3
    },
    # 25
    {
        "q": "Which famous actress and singer played the lead role of Renee Corliss in the original failed backdoor pilot of 'Empty Nest' on 'The Golden Girls'?",
        "correct": "Rita Moreno",
        "wrong": ["Chita Rivera", "Carol Channing", "Eartha Kitt"],
        "d": 1
    },
    # 26
    {
        "q": "What famous country music star and actress played nurse Laverne Todd on the spin-off 'Empty Nest'?",
        "correct": "Park Overall",
        "wrong": ["Reba McEntire", "Dolly Parton", "Barbara Mandrell"],
        "d": 3
    },
    # 27
    {
        "q": "What famous actress from 'Little House on the Prairie' played police officer Barbara Weston on 'Empty Nest'?",
        "correct": "Kristy McNichol",
        "wrong": ["Melissa Gilbert", "Melissa Sue Anderson", "Alison Arngrim"],
        "d": 1
    },
    # 28
    {
        "q": "What actress played high-strung daughter Carol Weston on 'Empty Nest' and made multiple guest appearances on 'The Golden Girls'?",
        "correct": "Dinah Manoff",
        "wrong": ["Valerie Bertinelli", "Mackenzie Phillips", "Nancy McKeon"],
        "d": 1
    },
    # 29
    {
        "q": "Which Golden Girl character made the most guest crossover appearances on 'Empty Nest' and 'Nurses'?",
        "correct": "Sophia Petrillo",
        "wrong": ["Dorothy Zbornak", "Blanche Devereaux", "Rose Nylund"],
        "d": 1
    },
    # 30
    {
        "q": "In fact, Sophia Petrillo became a permanent regular cast member on which spin-off series in 1993 after 'The Golden Palace' was cancelled?",
        "correct": "Empty Nest (for its final two seasons)",
        "wrong": ["Nurses", "Blossom", "Wings"],
        "d": 1
    },
    # 31
    {
        "q": "How many total television series did Estelle Getty portray Sophia Petrillo in across her career?",
        "correct": "Five series (The Golden Girls, The Golden Palace, Empty Nest, Nurses, and Blossom)",
        "wrong": ["Two series", "Three series", "Seven series"],
        "d": 1
    },
    # 32
    {
        "q": "In which teen sitcom did Estelle Getty appear as Sophia Petrillo in a 1991 dream sequence?",
        "correct": "Blossom",
        "wrong": ["Saved by the Bell", "Boy Meets World", "Full House"],
        "d": 2
    },
    # 33
    {
        "q": "What was the total number of Primetime Emmy Awards won by 'The Golden Girls' across all categories throughout its run?",
        "correct": "11 Emmy Awards",
        "wrong": ["5 Emmy Awards", "22 Emmy Awards", "35 Emmy Awards"],
        "d": 2
    },
    # 34
    {
        "q": "In what year did Rue McClanahan receive her Primetime Emmy for Outstanding Lead Actress?",
        "correct": "1987",
        "wrong": ["1985", "1989", "1991"],
        "d": 2
    },
    # 35
    {
        "q": "In what year did Bea Arthur receive her Primetime Emmy for Outstanding Lead Actress?",
        "correct": "1988",
        "wrong": ["1986", "1987", "1990"],
        "d": 2
    },
    # 36
    {
        "q": "In what year did Betty White receive her Primetime Emmy for Outstanding Lead Actress?",
        "correct": "1986",
        "wrong": ["1987", "1988", "1992"],
        "d": 2
    },
    # 37
    {
        "q": "What record for Emmy nominations did 'The Golden Girls' achieve in the Lead Actress in a Comedy category in 1986 and 1987?",
        "correct": "Three of the five nominees in the category were stars from 'The Golden Girls'",
        "wrong": ["All five nominees were from 'The Golden Girls'", "All four stars tied for the award", "No other show was nominated for comedy writing"],
        "d": 2
    },
    # 38
    {
        "q": "In which category was Estelle Getty nominated for a Primetime Emmy for seven consecutive years?",
        "correct": "Outstanding Supporting Actress in a Comedy Series",
        "wrong": ["Outstanding Lead Actress in a Comedy Series", "Outstanding Guest Actress in a Comedy Series", "Outstanding Variety Performer"],
        "d": 2
    },
    # 39
    {
        "q": "What award did 'The Golden Girls' win from the Television Critics Association (TCA) in 1986?",
        "correct": "Outstanding Achievement in Comedy",
        "wrong": ["Program of the Year", "Heritage Award", "Best New Drama"],
        "d": 3
    },
    # 40
    {
        "q": "Which producer/director directed the Season 1 episodes before Terry Hughes took over in Season 2?",
        "correct": "Jay Sandrich (and Jim Drake)",
        "wrong": ["James Burrows", "Gene Saks", "Peter Bonerz"],
        "d": 3
    },
    # 41
    {
        "q": "What was the name of the soundstage complex where 'The Golden Girls' was filmed in front of live studio audiences in Los Angeles?",
        "correct": "Sunset Gower Studios (formerly Columbia Pictures Studios)",
        "wrong": ["Universal City Studios", "Warner Bros. Studios Burbank", "Paramount Studios Hollywood"],
        "d": 2
    },
    # 42
    {
        "q": "What famous daytime talk show did the four actresses appear on together in 1988 to celebrate their show's runaway success?",
        "correct": "The Oprah Winfrey Show",
        "wrong": ["The Phil Donahue Show", "The Joan Rivers Show", "Geraldo"],
        "d": 2
    },
    # 43
    {
        "q": "What was unique about the opening credits of 'The Golden Girls' throughout all seven seasons?",
        "correct": "They featured clips of the women laughing, hugging, and interacting rather than formal posed portraits",
        "wrong": ["They featured cartoon caricatures of the characters", "They showed the Miami skyline with no cast members", "They were filmed on location on Miami Beach every season"],
        "d": 2
    },
    # 44
    {
        "q": "What color was the signature text font used for the show's title logo during the opening theme?",
        "correct": "Yellow / gold script with shadow",
        "wrong": ["Hot pink neon block", "Navy blue serif italic", "Bright turquoise cursive"],
        "d": 1
    },
    # 45
    {
        "q": "Which character speaks the very first line of dialogue in the 1985 pilot episode of 'The Golden Girls'?",
        "correct": "Rose Nylund",
        "wrong": ["Dorothy Zbornak", "Blanche Devereaux", "Sophia Petrillo"],
        "d": 3
    },
    # 46
    {
        "q": "Which character speaks the very last line of dialogue in the 1992 series finale?",
        "correct": "Sophia Petrillo",
        "wrong": ["Dorothy Zbornak", "Blanche Devereaux", "Rose Nylund"],
        "d": 3
    },
    # 47
    {
        "q": "What is the final action seen in the series finale before the end credits roll?",
        "correct": "Rose, Blanche, and Sophia sobbing in an embrace in the living room after Dorothy exits",
        "wrong": ["The four women eating cheesecake at the kitchen table", "Blanche hanging a new roommate advertisement at the supermarket", "Sophia packing her wicker purse and heading for the bus"],
        "d": 2
    },
    # 48
    {
        "q": "What major American holiday always coincided with special holiday-themed episodes of 'The Golden Girls'?",
        "correct": "Mother's Day and Christmas",
        "wrong": ["Fourth of July and Labor Day", "Halloween and Thanksgiving", "Memorial Day and New Year's Eve"],
        "d": 2
    },
    # 49
    {
        "q": "In the Season 2 Christmas episode 'Twas the Nightmare Before Christmas', where do the women get stranded on Christmas Eve?",
        "correct": "At a counseling center held hostage by a man dressed as Santa Claus",
        "wrong": ["At the Miami airport during a snow cancellation up north", "In a highway diner with a broken radiator", "In an elevator at the department store"],
        "d": 2
    },
    # 50
    {
        "q": "Who played the desperate man dressed as Santa in 'Twas the Nightmare Before Christmas'?",
        "correct": "David Spade",
        "wrong": ["Jim Carrey", "Jon Lovitz", "Dana Carvey"],
        "d": 3
    },
    # 51
    {
        "q": "What weapon does the desperate Santa pull out at the grief center in the Christmas episode?",
        "correct": "A gun, which turns out to be a toy gun or loaded with blanks",
        "wrong": ["A switchblade knife", "A live grenade", "A stick of dynamite"],
        "d": 3
    },
    # 52
    {
        "q": "Which major television honor was awarded to 'The Golden Girls' in 1986 by the Peabody Awards committee?",
        "correct": "The George Foster Peabody Award for broadcasting excellence",
        "wrong": ["The Humanitas Prize", "The Television Academy Hall of Fame Induction", "The NAACP Image Award"],
        "d": 2
    },
    # 53
    {
        "q": "Why did the Peabody Board specifically commend 'The Golden Girls' in its 1986 citation?",
        "correct": "For dealing with mature women and senior citizen issues with wit, intelligence, and dignity",
        "wrong": ["For achieving record-breaking advertising revenue on Saturday nights", "For pioneering the use of digital multi-camera editing", "For filming on location throughout Florida communities"],
        "d": 2
    },
    # 54
    {
        "q": "What was the primary syndication distributor that sold 'The Golden Girls' into broadcast reruns?",
        "correct": "Buena Vista Television",
        "wrong": ["King World Productions", "Viacom Enterprises", "Tribune Entertainment"],
        "d": 3
    },
    # 55
    {
        "q": "How many times did 'The Golden Girls' appear on the cover of TV Guide during its original network run?",
        "correct": "Seven times",
        "wrong": ["Once", "Three times", "Fifteen times"],
        "d": 3
    },
    # 56
    {
        "q": "In what year did Betty White host 'Saturday Night Live' following a massive viral Facebook campaign, referencing 'The Golden Girls'?",
        "correct": "2010",
        "wrong": ["2005", "2015", "2020"],
        "d": 2
    },
    # 57
    {
        "q": "What Primetime Emmy did Betty White win for hosting 'Saturday Night Live' in 2010?",
        "correct": "Outstanding Guest Actress in a Comedy Series",
        "wrong": ["Outstanding Variety Special Host", "Outstanding Supporting Actress in a Comedy", "Lifetime Achievement Emmy"],
        "d": 2
    },
    # 58
    {
        "q": "Which writer/producer created the character of Sophia Petrillo as an Italian matriarch specifically based on her own Italian-American family roots?",
        "correct": "Susan Harris",
        "wrong": ["Paul Junger Witt", "Tony Thomas", "Marc Sotkin"],
        "d": 2
    },
    # 59
    {
        "q": "What sitcom did Witt/Thomas/Harris produce immediately following 'The Golden Girls' that also starred an ensemble of women?",
        "correct": "Nurses",
        "wrong": ["Designing Women", "Murphy Brown", "Kate & Allie"],
        "d": 2
    },
    # 60
    {
        "q": "What CBS comedy was often compared to 'The Golden Girls' as its Southern counterpart airing during the same late-1980s era?",
        "correct": "Designing Women",
        "wrong": ["The Facts of Life", "Alice", "Mama's Family"],
        "d": 2
    },
    # 61
    {
        "q": "In what year did Bea Arthur and Rue McClanahan reunite on television to guest-star on the sitcom 'Empty Nest'?",
        "correct": "1989 and 1991",
        "wrong": ["1985", "1995", "1998"],
        "d": 3
    },
    # 62
    {
        "q": "What was the title of the 1990 retrospective special hosted by the cast highlighting the best moments of the first five seasons?",
        "correct": "The Golden Girls: Their Greatest Moments",
        "wrong": ["Thank You for Being a Friend: 5 Years", "Golden Memories", "Miami Gold Retrospective"],
        "d": 3
    },
    # 63
    {
        "q": "Which famous theater critic and lyricist was the father of executive producer Tony Thomas?",
        "correct": "Danny Thomas (the legendary comedian and television pioneer)",
        "wrong": ["Lowell Thomas", "Dylan Thomas", "Marlo Thomas"],
        "d": 2
    },
    # 64
    {
        "q": "Who was executive producer Paul Junger Witt married to throughout the show's run?",
        "correct": "Creator Susan Harris",
        "wrong": ["Actress Rue McClanahan", "Director Jay Sandrich", "Producer Marcy Carsey"],
        "d": 2
    },
    # 65
    {
        "q": "What production company logo featuring a blue script and music fanfare appeared at the end of each Golden Girls episode?",
        "correct": "Witt/Thomas/Harris Productions with Touchstone Television",
        "wrong": ["MTM Enterprises with kitten mewing", "Stephen J. Cannell throwing paper", "Tandem Productions with torch"],
        "d": 2
    },
    # 66
    {
        "q": "In the episode 'The Golden Globe' (not the awards show), what happens to the girls' prized possessions?",
        "correct": "They reminisce through flashbacks of classic scenes",
        "wrong": ["Their house is put up for sale by mistake", "They win a local trophy for civic service", "Sophia sells their antiques at a swap meet"],
        "d": 3
    },
    # 67
    {
        "q": "How many total clip-show flashback episodes did 'The Golden Girls' produce over its seven-season run?",
        "correct": "Eight clip-show episodes",
        "wrong": ["Two clip-show episodes", "Twelve clip-show episodes", "None"],
        "d": 3
    },
    # 68
    {
        "q": "In what year did 'The Golden Girls' celebrate its 30th broadcast anniversary with widespread retrospective coverage?",
        "correct": "2015",
        "wrong": ["2010", "2020", "2005"],
        "d": 2
    },
    # 69
    {
        "q": "What popular streaming platform made 'The Golden Palace' available to stream for the first time in 2022?",
        "correct": "Hulu",
        "wrong": ["Netflix", "Disney+", "Paramount+"],
        "d": 2
    },
    # 70
    {
        "q": "What is the title of the popular off-Broadway parody puppet show celebrating 'The Golden Girls' that debuted in 2016?",
        "correct": "That Golden Girls Show! A Puppet Parody",
        "wrong": ["Puppet Pals in Miami", "Thank You for the Puppets", "Golden Marionettes Live"],
        "d": 2
    },

    # --- EXTRA-TEXTUAL QUESTIONS (71-100: Questions 1-30 of Extratextual) ---
    # 71
    {
        "q": "What famous casting swap occurred during the development and audition process of 'The Golden Girls'?",
        "correct": "Betty White was initially slated for Blanche and Rue McClanahan for Rose, but they switched roles",
        "wrong": ["Bea Arthur was originally cast as Sophia and Estelle Getty as Dorothy", "Rue McClanahan was originally cast as Dorothy and Bea Arthur as Blanche", "Betty White was originally cast as Sophia and Estelle Getty as Rose"],
        "d": 1
    },
    # 72
    {
        "q": "Which director suggested swapping Betty White and Rue McClanahan into the roles of Rose and Blanche to avoid typecasting?",
        "correct": "Jay Sandrich",
        "wrong": ["James Burrows", "Terry Hughes", "Hal Cooper"],
        "d": 1
    },
    # 73
    {
        "q": "Why was director Jay Sandrich concerned about casting Betty White as Blanche and Rue McClanahan as Rose?",
        "correct": "Betty had already played a vixen on 'Mary Tyler Moore' and Rue had played a naive scatterbrain on 'Maude'",
        "wrong": ["Both actresses had accents that didn't fit the original script", "Betty White refused to play a character who dated younger men", "Rue McClanahan wanted to play a tough Sicilian mother instead"],
        "d": 1
    },
    # 74
    {
        "q": "What surprising real-life age relationship existed between Estelle Getty (Sophia) and Bea Arthur (Dorothy)?",
        "correct": "Estelle Getty was actually one year and two months younger than Bea Arthur",
        "wrong": ["Estelle Getty was twenty years older than Bea Arthur", "Estelle Getty and Bea Arthur were identical twin sisters in real life", "Estelle Getty was ten years older than Bea Arthur"],
        "d": 1
    },
    # 75
    {
        "q": "What was Estelle Getty's exact birth year compared to Bea Arthur's birth year of 1922?",
        "correct": "1923",
        "wrong": ["1910", "1915", "1932"],
        "d": 2
    },
    # 76
    {
        "q": "How long did Estelle Getty spend in the makeup chair each filming day to transform into the 80-something Sophia?",
        "correct": "Roughly 45 to 60 minutes applying aging latex, wrinkles, and a gray wig",
        "wrong": ["Over four hours of full prosthetic body casting", "Ten minutes with just a dusting of baby powder", "Two full hours with silicone facial appliances"],
        "d": 2
    },
    # 77
    {
        "q": "What psychological challenge did Estelle Getty famously suffer from throughout her entire time on 'The Golden Girls'?",
        "correct": "Severe stage fright and anxiety about forgetting her lines in front of the live audience",
        "wrong": ["Agoraphobia that prevented her from leaving her dressing room", "Claustrophobia on the small kitchen soundstage", "Severe depression due to her character's dowdy wardrobe"],
        "d": 2
    },
    # 78
    {
        "q": "What footwear quirk was Bea Arthur known for on the set of 'The Golden Girls'?",
        "correct": "She despised wearing shoes and walked around barefoot whenever cameras didn't show her feet",
        "wrong": ["She insisted on wearing custom 6-inch stiletto heels in every scene", "She wore roller skates behind the kitchen counter", "She refused to wear anything other than orthopedic bowling shoes"],
        "d": 1
    },
    # 79
    {
        "q": "What common culinary item featured on the show did Bea Arthur genuinely dislike eating in real life?",
        "correct": "Cheesecake",
        "wrong": ["Marinara sauce", "Italian cannoli", "Coffee"],
        "d": 1
    },
    # 80
    {
        "q": "What common habit on set did Bea Arthur famously despise, to the point of banning people from doing it near her?",
        "correct": "Chewing gum",
        "wrong": ["Whistling show tunes", "Drinking iced tea from a straw", "Smoking cigars outside Stage 9"],
        "d": 2
    },
    # 81
    {
        "q": "How tall was Bea Arthur, giving her an imposing and commanding physical presence on stage?",
        "correct": "5 feet 10 inches (178 cm)",
        "wrong": ["5 feet 4 inches (163 cm)", "6 feet 2 inches (188 cm)", "5 feet 6 inches (168 cm)"],
        "d": 2
    },
    # 82
    {
        "q": "What branch of the United States military did Bea Arthur serve in during World War II before pursuing acting?",
        "correct": "The United States Marine Corps Women's Reserve",
        "wrong": ["The Women's Army Corps (WAC)", "The Navy WAVES", "The Coast Guard SPARS"],
        "d": 2
    },
    # 83
    {
        "q": "What military duties did Bea Arthur perform during her service in the Marine Corps Women's Reserve?",
        "correct": "She worked as a truck driver and typist",
        "wrong": ["She was a flight nurse in the Pacific", "She decoded Japanese naval communications", "She trained military guard dogs"],
        "d": 3
    },
    # 84
    {
        "q": "What was Bea Arthur's legal birth name before adopting her stage name?",
        "correct": "Bernice Frankel",
        "wrong": ["Beatrice Arkin", "Bernadette Arthur", "Barbara Feldman"],
        "d": 2
    },
    # 85
    {
        "q": "What was Rue McClanahan's full birth name?",
        "correct": "Eddi-Rue McClanahan",
        "wrong": ["Ruth Ann McClanahan", "Ruby Mae McClanahan", "Rochelle McClanahan"],
        "d": 3
    },
    # 86
    {
        "q": "In what US state was Rue McClanahan born and raised, giving her an authentic Southern heritage?",
        "correct": "Oklahoma",
        "wrong": ["Georgia", "Alabama", "Mississippi"],
        "d": 2
    },
    # 87
    {
        "q": "What special clause did Rue McClanahan negotiate into her contract for 'The Golden Girls' regarding her character's wardrobe?",
        "correct": "She was legally entitled to keep all of Blanche Devereaux's custom designer clothing",
        "wrong": ["She was allowed to choose her own hair color every season", "She received 10% of all merchandise sales", "She had veto power over all male guest star casting"],
        "d": 2
    },
    # 88
    {
        "q": "Approximately how many custom designer outfits from Blanche's wardrobe did Rue McClanahan keep in her private collection?",
        "correct": "Hundreds of custom dresses, robes, and suits (over 500 pieces)",
        "wrong": ["Fewer than 10 pieces", "Around 25 pieces", "Only her wedding dresses"],
        "d": 3
    },
    # 89
    {
        "q": "What was Betty White's lifelong philanthropic passion outside of show business?",
        "correct": "Animal health, welfare, and wildlife conservation",
        "wrong": ["Classical opera restoration", "Youth tennis academy coaching", "Historic lighthouse preservation"],
        "d": 1
    },
    # 90
    {
        "q": "What prestigious animal organization did Betty White serve on the board of trustees for over four decades?",
        "correct": "The Morris Animal Foundation and the Greater Los Angeles Zoo Association",
        "wrong": ["The World Wildlife Fund International", "The American Humane Association", "PETA"],
        "d": 2
    },
    # 91
    {
        "q": "Who was Betty White's beloved third husband and legendary game show host whom she called the love of her life?",
        "correct": "Allen Ludden",
        "wrong": ["Bill Cullen", "Gene Rayburn", "Peter Marshall"],
        "d": 1
    },
    # 92
    {
        "q": "What famous game show did Allen Ludden host, where Betty White appeared as a frequent celebrity panelist?",
        "correct": "Password",
        "wrong": ["Match Game", "Jeopardy!", "The Hollywood Squares"],
        "d": 1
    },
    # 93
    {
        "q": "In what year did Allen Ludden pass away from stomach cancer, just four years before Betty White was cast in 'The Golden Girls'?",
        "correct": "1981",
        "wrong": ["1975", "1985", "1990"],
        "d": 3
    },
    # 94
    {
        "q": "What Tony Award did Bea Arthur win in 1966 for her role as Vera Charles on Broadway?",
        "correct": "Best Featured Actress in a Musical for 'Mame'",
        "wrong": ["Best Leading Actress in a Musical for 'Fiddler on the Roof'", "Best Actress in a Play for 'The Threepenny Opera'", "Best Featured Actress in a Musical for 'Gypsy'"],
        "d": 2
    },
    # 95
    {
        "q": "What iconic role did Bea Arthur originate on Broadway in the 1964 original production of 'Fiddler on the Roof'?",
        "correct": "Yente the Matchmaker",
        "wrong": ["Golde", "Tzeitel", "Fruma-Sarah"],
        "d": 2
    },
    # 96
    {
        "q": "What Broadway role brought Estelle Getty national acclaim and led directly to her casting on 'The Golden Girls'?",
        "correct": "Mrs. Beckoff in Harvey Fierstein's 'Torch Song Trilogy'",
        "wrong": ["Mama Rose in 'Gypsy'", "Kate Jerome in 'Brighton Beach Memoirs'", "Golde in 'Fiddler on the Roof'"],
        "d": 2
    },
    # 97
    {
        "q": "What was Estelle Getty's birth name?",
        "correct": "Estelle Scher",
        "wrong": ["Estelle Gettleman", "Estelle Shapiro", "Estelle Schwartz"],
        "d": 3
    },
    # 98
    {
        "q": "Who was Estelle Getty married to from 1947 until his death in 2004?",
        "correct": "Arthur Gettleman",
        "wrong": ["Max Weinstock", "Irving Scher", "Sal Petrillo"],
        "d": 3
    },
    # 99
    {
        "q": "Which of the four Golden Girls was the oldest in real life, born in January 1922?",
        "correct": "Betty White",
        "wrong": ["Bea Arthur (born May 1922)", "Estelle Getty (born July 1923)", "Rue McClanahan (born February 1934)"],
        "d": 1
    },
    # 100
    {
        "q": "Which of the four Golden Girls was the youngest in real life, born in 1934?",
        "correct": "Rue McClanahan",
        "wrong": ["Estelle Getty", "Bea Arthur", "Betty White"],
        "d": 1
    }
]

if __name__ == "__main__":
    build_golden_girls_batch(RAW_QUESTIONS, 4, "tools/staging/golden_girls_batch4.json")
