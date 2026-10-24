import sys
import os
sys.path.append(os.path.dirname(__file__))
from utils import assemble_batch, save_batch

QUESTIONS = [
    # 1-10
    {
        "q": "Which The Weeknd synth-pop smash spent an unprecedented 90 weeks on the Billboard Hot 100 and was crowned the #1 song in Hot 100 history in 2021?",
        "correct": "Blinding Lights",
        "wrong": ["Save Your Tears", "Heartless", "Starboy"],
        "d": 1
    },
    {
        "q": "How many weeks did The Weeknd's 'Blinding Lights' spend in the top 5 of the Billboard Hot 100, setting an all-time record?",
        "correct": "43 weeks",
        "wrong": ["26 weeks", "35 weeks", "52 weeks"],
        "d": 2
    },
    {
        "q": "Which pop superstar was featured on the remix of The Weeknd's 'Save Your Tears', propelling it to #1 on the Billboard Hot 100 in May 2021?",
        "correct": "Ariana Grande",
        "wrong": ["Doja Cat", "Dua Lipa", "Rosalía"],
        "d": 1
    },
    {
        "q": "What debut single by 17-year-old Olivia Rodrigo spent its first eight weeks at #1 on the Billboard Hot 100 in early 2021?",
        "correct": "drivers license",
        "wrong": ["deja vu", "good 4 u", "traitor"],
        "d": 1
    },
    {
        "q": "Which pop-punk song by Olivia Rodrigo debuted at #1 on the Billboard Hot 100 in May 2021, her second #1 debut from 'SOUR'?",
        "correct": "good 4 u",
        "wrong": ["brutal", "deja vu", "vampire"],
        "d": 1
    },
    {
        "q": "Which members of Paramore were retroactively awarded songwriting credits on Olivia Rodrigo's 'good 4 u' due to similarities to 'Misery Business'?",
        "correct": "Hayley Williams and Josh Farro",
        "wrong": ["Taylor York and Zac Farro", "Jeremy Davis and Chad Gilbert", "Hayley Williams and Taylor York"],
        "d": 2
    },
    {
        "q": "What lead single from Olivia Rodrigo's second album 'GUTS' debuted at #1 on the Billboard Hot 100 in July 2023?",
        "correct": "vampire",
        "wrong": ["bad idea right?", "get him back!", "all-american bitch"],
        "d": 1
    },
    {
        "q": "Which Dua Lipa disco-pop track was crowned the Billboard Year-End #1 single of 2021 despite never reaching #1 on the weekly Hot 100?",
        "correct": "Levitating",
        "wrong": ["Don't Start Now", "Break My Heart", "Physical"],
        "d": 2
    },
    {
        "q": "What was the highest weekly peak position reached by Dua Lipa's 'Levitating' on the Billboard Hot 100?",
        "correct": "#2",
        "wrong": ["#3", "#4", "#5"],
        "d": 2
    },
    {
        "q": "Which Harry Styles single spent 15 weeks at #1 on the Billboard Hot 100 in 2022, becoming the fourth-longest-running #1 in chart history?",
        "correct": "As It Was",
        "wrong": ["Watermelon Sugar", "Adore You", "Late Night Talking"],
        "d": 1
    },

    # 11-20
    {
        "q": "Whose child's voice appears at the beginning of Harry Styles' 'As It Was', saying 'Come on Harry, we want to say goodnight to you'?",
        "correct": "His goddaughter Ruby Winston",
        "wrong": ["His younger cousin", "A fan's voice memo", "His producer's daughter"],
        "d": 3
    },
    {
        "q": "What was Harry Styles' very first #1 single on the Billboard Hot 100, reaching the summit in August 2020?",
        "correct": "Watermelon Sugar",
        "wrong": ["Sign of the Times", "Lights Up", "Adore You"],
        "d": 2
    },
    {
        "q": "In November 2022, Taylor Swift made Billboard history with 'Midnights' by achieving what unprecedented Hot 100 feat?",
        "correct": "Occupying all top 10 positions simultaneously",
        "wrong": ["Holding the top 5 spots for 10 straight weeks", "Debuting 25 songs in the top 25", "Selling 2 million physical vinyl in 3 days"],
        "d": 1
    },
    {
        "q": "Which Taylor Swift single led the top 10 sweep on the Billboard Hot 100 in November 2022, spending eight weeks at #1?",
        "correct": "Anti-Hero",
        "wrong": ["Lavender Haze", "Karma", "Bejeweled"],
        "d": 1
    },
    {
        "q": "What lyric does Taylor Swift sing in the chorus of 'Anti-Hero' describing herself as the issue?",
        "correct": "It's me, hi, I'm the problem, it's me",
        "wrong": ["I'm the monster on the hill", "Sometimes I feel like everybody is a sexy baby", "Did you hear my covert narcissism"],
        "d": 1
    },
    {
        "q": "Which Taylor Swift song from her 2019 album 'Lover' had a resurgence on TikTok and the Eras Tour, finally reaching #1 in October 2023?",
        "correct": "Cruel Summer",
        "wrong": ["Paper Rings", "The Archer", "I Think He Knows"],
        "d": 1
    },
    {
        "q": "Which Morgan Wallen song spent 16 non-consecutive weeks at #1 on the Billboard Hot 100 in 2023, the longest run ever for a solo song?",
        "correct": "Last Night",
        "wrong": ["You Proof", "Thought You Should Know", "Wasted on You"],
        "d": 1
    },
    {
        "q": "Morgan Wallen's 2023 album 'One Thing at a Time' spent how many non-consecutive weeks at #1 on the Billboard 200?",
        "correct": "19 weeks",
        "wrong": ["10 weeks", "12 weeks", "26 weeks"],
        "d": 2
    },
    {
        "q": "Which SZA ballad reached #1 on the Billboard Hot 100 in April 2023, telling a revenge fantasy about her ex?",
        "correct": "Kill Bill",
        "wrong": ["Snooze", "Nobody Gets Me", "I Hate U"],
        "d": 1
    },
    {
        "q": "Which film by Quentin Tarantino provided the direct title and thematic inspiration for SZA's 'Kill Bill'?",
        "correct": "Kill Bill",
        "wrong": ["Pulp Fiction", "Jackie Brown", "Django Unchained"],
        "d": 1
    },

    # 21-30
    {
        "q": "What 2022 SZA album spent 10 weeks at #1 on the Billboard 200, the longest run for an R&B album by a female artist since Mariah Carey?",
        "correct": "SOS",
        "wrong": ["Ctrl", "Z", "Lana"],
        "d": 2
    },
    {
        "q": "Which Lil Nas X country-trap phenomenon spent a record-shattering 19 consecutive weeks at #1 on the Billboard Hot 100 in 2019?",
        "correct": "Old Town Road",
        "wrong": ["Panini", "Rodeo", "Montero (Call Me by Your Name)"],
        "d": 1
    },
    {
        "q": "Which country music legend was featured on the definitive remix of Lil Nas X's 'Old Town Road' that catapulted it to history?",
        "correct": "Billy Ray Cyrus",
        "wrong": ["Keith Urban", "Tim McGraw", "Alan Jackson"],
        "d": 1
    },
    {
        "q": "Which 2008 Nine Inch Nails instrumental track was sampled as the banjo foundation for Lil Nas X's 'Old Town Road'?",
        "correct": "34 Ghosts IV",
        "wrong": ["Hurt", "The Hand That Feeds", "A Warm Place"],
        "d": 2
    },
    {
        "q": "What was BTS's first single to debut at #1 on the Billboard Hot 100, reaching the top in September 2020?",
        "correct": "Dynamite",
        "wrong": ["Butter", "Life Goes On", "Boy with Luv"],
        "d": 1
    },
    {
        "q": "Which BTS dance-pop track spent 10 non-consecutive weeks at #1 on the Billboard Hot 100 in the summer of 2021?",
        "correct": "Butter",
        "wrong": ["Dynamite", "Permission to Dance", "My Universe"],
        "d": 1
    },
    {
        "q": "Which BTS single became the first Korean-language song in history to debut at #1 on the Billboard Hot 100 in December 2020?",
        "correct": "Life Goes On",
        "wrong": ["Fake Love", "Idol", "On"],
        "d": 2
    },
    {
        "q": "Which Jack Harlow single sampled Fergie's 2006 hit 'Glamorous' and spent three non-consecutive weeks at #1 on the Hot 100 in 2022?",
        "correct": "First Class",
        "wrong": ["Whats Poppin", "Lovin On Me", "Nail Tech"],
        "d": 1
    },
    {
        "q": "What 2023-2024 Jack Harlow hit reached #1 on the Billboard Hot 100, sampling Cadillac Dale's 'Whatever'?",
        "correct": "Lovin On Me",
        "wrong": ["First Class", "They Don't Love It", "Denver"],
        "d": 2
    },
    {
        "q": "Which 2022 Bad Bunny album became the first all-Spanish album to top the Billboard 200 Year-End chart in history?",
        "correct": "Un Verano Sin Ti",
        "wrong": ["El Último Tour Del Mundo", "YHLQMDLG", "Nadie Sabe Lo Que Va a Pasar Mañana"],
        "d": 1
    },

    # 31-40
    {
        "q": "How many total non-consecutive weeks did Bad Bunny's 'Un Verano Sin Ti' spend at #1 on the Billboard 200 in 2022?",
        "correct": "13 weeks",
        "wrong": ["8 weeks", "16 weeks", "20 weeks"],
        "d": 2
    },
    {
        "q": "Which Miley Cyrus disco-pop empowerment anthem spent eight weeks at #1 on the Billboard Hot 100 in early 2023?",
        "correct": "Flowers",
        "wrong": ["Midnight Sky", "Jaded", "River"],
        "d": 1
    },
    {
        "q": "Which Bruno Mars hit's lyrics are directly flipped and answered in Miley Cyrus's #1 hit 'Flowers'?",
        "correct": "When I Was Your Man",
        "wrong": ["Just the Way You Are", "Grenade", "Talking to the Moon"],
        "d": 1
    },
    {
        "q": "Miley Cyrus's 'Flowers' won which prestigious award at the 66th Annual Grammy Awards in 2024?",
        "correct": "Record of the Year",
        "wrong": ["Song of the Year", "Album of the Year", "Best Dance Recording"],
        "d": 2
    },
    {
        "q": "Which Zach Bryan country-rock ballad featuring Kacey Musgraves debuted at #1 on the Billboard Hot 100 in September 2023?",
        "correct": "I Remember Everything",
        "wrong": ["Something in the Orange", "Hey Driver", "Heading South"],
        "d": 1
    },
    {
        "q": "What solo breakthrough single by Zach Bryan peaked at #10 on the Hot 100 and spent 66 weeks on the chart in 2022-2023?",
        "correct": "Something in the Orange",
        "wrong": ["From Austin", "Oklahoma Smokeshow", "Burn, Burn, Burn"],
        "d": 2
    },
    {
        "q": "Which British indie band's single 'Heat Waves' set a record for the longest climb to #1 in Hot 100 history, taking 59 weeks to reach the top in 2022?",
        "correct": "Glass Animals",
        "wrong": ["Alt-J", "Bastille", "Foals"],
        "d": 1
    },
    {
        "q": "How many total weeks did Glass Animals' 'Heat Waves' spend on the Billboard Hot 100, breaking the all-time record with 91 weeks?",
        "correct": "91 weeks",
        "wrong": ["87 weeks", "90 weeks", "102 weeks"],
        "d": 2
    },
    {
        "q": "Which 24kGoldn rap-rock crossover featuring Iann Dior topped the Billboard Hot 100 for eight non-consecutive weeks in 2020?",
        "correct": "Mood",
        "wrong": ["Valentino", "Coco", "City of Angels"],
        "d": 1
    },
    {
        "q": "Which The Kid LAROI and Justin Bieber pop-rock collaboration spent seven weeks at #1 on the Billboard Hot 100 in 2021?",
        "correct": "Stay",
        "wrong": ["Without You", "Peaches", "Ghost"],
        "d": 1
    },

    # 41-50
    {
        "q": "Which Steve Lacy DIY indie-soul track reached #1 on the Billboard Hot 100 in October 2022 after going viral on TikTok?",
        "correct": "Bad Habit",
        "wrong": ["Dark Red", "Static", "Mercury"],
        "d": 2
    },
    {
        "q": "Which pop collaboration by Sam Smith and Kim Petras topped the Billboard Hot 100 in October 2022, making Petras the first openly transgender woman to hit #1?",
        "correct": "Unholy",
        "wrong": ["Stay with Me", "Heartbreak", "I'm Not Here to Make Friends"],
        "d": 1
    },
    {
        "q": "Which Beyoncé dance track from her 2022 album 'Renaissance' hit #1 on the Billboard Hot 100, sampling Robin S.'s 'Show Me Love'?",
        "correct": "Break My Soul",
        "wrong": ["Cuff It", "Alien Superstar", "Church Girl"],
        "d": 1
    },
    {
        "q": "Which Beyoncé country track debuted at #1 on the Hot Country Songs chart and topped the Billboard Hot 100 in early 2024?",
        "correct": "Texas Hold 'Em",
        "wrong": ["16 Carriages", "II Most Wanted", "Jolene"],
        "d": 1
    },
    {
        "q": "With 'Texas Hold 'Em' hitting #1 on Hot Country Songs, Beyoncé achieved which historic chart distinction?",
        "correct": "First Black woman to top the Hot Country Songs chart",
        "wrong": ["First woman to ever top the country chart", "First artist to top country and classical charts", "Only female artist with 20 country #1s"],
        "d": 1
    },
    {
        "q": "Which Luke Combs country cover of a 1988 Tracy Chapman classic peaked at #2 on the Billboard Hot 100 in 2023?",
        "correct": "Fast Car",
        "wrong": ["Give Me One Reason", "Baby Can I Hold You", "Talkin' 'bout a Revolution"],
        "d": 1
    },
    {
        "q": "What peak position did Tracy Chapman's original 1988 version of 'Fast Car' reach on the Billboard Hot 100?",
        "correct": "#6",
        "wrong": ["#2", "#10", "#15"],
        "d": 2
    },
    {
        "q": "Which Doja Cat disco-pop hit reached #1 on the Billboard Hot 100 in May 2020, boosted by a remix featuring Nicki Minaj?",
        "correct": "Say So",
        "wrong": ["Kiss Me More", "Streets", "Need to Know"],
        "d": 1
    },
    {
        "q": "Doja Cat's 'Say So' remix featuring Nicki Minaj marked what historic milestone for both artists?",
        "correct": "The first Billboard Hot 100 #1 hit for both Doja Cat and Nicki Minaj",
        "wrong": ["The fastest song to reach Gold", "The first rap song to win a Tony Award", "The longest rap intro in chart history"],
        "d": 2
    },
    {
        "q": "What 2023 Doja Cat hip-hop track topped the Billboard Hot 100 for three weeks, sampling Dionne Warwick's 'Walk On By'?",
        "correct": "Paint the Town Red",
        "wrong": ["Demons", "Agora Hills", "Attention"],
        "d": 2
    },

    # 51-60
    {
        "q": "Which Roddy Ricch track spent 11 weeks at #1 on the Billboard Hot 100 in early 2020, famous for its squeaky vocal intro?",
        "correct": "The Box",
        "wrong": ["High Fashion", "Ballin'", "Late at Night"],
        "d": 1
    },
    {
        "q": "What debut album by Roddy Ricch spent four non-consecutive weeks at #1 on the Billboard 200 in 2020?",
        "correct": "Please Excuse Me for Being Antisocial",
        "wrong": ["Live Life Fast", "Feed Tha Streets II", "The Big Steppers"],
        "d": 2
    },
    {
        "q": "Which Megan Thee Stallion single featuring Beyoncé reached #1 on the Billboard Hot 100 in May 2020, donating proceeds to Houston charity?",
        "correct": "Savage",
        "wrong": ["WAP", "Body", "Hot Girl Summer"],
        "d": 1
    },
    {
        "q": "Which Cardi B and Megan Thee Stallion collaboration debuted at #1 on the Billboard Hot 100 in August 2020, generating 93 million first-week US streams?",
        "correct": "WAP",
        "wrong": ["Bongos", "Savage", "Up"],
        "d": 1
    },
    {
        "q": "What 1993 Frank Ski Baltimore club track was sampled in Cardi B and Megan Thee Stallion's 'WAP'?",
        "correct": "Whores in This House",
        "wrong": ["Percolator", "Doo Doo Brown", "Work Them Legs"],
        "d": 3
    },
    {
        "q": "Which DaBaby track featuring Roddy Ricch spent seven non-consecutive weeks at #1 on the Billboard Hot 100 in summer 2020?",
        "correct": "Rockstar",
        "wrong": ["Suzy", "Bop", "Vibez"],
        "d": 1
    },
    {
        "q": "Which Jawsh 685 and Jason Derulo dance track hit #1 on the Billboard Hot 100 in October 2020 after BTS joined for a remix?",
        "correct": "Savage Love (Laxed – Siren Beat)",
        "wrong": ["Take You Dancing", "Swalla", "CoCo"],
        "d": 2
    },
    {
        "q": "Which Glass Animals track was originally released in June 2020 before its record-breaking slow rise to #1?",
        "correct": "Heat Waves",
        "wrong": ["Tangerine", "Space Ghost Coast to Coast", "Youth"],
        "d": 2
    },
    {
        "q": "Which Future single featuring Drake and Tems debuted at #1 on the Billboard Hot 100 in May 2022?",
        "correct": "Wait for U",
        "wrong": ["Life Is Good", "Way 2 Sexy", "Too Sexy"],
        "d": 2
    },
    {
        "q": "Which Drake and 21 Savage collaborative album debuted at #1 on the Billboard 200 in November 2022, spawning the #1 hit 'Jimmy Cooks'?",
        "correct": "Her Loss",
        "wrong": ["Certified Lover Boy", "Honestly, Nevermind", "For All the Dogs"],
        "d": 2
    },

    # 61-70
    {
        "q": "What was the lead single from Taylor Swift's surprise 2020 folk album 'folklore' that debuted at #1 on the Hot 100 simultaneously with the album?",
        "correct": "cardigan",
        "wrong": ["exile", "the 1", "august"],
        "d": 1
    },
    {
        "q": "What record did Taylor Swift set in August 2020 with the release of 'folklore' and 'cardigan'?",
        "correct": "First artist to debut at #1 on both Billboard 200 and Hot 100 in the same week",
        "wrong": ["First artist with 10 albums at #1", "Most streamed album in 10 minutes", "First female artist with two albums in the top 2"],
        "d": 2
    },
    {
        "q": "Which Taylor Swift song from 'evermore' also debuted at #1 on the Billboard Hot 100 in December 2020 alongside the album at #1?",
        "correct": "willow",
        "wrong": ["champagne problems", "gold rush", "no body, no crime"],
        "d": 2
    },
    {
        "q": "In April 2024, Taylor Swift surpassed her own record by monopolizing how many top positions on the Billboard Hot 100 with 'The Tortured Poets Department'?",
        "correct": "All top 14 positions simultaneously",
        "wrong": ["Top 10 positions", "Top 12 positions", "Top 16 positions"],
        "d": 2
    },
    {
        "q": "Which lead single from 'The Tortured Poets Department' featuring Post Malone debuted at #1 on the Billboard Hot 100 in May 2024?",
        "correct": "Fortnight",
        "wrong": ["The Tortured Poets Department", "Down Bad", "So Long, London"],
        "d": 1
    },
    {
        "q": "Which 10-minute Taylor Swift song became the longest song in history to reach #1 on the Billboard Hot 100 in November 2021?",
        "correct": "All Too Well (10 Minute Version)",
        "wrong": ["Dear John (Taylor's Version)", "Last Kiss (Taylor's Version)", "Enchanted (Taylor's Version)"],
        "d": 1
    },
    {
        "q": "Whose 1972 record for the longest song to reach #1 on the Hot 100 did Taylor Swift's 'All Too Well (10 Minute Version)' break?",
        "correct": "Don McLean ('American Pie')",
        "wrong": ["The Beatles ('Hey Jude')", "Meat Loaf ('I'd Do Anything for Love')", "Guns N' Roses ('November Rain')"],
        "d": 2
    },
    {
        "q": "Which Kendrick Lamar diss track aimed at Drake debuted at #1 on the Billboard Hot 100 in May 2024, repeating 'They not like us'?",
        "correct": "Not Like Us",
        "wrong": ["Euphoria", "Meet the Grahams", "Like That"],
        "d": 1
    },
    {
        "q": "Which Future and Metro Boomin track featuring Kendrick Lamar reached #1 on the Billboard Hot 100 in April 2024, sparking the rap feud?",
        "correct": "Like That",
        "wrong": ["Type Shit", "Young Metro", "Cinderella"],
        "d": 1
    },
    {
        "q": "Which Sabrina Carpenter pop anthem reached #1 on the Billboard Hot 100 in June 2024, singing 'Please, please, please, don't prove 'em right'?",
        "correct": "Please Please Please",
        "wrong": ["Espresso", "Feather", "Nonsense"],
        "d": 1
    },

    # 71-80
    {
        "q": "What peak position did Sabrina Carpenter's breezy summer pop hit 'Espresso' reach on the Billboard Hot 100 in 2024?",
        "correct": "#3",
        "wrong": ["#1", "#5", "#8"],
        "d": 2
    },
    {
        "q": "Which Post Malone and Morgan Wallen country-pop collaboration debuted at #1 on the Billboard Hot 100 in May 2024?",
        "correct": "I Had Some Help",
        "wrong": ["Pour Me a Drink", "Guy for That", "Broadway Girls"],
        "d": 1
    },
    {
        "q": "Which country singer reached #1 on the Billboard Hot 100 with 'A Bar Song (Tipsy)' in 2024, interpolating J-Kwon's 2004 club hit 'Tipsy'?",
        "correct": "Shaboozey",
        "wrong": ["Kane Brown", "Jelly Roll", "Bailey Zimmerman"],
        "d": 1
    },
    {
        "q": "With Shaboozey and Beyoncé reaching #1 in 2024, what milestone occurred on the Hot Country Songs chart?",
        "correct": "Two Black artists topped the Hot Country Songs chart back-to-back for the first time in history",
        "wrong": ["Country music replaced hip-hop on top of all 50 charts", "Both songs were banned from Nashville radio", "Both songs were recorded in Jamaica"],
        "d": 2
    },
    {
        "q": "Which Tommy Richman alternative R&B single reached #2 on the Billboard Hot 100 in May 2024 after going viral on TikTok with 'Million Dollar Baby'?",
        "correct": "Million Dollar Baby",
        "wrong": ["Devil Is a Lie", "Whitney", "Soul Collector"],
        "d": 2
    },
    {
        "q": "Which Billie Eilish track from the 2023 movie 'Barbie' reached #14 on the Hot 100 and won both the Oscar and Grammy for Song of the Year?",
        "correct": "What Was I Made For?",
        "wrong": ["Dance the Night", "Barbie World", "I'm Just Ken"],
        "d": 1
    },
    {
        "q": "Which Dua Lipa song from the 'Barbie' soundtrack peaked at #6 on the Billboard Hot 100 in 2023?",
        "correct": "Dance the Night",
        "wrong": ["Houdini", "Training Season", "Illusion"],
        "d": 2
    },
    {
        "q": "Which Nicki Minaj and Ice Spice collaboration from 'Barbie' peaked at #7 on the Billboard Hot 100 in 2023, sampling Aqua's 1997 'Barbie Girl'?",
        "correct": "Barbie World",
        "wrong": ["Princess Diana", "Munch (Feelin' U)", "Karma"],
        "d": 1
    },
    {
        "q": "Which Ice Spice track with PinkPantheress reached #3 on the Billboard Hot 100 in early 2023, featuring UK garage beats?",
        "correct": "Boy's a Liar Pt. 2",
        "wrong": ["In Ha Mood", "Deli", "Munch (Feelin' U)"],
        "d": 2
    },
    {
        "q": "Which Noah Kahan folk-pop anthem peaked at #9 on the Billboard Hot 100 in 2024, leading his breakthrough album of the same name?",
        "correct": "Stick Season",
        "wrong": ["Dial Drunk", "Northern Attitude", "Call Your Mom"],
        "d": 2
    },

    # 81-90
    {
        "q": "Which Benson Boone emotional pop-rock ballad peaked at #2 on the Billboard Hot 100 in spring 2024, singing 'I need you to hold on to me'?",
        "correct": "Beautiful Things",
        "wrong": ["Ghost Town", "In the Stars", "Slow It Down"],
        "d": 1
    },
    {
        "q": "Which Hozier single gave him his very first Billboard Hot 100 #1 hit in April 2024, a full decade after 'Take Me to Church'?",
        "correct": "Too Sweet",
        "wrong": ["Work Song", "Francesca", "Eat Your Young"],
        "d": 1
    },
    {
        "q": "In Hozier's #1 hit 'Too Sweet', how does the singer prefer to take his coffee?",
        "correct": "Black and his whiskey neat",
        "wrong": ["Sweet with two lumps of sugar", "With cream and cinnamon", "Cold brew with vanilla"],
        "d": 2
    },
    {
        "q": "Which Chappell Roan breakout pop anthem reached the Billboard Hot 100 top 10 in summer 2024, spelling out the title phrase?",
        "correct": "HOT TO GO!",
        "wrong": ["Good Luck, Babe!", "Pink Pony Club", "Red Wine Supernova"],
        "d": 1
    },
    {
        "q": "What Chappell Roan synth-pop single peaked at #4 on the Billboard Hot 100 in August 2024, singing 'You'd have to stop the world just to stop the feeling'?",
        "correct": "Good Luck, Babe!",
        "wrong": ["Casual", "HOT TO GO!", "Femininomenon"],
        "d": 1
    },
    {
        "q": "Which producer collaborated extensively with both Olivia Rodrigo on 'SOUR'/'GUTS' and Chappell Roan on 'The Rise and Fall of a Midwest Princess'?",
        "correct": "Dan Nigro",
        "wrong": ["Jack Antonoff", "Louis Bell", "Ian Kirkpatrick"],
        "d": 2
    },
    {
        "q": "Which Charli XCX album topped UK charts and reached #3 on the Billboard 200 in summer 2024, sparking the cultural 'Brat summer' phenomenon?",
        "correct": "Brat",
        "wrong": ["Crash", "Charli", "how i'm feeling now"],
        "d": 1
    },
    {
        "q": "Which Charli XCX track from 'Brat' was remixed featuring Lorde to wide critical acclaim, addressing female friendship and rivalry?",
        "correct": "Girl, so confusing",
        "wrong": ["360", "Apple", "Von Dutch"],
        "d": 2
    },
    {
        "q": "Which Billie Eilish track from her 2024 album 'Hit Me Hard and Soft' peaked at #2 on the Billboard Hot 100, singing 'Open up the door, can you open up the door?'?",
        "correct": "Birds of a Feather",
        "wrong": ["Lunch", "Chihiro", "Wildflower"],
        "d": 1
    },
    {
        "q": "What was the highest Billboard 200 peak position for Billie Eilish's third studio album 'Hit Me Hard and Soft' in 2024?",
        "correct": "#2",
        "wrong": ["#1", "#3", "#5"],
        "d": 2
    },

    # 91-100
    {
        "q": "Which Oliver Anthony folk-country track debuted at #1 on the Billboard Hot 100 in August 2023, making him the first artist ever to debut at #1 without any prior chart history?",
        "correct": "Rich Men North of Richmond",
        "wrong": ["Aint Gotta Dollar", "I Want to Go Home", "Doggonit"],
        "d": 2
    },
    {
        "q": "Which Jason Aldean single reached #1 on the Billboard Hot 100 in August 2023, sparked by national media controversy over its music video?",
        "correct": "Try That in a Small Town",
        "wrong": ["Dirt Road Anthem", "Big Green Tractor", "Burnin' It Down"],
        "d": 2
    },
    {
        "q": "Which Jung Kook solo single featuring Latto debuted at #1 on the Billboard Hot 100 in July 2023, making him the second BTS member with a solo #1?",
        "correct": "Seven",
        "wrong": ["3D", "Standing Next to You", "Left and Right"],
        "d": 1
    },
    {
        "q": "Who was the first BTS member to score a solo Billboard Hot 100 #1 hit with 'Like Crazy' in April 2023?",
        "correct": "Jimin",
        "wrong": ["Jung Kook", "V", "Suga"],
        "d": 2
    },
    {
        "q": "Which Drake and J. Cole collaboration reached #1 on the Billboard Hot 100 in October 2023 from 'For All the Dogs'?",
        "correct": "First Person Shooter",
        "wrong": ["Slime You Out", "IDGAF", "Rich Baby Daddy"],
        "d": 2
    },
    {
        "q": "With 'First Person Shooter' hitting #1 in 2023, Drake tied which artist for the fourth-most Billboard Hot 100 #1 hits with 13?",
        "correct": "Michael Jackson",
        "wrong": ["Madonna", "Stevie Wonder", "Elton John"],
        "d": 2
    },
    {
        "q": "Which Taylor Swift and Ice Spice remix reached #2 on the Billboard Hot 100 in June 2023?",
        "correct": "Karma",
        "wrong": ["Snow on the Beach", "Anti-Hero", "Lavender Haze"],
        "d": 2
    },
    {
        "q": "Which Lady Gaga and Bruno Mars pop-soul duet debuted at #3 on the Billboard Hot 100 in August 2024?",
        "correct": "Die with a Smile",
        "wrong": ["Hold My Hand", "Rain on Me", "Sour Candy"],
        "d": 1
    },
    {
        "q": "Which Lady Gaga and Ariana Grande dance anthem debuted at #1 on the Billboard Hot 100 in June 2020, winning the Grammy for Best Pop Duo/Group Performance?",
        "correct": "Rain on Me",
        "wrong": ["Stupid Love", "Sour Candy", "911"],
        "d": 1
    },
    {
        "q": "Which Travis Scott track featuring Playboi Carti reached #3 on the Billboard Hot 100 in August 2023 from his #1 album 'Utopia'?",
        "correct": "Fe!n",
        "wrong": ["Meltdown", "K-pop", "I Know ?"],
        "d": 2
    }
]

if __name__ == "__main__":
    formatted = assemble_batch(QUESTIONS, 8)
    save_batch(formatted, 8)
