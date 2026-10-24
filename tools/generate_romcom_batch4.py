#!/usr/bin/env python3
"""
Generate Batch 4 for Romantic Comedies:
100 Questions:
 - 50 Metatextual (Soundtracks, Chart-Topping Hits, Score Composers, Music Moments)
 - 50 Extratextual (Casting Near-Misses, Alternate Castings, Rejections, Audition Lore)
Difficulty: 30 d1, 40 d2, 30 d3.
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))
from rom_com_builder import make_batch

questions_batch4 = [
    # 1 - d1
    (
        "Which Scottish band spent 15 consecutive weeks at #1 on the UK Singles Chart in 1994 with 'Love Is All Around' from 'Four Weddings and a Funeral'?",
        "Wet Wet Wet",
        ["The Proclaimers", "Simple Minds", "Deacon Blue"],
        1
    ),
    # 2 - d1
    (
        "Which pop-rock group had a massive international smash hit with 'Kiss Me' after it was featured in the 1999 teen rom-com 'She's All That'?",
        "Sixpence None the Richer",
        ["The Cardigans", "The Cranberries", "Letters to Cleo"],
        1
    ),
    # 3 - d1
    (
        "Which Swedish pop duo scored a Billboard #1 hit with 'It Must Have Been Love', prominently featured on the 'Pretty Woman' soundtrack?",
        "Roxette",
        ["Ace of Base", "ABBA", "The Cardigans"],
        1
    ),
    # 4 - d1
    (
        "Which Peter Gabriel ballad became an immortal romantic film staple when John Cusack held a boombox over his head in 'Say Anything...'?",
        "In Your Eyes",
        ["Sledgehammer", "Don't Give Up", "Biko"],
        1
    ),
    # 5 - d1
    (
        "In '10 Things I Hate About You', which classic Frankie Valli hit does Heath Ledger sing on the stadium bleachers accompanied by the high school marching band?",
        "Can't Take My Eyes Off You",
        ["December, 1963 (Oh, What a Night)", "Grease", "Sherry"],
        1
    ),
    # 6 - d1
    (
        "Which song by The Pointer Sisters provides the energetic soundtrack to Hugh Grant dancing solo through 10 Downing Street in 'Love Actually'?",
        "Jump (For My Love)",
        ["I'm So Excited", "Neutron Dance", "Slow Hand"],
        1
    ),
    # 7 - d1
    (
        "Which Natasha Bedingfield pop anthem enjoyed a massive viral chart resurgence in 2024 after being featured as Ben's serenity song in 'Anyone But You'?",
        "Unwritten",
        ["Pocketful of Sunshine", "These Words", "Single"],
        1
    ),
    # 8 - d1
    (
        "Which classic Irish rock band's song 'Dreams' plays over the opening credits of Nora Ephron's 1998 romantic comedy 'You've Got Mail'?",
        "The Cranberries",
        ["The Corrs", "U2", "The Cranes"],
        1
    ),
    # 9 - d1
    (
        "Which iconic pop star sang 'Let the River Run' for the 1988 film 'Working Girl', winning an Oscar, a Golden Globe, and a Grammy?",
        "Carly Simon",
        ["Bette Midler", "Barbra Streisand", "Cyndi Lauper"],
        1
    ),
    # 10 - d1
    (
        "Which classic Audrey Hepburn song from 'Breakfast at Tiffany's' won the Academy Award for Best Original Song in 1962?",
        "Moon River",
        ["Days of Wine and Roses", "Charade", "Two for the Road"],
        1
    ),
    # 11 - d1
    (
        "Which 1965 Sonny & Cher anthem plays on Phil Connors's clock radio every morning at 6:00 AM sharp in 'Groundhog Day'?",
        "I Got You Babe",
        ["The Beat Goes On", "Baby Don't Go", "Bang Bang"],
        1
    ),
    # 12 - d1
    (
        "Which 1980s teen icon famously turned down the lead role of Vivian Ward in 'Pretty Woman', paving the way for Julia Roberts's breakthrough?",
        "Molly Ringwald",
        ["Winona Ryder", "Ally Sheedy", "Jennifer Grey"],
        1
    ),
    # 13 - d1
    (
        "Which major Hollywood star was offered the role of Harry Burns in 'When Harry Met Sally...' but passed because he found the material too lightweight?",
        "Tom Hanks",
        ["Harrison Ford", "Richard Gere", "Michael Douglas"],
        1
    ),
    # 14 - d1
    (
        "Which actress was cast as Cher Horowitz in 'Clueless' without an audition after writer-director Amy Heckerling saw her in Aerosmith music videos?",
        "Alicia Silverstone",
        ["Reese Witherspoon", "Keri Russell", "Sarah Michelle Gellar"],
        1
    ),
    # 15 - d1
    (
        "Which actress famously turned down the role of Elle Woods in 'Legally Blonde' because she feared being typecast as a dumb blonde after 'Married... with Children'?",
        "Christina Applegate",
        ["Tara Reid", "Alicia Silverstone", "Denise Richards"],
        1
    ),
    # 16 - d1
    (
        "Who was Cameron Crowe's first and only choice to play romantic kickboxer Lloyd Dobler in 'Say Anything...'?",
        "John Cusack",
        ["Rob Lowe", "Christian Slater", "Matthew Broderick"],
        1
    ),
    # 17 - d1
    (
        "Which English actor almost quit acting completely out of frustration before landing the career-making role of Charles in 'Four Weddings and a Funeral'?",
        "Hugh Grant",
        ["Colin Firth", "Pierce Brosnan", "Rupert Everett"],
        1
    ),
    # 18 - d1
    (
        "Which Hollywood A-lister was originally slated to star in 'The Proposal' before walking away over salary disputes, leading to Sandra Bullock's casting?",
        "Julia Roberts",
        ["Nicole Kidman", "Meg Ryan", "Cameron Diaz"],
        1
    ),
    # 19 - d1
    (
        "Which American actress faced heavy British media skepticism when cast as the beloved London heroine Bridget Jones?",
        "Renée Zellweger",
        ["Cameron Diaz", "Gwyneth Paltrow", "Sandra Bullock"],
        1
    ),
    # 20 - d1
    (
        "Cameron Crowe originally wrote the title role of sports agent Jerry Maguire specifically with which actor in mind?",
        "Tom Hanks",
        ["Tom Cruise", "Kevin Costner", "Robin Williams"],
        1
    ),
    # 21 - d1
    (
        "Which actor was Harold Ramis's first thought to play cynical weatherman Phil Connors in 'Groundhog Day' before realizing the audience would expect him to be too nice?",
        "Tom Hanks",
        ["Steve Martin", "Robin Williams", "John Candy"],
        1
    ),
    # 22 - d1
    (
        "Which charismatic actor made a legendary, self-parodying cameo as himself dating Sasha Tran in the 2019 rom-com 'Always Be My Maybe'?",
        "Keanu Reeves",
        ["Daniel Dae Kim", "Randall Park", "Steven Yeun"],
        1
    ),
    # 23 - d1
    (
        "Which pop song by Hall & Oates provides the backdrop to Tom's joyful post-hookup street dance parade in '(500) Days of Summer'?",
        "You Make My Dreams",
        ["Maneater", "Kiss on My List", "Private Eyes"],
        1
    ),
    # 24 - d1
    (
        "Which singer had the first #1 hit by an unsigned artist on the Billboard Hot 100 with 'Stay (I Missed You)' from the 1994 rom-com 'Reality Bites'?",
        "Lisa Loeb",
        ["Alanis Morissette", "Fiona Apple", "Jewel"],
        1
    ),
    # 25 - d1
    (
        "In 'Crazy Rich Asians', which indie singer performs an acoustic cover of Elvis Presley's 'Can't Help Falling in Love' during Araminta's water wedding procession?",
        "Kina Grannis",
        ["Priscilla Ahn", "Yuna", "Jhené Aiko"],
        1
    ),
    # 26 - d1
    (
        "In 'The Wedding Singer', which musical icon makes a triumphant airplane first-class cameo to help Robbie win back Julia Sullivan?",
        "Billy Idol",
        ["Boy George", "David Bowie", "Cyndi Lauper"],
        1
    ),
    # 27 - d1
    (
        "Which song from 'Dirty Dancing' sung by Bill Medley and Jennifer Warnes won the Academy Award for Best Original Song in 1988?",
        "(I've Had) The Time of My Life",
        ["Hungry Eyes", "She's Like the Wind", "Stay"],
        1
    ),
    # 28 - d1
    (
        "Which Scottish duo's anthem 'I'm Gonna Be (500 Miles)' hit #3 on the Billboard Hot 100 five years after its release thanks to the 1993 rom-com 'Benny & Joon'?",
        "The Proclaimers",
        ["The Waterboys", "Del Amitri", "Travis"],
        1
    ),
    # 29 - d1
    (
        "In '13 Going on 30', which Michael Jackson song does Jenna Rink use to ignite an otherwise lifeless corporate party dance floor?",
        "Thriller",
        ["Billie Jean", "Beat It", "Bad"],
        1
    ),
    # 30 - d1
    (
        "Which actress was cast as Viola de Lesseps in 'Shakespeare in Love' and won an Oscar after Kate Winslet turned the part down?",
        "Gwyneth Paltrow",
        ["Cate Blanchett", "Helena Bonham Carter", "Rachel Weisz"],
        1
    ),

    # 31 - d2
    (
        "Which British singer recorded 'When You Say Nothing at All' for the 1999 'Notting Hill' soundtrack, topping the UK Singles Chart?",
        "Ronan Keating",
        ["Robbie Williams", "Gary Barlow", "David Gray"],
        2
    ),
    # 32 - d2
    (
        "Which Bill Withers soul classic plays during the famous seasonal tracking shot where William Thacker walks through Portobello Road market in 'Notting Hill'?",
        "Ain't No Sunshine",
        ["Lean on Me", "Lovely Day", "Just the Two of Us"],
        2
    ),
    # 33 - d2
    (
        "Which British singer recorded the opening and closing theme song 'She' for the 'Notting Hill' soundtrack?",
        "Elvis Costello",
        ["Van Morrison", "Bryan Ferry", "Paul Weller"],
        2
    ),
    # 34 - d2
    (
        "In 'Bridget Jones's Diary', which power ballad does Bridget dramatically lip-sync in her pajamas with red wine during the opening credits?",
        "All by Myself",
        ["Without You", "I Will Always Love You", "Total Eclipse of the Heart"],
        2
    ),
    # 35 - d2
    (
        "Which British R&B singer wrote and recorded the hit single 'Out of Reach' specifically for 'Bridget Jones's Diary'?",
        "Gabrielle",
        ["Des'ree", "Beverley Knight", "Corinne Bailey Rae"],
        2
    ),
    # 36 - d2
    (
        "In 'Love Actually', which Beatles song is performed by surprise horn players planted in the church pews at Peter and Juliet's wedding?",
        "All You Need Is Love",
        ["In My Life", "Here Comes the Sun", "Something"],
        2
    ),
    # 37 - d2
    (
        "In 'White Chicks', which Terry Crews car sing-along turned which 2002 Vanessa Carlton piano-pop hit into an iconic comedic meme?",
        "A Thousand Miles",
        ["Ordinary Day", "White Houses", "Pretty Baby"],
        2
    ),
    # 38 - d2
    (
        "In 'Easy A', which Natasha Bedingfield song drives Olive Penderghast crazy after opening a musical greeting card from her grandmother?",
        "Pocketful of Sunshine",
        ["Unwritten", "These Words", "Soulmate"],
        2
    ),
    # 39 - d2
    (
        "In '27 Dresses', which Elton John classic do Jane Nichols and Kevin Doyle belt out atop a dive bar counter while soaking wet?",
        "Bennie and the Jets",
        ["Tiny Dancer", "Rocket Man", "Crocodile Rock"],
        2
    ),
    # 40 - d2
    (
        "In 'Crazy Rich Asians', which Mandarin-language cover of Coldplay's 'Yellow' plays during the climactic flight scene between Rachel and Nick?",
        "Katherine Ho's Chinese cover",
        ["Faye Wong's cover", "Teresa Teng's cover", "Karen Mok's cover"],
        2
    ),
    # 41 - d2
    (
        "Who arranged and performed the vintage big-band standards on the Grammy-winning 'When Harry Met Sally...' soundtrack?",
        "Harry Connick Jr.",
        ["Michael Bublé", "Tony Bennett", "Diana Krall"],
        2
    ),
    # 42 - d2
    (
        "In '(500) Days of Summer', which British indie rock band's song 'There Is a Light That Never Goes Out' sparks Tom and Summer's elevator conversation?",
        "The Smiths",
        ["The Cure", "Joy Division", "Echo & the Bunnymen"],
        2
    ),
    # 43 - d2
    (
        "Which Australian indie rock band had their breakout international hit with 'Sweet Disposition' after it was featured in '(500) Days of Summer'?",
        "The Temper Trap",
        ["Empire of the Sun", "Cut Copy", "Miami Horror"],
        2
    ),
    # 44 - d2
    (
        "In 'My Best Friend's Wedding', which Diana King reggae-pop cover opens the movie's theatrical credits with dancing bridesmaids?",
        "I Say a Little Prayer",
        ["Shy Guy", "Ain't Nobody", "I'll Do It to You"],
        2
    ),
    # 45 - d2
    (
        "Which romantic comedy's soundtrack features Adam Sandler performing original songs like 'Somebody Kill Me' and 'Grow Old with You'?",
        "The Wedding Singer",
        ["50 First Dates", "Big Daddy", "Happy Gilmore"],
        2
    ),
    # 46 - d2
    (
        "Which British band's song 'Lovefool' became an international pop phenomenon in 1996 after appearing in 'Romeo + Juliet' and rom-com trailers?",
        "The Cardigans",
        ["The Cranberries", "The Sundays", "Garbage"],
        2
    ),
    # 47 - d2
    (
        "Which iconic singer performed the Academy Award-nominated closing theme 'Storybook Love' for Rob Reiner's 'The Princess Bride'?",
        "Willy DeVille",
        ["Joe Cocker", "Bryan Adams", "Sting"],
        2
    ),
    # 48 - d2
    (
        "Which American rock band's song 'Accidentally in Love' was written specifically for the opening honeymoon sequence of 'Shrek 2'?",
        "Counting Crows",
        ["Smash Mouth", "Goo Goo Dolls", "Third Eye Blind"],
        2
    ),
    # 49 - d2
    (
        "Which soul ballad by Solomon Burke serves as the sensual soundtrack to Baby and Johnny's rehearsal in 'Dirty Dancing'?",
        "Cry to Me",
        ["A Change Is Gonna Come", "These Arms of Mine", "Stand by Me"],
        2
    ),
    # 50 - d2
    (
        "Which dream pop song by Mazzy Star became a staple of 1990s romance films and teen soundtracks, defining intimate bedroom slow dances?",
        "Fade Into You",
        ["Into Dust", "Flowers in December", "Halah"],
        2
    ),
    # 51 - d2
    (
        "Which Oscar-nominated actress turned down the lead in 'Pretty Woman' because she found the character and script demeaningly sexist?",
        "Michelle Pfeiffer",
        ["Glenn Close", "Sigourney Weaver", "Meryl Streep"],
        2
    ),
    # 52 - d2
    (
        "Which acclaimed actor screen-tested with Julia Roberts for the male lead in 'Pretty Woman' before dropping out of the production?",
        "Al Pacino",
        ["Dustin Hoffman", "Robert De Niro", "Jack Nicholson"],
        2
    ),
    # 53 - d2
    (
        "Which comedy star and filmmaker turned down the role of Harry Burns in 'When Harry Met Sally...' because he thought it sounded too much like Woody Allen?",
        "Albert Brooks",
        ["Steve Martin", "Dan Aykroyd", "Harold Ramis"],
        2
    ),
    # 54 - d2
    (
        "Which actor originally auditioned for the role of wealthy Christian Stovitz in 'Clueless' before director Amy Heckerling cast him as Josh?",
        "Paul Rudd",
        ["Breckin Meyer", "Jeremy Sisto", "Donald Faison"],
        2
    ),
    # 55 - d2
    (
        "Which Australian actor beat out hundreds of American hopefuls including Ashton Kutcher and Josh Hartnett for Patrick Verona in '10 Things I Hate About You'?",
        "Heath Ledger",
        ["Hugh Jackman", "Guy Pearce", "Simon Baker"],
        2
    ),
    # 56 - d2
    (
        "Which English actor was considered for the role of Charles in 'Four Weddings and a Funeral' before Hugh Grant blew away the producers with his tape?",
        "Alan Rickman",
        ["Kenneth Branagh", "Ralph Fiennes", "Jeremy Irons"],
        2
    ),
    # 57 - d2
    (
        "Which British actress turned down the title role in 'Bridget Jones's Diary' because she was starring on Broadway in 'The Wild Party'?",
        "Toni Collette",
        ["Rachel Weisz", "Emily Mortimer", "Kate Winslet"],
        2
    ),
    # 58 - d2
    (
        "Which actor was cast in 'The Wedding Planner' as Dr. Steve Edison opposite Jennifer Lopez after Antonio Banderas dropped out?",
        "Matthew McConaughey",
        ["Brendan Fraser", "Mark Ruffalo", "Ben Affleck"],
        2
    ),
    # 59 - d2
    (
        "Which actor did Nancy Meyers write the role of Hollywood film composer Miles Dumont in 'The Holiday' specifically for?",
        "Jack Black",
        ["Paul Rudd", "Jason Segel", "Steve Carell"],
        2
    ),
    # 60 - d2
    (
        "Which television actress was originally cast as Dorothy Boyd in 'Jerry Maguire' and screen-tested with Tom Cruise before Renée Zellweger replaced her?",
        "Connie Britton",
        ["Courteney Cox", "Lauren Graham", "Maura Tierney"],
        2
    ),
    # 61 - d2
    (
        "Which comedy legend turned down the lead role in 'Groundhog Day' because he admitted he 'didn't get' the script when he read it?",
        "Michael Keaton",
        ["John Belushi", "Eddie Murphy", "Martin Short"],
        2
    ),
    # 62 - d2
    (
        "Which actor was cast as Mark Darcy in 'Bridget Jones's Diary' largely because author Helen Fielding had based the character on his BBC TV role?",
        "Colin Firth",
        ["Hugh Grant", "Alan Rickman", "Pierce Brosnan"],
        2
    ),
    # 63 - d2
    (
        "Which breakout star of 'Crazy Rich Asians' was discovered while working as a BBC travel television host in London and Singapore?",
        "Henry Golding",
        ["Ronny Chieng", "Harry Shum Jr.", "Chris Pang"],
        2
    ),
    # 64 - d2
    (
        "Which lead actress almost had to pass on 'Crazy Rich Asians' due to ABC sitcom conflicts until director Jon M. Chu accommodated her schedule?",
        "Constance Wu",
        ["Gemma Chan", "Awkwafina", "Sonoya Mizuno"],
        2
    ),
    # 65 - d2
    (
        "How many days of filming did Keanu Reeves have available to shoot his hilarious extended cameo in 'Always Be My Maybe'?",
        "Four days",
        ["One day", "Ten days", "Two weeks"],
        2
    ),
    # 66 - d2
    (
        "Which 'Friends' star turned down the male lead in 'My Best Friend's Wedding' because he chose to direct the television movie 'Since You've Been Gone'?",
        "David Schwimmer",
        ["Matthew Perry", "Matt LeBlanc", "Paul Rudd"],
        2
    ),
    # 67 - d2
    (
        "Where did Drew Barrymore and Adam Sandler meet to discuss partnering up for what became their hit romantic comedy 'The Wedding Singer'?",
        "Over breakfast at a diner eating pancakes",
        ["At an SNL afterparty at Rockefeller Center", "At a Hollywood agency rooftop mixer", "In the Universal Studios commissary"],
        2
    ),
    # 68 - d2
    (
        "Which lead actress publicly criticized 'Knocked Up' in a 2007 Vanity Fair interview, expressing discomfort with how women were portrayed?",
        "Katherine Heigl",
        ["Leslie Mann", "Kristen Wiig", "Paul Rudd"],
        2
    ),
    # 69 - d2
    (
        "Which actress was cast in 'When Harry Met Sally...' after director Rob Reiner was charmed by her comedic timing in 'Innerspace' (1987)?",
        "Meg Ryan",
        ["Melanie Griffith", "Demi Moore", "Kelly McGillis"],
        2
    ),
    # 70 - d2
    (
        "Which 1999 romantic comedy's casting director discovered Heath Ledger through a self-taped Australian audition tape that immediately stood out?",
        "10 Things I Hate About You",
        ["She's All That", "Never Been Kissed", "Drive Me Crazy"],
        2
    ),

    # 71 - d3
    (
        "Which indie singer-songwriter wrote and performed the melancholic acoustic soundtrack songs 'The Wind' and 'Hero' in '(500) Days of Summer'?",
        "Regina Spektor",
        ["Feist", "Cat Power", "Fiona Apple"],
        3
    ),
    # 72 - d3
    (
        "Which song by The Sundays from their 1997 album played during the romantic prom sequence in the high school comedy 'SubUrbia' and 90s indie rom-coms?",
        "Summertime",
        ["Here's Where the Story Ends", "Wild Horses", "Can't Be Sure"],
        3
    ),
    # 73 - d3
    (
        "Which British soul artist sang the lush romantic ballad 'Kissing You' featured during the fish tank encounter in 'Romeo + Juliet'?",
        "Des'ree",
        ["Sade", "Seal", "Lisa Stansfield"],
        3
    ),
    # 74 - d3
    (
        "Which 1980s singer-songwriter wrote and sang the theme song 'Crazy for You' for the 1985 romantic drama/comedy 'Vision Quest'?",
        "Madonna",
        ["Cyndi Lauper", "Pat Benatar", "Belinda Carlisle"],
        3
    ),
    # 75 - d3
    (
        "Which Grammy-winning jazz record by Harry Connick Jr. served as the official soundtrack album for 'When Harry Met Sally...', certified double platinum?",
        "We Are in Love",
        ["20", "Blue Light, Red Light", "When My Heart Finds Christmas"],
        3
    ),
    # 76 - d3
    (
        "In 'High Fidelity', what song does Jack Black's character Barry surprise the entire club audience by singing passionately at the end of the film?",
        "Let's Get It On by Marvin Gaye",
        ["Sexual Healing by Marvin Gaye", "Superstition by Stevie Wonder", "Tracks of My Tears by Smokey Robinson"],
        3
    ),
    # 77 - d3
    (
        "Which French pop musician and composer created the entire instrumental accordion and piano score for Jean-Pierre Jeunet's 'Amélie'?",
        "Yann Tiersen",
        ["Ludovico Einaudi", "Émilie Simon", "Benjamin Biolay"],
        3
    ),
    # 78 - d3
    (
        "In 'Rye Lane' (2023), which British musician and producer composed the vibrant, contemporary neo-soul and hip-hop original score?",
        "Kwes",
        ["Dev Hynes", "Floating Points", "Sampha"],
        3
    ),
    # 79 - d3
    (
        "Which 1980s pop standard by Spandau Ballet plays during the memorable high school slow-dance sequence in 'The Wedding Singer'?",
        "True",
        ["Gold", "Through the Barricades", "Only When You Leave"],
        3
    ),
    # 80 - d3
    (
        "Which 1990 romantic comedy soundtrack spent three weeks at #1 on the Billboard 200, certified triple platinum with hits by Roxette and Go West?",
        "Pretty Woman",
        ["Ghost", "Dances with Wolves", "Home Alone"],
        3
    ),
    # 81 - d3
    (
        "Which Oscar-winning actress was originally attached to star as Kathleen Kelly in 'You've Got Mail' before Meg Ryan signed on?",
        "Nicole Kidman",
        ["Jodie Foster", "Holly Hunter", "Emma Thompson"],
        3
    ),
    # 82 - d3
    (
        "Which actress was originally cast as Vivian Ward in 'Pretty Woman' when it was still titled '$3,000' at Touchstone before being recast?",
        "Julia Roberts remained cast despite studio ownership changes",
        ["Valeria Golino", "Robin Wright", "Winona Ryder"],
        3
    ),
    # 83 - d3
    (
        "Which actor was considered for the role of Westley in 'The Princess Bride' before Cary Elwes's flawless English swashbuckler audition?",
        "Colin Firth",
        ["Pierce Brosnan", "Christopher Lambert", "Kenneth Branagh"],
        3
    ),
    # 84 - d3
    (
        "Which Oscar-winning British actress was considered for Bridget Jones before Renée Zellweger's casting caused tabloid controversy?",
        "Helena Bonham Carter",
        ["Emma Watson", "Keira Knightley", "Rosamund Pike"],
        3
    ),
    # 85 - d3
    (
        "Which actor was originally offered the role of sports agent Bob Sugar in 'Jerry Maguire' before Jay Mohr was cast?",
        "Philip Seymour Hoffman",
        ["Hank Azaria", "Jon Cryer", "Christian Slater"],
        3
    ),
    # 86 - d3
    (
        "Which actress auditioned for the role of Kat Stratford in '10 Things I Hate About You' before Julia Stiles won the part?",
        "Katie Holmes",
        ["Kirsten Dunst", "Larisa Oleynik", "Tara Reid"],
        3
    ),
    # 87 - d3
    (
        "Which actress played Bianca Stratford in '10 Things I Hate About You', having previously starred in Nickelodeon's 'The Secret World of Alex Mack'?",
        "Larisa Oleynik",
        ["Melissa Joan Hart", "Amanda Bynes", "Danielle Fishel"],
        3
    ),
    # 88 - d3
    (
        "Which actress auditioned for the role of Cher in 'Clueless' and later starred opposite Paul Rudd in 'The Object of My Affection'?",
        "Jennifer Aniston",
        ["Gwyneth Paltrow", "Courteney Cox", "Cameron Diaz"],
        3
    ),
    # 89 - d3
    (
        "Which British actor auditioned for the role of Hugh Grant's bohemian flatmate Spike in 'Notting Hill' before Rhys Ifans was cast?",
        "David Thewlis",
        ["Eddie Izzard", "Paul Bettany", "Mark Addy"],
        3
    ),
    # 90 - d3
    (
        "Which actor was Garry Marshall's initial choice to play hotel manager Barney Thompson in 'Pretty Woman', before casting Hector Elizondo?",
        "Hector Elizondo was always Marshall's good-luck charm and first choice",
        ["Alan Alda", "Gene Hackman", "Charles Durning"],
        3
    ),
    # 91 - d3
    (
        "In 'Pretty Woman', how many feature films did Hector Elizondo appear in with director Garry Marshall across Marshall's career?",
        "Over 15 films (he appeared in all 18 of Marshall's directed features)",
        ["Exactly 5 films", "Exactly 8 films", "Exactly 10 films"],
        3
    ),
    # 92 - d3
    (
        "Which actor was originally considered for the role of Lloyd Dobler in 'Say Anything...' before Cameron Crowe met John Cusack?",
        "Robert Downey Jr.",
        ["Emilio Estevez", "Judd Nelson", "Anthony Michael Hall"],
        3
    ),
    # 93 - d3
    (
        "Which actress was offered the role of Julianne Potter in 'My Best Friend's Wedding' by the studio before Julia Roberts chose it?",
        "Julia Roberts had first-look script privilege and selected it herself",
        ["Demi Moore", "Sandra Bullock", "Meg Ryan"],
        3
    ),
    # 94 - d3
    (
        "Which actor did Julia Roberts personally select to play her charming fiancé-turned-target Michael O'Neal in 'My Best Friend's Wedding'?",
        "Dermot Mulroney",
        ["Dylan McDermott", "Matthew Broderick", "Campbell Scott"],
        3
    ),
    # 95 - d3
    (
        "Which actress was originally cast as the lead in 'While You Were Sleeping' when the project was envisioned with a male rescuer and female comatose patient?",
        "Demi Moore",
        ["Julia Roberts", "Meg Ryan", "Geena Davis"],
        3
    ),
    # 96 - d3
    (
        "Which actor turned down the lead role in 'Serendipity' (2001) before John Cusack was cast?",
        "Hugh Grant",
        ["Tom Hanks", "Ben Stiller", "Ethan Hawke"],
        3
    ),
    # 97 - d3
    (
        "Which actress turned down the female lead in 'Serendipity' opposite John Cusack due to filming conflicts with 'Friends'?",
        "Jennifer Aniston",
        ["Courteney Cox", "Lisa Kudrow", "Téa Leoni"],
        3
    ),
    # 98 - d3
    (
        "Which actor was considered for the role of Edward Lewis in 'Pretty Woman' before Richard Gere accepted the offer?",
        "Christopher Reeve",
        ["Harrison Ford", "Mel Gibson", "Kevin Costner"],
        3
    ),
    # 99 - d3
    (
        "Which actress was considered for Sally Albright in 'When Harry Met Sally...' after Susan Dey declined the offer?",
        "Elizabeth Perkins",
        ["Geena Davis", "Sigourney Weaver", "Glenn Close"],
        3
    ),
    # 100 - d3
    (
        "Which actress was considered for the role of Cher in 'Clueless' before Amy Heckerling spotted Alicia Silverstone?",
        "Sarah Michelle Gellar",
        ["Alicia Witt", "Denise Richards", "Shannon Elizabeth"],
        3
    ),
]

if __name__ == "__main__":
    make_batch(questions_batch4, 4, "tools/staging/rom_com_batch4.json")
