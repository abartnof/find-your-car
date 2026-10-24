#!/usr/bin/env python3
"""
Generate Batch 10: Iconic Episodes, Finales, Catchphrases, Awards & Cultural Legacy (100 questions)
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from sitcom_builder import make_batch

q_batch10 = [
    # Iconic Series Finales (25 questions)
    {
        "q": "In the controversial 1998 series finale of Seinfeld, why are Jerry, George, Elaine, and Kramer arrested in Latham, Massachusetts?",
        "correct": "Violating the local 'Good Samaritan Law' by mocking and filming a carjacking victim instead of helping him",
        "distractors": ["Accidentally burning down a historic colonial church with a Cuban cigar", "Fleeing the scene of a hit-and-run accident involving a mail truck", "Smuggling illegal Cuban cigars aboard NBC's private jet"],
        "d": 1
    },
    {
        "q": "What is the famous final visual shot of The Fresh Prince of Bel-Air before the screen fades to black in the series finale?",
        "correct": "Will standing completely alone in the empty, echoey living room of the Banks mansion",
        "distractors": ["Uncle Phil hugging Will on the front lawn as a taxi pulls away", "Jazz being thrown out of the front doors one last time into the sunset", "The Banks family waving from the back of an airport limousine"],
        "d": 1
    },
    {
        "q": "Why is the 1994 series finale of Dinosaurs ('Changing Nature') remembered as one of the darkest in television history?",
        "correct": "Earl Sinclair's corporate blunder triggers an irreversible global Ice Age, ending the series with the family facing impending extinction",
        "distractors": ["A volcanic super-eruption incinerates their suburban neighborhood live on air", "A giant asteroid strikes Pangea, destroying the Wesayso Corporation", "The characters are captured by time-traveling human scientists and put into zoos"],
        "d": 1
    },
    {
        "q": "What plot resolution occurs in the two-part Full House series finale 'Michelle Rides Again'?",
        "correct": "Michelle recovers her lost memory following a horseback riding fall, and DJ attends her prom accompanied by Steve",
        "distractors": ["Uncle Jesse lands a permanent recording contract in Tokyo and moves the family to Japan", "Danny Tanner is named network anchor of Good Morning America in New York", "Joey Gladstone wins a nationwide talent search to star in a feature film"],
        "d": 1
    },
    {
        "q": "In the series finale of Home Improvement, what absurd solution does Tim Taylor contemplate to avoid leaving Detroit?",
        "correct": "Physically hoisting their entire suburban house onto a flatbed barge to move it across Lake Michigan",
        "distractors": ["Building an underground tunnel from their garage directly to Indiana", "Buying Binford Tools and converting it into a residential compound", "Installing jet engines on their station wagon to commute daily"],
        "d": 2
    },
    {
        "q": "What shocking revelation in the Roseanne series finale overturned the entire premise of Season 9?",
        "correct": "Dan actually died of his Season 8 heart attack, and the lottery millions and luxury life were Roseanne's fictional grief fantasy",
        "distractors": ["Roseanne was dreaming while recovering from surgery at Wellman Plastics", "Darlene was the real mother of Becky's child all along", "The family had been living in witness protection following a mob trial"],
        "d": 1
    },
    {
        "q": "In the emotional series finale of Boy Meets World ('Brave New World'), what are Mr. Feeny's unforgettable parting words to his students?",
        "correct": "\"Believe in yourselves. Dream. Try. Do good.\"",
        "distractors": [
            "\"Work hard, be kind, and never give up on love.\"",
            "\"Knowledge is power. Go out and change the world.\"",
            "\"Life is tough, but you are tougher. Goodbye.\""
        ],
        "d": 1
    },
    {
        "q": "In the finale of Boy Meets World, when Cory asks Mr. Feeny 'Don't you mean do well?', what does Feeny reply?",
        "correct": "\"No, I mean do good.\"",
        "distractors": [
            "\"Doing well is easy; doing good is what matters.\"",
            "\"Do well for yourself, do good for others.\"",
            "\"Both, Cory. Always both.\""
        ],
        "d": 2
    },
    {
        "q": "How does the sitcom Wings conclude its eight-season run in 1997?",
        "correct": "Joe and Helen prepare to move to Boston for Helen's cello scholarship, while Brian and Casey agree to run Sandpiper Air",
        "distractors": ["Roy Biggins buys Sandpiper Air and merges it with Aeromass", "Tom Nevers Field is demolished to make way for a luxury resort", "Antonio Scarpacci wins the Massachusetts state lottery and buys the airfield"],
        "d": 2
    },
    {
        "q": "In the Season 6 series finale of The Nanny, what double celebration takes place in the hospital?",
        "correct": "Fran gives birth to twins while C.C. Babcock and Niles announce their surprise marriage",
        "distractors": ["Maxwell wins his first Tony Award while Sylvia announces she is remarrying", "Fran and Maxwell adopt three French orphans while Yetta wins the lottery", "Val marries Danny Imperiali while Maggie graduates from Oxford"],
        "d": 1
    },
    {
        "q": "In the Season 10 finale of Murphy Brown, whom does Murphy encounter in a surreal dream sequence during her cancer surgery?",
        "correct": "God, portrayed by veteran comedic actor Alan Ball",
        "distractors": ["Dan Quayle, apologizing for his 1992 speech", "Edward R. Murrow, welcoming her to the journalistic pantheon", "Her former house painter Eldin Bernecky in heaven"],
        "d": 2
    },
    {
        "q": "In the final episode of NewsRadio ('New Hampshire'), what drastic life change does eccentric billionaire Jimmy James announce?",
        "correct": "He trades WNYX for a tiny radio station and newspaper in New Hampshire and moves the entire staff with him",
        "distractors": ["He sells the station to an Australian conglomerate and retires to Tahiti", "He liquidates his fortune to run for the United Nations General Assembly", "He admits he was D.B. Cooper and disappears via parachute"],
        "d": 2
    },
    {
        "q": "What futuristic format was used for the series finale of Mad About You ('The Final Frontier') in 1999?",
        "correct": "A documentary made decades in the future by Paul and Jamie's adult daughter Mabel (played by Janeane Garofalo)",
        "distractors": ["A live broadcast from Times Square with celebrity musical cameos", "An animated special showing Paul and Jamie living on a lunar colony", "A courtroom trial where their neighbors sue them for noisy arguments"],
        "d": 2
    },
    {
        "q": "In the final season of Family Matters, what romantic milestone do Steve Urkel and Laura Winslow finally achieve?",
        "correct": "Steve proposes to Laura in Paris and she enthusiastically accepts, choosing Steve over Stefan",
        "distractors": ["Laura rejects Steve permanently, leading him to marry Myra Monkhouse", "Steve uses his transformation machine to become Stefan forever", "They elope to Las Vegas without telling Carl and Harriette"],
        "d": 1
    },
    {
        "q": "In the series finale of The Larry Sanders Show ('Flip'), what superstar guest stars sing and perform as Larry hosts his final broadcast?",
        "correct": "Jim Carrey, Carol Burnett, Warren Beatty, and Sean Penn",
        "distractors": ["Robin Williams, Jerry Seinfeld, and Tom Hanks", "Johnny Carson, David Letterman, and Jay Leno", "Billy Crystal, Steve Martin, and Martin Short"],
        "d": 2
    },
    {
        "q": "How does the long-running sports sitcom Coach conclude in 1997?",
        "correct": "Hayden Fox retires from the NFL's Orlando Breakers to return to Minnesota and raise his adopted baby son Timothy with Christine",
        "distractors": ["Hayden leads the Breakers to a Super Bowl victory and is named NFL Commissioner", "Hayden is inducted into the College Football Hall of Fame in South Bend", "Luther Van Dam takes over as head coach after Hayden moves to Hawaii"],
        "d": 2
    },
    {
        "q": "In the series finale of Martin, why do Martin and Gina pack their bags and say goodbye to their Detroit friends?",
        "correct": "Martin lands a syndicated television talk show host job and Gina receives a corporate promotion in Los Angeles",
        "distractors": ["Martin is offered the morning radio drive-time slot at Power 105 in New York", "They inherit a Caribbean beach resort from Uncle Phil", "Martin enters the witness protection program after exposing a local crime boss"],
        "d": 1
    },
    {
        "q": "How does the final season of Living Single conclude for Maxine Shaw and Kyle Barker?",
        "correct": "Maxine discovers she is pregnant through an anonymous sperm donor who turns out to be Kyle, and Kyle returns to profess his love",
        "distractors": ["Maxine and Kyle get married in a double wedding alongside Khadijah and Scooter", "Maxine is appointed to the New York State Supreme Court and moves to Albany", "Kyle loses his Wall Street firm and becomes the building's new handyman"],
        "d": 2
    },
    {
        "q": "In the series finale of Sister, Sister, what milestone event brings the entire family together in Hawaii?",
        "correct": "Lisa Landry's wedding to Victor Sims, alongside the twins' high school and college milestones",
        "distractors": ["Ray Campbell's election as Mayor of Detroit", "Tia and Tamera launching their own syndicated television show", "The opening of Lisa's flagship fashion department store in Honolulu"],
        "d": 2
    },
    {
        "q": "In the series finale of Blossom, what family transition occurs as the children prepare for adulthood?",
        "correct": "Nick and Carol put the family home up for sale, while Blossom prepares to move into a college dormitory",
        "distractors": ["Blossom marries Vinnie Bonitardi in the backyard", "Joey is drafted into the Major Leagues by the New York Yankees", "Anthony opens his own private medical clinic in San Francisco"],
        "d": 2
    },
    {
        "q": "In Saved by the Bell's final high school broadcast, what emotional song do the six friends sing together at graduation?",
        "correct": "\"Friends Forever\"",
        "distractors": [
            "\"Memories of Bayside\"",
            "\"Time of Our Lives\"",
            "\"Here's to the Future\""
        ],
        "d": 1
    },
    {
        "q": "In the series finale of 3rd Rock from the Sun ('The Thing That Wouldn't Die'), how does the alien mission conclude?",
        "correct": "The Big Giant Head orders the Solomons to extract themselves and return to their home planet, forcing Dick to say a heartbreaking goodbye to Mary",
        "distractors": ["The aliens choose to become permanent mortals and live out their human lives in Ohio", "Their spaceship crashes into Pendelton State University, exposing their secret to the world", "The military captures the Solomons and transports them to Area 51"],
        "d": 1
    },
    {
        "q": "In the finale of Just Shoot Me!, what happens to Blush Magazine and the staff?",
        "correct": "Jack Gallo suddenly retires and leaves the magazine to Maya, who decides to shut it down and start her own publication",
        "distractors": ["Blush is bought out by a French fashion conglomerate and moved to Paris", "Dennis Finch inherits the publisher position after marrying Jack's widow", "Nina Van Horn burns down the Blush offices in an accidental martini fire"],
        "d": 2
    },
    {
        "q": "What major plot twist marks the end of Michael J. Fox's character Mike Flaherty on Spin City?",
        "correct": "He takes public responsibility for an alleged mob bribery scandal to shield Mayor Winston from political ruin and resigns",
        "distractors": ["He is elected Mayor of New York City in a landslide victory", "He marries his journalist girlfriend and moves to Washington to advise the President", "He suffers an on-screen health emergency that requires immediate medical retirement"],
        "d": 1
    },
    {
        "q": "How does the sitcom Herman's Head end in 1994?",
        "correct": "Herman finally finds romantic balance and his four mental personas learn to cooperate inside his brain",
        "distractors": ["Herman suffers head trauma that knocks out all four personas permanently", "A fifth character representing Paranoia takes over his brain", "Herman becomes a famous author by publishing the arguments in his head"],
        "d": 3
    },

    # Iconic Cultural Catchphrases & Running Gags (25 questions)
    {
        "q": "What famous Seinfeld catchphrase was coined by George's girlfriend to gloss over significant details of an encounter?",
        "correct": "Yada, yada, yada",
        "distractors": ["Bada bing, bada boom", "Blah, blah, blah", "Et cetera, et cetera"],
        "d": 1
    },
    {
        "q": "What mantra does Frank Costanza scream to lower his blood pressure on Seinfeld, which Lloyd Braun warns will lead to insanity?",
        "correct": "Serenity now!",
        "distractors": ["Peace be still!", "Calmness rules!", "Hoochie mama!"],
        "d": 1
    },
    {
        "q": "What iconic catchphrase does Kramer deliver upon tasting a dry snack on the set of a Woody Allen film?",
        "correct": "These pretzels are making me thirsty!",
        "distractors": ["These peanuts are driving me nuts!", "This popcorn needs some butter!", "These crackers are drying my mouth!"],
        "d": 1
    },
    {
        "q": "What politically correct qualifier do Jerry and George repeatedly append whenever discussing homosexuality in 'The Outing'?",
        "correct": "Not that there's anything wrong with that!",
        "distractors": ["To each their own!", "Live and let live!", "Whatever works for you!"],
        "d": 1
    },
    {
        "q": "What was Tim 'The Tool Man' Taylor's signature vocalization whenever he admired raw mechanical power?",
        "correct": "A series of guttural chimpanzee grunts: Arrgh, arrgh, arrgh!",
        "distractors": ["A loud cowboy yee-haw and knee slap", "A mechanical siren howl", "A high-pitched wolf whistle"],
        "d": 1
    },
    {
        "q": "What catchphrase did little Michelle Tanner deliver accompanied by a thumbs-up on Full House?",
        "correct": "You got it, dude!",
        "distractors": ["No problem, pal!", "Right on, mister!", "Thumbs up, buddy!"],
        "d": 1
    },
    {
        "q": "What phrase did Stephanie Tanner exclaim whenever she felt insulted or slighted by her sisters?",
        "correct": "How rude!",
        "distractors": ["That's uncalled for!", "So totally bogus!", "Get out of here!"],
        "d": 1
    },
    {
        "q": "What phrase did Uncle Jesse Katsopolis utter whenever he was overwhelmed by passion or beauty?",
        "correct": "Have mercy!",
        "distractors": ["Mercy me!", "Good heavens!", "Lord have mercy!"],
        "d": 1
    },
    {
        "q": "What catchphrase did Joey Gladstone deliver with two snipping fingers across his chest?",
        "correct": "Cut it out!",
        "distractors": ["Knock it off!", "Chill on out!", "Wrap it up!"],
        "d": 1
    },
    {
        "q": "What was Cody Lambert's iconic California-surfer exclamation on Step by Step?",
        "correct": "Whoa, dude!",
        "distractors": ["Totally tubular!", "Gnarly times!", "Righteous, man!"],
        "d": 1
    },
    {
        "q": "What one-word catchphrase made Joey Russo (Joey Lawrence) a 1990s teen culture phenomenon on Blossom?",
        "correct": "Whoa!",
        "distractors": ["Dude!", "Yeah!", "Bummer!"],
        "d": 1
    },
    {
        "q": "What chorus of dismissal greeted intrusive neighbor Roger Evans whenever he walked into the Campbell house on Sister, Sister?",
        "correct": "Go home, Roger!",
        "distractors": ["Beat it, Roger!", "Get out, Roger!", "Later, Roger!"],
        "d": 1
    },
    {
        "q": "What catchphrase accompanied Hank Kingsley's double finger-guns and booming self-promotion on The Larry Sanders Show?",
        "correct": "Hey now!",
        "distractors": ["Look out!", "Here we go!", "Alright now!"],
        "d": 1
    },
    {
        "q": "What was Baby Sinclair's favorite defiant shout before bashing Earl over the head with a saucepan on Dinosaurs?",
        "correct": "Not the mama!",
        "distractors": ["Bad daddy!", "Go away, fat man!", "You're not the boss!"],
        "d": 1
    },
    {
        "q": "What was Frank Barone's cynical, armchair-bound catchphrase of disgust on Everybody Loves Raymond?",
        "correct": "Holy crap!",
        "distractors": ["What a crock!", "For crying out loud!", "Shut up already!"],
        "d": 1
    },
    {
        "q": "What enthusiastic three-word exclamation did Synclaire James utter whenever she was excited on Living Single?",
        "correct": "Woo woo woo!",
        "distractors": ["Yeah yeah yeah!", "Oh boy oh!", "Cha-ching baby!"],
        "d": 1
    },
    {
        "q": "What dismissive command did Martin Payne give whenever someone annoyed him and needed to leave on Martin?",
        "correct": "Get ta steppin'!",
        "distractors": ["Hit the curb!", "Take a hike!", "Bounce on out!"],
        "d": 1
    },
    {
        "q": "What shocked phrase did Martin Payne repeatedly shout at his girlfriend Gina on Martin?",
        "correct": "Damn, Gina!",
        "distractors": ["Gina, please!", "Stop it, Gina!", "Lord have mercy, Gina!"],
        "d": 1
    },
    {
        "q": "What rhythmic call did Eric Matthews invent to summon his neighbor and teacher across the backyard on Boy Meets World?",
        "correct": "Fee-fee-fee-feeny! Feeny!",
        "distractors": ["Mister Fee-nay! Oh Feeny!", "Hey there Feeny-man!", "Yoo-hoo, Professor!"],
        "d": 1
    },
    {
        "q": "What was Bruh Man's signature explanation whenever Martin caught him crawling through the window and raiding the fridge?",
        "correct": "Just chillin'!",
        "distractors": ["Just lookin'!", "Need a bite!", "Passin' through!"],
        "d": 1
    },
    {
        "q": "What was Frasier Crane's signature sign-off catchphrase at the end of each radio broadcast?",
        "correct": "Good night, Seattle, and good mental health",
        "distractors": ["May peace be with your minds, Seattle", "Stay balanced, Seattle, and stay calm", "Seattle, you have been heard"],
        "d": 1
    },
    {
        "q": "What was Sheneneh Jenkins' loud, flamboyant exclamation of astonishment on Martin?",
        "correct": "Oh my goooooodness!",
        "distractors": ["Child, please!", "Hold up now!", "Ain't no way!"],
        "d": 1
    },
    {
        "q": "What catchphrase did Al Borland use on Tool Time to gently warn Tim that his plan was catastrophic?",
        "correct": "I don't think so, Tim",
        "distractors": ["That's not safe, Tim", "Hold on there, Tim", "Check the manual, Tim"],
        "d": 1
    },
    {
        "q": "What phrase did Jerry Seinfeld's father Morty use whenever someone attempted to pay for dinner?",
        "correct": "You're not paying for this! My money is no good here?!",
        "distractors": ["Put that wallet away or I'll break your hand!", "I am the father, I pay the bill!", "Don't insult me in a public diner!"],
        "d": 2
    },
    {
        "q": "What catchphrase did Mimi Bobeck scream at Drew Carey across the cosmetic counter on The Drew Carey Show?",
        "correct": "Pig!",
        "distractors": ["Lardo!", "Loser!", "Toad!"],
        "d": 1
    },

    # Legendary Sitcom Episodes & Plot Disasters (25 questions)
    {
        "q": "In Seinfeld's Emmy-winning episode 'The Contest', who is the first person in the group to cave and forfeit the bet?",
        "correct": "Kramer (after seeing a naked woman in the window across the street)",
        "distractors": ["George (after visiting his mother in the hospital)", "Elaine (after taking an aerobics class with JFK Jr.)", "Jerry (after dating a virgin)"],
        "d": 1
    },
    {
        "q": "In 'The Marine Biologist', what object did Kramer hit into the ocean that became lodged inside the beached whale's blowhole?",
        "correct": "A Titleist golf ball",
        "distractors": ["A tennis ball", "A plastic bottle", "A baseball"],
        "d": 1
    },
    {
        "q": "How does Elaine Benes finally destroy the strict business of the Soup Nazi in Season 7 of Seinfeld?",
        "correct": "She finds his secret written soup recipes in an antique armoire and threatens to publish them publicly",
        "distractors": ["She calls the city health inspector after finding a cockroach in the mulligatawny", "She organizes a mass picket line of banned customers outside his door", "She buys his lease from the landlord and evicts him to Argentina"],
        "d": 1
    },
    {
        "q": "In Friends' iconic episode 'The One with the Prom Video', what famous metaphor does Phoebe use to describe Ross and Rachel's eternal bond?",
        "correct": "She's his lobster!",
        "distractors": ["She's his anchor!", "They're two peas in a pod!", "They're written in the stars!"],
        "d": 1
    },
    {
        "q": "What is unique about the structure of the acclaimed Season 3 Friends episode 'The One Where No One's Ready'?",
        "correct": "It is a real-time bottle episode taking place entirely inside Monica and Rachel's living room over 22 minutes",
        "distractors": ["It contains zero spoken dialogue between the six characters", "It was filmed entirely on the streets of Greenwich Village", "It was shot in a single continuous camera take without any edits"],
        "d": 1
    },
    {
        "q": "In the Season 4 Friends episode 'The One with the Embryos', what high-stakes prize do the boys win from the girls in a trivia contest?",
        "correct": "Monica and Rachel's spacious two-bedroom apartment",
        "distractors": ["All of Rachel's designer clothes and shoes", "Permanent rights to the big couch at Central Perk", "Free dinners and laundry service for an entire year"],
        "d": 1
    },
    {
        "q": "What question causes Monica and Rachel to lose the trivia contest in 'The One with the Embryos'?",
        "correct": "What is Chandler Bing's actual job? (Rachel guesses 'A transponster!')",
        "distractors": ["What is Chandler's middle name?", "What is the name of Chandler's childhood imaginary friend?", "Where did Chandler go to high school?"],
        "d": 1
    },
    {
        "q": "In The Fresh Prince of Bel-Air episode 'Papa's Got a Brand New Excuse', what gift did Will's deadbeat father Lou bring him before leaving again?",
        "correct": "A cheap, hollow wooden sculpture of a cheetah",
        "distractors": ["A set of vintage Philadelphia Phillies baseball cards", "A leather basketball signed by Julius Erving", "A silver pocket watch that didn't work"],
        "d": 2
    },
    {
        "q": "In Season 5's dramatic Fresh Prince episode 'Bullets Over Bel-Air', what does Will discover Carlton has secretly bought for protection?",
        "correct": "A handgun",
        "distractors": ["A switchblade knife", "A pit bull puppy", "A set of brass knuckles"],
        "d": 1
    },
    {
        "q": "What disaster occurs on Home Improvement when Tim Taylor attempts to boost the horsepower of the family dishwasher?",
        "correct": "It shakes violently, explodes with steam, and shoots dinner plates through the kitchen cabinets",
        "distractors": ["It floods the entire ground floor with four feet of soapy foam", "It sets the dining room curtains on fire", "It drains the city municipal water reservoir"],
        "d": 1
    },
    {
        "q": "In the acclaimed Roseanne episode 'A Stash from the Past', where do Roseanne, Dan, and Jackie get high after finding old marijuana?",
        "correct": "Trapped inside the family bathroom, giggling while sitting in the bathtub",
        "distractors": ["Hidden inside Dan's drywalled garage under a drop cloth", "Up in the attic sorting through old high school yearbooks", "In the basement next to the broken washing machine"],
        "d": 2
    },
    {
        "q": "In the famous Season 4 episode of Family Matters, what vehicle does Steve Urkel accidentally crash directly into the Winslow living room?",
        "correct": "Carl's Chicago police squad car",
        "distractors": ["His own BMW Isetta", "A giant yellow school bus", "Rachel's catering delivery van"],
        "d": 2
    },
    {
        "q": "In the dramatic Season 4 Boy Meets World episode 'Cult Fiction', which charismatic cult leader brainwashes Shawn Hunter?",
        "correct": "Mr. Mack (leader of 'The Centre')",
        "distractors": ["Brother Joshua", "Father Thomas", "The Grand Prophet"],
        "d": 2
    },
    {
        "q": "In the classic Frasier farce 'The Innkeepers', what culinary disaster ruins Frasier and Niles' opening night at their new restaurant?",
        "correct": "An exploding cherries jubilee sets off the sprinkler system while the main chef walks out and Daphne drops eels",
        "distractors": ["Martin's dog Eddie eats the caviar and infects all the food with rabies", "A health inspector condemns the building while the Mayor is eating soup", "Frasier insults the head food critic on live television by accident"],
        "d": 2
    },
    {
        "q": "In Frasier's hilarious episode 'Ham Radio', what character does Niles play who ends up performing multiple murdered voices in Frasier's radio play?",
        "correct": "Hans the German butler, Thor, and several other characters after Frasier fires the cast",
        "distractors": ["The Inspector who solves the crime in the parlor", "The hysterical grieving widow", "The American detective from Chicago"],
        "d": 2
    },
    {
        "q": "In the Frasier episode 'The Ski Lodge', why is Frasier heartbroken at the end of the weekend despite a cabin full of romantic triangles?",
        "correct": "Everyone was chasing someone else, and nobody was chasing Frasier: 'I was the only one who didn't get any action!'",
        "distractors": ["He broke his leg on the bunny slope before getting to ski", "Maris bought the entire mountain and banned him from the lodge", "His vintage bottle of Bordeaux was consumed by Martin with beef jerky"],
        "d": 2
    },
    {
        "q": "In the Season 2 NewsRadio episode 'The Cane', what does anchor Bill McNeal do after stealing Dave Nelson's walking stick?",
        "correct": "He parades around the office mimicking a 19th-century dandy and performs tap-dancing routines to mock Dave",
        "distractors": ["He throws it out of the 14th-story window into traffic", "He snaps it in half over his knee during a live news broadcast", "He pawns it to buy a vintage cigarette lighter"],
        "d": 2
    },
    {
        "q": "What surreal Season 4 episode of NewsRadio transported the entire WNYX office staff onto a spacecraft in deep space?",
        "correct": "\"Space\"",
        "distractors": [
            "\"Cosmic WNYX\"",
            "\"Starship News\"",
            "\"Radio Galaxy\""
        ],
        "d": 2
    },
    {
        "q": "What disaster ruins Joe and Helen's highly anticipated wedding day in the Season 6 finale of Wings?",
        "correct": "Helen burns off half her hair with a curling iron and Joe gets stranded in a remote swamp",
        "distractors": ["The wedding plane crashes into the Nantucket sound", "Roy Biggins accidentally drinks the communion wine and brawls with the priest", "Lowell drives the wedding cake into the harbor"],
        "d": 2
    },
    {
        "q": "In a memorable episode of The Nanny, where do Fran and her mother Sylvia get trapped together overnight?",
        "correct": "Inside a commercial refrigerated meat freezer at a kosher butcher shop",
        "distractors": ["In the elevator of Bloomingdale's department store", "In the wine cellar of the Sheffield townhouse", "In the subway tunnel beneath 59th Street"],
        "d": 2
    },
    {
        "q": "In the Season 1 premiere of 3rd Rock from the Sun, what natural Earth weather phenomenon terrifies the alien Solomon family?",
        "correct": "A snowstorm, which they mistake for the sky disintegrating and attacking the planet",
        "distractors": ["A thunderstorm, which they believe is an orbital particle cannon", "A summer heatwave, which they fear is the Earth falling into the sun", "An earthquake, which they believe is a planetary self-destruct mechanism"],
        "d": 1
    },
    {
        "q": "In an elaborate episode of The Drew Carey Show, what cult musical movie do Drew and his friends perform against rival movie patrons in a theater line?",
        "correct": "The Rocky Horror Picture Show (performing 'Time Warp')",
        "distractors": ["Grease", "Little Shop of Horrors", "West Side Story"],
        "d": 2
    },
    {
        "q": "In the Season 8 episode of Seinfeld 'The Bizarro Jerry', what does Elaine discover about her new friend Kevin and his circle?",
        "correct": "They are the exact polar opposites of Jerry, George, and Kramer: polite, considerate, well-read, and generous",
        "distractors": ["They are secret millionaires who run an illegal gambling ring", "They are undercover FBI agents investigating Newman", "They are professional actors hired by Kramer to test her loyalty"],
        "d": 1
    },
    {
        "q": "What happens to George Costanza's fiancée Susan Ross at the end of Season 7 of Seinfeld?",
        "correct": "She dies from licking toxic glue on the cheap, bargain wedding invitations George insisted on buying",
        "distractors": ["She runs away to Paris with Jerry's dentist Dr. Tim Whatley", "She is killed in an elevator accident at NBC headquarters", "She discovers George's financial lies and leaves him at the altar"],
        "d": 1
    },
    {
        "q": "How did the four friends react at the hospital when the doctor announced Susan Ross had died in Seinfeld?",
        "correct": "With brief awkward pauses, lukewarm indifference, and an immediate proposal to go get coffee",
        "distractors": ["With hysterical weeping and uncontrollable guilt", "By demanding a malpractice investigation into the hospital", "By throwing a celebratory party in Jerry's apartment"],
        "d": 1
    },

    # Cultural Legacy, Smithsonian Artifacts & Lasting Impact (25 questions)
    {
        "q": "What iconic prop from Seinfeld was officially donated to the Smithsonian National Museum of American History in Washington D.C.?",
        "correct": "Jerry's original pirate-style 'Puffy Shirt'",
        "distractors": ["George Costanza's velvet tracksuit", "Kramer's lobster-patterned bowling shirt", "The original metal Festivus pole"],
        "d": 1
    },
    {
        "q": "What item of clothing worn by Jaleel White on Family Matters was requested for preservation by the Smithsonian Institution?",
        "correct": "Steve Urkel's signature red suspenders, saddle shoes, and oversized eyeglasses",
        "distractors": ["His silver transformation chamber suit", "Stefan Urquelle's black silk tuxedo", "His polka-dot high-water pants"],
        "d": 1
    },
    {
        "q": "In 2002, what magazine ranked Seinfeld as the #1 Greatest Television Show of All Time?",
        "correct": "TV Guide",
        "distractors": ["Rolling Stone", "Entertainment Weekly", "Time Magazine"],
        "d": 1
    },
    {
        "q": "What iconic layered hairstyle, created by stylist Chris McMillan in 1995, became an international salon craze copied by millions of women?",
        "correct": "'The Rachel' (worn by Jennifer Aniston on Friends)",
        "distractors": ["'The Monica'", "'The Topanga'", "'The Blossom'"],
        "d": 1
    },
    {
        "q": "What secular alternative holiday introduced on Seinfeld is celebrated annually by real-world fans on December 23rd?",
        "correct": "Festivus ('for the rest of us')",
        "distractors": ["Kramerica Day", "Vandelay Day", "Newmanalia"],
        "d": 1
    },
    {
        "q": "What two traditional rituals define the real-world celebration of Festivus?",
        "correct": "The 'Airing of Grievances' and the 'Feats of Strength'",
        "distractors": ["The Lighting of the Pole and the Drinking of the Rye", "The Exchange of Insults and the Breaking of the Bagel", "The Shouting of Complaints and the Wrestling of the Neighbor"],
        "d": 1
    },
    {
        "q": "Which relationship term, describing a platonic friendship where one person desires romance, was popularized by Joey Tribbiani on Friends in 1994?",
        "correct": "The 'Friend Zone'",
        "distractors": ["Ghosting", "Catfishing", "Breadcrumbing"],
        "d": 1
    },
    {
        "q": "Which of the following common English idioms was popularized and entered mainstream culture directly through Seinfeld?",
        "correct": "Double-dipping (a chip)",
        "distractors": ["Bite the bullet", "Spill the tea", "Throw shade"],
        "d": 1
    },
    {
        "q": "What video game franchise sparked a high-profile copyright lawsuit from Alfonso Ribeiro over its unlicensed use of the 'Carlton Dance'?",
        "correct": "Fortnite (developed by Epic Games)",
        "distractors": ["Call of Duty", "Grand Theft Auto", "Overwatch"],
        "d": 1
    },
    {
        "q": "In 2012, which U.S. political leader credited Will & Grace with doing more to educate the American public on LGBTQ+ rights than almost anything else?",
        "correct": "Vice President Joe Biden (on Meet the Press)",
        "distractors": ["President Barack Obama", "Secretary of State Hillary Clinton", "Senator Bernie Sanders"],
        "d": 1
    },
    {
        "q": "Which Netflix revival series debuted in 2016, reuniting the Tanner family and running for five successful seasons?",
        "correct": "Fuller House",
        "distractors": ["Fullest House", "Full House Returns", "The Tanners of San Francisco"],
        "d": 1
    },
    {
        "q": "Which Disney Channel sequel series debuted in 2014, continuing the story of Cory and Topanga Matthews raising their own daughter in New York?",
        "correct": "Girl Meets World",
        "distractors": ["Boy Meets Family", "The Matthews Legacy", "Feeny's World"],
        "d": 1
    },
    {
        "q": "What happened to the smash-hit 2018 revival of Roseanne after star Roseanne Barr posted a racist tweet about Valerie Jarrett?",
        "correct": "ABC immediately cancelled the show, fired Barr, and retooled the series without her as The Conners",
        "distractors": ["ABC suspended the show for one year before bringing it back with a co-star", "The series moved to Fox with the entire original cast intact", "The cast walked out in protest and the show was permanently buried"],
        "d": 1
    },
    {
        "q": "Which streaming giant acquired global streaming rights to Seinfeld in 2019 in a blockbuster deal reported at over $500 million?",
        "correct": "Netflix",
        "distractors": ["Hulu", "Amazon Prime Video", "Max (HBO Max)"],
        "d": 1
    },
    {
        "q": "Which classic 90s sitcom returned in 2023 for a new revival series on Paramount+, following the title character moving back to Boston?",
        "correct": "Frasier",
        "distractors": ["Wings", "NewsRadio", "Mad About You"],
        "d": 1
    },
    {
        "q": "Which nostalgic sitcom debuted in 1998, capturing 1970s teenage suburban life and launching the careers of Ashton Kutcher and Mila Kunis?",
        "correct": "That '70s Show",
        "distractors": ["Freaks and Geeks", "Dazed and Confused (the series)", "Groovy Times"],
        "d": 1
    },
    {
        "q": "What critically acclaimed animated sitcom created by Mike Judge and Greg Daniels debuted on Fox in 1997, depicting everyday life in Arlen, Texas?",
        "correct": "King of the Hill",
        "distractors": ["The Goode Family", "Beavis and Butt-Head", "South Park"],
        "d": 1
    },
    {
        "q": "What landmark comedy distinction did Everybody Loves Raymond achieve in its later seasons, winning the top prize in 2003 and 2005?",
        "correct": "The Primetime Emmy Award for Outstanding Comedy Series",
        "distractors": ["The Golden Globe for Best Drama Series", "The Peabody Award for Investigative Comedy", "The Television Critics Association Heritage Award"],
        "d": 2
    },
    {
        "q": "Which cable network block became a cultural late-night sanctuary in the 1990s and 2000s by acquiring rerun rights to 90s sitcom classics?",
        "correct": "Nick at Nite (and later TV Land)",
        "distractors": ["Comedy Central After Dark", "USA Up All Night", "TBS Very Funny Late Night"],
        "d": 1
    },
    {
        "q": "What major technological shift in television production began to replace the dominant multi-camera live-audience format in the early 2000s?",
        "correct": "The single-camera cinematic format with no studio audience or laugh track (e.g., Malcolm in the Middle, Scrubs, Arrested Development)",
        "distractors": ["CGI virtual soundstages using green-screen backgrounds exclusively", "Animated live-action motion capture sitcoms", "Improvised webisodes broadcast exclusively via broadband"],
        "d": 2
    },
    {
        "q": "What teen magazine frequently featured Jonathan Taylor Thomas on its cover during his mid-90s Home Improvement peak?",
        "correct": "Tiger Beat (and BOP Magazine)",
        "distractors": ["Seventeen", "YM", "Rolling Stone"],
        "d": 1
    },
    {
        "q": "What phrase did Seinfeld popularize to describe someone who invades personal physical space while talking?",
        "correct": "A 'Close-talker'",
        "distractors": ["A 'Space-invader'", "A 'Breath-blower'", "A 'Nose-to-noser'"],
        "d": 1
    },
    {
        "q": "What term did Elaine Benes coin on Seinfeld to describe an item of contraception worthy of intimacy?",
        "correct": "'Sponge-worthy'",
        "distractors": ["'Date-worthy'", "'Gold-standard'", "'Pass-worthy'"],
        "d": 1
    },
    {
        "q": "What word did Seinfeld introduce into the national vocabulary for giving away a previously received gift to someone else?",
        "correct": "\"Regifting\"",
        "distractors": [
            "\"Recycling\"",
            "\"Re-wrapping\"",
            "\"Re-bestowing\""
        ],
        "d": 1
    },
    {
        "q": "Why is the 1990s universally celebrated by television historians as the zenith of the traditional American sitcom?",
        "correct": "It combined record-setting live network viewership (over 30-70 million viewers per episode) with peak cultural ubiquity and immense talent before media fragmentation",
        "distractors": ["It was the only decade where government subsidies funded sitcom writing rooms", "All sitcoms were broadcast globally in 40 languages simultaneously", "Every single 1990s sitcom ran for a minimum of ten seasons without cancellation"],
        "d": 1
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "staging", "90s_sitcoms_batch10.json")
    make_batch(q_batch10, 10, out)
