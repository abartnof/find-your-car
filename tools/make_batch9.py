#!/usr/bin/env python3
"""
Generate Batch 9: Extratextual & Metatextual: Casting Secrets, Unsold Pilots, Cameos & Historic Crossovers (100 questions)
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from sitcom_builder import make_batch

q_batch9 = [
    # Crossovers Across Sitcom Universes (25 questions)
    {
        "q": "How did Lisa Kudrow's characters on Mad About You and Friends end up existing in the exact same television universe?",
        "correct": "Producers made Phoebe Buffay the identical twin sister of Ursula Buffay, the inept waitress Kudrow was already playing on Mad About You",
        "distractors": ["Phoebe was revealed to have amnesia and was living a double life under an alias", "It was never explained, and Kudrow simply played two completely unrelated roles on the same night", "Phoebe was originally written as a hallucination in Ursula's mind"],
        "d": 1
    },
    {
        "q": "Which Mad About You characters walk into Central Perk on Friends, mistake Phoebe Buffay for her twin sister Ursula, and try to order coffee?",
        "correct": "Jamie Buchman (Helen Hunt) and Fran Devanow (Leila Kenzle)",
        "distractors": ["Paul Buchman (Paul Reiser) and his brother Danny", "Ira Buchman and Lisa Stemple", "Sylvia Buchman and Debbie Buchman"],
        "d": 1
    },
    {
        "q": "Why does Cosmo Kramer appear inside Paul Buchman's bachelor apartment in an early crossover episode of Mad About You?",
        "correct": "Kramer was subletting the apartment from Paul, establishing that Seinfeld and Mad About You shared the same universe",
        "distractors": ["Kramer was working as an exterminator spraying for Manhattan roaches", "Kramer was hired by Paul to direct a low-budget documentary", "Kramer accidentally broke into the apartment thinking it was Newman's"],
        "d": 1
    },
    {
        "q": "What major city-wide emergency linked the plots of Mad About You and Friends on the night of November 3, 1994?",
        "correct": "A massive New York City electrical blackout dubbed 'Blackout Thursday'",
        "distractors": ["A severe blizzard that shut down the subway system", "A water main break that flooded Central Park", "A transit strike that forced everyone to walk"],
        "d": 2
    },
    {
        "q": "In a 1991 TGIF crossover event, why does Steve Urkel visit San Francisco and enter the Tanner residence on Full House?",
        "correct": "To help Uncle Jesse's friend and comfort Michelle Tanner, who is anxious about wearing eyeglasses",
        "distractors": ["To repair Joey Gladstone's broken comedy car with his tools", "To tutor DJ Tanner in high school trigonometry", "To compete in an amateur accordion contest against Danny Tanner"],
        "d": 1
    },
    {
        "q": "On which other ABC TGIF sitcom did Steve Urkel crash-land with a jetpack into a backyard and teach the family how to do 'The Urkel'?",
        "correct": "Step by Step",
        "distractors": ["Boy Meets World", "Hangin' with Mr. Cooper", "Dinosaurs"],
        "d": 1
    },
    {
        "q": "In which Nantucket airport episode of Wings does Dr. Frasier Crane make a crossover guest appearance alongside his wife Lilith?",
        "correct": "\"Planes, Trains and Visiting Cranes\"",
        "distractors": [
            "\"A Crane Over Nantucket\"",
            "\"Cheers to Sandpiper\"",
            "\"Psychiatry in the Sky\""
        ],
        "d": 2
    },
    {
        "q": "Which two beloved Cheers regulars also made a memorable crossover guest appearance at the Wings airport terminal?",
        "correct": "Norm Peterson (George Wendt) and Cliff Clavin (John Ratzenberger)",
        "distractors": ["Sam Malone (Ted Danson) and Woody Boyd (Woody Harrelson)", "Carla Tortelli (Rhea Perlman) and Coach Ernie Pantusso (Nicholas Colasanto)", "Frasier Crane and Rebecca Howe (Kirstie Alley)"],
        "d": 2
    },
    {
        "q": "Which classic 1970s sitcom couple made a historic cameo in the series finale of The Fresh Prince of Bel-Air to buy the Banks mansion?",
        "correct": "George and Louise Jefferson (The Jeffersons)",
        "distractors": ["Fred and Lamont Sanford (Sanford and Son)", "Archie and Edith Bunker (All in the Family)", "J.J. and Thelma Evans (Good Times)"],
        "d": 1
    },
    {
        "q": "In a special 1997 TGIF promotion, what magical event caused characters from Sabrina, Boy Meets World, You Wish, and Teen Angel to cross paths?",
        "correct": "Salem the cat swallowed a 'time ball' that sent the characters hurling through different historical eras across all four shows",
        "distractors": ["A magical meteor struck the ABC broadcast antenna in Burbank", "A wicked sorceress transported all the teenagers into an enchanted medieval castle", "A freak solar eclipse swapped the minds of the characters between households"],
        "d": 2
    },
    {
        "q": "Which Fresh Prince of Bel-Air character made a guest crossover appearance on Blossom in Season 2?",
        "correct": "Hilary Banks (Karyn Parsons)",
        "distractors": ["Will Smith", "Carlton Banks", "Ashley Banks"],
        "d": 2
    },
    {
        "q": "Which Everybody Loves Raymond character made recurring crossover appearances on The King of Queens, hanging out with Doug Heffernan?",
        "correct": "Ray Barone (Ray Romano)",
        "distractors": ["Robert Barone", "Frank Barone", "Marie Barone"],
        "d": 1
    },
    {
        "q": "On The King of Queens, which other Everybody Loves Raymond family members appeared to play cards and argue with Arthur Spooner?",
        "correct": "Marie Barone (Doris Roberts) and Frank Barone (Peter Boyle)",
        "distractors": ["Debra Barone and Amy MacDougall", "Robert Barone and Gianni", "Hank and Pat MacDougall"],
        "d": 2
    },
    {
        "q": "Which NBC sitcom featured crossover cameos where Matthew Perry (Chandler Bing) and David Hyde Pierce (Niles Crane) appeared as their TV characters?",
        "correct": "Caroline in the City",
        "distractors": ["Suddenly Susan", "The Single Guy", "Just Shoot Me!"],
        "d": 2
    },
    {
        "q": "In a 1995 crossover, which character from Wings appeared on NewsRadio trying to acquire broadcasting equipment?",
        "correct": "Roy Biggins (David Schramm)",
        "distractors": ["Lowell Mather", "Joe Hackett", "Antonio Scarpacci"],
        "d": 3
    },
    {
        "q": "Which classic character played by Don Knotts made a cameo appearance in the fantasy sequences of Step by Step?",
        "correct": "Deputy Barney Fife",
        "distractors": ["Ralph Furley", "Mr. Morrison", "The Apple Dumpling Sheriff"],
        "d": 3
    },
    {
        "q": "What ABC daytime soap opera crossed over with Boy Meets World when Eric Matthews became obsessed with his favorite soap star?",
        "correct": "General Hospital",
        "distractors": ["All My Children", "One Life to Live", "Days of Our Lives"],
        "d": 2
    },
    {
        "q": "In the Season 5 episode of Martin titled 'Goin' Overboard', which Fox teen drama characters did Martin interact with on a cruise ship?",
        "correct": "Cast members of Beverly Hills, 90210",
        "distractors": ["Cast members of Party of Five", "Cast members of Melrose Place", "Cast members of New York Undercover"],
        "d": 3
    },
    {
        "q": "Which popular sitcom featured an episode where characters attended a taping of The Jerry Springer Show and incited a studio brawl?",
        "correct": "Roseanne",
        "distractors": ["The Fresh Prince of Bel-Air", "Home Improvement", "The Drew Carey Show"],
        "d": 2
    },
    {
        "q": "What ABC sitcom featured an elaborate crossover where Drew Carey fell asleep and woke up on the sets of multiple ABC sitcoms?",
        "correct": "The Drew Carey Show (visiting Grace Under Fire, Coach, and Ellen)",
        "distractors": ["Home Improvement visiting Boy Meets World", "Step by Step visiting Full House", "Hangin' with Mr. Cooper visiting Family Matters"],
        "d": 2
    },
    {
        "q": "On Moesha, which character crossed over into the pilot of The Parkers to establish the mother-daughter spinoff?",
        "correct": "Kim Parker (Countess Vaughn)",
        "distractors": ["Dee Mitchell", "Hakeem Campbell", "Frank Mitchell"],
        "d": 1
    },
    {
        "q": "Which iconic Dick Van Dyke Show star made a guest crossover appearance on Mad About You as Alan Brady?",
        "correct": "Carl Reiner",
        "distractors": ["Dick Van Dyke", "Morey Amsterdam", "Rose Marie"],
        "d": 2
    },
    {
        "q": "Which cartoon characters crossed over into a live-action episode of Home Improvement in a dream sequence?",
        "correct": "The Flintstones",
        "distractors": ["The Jetsons", "The Simpsons", "Scooby-Doo"],
        "d": 3
    },
    {
        "q": "Which character from Boy Meets World appeared on Sabrina the Teenage Witch in a magical time-warp crossover?",
        "correct": "Cory Matthews and Eric Matthews",
        "distractors": ["Mr. Feeny", "Shawn Hunter", "Topanga Lawrence"],
        "d": 2
    },
    {
        "q": "In a 1995 episode of Friends, which famous action hero made a guest cameo filming a movie in New York called 'Shut Up and Dance'?",
        "correct": "Jean-Claude Van Damme",
        "distractors": ["Arnold Schwarzenegger", "Sylvester Stallone", "Chuck Norris"],
        "d": 2
    },

    # Casting What-Ifs & Pilot Recastings (35 questions)
    {
        "q": "Which role on Friends was Courteney Cox originally invited by producers to audition for before she requested to play Monica Geller?",
        "correct": "Rachel Green",
        "distractors": ["Phoebe Buffay", "Carol Willick", "Janice Hosenstein"],
        "d": 1
    },
    {
        "q": "Which friend on Friends was the very first to be officially cast, with the character written specifically for his unique vocal cadence?",
        "correct": "Ross Geller (David Schwimmer)",
        "distractors": ["Chandler Bing (Matthew Perry)", "Joey Tribbiani (Matt LeBlanc)", "Jerry Seinfeld"],
        "d": 2
    },
    {
        "q": "Which future Marvel Cinematic Universe director and Swingers star was offered the role of Chandler Bing on Friends but turned it down?",
        "correct": "Jon Favreau",
        "distractors": ["Ben Stiller", "Paul Rudd", "Adam Sandler"],
        "d": 2
    },
    {
        "q": "Which actress was famously offered the role of Rachel Green on Friends first, but turned it down to star on the sketch show Saturday Night Live?",
        "correct": "Janeane Garofalo",
        "distractors": ["Molly Shannon", "Cheri Oteri", "Ana Gasteyer"],
        "d": 2
    },
    {
        "q": "Which future The Simpsons star auditioned twice for the role of Joey Tribbiani on Friends before being cast as recurring boyfriend David the Scientist Guy?",
        "correct": "Hank Azaria",
        "distractors": ["Dan Castellaneta", "Harry Shearer", "Rob Paulsen"],
        "d": 2
    },
    {
        "q": "Which celebrated comedian and actress was originally cast as radio producer Roz Doyle on Frasier and rehearsed for days before being replaced by Peri Gilpin?",
        "correct": "Lisa Kudrow",
        "distractors": ["Jane Lynch", "Patricia Heaton", "Julia Louis-Dreyfus"],
        "d": 1
    },
    {
        "q": "Why did Frasier creators Peter Casey and David Lee replace Lisa Kudrow with Peri Gilpin during rehearsals for the Frasier pilot?",
        "correct": "Kudrow's quirky, ethereal comedic energy didn't provide enough assertive force to push back against Kelsey Grammer's booming ego",
        "distractors": ["Kudrow forgot her lines repeatedly during the network run-through", "Kelsey Grammer demanded that his real-life friend be given the role", "Kudrow was already committed to an HBO comedy special"],
        "d": 2
    },
    {
        "q": "How did Lisa Kudrow's firing from Frasier directly lead to her life-changing casting on Friends months later?",
        "correct": "Frasier director James Burrows felt terrible about letting her go and championed her to the Friends casting directors",
        "distractors": ["She used her Frasier severance money to finance an independent pilot showcase", "NBC executives gave her a guaranteed development contract as an apology", "Her audition tape for Frasier was accidentally mailed to Marta Kauffman"],
        "d": 2
    },
    {
        "q": "Which actress, who later starred in Everybody Loves Raymond, auditioned for the role of Elaine Benes on Seinfeld?",
        "correct": "Patricia Heaton",
        "distractors": ["Jane Kaczmarek", "Felicity Huffman", "Allison Janney"],
        "d": 2
    },
    {
        "q": "Which actress, who later became famous as Karen Walker on Will & Grace, also auditioned for Elaine Benes on Seinfeld?",
        "correct": "Megan Mullally",
        "distractors": ["Kristen Johnston", "Leah Remini", "Wendie Malick"],
        "d": 2
    },
    {
        "q": "Which actor, who famously played George Costanza, was NOT the first choice of Larry David, who initially envisioned which comedian for George?",
        "correct": "Larry David initially wanted Steve Buscemi or Chris Alkaitis, while Paul Shaffer was offered the role directly and turned it down",
        "distractors": ["Jerry Stiller", "Richard Lewis", "Jon Lovitz"],
        "d": 3
    },
    {
        "q": "Why did David Letterman's bandleader Paul Shaffer famously turn down the role of George Costanza on Seinfeld?",
        "correct": "He received a voicemail from Jerry Seinfeld offering him the role, but never got around to returning the phone call",
        "distractors": ["His contract with NBC late night explicitly forbade prime-time acting", "He didn't want to relocate from Manhattan to Los Angeles", "He found the script uninteresting and thought the show would be cancelled in weeks"],
        "d": 2
    },
    {
        "q": "Which actress filmed the entire original unaired pilot of Home Improvement as Jill Taylor before Patricia Richardson was cast?",
        "correct": "Frances Fisher",
        "distractors": ["Jobeth Williams", "Geena Davis", "Annette O'Toole"],
        "d": 2
    },
    {
        "q": "Why did producers recast Frances Fisher with Patricia Richardson just days before shooting Home Improvement's second pilot?",
        "correct": "Test audiences felt Fisher played Jill with too much dramatic severity, creating poor comedic chemistry with Tim Allen",
        "distractors": ["Fisher suffered an ankle fracture during kitchen rehearsals", "Fisher walked out after a dispute over billing on the title screen", "Disney executives wanted an actress with stand-up comedy experience"],
        "d": 2
    },
    {
        "q": "Which actor was originally cast as Tim Taylor's Tool Time assistant Glen, but had to drop out to film Groundhog Day?",
        "correct": "Stephen Tobolowsky",
        "distractors": ["Kurt Fuller", "John Kapelos", "Wayne Knight"],
        "d": 2
    },
    {
        "q": "Who was originally cast and filmed the entire unaired pilot of Full House as Danny Tanner before Bob Saget took the role?",
        "correct": "John Posey",
        "distractors": ["Alan Thicke", "Paul Reiser", "David Coulier"],
        "d": 2
    },
    {
        "q": "Why was Bob Saget not available when the original Full House pilot was initially produced?",
        "correct": "He was under contract as an on-air contributor for CBS's The Morning Program",
        "distractors": ["He was touring Europe with a stand-up comedy festival", "He was directing an independent feature film in New York", "He refused to work with toddler actors until his agent convinced him"],
        "d": 2
    },
    {
        "q": "Which future Friends megastar auditioned for the role of Dan Conner on Roseanne before John Goodman won the part?",
        "correct": "None — John Goodman was the only actor who read with Roseanne, but Bob Hoskins was briefly considered",
        "distractors": ["Ted Danson", "Chevy Chase", "Dan Aykroyd"],
        "d": 3
    },
    {
        "q": "Which actress auditioned for the role of Rachel Green on Friends and later played Ross's British second wife Emily Waltham?",
        "correct": "Helen Baxendale",
        "distractors": ["Jane Leeves", "Minnie Driver", "Emily Mortimer"],
        "d": 3
    },
    {
        "q": "Which future Sex and the City star was offered the title role in Clueless (the television adaptation) and turned it down?",
        "correct": "Sarah Jessica Parker",
        "distractors": ["Kristin Davis", "Cynthia Nixon", "Kim Cattrall"],
        "d": 3
    },
    {
        "q": "Which actor auditioned for the role of Niles Crane on Frasier before David Hyde Pierce was cast without an audition?",
        "correct": "No one — the role of Niles was specifically created for David Hyde Pierce by the writers after seeing his photograph",
        "distractors": ["Hank Azaria", "Peter MacNicol", "Thomas Gibson"],
        "d": 2
    },
    {
        "q": "Which future Desperate Housewives star was cast in the pilot of Friends as Rachel Green's friend before her scene was cut?",
        "correct": "Teri Hatcher (who also guest starred on Seinfeld as Sidra)",
        "distractors": ["Marcia Cross", "Felicity Huffman", "Eva Longoria"],
        "d": 2
    },
    {
        "q": "Which Oscar-winning actress was originally approached to star as Grace Adler on Will & Grace before Debra Messing was cast?",
        "correct": "Nicollette Sheridan",
        "distractors": ["Marisa Tomei", "Helen Hunt", "Tia Leoni"],
        "d": 3
    },
    {
        "q": "How many times did Debra Messing turn down the role of Grace Adler before creators David Kohan and Max Mutchnick persuaded her with vodka?",
        "correct": "Several times, until they visited her apartment with a bottle of vodka and walked her through the scripts",
        "distractors": ["She accepted immediately at the first phone call", "She auditioned eight separate times against fifty other actresses", "She was forced to take it by an existing NBC talent holding contract"],
        "d": 2
    },
    {
        "q": "Which famous actress was considered for the role of Dharma in Dharma & Greg before Jenna Elfman gave her breakout audition?",
        "correct": "Janeane Garofalo",
        "distractors": ["Calista Flockhart", "Drew Barrymore", "Cameron Diaz"],
        "d": 3
    },
    {
        "q": "Which Saturday Night Live star was originally offered the role of Doug Heffernan on The King of Queens before Kevin James was cast?",
        "correct": "None — the show was created specifically around Kevin James following his stand-up appearance on Letterman",
        "distractors": ["Chris Farley", "Norm Macdonald", "David Spade"],
        "d": 2
    },
    {
        "q": "Which actress auditioned for the role of Debra Barone on Everybody Loves Raymond and was favored by CBS executives over Patricia Heaton?",
        "correct": "Jane Sibbett (who played Carol on Friends)",
        "distractors": ["Maggie Wheeler", "Faith Ford", "Leah Remini"],
        "d": 3
    },
    {
        "q": "Why did Ray Romano fight network executives to cast Patricia Heaton instead of their preferred choices?",
        "correct": "She was the only actress willing to kiss him during the audition read-through, showing natural married intimacy",
        "distractors": ["She brought homemade Italian cookies to the audition room", "Her father was a prominent sportswriter who knew Romano", "She agreed to take a 50% pay cut for the first season"],
        "d": 2
    },
    {
        "q": "Which actress was originally cast as Aunt Vivian on The Fresh Prince before Janet Hubert was chosen?",
        "correct": "None — Janet Hubert won the role directly over 400 actresses who auditioned in New York and L.A.",
        "distractors": ["Phylicia Rashad", "Diahann Carroll", "Sheryl Lee Ralph"],
        "d": 3
    },
    {
        "q": "Which young actor auditioned for the role of Cory Matthews on Boy Meets World before Ben Savage was selected?",
        "correct": "Rider Strong (who was subsequently cast as his best friend Shawn Hunter)",
        "distractors": ["Joseph Gordon-Levitt", "Jonathan Taylor Thomas", "Elijah Wood"],
        "d": 2
    },
    {
        "q": "Which actor auditioned for the role of Steve Urkel on Family Matters before Jaleel White walked in with his father's glasses?",
        "correct": "Bumper Robinson",
        "distractors": ["Merlin Santana", "Brandon Adams", "Deon Richmond"],
        "d": 3
    },
    {
        "q": "Which famous actress was offered the role of Phoebe Buffay on Friends but passed to star in her own short-lived sitcom?",
        "correct": "Ellen DeGeneres",
        "distractors": ["Kathy Griffin", "Paula Poundstone", "Rosie O'Donnell"],
        "d": 2
    },
    {
        "q": "What major star auditioned for the role of Kramer on Seinfeld before Michael Richards secured the role?",
        "correct": "Tony Shalhoub (as well as Larry Hankin, who later played 'TV Kramer')",
        "distractors": ["Christopher Lloyd", "Jeff Goldblum", "John Malkovich"],
        "d": 2
    },
    {
        "q": "Which actor, who played 'TV Kramer' in the Season 4 Seinfeld pilot arc, had actually auditioned for the real Kramer in 1989?",
        "correct": "Larry Hankin",
        "distractors": ["Stephen Tobolowsky", "Kevin McDonald", "Mark Metcalf"],
        "d": 2
    },
    {
        "q": "Which actress was considered for the role of Kelly Kapowski on Saved by the Bell before Tiffani-Amber Thiessen won it?",
        "correct": "Jennie Garth (who was subsequently cast in Beverly Hills, 90210)",
        "distractors": ["Tori Spelling", "Shannen Doherty", "Alyssa Milano"],
        "d": 2
    },

    # High-Profile Guest Stars & Cameos (40 questions)
    {
        "q": "Which two legendary film comedy superstars made an entirely improvised, uncredited cold-open cameo on Friends in Season 3?",
        "correct": "Robin Williams and Billy Crystal",
        "distractors": ["Steve Martin and Martin Short", "Dan Aykroyd and Chevy Chase", "Jim Carrey and Jeff Daniels"],
        "d": 1
    },
    {
        "q": "Why were Robin Williams and Billy Crystal in the building to film their impromptu Friends coffeehouse scene?",
        "correct": "They were filming the comedy movie 'Fathers' Day' on an adjacent Warner Bros. soundstage and dropped in to say hello",
        "distractors": ["They had lost a charity poker game to director James Burrows", "NBC paid them each $1 million to boost sweeps ratings", "They were scouting Matthew Perry for an upcoming film"],
        "d": 2
    },
    {
        "q": "Which Hollywood superstar guest starred on Friends as Rachel's high school rival Will Colbert, co-founder of the 'I Hate Rachel Green Club'?",
        "correct": "Brad Pitt (who was married to Jennifer Aniston at the time)",
        "distractors": ["George Clooney", "Tom Cruise", "Johnny Depp"],
        "d": 1
    },
    {
        "q": "Why did Bruce Willis agree to guest star on Friends as Elizabeth's father Paul Stevens for SAG scale pay and donate his fee to charity?",
        "correct": "He lost a box-office wager to Matthew Perry regarding whether their film 'The Whole Nine Yards' would open at #1",
        "distractors": ["He was a massive fan of Courteney Cox from their music video days", "His daughter begged him to appear on the show", "Director James Burrows had saved his early acting career"],
        "d": 1
    },
    {
        "q": "Which Oscar-winning superstar demanded that Matthew Perry write her a paper on quantum physics before agreeing to guest star on Friends?",
        "correct": "Julia Roberts",
        "distractors": ["Sandra Bullock", "Nicole Kidman", "Jodie Foster"],
        "d": 2
    },
    {
        "q": "Which legendary Hollywood icon appeared on Friends as an eccentric actor who catches Joey Tribbiani showering in his dressing room?",
        "correct": "Charlton Heston",
        "distractors": ["Kirk Douglas", "Gregory Peck", "Robert Mitchum"],
        "d": 2
    },
    {
        "q": "What real estate mogul and future U.S. President made a cameo on The Fresh Prince of Bel-Air in Season 4, seeking to buy the mansion?",
        "correct": "Donald Trump (accompanied by Marla Maples)",
        "distractors": ["Ross Perot", "Steve Forbes", "Michael Bloomberg"],
        "d": 1
    },
    {
        "q": "Which daytime talk show queen made a guest appearance on The Fresh Prince of Bel-Air as herself, inviting the Banks family onto her show?",
        "correct": "Oprah Winfrey",
        "distractors": ["Sally Jessy Raphael", "Ricki Lake", "Jenny Jones"],
        "d": 1
    },
    {
        "q": "What multi-platinum R&B vocal group performed at baby Nicky's christening in Season 4 of The Fresh Prince of Bel-Air?",
        "correct": "Boyz II Men",
        "distractors": ["Jodeci", "Shai", "All-4-One"],
        "d": 1
    },
    {
        "q": "Which Broadway and film superstar guest starred on Seinfeld in 'The Understudy', playing an emotional softball player?",
        "correct": "Bette Midler",
        "distractors": ["Barbra Streisand", "Liza Minnelli", "Bernadette Peters"],
        "d": 1
    },
    {
        "q": "Which Oscar-winning actress played a fictionalized version of herself on Seinfeld, agreeing to date George Costanza because she likes short, funny, quirky bald men?",
        "correct": "Marisa Tomei",
        "distractors": ["Winona Ryder", "Diane Keaton", "Mira Sorvino"],
        "d": 1
    },
    {
        "q": "In the famous Seinfeld episode 'The Mom & Pop Store', which Oscar-winning actor bites Kramer on the arm while hailing a cab?",
        "correct": "Jon Voight",
        "distractors": ["Dustin Hoffman", "Gene Hackman", "Robert De Niro"],
        "d": 1
    },
    {
        "q": "Which former New York Mets baseball legend guest starred on Seinfeld in a two-part episode parodying the JFK assassination magic bullet theory?",
        "correct": "Keith Hernandez",
        "distractors": ["Darryl Strawberry", "Dwight Gooden", "Mookie Wilson"],
        "d": 1
    },
    {
        "q": "Which New York City Mayor made a cameo appearance on Seinfeld in the episode 'The Non-Fat Yogurt'?",
        "correct": "Rudy Giuliani",
        "distractors": ["Ed Koch", "David Dinkins", "Michael Bloomberg"],
        "d": 1
    },
    {
        "q": "Which morning talk show host appeared as himself on Seinfeld when Kramer promoted his coffee table book about coffee tables?",
        "correct": "Regis Philbin (along with Kathie Lee Gifford)",
        "distractors": ["Phil Donahue", "Geraldo Rivera", "Maury Povich"],
        "d": 1
    },
    {
        "q": "Which legendary sci-fi actor guest starred on 3rd Rock from the Sun as the Big Giant Head, reenacting his famous Twilight Zone airline gremlin scene with John Lithgow?",
        "correct": "William Shatner",
        "distractors": ["Leonard Nimoy", "George Takei", "Patrick Stewart"],
        "d": 1
    },
    {
        "q": "Which British rock icon guest starred on The Drew Carey Show as a musician auditioning for Drew's garage band?",
        "correct": "Joe Walsh (along with Slash and Rick Nielsen)",
        "distractors": ["Eric Clapton", "Jimmy Page", "Pete Townshend"],
        "d": 2
    },
    {
        "q": "Which pop music legend guest starred on Home Improvement, challenging Tim Taylor to an electric lawnmower race?",
        "correct": "George Foreman (and also Mario Andretti and race car drivers)",
        "distractors": ["Muhammad Ali", "Mike Tyson", "Evander Holyfield"],
        "d": 2
    },
    {
        "q": "Which astronaut and American hero appeared as himself on Home Improvement to discuss space exploration on Tool Time?",
        "correct": "Buzz Aldrin (and also John Glenn)",
        "distractors": ["Neil Armstrong", "Alan Shepard", "Jim Lovell"],
        "d": 2
    },
    {
        "q": "Which comedy legend won three consecutive Emmy Awards for Outstanding Guest Actor playing Paul's Uncle Phil on Mad About You?",
        "correct": "Mel Brooks",
        "distractors": ["Carl Reiner", "Sid Caesar", "Don Rickles"],
        "d": 1
    },
    {
        "q": "Which former Tonight Show host made a rare television acting cameo on The Larry Sanders Show as himself?",
        "correct": "Johnny Carson (appearing in an elevator with Garry Shandling)",
        "distractors": ["Jay Leno", "David Letterman", "Conan O'Brien"],
        "d": 2
    },
    {
        "q": "Which country music superstar guest starred on Wings as himself, stranded at the Nantucket airport and playing guitar?",
        "correct": "Clint Black",
        "distractors": ["Garth Brooks", "Vince Gill", "Randy Travis"],
        "d": 2
    },
    {
        "q": "Which veteran actress played Frasier and Niles' eccentric, sherry-loving mother Hester Crane in home video flashbacks on Frasier?",
        "correct": "Rita Wilson",
        "distractors": ["Nancy Marchand", "Blythe Danner", "Piper Laurie"],
        "d": 3
    },
    {
        "q": "Which superstar actor made a guest appearance on Friends as Dr. Michael Mitchell alongside George Clooney, parodying their ER roles?",
        "correct": "Noah Wyle",
        "distractors": ["Anthony Edwards", "Eriq La Salle", "Goran Visnjic"],
        "d": 1
    },
    {
        "q": "Which supermodel guest starred on Just Shoot Me! as Dennis Finch's gorgeous rock-star wife?",
        "correct": "Rebecca Romijn",
        "distractors": ["Tyra Banks", "Cindy Crawford", "Elle Macpherson"],
        "d": 1
    },
    {
        "q": "Which iconic heavyweight boxing champion made a guest appearance on The Fresh Prince of Bel-Air, knocking out Will's rival?",
        "correct": "Evander Holyfield (and Riddick Bowe in another episode)",
        "distractors": ["Mike Tyson", "Lennox Lewis", "George Foreman"],
        "d": 2
    },
    {
        "q": "Which Grammy-winning jazz vocalist made a memorable guest appearance on Frasier as the station manager Kenny's favorite singer?",
        "correct": "Tony Bennett",
        "distractors": ["Harry Connick Jr.", "Michael Bublé", "Bobby Darin"],
        "d": 3
    },
    {
        "q": "Which legendary rock star made a guest cameo on Martin as himself, offering Martin Payne career advice?",
        "correct": "Snoop Dogg (and The Notorious B.I.G. in another classic episode)",
        "distractors": ["Tupac Shakur", "Ice Cube", "Dr. Dre"],
        "d": 2
    },
    {
        "q": "Which legendary hip-hop icon guest starred as himself on Martin, performing at Martin's apartment in Season 4?",
        "correct": "The Notorious B.I.G.",
        "distractors": ["Jay-Z", "Nas", "Method Man"],
        "d": 1
    },
    {
        "q": "Which Golden Globe-winning actress guest starred on Seinfeld as George's girlfriend who looked uncannily like Jerry Seinfeld?",
        "correct": "Janeane Garofalo (Jeannie Steinman)",
        "distractors": ["Courteney Cox", "Amanda Peet", "Mariska Hargitay"],
        "d": 2
    },
    {
        "q": "Which future Law & Order: SVU superstar auditioned for Elaine and later guest starred on Seinfeld as an actress auditioning for 'Jerry'?",
        "correct": "Mariska Hargitay",
        "distractors": ["Kelli Giddish", "Stephanie March", "Diane Neal"],
        "d": 2
    },
    {
        "q": "Which legendary comedian played Jerry Seinfeld's father Morty Costanza... wait, Morty Seinfeld in the Season 1 episode before Barney Martin took over?",
        "correct": "Phil Bruns",
        "distractors": ["Jack Carter", "Harold Gould", "Tom Poston"],
        "d": 3
    },
    {
        "q": "Which Oscar-winning actor guest starred on The Nanny as himself, hiring Fran to look after his children in Manhattan?",
        "correct": "Dan Aykroyd (and also Chevy Chase in another cameo)",
        "distractors": ["Bill Murray", "Steve Martin", "Eddie Murphy"],
        "d": 2
    },
    {
        "q": "Which legendary Hollywood sex symbol made a guest appearance on The Nanny as Maxwell Sheffield's glamorous starlet friend?",
        "correct": "Joan Collins",
        "distractors": ["Elizabeth Taylor", "Zsa Zsa Gabor", "Raquel Welch"],
        "d": 2
    },
    {
        "q": "Which screen icon appeared on The Nanny promoting her signature perfume and trading one-liners with Fran Fine?",
        "correct": "Elizabeth Taylor",
        "distractors": ["Sophia Loren", "Audrey Hepburn", "Lauren Bacall"],
        "d": 2
    },
    {
        "q": "Which future Breaking Bad superstar guest starred on Seinfeld as Dr. Tim Whatley, the dentist who converted to Judaism for the jokes?",
        "correct": "Bryan Cranston",
        "distractors": ["Bob Odenkirk", "Dean Norris", "Aaron Paul"],
        "d": 1
    },
    {
        "q": "Which future Better Call Saul superstar played Elaine's medical student boyfriend who fails the medical exam on Seinfeld?",
        "correct": "Bob Odenkirk",
        "distractors": ["David Cross", "Michael McKean", "Peter Gould"],
        "d": 1
    },
    {
        "q": "Which Saturday Night Live veteran played Elaine's rabidly anti-abortion boyfriend who refused to move a sofa on Seinfeld?",
        "correct": "Kevin McDonald (from The Kids in the Hall)",
        "distractors": ["Mark McKinney", "Scott Thompson", "Bruce McCulloch"],
        "d": 3
    },
    {
        "q": "Which famous news anchor appeared as himself on Murphy Brown to interview Murphy about her journalistic controversies?",
        "correct": "Walter Cronkite (along with Connie Chung and Irving R. Levine)",
        "distractors": ["Tom Brokaw", "Peter Jennings", "Dan Rather"],
        "d": 2
    },
    {
        "q": "Which Hollywood superstar guest starred on Friends in a two-part post-Super Bowl episode as Susie Moss, seeking revenge on Chandler Bing?",
        "correct": "Julia Roberts",
        "distractors": ["Brooke Shields", "Cameron Diaz", "Demi Moore"],
        "d": 1
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "staging", "90s_sitcoms_batch9.json")
    make_batch(q_batch9, 9, out)
