#!/usr/bin/env python3
"""
Generate Batch 6: Quirky, High-Concept, Sci-Fi & Workplace Comedies (100 questions)
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from sitcom_builder import make_batch

q_batch6 = [
    # The Nanny (25 questions)
    {
        "q": "What neighborhood in Queens was Fran Fine from before becoming a nanny on Manhattan's Upper East Side?",
        "correct": "Flushing",
        "distractors": ["Astoria", "Bayside", "Forest Hills"],
        "d": 1
    },
    {
        "q": "What was the theatrical profession of British widower Maxwell Sheffield on The Nanny?",
        "correct": "Broadway theatrical producer",
        "distractors": ["Symphony orchestra conductor", "Shakespearean stage actor", "Art gallery curator"],
        "d": 1
    },
    {
        "q": "What was the name of the sharp-witted, dry English butler played by Daniel Davis on The Nanny?",
        "correct": "Niles",
        "distractors": ["Arthur", "Geoffrey", "Wiggins"],
        "d": 1
    },
    {
        "q": "What was the full name of Maxwell's haughty, socialite business partner who constantly competed with Fran for Maxwell's affection?",
        "correct": "Chastity Claire 'C.C.' Babcock",
        "distractors": ["Constance Camille Babcock", "Cordelia Christine Babcock", "Catherine Clarissa Babcock"],
        "d": 2
    },
    {
        "q": "What romantic twist involving Niles the butler occurs in the final season of The Nanny?",
        "correct": "Niles and his long-time insult sparring partner C.C. Babcock fall in love and marry",
        "distractors": ["Niles inherits a British earldom and moves to London alone", "Niles proposes to Fran's best friend Val", "Niles discovers he is Maxwell Sheffield's half-brother"],
        "d": 2
    },
    {
        "q": "Who portrayed Fran Fine's food-obsessed, polyester-wearing mother Sylvia Fine?",
        "correct": "Renée Taylor",
        "distractors": ["Ann Morgan Guilbert", "Lainie Kazan", "Doris Roberts"],
        "d": 1
    },
    {
        "q": "What was the name of Fran's senile, chain-smoking, silver-haired maternal grandmother?",
        "correct": "Yetta Rosenberg",
        "distractors": ["Ida Morgenstern", "Estelle Blundetto", "Bella Fine"],
        "d": 1
    },
    {
        "q": "What was the name of Fran Fine's dim-witted best friend from Queens played by Rachel Chagall?",
        "correct": "Val Toriello",
        "distractors": ["Nadine Cooper", "Bobbi Flekman", "Lizzie Miller"],
        "d": 1
    },
    {
        "q": "Which dog breed and name was C.C. Babcock's pampered pet, who ironically despised C.C. and loved Fran?",
        "correct": "A Pomeranian named Chester",
        "distractors": ["A Poodle named Pierre", "A Maltese named Prince", "A Shih Tzu named Winston"],
        "d": 2
    },
    {
        "q": "What real-life connection did Chester the dog have to star Fran Drescher?",
        "correct": "Chester was Fran Drescher's actual real-life pet dog",
        "distractors": ["Chester was adopted from an animal shelter during the pilot shoot", "Chester belonged to executive producer Peter Marc Jacobson", "Chester was trained by the same handler as Eddie from Frasier"],
        "d": 2
    },
    {
        "q": "What famous mega-musical did Maxwell Sheffield notoriously turn down producing, only for it to become a global phenomenon?",
        "correct": "Cats",
        "distractors": ["The Phantom of the Opera", "Les Misérables", "The Lion King"],
        "d": 1
    },
    {
        "q": "Who was Maxwell Sheffield's arch-rival in the Broadway theatrical producing world?",
        "correct": "Andrew Lloyd Webber",
        "distractors": ["Cameron Mackintosh", "Hal Prince", "David Merrick"],
        "d": 2
    },
    {
        "q": "How was Fran's father Morty Fine treated for the first five seasons of The Nanny?",
        "correct": "He was an unseen character hidden behind newspapers or off-screen until Season 6",
        "distractors": ["He was deceased, communicating through Yetta's spiritual séances", "He was serving a long sentence for tax fraud in federal prison", "He lived in Florida and only sent cassette audio tapes"],
        "d": 2
    },
    {
        "q": "Which legendary singer portrayed Fran's father Morty Fine when he was finally revealed on screen in Season 6?",
        "correct": "Steve Lawrence",
        "distractors": ["Neil Sedaka", "Paul Anka", "Jerry Vale"],
        "d": 3
    },
    {
        "q": "Who wrote and performed the memorable animated opening theme song 'The Nanny Named Fran'?",
        "correct": "Ann Hampton Callaway",
        "distractors": ["Cyndi Lauper", "Bette Midler", "Liza Minnelli"],
        "d": 2
    },
    {
        "q": "Why was Fran Fine visiting the Sheffield residence in the pilot episode when she was hired as nanny?",
        "correct": "She was selling Shade Shades cosmetics door-to-door after being fired from a bridal shop",
        "distractors": ["She was delivering dry-cleaned theatrical costumes from Queens", "She was catering a cocktail party for Broadway investors", "She was auditioning for a minor chorus role in Maxwell's musical"],
        "d": 1
    },
    {
        "q": "What was the name of Fran's ex-fiancé who dumped her and fired her from the bridal shop in the pilot?",
        "correct": "Danny Imperiali",
        "distractors": ["Tony DeMarco", "Sal Manetti", "Vinny Delgato"],
        "d": 2
    },
    {
        "q": "What were the names of the three Sheffield children raised by Fran Fine?",
        "correct": "Maggie, Brighton, and Grace",
        "distractors": ["Chloe, Julian, and Penelope", "Sarah, Colin, and Lily", "Emma, Oliver, and Beatrice"],
        "d": 1
    },
    {
        "q": "Which costume designer won an Emmy Award for curating Fran Fine's iconic high-fashion Moschino and Dolce & Gabbana wardrobe?",
        "correct": "Brenda Cooper",
        "distractors": ["Patricia Field", "Bob Mackie", "Edith Head"],
        "d": 3
    },
    {
        "q": "In the series finale, what milestone happens as Fran and Maxwell prepare to move to California?",
        "correct": "Fran gives birth to fraternal twins, Jonah and Eve",
        "distractors": ["Fran wins a Tony Award for producing her own Broadway comedy", "Maxwell sells his production firm to Disney for $50 million", "Yetta runs off to Europe with her new husband"],
        "d": 2
    },
    {
        "q": "What country did Daniel Davis (Niles) actually hail from in real life, despite his flawless aristocratic British accent?",
        "correct": "The United States (born in Little Rock, Arkansas)",
        "distractors": ["Canada (born in Toronto, Ontario)", "Australia (born in Sydney)", "New Zealand (born in Wellington)"],
        "d": 2
    },
    {
        "q": "What was the name of Yetta's wealthy nursing-home boyfriend played by Ray Charles in guest appearances?",
        "correct": "Sammy",
        "distractors": ["Arthur", "Lou", "Benny"],
        "d": 2
    },
    {
        "q": "In Season 4's Paris episode, what does Maxwell Sheffield impulsively confess to Fran when their plane hits turbulence?",
        "correct": "He confesses that he is in love with her, only to retract it once they land",
        "distractors": ["He reveals that he lost his entire theatrical fortune in the stock market", "He admits he was responsible for getting her bridal shop closed down", "He proposes marriage on the spot with a champagne cork"],
        "d": 2
    },
    {
        "q": "What musical instrument did youngest daughter Gracie Sheffield play during family musical evenings?",
        "correct": "Violin / Fiddle",
        "distractors": ["Flute", "Cello", "Harp"],
        "d": 3
    },
    {
        "q": "What was the title of Fran Drescher's best-selling 1996 autobiography recounting her life and rise to television stardom?",
        "correct": "Enter Whining",
        "distractors": ["The Queen of Queens", "Having Mercy", "Big Hair, Big Heart"],
        "d": 2
    },

    # Spin City (15 questions)
    {
        "q": "On Spin City, what high-ranking municipal government post was held by Michael J. Fox's character Mike Flaherty?",
        "correct": "Deputy Mayor of New York City",
        "distractors": ["City Comptroller", "Chief of the Police Department", "Borough President of Manhattan"],
        "d": 1
    },
    {
        "q": "Who portrayed the well-meaning but hopelessly clueless Mayor Randall Winston on Spin City?",
        "correct": "Barry Bostwick",
        "distractors": ["Richard Kind", "Alan Ruck", "Michael Gross"],
        "d": 1
    },
    {
        "q": "What was the role of the neurotic, hyper-anxious Paul Lassiter (Richard Kind) in the Mayor's administration?",
        "correct": "Press Secretary",
        "distractors": ["Chief Financial Officer", "Director of Communications", "Legal Counsel"],
        "d": 1
    },
    {
        "q": "What was the name of the cynical, politically incorrect Head of Sanitation and Chief of Budget played by Alan Ruck?",
        "correct": "Stuart Bondek",
        "distractors": ["James Hobert", "Carter Heywood", "Janelle Cooper"],
        "d": 1
    },
    {
        "q": "What groundbreaking character did Michael Boatman portray on Spin City starting in 1996?",
        "correct": "Carter Heywood, an openly gay, politically sharp Black head of minority affairs",
        "distractors": ["The first openly transgender city commissioner on prime-time TV", "The youngest district attorney in New York City history", "An undercover NYPD internal affairs detective"],
        "d": 2
    },
    {
        "q": "What was the name and peculiar behavior of Carter Heywood's pet dog on Spin City?",
        "correct": "Rags, an elderly dog with apparently suicidal tendencies",
        "distractors": ["Barnaby, a bulldog who only ate gourmet pastrami", "Max, a beagle who barked whenever politicians lied", "Buster, a terrier who attacked reporters' microphones"],
        "d": 2
    },
    {
        "q": "What unexpected living arrangement was formed between the chauvinistic Stuart Bondek and the refined Carter Heywood?",
        "correct": "They became roommates sharing an upscale Manhattan apartment",
        "distractors": ["They bought a weekend cabin together in the Adirondacks", "They co-owned a failing sports pub in Brooklyn", "They entered an arranged business partnership selling real estate"],
        "d": 2
    },
    {
        "q": "Why did Michael J. Fox announce his departure from Spin City at the conclusion of Season 4?",
        "correct": "To focus on managing his symptoms of Parkinson's disease and establish his research foundation",
        "distractors": ["To direct major Hollywood feature films full-time", "Due to creative disputes with co-creator Bill Lawrence", "To return to Canada to run for parliamentary office"],
        "d": 1
    },
    {
        "q": "Which actor joined Spin City in Season 5 to lead the mayoral office as new Deputy Mayor Charlie Crawford?",
        "correct": "Charlie Sheen",
        "distractors": ["Rob Lowe", "Emilio Estevez", "Alec Baldwin"],
        "d": 1
    },
    {
        "q": "Which acclaimed television creator co-created Spin City before going on to create Scrubs and Ted Lasso?",
        "correct": "Bill Lawrence",
        "distractors": ["Greg Daniels", "Michael Schur", "Steve Levitan"],
        "d": 2
    },
    {
        "q": "In Michael J. Fox's emotional final episode as a series regular ('Goodbye'), how does Mike Flaherty leave City Hall?",
        "correct": "He takes the fall for a mob-connected political scandal to protect Mayor Winston's reputation",
        "distractors": ["He is appointed United States Ambassador to France", "He resigns to marry his journalist girlfriend in London", "He is elected Mayor of his hometown in Connecticut"],
        "d": 2
    },
    {
        "q": "Which future Friday Night Lights and Nashville star played the Mayor's executive assistant Nikki Faber in early seasons?",
        "correct": "Connie Britton",
        "distractors": ["Carla Gugino", "Jennifer Esposito", "Heather Locklear"],
        "d": 2
    },
    {
        "q": "Which television superstar joined Spin City in Season 4 as campaign manager Caitlin Moore?",
        "correct": "Heather Locklear",
        "distractors": ["Courtney Thorne-Smith", "Laura Leighton", "Marcia Cross"],
        "d": 1
    },
    {
        "q": "What was the name of the shy, naive speechwriter played by Alexander Chaplin who idolized Mike Flaherty?",
        "correct": "James Hobert",
        "distractors": ["Scott Miller", "David Bell", "Tom Wallace"],
        "d": 2
    },
    {
        "q": "How many Golden Globe Awards for Best Actor in a Television Series Musical or Comedy did Michael J. Fox win for Spin City?",
        "correct": "Three",
        "distractors": ["One", "Two", "Four"],
        "d": 2
    },

    # Just Shoot Me! (15 questions)
    {
        "q": "What high-fashion women's magazine provided the workplace setting for NBC's sitcom Just Shoot Me!?",
        "correct": "Blush Magazine",
        "distractors": ["Chic Magazine", "Glamour New York", "Vogue World"],
        "d": 1
    },
    {
        "q": "What was the inciting premise of Just Shoot Me! in the pilot episode?",
        "correct": "Serious feminist journalist Maya Gallo is fired and reluctantly takes a job at her estranged father's fashion magazine",
        "distractors": ["A beauty pageant contestant inherits a major editorial firm from an eccentric uncle", "An undercover reporter infiltrates the modeling industry to expose child labor", "A fashion photographer accidentally publishes scandalous photos of the mayor"],
        "d": 1
    },
    {
        "q": "Who portrayed Maya's vain, eccentric billionaire father and publisher Jack Gallo on Just Shoot Me!?",
        "correct": "George Segal",
        "distractors": ["Rip Torn", "Peter Boyle", "Robert Wagner"],
        "d": 1
    },
    {
        "q": "What was David Spade's role as the scheming, sex-obsessed assistant on Just Shoot Me!?",
        "correct": "Dennis Finch",
        "distractors": ["Elliot DiMauro", "Kevin Hunter", "Donnie Peters"],
        "d": 1
    },
    {
        "q": "Which actress stole scenes as Nina Van Horn, the aging, martini-swilling former 1970s supermodel turned fashion editor?",
        "correct": "Wendie Malick",
        "distractors": ["Christine Baranski", "Jane Leeves", "Joanna Lumley"],
        "d": 1
    },
    {
        "q": "Who played Elliot DiMauro, Blush's suave, womanizing lead photographer and Maya's on-again/off-again boyfriend?",
        "correct": "Enrico Colantoni",
        "distractors": ["Joe Regalbuto", "David Foley", "Mark Valley"],
        "d": 2
    },
    {
        "q": "Who created Just Shoot Me! before later co-creating the landmark comedy series Modern Family?",
        "correct": "Steven Levitan",
        "distractors": ["Christopher Lloyd", "Phil Rosenthal", "Paul Simms"],
        "d": 2
    },
    {
        "q": "What was Nina Van Horn's scandalous real first name, which she kept fiercely hidden from the fashion world?",
        "correct": "Chloe",
        "distractors": ["Gertrude", "Mildred", "Bertha"],
        "d": 3
    },
    {
        "q": "What supermodel guest starred as Dennis Finch's gorgeous, statuesque rock-star wife in Season 4?",
        "correct": "Rebecca Romijn",
        "distractors": ["Cindy Crawford", "Claudia Schiffer", "Heidi Klum"],
        "d": 2
    },
    {
        "q": "What bizarre childhood hobby and collectible obsession did Dennis Finch display in his office?",
        "correct": "Action figures, comic book memorabilia, and rock band trading cards",
        "distractors": ["Porcelain tea sets and vintage tiaras", "Antique medical bone saws", "Taxidermy woodland squirrels"],
        "d": 2
    },
    {
        "q": "What was Jack Gallo's favorite competitive rivalry throughout the run of Just Shoot Me!?",
        "correct": "His bitter personal and business rivalry with real estate mogul Donald Trump",
        "distractors": ["His ongoing squash matches against Hugh Hefner", "His circulation war against Rupert Murdoch", "His sailing regatta races against Ted Turner"],
        "d": 2
    },
    {
        "q": "What catchphrase and physical celebration did Dennis Finch frequently perform after scoring a victory?",
        "correct": "Snapping his fingers and yelling 'Chicken and a biscuit!'",
        "distractors": ["Dropping to one knee and shouting 'Boom goes the dynamite!'", "Spinning around and yelling 'Bingo baby!'", "Slapping his forehead and shouting 'Ka-ching!'"],
        "d": 2
    },
    {
        "q": "What prestigious television block did Just Shoot Me! anchor for NBC during its ratings peak in the late 1990s?",
        "correct": "Thursday 'Must See TV' (following Friends or Frasier)",
        "distractors": ["Tuesday night comedy block", "Wednesday 'Must Laugh' hour", "Sunday family night"],
        "d": 1
    },
    {
        "q": "In Season 5, what major milestone occurs between Maya Gallo and photographer Elliot DiMauro?",
        "correct": "They get engaged after an extended romance, though they later break up",
        "distractors": ["They buy a competing fashion magazine together", "They elope to Las Vegas on a drunken dare", "They have a child out of wedlock"],
        "d": 2
    },
    {
        "q": "What secret addiction from her 1970s runway modeling heyday did Nina Van Horn constantly battle?",
        "correct": "Cocktails, diet pills, and partying with rock stars",
        "distractors": ["High-stakes underground poker", "Compulsive shoplifting of cashmere scarves", "Gambling on thoroughbred horse racing"],
        "d": 1
    },

    # The Larry Sanders Show (15 questions)
    {
        "q": "What premium cable network broadcast the revolutionary showbiz satire The Larry Sanders Show from 1992 to 1998?",
        "correct": "HBO",
        "distractors": ["Showtime", "Cinemax", "The Movie Channel"],
        "d": 1
    },
    {
        "q": "Who was the star, co-creator, and creative mastermind behind The Larry Sanders Show?",
        "correct": "Garry Shandling",
        "distractors": ["Larry David", "Albert Brooks", "Richard Lewis"],
        "d": 1
    },
    {
        "q": "Who portrayed Artie, Larry's fiercely loyal, hard-drinking veteran executive producer, winning an Emmy in 1996?",
        "correct": "Rip Torn",
        "distractors": ["Jeffrey Tambor", "Wallace Langham", "Bob Odenkirk"],
        "d": 1
    },
    {
        "q": "What was the iconic on-air catchphrase of Larry's insecure, sycophantic sidekick Hank Kingsley (Jeffrey Tambor)?",
        "correct": "Hey now!",
        "distractors": ["Here we go!", "That's what I'm talkin' about!", "Right on time!"],
        "d": 1
    },
    {
        "q": "What aesthetic convention pioneered by The Larry Sanders Show became standard for modern prestige television comedy?",
        "correct": "Shooting behind-the-scenes drama on cinematic film with no laugh track, contrasting with video cameras on the talk show set",
        "distractors": ["Having characters speak directly to hidden cameras documentary-style", "Using split-screen phone calls across multiple time zones", "Filming entire seasons chronologically without a live audience"],
        "d": 2
    },
    {
        "q": "Which celebrated comedian and actress played Paula, the tough, cynical talent booker for Larry Sanders?",
        "correct": "Janeane Garofalo",
        "distractors": ["Sarah Silverman", "Kathy Griffin", "Mary Lynn Rajskub"],
        "d": 2
    },
    {
        "q": "Which X-Files star famously played a version of himself who harbored an intense romantic crush on Larry Sanders?",
        "correct": "David Duchovny",
        "distractors": ["Gillian Anderson", "Mitch Pileggi", "Robert Patrick"],
        "d": 2
    },
    {
        "q": "What ill-fated restaurant franchise did Hank Kingsley foolishly invest his life savings into opening?",
        "correct": "Hank's Look-Around Cafe",
        "distractors": ["Hank's Hey Now Burgers", "Kingsley's Comedy Rib Shack", "The Sidekick Grill"],
        "d": 2
    },
    {
        "q": "Which future Breaking Bad and Better Call Saul star played Larry's ambitious, fast-talking young agent Stevie Grant?",
        "correct": "Bob Odenkirk",
        "distractors": ["Bryan Cranston", "David Cross", "Paul Feig"],
        "d": 1
    },
    {
        "q": "What superstar comedian performed an intense, emotional musical rendition of 'And I Am Telling You I'm Not Going' to Larry in the series finale?",
        "correct": "Jim Carrey",
        "distractors": ["Robin Williams", "Eddie Murphy", "Steve Martin"],
        "d": 2
    },
    {
        "q": "What was the name of Larry Sanders' sweet, endlessly patient personal assistant played by Penny Johnson Jerald?",
        "correct": "Beverly",
        "distractors": ["Darlene", "Francine", "Melanie"],
        "d": 2
    },
    {
        "q": "What favorite alcoholic cocktail did producer Artie constantly mix and sip in his office during crises?",
        "correct": "Salty Dog (vodka and grapefruit juice in a salt-rimmed glass)",
        "distractors": ["Dry Gin Martini", "Old Fashioned", "Bourbon and Branch Water"],
        "d": 3
    },
    {
        "q": "In the series finale 'Flip', who was originally slated to replace Larry Sanders as host before turning it down?",
        "correct": "Jon Stewart",
        "distractors": ["Conan O'Brien", "Bill Maher", "Greg Kinnear"],
        "d": 2
    },
    {
        "q": "How many Primetime Emmy Award nominations did The Larry Sanders Show receive over its six-season run?",
        "correct": "56 nominations",
        "distractors": ["28 nominations", "84 nominations", "112 nominations"],
        "d": 3
    },
    {
        "q": "What phrase did Larry Sanders whisper into the ear of each guest during the final commercial break of his show?",
        "correct": "You were great. I love you.",
        "distractors": ["Thanks for coming. Cash your check.", "Keep it real out there.", "See you at the Ivy."],
        "d": 2
    },

    # Herman's Head (10 questions)
    {
        "q": "What was the unique central concept of the Fox comedy Herman's Head (1991-1994)?",
        "correct": "Four distinct actors portrayed the warring psychological emotions inside a young man's brain",
        "distractors": ["A man with amnesia believes he is four different historical figures", "A brain surgeon can hear the private thoughts of his patients", "A ghost inhabits the mind of an advertising executive"],
        "d": 1
    },
    {
        "q": "What was the name of the four interior psychological characters battling inside Herman Brooks' mind?",
        "correct": "Angel, Animal, Genius, and Wimp",
        "distractors": ["Joy, Sadness, Anger, and Fear", "Ego, Superego, Id, and Libido", "Logic, Passion, Caution, and Courage"],
        "d": 1
    },
    {
        "q": "Which actor portrayed Animal, the slobbering personification of Herman's base lust, hunger, and primal urges?",
        "correct": "Ken Hudson Campbell",
        "distractors": ["Peter Mackenzie", "Rick Lawless", "William Ragsdale"],
        "d": 2
    },
    {
        "q": "Which voice actress, famous for voicing Lisa Simpson on The Simpsons, co-starred on Herman's Head as his co-worker Louise Davis?",
        "correct": "Yeardley Smith",
        "distractors": ["Nancy Cartwright", "Julie Kavner", "Pamela Adlon"],
        "d": 1
    },
    {
        "q": "What was Herman Brooks' (William Ragsdale) real-world day job in Manhattan?",
        "correct": "Fact-checker for Waterville Publishing",
        "distractors": ["Copy editor for The New York Post", "Archivist for the New York Public Library", "Speechwriter for the City Council"],
        "d": 2
    },
    {
        "q": "What animated Pixar blockbuster film is widely considered by critics to share its fundamental DNA with Herman's Head?",
        "correct": "Inside Out",
        "distractors": ["Soul", "Monsters, Inc.", "Toy Story"],
        "d": 1
    },
    {
        "q": "Which actress portrayed Angel, the personification of Herman's sensitivity, morality, and romantic ideals?",
        "correct": "Molly Hagan",
        "distractors": ["Jane Sibbett", "Yeardley Smith", "Wendie Malick"],
        "d": 2
    },
    {
        "q": "What was the character Genius primarily concerned with inside Herman's mind?",
        "correct": "Logic, intellectual analysis, and long-term planning",
        "distractors": ["Artistic creativity and poetry", "Financial accounting and investments", "Scientific inventions and trivia"],
        "d": 2
    },
    {
        "q": "Who was Herman's arrogant, social-climbing co-worker and chief rival at Waterville Publishing?",
        "correct": "Jay Nichols (Hank Azaria)",
        "distractors": ["Heddy Newman (Jane Sibbett)", "Mr. Bracken (Jason Bernard)", "Paul (Grant Shaud)"],
        "d": 2
    },
    {
        "q": "What network aired Herman's Head as part of its edgy Sunday night comedy block alongside The Simpsons and Married... with Children?",
        "correct": "FOX",
        "distractors": ["NBC", "ABC", "The WB"],
        "d": 1
    },

    # Dharma & Greg (15 questions)
    {
        "q": "What was the fundamental premise of Chuck Lorre's hit romantic comedy Dharma & Greg?",
        "correct": "A free-spirited bohemian yoga instructor and a buttoned-up conservative federal prosecutor marry on their very first date",
        "distractors": ["An environmental activist is assigned to community service at a Wall Street brokerage firm", "A San Francisco detective investigates an eccentric hippie commune and falls for its leader", "Two rival divorce attorneys inherit a bed and breakfast in Napa Valley"],
        "d": 1
    },
    {
        "q": "Which actress won a Golden Globe Award for her portrayal of the joyful, eccentric Dharma Finkelstein?",
        "correct": "Jenna Elfman",
        "distractors": ["Courtney Thorne-Smith", "Calista Flockhart", "Tea Leoni"],
        "d": 1
    },
    {
        "q": "Which actor, later famous as Aaron Hotchner on Criminal Minds, played strait-laced attorney Greg Montgomery?",
        "correct": "Thomas Gibson",
        "distractors": ["Peter Krause", "David Boreanaz", "Craig Bierko"],
        "d": 1
    },
    {
        "q": "What California city provided the setting for the cultural clash between the Finkelsteins and the Montgomerys?",
        "correct": "San Francisco",
        "distractors": ["Los Angeles", "San Diego", "Santa Cruz"],
        "d": 1
    },
    {
        "q": "What was the background and lifestyle of Dharma's counter-culture parents, Larry and Abby (Alan Rachins and Mimi Kennedy)?",
        "correct": "Aging 1960s hippies who lived off the grid and rejected conventional social institutions",
        "distractors": ["Wealthy Hollywood movie producers who practiced transcendental meditation", "Marxist college professors who ran a communal organic vineyard", "New Age guru authors who led spiritual retreats in Big Sur"],
        "d": 1
    },
    {
        "q": "What social class and demeanor defined Greg's blue-blood parents, Edward and Kitty Montgomery (Mitchell Ryan and Susan Sullivan)?",
        "correct": "High-society country-club snobs who consumed copious cocktails and obsessed over family lineage",
        "distractors": ["Self-made Texas oil tycoons who wore cowboy hats and boots", "Devout Boston Catholic philanthropists who funded private universities", "Strict military admirals who treated dinner like boot camp"],
        "d": 1
    },
    {
        "q": "What famous television tradition did producer Chuck Lorre establish at the end of each episode of Dharma & Greg?",
        "correct": "His personalized, micro-second 'Vanity Cards' featuring essays and personal reflections",
        "distractors": ["Outtakes of the cast breaking into laughter during rehearsals", "Viewer mail read aloud by the studio announcer", "Donation links for San Francisco homeless shelters"],
        "d": 1
    },
    {
        "q": "What was the name of Greg Montgomery's smarmy, freeloading lawyer buddy played by Joel Murray?",
        "correct": "Pete Cavanaugh",
        "distractors": ["Steve Carey", "Bob Higgins", "Gary Miller"],
        "d": 2
    },
    {
        "q": "What was the name of Dharma's bizarre, deadpan friend who lived in a loft and hated humanity?",
        "correct": "Jane (Shae D'Lyn)",
        "distractors": ["Chloe", "Rain", "Meadow"],
        "d": 2
    },
    {
        "q": "What federal government position did Greg Montgomery hold during the first three seasons?",
        "correct": "Assistant United States Attorney",
        "distractors": ["Public Defender", "Securities and Exchange Commission investigator", "Federal Appeals Court Clerk"],
        "d": 2
    },
    {
        "q": "What unusual living space did Dharma and Greg share in San Francisco?",
        "correct": "A converted industrial loft with a spiral staircase and eccentric furniture",
        "distractors": ["A classic Victorian Painted Lady rowhouse", "A houseboat moored in Sausalito", "A converted firehouse with a working pole"],
        "d": 2
    },
    {
        "q": "What was the profession and personal practice of Dharma Finkelstein Montgomery?",
        "correct": "Yoga instructor and dog trainer",
        "distractors": ["Acupuncturist and herbalist", "Ceramic pottery maker and sculptor", "Freelance astrology columnist"],
        "d": 1
    },
    {
        "q": "In the Season 4 finale, what traumatic event leaves Dharma fighting for her life in the hospital?",
        "correct": "A severe automobile accident during a rainstorm",
        "distractors": ["A fall from the roof of their loft building", "A carbon monoxide leak in their apartment", "A structural collapse at her yoga studio"],
        "d": 2
    },
    {
        "q": "What was the full bohemian name given to Dharma at birth by her counter-culture parents?",
        "correct": "Dharma Freedom Finkelstein",
        "distractors": ["Dharma Sunshine Finkelstein", "Dharma Peace Finkelstein", "Dharma Harmony Finkelstein"],
        "d": 2
    },
    {
        "q": "What athletic hobby did Kitty Montgomery play obsessively while gossiping and criticizing Dharma?",
        "correct": "Country club tennis",
        "distractors": ["Equestrian dressage", "Polo", "Croquet"],
        "d": 2
    },
    {
        "q": "What were the names of Dharma's two beloved pet dogs who often created chaos in her loft?",
        "correct": "Stinky and Nunzio",
        "distractors": ["Peanut and Butter", "Cosmo and Wanda", "Rusty and Bingo"],
        "d": 2
    },
    {
        "q": "Which Spinal Tap star guest starred on The Nanny as C.C. Babcock's handsome brother Noel who takes Fran on a date?",
        "correct": "Michael McKean",
        "distractors": ["Christopher Guest", "Harry Shearer", "Rob Reiner"],
        "d": 2
    },
    {
        "q": "On Spin City, what higher political office does Mayor Randall Winston campaign for during the later seasons?",
        "correct": "United States Senator from New York",
        "distractors": ["Governor of New York", "President of the United States", "United States Ambassador to the U.N."],
        "d": 2
    },
    {
        "q": "On Just Shoot Me!, who was Jack Gallo's youthful, high-school-aged fourth wife played by Rebecca Budig?",
        "correct": "Allie Gallo",
        "distractors": ["Chloe Gallo", "Tiffany Gallo", "Amber Gallo"],
        "d": 3
    },
    {
        "q": "On The Larry Sanders Show, what was the name of Hank Kingsley's fiercely protective agent played by Bob Odenkirk in early seasons?",
        "correct": "Stevie Grant",
        "distractors": ["Ari Gold", "Marty Funkhouser", "Sammy Rhodes"],
        "d": 3
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "staging", "90s_sitcoms_batch6.json")
    make_batch(q_batch6, 6, out)
