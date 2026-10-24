#!/usr/bin/env python3
"""
Generate tools/staging/friends_batch4.json (100 questions, Deep Cuts & Character Lore).
"""
import sys
import os

from build_friends_batch import build_batch

questions = [
    {
        "q": "What Japanese men's cosmetic product did Joey promote in an infamous Tokyo television commercial?",
        "correct": "Ichiban, Lipstick for Men",
        "distractors": ["Samurai Hair Pomade", "Tokyo Blue Cologne", "Kabuki Facial Mud"],
        "d": 1
    },
    {
        "q": "What is Joey Tribbiani's signature four-word pickup line used throughout the series?",
        "correct": "\"How you doin'?\"",
        "distractors": ["\"Hey there, gorgeous!\"", "\"What's cookin', good-lookin'?\"", "\"Could you be sweeter?\""],
        "d": 1
    },
    {
        "q": "What passionate food philosophy does Joey scream when a date takes a french fry from his plate?",
        "correct": "\"JOEY DOESN'T SHARE FOOD!\"",
        "distractors": ["\"GET YOUR OWN FRIES!\"", "\"DON'T TOUCH MY PLATE!\"", "\"FOOD IS SACRED!\""],
        "d": 1
    },
    {
        "q": "What crime-fighting television pilot did Joey star in alongside an intelligent robot partner?",
        "correct": "'Mac and C.H.E.E.S.E.'",
        "distractors": ["'Robo-Cop and Joey'", "'Detective and Droid'", "'Cyber-Cop NYC'"],
        "d": 1
    },
    {
        "q": "What musical theater production did Joey star in where he portrayed Sigmund Freud?",
        "correct": "'Freud!'",
        "distractors": ["'Dr. Sigmund'", "'Id and Ego: The Musical'", "'Vienna Nights'"],
        "d": 2
    },
    {
        "q": "What song does Joey sing during his audition performance in the musical 'Freud!'?",
        "correct": "\"All you want is a dink, what you envy's a wink\"",
        "distractors": ["\"Dreams and Desires of the Subconscious Mind\"", "\"Tell Me About Your Mother\"", "\"The Psychoanalytic Rag\""],
        "d": 3
    },
    {
        "q": "What is the alias Phoebe Buffay frequently uses whenever she needs a fake identity?",
        "correct": "Regina Phalange",
        "distractors": ["Phyllis Nealon", "Anastasia Beaverhausen", "Helena Handbasket"],
        "d": 1
    },
    {
        "q": "What matching alias does Joey Tribbiani use when pretending to be an aristocratic businessman?",
        "correct": "Ken Adams",
        "distractors": ["Johnny Detroit", "Holden McGroin", "Jack Geller Jr."],
        "d": 2
    },
    {
        "q": "What terrifying three-dimensional wall art sculptures does Phoebe construct, featuring a woman crawling out of a frame?",
        "correct": "Gladys and Glynnis",
        "distractors": ["Bertha and Beatrice", "Agnes and Astrid", "Gertrude and Gwendolyn"],
        "d": 1
    },
    {
        "q": "What is the name of Joey's childhood imaginary friend who is a space cowboy?",
        "correct": "Maurice",
        "distractors": ["Cosmo", "Barnaby", "Buzz"],
        "d": 2
    },
    {
        "q": "What is the profession of Joey's imaginary friend Maurice?",
        "correct": "Space cowboy",
        "distractors": ["Time detective", "Submarine captain", "Alien chef"],
        "d": 2
    },
    {
        "q": "What was the name of the white ceramic canine statue that Joey bought and kept in the apartment?",
        "correct": "Pat the Dog",
        "distractors": ["Fido the Hound", "Spot the Terrier", "Rex the Marble Pooch"],
        "d": 2
    },
    {
        "q": "What bodily oddity did Chandler have surgically removed in Season 3?",
        "correct": "A third nipple (his 'nubbin')",
        "distractors": ["A sixth toe on his left foot", "A webbed finger", "A benign tailbone spur"],
        "d": 1
    },
    {
        "q": "What corporate acronym at Chandler's data processing office stands for 'Weekly Estimated Net Usage Statistics'?",
        "correct": "WENUS",
        "distractors": ["NEXUS", "MENUS", "TENUS"],
        "d": 1
    },
    {
        "q": "What corresponding annual data metric did Chandler complain about having to review?",
        "correct": "ANUS (Annual Net Usage Statistics)",
        "distractors": ["YEARUS", "CANUS", "TOTALUS"],
        "d": 1
    },
    {
        "q": "What stage name does Chandler's father Charles Bing use in his Las Vegas drag musical revue?",
        "correct": "Helena Handbasket",
        "distractors": ["Nora Bing Jr.", "Viva Las Diva", "Chloe Champagne"],
        "d": 1
    },
    {
        "q": "Which Hollywood actress famously portrayed Chandler's father, Charles Bing / Helena Handbasket?",
        "correct": "Kathleen Turner",
        "distractors": ["Faye Dunaway", "Glenn Close", "Sigourney Weaver"],
        "d": 1
    },
    {
        "q": "What title did Chandler's father's Las Vegas cabaret stage show carry?",
        "correct": "'Viva Las Gaygas'",
        "distractors": ["'Fabulous Bing'", "'The Vegas Queen Revue'", "'Midnight in Nevada'"],
        "d": 2
    },
    {
        "q": "To what remote country does Chandler purchase an expensive one-way ticket to escape Janice in Season 4?",
        "correct": "Yemen",
        "distractors": ["Oman", "Morocco", "Saudi Arabia"],
        "d": 1
    },
    {
        "q": "What fake residential address does Chandler invent in Yemen while speaking to Janice at the airport?",
        "correct": "\"15 Yemen Road, Yemen\"",
        "distractors": ["\"42 Desert Palm Way, Sana'a\"", "\"100 Camel Street, Yemen\"", "\"7 Oases Boulevard, Yemen\""],
        "d": 1
    },
    {
        "q": "Why does Chandler dread Thanksgiving dinner every year?",
        "correct": "His parents announced their divorce over roast turkey when he was nine years old",
        "distractors": ["He choked on a turkey bone at school and had a tracheotomy", "His pet dog ran away during the Macy's Thanksgiving Day Parade", "His mother burned down the family dining room while basting a turkey"],
        "d": 1
    },
    {
        "q": "What alternative non-Thanksgiving food did the young houseboy serve to Chandler's family during the divorce announcement?",
        "correct": "Tomato soup and grilled cheese sandwiches",
        "distractors": ["Hot dogs and macaroni and cheese", "Cheeseburgers and fries", "Spaghetti and meatballs"],
        "d": 3
    },
    {
        "q": "What 1950s-themed diner did Monica work at where she had to wear roller skates and a blonde wig?",
        "correct": "The Moondance Diner",
        "distractors": ["The Starlight Drive-In", "Mel's 50s Diner", "The Big Apple Hop"],
        "d": 1
    },
    {
        "q": "What prosthetic costume enhancement was Monica forced to wear while working at the Moondance Diner?",
        "correct": "Flame-retardant oversized artificial breasts",
        "distractors": ["A padded foam backside", "Neon flashing shoulder pads", "An inflatable beehive hairdo"],
        "d": 2
    },
    {
        "q": "What Italian restaurant hires Monica as head chef after she writes a scathing newspaper review of their food?",
        "correct": "Alessandro's",
        "distractors": ["Luigi's Ristorante", "Trattoria Bella", "Little Venice Bistro"],
        "d": 2
    },
    {
        "q": "Why does Monica hire Joey as a waiter at Alessandro's soon after taking the head chef position?",
        "correct": "So she can publicly fire him to intimidate the mutinous kitchen staff",
        "distractors": ["Because Joey desperately needed money to pay back Chandler", "Because Joey was fluent in traditional Italian cooking techniques", "To have an ally who could spy on the sous chefs"],
        "d": 1
    },
    {
        "q": "What high-end Manhattan restaurant does Monica run as head chef during the later seasons of the show?",
        "correct": "Javu",
        "distractors": ["Le Bistro", "Gusteau's", "L'Amour"],
        "d": 2
    },
    {
        "q": "What musical instrument does Monica play in her high school marching band?",
        "correct": "The glockenspiel",
        "distractors": ["The flute", "The clarinet", "The bass drum"],
        "d": 2
    },
    {
        "q": "What candy confection did Monica obsessively bake and distribute to all the building neighbors in Season 7?",
        "correct": "Holiday candy and chocolate truffles",
        "distractors": ["Peppermint bark", "Fudge brownies", "Almond biscotti"],
        "d": 2
    },
    {
        "q": "What cleaning appliance does Monica famously clean with an even smaller cleaning appliance?",
        "correct": "She cleans her full-size vacuum cleaner with a Dustbuster handheld vacuum",
        "distractors": ["She cleans her washing machine with a sponge brush", "She cleans her oven with an electric toothbrush", "She polishes her dishwasher with a jeweler's cloth"],
        "d": 1
    },
    {
        "q": "What breed of hairless sphynx cat does Rachel buy for one thousand dollars in Season 5?",
        "correct": "A hairless Sphynx cat",
        "distractors": ["A Persian show cat", "A Siamese pedigree kitten", "A Scottish Fold cat"],
        "d": 1
    },
    {
        "q": "What was the name of Rachel's hairless cat that Gunther eventually bought from her?",
        "correct": "Mrs. Whiskerson",
        "distractors": ["Fluffy", "Cleopatra", "Princess Sophia"],
        "d": 2
    },
    {
        "q": "What does Joey mistake Rachel's hairless cat for when he first sees it sitting on a cushion?",
        "correct": "\"It's not a cat! Why is it inside out?!\"",
        "distractors": ["\"A plucked Thanksgiving turkey!\"", "\"A giant rat with whiskers!\"", "\"An alien invasion specimen!\""],
        "d": 1
    },
    {
        "q": "What fashion apparel company hires Rachel away from Central Perk to sort coat hangers in a dark basement?",
        "correct": "Fortunata Fashions",
        "distractors": ["Style World", "Manhattan Garment Co.", "Empire Threads"],
        "d": 2
    },
    {
        "q": "Who was Rachel's sharp, demanding boss at Bloomingdale's who was tragically killed in a traffic accident?",
        "correct": "Joanna",
        "distractors": ["Sophie", "Nora", "Amanda"],
        "d": 2
    },
    {
        "q": "What long-suffering administrative assistant worked alongside Rachel under Joanna at Bloomingdale's?",
        "correct": "Sophie",
        "distractors": ["Chloe", "Mona", "Julie"],
        "d": 2
    },
    {
        "q": "What department at Bloomingdale's is Rachel transferred to, where she meets Joshua Burgin?",
        "correct": "Personal Shopping Department",
        "distractors": ["Men's High Fashion Fragrances", "Bridal Registry Salon", "Designer Handbags & Luggage"],
        "d": 2
    },
    {
        "q": "What iconic American fashion corporation employs Rachel for five seasons starting in Season 5?",
        "correct": "Ralph Lauren",
        "distractors": ["Calvin Klein", "Donna Karan New York (DKNY)", "Tommy Hilfiger"],
        "d": 1
    },
    {
        "q": "What is the name of Rachel's intimidating supervisor at Ralph Lauren?",
        "correct": "Mr. Zelner",
        "distractors": ["Mr. Waltham", "Mr. Kaplan", "Mr. Douglas"],
        "d": 2
    },
    {
        "q": "What blunder does Rachel commit during her initial interview with Mr. Zelner at Ralph Lauren?",
        "correct": "She accidentally kisses him on the cheek when leaving",
        "distractors": ["She spills hot coffee over his executive desk", "She insults the fabric of his necktie", "She gets her heel caught in his carpet and falls"],
        "d": 2
    },
    {
        "q": "What false rumor does Rachel invent to explain her bizarre conduct to Mr. Zelner during a later interview?",
        "correct": "She claims that Ralph Lauren himself is sexually infatuated with her",
        "distractors": ["She claims that she is suffering from temporary amnesia", "She claims she is an undercover investigative reporter", "She claims she was auditioning for a fashion documentary"],
        "d": 2
    },
    {
        "q": "Which younger sister of Rachel arrives in New York in Season 6, played by Reese Witherspoon?",
        "correct": "Jill Green",
        "distractors": ["Amy Green", "Tori Green", "Chloe Green"],
        "d": 1
    },
    {
        "q": "Why does Rachel become incensed when her spoiled sister Jill visits New York?",
        "correct": "Jill starts dating Ross purely out of spite toward Rachel",
        "distractors": ["Jill steals Rachel's designer clothes and pawns them", "Jill tries to get Rachel fired from Ralph Lauren", "Jill invites their father to Monica's apartment"],
        "d": 1
    },
    {
        "q": "What is the name of Rachel and Monica's beloved childhood dog whose death was hidden from Ross for years?",
        "correct": "Chi-Chi",
        "distractors": ["LaPooh", "Rover", "Buster"],
        "d": 2
    },
    {
        "q": "What did Jack and Judy Geller tell Ross had happened to Chi-Chi instead of telling him the dog died?",
        "correct": "She was sent to live on the Milner family farm in Connecticut",
        "distractors": ["She was adopted by a family of circus performers", "She ran off to the Adirondack mountains", "She joined a military rescue team"],
        "d": 2
    },
    {
        "q": "What was the name of Rachel's childhood pet dog who was tragically run over by an ice cream truck?",
        "correct": "LaPooh",
        "distractors": ["Chi-Chi", "Fifi", "Peaches"],
        "d": 3
    },
    {
        "q": "What subject does Ross teach as a tenured professor at New York University (NYU)?",
        "correct": "Paleontology",
        "distractors": ["Archaeology", "Anthropology", "Evolutionary Biology"],
        "d": 1
    },
    {
        "q": "What affected accent does Ross use during his first lecture as an NYU professor because of performance anxiety?",
        "correct": "A phony British accent",
        "distractors": ["A thick Southern drawl", "A French accent", "An aristocratic Boston Brahmin accent"],
        "d": 1
    },
    {
        "q": "What unusual musical hobby does Ross demonstrate for the group, claiming he hasn't played his 'sound' in years?",
        "correct": "Experimental synthesized keyboard electronic music",
        "distractors": ["The bagpipes", "The accordion", "The didgeridoo"],
        "d": 1
    },
    {
        "q": "What musical instrument does Ross attempt to learn to play for Monica and Chandler's wedding ceremony?",
        "correct": "The Scottish Highland bagpipes",
        "distractors": ["The classical cello", "The harp", "The French horn"],
        "d": 1
    },
    {
        "q": "What song does Ross painfully screech on the bagpipes while asking the gang to sing along?",
        "correct": "\"Celebration\" by Kool & the Gang",
        "distractors": ["\"Auld Lang Syne\"", "\"Amazing Grace\"", "\"I'll Be There for You\""],
        "d": 2
    },
    {
        "q": "What is the name of Ross's first wife who leaves him for Susan Bunch before the pilot episode?",
        "correct": "Carol Willick",
        "distractors": ["Emily Waltham", "Mindy Hunter", "Chloe"],
        "d": 1
    },
    {
        "q": "What institution employed Ross as a research paleontologist during the first five seasons?",
        "correct": "The Museum of Natural History",
        "distractors": ["The Metropolitan Museum of Art", "The Smithsonian Institution", "The Bronx Zoo Evolutionary Research Center"],
        "d": 1
    },
    {
        "q": "What childhood nickname did Judy and Jack Geller bestow upon Ross, much to Monica's resentment?",
        "correct": "\"The Medical Miracle\"",
        "distractors": ["\"The Golden Boy\"", "\"The Little Prince\"", "\"The Einstein of Long Island\""],
        "d": 2
    },
    {
        "q": "Why was Ross called 'the medical miracle' by his parents Jack and Judy?",
        "correct": "Judy was told by doctors that she was barren and could never conceive",
        "distractors": ["Ross survived a rare childhood illness at age two", "Ross walked and talked at five months old", "Ross was born two months premature in a taxi"],
        "d": 2
    },
    {
        "q": "What was the name of the girl from Long Island with whom Ross lost his virginity?",
        "correct": "Carol Willick",
        "distractors": ["Mindy Hunter", "Rachel Green", "Julie"],
        "d": 2
    },
    {
        "q": "What is the name of the eccentric Central Perk barista who is hopelessly in love with Rachel for ten years?",
        "correct": "Gunther",
        "distractors": ["Terry", "Kip", "Mark"],
        "d": 1
    },
    {
        "q": "What was Gunther's former acting claim to fame on a daytime soap opera before working at Central Perk?",
        "correct": "He played Bryce on 'All My Children' and was buried in an avalanche",
        "distractors": ["He played a villain on 'General Hospital' who got poisoned", "He played a surgeon on 'One Life to Live'", "He played an orderly on 'Days of Our Lives'"],
        "d": 3
    },
    {
        "q": "What foreign language is Gunther revealed to speak fluently when insulting Ross at Central Perk?",
        "correct": "Dutch",
        "distractors": ["German", "Swedish", "Polish"],
        "d": 2
    },
    {
        "q": "What color and material is the iconic central sofa inside the Central Perk coffeehouse?",
        "correct": "Burnt orange mohair velvet",
        "distractors": ["Dark red tufted leather", "Mustard yellow corduroy", "Emerald green plush chenille"],
        "d": 1
    },
    {
        "q": "What small sign is frequently visible on the low wooden coffee table in front of the Central Perk orange sofa?",
        "correct": "\"Reserved\"",
        "distractors": ["\"Staff Only\"", "\"Please Order at Counter\"", "\"No Smoking\""],
        "d": 2
    },
    {
        "q": "Who was the original grouchy owner/manager of Central Perk in Season 1 and Season 2 who called Phoebe terrible?",
        "correct": "Terry",
        "distractors": ["Gunther", "Pete", "Stanley"],
        "d": 2
    },
    {
        "q": "What is the opening line of Phoebe Buffay's world-famous song 'Smelly Cat'?",
        "correct": "\"Smelly Cat, Smelly Cat, what are they feeding you?\"",
        "distractors": ["\"Smelly Cat, Smelly Cat, it's not your fault!\"", "\"Oh little stinky kitty walking in the alley\"", "\"Cat with no bath, why do you stink so bad?\""],
        "d": 1
    },
    {
        "q": "What lyrics complete the iconic couplet: 'Smelly Cat, Smelly Cat, what are they feeding you? / Smelly Cat, Smelly Cat...'",
        "correct": "\"...it's not your fault!\"",
        "distractors": ["\"...nobody loves you!\"", "\"...you smell like trash!\"", "\"...we will bathe you soon!\""],
        "d": 1
    },
    {
        "q": "In Phoebe's music video for 'Smelly Cat', what scandalous discovery does Phoebe make about her vocals?",
        "correct": "Her voice was secretly dubbed over by a professional studio session singer",
        "distractors": ["The producers altered her pitch using electronic synthesizers", "They hired an opera soprano to sing the chorus only", "The audio track was played backwards to mask her tone"],
        "d": 2
    },
    {
        "q": "What is the name of Phoebe Buffay's biological mother, who was friends with Lily Buffay and lives in Montauk?",
        "correct": "Phoebe Abbott",
        "distractors": ["Lily Buffay", "Frances Buffay", "Ursula Buffay"],
        "d": 2
    },
    {
        "q": "Which acclaimed actress portrays Phoebe's biological mother, Phoebe Abbott, in Seasons 3 and 4?",
        "correct": "Teri Garr",
        "distractors": ["Diane Keaton", "Blythe Danner", "Shelley Duvall"],
        "d": 2
    },
    {
        "q": "What bizarre object does Phoebe's biological mother give her to test whether Phoebe is ready to raise children?",
        "correct": "A fresh chicken egg",
        "distractors": ["A pet goldfish", "A miniature succulent cactus", "A mechanical baby doll"],
        "d": 2
    },
    {
        "q": "What is the name of Phoebe's eccentric grandmother who passed away in Season 5, leaving her her yellow taxi?",
        "correct": "Frances",
        "distractors": ["Althea", "Sylvia", "Gladys"],
        "d": 2
    },
    {
        "q": "What vehicle does Phoebe inherit from her grandmother Frances, which the gang drives on various road trips?",
        "correct": "A yellow 1977 Checker Taxicab",
        "distractors": ["A vintage blue Volkswagen Beetle", "A wood-paneled Ford Country Squire station wagon", "A rusted red Chevrolet pickup"],
        "d": 2
    },
    {
        "q": "What framing device did Phoebe's grandmother Frances use regarding the identity of Phoebe's biological father?",
        "correct": "She framed pictures of the handsome scientist from photo frame packaging and claimed it was him",
        "distractors": ["She showed Phoebe photos of Albert Einstein", "She pointed to famous politicians on television", "She claimed her father was an astronaut in orbit"],
        "d": 2
    },
    {
        "q": "What famous framing model's picture did Phoebe believe was her father until high school?",
        "correct": "The frame insert model (later revealed to be framed picture model)",
        "distractors": ["Fabio Lanzoni", "The Marlboro Man", "A portrait of Ernest Hemingway"],
        "d": 3
    },
    {
        "q": "What is the name of the scientist Phoebe falls in love with in Season 1, who moves to Minsk on a research grant?",
        "correct": "David",
        "distractors": ["Max", "Gary", "Roger"],
        "d": 1
    },
    {
        "q": "Which actor portrayed David the Scientist Guy, Phoebe's recurring great romantic love?",
        "correct": "Hank Azaria",
        "distractors": ["Jon Favreau", "Tate Donovan", "Paul Rudd"],
        "d": 1
    },
    {
        "q": "To which Eastern European city does David relocate for his scientific particle research?",
        "correct": "Minsk, Belarus",
        "distractors": ["Moscow, Russia", "Kyiv, Ukraine", "Prague, Czech Republic"],
        "d": 1
    },
    {
        "q": "What eccentric billionaire software entrepreneur dates Monica in Season 3 and dreams of becoming the Ultimate Fighting Champion?",
        "correct": "Pete Becker",
        "distractors": ["Mark Robinson", "Chip Matthews", "Paul the Wine Guy"],
        "d": 1
    },
    {
        "q": "Which Hollywood actor/director portrayed billionaire Pete Becker in Season 3?",
        "correct": "Jon Favreau",
        "distractors": ["Vince Vaughn", "Ben Stiller", "Paul Feig"],
        "d": 1
    },
    {
        "q": "Why does Monica break up with billionaire Pete Becker?",
        "correct": "He refuses to give up UFC cage fighting despite being brutally beaten and hospitalized",
        "distractors": ["He loses his entire software fortune in a failed venture", "He proposes to Monica during a business conference", "He demands she move to Silicon Valley with him"],
        "d": 1
    },
    {
        "q": "What is the full name of Monica and Ross's affable, pipe-smoking father?",
        "correct": "Jack Geller",
        "distractors": ["Richard Geller", "Irving Geller", "Arthur Geller"],
        "d": 1
    },
    {
        "q": "Which veteran Hollywood actor played Monica and Ross's father Jack Geller?",
        "correct": "Elliott Gould",
        "distractors": ["Donald Sutherland", "Alan Alda", "Judd Hirsch"],
        "d": 1
    },
    {
        "q": "Which veteran actress portrayed Judy Geller, Monica and Ross's hypercritical mother?",
        "correct": "Christina Pickles",
        "distractors": ["Marlo Thomas", "Blythe Danner", "Marion Ross"],
        "d": 2
    },
    {
        "q": "What classic luxury sports car does Jack Geller give to Monica after her childhood memories are ruined by flood water in the garage?",
        "correct": "His vintage Porsche 911",
        "distractors": ["His Chevrolet Corvette Stingray", "His Mercedes-Benz SL Convertible", "His Jaguar E-Type"],
        "d": 2
    },
    {
        "q": "What childhood boxes of Monica's did Jack Geller use to divert flood water away from his Porsche?",
        "correct": "Monica's childhood scrapbooks, photo albums, and school memorabilia",
        "distractors": ["Monica's collection of dollhouse furniture", "Monica's middle school culinary ribbons", "Monica's high school yearbooks and uniforms"],
        "d": 2
    },
    {
        "q": "What is the name of Joey's elderly, chain-smoking theatrical agent?",
        "correct": "Estelle Leonard",
        "distractors": ["Mindy Hunter", "Iris Buffay", "Ruthie Tartaglione"],
        "d": 1
    },
    {
        "q": "What other client of Estelle's is an entertainer who eats paper and performs pyramid tricks?",
        "correct": "Al Zebooker (the guy who eats paper)",
        "distractors": ["A dog that plays poker", "A juggling fire-eater", "A contortionist tap dancer"],
        "d": 3
    },
    {
        "q": "How many sisters does Joey Tribbiani have?",
        "correct": "Seven sisters",
        "distractors": ["Five sisters", "Six sisters", "Eight sisters"],
        "d": 2
    },
    {
        "q": "Which of Joey's sisters becomes pregnant in Season 8 and asks Rachel for advice?",
        "correct": "Dina",
        "distractors": ["Gina", "Mary Angela", "Mary Therese"],
        "d": 2
    },
    {
        "q": "What musical instrument does Phoebe play during her street performances outside Central Perk?",
        "correct": "Acoustic guitar",
        "distractors": ["Ukulele", "Banjo", "Tambourine"],
        "d": 1
    },
    {
        "q": "What song does Phoebe write about the building superintendent in Season 2?",
        "correct": "\"The Treeger Song\"",
        "distractors": ["\"Mr. Heckles Got Away\"", "\"The Super in the Basement\"", "\"Mops and Buckets\""],
        "d": 3
    },
    {
        "q": "What is the title of Phoebe's song about a holiday season in which she struggles to find rhymes for Chandler and Rachel?",
        "correct": "\"The Holiday Song\"",
        "distractors": ["\"Christmas in New York\"", "\"Hanukkah for Monica\"", "\"Spin the Dreidel, Joey\""],
        "d": 2
    },
    {
        "q": "What does Phoebe rhyme with 'Rachel and Chandler' in her festive holiday song?",
        "correct": "\"And please tell Joey / Christmas will be snowy!\"",
        "distractors": ["\"Handler and candle\"", "\"Reindeer and blizzard\"", "\"Santa's little handler\""],
        "d": 3
    },
    {
        "q": "What color was the iconic picture frame hanging over the peephole on the door of Monica's apartment?",
        "correct": "Bright yellow",
        "distractors": ["Sky blue", "Burnished gold", "Deep cherry red"],
        "d": 1
    },
    {
        "q": "What apartment number was Monica's apartment originally in Season 1 before writers changed it to reflect an upper floor?",
        "correct": "Apartment 5 (changed to Apartment 20)",
        "distractors": ["Apartment 4 (changed to Apartment 19)", "Apartment 2 (changed to Apartment 14)", "Apartment 1 (changed to Apartment 12)"],
        "d": 3
    },
    {
        "q": "What apartment number was Chandler and Joey's apartment originally before being renumbered to 19?",
        "correct": "Apartment 4",
        "distractors": ["Apartment 3", "Apartment 6", "Apartment 5"],
        "d": 3
    },
    {
        "q": "What is the name of Joey's beloved pet rooster who crows early in the morning?",
        "correct": "The Rooster (formerly the baby chick)",
        "distractors": ["Barnaby", "Foghorn", "Pecker"],
        "d": 2
    },
    {
        "q": "What sport does the gang play on the foosball table inside Joey and Chandler's apartment?",
        "correct": "Table football (foosball)",
        "distractors": ["Air hockey", "Table tennis", "Billiards"],
        "d": 1
    },
    {
        "q": "What happened to Joey and Chandler's foosball table in the series finale?",
        "correct": "Monica smashes it open with a hammer and crowbar to rescue Chick Jr. and Duck Jr.",
        "distractors": ["Joey moves it into his new apartment in Los Angeles", "They leave it on the curb for street sanitation pickup", "Chandler gives it to the neighborhood youth center"],
        "d": 2
    },
    {
        "q": "What is the name of the soap opera co-star who gets Joey fired from Days of Our Lives for refusing her advances?",
        "correct": "Kate Miller",
        "distractors": ["Jessica Lockhart", "Cecilia Monroe", "Erin"],
        "d": 3
    },
    {
        "q": "What is the full name of Ross's boss at the museum who eats his Thanksgiving sandwich?",
        "correct": "Dr. Donald Ledbetter",
        "distractors": ["Dr. Kenneth Oberman", "Dr. Richard Burke", "Dr. Alan Fluffy"],
        "d": 3
    },
    {
        "q": "What is the name of the girl who works at the Xerox store who dates both Joey and Ross?",
        "correct": "Chloe",
        "distractors": ["Kathy", "Janice", "Mona"],
        "d": 2
    }
]

if __name__ == "__main__":
    out_path = os.path.join(os.path.dirname(__file__), "staging", "friends_batch4.json")
    build_batch(questions, out_path, batch_num=4)
