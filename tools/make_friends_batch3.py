#!/usr/bin/env python3
"""
Generate tools/staging/friends_batch3.json (100 questions, Seasons 7-10 Textual).
"""
import sys
import os

from build_friends_batch import build_batch

questions = [
    {
        "q": "In the Season 7 premiere 'The One with Monica's Thunder', why does Monica become furious with Rachel?",
        "correct": "Rachel kisses Ross in the hallway, stealing Monica's engagement spotlight",
        "distractors": ["Rachel accidentally spills red wine on Monica's engagement gown", "Rachel announces that she is moving to London", "Rachel criticizes Chandler's diamond engagement ring"],
        "d": 1
    },
    {
        "q": "What hidden book does Joey discover under Rachel's mattress in 'The One with Rachel's Book'?",
        "correct": "A spicy erotic romance novel called 'Be My Duchess'",
        "distractors": ["A diary filled with romantic poems about Ross", "A book on how to marry a millionaire", "A novel about male underwear models"],
        "d": 2
    },
    {
        "q": "What famous brand of pre-packaged chocolate chip cookie dough was Phoebe's grandmother's secret recipe?",
        "correct": "Nestlé Toll House",
        "distractors": ["Pillsbury Chocolate Chip", "Keebler Soft Batch", "Famous Amos"],
        "d": 1
    },
    {
        "q": "What French name does Phoebe invent when trying to recall the family name behind her grandmother's cookie recipe?",
        "correct": "\"Nestlé Toulouse\"",
        "distractors": ["\"Madame Bordelaise\"", "\"Chef Chamonix\"", "\"Duchess de Chocolat\""],
        "d": 1
    },
    {
        "q": "In 'The One with the Nap Partners', which two male friends discover they enjoy taking afternoon naps snuggled together?",
        "correct": "Joey and Ross",
        "distractors": ["Chandler and Ross", "Joey and Chandler", "Gunther and Ross"],
        "d": 1
    },
    {
        "q": "What costume does Ross rent to teach his son Ben about Hanukkah when all Santa costumes are rented out?",
        "correct": "A giant armadillo costume",
        "distractors": ["A brown beaver costume", "A turtle shell outfit", "A reindeer mascot suit"],
        "d": 1
    },
    {
        "q": "What festive title does Ross give himself while dressed in the rented armadillo suit?",
        "correct": "\"The Holiday Armadillo\"",
        "distractors": ["\"The Hanukkah Hedgehog\"", "\"The Festival Ferret\"", "\"The Mitzvah Mammal\""],
        "d": 1
    },
    {
        "q": "Which characters arrive at Monica's apartment dressed as Santa Claus and Superman to join the Holiday Armadillo?",
        "correct": "Chandler as Santa and Joey as Superman",
        "distractors": ["Joey as Santa and Chandler as Superman", "Phoebe as Santa and Joey as Superman", "Ross as Santa and Chandler as Superman"],
        "d": 1
    },
    {
        "q": "From which bakery in Chicago do Chandler and Rachel repeatedly steal misdelivered mail-order cheesecakes?",
        "correct": "Mama's Little Bakery",
        "distractors": ["Sweet Chicago Bakery", "Windy City Delights", "Little Italy Bakeshop"],
        "d": 2
    },
    {
        "q": "What do Chandler and Rachel do after dropping their stolen cheesecake onto the hallway floor?",
        "correct": "They kneel on the carpet and eat it directly off the floor with forks",
        "distractors": ["They scoop it into a trash bag and throw it out the window", "They wash the dirt off in the bathroom sink", "They feed the remaining crumbs to the street pigeons"],
        "d": 1
    },
    {
        "q": "What does Joey do when he discovers Chandler and Rachel eating dropped cheesecake off the hallway carpet?",
        "correct": "He pulls a fork from his coat pocket and joins in",
        "distractors": ["He threatens to call the police unless they pay him", "He scolds them for violating health codes", "He stomps on the cheesecake with his leather boot"],
        "d": 1
    },
    {
        "q": "What emotional lament does Joey cry out to the heavens on his 30th birthday?",
        "correct": "\"Why, God, why?! We had a deal! Let the others grow old, not me!\"",
        "distractors": ["\"I don't want to turn thirty! Take Chandler instead!\"", "\"Thirty is the end of life! I will never be an actor now!\"", "\"God, please rewind the clock five years!\""],
        "d": 1
    },
    {
        "q": "Why does Rachel break up with her handsome young assistant Tag Jones on her 30th birthday?",
        "correct": "Tag is only 24 and she realizes their life and family timelines do not match",
        "distractors": ["Tag accidentally damages Ralph Lauren's private designer collection", "Tag forgets Rachel's milestone 30th birthday party", "Tag decides to move back to Colorado to join a band"],
        "d": 2
    },
    {
        "q": "Which Oscar-winning actress guest stars as soap diva Jessica Lockhart in 'The One with Joey's New Brain'?",
        "correct": "Susan Sarandon",
        "distractors": ["Meryl Streep", "Glenn Close", "Sigourney Weaver"],
        "d": 1
    },
    {
        "q": "How is Joey's character Dr. Drake Ramoray miraculously revived from his coma on 'Days of Our Lives'?",
        "correct": "He receives the transplanted brain of deceased character Jessica Lockhart",
        "distractors": ["He undergoes experimental cybernetic neurological surgery", "He awakens after hearing his long-lost twin sister sing", "His evil twin brother donates a kidney and spinal cord"],
        "d": 1
    },
    {
        "q": "What revelation about the London trip is uncovered in 'The One with the Truth About London'?",
        "correct": "Monica originally went to Chandler's hotel room looking to sleep with Joey",
        "distractors": ["Joey accidentally filmed Chandler and Monica on his handheld camcorder", "Chandler initially wanted to propose to Rachel in London", "Ross heard Chandler and Monica together the night before the wedding"],
        "d": 1
    },
    {
        "q": "Which actress guest stars as Ross and Monica's gorgeous cousin Cassie in Season 7?",
        "correct": "Denise Richards",
        "distractors": ["Carmen Electra", "Tara Reid", "Rebecca Gayheart"],
        "d": 1
    },
    {
        "q": "Which Hollywood actress guest stars as Melissa Warburton, Rachel's college sorority sister with whom she shared a drunken kiss?",
        "correct": "Winona Ryder",
        "distractors": ["Gwyneth Paltrow", "Drew Barrymore", "Cameron Diaz"],
        "d": 1
    },
    {
        "q": "Which legendary actor guest stars as Richard Crosby, the spitting Shakespearean actor filming a war movie with Joey?",
        "correct": "Gary Oldman",
        "distractors": ["Anthony Hopkins", "Kenneth Branagh", "Ian McKellen"],
        "d": 1
    },
    {
        "q": "What costume does Joey wear while officiating Monica and Chandler's wedding ceremony?",
        "correct": "A World War I military soldier uniform covered in fake mud",
        "distractors": ["A Roman gladiator costume from Caesar's Palace", "A tuxedo with tennis shoes and no socks", "A medieval knight tunic and chainmail"],
        "d": 1
    },
    {
        "q": "Where does Phoebe discover a positive pregnancy test on the day of Monica and Chandler's wedding?",
        "correct": "In the wastebasket inside Monica's bathroom",
        "distractors": ["Inside Rachel's handbag on the coffee table", "On the edge of the kitchen sink", "In the pocket of Monica's bridal robe"],
        "d": 1
    },
    {
        "q": "Who is revealed to be the actual pregnant woman at the conclusion of the Season 7 finale?",
        "correct": "Rachel",
        "distractors": ["Monica", "Phoebe", "Janice"],
        "d": 1
    },
    {
        "q": "What piece of clothing left in Monica's apartment leads Joey and Phoebe to identify the father of Rachel's baby?",
        "correct": "A red long-sleeve sweater",
        "distractors": ["A brown leather bomber jacket", "A blue wool baseball cap", "A green cashmere scarf"],
        "d": 1
    },
    {
        "q": "Who picks up the red sweater and says 'Hey, my sweater! I've been looking for this for like a month!'?",
        "correct": "Ross",
        "distractors": ["Tag", "Joey", "Chandler"],
        "d": 1
    },
    {
        "q": "What contraceptive statistic does Ross learn that causes him to shout in horror at his doctor?",
        "correct": "Condoms are only 97% effective",
        "distractors": ["Condoms are only 90% effective", "Birth control pills fail 15% of the time", "Spermicides have a 25% failure rate"],
        "d": 2
    },
    {
        "q": "In 'The One with the Videotape', what seductive backpacking story does Joey teach Ross to use on women?",
        "correct": "The Western Europe and Mount Tibidabo story",
        "distractors": ["The backpacking through the Swiss Alps story", "The romantic Venice gondola story", "The lost traveler in Prague story"],
        "d": 1
    },
    {
        "q": "What mountain foothills outside Barcelona are featured in Joey's famous seduction story?",
        "correct": "Mount Tibidabo",
        "distractors": ["Montserrat", "Mount Montjuïc", "The Pyrenees"],
        "d": 1
    },
    {
        "q": "What costume does Ross wear to Monica's Halloween party that everyone mistakes for a giant piece of excrement?",
        "correct": "\"Spud-nik\" (a brown potato costume with an antenna)",
        "distractors": ["A brown acorn with a twig", "A chocolate bean with a wire", "A coconut with an umbrella"],
        "d": 1
    },
    {
        "q": "What costume does Chandler wear to Monica's Halloween party in Season 8?",
        "correct": "A pink velvet bunny rabbit costume",
        "distractors": ["Catwoman", "Supergirl", "A giant carrot"],
        "d": 1
    },
    {
        "q": "Which superstar guest stars as Will Colbert, a former high school classmate who co-founded the 'I Hate Rachel Green Club'?",
        "correct": "Brad Pitt",
        "distractors": ["Tom Cruise", "Johnny Depp", "Christian Bale"],
        "d": 1
    },
    {
        "q": "What rumor did Will Colbert and Ross spread about Rachel during high school in the 'I Hate Rachel Green Club'?",
        "correct": "That Rachel was born a hermaphrodite with both male and female reproductive organs",
        "distractors": ["That Rachel wore a wig to cover up a bald patch", "That Rachel cheated on her high school SAT exams", "That Rachel was secretly thirty years old in high school"],
        "d": 1
    },
    {
        "q": "What musical artist does Phoebe try to get concert tickets from because his son attends school with Ben?",
        "correct": "Sting",
        "distractors": ["Bono", "Elton John", "Billy Joel"],
        "d": 2
    },
    {
        "q": "What awkward gesture does Ross make to Mona when she suggests sending a joint holiday card together?",
        "correct": "He gives her a key to his apartment and then immediately changes the deadbolt lock",
        "distractors": ["He gives her an empty jewelry box and runs away", "He invents a fake overseas business trip to Tokyo", "He claims he cannot celebrate holidays due to paleontology"],
        "d": 2
    },
    {
        "q": "Where does Joey finally confess his genuine romantic feelings to Rachel in Season 8?",
        "correct": "At a dimly lit romantic restaurant over dinner",
        "distractors": ["On the Central Perk couch", "On the fire escape outside her bedroom", "In the hospital waiting room"],
        "d": 1
    },
    {
        "q": "Which actor guest stars as Parker, Phoebe's hyper-enthusiastic date who finds everything miraculously delightful?",
        "correct": "Alec Baldwin",
        "distractors": ["Jeff Goldblum", "Steve Martin", "Christopher Walken"],
        "d": 1
    },
    {
        "q": "What bizarre fictional game show does Joey audition to host in Season 8?",
        "correct": "\"Bamboozled\"",
        "distractors": ["\"Spin to Win\"", "\"The Golden Ladder\"", "\"Wicked Wingo\""],
        "d": 1
    },
    {
        "q": "Who turns out to be Rachel's loud and irritating labor roommate at the hospital in the Season 8 finale?",
        "correct": "Janice Litman-Goralnik",
        "distractors": ["Ursula Buffay", "Amy Green", "Jill Green"],
        "d": 1
    },
    {
        "q": "What baby name did Monica plan to use for her own future daughter, but generously gives to Rachel for her newborn girl?",
        "correct": "Emma",
        "distractors": ["Isabella", "Delilah", "Ruth"],
        "d": 1
    },
    {
        "q": "How does Joey accidentally propose to Rachel in the hospital recovery room right after Emma is born?",
        "correct": "An engagement ring drops from Ross's coat, and Joey kneels to pick it up, facing Rachel",
        "distractors": ["Joey blurts out 'Marry me!' in an emotional delirium", "Joey hands Rachel a box of chocolates with a ring inside", "Joey reads a script from Days of Our Lives by mistake"],
        "d": 1
    },
    {
        "q": "What medical doctor does Ross still secretly visit as an adult in Season 9 until Monica exposes him?",
        "correct": "His childhood pediatrician Dr. Gettleman",
        "distractors": ["His pediatric orthodontist", "His high school optometrist", "His childhood dermatologist"],
        "d": 2
    },
    {
        "q": "In 'The One with the Sharks', what bizarre sexual fetish does Monica mistakenly believe Chandler possesses?",
        "correct": "Getting sexually aroused by watching sharks on nature documentaries",
        "distractors": ["Getting turned on by women wearing medieval armor", "A fetish for high-heeled cowboy boots", "A fetish for giant inflatable furniture"],
        "d": 1
    },
    {
        "q": "Which actor guest stars as Sandy, the sensitive male nanny hired by Ross and Rachel in Season 9?",
        "correct": "Freddie Prinze Jr.",
        "distractors": ["Mark-Paul Gosselaar", "James Van Der Beek", "Joshua Jackson"],
        "d": 1
    },
    {
        "q": "Why does Ross fire the wonderfully qualified male nanny Sandy?",
        "correct": "He feels deeply uncomfortable with a man being so emotional, nurturing, and playing recorder",
        "distractors": ["Sandy accidentally drops baby Emma's favorite stuffed animal", "Sandy charges three times the market rate for nannies", "Sandy flirts openly with Joey and Rachel"],
        "d": 2
    },
    {
        "q": "Which actress won an Emmy for guest starring as Rachel's self-centered sister Amy Green in Season 9?",
        "correct": "Christina Applegate",
        "distractors": ["Reese Witherspoon", "Alyssa Milano", "Sarah Michelle Gellar"],
        "d": 1
    },
    {
        "q": "What precious possession of Monica's does Rachel's sister Amy shatter during Thanksgiving dinner in Season 9?",
        "correct": "Her prized wedding china plates",
        "distractors": ["Her antique crystal punch bowl", "Her hand-carved mahogany salad bowl", "Her grandmother's porcelain gravy boat"],
        "d": 2
    },
    {
        "q": "To which Midwestern city is Chandler transferred for his corporate job in Season 9, requiring him to commute weekly?",
        "correct": "Tulsa, Oklahoma",
        "distractors": ["Omaha, Nebraska", "Kansas City, Missouri", "Des Moines, Iowa"],
        "d": 1
    },
    {
        "q": "What life-changing career decision does Chandler make on Christmas Eve in Tulsa?",
        "correct": "He resigns from his executive job to return home to New York and be with Monica",
        "distractors": ["He accepts a promotion to oversee European branches in London", "He sues his firm for wrongful holiday relocation", "He launches an independent accounting firm with Joey"],
        "d": 1
    },
    {
        "q": "In 'The One with the Mugging', what startling childhood secret does Phoebe reveal to Ross?",
        "correct": "She was the street kid who mugged Ross and stole his 'Geology Boy' comic book",
        "distractors": ["She lived in the crawlspace beneath Ross's college dorm", "She stolen Ross's bicycle when he was twelve years old", "She threw an egg at Ross during his high school graduation"],
        "d": 2
    },
    {
        "q": "Why does Joey mistakenly believe Monica underwent plastic surgery in 'The One with the Boob Job'?",
        "correct": "Chandler and Monica each secretly borrow money from Joey and concoct false cover stories",
        "distractors": ["Monica buys a padded push-up bra for a job interview", "Joey misreads a brochure left in Monica's bathroom", "Phoebe tells Joey that Monica got breast implants in New Jersey"],
        "d": 2
    },
    {
        "q": "What fake news do Chandler and Ross post about each other on their college alumni message board?",
        "correct": "Chandler posts that Ross died getting hit by a blimp, and Ross posts that Chandler is gay",
        "distractors": ["Chandler posts that Ross joined a cult, and Ross posts that Chandler was arrested", "Ross posts that Chandler went bankrupt, and Chandler posts that Ross married a monkey", "Chandler posts that Ross went bald, and Ross posts that Chandler moved to Antarctica"],
        "d": 2
    },
    {
        "q": "How does Phoebe accidentally destroy the gang's communal lottery tickets in Season 9?",
        "correct": "A pigeon startles her on the balcony and she drops the bowl of tickets into the street",
        "distractors": ["She accidentally runs them through the laundry washing machine", "She lights incense and sets the entire stack of tickets ablaze", "Joey mistakes the tickets for napkins and throws them in the trash"],
        "d": 2
    },
    {
        "q": "Which actress portrayed Dr. Charlie Wheeler, the brilliant paleontology professor who dates both Joey and Ross?",
        "correct": "Aisha Tyler",
        "distractors": ["Gabrielle Union", "Kerry Washington", "Rosario Dawson"],
        "d": 1
    },
    {
        "q": "Where does the gang travel for Ross's keynote paleontology conference in the Season 9 finale?",
        "correct": "Barbados",
        "distractors": ["Bermuda", "Jamaica", "The Bahamas"],
        "d": 1
    },
    {
        "q": "What happens to Monica's hair due to the tropical climate in Barbados?",
        "correct": "It swells into a massive ball of frizz due to the extreme humidity",
        "distractors": ["It turns bright green from pool chlorine", "She accidentally burns off her bangs with a curling iron", "She gets cornrows braided with seashells that get tangled"],
        "d": 1
    },
    {
        "q": "Which actor plays Mike Hannigan, the former lawyer and pianist who falls in love with Phoebe?",
        "correct": "Paul Rudd",
        "distractors": ["Hank Azaria", "Jason Segel", "Edward Norton"],
        "d": 1
    },
    {
        "q": "What competitive game do Monica and Mike Hannigan play obsessively for hours at the hotel resort in Barbados?",
        "correct": "Table tennis (ping-pong)",
        "distractors": ["Foosball", "Air hockey", "Billiards"],
        "d": 1
    },
    {
        "q": "What romantic twist occurs between Joey and Rachel in Joey's hotel room in the Season 9 finale?",
        "correct": "Joey kisses Rachel after seeing Ross kissing Charlie in the garden",
        "distractors": ["Rachel proposes marriage to Joey on the beach", "Joey tells Rachel he only loves her as a sister", "Rachel confesses she wants to move back to Paris"],
        "d": 1
    },
    {
        "q": "What culinary dish does Ross insist on making while drunkenly claiming 'I'M FINE!' in Season 10?",
        "correct": "Sizzling Mexican fajitas and margaritas",
        "distractors": ["Spaghetti bolognese and garlic bread", "Barbecue ribs and potato salad", "Cheese fondue with sourdough bread"],
        "d": 1
    },
    {
        "q": "What spelling acrostic does an intoxicated Ross tearfully declaim about relationships in 'The One Where Ross Is Fine'?",
        "correct": "\"L-O-V-E\"",
        "distractors": ["\"H-U-R-T\"", "\"B-R-E-A-K\"", "\"F-I-N-E\""],
        "d": 2
    },
    {
        "q": "In 'The One with Ross's Tan', what blunder does Ross make inside the automated spray tan booth?",
        "correct": "He counts 'Mississippis' too slowly and gets sprayed repeatedly on his front side only",
        "distractors": ["He forgets to take off his clothes before the mist sprays", "He accidentally sprays himself with permanent dark mahogany stain", "He faces the wrong wall and gets sprayed entirely in the eyes"],
        "d": 1
    },
    {
        "q": "What shade number difference does Ross end up with between his front and back after two spray tan visits?",
        "correct": "He is an 8 on the front and a 0 on his back",
        "distractors": ["He is a 10 on the front and a 2 on his back", "He is a 6 on the front and a 1 on his back", "He is a 4 on the front and a 0 on his back"],
        "d": 2
    },
    {
        "q": "What shape was the inappropriate erotic cake mistakenly delivered for Emma's first birthday party?",
        "correct": "A penis",
        "distractors": ["A pair of breasts", "A naked human torso", "A pair of buttocks"],
        "d": 1
    },
    {
        "q": "How does Ross creatively reshape Emma's birthday cake before Rachel's parents arrive?",
        "correct": "He carves and rearranges the cake into a cute puppy dog",
        "distractors": ["He slices it into a fluffy bunny rabbit", "He transforms it into a racing car", "He covers it in icing to resemble a baseball glove"],
        "d": 2
    },
    {
        "q": "What unauthorized cosmetic procedure does Amy Green perform on baby Emma in Season 10?",
        "correct": "She gets Emma's ears pierced at the mall",
        "distractors": ["She cuts Emma's baby bangs into a blunt bob", "She paints Emma's toenails with indelible pink lacquer", "She trims Emma's eyelashes with manicure scissors"],
        "d": 1
    },
    {
        "q": "Why is Laura, the adoption agency social worker, deeply biased against Chandler and Monica's building?",
        "correct": "Joey dated her in the past and never called her back after sleeping with her",
        "distractors": ["Mr. Treeger refused to let her ride the service elevator", "Ross broke her heart at a college paleontology mixer", "Monica gave her terrible catering service at a charity gala"],
        "d": 2
    },
    {
        "q": "In 'The One with the Late Thanksgiving', why are Joey, Ross, Rachel, and Phoebe locked out of Monica's apartment?",
        "correct": "They arrive nearly an hour late after attending a Rangers game and beauty pageant",
        "distractors": ["They forgot to bring the turkey and pumpkin pie", "They invited Janice to dinner without asking Monica", "They got arrested for jaywalking on Sixth Avenue"],
        "d": 1
    },
    {
        "q": "What comical dilemma befalls Joey through the door crack while begging Monica for Thanksgiving forgiveness?",
        "correct": "He gets his head trapped inside the doorway chain opening",
        "distractors": ["He gets his arm stuck inside the brass letter mail slot", "His foot gets wedged under the wooden threshold", "He gets his jacket zipper caught on the doorknob"],
        "d": 1
    },
    {
        "q": "What joyous news do Monica and Chandler receive over the phone at the end of their late Thanksgiving in Season 10?",
        "correct": "An expectant birth mother from Ohio has chosen them to adopt her baby",
        "distractors": ["Monica has been awarded a prestigious Michelin star", "Chandler's advertising firm made him a full partner", "Monica has discovered she is naturally pregnant with twins"],
        "d": 1
    },
    {
        "q": "Which comedic actress guest stars as Erica, the pregnant teen from Ohio who chooses Monica and Chandler to adopt her baby?",
        "correct": "Anna Faris",
        "distractors": ["Amy Adams", "Isla Fisher", "Kaley Cuoco"],
        "d": 1
    },
    {
        "q": "What profession does Erica mistakenly believe Chandler and Monica have based on a mixed-up adoption agency file?",
        "correct": "A doctor and a reverend",
        "distractors": ["A lawyer and an architect", "A college professor and a diplomat", "A senator and a veterinarian"],
        "d": 2
    },
    {
        "q": "Why do the friends mistakenly suspect Chandler of having an extramarital affair in Season 10?",
        "correct": "They see him getting into a blonde woman's car, unaware she is a real estate agent showing them houses",
        "distractors": ["They find lipstick on his business collar from a client", "He sneaks out of town on weekends claiming to go to dentist conventions", "They find hotel room receipts in his coat pocket"],
        "d": 1
    },
    {
        "q": "Where are Monica and Chandler secretly planning to move to raise their new baby?",
        "correct": "Westchester County, New York",
        "distractors": ["Hoboken, New Jersey", "Greenwich, Connecticut", "Long Island, New York"],
        "d": 1
    },
    {
        "q": "Which legendary Hollywood actor guest stars as Roy, the weeping 50-year-old stripper at Phoebe's bachelorette party?",
        "correct": "Danny DeVito",
        "distractors": ["Joe Pesci", "Christopher Walken", "Harvey Keitel"],
        "d": 1
    },
    {
        "q": "Where do Phoebe and Mike hold their wedding ceremony after a massive blizzard shuts down New York City?",
        "correct": "Outside in the snowy street right in front of Central Perk",
        "distractors": ["Inside the Central Perk coffeehouse around the orange sofa", "Inside the hallway between Monica and Joey's apartments", "In the subway station beneath Grand Central Terminal"],
        "d": 1
    },
    {
        "q": "Who walks Phoebe down the snowy aisle during her wedding to Mike Hannigan?",
        "correct": "Joey",
        "distractors": ["Chandler", "Ross", "Her stepdad Frank Buffay Sr."],
        "d": 1
    },
    {
        "q": "In 'The One Where Joey Speaks French', what gibberish sounds does Joey produce while attempting to repeat 'Je m'appelle Claude'?",
        "correct": "\"Mi poo poo\" and \"Bla bla bla\"",
        "distractors": ["\"Oui oui oui\" and \"Toot toot toot\"", "\"Bonjour monsieur\" and \"Ooh la la\"", "\"Garçon de café\" and \"Chapeau bas\""],
        "d": 2
    },
    {
        "q": "What absurd name does Phoebe legally change her name to in Season 10 after discovering she can pick anything?",
        "correct": "Princess Consuela Banana Hammock",
        "distractors": ["Duchess Valentina Sparkle Toes", "Lady Guinevere Cinnamon Twist", "Queen Regina Honeydew Phalange"],
        "d": 1
    },
    {
        "q": "What equally ridiculous name does Mike threaten to adopt in response to Phoebe's name change?",
        "correct": "Crap Bag",
        "distractors": ["Dirt Bag", "Garbage Can", "Stinky Pants"],
        "d": 1
    },
    {
        "q": "What talent agent of Joey's passes away in Season 10, prompting Phoebe to impersonate her on the phone?",
        "correct": "Estelle Leonard",
        "distractors": ["Joanna Miller", "Mindy Hunter", "Erika Ford"],
        "d": 2
    },
    {
        "q": "For which iconic luxury French fashion house does Rachel accept a dream executive job in Paris in Season 10?",
        "correct": "Louis Vuitton",
        "distractors": ["Chanel", "Christian Dior", "Hermès"],
        "d": 1
    },
    {
        "q": "Why does Rachel say goodbye privately to Joey, Monica, Chandler, and Phoebe, but initially skip saying goodbye to Ross?",
        "correct": "It was too painful and emotionally overwhelming because Ross meant too much to her",
        "distractors": ["She was furious that Ross didn't throw her a farewell party", "She believed Ross didn't care whether she moved to France", "Ross told her earlier that he never wanted to see her again"],
        "d": 1
    },
    {
        "q": "What major surprise occurs during Erica's delivery in the series finale 'The Last One'?",
        "correct": "Erica gives birth to unexpected fraternal twins (a boy and a girl)",
        "distractors": ["Erica decides at the last minute to keep the baby herself", "The doctor delivers triplets instead of one baby", "Erica's estranged fiancé bursts into the room demanding custody"],
        "d": 1
    },
    {
        "q": "What names do Monica and Chandler choose for their newborn twins in the series finale?",
        "correct": "Jack (after Monica's father) and Erica (after the birth mother)",
        "distractors": ["Ross and Rachel", "Frank and Judy", "Richard and Nora"],
        "d": 1
    },
    {
        "q": "Which airport do Ross and Phoebe accidentally race to first in Phoebe's yellow cab to stop Rachel?",
        "correct": "John F. Kennedy International Airport (JFK)",
        "distractors": ["LaGuardia Airport (LGA)", "Newark Liberty International Airport (EWR)", "Westchester County Airport (HPN)"],
        "d": 1
    },
    {
        "q": "Which airport was Rachel actually departing from to fly to Paris in the series finale?",
        "correct": "Newark Liberty International Airport (EWR)",
        "distractors": ["John F. Kennedy International Airport (JFK)", "LaGuardia Airport (LGA)", "Stewart International Airport (SWF)"],
        "d": 1
    },
    {
        "q": "What fictional missing aircraft component does Phoebe invent over the telephone to panic passengers and delay Rachel's flight?",
        "correct": "\"The left phalange\"",
        "distractors": ["\"The secondary fuel intake valve\"", "\"The starboard wing rudder pin\"", "\"The primary fuselage stabilizer\""],
        "d": 1
    },
    {
        "q": "Which passenger on Rachel's plane overhears Phoebe's warning about the 'phalange' and frantically demands to disembark?",
        "correct": "A neurotic passenger played by Jim Rash",
        "distractors": ["A businessman played by Thomas Lennon", "A flight attendant played by Dan Castellaneta", "A tourist played by Hank Azaria"],
        "d": 2
    },
    {
        "q": "What does Rachel say on the recorded answering machine message in the series finale right before the tape cuts off?",
        "correct": "\"I got off the plane.\"",
        "distractors": ["\"I'm sorry, Ross, I had to fly.\"", "\"I will always love you from Paris.\"", "\"Meet me at Central Perk right now.\""],
        "d": 1
    },
    {
        "q": "What physical objects do all six friends leave behind on the kitchen counter in the empty apartment in the final scene?",
        "correct": "Their apartment keys",
        "distractors": ["Their Central Perk coffee mugs", "Their favorite framed group photos", "Their personal cell phones"],
        "d": 1
    },
    {
        "q": "What is the very last spoken line of dialogue in the entire ten-season run of Friends, uttered by Chandler?",
        "correct": "\"Sure. Where?\"",
        "distractors": ["\"I love you guys.\"", "\"Here we go.\"", "\"Goodbye, apartment twenty.\""],
        "d": 1
    },
    {
        "q": "Where does Rachel suggest the friends go for coffee one last time in the closing lines of the series finale?",
        "correct": "Central Perk",
        "distractors": ["The corner diner", "Starbucks", "The bakery on Fifth"],
        "d": 1
    },
    {
        "q": "In Season 8, what does Chandler discover he is incapable of doing on command in photography studios?",
        "correct": "Smiling naturally without making a hideous grimace",
        "distractors": ["Keeping both of his eyes open at the same time", "Standing upright without tilting his head awkwardly", "Looking directly into the camera lens without blinking"],
        "d": 2
    },
    {
        "q": "What is the name of Joey's stuffed penguin toy that he refuses to part with?",
        "correct": "Hugsy, the bedtime penguin pal",
        "distractors": ["Waddles, the cuddle penguin", "Pippy, the sleep buddy", "Flipper, the chilly pal"],
        "d": 1
    },
    {
        "q": "In Season 10, what does Phoebe receive from Mike's eccentric mother Bitsy Hannigan at their upscale dinner?",
        "correct": "Extreme condescension regarding Phoebe's bohemian background",
        "distractors": ["An antique silver soup tureen", "A check for ten thousand dollars to stay away from Mike", "An invitation to join a competitive polo club"],
        "d": 2
    },
    {
        "q": "What was the name of the woman from the adoption agency who interviewed Monica and Chandler and remembered Joey?",
        "correct": "Laura",
        "distractors": ["Sarah", "Nancy", "Karen"],
        "d": 2
    },
    {
        "q": "What animal does Joey adopt in Season 10 to replace the chick and duck, only for it to be a bird?",
        "correct": "Chick Jr. and Duck Jr.",
        "distractors": ["Pigeon Pete", "Rooster Ralph", "Goose Gary"],
        "d": 2
    },
    {
        "q": "In Season 7, how does Chandler discover that Monica has no wedding savings left?",
        "correct": "Monica spent her entire life savings on catering deposits and dresses earlier in life",
        "distractors": ["Her parents Judy and Jack spent her wedding fund on a beach house", "Her bank went bankrupt during the tech bubble", "She lent her entire life savings to Richard Burke"],
        "d": 2
    },
    {
        "q": "In Season 7, why did Jack and Judy Geller spend Monica's wedding fund before she got engaged?",
        "correct": "They assumed she would never get married after turning thirty",
        "distractors": ["They used it to pay for Ross's two divorces and legal settlements", "They lost it in a fraudulent real estate investment in Florida", "They spent it renovating their kitchen and buying a boat"],
        "d": 2
    },
    {
        "q": "What job does Chandler transition into after quitting his data reconfiguration position in Season 9?",
        "correct": "Junior advertising copywriter",
        "distractors": ["Children's book illustrator", "High school literature teacher", "Restaurant business manager"],
        "d": 1
    },
    {
        "q": "What clever slogan does Chandler pitch for roller sneakers during his advertising internship?",
        "correct": "\"Shoes that let you roll when you don't feel like walking\"",
        "distractors": ["\"Roll into the future on four wheels\"", "\"Fast feet for fast people\"", "\"Why walk when you can glide?\""],
        "d": 3
    }
]

if __name__ == "__main__":
    out_path = os.path.join(os.path.dirname(__file__), "staging", "friends_batch3.json")
    build_batch(questions, out_path, batch_num=3)
