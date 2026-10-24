#!/usr/bin/env python3
import json

raw_questions = [
    # Leo Markus (Harry Connick Jr.) arc
    ("What is Leo Markus's legal first name on Will & Grace?", "Marvin", ["Mortimer", "Maurice", "Maxwell"], 2),
    ("What is Dr. Leo Markus's medical profession?", "Doctor / obstetrician with Doctors Without Borders", ["Pediatric surgeon", "Cardiologist", "Neurologist"], 1),
    ("How do Grace Adler and Leo Markus first meet in Season 5?", "Grace mistakes his horse-drawn carriage in Central Park for an available ride", ["They reach for the same melon at Zabar's", "He treats her broken finger in the ER", "They get stuck in an elevator at Bloomingdale's"], 2),
    ("Which celebrity singer and actor played Leo Markus?", "Harry Connick Jr.", ["Michael Bublé", "Bobby Darin", "Marc Anthony"], 1),
    ("Where do Grace and Leo get married on a spontaneous whim in Season 5?", "In Central Park on The Today Show", ["At City Hall in Manhattan", "In Las Vegas at the Little White Chapel", "On a beach in Montauk"], 2),
    ("Why was Grace and Leo's initial Today Show wedding invalid?", "The officiant was not legally ordained in New York", ["Grace had not signed the marriage certificate", "Leo was still legally married to an ex", "The ceremony occurred outside city boundaries"], 3),
    ("Where do Grace and Leo hold their lavish, official second wedding ceremony?", "A synagogal hall in New York City", ["A vineyard in Long Island", "A cathedral in Brooklyn", "A country club in Westchester"], 2),
    ("To what country does Leo travel with Doctors Without Borders, putting strain on his marriage to Grace?", "Cambodia", ["Guatemala", "Sudan", "Kenya"], 2),
    ("What devastating betrayal does Leo confess to Grace after returning from Cambodia?", "He had a one-night stand with another doctor", ["He gambled away their life savings", "He decided to move to Africa permanently", "He fathered a child with a local nurse"], 1),
    ("What was the name of the woman Leo cheated on Grace with in Cambodia?", "Diane", ["Chloe", "Sasha", "Becca"], 2),
    ("What shocking revelation does Grace learn about Diane (played by Mira Sorvino)?", "Diane was the only woman Will Truman ever slept with", ["Diane was Leo's former fiancée", "Diane was Karen's estranged half-sister", "Diane was Grace's college roommate"], 1),
    ("Where do Grace and Leo move briefly into an apartment before their marriage unravels?", "Brooklyn", ["Queens", "Hoboken", "Staten Island"], 2),
    ("On an airplane to London in Season 8, what unexpected encounter occurs between Grace and Leo?", "They run into each other and consummate their lingering feelings", ["They argue over their divorce papers", "Leo introduces Grace to his new pregnant wife", "Grace spills red wine on Leo's tuxedo"], 2),
    ("What is the name of the daughter Grace gives birth to as a result of her airplane reunion with Leo?", "Laila", ["Sarah", "Hannah", "Maya"], 2),
    ("In the original Season 8 finale, whom does Grace's daughter Laila marry in college?", "Will's son Ben", ["Jack's son Elliott", "Karen's stepson Mason", "Joe and Larry's daughter Hannah"], 1),

    # Vince D'Angelo (Bobby Cannavale) arc
    ("What is Vince D'Angelo's profession when he first meets Will Truman?", "NYPD police officer", ["FDNY firefighter", "Paramedic", "District Attorney investigator"], 1),
    ("Which actor portrayed Will Truman's major long-term love interest Vince D'Angelo?", "Bobby Cannavale", ["Mark Ruffalo", "Justin Theroux", "Joe Manganiello"], 1),
    ("How do Will and Vince first cross paths in Season 6?", "Vince pulls Will and Grace over for a traffic violation", ["Vince responds to a noise complaint at Will's apartment", "They meet at a gay bar in Chelsea", "Vince investigates a theft at Grace Adler Designs"], 2),
    ("What is Vince D'Angelo's ethnic heritage that plays a prominent comedic role in his family episodes?", "Italian-American", ["Irish-American", "Greek-American", "Puerto Rican"], 1),
    ("What is the name of Vince's eccentric sister who works at a toll booth?", "Ro (Rosalba)", ["Gina", "Maria", "Carmela"], 2),
    ("Which actress played Vince D'Angelo's sister Ro?", "Michele Lee", ["Rosie Perez", "Marisa Tomei", "Mira Sorvino"], 3),
    ("Why does Vince lose his job with the NYPD in Season 7?", "He falls asleep on stakeout duty after comforting Will", ["He punches a superior officer", "He fails a mandatory drug test", "He accidentally shoots a department vehicle"], 3),
    ("After being suspended from the police force, what job does Vince take with Karen's help?", "Head of Loss Prevention / Security at Barneys New York", ["A bouncer at a Chelsea nightclub", "A personal bodyguard for Stan Walker", "A driver for a limousine company"], 2),
    ("What is the name of Vince D'Angelo's best friend and former police partner?", "Joe", ["Sal", "Tony", "Frankie"], 3),
    ("Why do Will and Vince break up at the end of Season 7?", "Vince needs time apart to figure out his life and career", ["Will discovers Vince is cheating on him", "Vince is offered a police chief job in Chicago", "Will refuses to move in with Vince"], 2),
    ("In Season 8, what event brings Will and Vince back together?", "The death of Will's father George Truman", ["Grace's wedding", "Karen's charity gala", "A chance meeting at an art museum"], 2),
    ("What is the name of Will and Vince's son shown in the flash-forward in the original series finale?", "Ben", ["George", "Leo", "Lucas"], 2),
    ("In the 2017 revival, what was revealed about Will and Vince's relationship status?", "They had married but later divorced, remaining amicable", ["They were still happily married", "Vince had passed away", "They never actually dated and it was all a dream"], 2),
    ("What was the occupation of Vince's new husband whom Will meets in the revival?", "A fellow police officer", ["A dentist", "A Broadway actor", "A real estate agent"], 3),
    ("What Emmy Award did Bobby Cannavale win for his role as Vince D'Angelo in 2005?", "Outstanding Guest Actor in a Comedy Series", ["Outstanding Supporting Actor in a Comedy Series", "Outstanding Lead Actor in a Comedy Series", "Screen Actors Guild Best Actor"], 2),

    # Nathan (Woody Harrelson) arc
    ("Which Hollywood star played Grace's scruffy, unconventional boyfriend Nathan in Season 3 and 4?", "Woody Harrelson", ["Matthew McConaughey", "Owen Wilson", "Luke Wilson"], 1),
    ("Where did Nathan live when Grace first met him?", "Across the hall in an apartment in Will's building", ["Down the street in a brownstone", "In a loft in SoHo", "In a houseboat in New Jersey"], 2),
    ("What unusual habit of Nathan's frequently shocked Will and Grace?", "Walking around his apartment and hallway in the nude", ["Eating raw meat straight from the fridge", "Practicing bagpipes late at night", "Hoarding abandoned pigeons"], 2),
    ("What outdoor hobby was Nathan passionate about?", "Making elaborate ice sculptures", ["Fly fishing in Central Park", "Urban rock climbing", "Beekeeping on the fire escape"], 3),
    ("Where was Nathan originally from?", "Minnesota", ["Texas", "Montana", "Ohio"], 3),
    ("How did Nathan and Grace's relationship end right when it seemed at its peak?", "Grace pressured him into proposing, and he panicked and broke up with her", ["Nathan took a job in Alaska", "Grace caught Nathan kissing Karen", "Nathan confessed he was already married"], 1),
    ("What game did Nathan, Grace, Will, and Karen play that led to competitive bickering?", "Charades / Celebrity", ["Pictionary", "Poker", "Twister"], 2),
    ("How many episodes did Woody Harrelson appear in as Nathan across Seasons 3 and 4?", "7 episodes", ["3 episodes", "12 episodes", "15 episodes"], 3),

    # Danny (Pilot fiancé)
    ("Who was Grace's fiancé in the very first episode (Pilot) of Will & Grace?", "Danny", ["Nathan", "Leo", "Mark"], 1),
    ("Why did Grace decide not to marry Danny in the Pilot?", "She realized she was settling and ran out of the wedding to be with Will", ["Danny admitted he was gay", "Danny was caught cheating with the bridesmaid", "Danny lost his job on the wedding day"], 1),
    ("What business did Danny run in the pilot episode?", "A dermatology practice", ["A law firm", "A sports apparel business", "A restaurant chain"], 3),

    # Barry (Dan Futterman)
    ("Who played Will and Jack's newly out-of-the-closet cousin Barry in Season 5?", "Dan Futterman", ["Justin Theroux", "Taye Diggs", "Patrick Dempsey"], 2),
    ("Why did Jack and Will initially take Barry under their wings?", "To give him a gay makeover and teach him how to date men", ["To help him sue his employer for discrimination", "To find him an apartment in Chelsea", "To cast him in Jack's cabaret show"], 2),
    ("What unexpected turn happened after Barry's dramatic makeover?", "He became extremely handsome and desirable, leading Will and Jack to fight over him", ["He decided to return to his ex-wife", "He moved to San Francisco to become a monk", "He became an obnoxious fashion critic who insulted them"], 1),
    ("Whom did Barry ultimately choose between Will and Jack?", "Neither—he wanted to play the field and date around", ["Will", "Jack", "A random man at the gym"], 2),

    # Stuart Lamarack (Dave Foley)
    ("Which comedian and actor played Jack's wealthy, sweet boyfriend Stuart Lamarack in Season 6?", "Dave Foley", ["Kevin McDonald", "Scott Thompson", "Mark McKinney"], 2),
    ("What was Stuart's profession on the show?", "A wealthy client of Will's firm / real estate heir", ["A television producer", "A plastic surgeon", "An art dealer"], 3),
    ("What lavish gift did Stuart buy Jack that caused friction with Will?", "A luxury high-end apartment / expensive lifestyle", ["A private jet ride to Paris", "A diamond-encrusted watch", "A red sports convertible"], 3),
    ("Why did Jack and Stuart eventually break up?", "Jack cheated on Stuart with another man", ["Stuart moved back to Canada", "Stuart went bankrupt", "Jack realized Stuart was secretly married"], 2),

    # James Hanson (Taye Diggs)
    ("Which actor played James Hanson, the handsome Canadian Will falls for in Season 8?", "Taye Diggs", ["Blair Underwood", "Shemar Moore", "Idris Elba"], 1),
    ("Why did James Hanson need to marry an American citizen?", "To avoid deportation back to Canada and obtain a green card", ["To inherit his grandfather's estate", "To join the New York Bar Association", "To adopt a foster child"], 2),
    ("Who initially offered to marry James to help him stay in the US?", "Grace Adler", ["Karen Walker", "Rosario Salazar", "Jack McFarland"], 2),
    ("What turned Will completely off James right before the planned green card wedding?", "James revealed an arrogant, demanding, and rude personality at the rehearsal dinner", ["James revealed he was secretly straight", "James stole Karen's diamond necklace", "James had a secret criminal record in Montreal"], 2),

    # Matthew (Patrick Dempsey)
    ("Which Grey's Anatomy star played Will's closeted sportscaster boyfriend Matthew in Season 6?", "Patrick Dempsey", ["Eric Dane", "Justin Chambers", "TR Knight"], 1),
    ("What was Matthew's profession that caused him to keep his sexuality secret?", "Television sports anchor", ["NFL quarterback", "High school basketball coach", "Sports agent"], 2),
    ("Why did Will break up with Matthew?", "Will refused to be forced back into the closet and hide in public", ["Matthew got engaged to a female supermodel", "Matthew refused to introduce Will to his children", "Matthew moved to Los Angeles for ESPN"], 1),

    # Michael (Chris Potter)
    ("What was the name of Will Truman's long-term ex-boyfriend with whom he shared a seven-year relationship?", "Michael", ["David", "Jason", "Brian"], 2),
    ("In Season 2, why does Will become upset when Michael visits?", "Michael wants to adopt a baby with his new partner", ["Michael asks Will to return all their shared art", "Michael writes a tell-all memoir about their relationship", "Michael starts dating Jack"], 2),
    ("Which Canadian actor played Will's ex Michael?", "Chris Potter", ["Paul Gross", "Peter Gallagher", "Gordon Pinsent"], 3),

    # Claire (Megyn Price)
    ("What was the name of Will's high school girlfriend who asked him to father her child in Season 2?", "Claire", ["Chloe", "Catherine", "Cynthia"], 2),
    ("To which European city did Claire plan to move with the baby, causing Will to withdraw his consent?", "Paris", ["London", "Rome", "Barcelona"], 2),

    # Ben Doucette (Gregory Hines) & Grace
    ("Which famous tap dancer and actor played Will's boss Ben Doucette who dated Grace?", "Gregory Hines", ["Savion Glover", "Maurice Hines", "Bill Irwin"], 1),
    ("Why was Will deeply uncomfortable with Grace dating Ben Doucette?", "Ben was Will's boss and managing partner at the law firm", ["Ben had previously represented Will's father in a lawsuit", "Ben was married to Will's cousin", "Ben refused to promote Will unless Grace stayed with him"], 1),
    ("How did Grace and Ben Doucette's romance end?", "They realized they wanted different things and parted ways amicably", ["Ben was arrested for securities fraud", "Grace caught Ben cheating on a business trip", "Ben fired Will in a fit of rage"], 2),

    # Karen's romantic arcs: Lyle Finster, Malcolm Widmark, Nikki Green
    ("Which Monty Python comedy icon played Lyle Finster, Karen's brief husband in Season 6?", "John Cleese", ["Eric Idle", "Michael Palin", "Terry Jones"], 1),
    ("How was Lyle Finster related to Karen's former stepdaughter-in-law Lorraine?", "He was Lorraine's father", ["He was Lorraine's ex-husband", "He was Lorraine's uncle", "He was Lorraine's brother"], 2),
    ("Which British actress played Lorraine Finster, Stan Walker's mistress who became Karen's rival?", "Minnie Driver", ["Helena Bonham Carter", "Rachel Weisz", "Emma Thompson"], 1),
    ("Where did Karen and Lyle Finster get married in the Season 6 finale?", "Las Vegas", ["The Plaza Hotel", "Stan's yacht in the Caribbean", "A castle in Scotland"], 2),
    ("How long did Karen and Lyle's marriage last before she demanded a divorce?", "About twenty minutes at the wedding reception", ["Two weeks", "Six months", "One year"], 2),
    ("Which Emmy-winning actor played Malcolm Widmark, the secret government agent who loved Karen in Seasons 7 & 8?", "Alec Baldwin", ["Jeff Daniels", "James Woods", "Kelsey Grammer"], 1),
    ("Why had Malcolm Widmark entered Karen's life originally?", "He helped Stan Walker fake his death to escape the mob / government scrutiny", ["He was auditing Karen's taxes for the IRS", "He was hired by Beverley Leslie to spy on her", "He was investigating Rosario's immigration status"], 2),
    ("In the revival (Season 11), what groundbreaking romantic storyline did Karen have?", "A romantic relationship with a woman named Nikki Green", ["A romance with a younger male supermodel", "An engagement to Beverley Leslie", "Marriage to an Italian count"], 2),
    ("Which Orange Is the New Black and Handmaid's Tale star played Karen's girlfriend Nikki Green?", "Samira Wiley", ["Danielle Brooks", "Uzo Aduba", "Laverne Cox"], 2),
    ("What was Nikki Green's profession in the revival?", "A baseball player / sports figure", ["An interior designer", "A mixologist", "A corporate CEO"], 3),

    # Revival romantic arcs: McCoy Whitman, Estefan Gloria
    ("Which White Collar and Magic Mike star played Will's handsome news anchor fiancé McCoy Whitman in the revival?", "Matt Bomer", ["Cheyenne Jackson", "Jonathan Groff", "Neil Patrick Harris"], 1),
    ("What career opportunity caused McCoy Whitman to postpone his wedding to Will in Season 11?", "A prime news anchor job in London", ["A network morning show host in Los Angeles", "A political campaign spokesperson in Washington", "A foreign correspondent gig in Tokyo"], 2),
    ("What was the name of Jack's passionate, dramatic flight attendant husband in the revival?", "Estefan Gloria", ["Carlos Sanchez", "Mateo Morales", "Diego Ortiz"], 1),
    ("Which actor and internet creator portrayed Estefan Gloria?", "Brian Jordan Alvarez", ["Benito Skinner", "Bowen Yang", "Harvey Guillén"], 2),
    ("Where did Jack and Estefan Gloria get married in the Season 10 finale?", "In an airport terminal / gate waiting area", ["At a Spanish tapas restaurant", "On top of the Empire State Building", "In Will and Grace's living room"], 2),
    ("Who officiated Jack and Estefan's impromptu airport wedding ceremony?", "Miss Coco Peru", ["Beverley Leslie", "Will Truman", "Grace Adler"], 3),

    # Other romantic guests and blind dates
    ("Which Friends star guest-starred on Will & Grace as Karen's high-strung manicurist Cheryl?", "Lisa Kudrow", ["Courteney Cox", "Jennifer Aniston", "Jane Sibbett"], 1),
    ("Which SVU star played the hunky hot-dog vendor whom Will and Jack both fawn over?", "Christopher Meloni", ["Mariska Hargitay", "Dean Winters", "Ice-T"], 2),
    ("What happened when Will went on a blind date with a man played by Jon Stewart in Season 2?", "They realized they were stepbrothers or had identical neuroses", ["Will accidentally spilled hot soup on his lap", "The date was interrupted by Jack's performance", "Jon Stewart's character was still closeted"], 3),
    ("Which star played Grace's boyfriend Mark, who was terrified of confrontation and wept constantly?", "Ken Marino", ["Thomas Lennon", "Michael Ian Black", "Rob Corddry"], 3),
    ("Which actor played Grace's boyfriend Tom, whom she dated while living in Brooklyn?", "Corey Parker", ["Adam Goldberg", "Jon Tenney", "Josh Stamberg"], 3),
    ("What character did actor Jason Biggs play when he courted Grace in Season 8?", "Baby Glenn / a younger nerdy suitor named Glenn", ["A competitive interior designer", "Leo's medical assistant", "A city council member"], 3),
    ("In Season 1, what did Will's date with a competitive sports guy reveal about Will's self-image?", "Will tried desperately to hide his lack of sports knowledge", ["Will pretended to be an ex-college quarterback", "Will faked an injury to avoid playing touch football", "Will paid Jack to feed him football trivia through an earpiece"], 2),

    # More relationship themes and iconic moments
    ("Why did Grace and Will decide against having a child together via artificial insemination in Season 5?", "Grace met Leo right as the insemination procedure was scheduled", ["The clinic lost Will's sample", "Will decided he was not ready to be a father", "Karen convinced Grace that babies ruin carpets"], 1),
    ("In the Season 4 finale, what major life decision did Will and Grace make on the porch of a beach house?", "To have a baby together through artificial insemination", ["To get married for tax purposes", "To purchase a house together in Vermont", "To merge their businesses into one"], 1),
    ("What was the name of the hunky closeted cop Jack dated named Drew?", "Drew", ["Greg", "Dave", "Brett"], 3),
    ("What was Drew's occupation before Jack pushed him to come out of the closet?", "NYPD officer", ["Firefighter", "Secret Service agent", "Construction foreman"], 2),
    ("How did Jack react when Drew finally came out and left his wife for him?", "Jack panicked and found being Drew's primary emotional support overwhelming", ["Jack immediately proposed marriage", "Jack moved into Drew's precinct house", "Jack threw a lavish coming-out gala"], 2),
    ("Who was Grace's boyfriend Josh (Corey Parker) who drove Will crazy with what physical quirk?", "He kissed everyone on the mouth as a friendly greeting", ["He constantly gave unsolicited neck massages", "He refused to wear shoes indoors or outdoors", "He walked around snapping his chewing gum"], 2),
    ("In Season 3, what did Grace discover about her new boyfriend Ben Doucette's personal habits?", "He lived in a hyper-minimalist apartment with almost no furniture", ["He slept in a hyperbaric oxygen tent", "He owned forty identical black suits", "He kept a live terrarium of tarantulas"], 3),
    ("When Grace dated a man who was insecure about his height, what did she do that backfired?", "She secretly slouched and took off her high heels", ["She bought him elevator shoes as a gift", "She refused to stand next to him in photos", "She booked tables only at booths"], 2),
    ("What did Will and Grace realize every time either of them entered a serious relationship?", "Their co-dependent bond interfered with their romantic partners", ["Their romantic partners always fell in love with Jack", "They competed over who could spend more on anniversary gifts", "They immediately stopped talking for months at a time"], 1),
    ("In Season 8, whom did Will almost move to Chicago with before changing his mind?", "Vince D'Angelo", ["James Hanson", "Leo Markus", "Malcolm Widmark"], 2),
    ("What was the relationship status between Will Truman and Vince D'Angelo at the end of the original Season 8 finale?", "They reunited, had a son named Ben, and raised him together", ["They remained best friends but dated other men", "Vince moved to Rome and Will stayed in NYC", "They broke up permanently at Will's father's funeral"], 1),
    ("In the 2017 revival, how was Grace's marital status to Leo addressed?", "They were officially divorced, though Leo reappeared for key moments", ["They were still married and living in Brooklyn", "Leo had died of malaria in Africa", "Grace revealed she had never legally married him"], 1),
    ("When Leo Markus reappears in the revival, what advice does he give Grace about moving forward?", "To stop letting her past and fear of commitment define her future", ["To never start a business with Will", "To move to Paris and pursue painting", "To marry her newest client immediately"], 2),
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

with open("tools/staging/will_and_grace_batch2.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)

print(f"Successfully generated batch 2 with {len(questions)} questions.")
