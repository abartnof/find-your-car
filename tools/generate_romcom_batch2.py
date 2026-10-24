#!/usr/bin/env python3
"""
Generate Batch 2 for Romantic Comedies:
100 Textual questions (Iconic lines, airport sprints, grand declarations, quirky best friends, plot climaxes).
Difficulty: 30 d1, 40 d2, 30 d3.
"""
import sys
import os

# Add tools to path
sys.path.append(os.path.dirname(__file__))
from rom_com_builder import make_batch

questions_batch2 = [
    # 1 - d1
    (
        "In 'When Harry Met Sally...', what iconic line is delivered by an elderly female diner after Sally fakes an orgasm in Katz's Deli?",
        "I'll have what she's having",
        ["She's definitely faking it", "Give me two of whatever that was", "Check, please"],
        1
    ),
    # 2 - d1
    (
        "In 'Notting Hill', what does movie star Anna Scott famously say to William Thacker in his travel bookshop?",
        "I'm also just a girl, standing in front of a boy, asking him to love her",
        ["I'm just an actress, looking for an ordinary life", "You had me at hello", "There is no one else I would rather share a garden with"],
        1
    ),
    # 3 - d1
    (
        "Which line does Jerry Maguire deliver to Dorothy Boyd when he interrupts her living room book club meeting?",
        "You had me at hello",
        ["You complete me", "Show me the money", "I love you with all my heart"],
        1
    ),
    # 4 - d1
    (
        "In 'Pretty Woman', what does Vivian Ward say when she returns to the Rodeo Drive boutique that refused to serve her the day before?",
        "Big mistake. Big. Huge! I have to go shopping now",
        ["You work on commission, right? Terrible mistake!", "Look what you missed out on!", "Never judge a girl by her boots"],
        1
    ),
    # 5 - d1
    (
        "In 'The Princess Bride', what phrase does Westley repeatedly say to Buttercup that actually means 'I love you'?",
        "As you wish",
        ["Whatever you desire", "To the end of the world", "Always and forever"],
        1
    ),
    # 6 - d1
    (
        "In 'Clueless', what is Cher Horowitz's famous catchphrase when dismissing unwanted advances?",
        "As if!",
        ["Whatever!", "Totally bogus!", "Get real!"],
        1
    ),
    # 7 - d1
    (
        "In '13 Going on 30', what rhyming phrase is Jenna Rink obsessed with repeating on her 13th birthday?",
        "Thirty, flirty, and thriving",
        ["Thirty, pretty, and thriving", "Twenty, flirty, and sporty", "Thirty, happy, and shining"],
        1
    ),
    # 8 - d1
    (
        "In 'Legally Blonde', what signature move does Elle Woods teach Paulette and the salon patrons to attract men?",
        "The Bend and Snap",
        ["The Hair Toss and Smile", "The Prance and Glance", "The Dip and Wink"],
        1
    ),
    # 9 - d1
    (
        "In 'Moonstruck', what does Loretta Castorini (Cher) say to Ronny Cammareri (Nicolas Cage) immediately after slapping him across the face twice?",
        "Snap out of it!",
        ["Get over yourself!", "Shut up and kiss me!", "Act like a man!"],
        1
    ),
    # 10 - d1
    (
        "In 'Love Actually', what words are written on Mark's cue card as he silently professes his feelings to Juliet on her doorstep?",
        "To me, you are perfect",
        ["You are my only love", "I will love you always", "Merry Christmas, beautiful"],
        1
    ),
    # 11 - d1
    (
        "In 'My Best Friend's Wedding', who plays Julianne Potter's flamboyant gay best friend and editor, George Downes?",
        "Rupert Everett",
        ["Colin Firth", "Hugh Grant", "Alan Rickman"],
        1
    ),
    # 12 - d1
    (
        "In 'Notting Hill', what is the name of William Thacker's eccentric, Welsh, underwear-wearing flatmate?",
        "Spike",
        ["Bernie", "Max", "Martin"],
        1
    ),
    # 13 - d1
    (
        "In 'When Harry Met Sally...', what household furnishing do Jess and Marie argue intensely about moving into their shared apartment?",
        "A wagon wheel coffee table",
        ["A Tiffany floor lamp", "A giant recliner chair", "A stuffed deer head"],
        1
    ),
    # 14 - d1
    (
        "In '10 Things I Hate About You', how does Kat Stratford break down during English class at the end of the film?",
        "She recites an emotional poem she wrote about Patrick",
        ["She storms out and throws her textbook at Mr. Morgan", "She confesses her love over the school PA system", "She sings an acoustic love song"],
        1
    ),
    # 15 - d1
    (
        "In 'The Wedding Singer', where does Robbie Hart finally perform his song 'Grow Old With You' for Julia Sullivan?",
        "On an airplane flight to Las Vegas",
        ["At a crowded reception hall", "Outside her bedroom window in the rain", "In front of an altar at a church"],
        1
    ),
    # 16 - d1
    (
        "In 'Pretty Woman', what does Edward Lewis do at the end of the film to rescue Vivian from her apartment?",
        "He climbs up her fire escape holding a bouquet of red roses",
        ["He drives a horse-drawn carriage through Hollywood", "He lands a private helicopter on her roof", "He walks through her front door with an engagement ring"],
        1
    ),
    # 17 - d1
    (
        "In 'Crazy Rich Asians', who plays Rachel Chu's hilariously wealthy, ostentatious college friend Goh Peik Lin?",
        "Awkwafina",
        ["Constance Wu", "Gemma Chan", "Ali Wong"],
        1
    ),
    # 18 - d1
    (
        "In 'Clueless', who turns out to be Cher's true romantic match at the end of the film?",
        "Her ex-stepbrother Josh",
        ["High school heartthrob Christian", "Popular rich kid Elton", "Skater Travis Birkenstock"],
        1
    ),
    # 19 - d1
    (
        "In 'How to Lose a Guy in 10 Days', what pet name does Andie Anderson give to Ben Barry's male anatomy during a poker game?",
        "Princess Sophia",
        ["Little Benny", "Captain Jack", "Sweet Pea"],
        1
    ),
    # 20 - d1
    (
        "In 'How to Lose a Guy in 10 Days', what plant does Andie Anderson give Ben to test his relationship commitment, claiming it represents their bond?",
        "A love fern",
        ["A bonsai tree", "An orchid", "A weeping willow"],
        1
    ),
    # 21 - d1
    (
        "In 'Groundhog Day', which specific musical instrument does Phil Connors dedicate himself to mastering across endless time loops?",
        "Piano",
        ["Violin", "Acoustic guitar", "Saxophone"],
        1
    ),
    # 22 - d1
    (
        "In 'Sleepless in Seattle', who initiates contact with Annie Reed by calling into a national late-night radio broadcast about his grieving dad?",
        "Sam's son Jonah",
        ["Sam's sister Suzy", "Sam's co-worker Greg", "Sam's psychiatrist"],
        1
    ),
    # 23 - d1
    (
        "In 'You've Got Mail', what is the name of the independent children's bookstore owned by Kathleen Kelly?",
        "The Shop Around the Corner",
        ["Fox Books", "Cornerstone Tales", "Once Upon a Time"],
        1
    ),
    # 24 - d1
    (
        "In 'Bridget Jones's Diary', what color soup does Bridget inadvertently serve to her dinner party guests after tying herbs with blue string?",
        "Blue soup",
        ["Green soup", "Purple soup", "Neon pink soup"],
        1
    ),
    # 25 - d1
    (
        "In 'Four Weddings and a Funeral', what sudden revelation ruins Charles's impending wedding to Henrietta at the altar?",
        "Carrie walks into the church",
        ["He realizes he left the rings at home", "Henrietta confesses an affair with his brother", "The priest suffers a fainting spell"],
        1
    ),
    # 26 - d1
    (
        "In '10 Things I Hate About You', what sport does Kat Stratford play before being expelled from the team?",
        "Soccer",
        ["Field hockey", "Tennis", "Basketball"],
        1
    ),
    # 27 - d1
    (
        "In 'Legally Blonde', what does Elle Woods say to Warner Huntington III when he expresses shock at seeing her at Harvard Law School?",
        "What, like it's hard?",
        ["Did you miss me?", "Surprise, sweetheart!", "Brains look good in pink, don't they?"],
        1
    ),
    # 28 - d1
    (
        "In 'Say Anything...', what object does Lloyd Dobler receive from Diane Court after he gives her his heart?",
        "A pen",
        ["A key", "A watch", "A mixtape"],
        1
    ),
    # 29 - d1
    (
        "In 'As Good as It Gets', what does Melvin Udall (Jack Nicholson) say to Carol Connelly (Helen Hunt) that represents his highest compliment?",
        "You make me want to be a better man",
        ["You are the reason I wake up smiling", "You are the sweetest medicine I know", "You make the world tolerable"],
        1
    ),
    # 30 - d1
    (
        "In 'The Princess Bride', which character delivers the famous revenge pledge: 'Hello. My name is Inigo Montoya. You killed my father. Prepare to die'?",
        "Inigo Montoya",
        ["Fezzik", "Westley", "Count Rugen"],
        1
    ),

    # 31 - d2
    (
        "In 'When Harry Met Sally...', during their climactic New Year's Eve confrontation, Harry explains why he rushed over by saying what?",
        "When you realize you want to spend the rest of your life with somebody, you want the rest of your life to start as soon as possible",
        ["I couldn't face midnight without looking into the eyes of my best friend", "I love that you get cold when it's 71 degrees out", "Because life without you is just passing the time until next year"],
        2
    ),
    # 32 - d2
    (
        "In 'Notting Hill', what obscure surrealist painting by Marc Chagall does Anna Scott gift to William Thacker?",
        "La Mariée",
        ["The Birthday", "Over the Town", "I and the Village"],
        2
    ),
    # 33 - d2
    (
        "In 'Clueless', what does Cher Horowitz call Tai Frasier's look before giving her an extreme Beverly Hills makeover?",
        "A full-on Monet",
        ["A total thrift store disaster", "A grunge casualty", "An urban tragedy"],
        2
    ),
    # 34 - d2
    (
        "In 'Jerry Maguire', who plays Jerry's loyal, adoring assistant and romantic interest Dorothy Boyd?",
        "Renée Zellweger",
        ["Kelly Preston", "Cameron Diaz", "Sandra Bullock"],
        2
    ),
    # 35 - d2
    (
        "In 'Jerry Maguire', what bizarre biological claim does Dorothy's young son Ray constantly share with people?",
        "The human head weighs eight pounds",
        ["Dogs only dream in black and white", "Bees cannot fly backwards", "A goldfish memory lasts only three seconds"],
        2
    ),
    # 36 - d2
    (
        "In 'The Princess Bride', who plays Miracle Max, the eccentric potion maker who brings Westley back from being 'mostly dead'?",
        "Billy Crystal",
        ["Peter Falk", "Wallace Shawn", "Mel Smith"],
        2
    ),
    # 37 - d2
    (
        "In 'The Princess Bride', what word does Vizzini keep repeating whenever his plans encounter an obstacle, prompting Inigo to question its meaning?",
        "Inconceivable!",
        ["Impossible!", "Unthinkable!", "Preposterous!"],
        2
    ),
    # 38 - d2
    (
        "In 'While You Were Sleeping', what misunderstanding leads the hospital nurse to introduce Lucy as Peter's fiancée?",
        "Lucy murmurs 'I was going to marry him' under her breath to herself",
        ["Lucy was wearing Peter's family signet ring", "Lucy was carrying Peter's marriage proposal draft in her bag", "Peter spoke Lucy's name just before falling comatose"],
        2
    ),
    # 39 - d2
    (
        "In 'While You Were Sleeping', which family member of Peter's does Lucy actually end up falling in love with?",
        "His brother Jack",
        ["His cousin Joe", "His best friend Jerry", "His business partner Saul"],
        2
    ),
    # 40 - d2
    (
        "In 'My Best Friend's Wedding', what dessert does Julianne use as an analogy to explain why Michael shouldn't marry Kimmy?",
        "Crème brûlée and Jell-O",
        ["Apple pie and lemon meringue", "Chocolate soufflé and vanilla pudding", "Tiramisu and cotton candy"],
        2
    ),
    # 41 - d2
    (
        "In 'Four Weddings and a Funeral', who delivers the heartbreaking recitation of W.H. Auden's 'Funeral Blues' for his deceased partner Gareth?",
        "Matthew",
        ["Charles", "Tom", "David"],
        2
    ),
    # 42 - d2
    (
        "In 'Bridget Jones's Diary', what hideous holiday clothing item is Mark Darcy wearing when Bridget first meets him at a family buffet?",
        "A knitted turtleneck with a giant reindeer on the chest",
        ["A bright red cardigan featuring dancing snowmen", "A plaid suit with jingle bell buttons", "A green sweater adorned with tinsel and lights"],
        2
    ),
    # 43 - d2
    (
        "In 'Love Actually', what role does young Sam take up in the school band to impress his American classmate Joanna?",
        "Drummer",
        ["Lead guitarist", "Keyboardist", "Saxophonist"],
        2
    ),
    # 44 - d2
    (
        "In 'Love Actually', which character runs through Heathrow Airport security dodging guards to kiss his crush before she boards a flight?",
        "Sam",
        ["Colin", "Mark", "Jamie"],
        2
    ),
    # 45 - d2
    (
        "In 'The Holiday', what classic movie soundtrack composer does Iris Simpkins form a charming friendship with in Los Angeles?",
        "Arthur Abbott",
        ["Miles Dumont", "Graham Simpkins", "Ethan Ebbers"],
        2
    ),
    # 46 - d2
    (
        "In 'The Holiday', what is the name of Graham's (Jude Law) home-built children's entertainment tent inside his English cottage?",
        "The Tent of Stars",
        ["The Enchanted Den", "The Little Castle", "The Cloud Palace"],
        2
    ),
    # 47 - d2
    (
        "In '10 Things I Hate About You', where do Kat and Patrick have their wildly fun, messy romantic paint-balloon fight?",
        "A paintball field with suspended target obstacles",
        ["An abandoned warehouse loft", "The high school bleachers", "Her father's backyard lawn"],
        2
    ),
    # 48 - d2
    (
        "In 'Clueless', which Jane Austen novel served as the modern-day template for writer-director Amy Heckerling's script?",
        "Emma",
        ["Sense and Sensibility", "Pride and Prejudice", "Mansfield Park"],
        2
    ),
    # 49 - d2
    (
        "In 'Groundhog Day', what infuriating, high-energy insurance salesman pesters Phil Connors every morning on the sidewalk?",
        "Ned Ryerson",
        ["Buster Green", "Ralph Parker", "Felix Ungar"],
        2
    ),
    # 50 - d2
    (
        "In '500 Days of Summer', what whimsical musical number erupts in a public park after Tom Hansen spends his first night with Summer?",
        "You Make My Dreams by Hall & Oates",
        ["Here Comes the Sun by The Beatles", "Wouldn't It Be Nice by The Beach Boys", "Sweet Disposition by The Temper Trap"],
        2
    ),
    # 51 - d2
    (
        "In '500 Days of Summer', what architectural style does Tom teach Summer about from their favorite bench in the city?",
        "Los Angeles historic architecture and art deco buildings",
        ["Chicago gothic skyscrapers", "Modernist brutalism", "Victorian gingerbread brownstones"],
        2
    ),
    # 52 - d2
    (
        "In 'Crazy, Stupid, Love.', what does Cal Weaver (Steve Carell) do for a living before his marriage falls apart?",
        "Insurance executive",
        ["Corporate accountant", "High school guidance counselor", "Real estate appraiser"],
        2
    ),
    # 53 - d2
    (
        "In 'Crazy, Stupid, Love.', what move from 'Dirty Dancing' does Jacob Palmer (Ryan Gosling) use as his foolproof pickup closer?",
        "The overhead dance lift",
        ["The water carry spin", "The mambo dip", "The watermelon carry"],
        2
    ),
    # 54 - d2
    (
        "In 'Silver Linings Playbook', what is the title of the Ernest Hemingway novel Pat Solitano Jr. hurls through his parents' window in frustration?",
        "A Farewell to Arms",
        ["The Sun Also Rises", "For Whom the Bell Tolls", "The Old Man and the Sea"],
        2
    ),
    # 55 - d2
    (
        "In 'Forgetting Sarah Marshall', who plays the eccentric, stoned surf instructor Chuck (who prefers to go by Kunu)?",
        "Paul Rudd",
        ["Jonah Hill", "Jason Segel", "Jack Black"],
        2
    ),
    # 56 - d2
    (
        "In 'Forgetting Sarah Marshall', what is the title of Aldous Snow's outrageous European hit song about romantic anatomy?",
        "Inside of You",
        ["Taste of Your Skin", "Flesh and Fantasy", "London Calling My Heart"],
        2
    ),
    # 57 - d2
    (
        "In 'Knocked Up', what major entertainment website does Alison Roberts (Katherine Heigl) work for as an on-camera reporter?",
        "E! News",
        ["Access Hollywood", "Entertainment Tonight", "MTV News"],
        2
    ),
    # 58 - d2
    (
        "In 'The Big Sick', how do Kumail's traditional Pakistani parents attempt to find him a suitable spouse during family dinners?",
        "Prospective Pakistani brides 'drop in' unexpectedly with headshot photos",
        ["They hire a professional matchmaker in Lahore", "They subscribe him to a South Asian dating portal", "They arrange a formal contract with an uncle's family"],
        2
    ),
    # 59 - d2
    (
        "In 'Palm Springs', what bizarre weapon does Roy Schlieffen (J.K. Simmons) repeatedly use to hunt down Nyles across different loops?",
        "A hunting bow and arrows",
        ["A vintage harpoon", "A machete", "A cattle prod"],
        2
    ),
    # 60 - d2
    (
        "In 'Set It Up', what sports event do Harper and Charlie orchestrate for their tyrannical bosses to attend together?",
        "A Brooklyn Nets basketball game",
        ["A New York Yankees baseball game", "A New York Rangers hockey match", "A US Open tennis championship match"],
        2
    ),
    # 61 - d2
    (
        "In 'Always Be My Maybe', what high-profile childhood memory drives Marcus Kim's stubborn refusal to move away from San Francisco?",
        "His mother Judy's tragic death in a car crash",
        ["His father's failing repair business", "His promise to his high school bandmates", "His dream of renovating his childhood house"],
        2
    ),
    # 62 - d2
    (
        "In 'Rye Lane', what peculiar public exhibit in the Peckham gallery serves as a pivotal stop on Dom and Yas's walking tour?",
        "A provocative photographic exhibition by Dom's ex-girlfriend",
        ["A giant sculpture of neon foam noodles", "An interactive mirrored sound installation", "A live-action karaoke performance booth"],
        2
    ),
    # 63 - d2
    (
        "In 'Roman Holiday', what Roman landmark does Joe Bradley take Princess Ann to where he pretends to lose his hand in a carved stone mouth?",
        "The Mouth of Truth (Bocca della Verità)",
        ["The Trevi Fountain", "The Spanish Steps", "The Colosseum arches"],
        2
    ),
    # 64 - d2
    (
        "In 'It Happened One Night', what do Ellie Andrews and Peter Warne hang between their twin beds in the motor motel room to maintain propriety?",
        "A blanket called the Walls of Jericho",
        ["A canvas curtain called the Iron Curtain", "A patchwork quilt called the Mason-Dixon Line", "A floral bedsheet called the Great Divide"],
        2
    ),
    # 65 - d2
    (
        "In 'It Happened One Night', how does Ellie Andrews successfully flag down a passing car when Peter's hitchhiking techniques fail miserably?",
        "She lifts up her skirt to reveal her silk-stockinged leg",
        ["She stands directly in the center of the road", "She waves a bright red handkerchief", "She pretends to faint onto the gravel shoulder"],
        2
    ),
    # 66 - d2
    (
        "In 'Bringing Up Baby' (1938), what missing object is paleontologist David Huxley desperately hunting for throughout the countryside?",
        "An intercostal clavicle bone for a brontosaurus skeleton",
        ["A golden mastodon tusk", "A rare jade dinosaur tooth", "A petrified velociraptor skull"],
        2
    ),
    # 67 - d2
    (
        "In 'Bringing Up Baby', what kind of animal is 'Baby'?",
        "A tame pet leopard",
        ["A mischievous chimpanzee", "A baby African lion", "A runaway tiger cub"],
        2
    ),
    # 68 - d2
    (
        "In 'The Philadelphia Story', what trade do Macaulay 'Mike' Connor and Liz Imbrie ply when they infiltrate Tracy Lord's wedding estate?",
        "Tabloid journalists for Spy Magazine",
        ["Private insurance investigators", "Hired caterers from New York", "Society portrait photographers"],
        2
    ),
    # 69 - d2
    (
        "In 'Breakfast at Tiffany's', what does Holly Golightly name her ginger cat throughout the entire film?",
        "Cat",
        ["Tiffany", "Doc", "Rusty"],
        2
    ),
    # 70 - d2
    (
        "In 'Annie Hall', which real-life media philosopher makes an unexpected cameo in a movie theater lobby to settle an intellectual argument?",
        "Marshall McLuhan",
        ["Noam Chomsky", "Susan Sontag", "Roland Barthes"],
        2
    ),

    # 71 - d3
    (
        "In 'Broadcast News' (1987), who plays the brilliant, cynical reporter Aaron Altman who endures an agonizing bout of profuse sweating on air?",
        "Albert Brooks",
        ["William Hurt", "Robert Prosky", "Jack Nicholson"],
        3
    ),
    # 72 - d3
    (
        "In 'Say Anything...', what specific model of boombox does Lloyd Dobler hold over his head on the lawn outside Diane's bedroom?",
        "Toshiba RT-SX1",
        ["Sony Boombox CFS-2000", "Panasonic RX-5085", "Sanyo M-9935"],
        3
    ),
    # 73 - d3
    (
        "In 'When Harry Met Sally...', what is the topic of the film Sally Albright and Harry Burns watch simultaneously over the phone while lying in their respective beds?",
        "Casablanca",
        ["An Affair to Remember", "The Apartment", "Roman Holiday"],
        3
    ),
    # 74 - d3
    (
        "In 'Sleepless in Seattle', what classic 1957 romance film does Suzy (Rita Wilson) tearfully recount over dinner, driving Sam and Greg crazy?",
        "An Affair to Remember",
        ["Love Affair", "Now, Voyager", "Brief Encounter"],
        3
    ),
    # 75 - d3
    (
        "In 'You've Got Mail', what 19th-century classic English novel do Kathleen Kelly and Joe Fox repeatedly discuss in their letters and meetings?",
        "Pride and Prejudice",
        ["Jane Eyre", "Wuthering Heights", "Sense and Sensibility"],
        3
    ),
    # 76 - d3
    (
        "In 'Four Weddings and a Funeral', who plays Henrietta, Charles's emotionally volatile former girlfriend known derisively as 'Duckface'?",
        "Anna Chancellor",
        ["Kristin Scott Thomas", "Sophie Thompson", "Charlotte Coleman"],
        3
    ),
    # 77 - d3
    (
        "In 'Notting Hill', what false identity does William Thacker assume when he blunders into Anna Scott's international press junket at the Ritz?",
        "A writer for Horse & Hound magazine",
        ["An editor for Country Life", "A critic for The Daily Telegraph", "A film correspondent for Time Out London"],
        3
    ),
    # 78 - d3
    (
        "In 'Pretty Woman', what is the name of the snooty saleswoman at the high-end boutique who snubs Vivian on her initial shopping trip?",
        "Mary Pat Gleason's boutique supervisor (credited as Saleswoman)",
        ["Evelyn Ward", "Madeline Vance", "Beatrice Montgomery"],
        3
    ),
    # 79 - d3
    (
        "In '10 Things I Hate About You', what musical instrument does Kat Stratford yearn to buy with her own savings, which Patrick secretly buys for her?",
        "A 1964 Fender Stratocaster guitar",
        ["A vintage Gibson Les Paul guitar", "An upright acoustic cello", "A vintage Yamaha trumpet"],
        3
    ),
    # 80 - d3
    (
        "In 'Clueless', what specific philosopher does Cher quote during her impromptu oral presentation on immigration and dinner parties?",
        "She quotes the statue of Liberty's inscription by Emma Lazarus and 'the Haitians'",
        ["Thomas Hobbes", "Jean-Jacques Rousseau", "John Locke"],
        3
    ),
    # 81 - d3
    (
        "In 'Groundhog Day', what is the name of the Pennsylvania diner where Phil Connors gorges on pastries and coffee every single day?",
        "Tip Top Cafe",
        ["Punxsutawney Corner Diner", "Gobbler's Grill", "Cherry Street Coffee Shop"],
        3
    ),
    # 82 - d3
    (
        "In 'Bridget Jones's Diary', what is the real name of the publishing firm where Bridget works for Daniel Cleaver?",
        "Pemberley Press",
        ["Bloomsbury House", "Picador Press", "Grafton & Cole"],
        3
    ),
    # 83 - d3
    (
        "In 'My Best Friend's Wedding', what song does Julianne sabotage Kimmy into singing poorly during an awkward night at a Chicago karaoke bar?",
        "I Just Don't Know What to Do with Myself",
        ["Wishin' and Hopin'", "The Look of Love", "Anyone Who Had a Heart"],
        3
    ),
    # 84 - d3
    (
        "In 'The Wedding Singer', what is the name of Robbie Hart's unreliable rival who is engaged to Julia Sullivan?",
        "Glenn Guglia",
        ["George Stitzer", "Ricky Taylor", "Brad Miller"],
        3
    ),
    # 85 - d3
    (
        "In 'High Fidelity' (2000), what is the name of Rob Gordon's vintage vinyl record store in Chicago?",
        "Championship Vinyl",
        ["Groove Records", "Wax Trax", "Sonic Sound Emporium"],
        3
    ),
    # 86 - d3
    (
        "In 'High Fidelity', what are the names of Rob Gordon's two idiosyncratic, opinionated record store clerks?",
        "Barry and Dick",
        ["Mark and Todd", "Sam and Steve", "Julian and Arthur"],
        3
    ),
    # 87 - d3
    (
        "In 'Amélie' (2001), what unusual souvenir does Amélie arrange for her reclusive father to receive from around the globe?",
        "Photographs of his garden gnome posing in front of world landmarks",
        ["Postcards from vintage French bakeries", "Antique porcelain tea spoons", "Snow globes from European capitals"],
        3
    ),
    # 88 - d3
    (
        "In 'Amélie', what eccentric object does Nino Quincampoix obsessively collect from Parisian train station photo booths?",
        "Discarded, torn passport photo strips",
        ["Lost metro transit tokens", "Abandoned train ticket stubs", "Unclaimed luggage tags"],
        3
    ),
    # 89 - d3
    (
        "In 'Along Came Polly' (2004), what unusual exotic pet does Polly Prince own that constantly runs into walls?",
        "A blind ferrets named Rodolfo",
        ["A hairless cat named Sphynx", "A three-legged iguana named Speedy", "A deaf parakeet named Paco"],
        3
    ),
    # 90 - d3
    (
        "In 'Along Came Polly', what sport does Reuben Feffer (Ben Stiller) uncomfortably play with an intensely sweaty Sandy Lyle (Philip Seymour Hoffman)?",
        "Racquetball",
        ["Squash", "Pickleball", "Badminton"],
        3
    ),
    # 91 - d3
    (
        "In 'Crazy Rich Asians', what dish are Rachel Chu, Nick Young, and his family hand-assembling during their intimate family gathering?",
        "Dumplings (jiaozi)",
        ["Spring rolls (lumpia)", "Curry puffs", "Mooncakes"],
        3
    ),
    # 92 - d3
    (
        "In 'Crazy Rich Asians', which high-society matriarch challenges Rachel to the tense climactic mahjong showdown?",
        "Eleanor Sung-Young",
        ["Ah Ma (Shang Su Yi)", "Astrid Leong-Teo", "Felicity Young"],
        3
    ),
    # 93 - d3
    (
        "In 'Palm Springs', what quantum physics phenomenon does Sarah Wilder study obsessively via online lectures to escape the time loop?",
        "Cauchy horizons and spacetime singularities inside the cave",
        ["String theory vibrations in micro-wormholes", "Quantum entanglement in tachyonic fields", "Bose-Einstein condensates in closed timelike curves"],
        3
    ),
    # 94 - d3
    (
        "In 'Set It Up', what unusual phobia or neurosis does sports tycoon boss Rick (Taye Diggs) suffer from?",
        "Extreme sensitivity to warm room temperature and specific golf stroke rhythm",
        ["Fear of elevator chimes", "Aversion to paper staples", "Obsession with green pens"],
        3
    ),
    # 95 - d3
    (
        "In 'Always Be My Maybe', what pretentious culinary technique does chef Sasha Tran showcase in her cutting-edge restaurant?",
        "Translucent noodles served with micro-herbs and soundscapes",
        ["Deconstructed liquid nitrogen pho", "Foam-infused edible gold dumplings", "Aerosolized wagyu beef vapors"],
        3
    ),
    # 96 - d3
    (
        "In 'His Girl Friday' (1940), what is the occupation of Hildy Johnson's mild-mannered fiancé Bruce Baldwin, whom Walter Burns tries to derail?",
        "An insurance salesman from Albany",
        ["A bond broker from Philadelphia", "A bank manager from Boston", "A dentist from Detroit"],
        3
    ),
    # 97 - d3
    (
        "In 'The Shop Around the Corner' (1940), what novelty musical item sold at Matuschek and Company causes a debate between Kralik and Mr. Matuschek?",
        "A musical cigarette box that plays 'Ochi Tchornya'",
        ["A clockwork dancing ballerina music box", "A miniature Swiss chime lighter", "A carved cuckoo clock that plays Strauss waltzes"],
        3
    ),
    # 98 - d3
    (
        "In 'Pillow Talk' (1959), what profession does Doris Day's character Jan Morrow pursue in Manhattan?",
        "Interior decorator",
        ["Advertising executive", "Fashion illustrator", "Magazine copywriter"],
        3
    ),
    # 99 - d3
    (
        "In 'Sabrina' (1954), what culinary culinary faux pas does Sabrina Fairchild commit while attending cooking school in Paris?",
        "She fails to crack an egg properly with one hand and burns her soufflé",
        ["She curdles the béarnaise sauce by overheating the pan", "She forgets the yeast in her brioche dough", "She mistakenly uses salt instead of sugar in the crêpes"],
        3
    ),
    # 100 - d3
    (
        "In 'Annie Hall' (1977), what classic line does Alvy Singer deliver regarding life being full of loneliness, misery, and suffering?",
        "And the other half is it's all over much too quickly",
        ["And yet we queue up for it every morning", "And that's why we move to California", "And God doesn't even offer a refund"],
        3
    ),
]

if __name__ == "__main__":
    make_batch(questions_batch2, 2, "tools/staging/rom_com_batch2.json")
