#!/usr/bin/env python3
import json

raw_questions = [
    # Will Truman fundamentals
    ("What is Will Truman's profession throughout most of Will & Grace?", "Corporate lawyer", ["Architect", "Accountant", "Real estate agent"], 1),
    ("Where did Will Truman and Grace Adler first meet as undergraduate students?", "Columbia University", ["New York University", "Yale University", "Harvard University"], 1),
    ("In which New York City apartment building do Will and Grace reside for most of the series?", "940 Park Avenue", ["740 Park Avenue", "15 Central Park West", "1040 Fifth Avenue"], 2),
    ("What is the number of Will Truman's apartment where Grace frequently lives?", "Apartment 9C", ["Apartment 4B", "Apartment 12A", "Apartment 7F"], 2),
    ("What is the number of Jack McFarland's apartment across the hall from Will?", "Apartment 9E", ["Apartment 9A", "Apartment 9B", "Apartment 9D"], 2),
    ("What is Will Truman's middle name?", "None (his legal first name is William)", ["Alexander", "Edward", "Charles"], 3),
    ("What is Grace Adler's middle name?", "Elizabeth", ["Marie", "Anne", "Louise"], 2),
    ("What is the name of Grace Adler's interior design company?", "Grace Adler Designs", ["Adler & Associates", "Manhattan Interiors", "Adler Design Group"], 1),
    ("What is Karen Walker's job title at Grace Adler Designs?", "Assistant", ["Managing Partner", "Senior Designer", "Receptionist"], 1),
    ("Why does Karen Walker continue working as Grace's assistant despite being extraordinarily wealthy?", "To get away from Stan and have social interaction", ["She needs health insurance", "She owns a 50% stake in the business", "Her father forced her to keep a job"], 2),
    
    # Karen Walker quirks and lore
    ("What is Karen Walker's maiden name?", "Delaney", ["Finster", "Harriman", "Van Horne"], 2),
    ("What is the name of Karen Walker's wealthy, obese husband seen mostly in obscured angles?", "Stanley Walker", ["Arthur Walker", "Sterling Walker", "Lyle Walker"], 1),
    ("What are the names of Stan Walker's two children from a previous relationship?", "Mason and Olivia", ["Justin and Chloe", "Spencer and Ashley", "Trevor and Brittany"], 2),
    ("What was Karen Walker's signature beverage of choice throughout the series?", "Vodka martini", ["Cosmopolitan", "Gin and tonic", "White wine spritzer"], 1),
    ("What is the name of Karen's loyal maid and confidante whom she treats with combative affection?", "Rosario Salazar", ["Consuela Lopez", "Maria Santos", "Lupe Fuentes"], 1),
    ("What country is Rosario Salazar originally from?", "El Salvador", ["Guatemala", "Nicaragua", "Honduras"], 2),
    ("Before coming to the United States and working for Karen, what was Rosario's profession in El Salvador?", "Clinical psychologist", ["Lawyer", "College professor", "Nurse"], 3),
    ("Why did Jack McFarland marry Rosario Salazar at the end of Season 1?", "To get her a green card to avoid deportation", ["To spite Karen", "To claim an inheritance", "To win a bet with Will"], 1),
    ("Which diminutive Southern socialite is Karen Walker's arch-rival and frenemy?", "Beverley Leslie", ["Beau Bridges", "Buckley Sterling", "Barton Fink"], 1),
    ("What is Beverley Leslie's famous recurring catchphrase whenever he encounters Karen?", "\"Well, well, well...\"", ["\"Bless your heart!\"", "\"Look what the cat dragged in!\"", "\"How delightful!\""], 1),

    # Jack McFarland quirks and lore
    ("What is Jack McFarland's full birth name?", "John Phillip Fisher McFarland", ["Jack Alexander McFarland", "John Thomas McFarland", "Jonathan David McFarland"], 3),
    ("What is the name of Jack McFarland's famous one-man cabaret show in early seasons?", "\"Just Jack!\"", ["\"All About Jack!\"", "\"Jack's World!\"", "\"Viva Jack!\""], 1),
    ("What hand gesture accompanies Jack's exclamation of \"Just Jack!\"?", "Framing his face with both hands like jazz hands", ["Snapping both fingers simultaneously", "Waving jazz hands above his head", "Pointing finger guns forward"], 1),
    ("What type of dog did Jack adopt and name Klaus Von Puppy?", "Whippet / Greyhound mix", ["Poodle", "Chihuahua", "Golden Retriever"], 2),
    ("What retail clothing store does Jack work at during the second season?", "Banana Republic", ["Gap", "Barneys New York", "J.Crew"], 2),
    ("What luxury department store does Jack work at as a window dresser and sales associate in later seasons?", "Barneys New York", ["Saks Fifth Avenue", "Bergdorf Goodman", "Bloomingdale's"], 2),
    ("What is the name of Jack's theater acting method/class that he teaches in Season 6?", "The McFarland Method", ["The Jack Experience", "The Actor's Instrument", "The Broadway Way"], 2),
    ("What is the name of the gay television network where Jack works as an executive in Season 7?", "Out TV", ["Pride Network", "Queer Vision", "Rainbow Cable"], 2),
    ("What talk show does Jack host on Out TV?", "\"Jack Talk\"", ["\"Chat with Jack\"", "\"Morning McFarland\"", "\"The Jack Beat\""], 2),
    ("What was the name of the beloved parrot Karen bought that repeated her insults?", "Guapo", ["Polly", "Chico", "Pepe"], 3),

    # Will & Grace food, habits, habits
    ("What snack food is Grace Adler famously obsessed with and frequently hides around the apartment?", "Funyuns", ["Cheetos", "Doritos", "Pringles"], 2),
    ("What pastry does Grace Adler obsessively eat when stressed or celebrating?", "Krispy Kreme doughnuts", ["Cinnamon rolls", "Chocolate croissants", "Apple fritters"], 1),
    ("What neurosis does Will Truman exhibit regarding his stationery and office supplies?", "Obsessive organization and color-coding with red pens", ["Hoarding vintage fountain pens", "Refusing to use yellow sticky notes", "Only writing on legal parchment"], 2),
    ("What sport did Will Truman excel at as a figure skater during his youth?", "Ice skating", ["Roller derby", "Gymnastics", "Diving"], 2),
    ("What musical instrument did Grace Adler play in her high school band?", "Flute", ["Clarinet", "Violin", "Oboe"], 3),
    ("In college, before Will came out as gay, what was his relationship with Grace?", "They dated and got engaged to be married", ["They were platonic roommates only", "They competed for class valedictorian", "Grace was his tutor"], 1),
    ("On what holiday in college did Will finally break off his romantic engagement with Grace and realize he was gay?", "Thanksgiving", ["Valentine's Day", "New Year's Eve", "Christmas Eve"], 1),
    ("Who was Will's freshman college roommate who encouraged him to come to terms with his sexuality?", "Jack McFarland", ["Danny", "Rob", "Leo"], 2),
    ("What is Grace Adler's hometown in upstate New York?", "Schenectady", ["Albany", "Rochester", "Binghamton"], 2),
    ("What college did Grace attend where she met Will?", "Columbia University", ["Cornell University", "Barnard College", "Vassar College"], 1),

    # Family & Friends
    ("What is the name of Will Truman's mother, played by Blythe Danner?", "Marilyn Truman", ["Eleanor Truman", "Martha Truman", "Vivian Truman"], 2),
    ("What is the name of Will Truman's father, played by Sydney Pollack?", "George Truman", ["Arthur Truman", "Harold Truman", "Richard Truman"], 2),
    ("What is the name of Will's brother who had a one-night stand with Grace, causing major friction?", "Sam Truman", ["Paul Truman", "David Truman", "Mark Truman"], 2),
    ("Which actor portrayed Will's brother Sam in Season 1?", "John Slattery", ["Jon Tenney", "Dylan McDermott", "Dermot Mulroney"], 3),
    ("What is the name of Will's other brother, who is married with children?", "Paul Truman", ["Peter Truman", "Philip Truman", "Patrick Truman"], 3),
    ("Who played Grace Adler's eccentric, showtune-loving mother Bobbi Adler?", "Debbie Reynolds", ["Shirley MacLaine", "Carol Burnett", "Liza Minnelli"], 1),
    ("What musical instrument or prop does Bobbi Adler often use to make a dramatic entrance?", "Singing showtunes and wearing elaborate hats", ["A tambourine", "A feather boa", "A baton"], 1),
    ("Who played Grace's father Martin Adler in the original series episode 'Cheaters'?", "Alan Arkin", ["Robert Klein", "Jerry Stiller", "Carl Reiner"], 3),
    ("What is the name of Grace's older sister who is erratic and portrayed by Geena Davis in Season 6?", "Janet Adler", ["Joyce Adler", "Judy Adler", "Joanie Adler"], 2),
    ("What is the name of Grace's other sister who struggles with her weight, played by Sara Rue?", "Joyce Adler", ["Janet Adler", "Jessica Adler", "Jill Adler"], 2),

    # Jack's family and pets
    ("What is the name of the biological son Jack McFarland discovers he fathered via sperm donation?", "Elliott", ["Caleb", "Ethan", "Lucas"], 1),
    ("Which actor portrayed Jack's son Elliott as a teenager?", "Michael Angarano", ["Josh Hutcherson", "Frankie Muniz", "Logan Lerman"], 2),
    ("What was the name of Elliott's mother, a nurse who had used Jack's anonymous sperm donation?", "Bonnie", ["Brenda", "Barbara", "Beatrice"], 2),
    ("Which actress played Elliott's lesbian mother Bonnie?", "Rosie O'Donnell", ["Jane Lynch", "Sandra Bernhard", "Kathy Griffin"], 2),
    ("What is the name of Jack's biological father, whom he tracked down only to discover he had passed away?", "Joe Black", ["Frank McFarland", "Walter White", "Charles Miller"], 3),
    ("What is the name of Jack's stylish mother, played by Christine Ebersole?", "Judith McFarland", ["Constance McFarland", "Evelyn McFarland", "Beatrice McFarland"], 3),
    ("What pet pig did Jack adopt in Season 4?", "Baby Glenn", ["Porky", "Hamlet", "Truffles"], 3),
    ("What was the name of the theater camp Jack McFarland attended as a boy?", "Camp Ovation", ["Camp Broadway", "Starlight Academy", "Applause Haven"], 3),
    ("What physical dance move does Jack frequently perform when excited, throwing his arms side to side?", "The Jack Shuffle", ["The Jazz Flick", "The Twirl", "The Kickstep"], 3),
    ("In which season did Jack first discover he had a biological son named Elliott?", "Season 3", ["Season 1", "Season 2", "Season 5"], 2),

    # Karen's lifestyle and surroundings
    ("What is the name of Karen Walker's regular bartender who serves her at high-end spots?", "Smitty", ["Mac", "Tommy", "Barney"], 2),
    ("What tragedy-laden stories does Smitty usually tell Karen, which she finds hilarious?", "Tales of personal misfortune, jail time, and loss", ["Stories about his failing marriage", "Jokes about celebrities", "Complaints about his low wages"], 2),
    ("What is the name of Karen's beloved sister who was trapped in an asylum?", "Virginia", ["Victoria", "Valerie", "Veronica"], 3),
    ("What is Karen Walker's preferred method of waking up in the morning?", "A cocktail and a cocktail shaker shaken by Rosario", ["An espresso machine", "A cold shower", "A personal trainer"], 2),
    ("What name does Karen playfully call Grace, referring to her ginger curls and height?", "\"Toots\" or \"Honey\"", ["\"Red\" or \"Freckles\"", "\"Carrot\" or \"Stretch\"", "\"Ginger\" or \"Legs\""], 2),
    ("What nickname does Karen constantly use when addressing Will Truman?", "\"Willie\"", ["\"Billy\"", "\"Trumy\"", "\"Lawyer boy\""], 1),
    ("How does Karen regularly refer to Jack McFarland?", "\"Jackie\"", ["\"Sparky\"", "\"Jackie Boy\"", "\"Action Jack\""], 1),
    ("What is the name of Karen Walker's favorite jewelry store where she has unlimited credit?", "Cartier", ["Tiffany & Co.", "Harry Winston", "Van Cleef & Arpels"], 2),
    ("What private helicopter service does Karen frequently use to bypass Manhattan traffic?", "Walker Aviation", ["Manhattan Air", "Skyline VIP", "Hamptons Copter"], 3),
    ("What kind of pills does Karen Walker notoriously consume throughout the day?", "Uppers and downers in a mix she calls candy", ["Only aspirin", "Only homeopathic herbs", "Only chewable vitamins"], 1),

    # Will Truman legal career
    ("What law school did Will Truman graduate from?", "Columbia Law School", ["Harvard Law School", "NYU School of Law", "Yale Law School"], 1),
    ("What was the name of the prestigious law firm where Will was a senior partner early in the show?", "Doucette & Stein", ["Sterling & Cooper", "Crane, Poole & Schmidt", "Lockhart & Gardner"], 2),
    ("Who was Will's wealthy, eccentric senior partner played by Sydney Pollack's contemporary, Gregory Hines?", "Ben Doucette", ["Mr. Stein", "Mr. Higgins", "Arthur Doucette"], 2),
    ("Who played Will's eccentric, reclusive boss Mr. Stein who returned to the firm after years in an institution?", "Gene Wilder", ["Carl Reiner", "Mel Brooks", "Alan Alda"], 1),
    ("What is the title of the two-part episode featuring Gene Wilder as Mr. Stein?", "\"Boardroom Bunny\"", ["\"The Lawyer Awakens\"", "\"Legal Eagles\"", "\"Wilder Days\""], 3),
    ("After leaving Doucette & Stein, what business entity did Will form with Karen's financial backing?", "A private solo practice", ["A non-profit legal clinic", "A sports agency", "A catering firm"], 2),
    ("What luxury retail chain hired Will Truman as head of their legal department in Season 7?", "Barneys New York", ["Bergdorf Goodman", "Bloomingdale's", "Saks Fifth Avenue"], 2),
    ("What was Will Truman's childhood nickname that embarrassed him?", "\"Piglet\"", ["\"Chubby\"", "\"Little Truman\"", "\"Smiley\""], 3),
    ("What sport did Will play in high school that surprises people because of his neurotic nature?", "Ice hockey", ["Basketball", "Wrestling", "Lacrosse"], 2),
    ("What musical artist is Will Truman secretly obsessed with despite pretending to be sophisticated?", "Barry Manilow", ["Celine Dion", "Michael Bolton", "Kenny G"], 1),

    # Grace Adler design and lifestyle
    ("In what building is Grace Adler Designs located in the original series?", "The Puck Building", ["The Flatiron Building", "The Chrysler Building", "The Woolworth Building"], 2),
    ("What is Grace Adler's primary phobia that sends her screaming?", "Bugs and insects", ["Heights", "Germs", "Enclosed spaces"], 2),
    ("What food item did Grace famously try to retrieve from the garbage can in her kitchen?", "A whole roasted chicken / ribs", ["A gourmet pizza", "A chocolate cake", "A blueberry pie"], 2),
    ("What is Grace's favorite Broadway musical of all time, which she constantly references?", "\"The Music Man\"", ["\"Annie\"", "\"Wicked\"", "\"Chicago\""], 3),
    ("Which celebrity's bathroom did Grace Adler famously get the job to redesign in Season 2?", "Rudy Giuliani's mayoral mansion", ["Donald Trump's penthouse", "Joan Rivers' apartment", "Martha Stewart's studio"], 3),
    ("What did Grace accidentally inject into her lips before a major date?", "A collagen bee-venom concoction", ["Botox", "Saline", "Cooking oil"], 3),
    ("What item of clothing did Grace wear in the episode 'Das Boob' that inflated with water?", "A water-filled bra", ["A blow-up jacket", "Inflatable shoulder pads", "Padded bike shorts"], 1),
    ("In 'Das Boob', what happens to Grace's water bra at the art gallery opening?", "It gets punctured and squirts water across the room", ["It freezes solid in the cold air", "It explodes with a loud pop", "It leaks slowly down her shoes"], 1),
    ("What high-end wedding dress boutique did Grace and Karen visit while pretending to be brides?", "Vera Wang", ["Kleinfeld", "Prada", "Carolina Herrera"], 2),
    ("What is the name of Grace Adler's first serious fiancé seen in the Pilot episode?", "Danny", ["Leo", "Nathan", "Mark"], 1),

    # The Core Four dynamics & game nights
    ("What board game or party game do Will and Grace play with friends Rob and Ellen?", "\"Pyramid\" / Celebrity Charades", ["Monopoly", "Trivial Pursuit", "Scrabble"], 2),
    ("Who are the happily married, competitive friends who regularly play game nights with Will and Grace?", "Rob and Ellen", ["Joe and Larry", "Bob and Carol", "Kevin and Donna"], 1),
    ("What was the name of the gay couple who were close friends with Will and Grace and adopted a baby?", "Joe and Larry", ["David and Mark", "Brian and Peter", "Kevin and Scott"], 2),
    ("What is the name of the baby girl adopted by Joe and Larry in Season 3?", "Hannah", ["Emma", "Lily", "Sophia"], 3),
    ("What does Karen Walker call Grace's breasts in several episodes?", "\"The girls\" or \"flapjacks\"", ["\"The twins\"", "\"The headlights\"", "\"The cushions\""], 3),
    ("Which character famously screams 'Oh, honey...' as a condescending intro to an insult?", "Karen Walker", ["Grace Adler", "Jack McFarland", "Bobbi Adler"], 1),
    ("What is Will's favorite cocktail to prepare for himself at the bar cart?", "A clean gin martini with an olive", ["A Manhattan", "An Old Fashioned", "A Scotch on the rocks"], 2),
    ("What color was the sweater that Will and Grace bickered over owning and sharing?", "A yellow cashmere sweater", ["A red merino turtleneck", "A blue cardigan", "A green cable-knit"], 3),
    ("What is the name of the annoying upstairs neighbor who constantly taps dance steps and causes noise?", "Val Bassett", ["Mrs. Timmons", "Miss Crandall", "Mrs. Freeman"], 2),
    ("Which actress portrayed the unhinged upstairs neighbor Val Bassett?", "Molly Shannon", ["Cheri Oteri", "Ana Gasteyer", "Amy Poehler"], 1),
]

assert len(raw_questions) == 100, f"Expected 100 questions, got {len(raw_questions)}"

questions = []
for i, (q, correct, distractors, d) in enumerate(raw_questions):
    assert len(distractors) == 3, f"Q{i+1} does not have 3 distractors: {distractors}"
    assert len(set([correct] + distractors)) == 4, f"Q{i+1} has duplicates: {[correct] + distractors}"
    
    target_idx = i % 4
    opts = list(distractors)
    opts.insert(target_idx, correct)
    
    questions.append({
        "show": "Will & Grace",
        "q": q,
        "options": opts,
        "answer": target_idx,
        "d": d
    })

with open("tools/staging/will_and_grace_batch1.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)

print(f"Successfully generated batch 1 with {len(questions)} questions.")
