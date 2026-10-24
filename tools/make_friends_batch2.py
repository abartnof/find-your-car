#!/usr/bin/env python3
"""
Generate tools/staging/friends_batch2.json (100 questions, Seasons 4-6 Textual).
"""
import sys
import os

from build_friends_batch import build_batch

questions = [
    {
        "q": "In the Season 4 premiere, what bodily fluid remedy does Joey propose to treat Monica's painful jellyfish sting at the beach?",
        "correct": "Urine",
        "distractors": ["Salt water", "Vinegar", "Baking soda paste"],
        "d": 1
    },
    {
        "q": "How many pages long was Rachel's handwritten letter to Ross at the beach house, written 'front and back'?",
        "correct": "18 pages",
        "distractors": ["12 pages", "24 pages", "8 pages"],
        "d": 1
    },
    {
        "q": "What memorable retort does Ross shout when Rachel insists that premature performance issues happen to every guy?",
        "correct": "\"It DOES NOT happen to every guy, and it IS a big deal!\"",
        "distractors": ["\"I was tired, Rachel!\"", "\"Nobody talks about this!\"", "\"That was one time!\""],
        "d": 1
    },
    {
        "q": "In 'The One with the Cat', whose reincarnated spirit does Phoebe wholeheartedly believe inhabits a stray feline?",
        "correct": "Her adoptive mother Lily Buffay",
        "distractors": ["Her grandmother Althea", "Her childhood pet guinea pig", "Her twin sister Ursula's former cat"],
        "d": 2
    },
    {
        "q": "In 'The One with the 'Cuffs', who handcuffs Chandler to an office filing cabinet without his pants on?",
        "correct": "Joanna, Rachel's Bloomingdale's boss",
        "distractors": ["Janice", "Kathy", "Sophie"],
        "d": 2
    },
    {
        "q": "Why does Joey learn ballroom dancing with building superintendent Mr. Treeger in Season 4?",
        "correct": "To prevent Mr. Treeger from evicting Rachel and Monica for illegal subletting",
        "distractors": ["To audition for a Broadway dance ensemble", "To win a neighborhood charity competition", "To impress a dancer he met at Central Perk"],
        "d": 2
    },
    {
        "q": "What is the name of the aspiring actress who dates Joey before developing mutual romantic feelings with Chandler?",
        "correct": "Kathy",
        "distractors": ["Janine", "Cheryl", "Ginger"],
        "d": 1
    },
    {
        "q": "What horrifying condition defines the apartment of Cheryl, the gorgeous paleontologist Ross dates in Season 4?",
        "correct": "It is covered in rotting trash, old food, and pests",
        "distractors": ["It is packed with live tarantulas and snakes", "It is completely painted neon orange with blaring rock music", "It has no furniture except for a velvet coffin"],
        "d": 2
    },
    {
        "q": "What punishment does Chandler voluntarily endure on Thanksgiving in Season 4 to earn Joey's forgiveness for kissing Kathy?",
        "correct": "Remaining locked silently inside a wooden shipping crate for hours",
        "distractors": ["Handing over his BarcaLounger recliner permanently", "Eating an entire raw Thanksgiving onion", "Doing Joey's laundry and dishes for six months"],
        "d": 1
    },
    {
        "q": "In 'The One with Chandler in a Box', why does Monica wear a pirate-style eyepatch during Thanksgiving dinner?",
        "correct": "She got ice in her eye and was treated by Richard's handsome son Timothy",
        "distractors": ["She scratched her cornea on a dried turkey wishbone", "She had an allergic reaction to onion steam", "She poked herself with a chopstick"],
        "d": 2
    },
    {
        "q": "In the famous apartment trivia contest in 'The One with the Embryos', who serves as the quizmaster and question creator?",
        "correct": "Ross",
        "distractors": ["Chandler", "Gunther", "Phoebe"],
        "d": 1
    },
    {
        "q": "According to the apartment trivia game, what is Monica's biggest pet peeve?",
        "correct": "Animals dressed as humans",
        "distractors": ["Dirty sponges in the sink", "Unfolded cloth napkins", "Loud chewing at the dinner table"],
        "d": 2
    },
    {
        "q": "In the apartment quiz, what was the title of the homemade comic book Ross created as a boy?",
        "correct": "'Science Boy'",
        "distractors": ["'Dino Boy'", "'Captain Fossil'", "'Geology Kid'"],
        "d": 2
    },
    {
        "q": "In the trivia showdown, what towel category does Monica have that brings her total number of towel categories to 11?",
        "correct": "\"Everyday use\"",
        "distractors": ["\"Guests only\"", "\"Kitchen cleanup\"", "\"Fancy display\""],
        "d": 3
    },
    {
        "q": "What incorrect fabricated occupation does Rachel shout out when trying to identify Chandler's actual job in the lightning round?",
        "correct": "\"Transponster\"",
        "distractors": ["\"Actuary\"", "\"Accountant\"", "\"Data Analyzer\""],
        "d": 1
    },
    {
        "q": "What is Chandler Bing's actual job field during the first several seasons before his career change?",
        "correct": "Statistical analysis and data reconfiguration",
        "distractors": ["Investment banking and derivatives trading", "Corporate human resources compliance", "Public relations and communications"],
        "d": 1
    },
    {
        "q": "What prize do Chandler and Joey win from Monica and Rachel at the conclusion of the apartment trivia contest?",
        "correct": "Monica and Rachel's spacious two-bedroom apartment",
        "distractors": ["Knicks courtside season tickets", "A year of free home-cooked dinners", "Their vintage ceramic white dog statue"],
        "d": 1
    },
    {
        "q": "What is the name of the handsome personal shopping client Rachel develops a massive crush on in Season 4?",
        "correct": "Joshua Burgin",
        "distractors": ["Mark Robinson", "Tag Jones", "Gavin Mitchell"],
        "d": 2
    },
    {
        "q": "What cheerleader uniform from Lincoln High does Rachel wear to a fake party in an attempt to seduce Joshua?",
        "correct": "Her high school cheerleading uniform",
        "distractors": ["A French maid costume", "A sailor dance costume", "Her high school prom dress"],
        "d": 2
    },
    {
        "q": "What free unscrambled cable television broadcast do Chandler and Joey refuse to turn off for days in Season 4?",
        "correct": "Adult pornography channel",
        "distractors": ["All-day action movie marathon", "International soccer pay-per-view", "Continuous music video channel"],
        "d": 2
    },
    {
        "q": "What is the full name of Ross's British fiancée whom he meets in Season 4?",
        "correct": "Emily Waltham",
        "distractors": ["Emily Sheffield", "Emily Winchester", "Emily Kensington"],
        "d": 1
    },
    {
        "q": "How do Monica and Rachel finally win their original apartment back from Chandler and Joey in 'The One with the Haste'?",
        "correct": "They move all their belongings back while the guys are away at a Knicks game",
        "distractors": ["They beat the guys in a rematch trivia competition", "They pay the guys two thousand dollars in cash", "They bribe Mr. Treeger to void the guys' lease"],
        "d": 2
    },
    {
        "q": "In 'The One with All the Wedding Dresses', which three women sit together on the sofa dressed in wedding gowns drinking beer?",
        "correct": "Monica, Phoebe, and Rachel",
        "distractors": ["Monica, Rachel, and Carol", "Monica, Phoebe, and Emily", "Rachel, Phoebe, and Janice"],
        "d": 1
    },
    {
        "q": "Why does Joshua abruptly end his relationship with Rachel in Season 4?",
        "correct": "Rachel impulsively suggests that they get married right away",
        "distractors": ["Rachel confesses that she is still in love with Ross", "Joshua catches Rachel wearing Emily's wedding dress", "Joshua's parents object to Rachel's career"],
        "d": 2
    },
    {
        "q": "Which British royal family member makes a cameo appearance interacting with Joey on video in London?",
        "correct": "Sarah, Duchess of York",
        "distractors": ["Princess Anne", "Princess Margaret", "Diana, Princess of Wales"],
        "d": 2
    },
    {
        "q": "Which billionaire founder of Virgin Atlantic makes a cameo selling London tourist hats to Joey and Chandler?",
        "correct": "Richard Branson",
        "distractors": ["Elon Musk", "Rupert Murdoch", "Ted Turner"],
        "d": 2
    },
    {
        "q": "Which British actor sits next to Rachel on the flight to London and tells her she is a terrible person for planning to ruin Ross's wedding?",
        "correct": "Hugh Laurie",
        "distractors": ["Stephen Fry", "Colin Firth", "Rowan Atkinson"],
        "d": 1
    },
    {
        "q": "What mistaken assumption by a London wedding guest causes Monica to spiral into emotional distress before sleeping with Chandler?",
        "correct": "The guest mistakenly assumes Monica is Ross's mother",
        "distractors": ["The guest asks if Monica is pregnant", "The guest thinks Monica is a catering waitress", "The guest tells Monica she will never find a husband"],
        "d": 2
    },
    {
        "q": "What shocking name does Ross say during his wedding vows to Emily at the altar in the Season 4 finale?",
        "correct": "\"Rachel\"",
        "distractors": ["\"Carol\"", "\"Susan\"", "\"Janice\""],
        "d": 1
    },
    {
        "q": "How does Emily escape from the wedding reception after Ross's disastrous blunder at the altar?",
        "correct": "She climbs out through a high bathroom window",
        "distractors": ["She speeds away in a vintage London black cab", "She runs out the kitchen fire exit into the alley", "She hides in her parents' hotel room"],
        "d": 2
    },
    {
        "q": "How does Chandler attempt to cover up accidentally kissing Monica in front of Rachel and Phoebe in early Season 5?",
        "correct": "He kisses Rachel and Phoebe on the lips as well, claiming it is a European greeting",
        "distractors": ["He pretends he tripped and fell forward onto Monica", "He claims he was performing a magic trick", "He says he mistook Monica for Joey in the dark"],
        "d": 1
    },
    {
        "q": "What are the names of the triplets born to Phoebe as a gestational surrogate for her brother Frank Jr. and Alice?",
        "correct": "Frank Jr. Jr., Leslie, and Chandler",
        "distractors": ["Frank Jr. Jr., Lily, and Joey", "Frankie, Mary, and Chandler", "Jack, Leslie, and Ross"],
        "d": 2
    },
    {
        "q": "In 'The One with the Triplets', what 1970s TV character is Phoebe's delivering obstetrician Dr. Harad obsessed with?",
        "correct": "Arthur Fonzarelli (\"The Fonz\") from 'Happy Days'",
        "distractors": ["Captain James T. Kirk from 'Star Trek'", "Kojak from 'Kojak'", "Hawkeye Pierce from 'M*A*S*H'"],
        "d": 2
    },
    {
        "q": "Why does Phoebe harbor a longstanding grudge against PBS in 'The One Where Phoebe Hates PBS'?",
        "correct": "Her mother died shortly after Sesame Street wrote a letter that made her cry",
        "distractors": ["Phoebe sent a donation and never received her promised tote bag", "PBS canceled her favorite children's puppet show", "Phoebe failed an audition to appear on Mister Rogers' Neighborhood"],
        "d": 3
    },
    {
        "q": "How does Joey first deduce that Chandler and Monica are secretly romantically involved in Season 5?",
        "correct": "He connects Monica leaving an eyelash curler in a hotel room with Chandler hunting for one",
        "distractors": ["He finds Monica's silk scarf tucked under Chandler's pillow", "He overhears them whispering on the fire escape", "He sees matching hotel keys in both of their jackets"],
        "d": 2
    },
    {
        "q": "In 'The One with the Yeti', what do Rachel and Monica spray at their bearded neighbor Danny in the dark basement?",
        "correct": "Insect fogger bug spray",
        "distractors": ["Pepper spray", "A fire extinguisher", "WD-40 lubricant"],
        "d": 2
    },
    {
        "q": "In 'The One with All the Thanksgivings', what bodily injury did Chandler suffer during Thanksgiving 1988 after calling Monica fat?",
        "correct": "Monica accidentally dropped a kitchen knife that severed the tip of his toe",
        "distractors": ["He slipped on butter and dislocated his left elbow", "A frozen turkey slid off the counter and broke his foot", "Monica slammed a pantry door shut on his fingers"],
        "d": 1
    },
    {
        "q": "What object does Monica wear on her head while dancing to cheer up Chandler on Thanksgiving in Season 5?",
        "correct": "A raw turkey wearing oversized sunglasses and a fez",
        "distractors": ["A hollowed-out pumpkin with candle holes", "A pilgrim hat made of construction paper", "A metal colander with dangling cranberry vines"],
        "d": 1
    },
    {
        "q": "What landmark emotional phrase does Chandler slip and utter for the first time while watching Monica dance with the turkey?",
        "correct": "\"I love you\"",
        "distractors": ["\"Marry me\"", "\"You are beautiful\"", "\"You are my best friend\""],
        "d": 1
    },
    {
        "q": "What was the special ingredient in Monica's leftover Thanksgiving turkey sandwich that Ross treasured?",
        "correct": "\"The Moist Maker\" (an extra slice of gravy-soaked bread in the middle)",
        "distractors": ["\"The Turkey Glaze\" (homemade cranberry reduction)", "\"The Crunch Layer\" (crispy stuffing baked twice)", "\"The Butter Dip\" (herb-infused melted butter spread)"],
        "d": 1
    },
    {
        "q": "What furious phrase does Ross scream across the museum courtyard when his boss confesses to eating Ross's leftover sandwich?",
        "correct": "\"MY SANDWICH?!\"",
        "distractors": ["\"YOU ATE IT?!\"", "\"THAT WAS MINE!\"", "\"HOW COULD YOU!\""],
        "d": 1
    },
    {
        "q": "What tight apparel piece causes Ross agony and embarrassment on a date in 'The One with All the Resolutions'?",
        "correct": "Black leather pants",
        "distractors": ["A tight velvet turtleneck", "Skin-tight denim overalls", "A latex muscle shirt"],
        "d": 1
    },
    {
        "q": "What paste-like mess forms on Ross's legs in his date's bathroom when he attempts to lubricate his tight leather pants?",
        "correct": "A sticky paste of body lotion and baby powder",
        "distractors": ["A gooey mixture of conditioner and bath salts", "A slippery blend of olive oil and flour", "A congealed film of hand soap and talcum"],
        "d": 2
    },
    {
        "q": "What fashionable men's accessory does Joey proudly carry around town, claiming 'It's unisex!' and 'European!'?",
        "correct": "A shoulder strap man-purse",
        "distractors": ["A leather fanny pack", "A silk pocket ascot", "A wool beret"],
        "d": 1
    },
    {
        "q": "What words does Phoebe scream in horror when she looks through the window and catches Chandler and Monica together?",
        "correct": "\"CHANDLER AND MONICA! CHANDLER AND MONICA! MY EYES! MY EYES!\"",
        "distractors": ["\"OH MY GOD! THEY'RE KISSING! CALL THE POLICE!\"", "\"WHAT ARE YOU DOING?! STOP IT RIGHT NOW!\"", "\"I CANNOT BELIEVE THIS! CHANDLER IS NAKED!\""],
        "d": 1
    },
    {
        "q": "In 'The One Where Everybody Finds Out', what do Phoebe and Chandler do to force the other to confess the secret relationship?",
        "correct": "They engage in an elaborate, awkward fake romantic seduction of each other",
        "distractors": ["They take polygraph lie-detector tests administered by Joey", "They hold a staged mock trial in Monica's living room", "They auction off Chandler's apartment keys"],
        "d": 2
    },
    {
        "q": "What physical habit makes Katie, the girl Joey dates in Season 5, unbearable for him?",
        "correct": "She constantly punches him hard on the arm when laughing",
        "distractors": ["She bites his earlobes during normal conversations", "She steps aggressively on his toes whenever excited", "She headbutts his shoulder as an affectionate greeting"],
        "d": 2
    },
    {
        "q": "What object does Phoebe discover under a cushion at Central Perk that leads her to meet police officer Gary?",
        "correct": "A NYPD police detective badge",
        "distractors": ["A police service revolver", "A pair of department handcuffs", "A traffic citation book"],
        "d": 2
    },
    {
        "q": "Which actor portrayed police officer Gary, who moves in with Phoebe in Season 5 before shooting a bird?",
        "correct": "Michael Rapaport",
        "distractors": ["Hank Azaria", "Jon Favreau", "Dermot Mulroney"],
        "d": 1
    },
    {
        "q": "Why does Phoebe abruptly break up with Gary the morning after they move into an apartment together?",
        "correct": "He shoots a chirping bird on the windowsill with his service gun from bed",
        "distractors": ["He reveals that he has a secret wife and three children", "He handcuffs Phoebe to the radiator as a joke", "He arrests Ross for jaywalking outside the deli"],
        "d": 1
    },
    {
        "q": "In 'The One with the Ball', what game do Joey, Ross, Chandler, and Monica play continuously for hours without stopping?",
        "correct": "Throwing a small rubber ball back and forth without letting it touch the ground",
        "distractors": ["Bouncing a ping-pong ball on a paddle", "Balancing an egg on a soup spoon", "Keeping a hacky sack airborne in the living room"],
        "d": 2
    },
    {
        "q": "In 'The One with the Ride-Along', why does Joey throw his body across Chandler when a car backfire sounds like a gunshot?",
        "correct": "He was trying to shield his delicious meatball sandwich from damage",
        "distractors": ["He instinctively reacted to save Chandler's life", "He tripped over the squad car seatbelt latch", "He thought the shooter was aiming for his leather jacket"],
        "d": 1
    },
    {
        "q": "What job does Joey end up doing at Caesar's Palace in Las Vegas after his indie movie production runs out of funds?",
        "correct": "Dressing as a Roman gladiator and posing with tourists",
        "distractors": ["Dealing twenty-one at the high-stakes blackjack table", "Serving cocktails poolside in Roman togas", "Operating the hotel casino luggage carousel"],
        "d": 2
    },
    {
        "q": "What bizarre match does Joey believe he discovers at the casino in the Season 5 Vegas finale?",
        "correct": "His identical hand twin",
        "distractors": ["His identical foot twin", "His long-lost biological brother", "His vocal voiceover twin"],
        "d": 1
    },
    {
        "q": "Which actor played the Vegas casino card dealer whom Joey harasses about being his 'identical hand twin'?",
        "correct": "Thomas Lennon",
        "distractors": ["Paul Rudd", "Adam Goldberg", "Jim Rash"],
        "d": 2
    },
    {
        "q": "What vandalism does Ross draw onto Rachel's face with permanent ink while drinking on the flight to Las Vegas?",
        "correct": "A black mustache and full beard",
        "distractors": ["Cat whiskers and a blackened nose", "A giant black unibrow and devil horns", "Glasses and fake vampire fangs"],
        "d": 1
    },
    {
        "q": "What shocking event occurs at the end of the Season 5 finale inside a 24-hour Las Vegas wedding chapel?",
        "correct": "Ross and Rachel stumble out intoxicated having just gotten legally married",
        "distractors": ["Monica and Chandler secretly exchange marriage vows", "Phoebe marries a casino pit boss for free buffet passes", "Joey marries an elderly tourist from Idaho"],
        "d": 1
    },
    {
        "q": "Why does Ross falsely tell Rachel in early Season 6 that he took care of their Las Vegas marriage annulment?",
        "correct": "He refuses to become known as 'the three-divorce guy'",
        "distractors": ["He hopes that Rachel will secretly fall back in love with him", "He lost the court filing paperwork on the subway", "The Nevada courthouse was closed for renovation"],
        "d": 1
    },
    {
        "q": "What medical condition does Joey suffer from in Season 6 right when his Screen Actors Guild health insurance lapses?",
        "correct": "A painful hernia",
        "distractors": ["Kidney stones", "A dislocated shoulder", "Acute appendicitis"],
        "d": 2
    },
    {
        "q": "In 'The One with Joey's Porsche', how does Joey capitalize on finding the lost keys to an expensive sports car?",
        "correct": "He washes the parked Porsche and wears matching Porsche merchandise to impress passersby",
        "distractors": ["He takes the car on high-speed joyrides down Broadway", "He rents the vehicle to tourists for photo shoots", "He enters the car in an illegal street race in Brooklyn"],
        "d": 2
    },
    {
        "q": "In 'The One on the Last Night', what fictional gambling card game does Chandler invent to secretly give Joey money?",
        "correct": "\"Cups\"",
        "distractors": ["\"Triangles\"", "\"Double Blackjack\"", "\"Royal Flush 500\""],
        "d": 2
    },
    {
        "q": "Why is Rachel mortified to go jogging with Phoebe through Central Park in Season 6?",
        "correct": "Phoebe runs wildly with flailing arms and legs like a startled colt",
        "distractors": ["Phoebe wears bright neon spandex and sings show tunes loudly", "Phoebe stops to pet every single dog and horse in the park", "Phoebe runs completely barefoot while challenging strangers to sprints"],
        "d": 1
    },
    {
        "q": "What cosmetic disaster befalls Ross before his date with Hillary in 'The One with Ross's Teeth'?",
        "correct": "He leaves whitening gel on so long his teeth glow neon white under blacklight",
        "distractors": ["His gums turn completely blue from expired dental rinse", "Two of his front veneers fall out into his clam chowder", "His dental trays stick to his lips and leave blisters"],
        "d": 1
    },
    {
        "q": "What catalog home-furnishings retailer does Rachel obsess over while lying to Phoebe that her furniture is authentic antique flea-market finds?",
        "correct": "Pottery Barn",
        "distractors": ["Crate & Barrel", "Restoration Hardware", "Williams-Sonoma"],
        "d": 1
    },
    {
        "q": "What specific item from Pottery Barn do both Rachel and Ross purchase, claiming it came from the days of yore?",
        "correct": "An apothecary table",
        "distractors": ["A mah-jongg sideboard", "A grandfather clock", "A rolled-arm club chair"],
        "d": 2
    },
    {
        "q": "What choreographed high school dance do Monica and Ross resurrect to get featured on camera during 'Dick Clark's New Year's Rockin' Eve'?",
        "correct": "\"The Routine\"",
        "distractors": ["\"The Geller Hustle\"", "\"The Long Island Shimmy\"", "\"The Sibling Twist\""],
        "d": 1
    },
    {
        "q": "What Australian supermodel portrayed Janine Lecroix, Joey's dancer roommate and short-term romantic interest in Season 6?",
        "correct": "Elle Macpherson",
        "distractors": ["Claudia Schiffer", "Kylie Minogue", "Rachel Hunter"],
        "d": 2
    },
    {
        "q": "Why do Joey and Janine break up after attending Dick Clark's New Year's Eve broadcast together?",
        "correct": "Janine cannot stand spending time with Monica and Chandler",
        "distractors": ["Janine lands a permanent dance gig in London", "Joey catches Janine eating his favorite sandwich", "Janine refuses to let Joey watch Days of Our Lives"],
        "d": 2
    },
    {
        "q": "What Japanese concept of total situational awareness does Ross claim to possess in 'The One with Unagi'?",
        "correct": "Unagi",
        "distractors": ["Sashimi", "Wasabi", "Karate-do"],
        "d": 1
    },
    {
        "q": "What do Phoebe and Rachel repeatedly tell Ross that 'unagi' actually is?",
        "correct": "A freshwater eel used in sushi",
        "distractors": ["A fermented soybean paste", "A steamed octopus dumpling", "A spicy seaweed salad"],
        "d": 1
    },
    {
        "q": "What culinary disaster does Rachel create on Thanksgiving in Season 6 after pages of her cookbook stick together?",
        "correct": "An English trifle combined with a shepherd's pie (beef, peas, onions, custard, jam)",
        "distractors": ["A pumpkin pie filled with tuna and scallions", "A cranberry tart layered with clam chowder", "A bread pudding stuffed with turkey giblets"],
        "d": 1
    },
    {
        "q": "What famous reaction quote does Joey give when eating Rachel's bizarre beef-and-custard Thanksgiving dessert?",
        "correct": "\"What's not to like? Custard, good. Jam, good. Meat, GOOD!\"",
        "distractors": ["\"It tastes like feet, but I'll eat it anyway!\"", "\"This is the best holiday dinner ever!\"", "\"More whipped cream and ground beef, please!\""],
        "d": 1
    },
    {
        "q": "What confession does Judy Geller blurt out during the chaotic Thanksgiving dinner argument in Season 6?",
        "correct": "She confesses that Jack and Judy always loved Ross more than Monica",
        "distractors": ["She admits she never wanted to buy Monica a car", "She confesses that she burned the kitchen curtains on purpose", "She reveals that Ross was not accepted into medical school"],
        "d": 2
    },
    {
        "q": "What secret about Chandler smoking in college led Jack and Judy Geller to dislike him for years?",
        "correct": "Ross blamed the smell of marijuana in his college bedroom on Chandler",
        "distractors": ["Chandler accidentally backed his car into Jack's boat", "Chandler broke Judy's heirloom punch bowl at graduation", "Chandler spilled red wine all over Judy's white carpet"],
        "d": 2
    },
    {
        "q": "In 'The One Where Chandler Can't Cry', what adult entertainment revelation does Joey make about Ursula Buffay?",
        "correct": "Ursula is starring in adult pornographic films using the stage name 'Phoebe Buffay'",
        "distractors": ["Ursula is working as an exotic dancer in Atlantic City", "Ursula is appearing in risqué swimsuit calendars", "Ursula runs a telephone psychic hotline"],
        "d": 2
    },
    {
        "q": "What movie finally causes Chandler to break down and cry like a baby in Season 6?",
        "correct": "Ross and Monica telling him that Ross and Rachel belong together",
        "distractors": ["'Old Yeller'", "'Bambi'", "'Terms of Endearment'"],
        "d": 3
    },
    {
        "q": "In the two-part alternate reality episode 'The One That Could Have Been', what career does Phoebe hold?",
        "correct": "A hard-charging, chain-smoking Wall Street stockbroker",
        "distractors": ["A world-touring folk-pop superstar", "A high school guidance counselor", "A corporate marketing director"],
        "d": 2
    },
    {
        "q": "In 'The One That Could Have Been', who is Ross still unhappily married to in the alternate timeline?",
        "correct": "Carol Willick",
        "distractors": ["Rachel Green", "Mindy Hunter", "Emily Waltham"],
        "d": 2
    },
    {
        "q": "What is the name of the undergraduate student Ross improperly dates in Season 6, violating university policy?",
        "correct": "Elizabeth Stevens",
        "distractors": ["Mona", "Charlie Wheeler", "Katie"],
        "d": 1
    },
    {
        "q": "Which Hollywood superstar guest starred as Paul Stevens, the stern and protective father of Ross's college student girlfriend Elizabeth?",
        "correct": "Bruce Willis",
        "distractors": ["Harrison Ford", "Sylvester Stallone", "Kurt Russell"],
        "d": 1
    },
    {
        "q": "What pep talk does Bruce Willis's character Paul give himself in front of the bedroom mirror at the mountain cabin?",
        "correct": "\"You're a neat guy. You're the man. You are the man!\"",
        "distractors": ["\"You're a tiger. Roar like a tiger!\"", "\"Nobody messes with Paul Stevens. Nobody!\"", "\"Look at that handsome devil in the glass!\""],
        "d": 2
    },
    {
        "q": "What childhood trauma causes Paul Stevens to break down into uncontrollable sobbing during his weekend with Rachel?",
        "correct": "Recalling how his father called him 'chicken boy' and wouldn't buy him a pet pony",
        "distractors": ["Remembering getting lost at a shopping mall carnival", "His eighth-grade science fair project collapsing on stage", "Getting pushed into a mud puddle on his birthday"],
        "d": 3
    },
    {
        "q": "In 'The One with the Ring', who assists Chandler in selecting an antique platinum diamond engagement ring for Monica?",
        "correct": "Phoebe",
        "distractors": ["Rachel", "Joey", "Ross"],
        "d": 2
    },
    {
        "q": "What vintage item does Chandler trade to another customer in a jewelry store to recover the antique engagement ring he selected?",
        "correct": "His classic watch plus extra cash",
        "distractors": ["His leather jacket and gold cufflinks", "A signed Knicks basketball", "His cellular phone and wallet"],
        "d": 2
    },
    {
        "q": "What unexpected former flame reappears at the restaurant where Chandler plans to propose to Monica in the Season 6 finale?",
        "correct": "Dr. Richard Burke",
        "distractors": ["Janice", "Paolo", "Pete Becker"],
        "d": 1
    },
    {
        "q": "What major promise does Dr. Richard Burke offer Monica when he confesses that he is still deeply in love with her?",
        "correct": "He promises he is now ready to marry her and have children together",
        "distractors": ["He promises to give up his medical practice and travel the world with her", "He offers to buy her a restaurant in the West Village", "He asks her to run away to Paris with him immediately"],
        "d": 2
    },
    {
        "q": "What reverse-psychology ruse does Chandler foolishly adopt that leads Monica to believe he never wants to marry?",
        "correct": "He constantly complains about marriage being a restrictive, antiquated institution",
        "distractors": ["He flirts with waitresses in front of her", "He pretends he wants to date other women exclusively", "He claims he is moving to Chicago for work"],
        "d": 2
    },
    {
        "q": "When Chandler walks into Monica's apartment expecting it to be empty in the Season 6 finale, what scene greets him?",
        "correct": "The living room is illuminated by hundreds of candles and Monica is down on one knee",
        "distractors": ["The room is filled with champagne bottles and all five friends shouting 'Congratulations!'", "Monica is sitting alone in the dark crying by the fireplace", "Richard Burke is waiting on the sofa to challenge him to a fight"],
        "d": 1
    },
    {
        "q": "Who actually completes speaking the marriage proposal vows when Monica becomes overcome with emotion and tears?",
        "correct": "Chandler",
        "distractors": ["Joey", "Ross", "Phoebe"],
        "d": 1
    },
    {
        "q": "What song is playing on the stereo as Monica and Chandler embrace on the floor following their emotional engagement?",
        "correct": "\"Wonderful Tonight\" by Eric Clapton",
        "distractors": ["\"With or Without You\" by U2", "\"The Way You Look Tonight\" by Frank Sinatra", "\"Unchained Melody\" by The Righteous Brothers"],
        "d": 2
    },
    {
        "q": "In Season 5, what did Ross name the monkey that Ugly Naked Guy supposedly owned across the alley?",
        "correct": "He did not own a monkey; Ugly Naked Guy owned a naked dog",
        "distractors": ["Babu", "Barnaby", "Buster"],
        "d": 3
    },
    {
        "q": "How does Ross convince Ugly Naked Guy to sublet his highly coveted apartment to Ross in Season 5?",
        "correct": "Ross strips completely naked and bonds with him over mini-muffins",
        "distractors": ["Ross offers him six months of rent paid in upfront cash", "Ross promises to let him sleep on the couch anytime", "Ross gives him his collection of rare dinosaur fossils"],
        "d": 1
    },
    {
        "q": "What phrase does Ross shout repeatedly at Chandler and Rachel while attempting to move a heavy sofa up the stairs?",
        "correct": "\"Pivot! Pivot! PIVOT!\"",
        "distractors": ["\"Lift! Lift! LIFT!\"", "\"Heave! Heave! HEAVE!\"", "\"Push! Push! PUSH!\""],
        "d": 1
    },
    {
        "q": "What sketch did Ross draw on a piece of paper to plan the maneuvering of his new sofa up the staircase?",
        "correct": "A geometric vector sketch with angles and arrows",
        "distractors": ["A blueprint of the apartment hallway", "A cartoon stick figure lifting weights", "A 3D isometric diagram of the stairs"],
        "d": 2
    },
    {
        "q": "What happens to Ross's new couch at the end of the moving ordeal in 'The One with the Cop'?",
        "correct": "It breaks completely in half, and Ross returns it to the store for four dollars in store credit",
        "distractors": ["It falls down three flights of stairs and crushes Mr. Treeger's mop", "It gets stuck permanently wedged between the banisters", "The delivery movers throw it into a dumpster on the street"],
        "d": 2
    },
    {
        "q": "What female roommate does Joey cast through auditions after Chandler moves in with Monica in Season 6?",
        "correct": "Janine Lecroix",
        "distractors": ["Erin", "Cheryl", "Kate Miller"],
        "d": 1
    },
    {
        "q": "In Season 4, what gift does Chandler buy for Kathy's birthday that makes Joey's gift look insignificant?",
        "correct": "A rare first-edition copy of her favorite childhood book 'The Velveteen Rabbit'",
        "distractors": ["A vintage gold fountain pen", "An antique silver pocket watch", "A signed playbill from her favorite Broadway musical"],
        "d": 2
    },
    {
        "q": "What does Joey end up giving Kathy as her birthday gift instead after Chandler hands over the rare book?",
        "correct": "A pencil case with a built-in pencil sharpener",
        "distractors": ["A box of chocolate cherries", "A pack of unscented votive candles", "A novelty coffee mug with a cat picture"],
        "d": 2
    },
    {
        "q": "What is the name of the woman with whom Ross goes on a disastrous date involving his glow-in-the-dark teeth?",
        "correct": "Hillary",
        "distractors": ["Kristen", "Cheryl", "Julie"],
        "d": 2
    },
    {
        "q": "In 'The One with the Apothecary Table', what does Rachel tell Phoebe the vintage apothecary table smells like?",
        "correct": "Opium and the French countryside",
        "distractors": ["Cedar and old lavender", "A Victorian apothecary shop", "Frankincense and ancient parchment"],
        "d": 3
    }
]

if __name__ == "__main__":
    out_path = os.path.join(os.path.dirname(__file__), "staging", "friends_batch2.json")
    build_batch(questions, out_path, batch_num=2)
