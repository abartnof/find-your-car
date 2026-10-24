#!/usr/bin/env python3
import json

raw_questions = [
    # Rosario Salazar (Shelley Morrison) details
    ("Which actress portrayed Karen's devoted yet fiery maid Rosario Salazar?", "Shelley Morrison", ["Lupe Ontiveros", "Elizabeth Peña", "Alma Martinez"], 1),
    ("What was Rosario Salazar's native country before moving to the United States?", "El Salvador", ["Guatemala", "Honduras", "Mexico"], 1),
    ("What degree did Rosario hold in El Salvador before emigrating?", "A master's degree in clinical psychology", ["A law degree", "A medical doctorate", "A fine arts degree"], 2),
    ("Why did Rosario marry Jack McFarland in the Season 1 finale?", "To obtain legal US permanent residency and avoid deportation", ["Because she secretly loved him", "To inherit Stan Walker's fortune", "To help Karen win a legal settlement"], 1),
    ("Where was Jack and Rosario's green card marriage interview conducted in Season 2?", "At the INS (Immigration and Naturalization Service) office", ["At City Hall", "At Will Truman's law office", "At Karen's penthouse"], 2),
    ("What physical chore did Karen and Rosario famously gamble over with a coin toss?", "Cleaning the penthouse bathrooms", ["Polishing the family silverware", "Ironing Stan's silk boxer shorts", "Walking the estate guard dogs"], 3),
    ("What nickname does Karen frequently use to insult Rosario affectionately?", "\"Smudge\" or \"Cattle\"", ["\"Peasant\"", "\"Shorty\"", "\"Guppy\""], 3),
    ("What does Rosario call Karen in return during their heated comedic exchanges?", "\"Mommy dearest\" or \"Crazy alcoholic lady\"", ["\"Princess\"", "\"Your Majesty\"", "\"Dolly\""], 2),
    ("When Rosario suffered a health emergency in Season 7, what medical issue hospitalized her?", "Heart trouble / cardiovascular issues", ["Appendicitis", "A broken hip", "Gallstones"], 3),
    ("Why did Shelley Morrison not return for the 2017 Will & Grace revival?", "She had officially retired from acting", ["She was starring in another sitcom", "She had a scheduling conflict with theatre", "The producers chose not to include her"], 2),
    ("How did the 2017 revival handle the absence of Shelley Morrison's Rosario?", "Her character passed away, and a poignant funeral episode was held", ["She moved back to El Salvador to open a clinic", "She was travelling the world on Stan's yacht", "She married a wealthy diplomat in Miami"], 1),
    ("What was the title of the acclaimed revival episode dedicated to Rosario's funeral?", "\"Rosario's Quinceañera\"", ["\"Farewell Rosario\"", "\"Goodbye, Little Smudge\"", "\"A Maid to Remember\""], 1),
    ("Where does Karen spend most of the episode 'Rosario's Quinceañera' before attending the memorial?", "At a local bar drinking and reminiscing in denial", ["In her penthouse walk-in closet", "At Will's apartment crying", "At the cemetery sitting by the grave"], 2),
    ("What dress did Karen put Rosario in for her funeral service?", "Her classic maid's uniform", ["An extravagant white designer ballgown", "A black silk evening dress", "A traditional Salvadoran dress"], 2),

    # Beverley Leslie (Leslie Jordan)
    ("Which Emmy-winning comedic actor portrayed Karen's diminutive rival Beverley Leslie?", "Leslie Jordan", ["Nathan Lane", "Wallace Shawn", "Paul Reubens"], 1),
    ("What is Beverley Leslie's signature opening greeting whenever he enters a room with Karen?", "\"Well, well, well...\"", ["\"Hello, darling!\"", "\"My heavens!\"", "\"Look who it is!\""], 1),
    ("What is the name of Beverley Leslie's ultra-wealthy, rarely seen elderly wife?", "Crystal", ["Bambi", "Cordelia", "Eugenia"], 2),
    ("What does Beverley Leslie euphemistically call his handsome young male companions?", "His \"business associates\"", ["His \"personal trainers\"", "\"nephews from Atlanta\"", "\"interns\""], 1),
    ("What is the name of Beverley Leslie's handsome young companion who appears in multiple seasons?", "Benji", ["Chad", "Tyler", "Brandon"], 2),
    ("Which physical competition did Karen and Beverley engage in at a charity event?", "A competitive ballroom dance / benefit showdown", ["A golf tournament", "A tennis doubles match", "A marathon walk"], 2),
    ("How did Beverley Leslie's character die in the 2017 revival series?", "He was blown off a balcony in high winds during a storm", ["He choked on a caviar canapé", "He had a heart attack on his yacht", "He was struck by lightning on a golf course"], 2),
    ("Who inherited Beverley Leslie's immense estate after his freak accidental death?", "Karen Walker", ["Benji", "Jack McFarland", "His wife Crystal"], 2),
    ("Why did Karen end up losing the inheritance she received from Beverley Leslie?", "Beverley's will had a clause requiring her to stay sober or give it away", ["Crystal contested the will and proved Karen forged it", "Beverley was secretly bankrupt and buried in debt", "Benji stole the entire trust fund"], 3),
    ("In which season did Leslie Jordan first appear as Beverley Leslie?", "Season 3", ["Season 1", "Season 2", "Season 5"], 2),
    ("What Southern state does Beverley Leslie frequently reference as his home territory?", "Tennessee / Georgia (Deep South)", ["Texas", "Virginia", "Kentucky"], 2),

    # Bobbi Adler (Debbie Reynolds)
    ("Which iconic Hollywood legend portrayed Grace's flamboyant mother Bobbi Adler?", "Debbie Reynolds", ["Shirley MacLaine", "Carol Burnett", "Lauren Bacall"], 1),
    ("What is Bobbi Adler's favorite performing arts medium that she constantly incorporates into conversation?", "Musical theatre and Broadway showtunes", ["Opera arias", "Shakespearean sonnets", "Stand-up comedy"], 1),
    ("What is the recurring song Bobbi Adler sings to announce her presence?", "\"I told you so, I told you so!\"", ["\"Here she is, world!\"", "\"Broadway Baby!\"", "\"Adler is the name!\""], 2),
    ("How does Bobbi Adler constantly undermine Grace's physical self-esteem?", "Critiquing her chest size, posture, and wild curly hair", ["Complaining that she is too short", "Criticizing her choice of eyeglasses", "Mocking her lack of athletic skills"], 1),
    ("How does Bobbi Adler treat Will Truman compared to her own daughter Grace?", "She adores him and considers him the perfect son she never had", ["She is suspicious of him and demands rent", "She constantly confuses him with Jack", "She blames him for Grace being unmarried"], 1),
    ("What peculiar accessory collection does Bobbi Adler wear throughout her visits?", "Outlandish, oversized hats and wigs", ["Feather boas in every color", "Glittering tiaras", "Opera gloves"], 2),
    ("What was Bobbi Adler's advice to Grace regarding how to keep a husband happy?", "Wear lipstick, laugh at his jokes, and never let him see you chew", ["Always maintain a separate bank account", "Cook a roast every Sunday", "Never disagree in front of houseguests"], 2),
    ("In the Season 8 episode 'The Forgetting of the Adler', what milestone was Bobbi celebrating?", "Her birthday with an extravagant musical revue she wrote", ["Her wedding anniversary", "Her retirement from local community theater", "Her induction into the country club hall of fame"], 3),
    ("How was Debbie Reynolds' real-life passing honored in the 2017 revival?", "The characters commemorated Bobbi's passing with an emotional tribute episode", ["A scholarship was created at Columbia University", "Grace named her new design showroom after Bobbi", "Jack performed a one-man show in her honor"], 2),

    # Martin Adler (Alan Arkin & Robert Klein)
    ("What was Martin Adler's profession before retirement?", "A cab driver / small businessman in Schenectady", ["A college professor", "A real estate broker", "A pharmacist"], 3),
    ("In the Season 2 episode 'Cheaters', what shocking secret does Will discover about Martin Adler?", "Martin is having an extramarital affair with another woman", ["Martin has a secret second family in Canada", "Martin lost the family savings in Atlantic City", "Martin was fired from his job years ago"], 1),
    ("Where did Will accidentally spot Martin Adler kissing his mistress?", "At a restaurant where Will was having dinner", ["At a Broadway theatre during intermission", "In the lobby of Doucette & Stein", "At Grand Central Terminal"], 2),
    ("How did Grace react when Will initially hesitated to tell her about her father's affair?", "She was furious at Will for keeping such a monumental secret from her", ["She thanked him for sparing her feelings", "She refused to believe him and accused him of lying", "She immediately told her mother Bobbi"], 1),

    # Will's Parents: Marilyn & George Truman
    ("Which Tony and Emmy-winning actress played Will's mother Marilyn Truman?", "Blythe Danner", ["Jill Clayburgh", "Christine Lahti", "Candice Bergen"], 1),
    ("What is Marilyn Truman's stereotypical social background depicted on the show?", "A wealthy, emotionally reserved Connecticut WASP", ["An eccentric bohemian Greenwich Village artist", "A Midwestern suburban housewife", "A Southern high-society matriarch"], 1),
    ("What pet breed does Marilyn Truman passionately pamper throughout the series?", "Her pampered show poodles", ["Siamese cats", "Pekingese dogs", "Golden retrievers"], 2),
    ("Which Oscar-winning film director portrayed Will's father George Truman?", "Sydney Pollack", ["Mike Nichols", "Rob Reiner", "Barry Levinson"], 1),
    ("What was George Truman's secret affair that nearly destroyed his marriage to Marilyn?", "A long-term affair with a woman named Tina", ["An affair with Will's high school teacher", "An affair with Grace's mother Bobbi", "A fling with his legal secretary"], 1),
    ("Which Oscar-nominated actress played George Truman's mistress Tina?", "Lesley Ann Warren", ["Teri Garr", "Karen Black", "Diane Ladd"], 2),
    ("What vocal and physical persona did Tina exhibit that irritated Will to no end?", "A squeaky, baby-doll voice with overly dramatic affectations", ["A loud, booming Southern drawl", "A stern, monotone lecturing style", "A perpetual nervous giggling fit"], 2),
    ("How does George Truman tragically pass away in Season 8?", "He suffers a sudden fatal heart attack shortly after an argument with Will", ["He dies in a car crash on the Merritt Parkway", "He passes away peacefully in his sleep in Connecticut", "He suffers a stroke while on vacation in Florida"], 1),
    ("Why was Will particularly grief-stricken by his father's sudden death?", "They had had a bitter argument about George's lifestyle and never reconciled", ["George had disinherited Will from his will", "Will had forgotten to visit George for his 70th birthday", "George died before Will could introduce him to Vince"], 2),

    # Will's Brothers: Sam & Paul Truman
    ("What profession does Will's handsome brother Sam (John Slattery) practice?", "Contractor / carpenter", ["Investment banker", "Doctor", "Pilot"], 2),
    ("What shocking romantic encounter occurred between Grace and Sam Truman in Season 1?", "They hooked up and slept together, horrifying Will", ["They got engaged after a weekend in the Hamptons", "Grace hired Sam to design her showroom and kissed him", "Sam proposed to Grace to make Will jealous"], 1),
    ("Which actor portrayed Will's other brother, Paul Truman, in Season 3?", "Jon Tenney", ["Dermot Mulroney", "Timothy Busfield", "Josh Brolin"], 3),
    ("What was the source of tension between Will and his brother Paul?", "Paul was uncomfortable with Will being gay and avoided discussing it", ["Paul borrowed money from Will and refused to pay it back", "Paul was their father's favorite child", "Paul married Will's high school girlfriend"], 2),

    # Grace's Sisters: Janet & Joyce Adler
    ("Which Oscar-winning actress played Grace's wildly unpredictable sister Janet Adler in Season 6?", "Geena Davis", ["Susan Sarandon", "Sigourney Weaver", "Patricia Clarkson"], 1),
    ("What bizarre business venture does Janet Adler try to launch during her visit?", "Selling jewelry made from junk / found objects from her van", ["A gourmet cupcake food truck", "An astrology phone hotline", "A high-end psychic dog training service"], 2),
    ("Which actress played Grace's sister Joyce Adler in Season 3?", "Sara Rue", ["Melissa McCarthy", "Ricki Lake", "Camryn Manheim"], 2),
    ("What does Grace try to force her sister Joyce to do during her stay in New York?", "Stick to an intense diet and makeover regimen", ["Break up with her fiancé from Schenectady", "Audition for a Broadway musical chorus", "Take a job at Grace Adler Designs"], 2),

    # Val Bassett (Molly Shannon)
    ("Who is Val Bassett on Will & Grace?", "The wildly eccentric and unstable neighbor in Will and Grace's building", ["Karen's estranged half-sister", "Jack's acting coach rival", "Will's rival at Doucette & Stein"], 1),
    ("What did Val Bassett do when she discovered Grace's design sketches in the trash?", "She stole them and passed them off as her own work to clients", ["She framed them and gave them back as a gift", "She burned them on the building roof", "She submitted them to an interior design magazine"], 2),
    ("What did Val Bassett do when she became obsessed with Jack McFarland?", "She created a rival one-woman cabaret show and stalked him", ["She pretended to be his long-lost biological sister", "She bought out his acting school", "She hired a private detective to follow him"], 2),
    ("In the Season 1 episode 'A New Lease on Life', how does Val first enter Grace's world?", "Grace befriends her when Will and Grace temporarily stop living together", ["She moves into Will's apartment as a subletter", "She sits next to Grace at a coffee shop and weeps", "She is hired as a temp at Grace Adler Designs"], 2),
    ("What did Val Bassett steal from Grace's purse during one of their bizarre interactions?", "Grace's music box / treasured heirloom", ["Her credit cards", "Her apartment keys", "Her address book"], 3),

    # Rob & Ellen (Tom Gallop & Leigh-Allyn Baker)
    ("What are the names of Will and Grace's long-time married couple friends from college?", "Rob and Ellen", ["Bob and Carol", "Kevin and Donna", "Mark and Sarah"], 1),
    ("Why did Rob and Ellen dread game nights with Will and Grace?", "Will and Grace were hyper-competitive, toxic, and telepathically cutthroat", ["Will and Grace never brought food or drinks", "Will always cheated at Trivial Pursuit", "Grace constantly broke the game board in anger"], 1),
    ("What did Grace accidentally do at Rob and Ellen's wedding rehearsal in Season 2?", "She accidentally ruined Ellen's hair and read a disastrous personal toast", ["She spilled red wine on the bride's gown", "She kissed the groom in the coat closet", "She lost the wedding rings down the drain"], 2),
    ("What major life transition do Rob and Ellen make in later seasons?", "They have a baby and move out to New Jersey suburbs", ["They divorce and Rob comes out as gay", "They move to California to open a winery", "They win the New York State lottery"], 2),

    # Joe & Larry (Jerry Levine & Tim Bagley)
    ("What are the names of Will and Grace's long-term gay couple friends who adopt a daughter?", "Joe and Larry", ["Greg and Peter", "Kevin and Scott", "David and Michael"], 1),
    ("What is the name of Joe and Larry's adopted daughter?", "Hannah", ["Emma", "Chloe", "Olivia"], 2),
    ("Which character had a brief romantic fling with Larry in Season 8 when Larry and Joe separated?", "Will Truman", ["Jack McFarland", "Vince D'Angelo", "Barry"], 2),
    ("What was Larry's neurosis that frequently exasperated his partner Joe?", "Extreme anxiety, over-parenting, and theatrical melodrama", ["Compulsive hoarding of antiques", "Refusing to spend any money on vacations", "Obsessive gym workouts and diets"], 2),

    # Elliott & Jack's family tree
    ("How old was Elliott when he first tracked down his biological father Jack McFarland?", "12 years old", ["8 years old", "16 years old", "18 years old"], 3),
    ("How did Elliott find Jack McFarland in Season 3?", "Through an open sperm donor registry matching his file", ["He recognized Jack on a billboard in Times Square", "Karen accidentally leaked the donor records", "Elliott's mother Bonnie hired a private eye"], 2),
    ("What sport was Elliott passionate about playing, forcing Jack to learn about sports?", "Basketball", ["Baseball", "Ice hockey", "Soccer"], 2),
    ("What surprising decision did Elliott make in the 2017 revival regarding his own family?", "He had married a conservative woman and had a son who was sent to conversion camp", ["He had become a Catholic priest in Boston", "He moved to Europe to become a professional soccer player", "He opened a Broadway theatre agency in Chicago"], 2),
    ("What did Jack and Will do when they learned Elliott's son was being sent to a conversion camp?", "They infiltrated the camp and helped the young boy escape and feel loved", ["They sued the camp for emotional distress", "They bought the camp property and shut it down", "They protested outside with megaphones"], 2),
    ("What was the name of Elliott's conservative wife in the revival?", "Emma", ["Sarah", "Beth", "Megan"], 3),
    ("Who played Jack's mother Judith McFarland who kept secrets from Jack?", "Christine Ebersole", ["Bette Midler", "Carol Kane", "Patti LuPone"], 2),
    ("What shocking secret did Judith McFarland keep from Jack until his adulthood?", "She had hidden the identity of his real biological father", ["She was never legally married to his father", "She was secretly an heiress to a fortune", "She had put Jack up for adoption as a baby"], 2),

    # Smitty the bartender & quirky recurring figures
    ("What was the name of the elderly bartender at Karen's country club and upscale haunts?", "Smitty", ["Gus", "Walter", "Frank"], 1),
    ("How does Karen typically react when Smitty shares horrifying tragedies from his life?", "She bursts into laughter and asks for another drink", ["She writes him a massive check to help him", "She fires him on the spot", "She breaks down in sympathetic tears"], 1),
    ("What tragic story did Smitty recount about his twin brother?", "His twin was lost at sea or died in a freak factory explosion", ["His twin ran off with his bride on their wedding day", "His twin stole his identity and went to prison", "His twin was eaten by a circus bear"], 3),
    ("What was the name of Karen's beloved cook who constantly argued with Rosario?", "Consuela", ["Rosa", "Carmen", "Elena"], 3),
    ("Which character famously worked as a receptionist at Grace Adler Designs before Karen?", "There was never a regular receptionist before Karen", ["Dorothy", "Sheila", "Miriam"], 2),
    ("What happened when Karen temporarily hired a second assistant named Scott (played by Macaulay Culkin)?", "Scott was a precocious young divorce lawyer representing Stan against Karen", ["Scott was a spy sent by Beverley Leslie", "Scott organized a union among Karen's household staff", "Scott replaced Grace as head of the firm"], 2),
    ("Which character did Gene Wilder play in his two Emmy-winning guest appearances?", "Mr. Stein, Will's eccentric law firm senior partner", ["Grace's uncle who loved puzzles", "A judge presiding over Karen's divorce", "A Broadway director staging Jack's show"], 1),
    ("What bizarre habit did Gene Wilder's character Mr. Stein exhibit during meetings?", "Yelling abruptly to hide his confusion and memory lapses", ["Speaking only in rhymes", "Taking off his shoes and socks at the boardroom table", "Jumping on top of desks to deliver speeches"], 2),
    ("Which actor portrayed Ben Doucette, Will's charismatic boss at Doucette & Stein?", "Gregory Hines", ["James Earl Jones", "Courtney B. Vance", "Keith David"], 1),
    ("What hobby did Ben Doucette engage in that bonded him with Grace?", "Playing basketball and joking about Will's stiffness", ["Collecting antique pocket watches", "Cooking authentic Southern barbecue", "Restoring classic convertibles"], 3),

    # More supporting cast lore
    ("What was the name of the upstairs tenant whose apartment Will and Grace tried to buy to combine into a duplex?", "Mrs. Freeman", ["Mrs. Gable", "Mrs. Henderson", "Mrs. Dubcek"], 3),
    ("What did Will and Grace do to butter up the elderly tenant Mrs. Freeman?", "They baked for her, ran errands, and waited eagerly for her to move or pass away", ["They paid her two years of advance rent", "They redecorated her entire apartment for free", "They adopted her aggressive feral cat"], 2),
    ("What happened when Mrs. Freeman finally moved out of her apartment?", "A bidding war erupted, and another buyer snatched it from Will and Grace", ["Karen bought the apartment to use as a shoe closet", "The building board rejected Will's application", "Jack accidentally flooded the apartment with the bathtub"], 2),
    ("Which actress played Joanne, the snobbish member of Karen's country club who challenged Karen in a drinking contest?", "Susan Sarandon", ["Sigourney Weaver", "Annette Bening", "Kathleen Turner"], 2),
    ("What was Joanne's signature talent in her episode with Karen?", "Playing high-stakes bar games and matching Karen drink for drink", ["Sailing luxury racing yachts in Newport", "Performing stand-up comedy at charity galas", "Bidding millions at modern art auctions"], 2),
    ("Who played Karen's mother Lois Whitley, a con artist who tried to scam Grace?", "Suzanne Pleshette", ["Florence Henderson", "Marion Ross", "Shirley Jones"], 2),
    ("What scam did Karen's mother Lois try to pull with Grace?", "Using Grace to secure a fake interior design loan or real estate scam", ["Faking a slip-and-fall lawsuit against Doucette & Stein", "Stealing jewelry from Karen's Park Avenue safe", "Selling counterfeit antique paintings to Grace's clients"], 2),
    ("How did Karen feel about her mother Lois Whitley?", "She deeply distrusted her because Lois used her in grifts as a child", ["She worshiped her and called her daily", "She thought her mother was a saintly nun", "She had not seen her since infancy"], 1),
    ("What did Lois Whitley call Karen during their childhood con games?", "\"The mark\" or her little helper in scams", ["\"Her little angel\"", "\"Baby bird\"", "\"Sweet pea\""], 3),
    ("Which actress played Stan Walker's overbearing mother, Karen's mother-in-law Sylvia Walker?", "Eileen Brennan", ["Bea Arthur", "Estelle Getty", "Charlotte Rae"], 2),
    ("What was Sylvia Walker's nickname on the show?", "\"Big Sylvia\"", ["\"Mama Walker\"", "\"Queen Sylvia\"", "\"The General\""], 3),
    ("Which veteran actress played Zandra, Jack's raspy-voiced, cynical acting class instructor?", "Eileen Brennan", ["Carol Kane", "Charlotte Rae", "Rue McClanahan"], 2),
    ("What was Zandra's frequent cynical advice to Jack and her acting students?", "\"You have no talent!\"", ["\"Reach for the stars!\"", "\"Live the moment!\"", "\"Trust the script!\""], 2),
    ("Which Golden Globe-winning actress played Karen's friend who stole her maid in Season 4?", "Rosie O'Donnell", ["Lily Tomlin", "Candice Bergen", "Whoopi Goldberg"], 3),
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

with open("tools/staging/will_and_grace_batch3.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)

print(f"Successfully generated batch 3 with {len(questions)} questions.")
