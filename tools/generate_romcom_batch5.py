#!/usr/bin/env python3
"""
Generate Batch 5 for Romantic Comedies:
100 Extratextual questions (Improv moments, behind-the-scenes production lore, real-life inspirations, on-set accidents, alternate endings, contemporary critical reviews).
Difficulty: 30 d1, 40 d2, 30 d3.
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))
from rom_com_builder import make_batch

questions_batch5 = [
    # 1 - d1
    (
        "In 'Pretty Woman', what famous spontaneous gesture by Richard Gere made Julia Roberts burst into genuine, unscripted laughter?",
        "He playfully snapped the jewelry box shut on her fingers",
        ["He tripped over a chair while offering her champagne", "He accidentally spilled strawberries down his tuxedo", "He spoke to her in an exaggerated French accent"],
        1
    ),
    # 2 - d1
    (
        "Who delivered the immortal line 'I'll have what she's having' in 'When Harry Met Sally...', as an inside family cameo?",
        "Estelle Reiner, director Rob Reiner's real-life mother",
        ["Nora Ephron, the screenwriter", "Jane Jenkins, the casting director", "Meg Ryan's mother"],
        1
    ),
    # 3 - d1
    (
        "In 'Clueless', what real-life pronunciation mistake did Alicia Silverstone make during Cher's speech that director Amy Heckerling kept in the film?",
        "She mispronounced 'Haitians' as 'Hate-ians'",
        ["She called 'dietary' 'die-terry'", "She pronounced 'ubiquitous' as 'you-bike-it-us'", "She pronounced 'pedestrian' as 'peed-estrian'"],
        1
    ),
    # 4 - d1
    (
        "In 'Roman Holiday', how did Gregory Peck genuinely terrify Audrey Hepburn during their scene at the Mouth of Truth?",
        "He pulled his hand out of the carving with his wrist hidden inside his jacket sleeve",
        ["He suddenly shouted in Italian", "He pretended to faint backwards onto the marble floor", "He dropped a fake snake into her lap"],
        1
    ),
    # 5 - d1
    (
        "In '10 Things I Hate About You', how did Julia Stiles surprise the filmmakers during Kat's emotional poem recitation?",
        "She spontaneously broke down into real tears on the first take",
        ["She threw her notebook at Patrick", "She walked out of the classroom mid-verse", "She improvised an entirely new final stanza"],
        1
    ),
    # 6 - d1
    (
        "During the filming of 'Groundhog Day', what animal injury did Bill Murray suffer that required him to get medical rabies shots?",
        "He was bitten twice by the groundhog",
        ["He was pecked by an aggressive goose", "He was scratched by a feral stray cat", "He was bitten by an agitated German Shepherd"],
        1
    ),
    # 7 - d1
    (
        "In 'Sleepless in Seattle', roughly how much screen time do lead stars Tom Hanks and Meg Ryan actually share together in person?",
        "Approximately two minutes",
        ["About twenty minutes", "Nearly forty-five minutes", "Over an hour"],
        1
    ),
    # 8 - d1
    (
        "What real-life undercover job did Renée Zellweger work for three weeks in London to master the role of Bridget Jones?",
        "An intern at a London publishing house",
        ["A cocktail waitress in Soho", "A secretary at the BBC", "A sales clerk at Harrods"],
        1
    ),
    # 9 - d1
    (
        "In 'Crazy Rich Asians', where did the iconic green emerald engagement ring worn by Michelle Yeoh actually come from?",
        "Michelle Yeoh's personal fine jewelry collection",
        ["A luxury Beverly Hills jeweler rental", "A prop bought for twenty dollars in Kuala Lumpur", "The Singapore National Museum"],
        1
    ),
    # 10 - d1
    (
        "In '(500) Days of Summer', what vengeful line appears in the opening legal disclaimer aimed at the writer's real-life ex-girlfriend?",
        "Especially you, Jenny Beckman. Bitch.",
        ["Dedicated to Sarah, who broke my heart in Paris.", "No thanks to Jessica, who knows what she did.", "Except for Rachel, who never called back."],
        1
    ),
    # 11 - d1
    (
        "Which real-life married couple turned their terrifying experience with a medically induced coma into the acclaimed romantic comedy 'The Big Sick'?",
        "Kumail Nanjiani and Emily V. Gordon",
        ["Judd Apatow and Leslie Mann", "John Krasinski and Emily Blunt", "Paul Rust and Lesley Arfin"],
        1
    ),
    # 12 - d1
    (
        "In 'My Best Friend's Wedding', why did director P.J. Hogan reshoot the film's ending before release?",
        "Test audiences hated Julianne for trying to break up the wedding and demanded she not get the groom",
        ["Julia Roberts refused to kiss Dermot Mulroney", "Cameron Diaz's character originally ran away to Europe", "The original ending was too sad with Julianne leaving alone in tears"],
        1
    ),
    # 13 - d1
    (
        "In 'It Happened One Night' (1934), what real-world industry reportedly suffered a catastrophic sales drop when Clark Gable removed his shirt to reveal a bare chest?",
        "Men's undershirt manufacturers",
        ["Men's pajama makers", "Men's necktie makers", "Men's leather belt makers"],
        1
    ),
    # 14 - d1
    (
        "In 'Love Actually', what real-life heartbreak did Emma Thompson draw upon when filming her character Karen's devastated bedroom crying scene?",
        "Her real-life divorce following her husband Kenneth Branagh's affair",
        ["The loss of her father to illness", "Her struggle with severe clinical depression", "A failed stage audition early in her career"],
        1
    ),
    # 15 - d1
    (
        "In '13 Going on 30', why did Mark Ruffalo initially want to drop out of the movie during pre-production rehearsals?",
        "He was terrified of learning and performing the 'Thriller' dance routine",
        ["He felt he was too old to play a 30-year-old high school sweetheart", "He clashed with director Gary Winick over line delivery", "He suffered a hamstring injury during athletic training"],
        1
    ),
    # 16 - d1
    (
        "In 'The Princess Bride', who improvised so extensively as Miracle Max that director Rob Reiner had to leave the set because of uncontrollable laughter?",
        "Billy Crystal",
        ["Wallace Shawn", "Peter Cook", "Christopher Guest"],
        1
    ),
    # 17 - d1
    (
        "In 'Notting Hill', what was the inside joke when Anna Scott answered that she made '$15 million' on her last movie?",
        "That was Julia Roberts's exact real-life salary for starring in Notting Hill",
        ["It was the entire production budget of Notting Hill", "It was the amount Richard Curtis earned from Four Weddings", "It was the salary of Tom Cruise in Jerry Maguire"],
        1
    ),
    # 18 - d1
    (
        "In 'When Harry Met Sally...', Sally's finicky restaurant ordering habits were taken directly from the real-life dining idiosyncrasies of which person?",
        "Screenwriter Nora Ephron",
        ["Director Rob Reiner's wife", "Actress Meg Ryan", "Producer Meg Lieberman"],
        1
    ),
    # 19 - d1
    (
        "Which iconic screen siren bought the film rights to 'The Philadelphia Story' herself to stage her triumphant Hollywood comeback after being labeled 'box office poison'?",
        "Katharine Hepburn",
        ["Bette Davis", "Joan Crawford", "Greta Garbo"],
        1
    ),
    # 20 - d1
    (
        "In 'There's Something About Mary', which infamous scene did studio executives almost force the Farrelly brothers to delete before test audiences roared with laughter?",
        "The hair gel scene on Mary's ear",
        ["The zipper scene at high school prom", "The reviving of Puffy the terrier", "The hitchhiker's 7-Minute Abs debate"],
        1
    ),
    # 21 - d1
    (
        "In 'Legally Blonde', which cardinal rule of hair care does Elle Woods cite to expose Chutney Windham's perjury on the witness stand?",
        "You cannot wash your hair within 48 hours of receiving a perm",
        ["You must never bleach colored hair with peroxide", "You cannot blow-dry wet hair after keratin treatment", "You cannot brush hair when wet without causing breakage"],
        1
    ),
    # 22 - d1
    (
        "In 'How to Lose a Guy in 10 Days', what breed of dog plays Ben Barry's dog 'Krull the Warrior King'?",
        "Chinese Crested Dog",
        ["Pug", "French Bulldog", "Chihuahua"],
        1
    ),
    # 23 - d1
    (
        "Who created the bizarre, elaborate Dracula vampire puppets featured in Peter Bretter's musical in 'Forgetting Sarah Marshall'?",
        "The Jim Henson Company",
        ["Avenue Q Puppet Workshop", "Laika Studios", "Sideshow Collectibles"],
        1
    ),
    # 24 - d1
    (
        "In 'Always Be My Maybe', which actor suggested wearing hipster glasses without lenses to emphasize his character's pretentious lifestyle?",
        "Keanu Reeves",
        ["Daniel Dae Kim", "Randall Park", "James Saito"],
        1
    ),
    # 25 - d1
    (
        "Which legendary Chicago film critic gave 'Say Anything...' a glowing 4 out of 4 stars, praising Lloyd Dobler as one of cinema's most genuine heroes?",
        "Roger Ebert",
        ["Gene Siskel", "Peter Travers", "Leonard Maltin"],
        1
    ),
    # 26 - d1
    (
        "Which 1990 romantic comedy was originally written as a dark, gritty drama about addiction and prostitution titled '$3,000'?",
        "Pretty Woman",
        ["Frankie and Johnny", "Leaving Las Vegas", "True Romance"],
        1
    ),
    # 27 - d1
    (
        "In 'When Harry Met Sally...', which famous personality was the primary real-life inspiration for Billy Crystal's cynical, neurotic character Harry Burns?",
        "Director Rob Reiner",
        ["Woody Allen", "Carl Reiner", "Larry David"],
        1
    ),
    # 28 - d1
    (
        "In 'The Princess Bride', what real injury did Cary Elwes suffer on set after joyriding on Andre the Giant's ATV before filming the sword fight?",
        "A broken big toe",
        ["A fractured wrist", "A dislocated shoulder", "A torn meniscus"],
        1
    ),
    # 29 - d1
    (
        "In 'Love Actually', which legendary British pop singer does Karen listen to while weeping in her bedroom after finding the necklace intended for another woman?",
        "Joni Mitchell",
        ["Carole King", "Kate Bush", "Dusty Springfield"],
        1
    ),
    # 30 - d1
    (
        "In 'Bridesmaids', what real-life improv comedy troupe in Los Angeles served as the training ground for Kristen Wiig, Maya Rudolph, and Melissa McCarthy?",
        "The Groundlings",
        ["Second City", "Upright Citizens Brigade", "ImprovOlympic"],
        1
    ),

    # 31 - d2
    (
        "In 'Four Weddings and a Funeral', which future British cabinet minister and Home Secretary served as the production's 'aristocracy coordinator'?",
        "Amber Rudd",
        ["Theresa May", "Priti Patel", "Liz Truss"],
        2
    ),
    # 32 - d2
    (
        "In 'Notting Hill', what famous line was inscribed on the wooden garden bench where William and Anna sit at the end of the movie?",
        "For June who loved this garden. From Joseph who always sat beside her.",
        ["In memory of sweet love that never dies.", "To Anna and William, lovers in the rain.", "For all who walk this path in search of hope."],
        2
    ),
    # 33 - d2
    (
        "In 'The Princess Bride', which co-star reportedly bruised a rib from desperately holding in his laughter while Billy Crystal ad-libbed as Miracle Max?",
        "Mandy Patinkin",
        ["Cary Elwes", "Andre the Giant", "Wallace Shawn"],
        2
    ),
    # 34 - d2
    (
        "In 'While You Were Sleeping', what major gender-swap was made by the screenwriters to avoid the premise coming across as creepy?",
        "Originally a man pretended to be the fiancé of a comatose woman",
        ["Originally two sisters fought over the same comatose man", "Originally Lucy was an undercover policewoman", "Originally the grandmother was in a coma"],
        2
    ),
    # 35 - d2
    (
        "In 'Groundhog Day', roughly how long did director Harold Ramis publicly state Phil Connors was trapped in the Punxsutawney time loop?",
        "Around 30 to 40 years",
        ["Exactly 100 days", "One full calendar year", "Over 1,000 years"],
        2
    ),
    # 36 - d2
    (
        "In 'Say Anything...', where did writer-director Cameron Crowe get the inspiration for Lloyd Dobler holding the boombox over his head?",
        "Seeing a neighborhood teenager playing music outside a girl's window in Los Angeles",
        ["An old European tradition of serenading lovers with accordions", "A dream he had while listening to Peter Gabriel's 'So' album", "A scene cut from 'Fast Times at Ridgemont High'"],
        2
    ),
    # 37 - d2
    (
        "In 'Jerry Maguire', which real-life NFL wide receiver inspired Rod Tidwell's iconic demand: 'Show me the money!'?",
        "Tim McDonald",
        ["Jerry Rice", "Michael Irvin", "Deion Sanders"],
        2
    ),
    # 38 - d2
    (
        "In 'Legally Blonde', where did screenwriters Karen McCullah and Kirsten Smith invent the famous 'Bend and Snap' routine?",
        "In a bar in Los Angeles while brainstorming physical comedy moves",
        ["During an aerobics dance class at an LA gym", "From a vintage 1950s charm school etiquette manual", "At a sorority mixer in Stanford"],
        2
    ),
    # 39 - d2
    (
        "In 'Four Weddings and a Funeral', why did the wedding guests and extras all wear their own personal formalwear?",
        "The production had a micro-budget of only $4 million and couldn't afford costume rentals",
        ["Director Mike Newell wanted an authentic documentary look", "The costumes were lost in transit from France", "A costume designer strike shut down wardrobe access"],
        2
    ),
    # 40 - d2
    (
        "Which prestigious New York Times film critic initially described 'When Harry Met Sally...' as a sitcom in feature-length clothing before praising its comedic energy?",
        "Vincent Canby",
        ["AO Scott", "Frank Rich", "Janet Maslin"],
        2
    ),
    # 41 - d2
    (
        "In 'Breakfast at Tiffany's', which author was notoriously furious when Audrey Hepburn was cast as Holly Golightly instead of Marilyn Monroe?",
        "Truman Capote",
        ["Tennessee Williams", "Gore Vidal", "Norman Mailer"],
        2
    ),
    # 42 - d2
    (
        "During the filming of 'Some Like It Hot' (1959), which star required up to 47 takes to deliver simple one-line dialogue due to intense anxiety?",
        "Marilyn Monroe",
        ["Tony Curtis", "Jack Lemmon", "George Raft"],
        2
    ),
    # 43 - d2
    (
        "In 'Annie Hall', what was Woody Allen's original working title for the film before distributor and editor Ralph Rosenblum intervened?",
        "Anhedonia",
        ["Manhattan Romance", "The Neurotic Lover", "Me and Annie"],
        2
    ),
    # 44 - d2
    (
        "In 'Annie Hall', what genre was the film originally conceived and shot as before being radically re-edited into a romantic comedy?",
        "A murder mystery and psychological puzzle",
        ["A broad slapstick farce", "A musical comedy", "A serious drama about existential depression"],
        2
    ),
    # 45 - d2
    (
        "In 'Pillow Talk' (1959), what affectionate nickname did Rock Hudson use for his lifelong friend and co-star Doris Day?",
        "Eunice",
        ["Dodo", "Sunny", "Daisy"],
        2
    ),
    # 46 - d2
    (
        "In 'Groundhog Day', the bitter friction between Bill Murray and director Harold Ramis on set resulted in what tragic real-life outcome?",
        "They stopped speaking to each other for over twenty years until just before Ramis's death",
        ["Murray sued Ramis for breach of contract over script changes", "Ramis was banned from directing Murray's future films", "The movie was shelved for six months during production"],
        2
    ),
    # 47 - d2
    (
        "In 'The Holiday', which legendary Hollywood film actor made an unscripted, spontaneous cameo appearance inside the Los Angeles video rental store?",
        "Dustin Hoffman",
        ["Jack Nicholson", "Warren Beatty", "Robert Redford"],
        2
    ),
    # 48 - d2
    (
        "In 'Crazy Rich Asians', how much of Peik Lin's wild and flamboyant dialogue did Awkwafina estimate she improvised on the spot?",
        "Almost all of her comedic one-liners and physical reactions",
        ["None, it was strictly adhered to from Kevin Kwan's book", "Only her lines in the opening boutique scene", "Only her driving banter in the sports car"],
        2
    ),
    # 49 - d2
    (
        "In 'Moonstruck', what quirky acting influence did Nicolas Cage explicitly draw upon for his intense performance as Ronny Cammareri?",
        "Klaus Kinski in 'Nosferatu the Vampyre'",
        ["Marlon Brando in 'A Streetcar Named Desire'", "Humphrey Bogart in 'Casablanca'", "James Dean in 'East of Eden'"],
        2
    ),
    # 50 - d2
    (
        "In 'Broadcast News', which network news anchorman served as the real-life model for William Hurt's handsome, charming anchor Tom Grunick?",
        "Peter Jennings",
        ["Dan Rather", "Tom Brokaw", "Ted Koppel"],
        2
    ),
    # 51 - d2
    (
        "In 'Clueless', who coached Alicia Silverstone and the young cast on contemporary 1990s Beverly Hills high school slang?",
        "Director Amy Heckerling, who sat in on classes at Beverly Hills High School",
        ["Costume designer Mona May", "A youth linguistics professor from UCLA", "Paul Rudd and Donald Faison"],
        2
    ),
    # 52 - d2
    (
        "In '10 Things I Hate About You', what location served as the stunning castle-like facade of Padua High School?",
        "Stadium High School in Tacoma, Washington",
        ["Seattle Central College", "Tacoma Castle Academy", "Bellingham High School"],
        2
    ),
    # 53 - d2
    (
        "In 'My Best Friend's Wedding', what was Rupert Everett's character George Downes's original role in the script before reshoots expanded his presence?",
        "A minor character appearing in only two brief telephone scenes",
        ["A rival chef in New York", "Michael's college roommate", "A fashion photographer in Chicago"],
        2
    ),
    # 54 - d2
    (
        "In 'When Harry Met Sally...', what real-life friendship inspired the banter and relationship between Harry Burns and Jess?",
        "The real-life friendship between director Rob Reiner and Billy Crystal",
        ["The partnership between Nora Ephron and Carl Bernstein", "The dynamic between Woody Allen and Tony Roberts", "The bond between Albert Brooks and Rob Reiner"],
        2
    ),
    # 55 - d2
    (
        "In 'Pretty Woman', what was the genuine security protocol for the multi-million dollar diamond and ruby necklace Vivian wears to the opera?",
        "An armed security guard stood behind director Garry Marshall during filming",
        ["It was kept in a mobile armored bank vault parked outside", "Julia Roberts was required to sign an hourly insurance indemnity waiver", "A jeweler was handcuffed to the sound technician"],
        2
    ),
    # 56 - d2
    (
        "In 'Say Anything...', which scene was shot on the very last day of production in an empty airplane cabin?",
        "The final scene of Lloyd and Diane waiting for the seatbelt sign to ding",
        ["Lloyd's kickboxing training sequence", "The graduation party aftermath", "The pawnshop argument over the watch"],
        2
    ),
    # 57 - d2
    (
        "In 'Bridget Jones's Diary', what did Renée Zellweger keep on her desk during her undercover publishing job to stay in character?",
        "A framed photograph of Hugh Grant",
        ["A bottle of gin and a pack of Silk Cut cigarettes", "A miniature union jack flag", "A dictionary of Cockney rhyming slang"],
        2
    ),
    # 58 - d2
    (
        "In 'Palm Springs', over how many days was the high-concept sci-fi romantic comedy filmed in Santa Clarita, California?",
        "21 days",
        ["10 days", "45 days", "60 days"],
        2
    ),
    # 59 - d2
    (
        "In 'Rye Lane', which iconic Oscar-winning actor makes an unexpected, hilarious cameo serving burritos inside 'Love Guacamole'?",
        "Colin Firth",
        ["Hugh Grant", "Gary Oldman", "Daniel Kaluuya"],
        2
    ),
    # 60 - d2
    (
        "In 'Set It Up', what real-life dynamic did screenwriter Katie Silberman base the frantic assistant camaraderie on?",
        "Her real-life tenure working as an overworked assistant in Hollywood",
        ["Her experience in a high-stakes Manhattan corporate law firm", "A reality TV production office in Burbank", "An internship at Vogue magazine"],
        2
    ),
    # 61 - d2
    (
        "In 'Crazy, Stupid, Love.', which scene was inspired by an actual real-life argument between screenwriters Glenn Ficarra and John Requa?",
        "The climactic parent-teacher conference brawl in the school backyard",
        ["The locker room advice session between Jacob and Cal", "The shopping mall clothing intervention", "The rain-soaked confession outside Emily's house"],
        2
    ),
    # 62 - d2
    (
        "In 'Silver Linings Playbook', how did director David O. Russell come to adapt Matthew Quick's novel about bipolar disorder?",
        "His own son suffers from bipolar disorder and OCD, making the story deeply personal",
        ["Robert De Niro gave him the book as a birthday gift", "Bradley Cooper optioned the film rights and brought it to him", "The Weinstein Company assigned him the project as a work-for-hire"],
        2
    ),
    # 63 - d2
    (
        "In 'Forgetting Sarah Marshall', who encouraged Jason Segel to write the film after seeing his heartbreak over real-life breakups?",
        "Judd Apatow",
        ["Paul Rudd", "Seth Rogen", "Nicholas Stoller"],
        2
    ),
    # 64 - d2
    (
        "In 'Knocked Up', why were certain close-up delivery shots in the climax blurred or edited for the theatrical release?",
        "They used actual graphic documentary footage of a childbirth that alarmed test audiences",
        ["Katherine Heigl refused to simulate real contractions", "The studio feared an NC-17 rating from the MPAA", "The camera lens cracked during filming"],
        2
    ),
    # 65 - d2
    (
        "In 'Trainwreck' (2015), which real-life NBA superstar won widespread critical acclaim for his hilarious comedic performance playing himself as cheap and sensitive?",
        "LeBron James",
        ["Kobe Bryant", "Kevin Durant", "Shaquille O'Neal"],
        2
    ),
    # 66 - d2
    (
        "In 'The Wedding Singer', which real-life 1980s music video inspired Robbie Hart's messy blue ruffled tuxedo shirt?",
        "Culture Club and Boy George's theatrical fashion style",
        ["Duran Duran's 'Rio' yacht suits", "Wham!'s neon beachwear", "Michael Jackson's 'Thriller' jacket"],
        2
    ),
    # 67 - d2
    (
        "In '10 Things I Hate About You', how did Heath Ledger prepare for his musical serenade on the stadium bleachers?",
        "He drew inspiration from Gene Kelly in 'Singin' in the Rain'",
        ["He studied Mick Jagger's live concert swagger", "He rehearsed with the high school marching band for three months", "He watched Elvis Presley's 'Jailhouse Rock'"],
        2
    ),
    # 68 - d2
    (
        "In 'You've Got Mail', what real-life independent New York bookstore inspired Kathleen Kelly's 'The Shop Around the Corner'?",
        "Books of Wonder in Manhattan",
        ["Strand Book Store", "Corner Bookstore on Madison Ave", "Shakespeare & Co. Booksellers"],
        2
    ),
    # 69 - d2
    (
        "In 'Sleepless in Seattle', which iconic building's management was initially reluctant to let Nora Ephron film the heart-shaped rooftop lighting?",
        "The Empire State Building",
        ["The Chrysler Building", "Rockefeller Center", "The Space Needle"],
        2
    ),
    # 70 - d2
    (
        "In 'Pretty Woman', who provided the singing voice for Vivian Ward when she sings in the bathtub wearing headphones?",
        "Julia Roberts herself (singing off-key to Prince's 'Kiss')",
        ["A professional studio vocal double", "Paula Abdul", "Belinda Carlisle"],
        2
    ),

    # 71 - d3
    (
        "In 'When Harry Met Sally...', what line did Billy Crystal ad-lib in the diner after Meg Ryan's fake orgasm that Rob Reiner loved and kept in the final cut?",
        "Pablum! (when looking over his sandwich)",
        ["That was incredible!", "I think I lost my appetite", "Can I get some mustard over here?"],
        3
    ),
    # 72 - d3
    (
        "In 'The Princess Bride', which member of the cast suffered from severe back pain and could not lift Cary Elwes, requiring a hidden cable harness?",
        "Andre the Giant",
        ["Pat Roach", "Wallace Shawn", "Peter Cook"],
        3
    ),
    # 73 - d3
    (
        "In 'Groundhog Day', what was screenwriter Danny Rubin's original narrative structure before Harold Ramis reorganized it chronologically?",
        "The film opened with Phil already stuck in the time loop for decades, without showing day one",
        ["The story was told in reverse from day 10,000 back to day 1", "Phil was trapped because an ex-lover placed a gypsy curse on him", "Rita was also trapped in the loop secretly the entire time"],
        3
    ),
    # 74 - d3
    (
        "In 'It Happened One Night', how much was Columbia Pictures forced to pay Frank Capra per week during the desperate production of the low-budget movie?",
        "Frank Capra was under contract and received a $100,000 bonus after it swept the Oscars",
        ["A nominal $500 weekly stipend", "Half of Columbia's box office shares", "No salary, working solely on deferred percentages"],
        3
    ),
    # 75 - d3
    (
        "In 'The Philadelphia Story', what was the original Broadway stage run that Katharine Hepburn starred in before bringing it to MGM?",
        "417 performances at the Shubert Theatre",
        ["Over 1,000 performances at the Lyceum", "Only 50 performances before closing", "A two-year national tour without a Broadway run"],
        3
    ),
    # 76 - d3
    (
        "In 'Roman Holiday', why was the film shot in black and white rather than lush Technicolor despite Rome's breathtaking scenery?",
        "Budget constraints forced director William Wyler to shoot on monochrome film stock",
        ["Audrey Hepburn requested black and white to match European neorealism", "Technicolor processing equipment was banned in Rome at the time", "Paramount insisted Technicolor was reserved only for musicals"],
        3
    ),
    # 77 - d3
    (
        "In 'Bringing Up Baby' (1938), what trick did director Howard Hawks use to get the tame leopard 'Nissa' to rub affectionately against Cary Grant and Katharine Hepburn?",
        "Spraying perfume and chicken broth onto their skirts and trousers",
        ["Hiding fresh sardines inside their pockets", "Playing soothing classical harp music between takes", "Keeping a trainer off-camera with a whip"],
        3
    ),
    # 78 - d3
    (
        "In 'His Girl Friday' (1940), what technical sound innovation did Howard Hawks pioneer to capture the rapid-fire overlapping dialogue?",
        "Multiple directional overhead microphones switched on and off manually by sound engineers",
        ["Pre-recording dialogue tracks in an echo chamber", "Wireless lapel microphones hidden inside hat brims", "Speeding up the magnetic sound reels in post-production by 10%"],
        3
    ),
    # 79 - d3
    (
        "In 'Broadcast News', how many takes did James L. Brooks require for Joan Cusack's legendary mad dash with the broadcast tape to make air?",
        "Dozens of takes until Joan Cusack was genuinely breathless and bruised",
        ["Exactly two takes on the first morning", "It was captured in a single flawless rehearsal take", "Only four takes before Cusack tripped and sprained her ankle"],
        3
    ),
    # 80 - d3
    (
        "In 'Moonstruck', what real-life New York bakery was used as the setting for the Cammareri Brothers Bakery in Brooklyn?",
        "Cammareri Brothers Bakery on Henry Street in Carroll Gardens",
        ["Ferrara Bakery in Little Italy", "Veniero's Pasticceria in East Village", "Court Pastry Shop in Cobble Hill"],
        3
    ),
    # 81 - d3
    (
        "In 'Say Anything...', what was John Cusack's condition before agreeing to hold the boombox in the immortal roadside scene?",
        "He insisted on playing Fishbone's music on set, though Peter Gabriel was later dubbed in",
        ["He demanded that Cameron Crowe shoot it in broad daylight", "He refused to wear Lloyd's trench coat during the shot", "He demanded that Diane look out the window in the same frame"],
        3
    ),
    # 82 - d3
    (
        "In 'Jerry Maguire', who coined the phrase 'You had me at hello' during script development?",
        "Cameron Crowe wrote it directly in the script, drawing from his own romantic experiences",
        ["Renée Zellweger ad-libbed it when she forgot her line", "Tom Cruise whispered it during their living room rehearsal", "Producer James L. Brooks suggested it during editing"],
        3
    ),
    # 83 - d3
    (
        "In 'Notting Hill', what happened to the famous blue front door of William Thacker's flat after the movie became a worldwide phenomenon?",
        "It was auctioned off for charity at Christie's because fans kept defacing it with graffiti",
        ["It was stolen by overzealous fans in the middle of the night", "It was preserved by the British Film Institute in London", "It was painted hot pink by the new homeowners to deter tourists"],
        3
    ),
    # 84 - d3
    (
        "In 'Notting Hill', who actually owned the flat with the famous blue door on Westbourne Park Road during production?",
        "Screenwriter Richard Curtis",
        ["Director Roger Michell", "Producer Duncan Kenworthy", "Hugh Grant's brother"],
        3
    ),
    # 85 - d3
    (
        "In 'Four Weddings and a Funeral', what was the production budget of the film that went on to gross over $245 million worldwide?",
        "Under $4 million (£2.7 million)",
        ["Around $15 million", "$25 million", "$8 million"],
        3
    ),
    # 86 - d3
    (
        "In 'Bridget Jones's Diary', which real-life author and friend of Helen Fielding has a brief speaking cameo at the book launch party?",
        "Salman Rushdie",
        ["Martin Amis", "Julian Barnes", "Ian McEwan"],
        3
    ),
    # 87 - d3
    (
        "In 'Clueless', what real-life high school tradition inspired the debate between Cher and Amber over tennis attire?",
        "Amy Heckerling observed real Beverly Hills teens negotiating P.E. excuses with gym teachers",
        ["A costume designer's high school memories in New Jersey", "A scene in Jane Austen's 'Emma' involving archery practice", "An article in Seventeen magazine about high school dress codes"],
        3
    ),
    # 88 - d3
    (
        "In '10 Things I Hate About You', what was the origin of the film's title according to screenwriter Karen McCullah?",
        "A diary entry from her own high school days about an ex-boyfriend titled 'Things I Hate About Anthony'",
        ["A line cut from Shakespeare's 'The Taming of the Shrew'", "A list written by Julia Stiles during table reads", "A brainstorming session by producer Andrew Lazar"],
        3
    ),
    # 89 - d3
    (
        "In 'Pretty Woman', what trick did Garry Marshall use to get Julia Roberts to laugh hysterically in the scene where she watches 'I Love Lucy' on the floor?",
        "Marshall stood just off-camera and physically tickled her feet",
        ["He told crude backstage jokes through a megaphone", "He made funny faces wearing a giant clown wig", "He had Richard Gere dance in his boxers behind the monitor"],
        3
    ),
    # 90 - d3
    (
        "In 'While You Were Sleeping', what Chicago weather disaster struck the production during filming, forcing the crew to create artificial snow?",
        "An unseasonably warm heatwave melted all natural snow in Chicago",
        ["A massive blizzard trapped the crew inside the hospital for four days", "A violent windstorm blew down the train station exterior set", "A sudden flood submerged the railway tracks"],
        3
    ),
    # 91 - d3
    (
        "In 'Amélie', what Parisian cafe where Amélie works as a waitress became a major tourist pilgrimage site following the film's release?",
        "Café des 2 Moulins in Montmartre",
        ["Café de Flore in Saint-Germain", "Les Deux Magots", "Café de la Paix"],
        3
    ),
    # 92 - d3
    (
        "In 'High Fidelity', why did author Nick Hornby initially hesitate before granting permission to move the film's setting from London to Chicago?",
        "He worried Chicago wouldn't understand record-nerd subculture, but was won over by John Cusack's passion",
        ["He wanted the film set in his hometown of Redbridge", "He demanded that the clerks remain British pub regulars", "He had already sold the UK rights to Channel 4"],
        3
    ),
    # 93 - d3
    (
        "In 'Crazy Rich Asians', what real-life Singapore hotel's rooftop infinity pool serves as the breathtaking setting for the climactic engagement party?",
        "Marina Bay Sands",
        ["Raffles Hotel Singapore", "The Fullerton Hotel", "Capella Singapore"],
        3
    ),
    # 94 - d3
    (
        "In 'Palm Springs', what real-life quantum physics consultant reviewed Andy Siara's screenplay to ensure the cave's time-loop theory sounded scientifically plausible?",
        "Clifford Johnson, theoretical physicist at USC",
        ["Sean Carroll, theoretical physicist at Caltech", "Brian Greene, string theorist at Columbia", "Neil deGrasse Tyson, astrophysicist"],
        3
    ),
    # 95 - d3
    (
        "In 'Always Be My Maybe', what real-life San Francisco restaurant served as the inspiration for Sasha Tran's high-end dining establishment?",
        "Modern upscale Asian fusion spots like Benu and Atelier Crenn",
        ["Classic Chinatown banquets like Far East Cafe", "Mission district taquerias", "Fisherman's Wharf seafood houses"],
        3
    ),
    # 96 - d3
    (
        "In 'Rye Lane', which iconic London South Bank cinema did Dom and Yas visit during their spontaneous daytime date?",
        "The BFI Southbank (British Film Institute)",
        ["The Odeon Leicester Square", "The Electric Cinema Notting Hill", "Curzon Soho"],
        3
    ),
    # 97 - d3
    (
        "In 'Bros' (2022), which historical LGBTQ+ institution serves as the professional project Bobby Leiber (Billy Eichner) is working to open?",
        "The first national LGBTQ+ history museum in Manhattan",
        ["The Stonewall National Monument visitor center", "The Leslie-Lohman Museum of Art expansion", "The Harvey Milk Archives in Greenwich Village"],
        3
    ),
    # 98 - d3
    (
        "In 'Fire Island' (2022), which Jane Austen character from 'Pride and Prejudice' was the direct inspiration for Bowen Yang's character Howie?",
        "Jane Bennet",
        ["Elizabeth Bennet", "Mary Bennet", "Charlotte Lucas"],
        3
    ),
    # 99 - d3
    (
        "In 'Anyone But You' (2023), what terrifying wildlife incident occurred during the filming of Ben and Bea's hike in the Australian bush?",
        "A huntsman spider used as a prop actually bit Glen Powell during the scene",
        ["A venomous brown snake slithered across Sydney Sweeney's foot", "A wild kangaroo charged into the lighting equipment", "A swarm of bluebottles stung the swimming crew in Sydney Harbour"],
        3
    ),
    # 100 - d3
    (
        "In 'Annie Hall', which future Hollywood megastar appears for literally two seconds as Alvy Singer's date outside a cinema at the end of the film?",
        "Sigourney Weaver",
        ["Meryl Streep", "Glenn Close", "Geena Davis"],
        3
    ),
]

if __name__ == "__main__":
    make_batch(questions_batch5, 5, "tools/staging/rom_com_batch5.json")
