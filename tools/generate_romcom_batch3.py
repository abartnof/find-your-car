#!/usr/bin/env python3
"""
Generate Batch 3 for Romantic Comedies:
100 Metatextual questions (Directors, Screenwriters, Box Office Records, Oscar Wins & Nominations, Golden Globes).
Difficulty: 30 d1, 40 d2, 30 d3.
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))
from rom_com_builder import make_batch

questions_batch3 = [
    # 1 - d1
    (
        "Who wrote the acclaimed, Oscar-nominated screenplay for the 1989 classic 'When Harry Met Sally...'?",
        "Nora Ephron",
        ["Nancy Meyers", "Amy Heckerling", "Carrie Fisher"],
        1
    ),
    # 2 - d1
    (
        "Which romantic comedy filmmaker directed both 'The Holiday' (2006) and 'Something's Gotta Give' (2003)?",
        "Nancy Meyers",
        ["Nora Ephron", "Amy Heckerling", "Penny Marshall"],
        1
    ),
    # 3 - d1
    (
        "Which British screenwriter and director wrote 'Four Weddings and a Funeral', 'Notting Hill', and directed 'Love Actually'?",
        "Richard Curtis",
        ["Anthony Minghella", "Danny Boyle", "Stephen Frears"],
        1
    ),
    # 4 - d1
    (
        "Who wrote and directed both 'Say Anything...' (1989) and 'Jerry Maguire' (1996)?",
        "Cameron Crowe",
        ["Rob Reiner", "Lawrence Kasdan", "John Hughes"],
        1
    ),
    # 5 - d1
    (
        "Which classic 1934 screwball comedy made history as the first film to sweep all 'Big Five' Academy Awards (Picture, Director, Actor, Actress, Screenplay)?",
        "It Happened One Night",
        ["The Philadelphia Story", "Bringing Up Baby", "His Girl Friday"],
        1
    ),
    # 6 - d1
    (
        "Which 1977 romantic comedy won four Academy Awards, including Best Picture, Best Director, and Best Actress for Diane Keaton?",
        "Annie Hall",
        ["Manhattan", "Hannah and Her Sisters", "The Goodbye Girl"],
        1
    ),
    # 7 - d1
    (
        "Cher won the Academy Award for Best Actress for her performance as Loretta Castorini in which 1987 romantic comedy?",
        "Moonstruck",
        ["The Witches of Eastwick", "Mermaids", "Silkwood"],
        1
    ),
    # 8 - d1
    (
        "Who directed the 1990 blockbuster romantic comedy 'Pretty Woman'?",
        "Garry Marshall",
        ["Rob Reiner", "Blake Edwards", "Ron Howard"],
        1
    ),
    # 9 - d1
    (
        "Which 1993 romantic comedy marked Nora Ephron's breakthrough second feature film as director, pairing Tom Hanks and Meg Ryan?",
        "Sleepless in Seattle",
        ["You've Got Mail", "Mixed Nuts", "Michael"],
        1
    ),
    # 10 - d1
    (
        "Who directed the 1995 cult classic teen comedy 'Clueless'?",
        "Amy Heckerling",
        ["Tamra Davis", "Sofia Coppola", "Catherine Hardwicke"],
        1
    ),
    # 11 - d1
    (
        "For which 1996 romantic comedy-drama did Cuba Gooding Jr. win the Academy Award for Best Supporting Actor after shouting 'Show me the money!'?",
        "Jerry Maguire",
        ["As Good as It Gets", "Jerry's World", "Boyz n the Hood"],
        1
    ),
    # 12 - d1
    (
        "Which 1997 romantic comedy achieved the rare feat of winning both Best Actor (Jack Nicholson) and Best Actress (Helen Hunt) at the Oscars?",
        "As Good as It Gets",
        ["Jerry Maguire", "My Best Friend's Wedding", "Shakespeare in Love"],
        1
    ),
    # 13 - d1
    (
        "Which 1998 romantic comedy won seven Academy Awards, including Best Picture and Best Actress for Gwyneth Paltrow?",
        "Shakespeare in Love",
        ["Life is Beautiful", "Elizabeth", "Saving Private Ryan"],
        1
    ),
    # 14 - d1
    (
        "Which 2002 independent romantic comedy became a historic sleeper hit, grossing over $241 million in North America without ever hitting #1 at the weekend box office?",
        "My Big Fat Greek Wedding",
        ["Bend It Like Beckham", "Amélie", "Mamma Mia!"],
        1
    ),
    # 15 - d1
    (
        "Who wrote and starred in the sleeper hit 'My Big Fat Greek Wedding', earning an Oscar nomination for Best Original Screenplay?",
        "Nia Vardalos",
        ["Tina Fey", "Andrea Martin", "Amy Poehler"],
        1
    ),
    # 16 - d1
    (
        "Which influential comedy filmmaker directed 'Knocked Up' and 'The 40-Year-Old Virgin' while producing hits like 'Bridesmaids'?",
        "Judd Apatow",
        ["Adam McKay", "Todd Phillips", "Jay Roach"],
        1
    ),
    # 17 - d1
    (
        "Who directed the 2018 smash hit 'Crazy Rich Asians', which became the highest-grossing romantic comedy of the 2010s?",
        "Jon M. Chu",
        ["Ang Lee", "Justin Lin", "James Wan"],
        1
    ),
    # 18 - d1
    (
        "Who directed the 1987 romantic fantasy adventure 'The Princess Bride'?",
        "Rob Reiner",
        ["Terry Gilliam", "Ron Howard", "Richard Donner"],
        1
    ),
    # 19 - d1
    (
        "Which actress won an Academy Award for Best Actress for her breakout American film role in 'Roman Holiday' (1953)?",
        "Audrey Hepburn",
        ["Grace Kelly", "Elizabeth Taylor", "Deborah Kerr"],
        1
    ),
    # 20 - d1
    (
        "Which 2011 comedy directed by Paul Feig earned Oscar nominations for both Best Original Screenplay and Best Supporting Actress for Melissa McCarthy?",
        "Bridesmaids",
        ["The Heat", "Spy", "Bad Teacher"],
        1
    ),
    # 21 - d1
    (
        "Who directed the 1998 romantic comedy 'You've Got Mail', re-teaming Meg Ryan and Tom Hanks?",
        "Nora Ephron",
        ["Nancy Meyers", "Penny Marshall", "Garry Marshall"],
        1
    ),
    # 22 - d1
    (
        "Which 1960 Billy Wilder romantic comedy-drama won 5 Academy Awards, including Best Picture, Best Director, and Best Original Screenplay?",
        "The Apartment",
        ["Some Like It Hot", "Sabrina", "Irma la Douce"],
        1
    ),
    # 23 - d1
    (
        "Which real-life husband-and-wife writing team received an Academy Award nomination for Best Original Screenplay for 'The Big Sick' (2017)?",
        "Kumail Nanjiani and Emily V. Gordon",
        ["Zoe Kazan and Paul Dano", "John Krasinski and Emily Blunt", "Noah Baumbach and Greta Gerwig"],
        1
    ),
    # 24 - d1
    (
        "Which 2008 musical romantic comedy grossed over $611 million worldwide, setting box office records across the UK and Europe?",
        "Mamma Mia!",
        ["Hairspray", "Enchanted", "Across the Universe"],
        1
    ),
    # 25 - d1
    (
        "Who directed the 1989 romantic comedy hit 'When Harry Met Sally...'?",
        "Rob Reiner",
        ["Nora Ephron", "Sydney Pollack", "Barry Levinson"],
        1
    ),
    # 26 - d1
    (
        "Which 1994 British comedy became a massive worldwide box office phenomenon, earning an Academy Award nomination for Best Picture?",
        "Four Weddings and a Funeral",
        ["The Full Monty", "Notting Hill", "Sense and Sensibility"],
        1
    ),
    # 27 - d1
    (
        "Who directed the 2000 fantasy romantic comedy 'What Women Want', which scored what was then the biggest December opening weekend in box office history?",
        "Nancy Meyers",
        ["Nora Ephron", "Betty Thomas", "Garry Marshall"],
        1
    ),
    # 28 - d1
    (
        "Which 2023 romantic comedy starring Sydney Sweeney and Glen Powell became a viral box office sleeper hit, grossing over $200 million worldwide?",
        "Anyone But You",
        ["No Hard Feelings", "The Idea of You", "Ticket to Paradise"],
        1
    ),
    # 29 - d1
    (
        "Who wrote the bestselling novel 'Bridget Jones's Diary', which was adapted into the hit 2001 romantic comedy film?",
        "Helen Fielding",
        ["Sophie Kinsella", "Marian Keyes", "Nick Hornby"],
        1
    ),
    # 30 - d1
    (
        "Which legendary playwright and screenwriter won an Academy Award for Best Original Screenplay for 'Moonstruck'?",
        "John Patrick Shanley",
        ["David Mamet", "Neil Simon", "Tom Stoppard"],
        1
    ),

    # 31 - d2
    (
        "Which iconic Hollywood screenwriter, blacklisted by studios in the 1950s, finally received posthumous credit and an Oscar for writing 'Roman Holiday'?",
        "Dalton Trumbo",
        ["Ring Lardner Jr.", "Alvah Bessie", "Lester Cole"],
        2
    ),
    # 32 - d2
    (
        "Which film festival premiered 'Palm Springs' in January 2020, leading to a record-setting $17.5 million distribution sale to Neon and Hulu?",
        "Sundance Film Festival",
        ["Toronto International Film Festival", "Telluride Film Festival", "Tribeca Film Festival"],
        2
    ),
    # 33 - d2
    (
        "For which 1940 romantic comedy did James Stewart win the Academy Award for Best Actor as reporter Macaulay Connor?",
        "The Philadelphia Story",
        ["Mr. Smith Goes to Washington", "The Shop Around the Corner", "Destry Rides Again"],
        2
    ),
    # 34 - d2
    (
        "Who directed '10 Things I Hate About You' (1999), launching the Hollywood careers of Heath Ledger and Julia Stiles?",
        "Gil Junger",
        ["Peyton Reed", "Mark Waters", "Peter Segal"],
        2
    ),
    # 35 - d2
    (
        "Which 1988 romantic comedy directed by Mike Nichols received six Academy Award nominations, including Best Picture, Best Director, and Best Actress for Melanie Griffith?",
        "Working Girl",
        ["Moonstruck", "Broadcast News", "Crossing Delancey"],
        2
    ),
    # 36 - d2
    (
        "Who wrote the screenplay for 'The Princess Bride', adapting his own 1973 fantasy novel?",
        "William Goldman",
        ["Michael Crichton", "Peter Benchley", "Neil Gaiman"],
        2
    ),
    # 37 - d2
    (
        "Which British romantic comedy marked Richard Curtis's final project as a feature film director in 2013?",
        "About Time",
        ["The Boat That Rocked", "Love Actually", "Yesterday"],
        2
    ),
    # 38 - d2
    (
        "In addition to 'Pretty Woman', Garry Marshall directed Julia Roberts and Richard Gere in which 1999 romantic comedy reunion?",
        "Runaway Bride",
        ["Valentine's Day", "The Princess Diaries", "Georgia Rule"],
        2
    ),
    # 39 - d2
    (
        "Which 2009 romantic comedy directed by Nancy Meyers starred Meryl Streep, Steve Martin, and Alec Baldwin?",
        "It's Complicated",
        ["Something's Gotta Give", "The Holiday", "Baby Boom"],
        2
    ),
    # 40 - d2
    (
        "Who directed 'Groundhog Day' (1993) and co-wrote the screenplay alongside Danny Rubin?",
        "Harold Ramis",
        ["Ivan Reitman", "John Landis", "Frank Oz"],
        2
    ),
    # 41 - d2
    (
        "Which prestigious award did 'Groundhog Day' win in 1994 for its original screenplay?",
        "BAFTA Award for Best Original Screenplay",
        ["Academy Award for Best Original Screenplay", "Golden Globe for Best Screenplay", "Writers Guild of America Award"],
        2
    ),
    # 42 - d2
    (
        "Which 1997 comedy written by Ronald Bass starred Julia Roberts and Cameron Diaz and grossed almost $300 million worldwide?",
        "My Best Friend's Wedding",
        ["Notting Hill", "Runaway Bride", "There's Something About Mary"],
        2
    ),
    # 43 - d2
    (
        "Who directed the 1999 romantic comedy blockbuster 'Notting Hill'?",
        "Roger Michell",
        ["Richard Curtis", "Mike Newell", "Stephen Frears"],
        2
    ),
    # 44 - d2
    (
        "Who directed the 1994 smash hit 'Four Weddings and a Funeral'?",
        "Mike Newell",
        ["Roger Michell", "Richard Curtis", "Hugh Hudson"],
        2
    ),
    # 45 - d2
    (
        "Which legendary screenwriting brothers directed and wrote the 1998 romantic gross-out comedy 'There's Something About Mary'?",
        "Peter and Bobby Farrelly",
        ["Joel and Ethan Coen", "Mark and Jay Duplass", "Anthony and Joe Russo"],
        2
    ),
    # 46 - d2
    (
        "Which 1987 romantic comedy-drama written and directed by James L. Brooks received seven Oscar nominations, including Best Picture and all three lead roles?",
        "Broadcast News",
        ["Terms of Endearment", "As Good as It Gets", "Say Anything..."],
        2
    ),
    # 47 - d2
    (
        "Who wrote the screenplay for 'Clueless', inventing slang phrases like 'as if' and 'audi' after studying high school linguistics?",
        "Amy Heckerling",
        ["Tina Fey", "Nancy Meyers", "Kay Cannon"],
        2
    ),
    # 48 - d2
    (
        "Which filmmaker directed both 'Easy A' (2010) and 'Friends with Benefits' (2011) before directing 'Anyone But You' (2023)?",
        "Will Gluck",
        ["Paul Feig", "Nicholas Stoller", "Mark Waters"],
        2
    ),
    # 49 - d2
    (
        "Who directed the 2008 romantic comedy 'Forgetting Sarah Marshall'?",
        "Nicholas Stoller",
        ["Judd Apatow", "David Gordon Green", "Greg Mottola"],
        2
    ),
    # 50 - d2
    (
        "Who wrote the screenplay for 'Forgetting Sarah Marshall', drawing from his own agonizing real-life breakups?",
        "Jason Segel",
        ["Paul Rudd", "Jonah Hill", "Seth Rogen"],
        2
    ),
    # 51 - d2
    (
        "Which 2009 romantic comedy-drama directed by Marc Webb made its debut at Sundance and earned two Golden Globe nominations including Best Picture (Comedy)?",
        "(500) Days of Summer",
        ["Nick & Norah's Infinite Playlist", "The Spectacular Now", "Adventureland"],
        2
    ),
    # 52 - d2
    (
        "Who wrote the witty, nonlinear screenplay for '(500) Days of Summer'?",
        "Scott Neustadter and Michael H. Weber",
        ["Jonathan Levine and Will Reiser", "John August and Dan Fogelman", "Paul Downs Colaizzo and Karen Maine"],
        2
    ),
    # 53 - d2
    (
        "Which 2004 romantic comedy drama written and directed by Alice Wu explored a secret lesbian romance within a traditional Chinese-American family in Flushing, Queens?",
        "Saving Face",
        ["The Half of It", "Better Luck Tomorrow", "The Joy Luck Club"],
        2
    ),
    # 54 - d2
    (
        "Who directed the 2023 acclaimed South London romantic comedy 'Rye Lane' in her feature directorial debut?",
        "Raine Allen-Miller",
        ["Emerald Fennell", "Charlotte Regan", "Molly Manning Walker"],
        2
    ),
    # 55 - d2
    (
        "Which 2003 film earned Diane Keaton an Academy Award nomination for Best Actress and a Golden Globe win for Best Actress in a Comedy?",
        "Something's Gotta Give",
        ["The First Wives Club", "The Family Stone", "Because I Said So"],
        2
    ),
    # 56 - d2
    (
        "Which 2012 romantic comedy-drama written and directed by David O. Russell received eight Academy Award nominations, including nods in all four acting categories?",
        "Silver Linings Playbook",
        ["American Hustle", "The Fighter", "Joy"],
        2
    ),
    # 57 - d2
    (
        "Who won the Academy Award for Best Actress at age 22 for her performance in 'Silver Linings Playbook'?",
        "Jennifer Lawrence",
        ["Emma Stone", "Brie Larson", "Anne Hathaway"],
        2
    ),
    # 58 - d2
    (
        "Who directed '13 Going on 30' (2004), starring Jennifer Garner and Mark Ruffalo?",
        "Gary Winick",
        ["Andy Tennant", "Peter Chelsom", "Donald Petrie"],
        2
    ),
    # 59 - d2
    (
        "Who directed the 2003 hit romantic comedy 'How to Lose a Guy in 10 Days'?",
        "Donald Petrie",
        ["Andy Tennant", "Peyton Reed", "Gary Winick"],
        2
    ),
    # 60 - d2
    (
        "Which director helmed the hit Sandra Bullock romantic comedies 'Miss Congeniality' and 'Two Weeks Notice'?",
        "Marc Lawrence (Two Weeks Notice) / Donald Petrie (Miss Congeniality)",
        ["Andy Tennant", "Garry Marshall", "Jon Turteltaub"],
        2
    ),
    # 61 - d2
    (
        "Who wrote the screenplay for the 2001 high-school makeover romantic comedy 'Legally Blonde', adapting Amanda Brown's novel?",
        "Karen McCullah and Kirsten Smith",
        ["Tina Fey", "Amy Heckerling", "Nancy Meyers"],
        2
    ),
    # 62 - d2
    (
        "Who wrote the screenplay for '10 Things I Hate About You', forming a successful writing partnership that also penned 'Legally Blonde'?",
        "Karen McCullah and Kirsten Smith",
        ["Cinco Paul and Ken Daurio", "Glenn Ficarra and John Requa", "Scott Neustadter and Michael H. Weber"],
        2
    ),
    # 63 - d2
    (
        "Which 1998 romantic comedy directed by Nora Ephron was a loose reimagining of Ernst Lubitsch's 1940 classic 'The Shop Around the Corner'?",
        "You've Got Mail",
        ["Sleepless in Seattle", "Mixed Nuts", "Michael"],
        2
    ),
    # 64 - d2
    (
        "Which 2009 romantic comedy starring Sandra Bullock and Ryan Reynolds grossed over $317 million worldwide?",
        "The Proposal",
        ["The Lake House", "All About Steve", "Two Weeks Notice"],
        2
    ),
    # 65 - d2
    (
        "Who directed 'The Proposal' (2009), as well as 'Step Up' and '27 Dresses'?",
        "Anne Fletcher",
        ["Nancy Meyers", "Phyllida Lloyd", "Betty Thomas"],
        2
    ),
    # 66 - d2
    (
        "Which 2008 romantic comedy written by Aline Brosh McKenna starred Katherine Heigl as a perennial bridesmaid?",
        "27 Dresses",
        ["The Ugly Truth", "Life as We Know It", "Killers"],
        2
    ),
    # 67 - d2
    (
        "Who directed the 1999 classic 'She's All That', a high school modernization of George Bernard Shaw's 'Pygmalion'?",
        "Robert Iscove",
        ["Gil Junger", "Mark Waters", "Tamra Davis"],
        2
    ),
    # 68 - d2
    (
        "Who directed the 2001 French whimsical romantic comedy 'Amélie'?",
        "Jean-Pierre Jeunet",
        ["Luc Besson", "François Ozon", "Michel Gondry"],
        2
    ),
    # 69 - d2
    (
        "How many Academy Award nominations did the French romantic comedy 'Amélie' receive in 2002?",
        "Five nominations",
        ["Two nominations", "Seven nominations", "Zero nominations"],
        2
    ),
    # 70 - d2
    (
        "Which 2000 romantic comedy directed by Stephen Frears adapted Nick Hornby's London-set novel and moved its setting to Chicago?",
        "High Fidelity",
        ["About a Boy", "Fever Pitch", "A Long Way Down"],
        2
    ),

    # 71 - d3
    (
        "Which 1977 Neil Simon-penned romantic comedy earned Richard Dreyfuss an Academy Award for Best Actor at age 30, making him then the youngest winner in that category?",
        "The Goodbye Girl",
        ["Barefoot in the Park", "The Sunshine Boys", "Chapter Two"],
        3
    ),
    # 72 - d3
    (
        "Which iconic French New Wave director declared 'The Shop Around the Corner' to be Ernst Lubitsch's masterpiece and 'close to perfection'?",
        "François Truffaut",
        ["Jean-Luc Godard", "Éric Rohmer", "Claude Chabrol"],
        3
    ),
    # 73 - d3
    (
        "For which 1959 gender-bending romantic comedy did Billy Wilder and I.A.L. Diamond receive an Oscar nomination for Best Adapted Screenplay?",
        "Some Like It Hot",
        ["The Apartment", "Sabrina", "Love in the Afternoon"],
        3
    ),
    # 74 - d3
    (
        "Which 1940 screwball classic directed by Howard Hawks was an adaptation of the Ben Hecht and Charles MacArthur stage play 'The Front Page'?",
        "His Girl Friday",
        ["Twentieth Century", "Ball of Fire", "Bringing Up Baby"],
        3
    ),
    # 75 - d3
    (
        "Which 1941 screwball masterpiece written and directed by Preston Sturges starred Barbara Stanwyck as con artist Jean Harrington opposite Henry Fonda?",
        "The Lady Eve",
        ["The Palm Beach Story", "Sullivan's Travels", "The Miracle of Morgan's Creek"],
        3
    ),
    # 76 - d3
    (
        "Which 1936 screwball comedy starring William Powell and Carole Lombard was the first film to receive Oscar nominations in all four acting categories?",
        "My Man Godfrey",
        ["The Thin Man", "Libeled Lady", "Nothing Sacred"],
        3
    ),
    # 77 - d3
    (
        "Who wrote the acclaimed screenplay for 'Broadcast News' (1987), earning an Academy Award nomination for Best Original Screenplay?",
        "James L. Brooks",
        ["Nora Ephron", "Barry Levinson", "Cameron Crowe"],
        3
    ),
    # 78 - d3
    (
        "In what year did the Writers Guild of America (WGA) rank the screenplay of 'Annie Hall' as the funniest screenplay in cinema history?",
        "2015",
        ["2005", "1999", "2021"],
        3
    ),
    # 79 - d3
    (
        "Which legendary screenwriting duo penned the 1949 Katharine Hepburn and Spencer Tracy battle-of-the-sexes classic 'Adam's Rib'?",
        "Ruth Gordon and Garson Kanin",
        ["Charles Brackett and Billy Wilder", "Ben Hecht and Charles MacArthur", "Frances Marion and George O'Neil"],
        3
    ),
    # 80 - d3
    (
        "For which 1986 film did Nora Ephron adapt her own semi-autobiographical roman à clef about her marriage to journalist Carl Bernstein?",
        "Heartburn",
        ["Silkwood", "When Harry Met Sally...", "Mixed Nuts"],
        3
    ),
    # 81 - d3
    (
        "Which 1995 romantic comedy directed by Jon Turteltaub became a major box office hit grossing over $182 million on a modest $17 million budget?",
        "While You Were Sleeping",
        ["French Kiss", "Nine Months", "Sabrina"],
        3
    ),
    # 82 - d3
    (
        "Who wrote the screenplay for the 1995 hit 'While You Were Sleeping'?",
        "Daniel G. Sullivan and Fredric LeBow",
        ["Richard Curtis", "Ronald Bass", "Steven Zaillian"],
        3
    ),
    # 83 - d3
    (
        "Who composed the lush, beloved romantic orchestral score for the 1993 film 'Sleepless in Seattle'?",
        "Marc Shaiman",
        ["Thomas Newman", "James Horner", "Alan Silvestri"],
        3
    ),
    # 84 - d3
    (
        "Who composed the romantic soundtrack and score for 'When Harry Met Sally...', arranging vintage standards performed by Harry Connick Jr.?",
        "Marc Shaiman",
        ["Marvin Hamlisch", "Dave Grusin", "Randy Newman"],
        3
    ),
    # 85 - d3
    (
        "Which composer scored Nancy Meyers's films 'The Holiday' and 'Something's Gotta Give'?",
        "Hans Zimmer",
        ["John Williams", "Alexandre Desplat", "James Newton Howard"],
        3
    ),
    # 86 - d3
    (
        "Which acclaimed composer wrote the whimsical, accordion-driven score for the 2001 film 'Amélie'?",
        "Yann Tiersen",
        ["Alexandre Desplat", "Gabriel Yared", "Ludovico Einaudi"],
        3
    ),
    # 87 - d3
    (
        "Which 2011 Woody Allen romantic fantasy comedy grossed over $151 million worldwide, becoming his highest-grossing film of all time?",
        "Midnight in Paris",
        ["Vicky Cristina Barcelona", "Blue Jasmine", "Match Point"],
        3
    ),
    # 88 - d3
    (
        "For which film did Woody Allen win the Academy Award for Best Original Screenplay in 2012?",
        "Midnight in Paris",
        ["Blue Jasmine", "Vicky Cristina Barcelona", "To Rome with Love"],
        3
    ),
    # 89 - d3
    (
        "Which prestigious film festival awarded 'Rye Lane' rave reviews at its worldwide premiere in January 2023?",
        "Sundance Film Festival",
        ["Venice Film Festival", "Cannes Film Festival", "SXSW Film Festival"],
        3
    ),
    # 90 - d3
    (
        "Who directed the 2018 Netflix romantic comedy 'Set It Up', which revitalized modern enthusiasm for studio-style rom-coms?",
        "Claire Scanlon",
        ["Susan Johnson", "Alice Wu", "Nahnatchka Khan"],
        3
    ),
    # 91 - d3
    (
        "Who directed the 2019 Netflix hit romantic comedy 'Always Be My Maybe'?",
        "Nahnatchka Khan",
        ["Alice Wu", "Lynn Shelton", "Cathy Yan"],
        3
    ),
    # 92 - d3
    (
        "Which writer wrote the screenplay for the 2018 romantic comedy 'Set It Up' after it was featured on the 2015 Black List of best unproduced scripts?",
        "Katie Silberman",
        ["Dana Fox", "Kay Cannon", "Aline Brosh McKenna"],
        3
    ),
    # 93 - d3
    (
        "Which 2020 romantic comedy-mystery directed by Max Barbakow was based on a story concept developed by screenwriter Andy Siara at the AFI Conservatory?",
        "Palm Springs",
        ["The Map of Tiny Perfect Things", "Long Shot", "Set It Up"],
        3
    ),
    # 94 - d3
    (
        "Which 2022 LGBTQ+ romantic comedy directed by Nicholas Stoller and co-written by Billy Eichner made history as one of the first gay rom-coms produced by a major studio (Universal)?",
        "Bros",
        ["Fire Island", "Happiest Season", "Red, White & Royal Blue"],
        3
    ),
    # 95 - d3
    (
        "Who directed the 2022 Searchlight Pictures romantic comedy 'Fire Island', which reimagined Jane Austen's 'Pride and Prejudice'?",
        "Andrew Ahn",
        ["Alice Wu", "Bowen Yang", "Joel Kim Booster"],
        3
    ),
    # 96 - d3
    (
        "Who wrote the screenplay and starred in the 2022 Hulu romantic comedy 'Fire Island'?",
        "Joel Kim Booster",
        ["Bowen Yang", "Conrad Ricamora", "Matt Rogers"],
        3
    ),
    # 97 - d3
    (
        "What was the worldwide box office haul of the 1990 romantic comedy 'Pretty Woman', cementing Julia Roberts as a global box office superstar?",
        "$463 million",
        ["$180 million", "$290 million", "$620 million"],
        3
    ),
    # 98 - d3
    (
        "What was the original dramatic script title of 'Pretty Woman' before Garry Marshall reworked it into a romantic comedy fairy tale?",
        "3,000",
        ["Walk of Fame", "Boulevard Angel", "Rodeo Dreams"],
        3
    ),
    # 99 - d3
    (
        "Which screenwriter wrote the original gritty drama script '$3,000' that was later rewritten and transformed into 'Pretty Woman'?",
        "J.F. Lawton",
        ["Robert Towne", "Steven Zaillian", "Bo Goldman"],
        3
    ),
    # 100 - d3
    (
        "Which classic romantic comedy directed by Frank Capra won Best Picture at the 1934 Academy Awards, saving Columbia Pictures from financial insolvency?",
        "It Happened One Night",
        ["Mr. Deeds Goes to Town", "You Can't Take It with You", "Lady for a Day"],
        3
    ),
]

if __name__ == "__main__":
    make_batch(questions_batch3, 3, "tools/staging/rom_com_batch3.json")
