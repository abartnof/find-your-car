#!/usr/bin/env python3
"""
Generate tools/staging/friends_batch8.json (100 questions, Extratextual: The Rachel Craze, Reviews, Guest Anecdotes, Pop Culture).
"""
import sys
import os

from build_friends_batch import build_batch

questions = [
    {
        "q": "What celebrity hairstylist created Jennifer Aniston's world-famous 'The Rachel' haircut in 1995?",
        "correct": "Chris McMillan",
        "distractors": ["Sally Hershberger", "Oribe Canales", "Frederic Fekkai"],
        "d": 1
    },
    {
        "q": "What styling technique defined the iconic silhouette of 'The Rachel' haircut?",
        "correct": "Heavily layered, square, face-framing shaggy layers with blonde highlights",
        "distractors": ["A blunt, chin-length asymmetric bob with micro-bangs", "Long, flowing beach waves with dark lowlights", "A sleek, straightened pixie crop"],
        "d": 2
    },
    {
        "q": "What did Jennifer Aniston famously confess to Allure magazine in 2011 regarding 'The Rachel' hairstyle?",
        "correct": "She thought it was 'the ugliest haircut I've ever seen' and a nightmare to style",
        "distractors": ["She considered it the proudest aesthetic achievement of her career", "She secretly wore a wig because her natural hair was damaged", "She copyrighted the haircut name to earn royalties from salons"],
        "d": 1
    },
    {
        "q": "Approximately how many women in the United Kingdom alone were estimated to have requested 'The Rachel' at hair salons in the 1990s?",
        "correct": "Over 11 million women",
        "distractors": ["Around 500,000 women", "Around 2 million women", "Over 25 million women"],
        "d": 2
    },
    {
        "q": "In which Season 1 episode did 'The Rachel' haircut make its on-screen debut?",
        "correct": "\"The One with the Evil Orthodontist\" (Season 1, Episode 19/20)",
        "distractors": ["\"The Pilot\"", "\"The One with the Blackout\"", "\"The One Where Rachel Finds Out\""],
        "d": 3
    },
    {
        "q": "What popular slang term did Friends help popularize into the English lexicon via Joey in 'The One with the Blackout'?",
        "correct": "\"The Friend Zone\"",
        "distractors": ["\"Ghosting\"", "\"Catfishing\"", "\"Binge-watching\""],
        "d": 1
    },
    {
        "q": "What specific phrase did Joey utter when diagnosing Ross's romantic predicament with Rachel in Season 1?",
        "correct": "\"You're the mayor of the friend zone!\"",
        "distractors": ["\"You've been locked in the buddy box!\"", "\"You're stuck in brother territory!\"", "\"You're stranded on platonic island!\""],
        "d": 1
    },
    {
        "q": "What linguistic syntactic structure did linguists note Friends popularized, particularly through Chandler's speech?",
        "correct": "Sarcastic emphasis on the copula: \"Could I BE any more...?\"",
        "distractors": ["Rhyming couplets at the end of every joke", "Inverted passive sentence structures", "Excessive use of French loanwords"],
        "d": 1
    },
    {
        "q": "What intensifying adverb did the characters frequently use that linguists noted surged in American youth speech during the 1990s?",
        "correct": "Using \"so\" to modify negative or prepositional clauses (\"That is so not true\")",
        "distractors": ["Using \"totally\" before every adjective", "Using \"wicked\" as a quantifier", "Using \"mega\" before verbs"],
        "d": 2
    },
    {
        "q": "What prominent Washington Post television critic wrote an infamously harsh 1994 review calling Friends 'another hollow creation'?",
        "correct": "Tom Shales",
        "distractors": ["Ken Tucker", "Howard Rosenberg", "Matt Zoller Seitz"],
        "d": 2
    },
    {
        "q": "What did Tom Shales derisively call the ensemble cast of Friends in his initial September 1994 review?",
        "correct": "A mindless, whiny group of twentysomething slackers",
        "distractors": ["A brilliant troupe of modern comedic geniuses", "An aristocratic collection of Broadway refugees", "A dangerous influence on American high schoolers"],
        "d": 2
    },
    {
        "q": "What grade did Entertainment Weekly critic Ken Tucker award the debut season of Friends in autumn 1994?",
        "correct": "B+",
        "distractors": ["A+", "C-", "F"],
        "d": 2
    },
    {
        "q": "Which major publication hailed Friends in 1995 as the definitive cultural sitcom voice of 'Generation X'?",
        "correct": "Time Magazine",
        "distractors": ["Newsweek", "The Wall Street Journal", "USA Today"],
        "d": 2
    },
    {
        "q": "Which legendary New York Times television critic noted that Friends effectively inherited the witty urban spirit of Seinfeld?",
        "correct": "John J. O'Connor",
        "distractors": ["Frank Rich", "Alessandra Stanley", "Caryn James"],
        "d": 3
    },
    {
        "q": "Why did two-time Oscar winner Sean Penn agree to guest-star as Eric, Ursula Buffay's fiancé, in Season 8?",
        "correct": "His children were enormous fans of Friends and begged him to appear on the show",
        "distractors": ["He lost a bet with director James Burrows", "He wanted to promote an independent drama film", "He was close childhood friends with Matthew Perry"],
        "d": 1
    },
    {
        "q": "Which Hollywood legend guest starred as himself in Season 4, catching Joey showering in his private studio dressing room?",
        "correct": "Charlton Heston",
        "distractors": ["Kirk Douglas", "Gregory Peck", "Paul Newman"],
        "d": 1
    },
    {
        "q": "What advice does Charlton Heston give Joey about an actor's body odor while Joey hides in his dressing room shower?",
        "correct": "He delivers a dignified speech telling Joey that an actor should never be ashamed of his natural sweat",
        "distractors": ["He threatens to have security throw Joey off the studio lot", "He offers Joey a bar of luxury French lavender soap", "He advises Joey to quit acting and pursue voiceovers"],
        "d": 2
    },
    {
        "q": "Which eccentric Hollywood superstar guest starred as acting director Leonard Hayes, who demands that Joey spit and be desperate?",
        "correct": "Jeff Goldblum",
        "distractors": ["Christopher Walken", "Willem Dafoe", "John Malkovich"],
        "d": 1
    },
    {
        "q": "How many episodes was Paul Rudd originally contracted to appear in as Mike Hannigan before producers expanded his role?",
        "correct": "Only two episodes",
        "distractors": ["Six episodes", "A full season of 24 episodes", "Ten episodes"],
        "d": 1
    },
    {
        "q": "Why did the writers change their original plan to have Phoebe end up with David the Scientist Guy (Hank Azaria)?",
        "correct": "Paul Rudd's chemistry with Lisa Kudrow was so undeniable that producers decided Mike was Phoebe's true soulmate",
        "distractors": ["Hank Azaria demanded too much money to return for the final season", "Paul Rudd signed a development deal with NBC requiring him to stay", "Fans voted on an NBC telephone poll to choose Mike over David"],
        "d": 1
    },
    {
        "q": "Which young actor portrayed Ross's son Ben Geller in Seasons 6, 7, and 8?",
        "correct": "Cole Sprouse",
        "distractors": ["Dylan Sprouse", "Haley Joel Osment", "Frankie Muniz"],
        "d": 1
    },
    {
        "q": "What acting milestone did playing Ben Geller mark for young Cole Sprouse?",
        "correct": "It was his very first acting role without his twin brother Dylan Sprouse",
        "distractors": ["It earned him a Young Artist Award for Best Child Actor", "It was his final on-screen acting performance before college", "It was his voiceover debut in a sitcom"],
        "d": 2
    },
    {
        "q": "What embarrassing challenge did Cole Sprouse admit he faced while filming scenes with Jennifer Aniston?",
        "correct": "He had such an overwhelming crush on her that he constantly forgot his lines and froze",
        "distractors": ["He was terrified of her character's pet cat", "He couldn't stop giggling at her hairstyle", "He refused to eat any of the studio cookies"],
        "d": 1
    },
    {
        "q": "Which celebrated child star played Mackenzie, the wise girl living in the suburban house Chandler and Monica buy?",
        "correct": "Dakota Fanning",
        "distractors": ["Abigail Breslin", "Elle Fanning", "Chloe Grace Moretz"],
        "d": 1
    },
    {
        "q": "Which pop icon performed a special duet of 'Smelly Cat' alongside Lisa Kudrow during 'Friends: The Reunion' in 2021?",
        "correct": "Lady Gaga",
        "distractors": ["Taylor Swift", "Katy Perry", "Billie Eilish"],
        "d": 1
    },
    {
        "q": "What acoustic musical artist performed 'Smelly Cat' with Lisa Kudrow during a live stadium concert at Staples Center in 2015?",
        "correct": "Taylor Swift (during 'The 1989 World Tour')",
        "distractors": ["Phoebe Bridgers", "Kacey Musgraves", "Alanis Morissette"],
        "d": 1
    },
    {
        "q": "What costume from Friends did pop star Justin Bieber model on the runway during 'Friends: The Reunion'?",
        "correct": "Ross's 'Spud-nik' potato Halloween costume",
        "distractors": ["Chandler's pink bunny suit", "The Holiday Armadillo", "Joey's lunging outfit of Chandler's clothes"],
        "d": 1
    },
    {
        "q": "What costume did supermodel Cindy Crawford model on the runway during the 2021 reunion special?",
        "correct": "Ross's tight black leather pants and button-up shirt",
        "distractors": ["Rachel's cheerleading outfit", "Monica's chef coat", "Phoebe's Supergirl costume"],
        "d": 1
    },
    {
        "q": "What costume did model/actress Cara Delevingne wear on the runway during 'Friends: The Reunion'?",
        "correct": "Rachel's Pepto-Bismol pink puffy bridesmaid dress (and the Holiday Armadillo)",
        "distractors": ["Monica's Catwoman suit", "Phoebe's bridal gown", "Joey's gladiator armor"],
        "d": 1
    },
    {
        "q": "Which global music sensation boy band appeared as guest interviewees in 'Friends: The Reunion' sharing how the show taught them English?",
        "correct": "BTS",
        "distractors": ["EXO", "Seventeen", "Stray Kids"],
        "d": 1
    },
    {
        "q": "Which BTS member specifically credited watching Friends on DVD with helping him learn to speak fluent English?",
        "correct": "RM (Kim Nam-joon)",
        "distractors": ["Jimin", "Jungkook", "V"],
        "d": 2
    },
    {
        "q": "Which Nobel Peace Prize laureate appeared in 'Friends: The Reunion' to profess her love for the comedy?",
        "correct": "Malala Yousafzai",
        "distractors": ["Greta Thunberg", "Nadia Murad", "Shirin Ebadi"],
        "d": 1
    },
    {
        "q": "Which soccer icon appeared in the reunion special discussing his favorite episode ('The One Where Ross Is Fine')?",
        "correct": "David Beckham",
        "distractors": ["Cristiano Ronaldo", "Lionel Messi", "Wayne Rooney"],
        "d": 1
    },
    {
        "q": "What official toy building-block brand released a massive, highly successful Central Perk set in 2019?",
        "correct": "LEGO (LEGO Ideas Central Perk Set 21319)",
        "distractors": ["Mega Bloks", "Playmobil", "K'NEX"],
        "d": 1
    },
    {
        "q": "What second official LEGO set based on the sitcom was released in 2021 to commemorate the apartments?",
        "correct": "The Friends Apartments Set (featuring both Monica/Rachel's and Joey/Chandler's apartments)",
        "distractors": ["The Central Perk Outdoor Fountain Set", "The Ross's Paleontology Museum Set", "The Las Vegas Wedding Chapel Set"],
        "d": 1
    },
    {
        "q": "In celebration of the show's 20th anniversary in September 2014, where did Warner Bros. open an authentic pop-up Central Perk?",
        "correct": "SoHo, Manhattan in New York City (Lafayette Street)",
        "distractors": ["Times Square, Manhattan", "Greenwich Village on Bedford Street", "Rockefeller Center"],
        "d": 2
    },
    {
        "q": "What actor who played Gunther personally attended and served complimentary coffee at the 2014 NYC Central Perk pop-up?",
        "correct": "James Michael Tyler",
        "distractors": ["Elliott Gould", "Paul Rudd", "Hank Azaria"],
        "d": 1
    },
    {
        "q": "How did actor James Michael Tyler originally land the background role of Gunther in Season 1?",
        "correct": "He was the only extra on set who knew how to operate an authentic espresso machine",
        "distractors": ["He was a cousin of director James Burrows", "He had auditioned for Ross and was offered a consolation role", "He was the personal assistant to producer Marta Kauffman"],
        "d": 1
    },
    {
        "q": "How many episodes did Gunther appear in before he was given his very first line of spoken dialogue?",
        "correct": "33 episodes (he finally spoke in Season 2, saying \"Yeah\")",
        "distractors": ["5 episodes", "12 episodes", "50 episodes"],
        "d": 2
    },
    {
        "q": "What natural hair color did James Michael Tyler have before bleaching it blonde weekly for ten years?",
        "correct": "Dark brown",
        "distractors": ["Bright red", "Jet black", "Sandy blonde"],
        "d": 2
    },
    {
        "q": "Why was James Michael Tyler's hair bleached bright platinum blonde the day before he was cast as Gunther?",
        "correct": "An acquaintance who was an aspiring hairstylist used him as a guinea pig to practice bleaching hair",
        "distractors": ["He was auditioning for a punk-rock music video", "He did it on a dare at a college fraternity party", "He tried to dye his hair silver for a science fiction role"],
        "d": 2
    },
    {
        "q": "On what date did beloved actor James Michael Tyler (Gunther) pass away from prostate cancer at age 59?",
        "correct": "October 24, 2021",
        "distractors": ["August 15, 2020", "December 1, 2021", "January 14, 2022"],
        "d": 2
    },
    {
        "q": "On what date did star Matthew Perry tragically pass away at his Los Angeles home at the age of 54?",
        "correct": "October 28, 2023",
        "distractors": ["September 22, 2023", "November 15, 2023", "December 25, 2023"],
        "d": 1
    },
    {
        "q": "What was the title of Matthew Perry's bestselling 2022 autobiographical memoir?",
        "correct": "'Friends, Lovers, and the Big Terrible Thing'",
        "distractors": ["'Could I BE Any Prouder?'", "'Life on Stage 24'", "'The Boy with the Wit'"],
        "d": 1
    },
    {
        "q": "What foundation was established in Matthew Perry's honor following his passing to support individuals battling addiction?",
        "correct": "The Matthew Perry Foundation",
        "distractors": ["The Chandler Bing Hope Fund", "The Perry Recovery Project", "Friends for Sobriety Foundation"],
        "d": 1
    },
    {
        "q": "What was the title of the multi-city interactive fan exhibition launched by Warner Bros. in 2019 featuring full set replicas?",
        "correct": "'The FRIENDS Experience' (The One in New York)",
        "distractors": ["'Central Perk Live Tour'", "'The Ultimate Friends Museum'", "'Must See Exhibition'"],
        "d": 2
    },
    {
        "q": "What popular coffee-table replica book of Monica's apartment scrapbook was officially released for fans?",
        "correct": "'Friends: The Official Advent Calendar' and 'Friends: The Official Recipe Book'",
        "distractors": ["'Monica's Clean House Manual'", "'Joey's Cookbook for Pizza Lovers'", "'Phoebe's Guitar Tablature Collection'"],
        "d": 3
    },
    {
        "q": "In which Chinese city did a passionate fan named Du Xin open an exact real-life replica of Central Perk and Joey's apartment?",
        "correct": "Beijing",
        "distractors": ["Shanghai", "Hong Kong", "Guangzhou"],
        "d": 2
    },
    {
        "q": "What English name did Chinese entrepreneur Du Xin legally adopt due to his profound obsession with Friends?",
        "correct": "\"Gunther\"",
        "distractors": ["\"Chandler\"", "\"Joey\"", "\"Ross\""],
        "d": 2
    },
    {
        "q": "What major UK city is home to a permanent replica of Central Perk located inside a Primark flagship store?",
        "correct": "Manchester (and later Birmingham)",
        "distractors": ["Edinburgh", "Glasgow", "Cardiff"],
        "d": 3
    },
    {
        "q": "Which Oscar-winning actor guest-starred in 'The One with the Two Parties' as Rachel's abrasive, wealthy father Dr. Leonard Green?",
        "correct": "Ron Leibman",
        "distractors": ["Martin Sheen", "Donald Sutherland", "James Caan"],
        "d": 2
    },
    {
        "q": "Which celebrated actress played Rachel's mother Sandra Green, who announces she wants a divorce to live like Rachel?",
        "correct": "Marlo Thomas",
        "distractors": ["Candice Bergen", "Blythe Danner", "Diane Ladd"],
        "d": 2
    },
    {
        "q": "Which acclaimed actor portrayed Monica and Ross's wealthy, eccentric uncle Ellis who leaves them antique heirlooms?",
        "correct": "No uncle Ellis appeared; Aunt Syl and Nana Althea were their featured relatives",
        "distractors": ["Jerry Stiller", "Carl Reiner", "Bob Newhart"],
        "d": 3
    },
    {
        "q": "Which television legend guest-starred as himself in 'The One with the Mugging', auditioning Joey for a serious stage play?",
        "correct": "Jeff Goldblum",
        "distractors": ["James Earl Jones", "Christopher Plummer", "Patrick Stewart"],
        "d": 2
    },
    {
        "q": "Which 'Sex and the City' star guest starred as Erin, a woman Joey dates who bonds with Chandler over sports in Season 7?",
        "correct": "Kristin Davis",
        "distractors": ["Sarah Jessica Parker", "Kim Cattrall", "Cynthia Nixon"],
        "d": 1
    },
    {
        "q": "Which 'Wild Things' and Bond girl actress guest-starred as Ross and Monica's cousin Cassie in Season 7?",
        "correct": "Denise Richards",
        "distractors": ["Carmen Electra", "Jenny McCarthy", "Shannon Elizabeth"],
        "d": 1
    },
    {
        "q": "What iconic slow-motion hair flip song plays whenever cousin Cassie shakes out her hair in front of the mesmerized characters?",
        "correct": "\"I Want You to Want Me\" by Cheap Trick (or Barry White's sensual soul music)",
        "distractors": ["\"Careless Whisper\" by George Michael", "\"Let's Get It On\" by Marvin Gaye", "\"Fever\" by Peggy Lee"],
        "d": 2
    },
    {
        "q": "Which actress played Tag Jones, Rachel's handsome young assistant and romantic partner at Ralph Lauren?",
        "correct": "Eddie Cahill (male actor)",
        "distractors": ["Tate Donovan", "Michael Vartan", "Dermot Mulroney"],
        "d": 1
    },
    {
        "q": "What actor portrayed Joshua Burgin, Rachel's personal shopping client whom she dated in Season 4?",
        "correct": "Tate Donovan",
        "distractors": ["Eddie Cahill", "George Newbern", "Hank Azaria"],
        "d": 1
    },
    {
        "q": "What real-life romantic history existed between Jennifer Aniston and Tate Donovan during their Season 4 episodes together?",
        "correct": "They had just broken off their real-life engagement after dating for two years",
        "distractors": ["They were secretly engaged and married shortly after", "They had never met before the first table read", "They were college sweethearts from New York"],
        "d": 1
    },
    {
        "q": "How did Tate Donovan describe the experience of filming romantic scenes with Jennifer Aniston right after their breakup?",
        "correct": "\"It was really tough... we were breaking up and the show was having us fall in love.\"",
        "distractors": ["\"It was completely hilarious and brought us back together.\"", "\"We refused to speak to each other off camera.\"", "\"The director had to use body doubles for our kisses.\""],
        "d": 2
    },
    {
        "q": "Which actor played Mona, Ross's patient girlfriend whom he met at Monica and Chandler's wedding in Season 8?",
        "correct": "Bonnie Somerville",
        "distractors": ["Alexandra Holden", "Lauren Tom", "Paget Brewster"],
        "d": 2
    },
    {
        "q": "Which actress played Julie, Ross's kind paleontologist girlfriend whom he brought home from China in Season 2?",
        "correct": "Lauren Tom",
        "distractors": ["Ming-Na Wen", "Lucy Liu", "Tamlyn Tomita"],
        "d": 1
    },
    {
        "q": "Which actress played Elizabeth Stevens, Ross's college student girlfriend in late Season 6?",
        "correct": "Alexandra Holden",
        "distractors": ["Bonnie Somerville", "Paget Brewster", "Soleil Moon Frye"],
        "d": 2
    },
    {
        "q": "Which actress played Kathy, the woman who dated Joey and then Chandler in Season 4?",
        "correct": "Paget Brewster",
        "distractors": ["Dina Meyer", "Elle Macpherson", "Rebecca Romijn"],
        "d": 1
    },
    {
        "q": "Which long-running CBS procedural drama did Paget Brewster go on to star in as Emily Prentiss for many years?",
        "correct": "'Criminal Minds'",
        "distractors": ["'NCIS'", "'CSI: Crime Scene Investigation'", "'Without a Trace'"],
        "d": 1
    },
    {
        "q": "Which actress portrayed Janice Litman-Goralnik across all ten seasons of Friends?",
        "correct": "Maggie Wheeler",
        "distractors": ["Fran Drescher", "Debi Mazar", "Marisa Tomei"],
        "d": 1
    },
    {
        "q": "What inspired Maggie Wheeler to invent Janice's distinctive, high-pitched nasal laugh during her audition?",
        "correct": "She knew Matthew Perry was so funny that she needed a laugh she could use if she cracked up on set",
        "distractors": ["She modeled it directly on her real-life mother-in-law", "The director instructed her to impersonate Woody Woodpecker", "She had a severe head cold during her initial casting call"],
        "d": 1
    },
    {
        "q": "How many of the ten seasons of Friends did Maggie Wheeler's character Janice appear in?",
        "correct": "All ten seasons (at least one episode per season)",
        "distractors": ["Only the first five seasons", "Eight seasons", "Six seasons"],
        "d": 1
    },
    {
        "q": "Which actor portrayed building superintendent Mr. Treeger across several seasons?",
        "correct": "Michael G. Hagerty",
        "distractors": ["Jon Polito", "Vincent Schiavelli", "M. Emmet Walsh"],
        "d": 2
    },
    {
        "q": "Which actor portrayed Gunther's rival, the smooth coffeehouse manager Terry who called Rachel a terrible waitress?",
        "correct": "Max Wright",
        "distractors": ["Paul Dooley", "Kurtwood Smith", "Jeffrey Tambor"],
        "d": 2
    },
    {
        "q": "What 1980s sitcom had Max Wright (Terry) famously starred in as suburban father Willie Tanner?",
        "correct": "'ALF'",
        "distractors": ["'Perfect Strangers'", "'Night Court'", "'Head of the Class'"],
        "d": 1
    },
    {
        "q": "Which actress portrayed Carol Willick in the Pilot episode before Anita Barone was replaced by Jane Sibbett?",
        "correct": "Anita Barone",
        "distractors": ["Jane Sibbett", "Lauren Tom", "Jessica Hecht"],
        "d": 2
    },
    {
        "q": "Which actress portrayed Carol Willick for the remainder of the series from Season 1 Episode 2 onward?",
        "correct": "Jane Sibbett",
        "distractors": ["Anita Barone", "Jessica Hecht", "Morgan Fairchild"],
        "d": 1
    },
    {
        "q": "Which actress played Susan Bunch, Carol's supportive partner throughout the show's run?",
        "correct": "Jessica Hecht",
        "distractors": ["Jane Sibbett", "Anita Barone", "Christine Taylor"],
        "d": 1
    },
    {
        "q": "What groundbreaking television milestone did Carol and Susan's Season 2 wedding episode represent in January 1996?",
        "correct": "One of the very first depictions of a lesbian wedding ceremony on American network primetime television",
        "distractors": ["The first television episode filmed entirely in black and white", "The first sitcom episode with no background laughter track", "The first episode to air without commercial interruption"],
        "d": 1
    },
    {
        "q": "How many affiliate stations across the United States refused to broadcast the lesbian wedding episode in 1996?",
        "correct": "Two affiliate stations (in Ohio and Texas)",
        "distractors": ["Zero affiliates; all aired it without objection", "Over twenty-five affiliates", "Nearly half of all Southern affiliates"],
        "d": 3
    },
    {
        "q": "What actress portrayed Phoebe's sister-in-law Alice Knight Buffay, who married Frank Buffay Jr.?",
        "correct": "Debra Jo Rupp",
        "distractors": ["Laurie Metcalf", "Marion Ross", "Swoosie Kurtz"],
        "d": 1
    },
    {
        "q": "What iconic sitcom did Debra Jo Rupp star in as matriarch Kitty Forman during and after her Friends recurring role?",
        "correct": "'That '70s Show'",
        "distractors": ["'Roseanne'", "'Everybody Loves Raymond'", "'Malcolm in the Middle'"],
        "d": 1
    },
    {
        "q": "Which actor portrayed Phoebe's eccentric half-brother Frank Buffay Jr.?",
        "correct": "Giovanni Ribisi",
        "distractors": ["Seth Green", "Lukas Haas", "Breckin Meyer"],
        "d": 1
    },
    {
        "q": "What minor background role did Giovanni Ribisi play in Season 2 before being cast as Frank Buffay Jr.?",
        "correct": "A stranger who drops a condom into Phoebe's guitar case outside Central Perk",
        "distractors": ["A customer ordering a muffin from Gunther", "A man reading a newspaper on the subway", "A laundromat patron who takes Rachel's cart"],
        "d": 2
    },
    {
        "q": "Which actor played Eddie Menuek, Chandler's erratic roommate in late Season 2?",
        "correct": "Adam Goldberg",
        "distractors": ["Jon Favreau", "Hank Azaria", "Fisher Stevens"],
        "d": 1
    },
    {
        "q": "Which actor played Roger, Phoebe's psychologist boyfriend who psychoanalyzes the group and makes them miserable in Season 1?",
        "correct": "Fisher Stevens",
        "distractors": ["Adam Goldberg", "Jon Lovitz", "French Stewart"],
        "d": 2
    },
    {
        "q": "Which actor played Kip, Chandler's former roommate who was phased out of the friend group before Joey moved in?",
        "correct": "Kip is never shown on screen; he is only discussed by the group",
        "distractors": ["David Schwimmer", "Adam Goldberg", "Hank Azaria"],
        "d": 2
    },
    {
        "q": "Which actor portrayed Ross's double 'Russ' in Season 2, who dates Rachel briefly?",
        "correct": "David Schwimmer (under the pseudonym Snaro)",
        "distractors": ["Matthew Perry in a wig", "A professional David Schwimmer lookalike", "David Schwimmer's real-life brother"],
        "d": 1
    },
    {
        "q": "Which iconic late-night host made a guest cameo in Season 7's 'The One with the Cheap Wedding Dress' as himself?",
        "correct": "Jay Leno appeared in Season 1; Regis Philbin appeared in Season 7",
        "distractors": ["David Letterman", "Conan O'Brien", "Craig Kilborn"],
        "d": 3
    },
    {
        "q": "Which iconic talk-show host cameos in 'The One with the Mugging' walking past Central Perk?",
        "correct": "Conan O'Brien (sitting as an extra in the background of Central Perk)",
        "distractors": ["Jay Leno", "Jon Stewart", "David Letterman"],
        "d": 3
    },
    {
        "q": "Why was Conan O'Brien sitting as an extra in Central Perk in Season 9?",
        "correct": "He won an NBC charity auction and chose to sit silently in the background as an extra",
        "distractors": ["He was visiting the set while shooting late-night promos", "He was filling in for an actor who missed his call", "He wanted to surprise his friend Lisa Kudrow"],
        "d": 2
    },
    {
        "q": "What British actress played Ross's second wife Emily Waltham throughout Season 4 and early Season 5?",
        "correct": "Helen Baxendale",
        "distractors": ["Minnie Driver", "Joely Richardson", "Natascha McElhone"],
        "d": 1
    },
    {
        "q": "Why was Emily Waltham's character written out of the show earlier than producers originally intended?",
        "correct": "Helen Baxendale became pregnant in real life and could not travel between England and the US",
        "distractors": ["She had creative clashes with David Schwimmer", "She was cast as the lead in a major Hollywood feature", "Network executives disliked her British accent"],
        "d": 2
    },
    {
        "q": "What legendary comedic actress played Ross and Monica's Nana Althea who passes away in Season 1?",
        "correct": "Elinor Donahue",
        "distractors": ["Marion Ross", "Christina Pickles", "Doris Roberts"],
        "d": 3
    },
    {
        "q": "Which veteran character actor played Mr. Heckles, the downstairs neighbor with the broom?",
        "correct": "Larry Hankin",
        "distractors": ["Harry Shearer", "Vincent Schiavelli", "M. Emmet Walsh"],
        "d": 2
    },
    {
        "q": "What iconic 1990 movie comedy had Larry Hankin (Mr. Heckles) previously starred in as Officer Balzak?",
        "correct": "'Home Alone'",
        "distractors": ["'Groundhog Day'", "'The Santa Clause'", "'Father of the Bride'"],
        "d": 2
    },
    {
        "q": "Which actress played Nora Tyler Bing, Chandler's glamorous erotic novelist mother?",
        "correct": "Morgan Fairchild",
        "distractors": ["Joan Collins", "Linda Gray", "Donna Mills"],
        "d": 1
    },
    {
        "q": "Which actor portrayed Chandler's father's lover, the houseboy Mr. Garibaldi in flashbacks?",
        "correct": "He is only referenced as the houseboy with whom his father had an affair",
        "distractors": ["Paolo", "Mario", "Antonio"],
        "d": 3
    },
    {
        "q": "Which actress played Phoebe's friend and former roommate Denise, whom the gang insists does not exist?",
        "correct": "Denise is never seen on screen; Phoebe only shouts 'I talk about her all the time! DENISE!'",
        "distractors": ["Winona Ryder", "Christina Applegate", "Paget Brewster"],
        "d": 2
    },
    {
        "q": "What was the name of the white capuchin monkey who played Ross's pet Marcel in Season 1?",
        "correct": "Katie the monkey (with a backup named Monkey)",
        "distractors": ["Bubbles the monkey", "Barnaby the monkey", "Coco the monkey"],
        "d": 3
    },
    {
        "q": "Why did David Schwimmer notoriously dislike working with Katie the capuchin monkey on set?",
        "correct": "The monkey threw live mealworms at him and required endless repetitive takes that ruined comedic timing",
        "distractors": ["The monkey bit his finger during a rehearsal", "The monkey had an allergic reaction to studio lights", "The animal trainer demanded higher pay than the actors"],
        "d": 2
    },
    {
        "q": "What major advertising campaign featured Katie the capuchin monkey after her appearance on Friends?",
        "correct": "The 1995 Taco Bell commercial campaign (and Rally's commercials)",
        "distractors": ["The Budweiser Super Bowl frogs", "The Geico gecko campaign", "The Energizer bunny ads"],
        "d": 3
    },
    {
        "q": "What enduring legacy message did the six stars post in their joint statement following Matthew Perry's passing in 2023?",
        "correct": "\"We are all so utterly devastated by the loss of Matthew. We were more than just cast mates. We are a family.\"",
        "distractors": ["\"He was the funniest man on television and our hearts are broken.\"", "\"Stage twenty-four will never be the same without Chandler Bing.\"", "\"Rest in peace, dear brother. You made the world laugh.\""],
        "d": 1
    }
]

if __name__ == "__main__":
    out_path = os.path.join(os.path.dirname(__file__), "staging", "friends_batch8.json")
    build_batch(questions, out_path, batch_num=8)
