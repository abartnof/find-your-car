import sys
from make_batch import build_batch

questions = [
    (
        'What was the real alien birth name of the furry extraterrestrial known as ALF?',
        'Gordon Shumway',
        ['Melmac Martin', 'Orson Cooper', 'Ziggy Stardust'],
        3
    ),
    (
        'What planet did ALF hail from before it exploded when all residents plugged in hair dryers?',
        'Melmac',
        ['Ork', 'Vulcan', 'Krypton'],
        1
    ),
    (
        'What did the acronym A.L.F. stand for when the Tanner family took him into their home?',
        'Alien Life Form',
        ['Advanced Lunar Flyer', 'Autonomous Living Foreigner', 'Astronomical Life Force'],
        1
    ),
    (
        'What household animal did ALF obsessively try to capture and eat as a Melmacian delicacy?',
        'Lucky the family cat',
        ["The neighbor's parrot", 'A pet ferret', 'A goldfish in the bowl'],
        1
    ),
    (
        'Who played the long-suffering, neurotic father Willie Tanner on ALF?',
        'Max Wright',
        ['Bob Saget', 'Alan Thicke', 'Michael Gross'],
        1
    ),
    (
        "Which actress played Willie's sensible wife Kate Tanner on ALF?",
        'Anne Schedeen',
        ['Joanna Kerns', 'Meredith Baxter', 'Marion Ross'],
        2
    ),
    (
        'Who was the puppeteer, co-creator, and primary voice behind ALF?',
        'Paul Fusco',
        ['Jim Henson', 'Frank Oz', 'Kevin Clash'],
        1
    ),
    (
        'What physical condition on the set made filming ALF a grueling nightmare for human cast members?',
        'Dozens of open trapdoors cut into the floor so puppeteers could operate the puppet',
        ['Extreme arctic air conditioning to prevent the puppet fur from melting', 'Deafening sound baffles that prevented actors from hearing cues', 'Harmful ultraviolet lighting required for puppet visibility'],
        2
    ),
    (
        'What dramatic reaction did actor Max Wright famously have when the final episode of ALF wrapped filming in 1990?',
        'He silently walked off the set, got in his car, and drove away without saying goodbye to anyone',
        ['He set the ALF puppet on fire in the studio parking lot', 'He smashed his dressing room mirror with a baseball bat', 'He immediately shaved his head and moved to Europe'],
        2
    ),
    (
        'How many stomachs did ALF have according to Melmacian biology?',
        'Eight stomachs',
        ['Four stomachs', 'Two stomachs', 'Twelve stomachs'],
        2
    ),
    (
        "What grim cliffhanger concluded the final televised episode of ALF ('Consider Me Gone') in 1990?",
        'ALF was captured and surrounded by armed soldiers of the Alien Task Force',
        ['The Tanner family home was destroyed in a gas leak', "ALF's rescue spaceship exploded in the upper atmosphere", 'Willie Tanner was arrested for harboring an illegal alien'],
        2
    ),
    (
        'What was the name of the snooping, obnoxious next-door neighbors on ALF?',
        'The Ochmoneks (Trevor and Raquel)',
        ['The Koosmans', 'The Kravitzes', 'The Steves'],
        2
    ),
    (
        'Which veteran comedy actor played neighbor Trevor Ochmonek on ALF?',
        'John LaMotta',
        ['Liz Sheridan', 'Ray Walston', 'Dolph Sweet'],
        3
    ),
    (
        "Which actress played the gossiping neighbor Raquel Ochmonek, and later Jerry's mother Helen on Seinfeld?",
        'Liz Sheridan',
        ['Estelle Harris', 'Doris Roberts', 'Alice Ghostley'],
        3
    ),
    (
        'What network broadcast ALF on Monday nights from 1986 to 1990?',
        'NBC',
        ['CBS', 'ABC', 'Fox'],
        1
    ),
    (
        'What was the name of the historic Vermont bed-and-breakfast inn run by Dick Loudon on Newhart?',
        'The Stratford Inn',
        ['The Green Mountain Lodge', 'The colonial Haven', 'The Yankee Wayfarer'],
        3
    ),
    (
        'Which legendary low-key comedian starred as author and innkeeper Dick Loudon on Newhart?',
        'Bob Newhart',
        ['Tom Poston', 'Dick Van Dyke', 'Alan Alda'],
        1
    ),
    (
        "Which actress played Dick Loudon's cheerful wife Joanna on Newhart?",
        'Mary Frann',
        ['Julia Duffy', 'Suzanne Pleshette', 'Bonnie Bartlett'],
        2
    ),
    (
        'Who played the lovable, dim-witted handyman George Utley at the Stratford Inn?',
        'Tom Poston',
        ['Peter Scolari', 'William Sanderson', 'Jack Elam'],
        1
    ),
    (
        'Which actress played the spoiled, wealthy maid Stephanie Vanderkellen who refused to do housework?',
        'Julia Duffy',
        ['Jennifer Holmes', 'Mary Frann', 'Annie Potts'],
        3
    ),
    (
        'Which actor played Michael Grassoff, the pretentious TV producer who fell in love with Stephanie?',
        'Peter Scolari',
        ['Tom Hanks', 'Mark Linn-Baker', 'Curtis Armstrong'],
        3
    ),
    (
        'What was the name of the local public television talk show hosted by Dick Loudon in Vermont?',
        'Vermont Today',
        ['Stratford Journal', 'Green Mountain Morning', 'New England Chronicle'],
        2
    ),
    (
        'What famous catchphrase introduced the three eccentric backwoods brothers on Newhart?',
        "Hi, I'm Larry, this is my brother Darryl, and this is my other brother Darryl",
        ["We're the Darryls and this is Larry", 'Good day from the mountain brothers', "Here's Larry and the boys from the woods"],
        1
    ),
    (
        'Which actor played the talkative backwoods brother Larry on Newhart?',
        'William Sanderson',
        ['Tony Papenfuss', 'John Voldstad', 'Tom Poston'],
        2
    ),
    (
        "What unusual quirk characterized Larry's two brothers, both named Darryl, throughout almost the entire series?",
        'They never spoke a single word until the final episode',
        ['They only communicated through acoustic guitar duets', 'They wore ski masks in every season', 'They walked exclusively backwards'],
        3
    ),
    (
        'What shocking revelation in the 1990 Newhart series finale is celebrated as one of the greatest twists in TV history?',
        'The entire series was a dream of psychologist Bob Hartley from The Bob Newhart Show',
        ['The Stratford Inn was actually a simulation aboard an alien spacecraft', 'Dick Loudon was revealed to be a patient in a psychiatric hospital', 'George Utley was revealed to be an undercover billionaire'],
        1
    ),
    (
        'Which classic actress made a surprise appearance in bed beside Bob Newhart in the final scene of Newhart?',
        'Suzanne Pleshette (as Emily Hartley)',
        ['Mary Frann', 'Julia Duffy', 'Mary Tyler Moore'],
        1
    ),
    (
        'Whose real-life idea was the brilliant dream-twist finale of Newhart?',
        "Bob Newhart's real-life wife Ginny Newhart",
        ['Executive producer Barry Kemp', 'Brandon Tartikoff', 'Suzanne Pleshette herself'],
        3
    ),
    (
        'What sport did Japanese developers turn the entire town of Stratford into during the surreal final season?',
        'A giant golf resort',
        ['A Formula 1 racing track', 'A mega ski resort', 'A luxury yacht harbor'],
        3
    ),
    (
        'How many seasons did Newhart air on CBS between 1982 and 1990?',
        '8 seasons',
        ['6 seasons', '7 seasons', '9 seasons'],
        2
    ),
    (
        'Which actor played the wide-eyed immigrant shepherd Balki Bartokomous on Perfect Strangers?',
        'Bronson Pinchot',
        ['Mark Linn-Baker', 'Curtis Armstrong', 'Sam Anderson'],
        1
    ),
    (
        'What fictional Mediterranean island nation did Balki Bartokomous emigrate from?',
        'Mypos',
        ['Sokovia', 'Krakhozia', 'Genovia'],
        1
    ),
    (
        "Who played Balki's high-strung, neurotic American cousin Larry Appleton?",
        'Mark Linn-Baker',
        ['Bronson Pinchot', 'Peter Scolari', 'Scott Valentine'],
        1
    ),
    (
        'In what major Midwestern city was Perfect Strangers set?',
        'Chicago, Illinois',
        ['Milwaukee, Wisconsin', 'Cleveland, Ohio', 'Detroit, Michigan'],
        1
    ),
    (
        'What celebratory routine did Balki and Larry perform whenever something went right?',
        'The Dance of Joy',
        ['The Mypos Mambo', 'The Shepherd Shuffle', 'The Victory Waltz'],
        3
    ),
    (
        "What was Balki Bartokomous's signature verbal catchphrase on Perfect Strangers?",
        "Don't be ridiculous!",
        ['Have mercy!', "Whatcha talkin' 'bout?", 'Cut it out!'],
        3
    ),
    (
        'What metropolitan newspaper company employed both Larry and Balki, starting in the basement mailroom?',
        'The Chicago Chronicle',
        ['The Chicago Sun-Times', 'The Chicago Tribune', 'The Daily Planet'],
        3
    ),
    (
        'Who played the mean-spirited, ulcer-ridden mailroom boss Mr. Sam Gorpley on Perfect Strangers?',
        'Sam Anderson',
        ["F.J. O'Neil", 'Ernie Sabella', 'Eugene Roche'],
        2
    ),
    (
        "What airline flight attendants lived upstairs and became Larry and Balki's romantic partners?",
        'Jennifer Lyons and Mary Anne Spencer',
        ['Caitlin and Trudy', 'Stephanie and Leslie', 'Becky and Dana'],
        2
    ),
    (
        'Which production powerhouse created Perfect Strangers, Full House, and Family Matters for ABC?',
        'Miller-Boyett Productions',
        ['Witt/Thomas/Harris Productions', 'MTM Enterprises', 'Carsey-Werner Company'],
        2
    ),
    (
        'What beloved ABC Friday night programming block was anchored by Perfect Strangers and Full House?',
        "TGIF (Thank Goodness It's Friday)",
        ['Must See TV', 'Friday Night Sins', 'Comedy Night Done Right'],
        1
    ),
    (
        'What popular sitcom spun off from Perfect Strangers after introducing elevator operator Harriette Winslow?',
        'Family Matters',
        ['Step by Step', "Hangin' with Mr. Cooper", 'Boy Meets World'],
        1
    ),
    (
        'What beloved character did Jaleel White introduce on Family Matters, becoming an international phenomenon?',
        'Steve Urkel',
        ['Carlton Banks', 'Waldo Geraldo Faldo', 'Eddie Winslow'],
        1
    ),
    (
        'What was the name of the traditional Myposian holiday game played with stuffed sheep organs?',
        'Bibibabkas / Pig-in-a-Poke traditions',
        ['Bocce ball', 'Tug-of-war', 'Fleece toss'],
        3
    ),
    (
        'Who played the miserable, cynical shoe salesman Al Bundy on Married... with Children?',
        "Ed O'Neill",
        ['David Faustino', 'David Garrison', 'Ted McGinley'],
        1
    ),
    (
        "Which actress played Al's leopard-print-wearing, bonbon-eating wife Peg Bundy?",
        'Katey Sagal',
        ['Amanda Bearse', 'Christina Applegate', 'Edie McClurg'],
        3
    ),
    (
        "Which actress starred as the ditzy, blonde teenage daughter Kelly Bundy ('The Pumpkin')?",
        'Christina Applegate',
        ['Katey Sagal', 'Amanda Bearse', 'Tracey Gold'],
        3
    ),
    (
        "Who played the younger son Bud Bundy, who invented the hip-hop alter-ego 'Grandmaster B'?",
        'David Faustino',
        ['Danny Pintauro', 'Jeremy Miller', 'Brian Bonsall'],
        3
    ),
    (
        "What was Al Bundy's proudest athletic accomplishment that he brought up in almost every episode?",
        'Scoring four touchdowns in a single game for Polk High',
        ['Winning the Illinois state wrestling championship', 'Hitting three home runs in the city finals', 'Kicking a 60-yard field goal in the snow'],
        1
    ),
    (
        "What was Al Bundy's depressing day job throughout Married... with Children?",
        "Women's shoe salesman at Gary's Shoes",
        ['Used car salesman', "Plumber's assistant", 'Tire mechanic at Sears'],
        1
    ),
    (
        "Which actress played the uptight, feminist bank manager neighbor Marcy Rhoades D'Arcy?",
        'Amanda Bearse',
        ['Katey Sagal', 'Christina Applegate', 'Julia Duffy'],
        2
    ),
    (
        "Who played Marcy's henpecked first husband Steve Rhoades, who eventually abandoned her to become a forest ranger?",
        'David Garrison',
        ['Ted McGinley', "Ed O'Neill", 'David Faustino'],
        2
    ),
    (
        "Who played Marcy's handsome, lazy second husband Jefferson D'Arcy starting in season 5?",
        'Ted McGinley',
        ['David Garrison', 'Michael Gross', 'Larry Manetti'],
        2
    ),
    (
        "What anti-feminist men's club did Al Bundy found with his neighborhood buddies?",
        "NO MA'AM (National Organization of Men Against Amazonian Masterhood)",
        ['THE BOYS (Brothers Over Yielding Spouses)', 'MEN ONLY', 'POLK ALUMNI'],
        2
    ),
    (
        'What Frank Sinatra standard served as the iconic theme song for Married... with Children?',
        'Love and Marriage',
        ['My Way', 'Fly Me to the Moon', 'Come Fly With Me'],
        3
    ),
    (
        'What national controversy in 1989 accidentally turned Married... with Children into a massive ratings smash?',
        'Michigan activist Terry Rakolta launched a nationwide boycott campaign against advertisers',
        ['The Catholic Church banned its broadcast in major cities', 'The FCC fined Fox $10 million for indecency', "Ed O'Neill was sued by shoe manufacturers"],
        2
    ),
    (
        'What network broadcast Married... with Children as its defining prime-time subversive hit starting in 1987?',
        'Fox',
        ['NBC', 'CBS', 'ABC'],
        3
    ),
    (
        "What was the name of the Bundy family's cynical sheepdog, whose inner thoughts were voiced by Cheech Marin?",
        'Buck',
        ['Lucky', 'Barnaby', 'Buster'],
        2
    ),
    (
        'What beat-up, brown American car did Al Bundy drive for hundreds of thousands of miles?',
        "1974 Dodge Dart (frequently called the 'Dodge')",
        ['1972 Ford Pinto', '1976 Chevrolet Vega', '1975 AMC Gremlin'],
        2
    ),
    (
        'Who played widowed morning show host and neat-freak father Danny Tanner on Full House?',
        'Bob Saget',
        ['John Stamos', 'Dave Coulier', 'Alan Thicke'],
        1
    ),
    (
        'Which heartthrob actor played Elvis-loving, guitar-playing Uncle Jesse Katsopolis on Full House?',
        'John Stamos',
        ['Bob Saget', 'Dave Coulier', 'Scott Valentine'],
        1
    ),
    (
        "What was Uncle Jesse's famous three-word catchphrase whenever he saw something alluring?",
        'Have mercy!',
        ['Cut it out!', 'How rude!', 'You got it, dude!'],
        1
    ),
    (
        'Who played comic-impressionist and stand-up comedian Joey Gladstone on Full House?',
        'Dave Coulier',
        ['Bob Saget', 'John Stamos', 'Howie Mandel'],
        3
    ),
    (
        'What physical gesture and catchphrase did Joey Gladstone use when delivering comedy bits?',
        'Cut... it... out! (with hand scissor gesture)',
        ['Have mercy!', 'Bada-bing bada-boom!', "Don't be ridiculous!"],
        3
    ),
    (
        'Which infant twin sisters shared the breakout role of youngest daughter Michelle Tanner?',
        'Mary-Kate and Ashley Olsen',
        ['Kelsey and Kirsten Dohring', 'Tia and Tamera Mowry', 'Camilla and Rebecca Rosso'],
        3
    ),
    (
        "What was toddler Michelle Tanner's signature thumbs-up catchphrase?",
        'You got it, dude!',
        ['How rude!', 'No way, Jose!', 'Have mercy!'],
        1
    ),
    (
        "Which actress played the sassy, middle daughter Stephanie Tanner, famous for saying 'How rude!'?",
        'Jodie Sweetin',
        ['Candace Cameron', 'Mary-Kate Olsen', 'Andrea Barber'],
        1
    ),
    (
        'Which actress played the responsible oldest daughter D.J. Tanner on Full House?',
        'Candace Cameron',
        ['Jodie Sweetin', 'Andrea Barber', 'Tracey Gold'],
        1
    ),
    (
        "Which actress played D.J.'s eccentric, foul-footed next-door neighbor Kimmy Gibbler?",
        'Andrea Barber',
        ['Lori Loughlin', 'Jodie Sweetin', 'Candace Cameron'],
        2
    ),
    (
        "Which actress played Danny's morning show co-host Rebecca Donaldson, who married Uncle Jesse?",
        'Lori Loughlin',
        ['Andrea Barber', 'Candace Cameron', 'Joanna Kerns'],
        2
    ),
    (
        'What was the name of the morning television talk show co-hosted by Danny Tanner and Rebecca Donaldson?',
        'Wake Up, San Francisco',
        ['Good Morning Bay Area', 'San Francisco Today', 'The Bay Morning Show'],
        2
    ),
    (
        "What was the name of Uncle Jesse's rock band on Full House?",
        'Jesse and the Rippers',
        ['The San Francisco Sound', "The Rockin' Tanner Boys", 'The Sunset Express'],
        2
    ),
    (
        "Who performed the upbeat Full House theme song 'Everywhere You Look'?",
        'Jesse Frederick',
        ['Gary Portnoy', 'Randy Newman', 'Alan Thicke'],
        3
    ),
    (
        'Which former WKRP in Cincinnati star played history teacher Charlie Moore on Head of the Class?',
        'Howard Hesseman',
        ['Billy Connolly', 'Gordon Jump', 'Hal Linden'],
        2
    ),
    (
        'What was the name of the gifted student program at Millard Fillmore High School in Head of the Class?',
        'IHP (Individualized Honors Program)',
        ['GATE (Gifted and Talented Education)', 'AP Scholars', 'The Fillmore Elite'],
        2
    ),
    (
        'Which future celebrity and heavyweight boxing wife starred as honors student Darlene Merriman on Head of the Class?',
        'Robin Givens',
        ['Holly Robinson', 'Kim Fields', 'Pam Grier'],
        2
    ),
    (
        'Which Scottish stand-up comedian took over the teaching role as Billy Mac in the final season of Head of the Class?',
        'Billy Connolly',
        ['Craig Ferguson', 'Robbie Coltrane', 'Peter Capaldi'],
        3
    ),
    (
        'Which actor played Boston private investigator Spenser on the acclaimed 1985-1988 drama Spenser: For Hire?',
        'Robert Urich',
        ['Avery Brooks', 'Tom Selleck', 'David Soul'],
        2
    ),
    (
        "Which future Star Trek: Deep Space Nine star played Spenser's lethal, bald enforcer ally Hawk?",
        'Avery Brooks',
        ['Tony Todd', 'Carl Weathers', 'Taurean Blacque'],
        2
    ),
    (
        'Which British rock drummer composed the driving synthesizer theme for The Equalizer starring Edward Woodward?',
        'Stewart Copeland (of The Police)',
        ['Phil Collins', 'Neil Peart', 'Roger Taylor'],
        3
    ),
    (
        'What British actor starred as former intelligence operative Robert McCall on the 1985 series The Equalizer?',
        'Edward Woodward',
        ['Patrick Macnee', 'John Gielgud', 'Michael Caine'],
        2
    ),
    (
        'Which iconic voice actor provided the booming, noble voice of Autobot leader Optimus Prime in The Transformers?',
        'Peter Cullen',
        ['Frank Welker', 'Scatman Crothers', 'Casey Kasem'],
        1
    ),
    (
        'Which legendary voice actor voiced Decepticon leader Megatron and Soundwave in The Transformers?',
        'Frank Welker',
        ['Peter Cullen', 'Don Messick', 'Mel Blanc'],
        2
    ),
    (
        'What battle cry did Prince Adam shout while lifting his magic sword in He-Man and the Masters of the Universe?',
        'By the power of Grayskull! I have the power!',
        ['Thunder, Thunder, Thundercats, Ho!', 'Autobots, roll out!', 'Knowing is half the battle!'],
        3
    ),
    (
        'What was the moral lesson slogan concluding every animated episode of G.I. Joe: A Real American Hero?',
        'Now you know, and knowing is half the battle!',
        ["Always do what's right!", 'Stay safe, stay American!', 'Heroes never give up!'],
        3
    ),
    (
        'What wealthy Disney character swam through a mountain of gold coins in the 1987 syndicated smash DuckTales?',
        'Scrooge McDuck',
        ['Donald Duck', 'Launchpad McQuack', 'Flintheart Glomgold'],
        3
    ),
    (
        "Which future Oscar-nominated superstar played Cowboy Curtis on Pee-wee's Playhouse in the late 1980s?",
        'Laurence Fishburne',
        ['Samuel L. Jackson', 'Morgan Freeman', 'Denzel Washington'],
        3
    ),
    (
        "What was the magic phrase chanted by Jambi the Genie on Pee-wee's Playhouse to grant wishes?",
        'Meka leka hi meka hiney ho',
        ['Abracadabra alakazam', 'Sim sala bim', 'Klaatu barada nikto'],
        2
    ),
    (
        "What network executive oversaw NBC's legendary prime-time turnaround in the 1980s with Cheers and The Cosby Show?",
        'Brandon Tartikoff',
        ['Grant Tinker', 'Fred Silverman', 'Warren Littlefield'],
        2
    ),
    (
        'What was the highest-rated single prime-time television broadcast of the entire 1980s decade (over 105 million viewers)?',
        "The series finale of M*A*S*H ('Goodbye, Farewell and Amen' in February 1983)",
        ["The 'Who Shot J.R.?' resolution on Dallas", 'The series finale of Cheers', 'The Moldavian Massacre on Dynasty'],
        2
    ),
    (
        'In what year did the Fox Broadcasting Company launch its revolutionary prime-time Sunday evening programming?',
        '1987',
        ['1985', '1989', '1991'],
        2
    ),
    (
        'Which iconic 1980s sci-fi series featured Scott Bakula leaping through time to correct historical mistakes?',
        'Quantum Leap',
        ['Voyagers!', 'Sliders', 'The Time Tunnel'],
        1
    ),
    (
        'Who played the cigar-smoking, hologram companion Admiral Al Calavicci on Quantum Leap?',
        'Dean Stockwell',
        ['Scott Bakula', 'John Cullum', 'Bruce McGill'],
        2
    ),
    (
        "What was Sam Beckett's famous two-word reaction whenever he leaped into a shocking new body or situation on Quantum Leap?",
        'Oh boy',
        ['Great Scott', 'Holy cow', 'Not again'],
        3
    ),
    (
        'Which newsroom sitcom starring Candice Bergen debuted on CBS in 1988, centering on the newsmagazine FYI?',
        'Murphy Brown',
        ['Designing Women', 'The Mary Tyler Moore Show', 'Broadcast News'],
        3
    ),
    (
        'Who created the sharp-witted political and feminist newsroom comedy Murphy Brown?',
        'Diane English',
        ['Linda Bloodworth-Thomason', 'Susan Harris', 'Marta Kauffman'],
        2
    ),
    (
        'Which groundbreaking blue-collar sitcom debuted on ABC in 1988 starring Roseanne Barr and John Goodman?',
        'Roseanne',
        ['Married... with Children', 'Grace Under Fire', 'The Conners'],
        1
    ),
    (
        'In what fictional Illinois factory town was the sitcom Roseanne set?',
        'Lanford',
        ['Springfield', 'Peoria', 'Rockford'],
        2
    ),
    (
        "Which actress won three consecutive Primetime Emmy Awards playing Roseanne's neurotic sister Jackie Harris?",
        'Laurie Metcalf',
        ['Sara Gilbert', 'Estelle Parsons', 'Sandra Bernhard'],
        2
    ),
    (
        "What was the name of the mechanical robot on Pee-wee's Playhouse who dispensed the secret word of the day?",
        'Conky 2000',
        ['Robbie the Robot', 'Clocky', 'Mr. Computer'],
        2
    ),
]

if __name__ == "__main__":
    build_batch(questions, 10, "tools/staging/80s_tv_shows_batch10.json")
