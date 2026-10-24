import sys
import os
sys.path.append(os.path.dirname(__file__))
from utils import assemble_batch, save_batch

QUESTIONS = [
    # 1-10
    {
        "q": "Which Adele album spent 24 non-consecutive weeks at #1 on the Billboard 200 and was the best-selling album in the US for both 2011 and 2012?",
        "correct": "21",
        "wrong": ["19", "25", "30"],
        "d": 1
    },
    {
        "q": "What was Adele's first Billboard Hot 100 #1 single, spending seven weeks at the summit in 2011?",
        "correct": "Rolling in the Deep",
        "wrong": ["Someone Like You", "Set Fire to the Rain", "Chasing Pavements"],
        "d": 1
    },
    {
        "q": "Which Adele ballad became the first single to sell over one million digital downloads in a single week in the US in late 2015?",
        "correct": "Hello",
        "wrong": ["Rolling in the Deep", "Someone Like You", "When We Were Young"],
        "d": 1
    },
    {
        "q": "Adele's 2015 album '25' shattered Nielsen SoundScan records by selling how many copies in its debut week in the US?",
        "correct": "3.38 million copies",
        "wrong": ["2.41 million copies", "1.76 million copies", "4.12 million copies"],
        "d": 2
    },
    {
        "q": "Which Katy Perry album tied Michael Jackson's 'Bad' by generating five #1 singles on the Billboard Hot 100?",
        "correct": "Teenage Dream",
        "wrong": ["One of the Boys", "Prism", "Witness"],
        "d": 1
    },
    {
        "q": "Which was the fifth and final single from Katy Perry's 'Teenage Dream' to hit #1, tying the Michael Jackson record in August 2011?",
        "correct": "Last Friday Night (T.G.I.F.)",
        "wrong": ["E.T.", "Firework", "California Gurls"],
        "d": 2
    },
    {
        "q": "Which rap legend was featured on Katy Perry's #1 remix of 'California Gurls' in summer 2010?",
        "correct": "Snoop Dogg",
        "wrong": ["Kanye West", "Juicy J", "Ludacris"],
        "d": 1
    },
    {
        "q": "Which Katy Perry hit featuring Juicy J spent four weeks at #1 on the Billboard Hot 100 in early 2014, blending trap beats with pop?",
        "correct": "Dark Horse",
        "wrong": ["Roar", "Part of Me", "Wide Awake"],
        "d": 1
    },
    {
        "q": "What was Taylor Swift's first official #1 single on the Billboard Hot 100, reaching the top in September 2012?",
        "correct": "We Are Never Ever Getting Back Together",
        "wrong": ["Love Story", "You Belong with Me", "Shake It Off"],
        "d": 1
    },
    {
        "q": "Which Taylor Swift album transitioned her fully into pop in 2014, debuting with 1.287 million copies sold and yielding three #1 singles?",
        "correct": "1989",
        "wrong": ["Red", "Reputation", "Lover"],
        "d": 1
    },

    # 11-20
    {
        "q": "What song replaced Taylor Swift's 'Shake It Off' at #1 on the Billboard Hot 100 in November 2014, making her the first woman to replace herself at #1?",
        "correct": "Blank Space",
        "wrong": ["Bad Blood", "Style", "Wildest Dreams"],
        "d": 1
    },
    {
        "q": "Which Kendrick Lamar-assisted remix gave Taylor Swift her third Billboard Hot 100 #1 hit from '1989' in 2015?",
        "correct": "Bad Blood",
        "wrong": ["Style", "Out of the Woods", "Look What You Made Me Do"],
        "d": 1
    },
    {
        "q": "Which Right Said Fred 1991 hit 'I'm Too Sexy' was officially credited as interpolated in Taylor Swift's 2017 #1 hit 'Look What You Made Me Do'?",
        "correct": "I'm Too Sexy",
        "wrong": ["Deeply Dippy", "Don't Talk Just Kiss", "Stick It Out"],
        "d": 2
    },
    {
        "q": "What was Drake's first Billboard Hot 100 #1 single as a lead artist, spending 10 weeks at the summit in 2016?",
        "correct": "One Dance",
        "wrong": ["Hotline Bling", "Best I Ever Had", "God's Plan"],
        "d": 1
    },
    {
        "q": "Which Nigerian Afrobeats superstar and British singer Kyla were featured on Drake's smash 'One Dance'?",
        "correct": "Wizkid",
        "wrong": ["Burna Boy", "Davido", "Tiwa Savage"],
        "d": 2
    },
    {
        "q": "Which Drake track debuted at #1 on the Billboard Hot 100 and spent 11 weeks at the top in 2018, famous for giving away nearly $1 million in its music video?",
        "correct": "God's Plan",
        "wrong": ["Nice for What", "In My Feelings", "Nonstop"],
        "d": 1
    },
    {
        "q": "Which Drake single spent 10 weeks at #1 in summer 2018, fueled by comedian Shiggy's viral 'In My Feelings' dance challenge?",
        "correct": "In My Feelings",
        "wrong": ["Nice for What", "God's Plan", "I'm Upset"],
        "d": 1
    },
    {
        "q": "Which Lauryn Hill classic was prominently sampled in Drake's 2018 #1 hit 'Nice for What'?",
        "correct": "Ex-Factor",
        "wrong": ["Doo Wop (That Thing)", "To Zion", "Lost Ones"],
        "d": 2
    },
    {
        "q": "What was Bruno Mars' debut solo single that reached #1 on the Billboard Hot 100 for four weeks in 2010?",
        "correct": "Just the Way You Are",
        "wrong": ["Grenade", "The Lazy Song", "Marry You"],
        "d": 1
    },
    {
        "q": "Which Mark Ronson funk collaboration featuring Bruno Mars spent 14 consecutive weeks at #1 on the Hot 100 in 2015?",
        "correct": "Uptown Funk",
        "wrong": ["Locked Out of Heaven", "Treasure", "24K Magic"],
        "d": 1
    },

    # 21-30
    {
        "q": "Which 1979 funk group's song 'Oops Up Side Your Head' was added to the songwriting credits of 'Uptown Funk' following a settlement?",
        "correct": "The Gap Band",
        "wrong": ["The Bar-Kays", "Kool & the Gang", "Cameo"],
        "d": 2
    },
    {
        "q": "Which Bruno Mars retro-R&B track from '24K Magic' spent five weeks at #1 on the Billboard Hot 100 in spring 2017?",
        "correct": "That's What I Like",
        "wrong": ["Versace on the Floor", "Finesse", "24K Magic"],
        "d": 2
    },
    {
        "q": "Which Rihanna dance-pop single produced by Calvin Harris spent 10 non-consecutive weeks at #1 on the Hot 100 in late 2011?",
        "correct": "We Found Love",
        "wrong": ["Where Have You Been", "Diamonds", "Only Girl (In the World)"],
        "d": 1
    },
    {
        "q": "Which Sia-penned ballad gave Rihanna her 12th Billboard Hot 100 #1 single in December 2012, shining 'bright like a diamond'?",
        "correct": "Diamonds",
        "wrong": ["Stay", "Pour It Up", "Love on the Brain"],
        "d": 1
    },
    {
        "q": "Which dancehall collaboration with Drake gave Rihanna her 14th Billboard Hot 100 #1 hit in 2016, spending nine weeks at the top?",
        "correct": "Work",
        "wrong": ["Needed Me", "What's My Name?", "Take Care"],
        "d": 1
    },
    {
        "q": "With 14 Billboard Hot 100 #1 hits, Rihanna ranks behind only which two musical acts in all-time chart history?",
        "correct": "The Beatles and Mariah Carey",
        "wrong": ["Elvis Presley and Michael Jackson", "Madonna and Stevie Wonder", "The Beatles and Elton John"],
        "d": 2
    },
    {
        "q": "What was The Weeknd's first Billboard Hot 100 #1 single, which topped the chart in August 2015 after being featured in an Apple Music ad?",
        "correct": "Can't Feel My Face",
        "wrong": ["The Hills", "Earned It", "Starboy"],
        "d": 1
    },
    {
        "q": "Which dark, moody track replaced 'Can't Feel My Face' at #1 on the Billboard Hot 100 in October 2015, giving The Weeknd consecutive chart-toppers?",
        "correct": "The Hills",
        "wrong": ["Often", "In the Night", "Starboy"],
        "d": 2
    },
    {
        "q": "Which French electronic duo collaborated with The Weeknd on his 2016 Billboard Hot 100 #1 title track 'Starboy'?",
        "correct": "Daft Punk",
        "wrong": ["Justice", "Phoenix", "Air"],
        "d": 1
    },
    {
        "q": "What Justin Bieber single debuted at #1 on the Billboard Hot 100 in September 2015, his very first chart-topper?",
        "correct": "What Do You Mean?",
        "wrong": ["Sorry", "Love Yourself", "Baby"],
        "d": 1
    },

    # 31-40
    {
        "q": "Which Ed Sheeran-penned acoustic pop track became Justin Bieber's third consecutive #1 single from 'Purpose' in early 2016?",
        "correct": "Love Yourself",
        "wrong": ["Sorry", "Company", "I'll Show You"],
        "d": 1
    },
    {
        "q": "Which Justin Bieber song was crowned the Billboard Year-End #1 single of 2016 on the Hot 100?",
        "correct": "Love Yourself",
        "wrong": ["Sorry", "What Do You Mean?", "Cold Water"],
        "d": 2
    },
    {
        "q": "Which Ed Sheeran tropical-pop hit debuted at #1 on the Billboard Hot 100 in January 2017 and spent 33 weeks in the top 10?",
        "correct": "Shape of You",
        "wrong": ["Castle on the Hill", "Perfect", "Thinking Out Loud"],
        "d": 1
    },
    {
        "q": "Which 1999 TLC hit was credited on Ed Sheeran's 'Shape of You' due to melodic similarities in the rhythmic verse?",
        "correct": "No Scrubs",
        "wrong": ["Waterfalls", "Creep", "Unpretty"],
        "d": 2
    },
    {
        "q": "Which romantic ballad gave Ed Sheeran his second Billboard Hot 100 #1 hit in late 2017, later remixed with Beyoncé?",
        "correct": "Perfect",
        "wrong": ["Thinking Out Loud", "Photograph", "Dive"],
        "d": 1
    },
    {
        "q": "What Lady Gaga and Bradley Cooper duet from 'A Star Is Born' won the Oscar for Best Original Song and reached #1 on the Hot 100 in March 2019?",
        "correct": "Shallow",
        "wrong": ["Always Remember Us This Way", "I'll Never Love Again", "Look What I Found"],
        "d": 1
    },
    {
        "q": "What was Post Malone's first Billboard Hot 100 #1 single, spending eight weeks at the top in late 2017 featuring 21 Savage?",
        "correct": "Rockstar",
        "wrong": ["Congratulations", "Psycho", "White Iverson"],
        "d": 1
    },
    {
        "q": "Which Post Malone and Swae Lee track from 'Spider-Man: Into the Spider-Verse' reached #1 on the Billboard Hot 100 in early 2019?",
        "correct": "Sunflower",
        "wrong": ["Wow.", "Goodbyes", "Circles"],
        "d": 1
    },
    {
        "q": "What record did Post Malone and Swae Lee's 'Sunflower' set for the RIAA in 2022?",
        "correct": "First single certified Double Diamond (20x Platinum) in RIAA history",
        "wrong": ["Fastest single to reach Gold status", "Most weeks at #1 on physical vinyl", "Most downloaded ringtone"],
        "d": 2
    },
    {
        "q": "Which Post Malone pop-rock ballad spent a record 39 weeks in the Billboard Hot 100 top 10 in 2019-2020?",
        "correct": "Circles",
        "wrong": ["Sunflower", "Better Now", "Take What You Want"],
        "d": 2
    },

    # 41-50
    {
        "q": "What Cardi B breakout single spent three weeks at #1 on the Billboard Hot 100 in autumn 2017, making her the first solo female rapper to top the chart since 1998?",
        "correct": "Bodak Yellow",
        "wrong": ["Bartier Cardi", "I Like It", "Money"],
        "d": 1
    },
    {
        "q": "Which Florida rapper's song 'No Flockin' served as the flow and stylistic inspiration for Cardi B's 'Bodak Yellow'?",
        "correct": "Kodak Black",
        "wrong": ["Denzel Curry", "XXXTentacion", "Ski Mask the Slump God"],
        "d": 2
    },
    {
        "q": "Which Cardi B bilingual smash featuring Bad Bunny and J Balvin topped the Billboard Hot 100 for one week in July 2018?",
        "correct": "I Like It",
        "wrong": ["Mia", "Taki Taki", "Finesse"],
        "d": 1
    },
    {
        "q": "What 1967 boogaloo song by Pete Rodriguez was sampled as the foundation for Cardi B's 'I Like It'?",
        "correct": "I Like It Like That",
        "wrong": ["Oye Como Va", "Bang Bang", "El Watusi"],
        "d": 2
    },
    {
        "q": "Which Ariana Grande single debuted at #1 on the Billboard Hot 100 in late 2018, name-dropping several of her famous ex-boyfriends?",
        "correct": "Thank U, Next",
        "wrong": ["7 Rings", "Break Up with Your Girlfriend, I'm Bored", "No Tears Left to Cry"],
        "d": 1
    },
    {
        "q": "Ariana Grande's '7 Rings' interpolates which classic song from 'The Sound of Music'?",
        "correct": "My Favorite Things",
        "wrong": ["Do-Re-Mi", "Edelweiss", "Climb Ev'ry Mountain"],
        "d": 1
    },
    {
        "q": "In February 2019, Ariana Grande became the first solo artist to monopolize the top three spots on the Billboard Hot 100 since which band in 1964?",
        "correct": "The Beatles",
        "wrong": ["The Rolling Stones", "The Beach Boys", "The Supremes"],
        "d": 2
    },
    {
        "q": "Which Maroon 5 collaboration with Cardi B spent seven weeks at #1 on the Billboard Hot 100 in 2018?",
        "correct": "Girls Like You",
        "wrong": ["Sugar", "One More Night", "Payphone"],
        "d": 1
    },
    {
        "q": "How many weeks did Maroon 5's 'Girls Like You' spend in the Billboard Hot 100 top 10, tying an all-time record at 33 weeks?",
        "correct": "33 weeks",
        "wrong": ["26 weeks", "40 weeks", "19 weeks"],
        "d": 2
    },
    {
        "q": "Which Macklemore & Ryan Lewis novelty hit featuring Wanz spent six weeks at #1 on the Billboard Hot 100 in early 2013?",
        "correct": "Thrift Shop",
        "wrong": ["Can't Hold Us", "Same Love", "White Walls"],
        "d": 1
    },

    # 51-60
    {
        "q": "What was the Billboard Year-End #1 single of 2013 on the Hot 100?",
        "correct": "Thrift Shop by Macklemore & Ryan Lewis",
        "wrong": ["Blurred Lines by Robin Thicke", "Radioactive by Imagine Dragons", "Royals by Lorde"],
        "d": 2
    },
    {
        "q": "What was Macklemore & Ryan Lewis's second consecutive #1 single on the Billboard Hot 100 in 2013, featuring Ray Dalton?",
        "correct": "Can't Hold Us",
        "wrong": ["Same Love", "Thrift Shop", "Downtown"],
        "d": 1
    },
    {
        "q": "Which 16-year-old New Zealand singer topped the Billboard Hot 100 for nine weeks in late 2013 with her minimalist anthem 'Royals'?",
        "correct": "Lorde",
        "wrong": ["Billie Eilish", "Alessia Cara", "Birdy"],
        "d": 1
    },
    {
        "q": "Which Gotye indie-pop breakup song featuring Kimbra spent eight weeks at #1 and was the Billboard Year-End #1 single of 2012?",
        "correct": "Somebody That I Used to Know",
        "wrong": ["Eyes Wide Open", "Heart's a Mess", "Smoke and Mirrors"],
        "d": 1
    },
    {
        "q": "Which Luis Fonsi and Daddy Yankee song, remixed with Justin Bieber, tied the all-time record by spending 16 weeks at #1 on the Hot 100 in 2017?",
        "correct": "Despacito",
        "wrong": ["Échame la Culpa", "Bailando", "Dura"],
        "d": 1
    },
    {
        "q": "Whose 1995-1996 record of 16 weeks at #1 did 'Despacito' tie in August 2017?",
        "correct": "Mariah Carey and Boyz II Men ('One Sweet Day')",
        "wrong": ["Whitney Houston ('I Will Always Love You')", "Elton John ('Candle in the Wind')", "The Black Eyed Peas ('I Gotta Feeling')"],
        "d": 2
    },
    {
        "q": "Which Camila Cabello Latin-pop single featuring Young Thug spent one week at #1 on the Billboard Hot 100 in January 2018?",
        "correct": "Havana",
        "wrong": ["Never Be the Same", "Señorita", "Crying in the Club"],
        "d": 1
    },
    {
        "q": "Which Shawn Mendes and Camila Cabello duet reached #1 on the Billboard Hot 100 in August 2019?",
        "correct": "Señorita",
        "wrong": ["I Know What You Did Last Summer", "Stitches", "Treat You Better"],
        "d": 1
    },
    {
        "q": "Which The Chainsmokers EDM-pop hit featuring Halsey spent 12 consecutive weeks at #1 on the Billboard Hot 100 in late 2016?",
        "correct": "Closer",
        "wrong": ["Don't Let Me Down", "Paris", "Something Just Like This"],
        "d": 1
    },
    {
        "q": "Which Sia dancehall-pop hit featuring Sean Paul topped the Billboard Hot 100 for four weeks in 2016, giving Sia her first Hot 100 #1?",
        "correct": "Cheap Thrills",
        "wrong": ["Chandelier", "Elastic Heart", "The Greatest"],
        "d": 2
    },

    # 61-70
    {
        "q": "Which Meghan Trainor doo-wop pop hit spent eight weeks at #1 on the Billboard Hot 100 in autumn 2014, celebrating body positivity?",
        "correct": "All About That Bass",
        "wrong": ["Lips Are Movin", "Like I'm Gonna Lose You", "Dear Future Husband"],
        "d": 1
    },
    {
        "q": "Which electro-hop duo scored back-to-back #1 hits in 2011 with 'Party Rock Anthem' and 'Sexy and I Know It'?",
        "correct": "LMFAO",
        "wrong": ["Far East Movement", "3OH!3", "The Cataracs"],
        "d": 1
    },
    {
        "q": "Which Carly Rae Jepsen infectious pop hit spent nine weeks at #1 on the Billboard Hot 100 in summer 2012?",
        "correct": "Call Me Maybe",
        "wrong": ["Good Time", "I Really Like You", "Run Away with Me"],
        "d": 1
    },
    {
        "q": "Which pop-rock band fronted by Nate Ruess reached #1 on the Billboard Hot 100 in 2012 with 'We Are Young' featuring Janelle Monáe?",
        "correct": "Fun.",
        "wrong": ["The Format", "Bleachers", "Walk the Moon"],
        "d": 1
    },
    {
        "q": "What 2013 viral dance-craze instrumental by Baauer became the first song to debut at #1 on the Hot 100 purely due to YouTube video views?",
        "correct": "Harlem Shake",
        "wrong": ["Gangnam Style", "Watch Me (Whip/Nae Nae)", "The Fox (What Does the Fox Say?)"],
        "d": 2
    },
    {
        "q": "What Robin Thicke song featuring T.I. and Pharrell spent 12 weeks at #1 on the Hot 100 in 2013 and later lost a landmark copyright trial?",
        "correct": "Blurred Lines",
        "wrong": ["Lost Without U", "Give It 2 U", "Sex Therapy"],
        "d": 1
    },
    {
        "q": "Which 1977 Marvin Gaye song was Robin Thicke and Pharrell found to have infringed upon in the 'Blurred Lines' copyright case?",
        "correct": "Got to Give It Up",
        "wrong": ["Sexual Healing", "Let's Get It On", "Inner City Blues"],
        "d": 2
    },
    {
        "q": "Which Pharrell Williams song from the 'Despicable Me 2' soundtrack spent 10 weeks at #1 on the Hot 100 and was the top song of 2014?",
        "correct": "Happy",
        "wrong": ["Get Lucky", "Freedom", "Come Get It Bae"],
        "d": 1
    },
    {
        "q": "Which Australian rapper's hit 'Fancy' featuring Charli XCX topped the Billboard Hot 100 for seven weeks in summer 2014?",
        "correct": "Iggy Azalea",
        "wrong": ["Tones and I", "Ruby Rose", "The Kid LAROI"],
        "d": 1
    },
    {
        "q": "Which Pitbull party track featuring Kesha topped the Billboard Hot 100 for three weeks in January 2014?",
        "correct": "Timber",
        "wrong": ["Give Me Everything", "Feel This Moment", "Fireball"],
        "d": 1
    },

    # 71-80
    {
        "q": "Which Pitbull club anthem featuring Ne-Yo, Afrojack, and Nayer gave Pitbull his first Billboard Hot 100 #1 in July 2011?",
        "correct": "Give Me Everything",
        "wrong": ["I Know You Want Me (Calle Ocho)", "Hotel Room Service", "Time of Our Lives"],
        "d": 2
    },
    {
        "q": "Which Imagine Dragons alt-rock song spent a тогда-record 87 weeks on the Billboard Hot 100 from 2012 to 2014, peaking at #3?",
        "correct": "Radioactive",
        "wrong": ["Demons", "Believer", "Thunder"],
        "d": 1
    },
    {
        "q": "Which OneRepublic pop-rock ballad peaked at #2 on the Billboard Hot 100 for four weeks in early 2014?",
        "correct": "Counting Stars",
        "wrong": ["Good Life", "Secrets", "Love Runs Out"],
        "d": 1
    },
    {
        "q": "Which Hozier blues-gospel indie rock single peaked at #2 on the Billboard Hot 100 in late 2014, criticizing church corruption?",
        "correct": "Take Me to Church",
        "wrong": ["Someone New", "Work Song", "Cherry Wine"],
        "d": 1
    },
    {
        "q": "Which OMI reggae-pop single topped the Billboard Hot 100 for six weeks in summer 2015, remixed by German DJ Felix Jaehn?",
        "correct": "Cheerleader",
        "wrong": ["Hula Hoop", "Drop in the Ocean", "Me 4 U"],
        "d": 2
    },
    {
        "q": "Which Walk the Moon indie-pop anthem peaked at #4 on the Billboard Hot 100 in 2015, repeating 'Shut up and dance with me'?",
        "correct": "Shut Up and Dance",
        "wrong": ["Anna Sun", "One Foot", "Kamikaze"],
        "d": 1
    },
    {
        "q": "Which Wiz Khalifa ballad featuring Charlie Puth spent 12 non-consecutive weeks at #1 on the Hot 100 in 2015 as a tribute to Paul Walker?",
        "correct": "See You Again",
        "wrong": ["Black and Yellow", "Young, Wild & Free", "Roll Up"],
        "d": 1
    },
    {
        "q": "In which blockbuster film was Wiz Khalifa and Charlie Puth's emotional tribute 'See You Again' featured?",
        "correct": "Furious 7",
        "wrong": ["Fast & Furious 6", "The Fate of the Furious", "Transformers: Age of Extinction"],
        "d": 1
    },
    {
        "q": "What was Wiz Khalifa's first #1 hit on the Billboard Hot 100, which reached the summit in February 2011 honoring Pittsburgh sports colors?",
        "correct": "Black and Yellow",
        "wrong": ["Roll Up", "No Sleep", "Work Hard, Play Hard"],
        "d": 2
    },
    {
        "q": "Which Rae Sremmurd trap single featuring Gucci Mane hit #1 on the Hot 100 in late 2016, fueled by the viral 'Mannequin Challenge'?",
        "correct": "Black Beatles",
        "wrong": ["No Type", "No Flex Zone", "Swang"],
        "d": 1
    },

    # 81-90
    {
        "q": "Which Childish Gambino track debuted at #1 on the Billboard Hot 100 in May 2018, accompanied by a shocking, socially conscious music video?",
        "correct": "This Is America",
        "wrong": ["Redbone", "Sober", "Feels Like Summer"],
        "d": 1
    },
    {
        "q": "Who directed the provocative, award-winning music video for Childish Gambino's 'This Is America'?",
        "correct": "Hiro Murai",
        "wrong": ["Dave Meyers", "Cole Bennett", "Director X"],
        "d": 2
    },
    {
        "q": "Which Travis Scott trap anthem spent one week at #1 on the Billboard Hot 100 in December 2018, featuring Drake?",
        "correct": "Sicko Mode",
        "wrong": ["Stargazing", "Antidote", "Goosebumps"],
        "d": 1
    },
    {
        "q": "Travis Scott's 2018 album 'Astroworld' spent three weeks at #1 on the Billboard 200 and was named after what closed amusement park?",
        "correct": "Six Flags AstroWorld in Houston, Texas",
        "wrong": ["AstroWorld in Arlington, Texas", "Six Flags Over Texas", "Space City Funland"],
        "d": 2
    },
    {
        "q": "Which Jonas Brothers comeback single debuted at #1 on the Billboard Hot 100 in March 2019, their first #1 single ever?",
        "correct": "Sucker",
        "wrong": ["Cool", "Only Human", "What a Man Gotta Do"],
        "d": 1
    },
    {
        "q": "Which Billie Eilish whisper-pop track reached #1 on the Billboard Hot 100 in August 2019, ending the record run of 'Old Town Road'?",
        "correct": "Bad Guy",
        "wrong": ["Bury a Friend", "Everything I Wanted", "Ocean Eyes"],
        "d": 1
    },
    {
        "q": "Billie Eilish became the first artist born in which decade to top the Billboard Hot 100 when 'Bad Guy' hit #1 in 2019?",
        "correct": "The 2000s",
        "wrong": ["The 1990s", "The 2010s", "The late 1990s"],
        "d": 2
    },
    {
        "q": "Who produced and co-wrote Billie Eilish's multi-platinum debut album 'When We All Fall Asleep, Where Do We Go?' in their bedroom studio?",
        "correct": "Finneas O'Connell",
        "wrong": ["Jack Antonoff", "Rick Rubin", "Max Martin"],
        "d": 1
    },
    {
        "q": "Which Lizzo flute-assisted empowerment anthem reached #1 on the Billboard Hot 100 for seven weeks in autumn 2019, two years after its release?",
        "correct": "Truth Hurts",
        "wrong": ["Good as Hell", "Juice", "About Damn Time"],
        "d": 1
    },
    {
        "q": "In Lizzo's #1 hit 'Truth Hurts', what percentage does a DNA test confirm that she is 'that chick'?",
        "correct": "100%",
        "wrong": ["99%", "90%", "110%"],
        "d": 1
    },

    # 91-100
    {
        "q": "Which Lewis Capaldi emotional piano ballad reached #1 on the Billboard Hot 100 in November 2019 after a slow 24-week climb?",
        "correct": "Someone You Loved",
        "wrong": ["Before You Go", "Hold Me While You Wait", "Bruises"],
        "d": 2
    },
    {
        "q": "Which Selena Gomez ballad became her first Billboard Hot 100 #1 hit in November 2019, widely believed to address Justin Bieber?",
        "correct": "Lose You to Love Me",
        "wrong": ["Look at Her Now", "Good for You", "Hands to Myself"],
        "d": 2
    },
    {
        "q": "Which South Korean group debuted on the Billboard Hot 100 top 10 with 'Fake Love' and 'Boy with Luv' before scoring their first #1?",
        "correct": "BTS",
        "wrong": ["EXO", "Blackpink", "Stray Kids"],
        "d": 1
    },
    {
        "q": "Which American pop singer was featured on BTS's 2019 Top 10 single 'Boy with Luv'?",
        "correct": "Halsey",
        "wrong": ["Nicki Minaj", "Sia", "Charli XCX"],
        "d": 2
    },
    {
        "q": "Which Kendrick Lamar album won the 2018 Pulitzer Prize for Music and spent four weeks at #1 on the Billboard 200?",
        "correct": "DAMN.",
        "wrong": ["To Pimp a Butterfly", "Good Kid, M.A.A.D City", "Mr. Morale & the Big Steppers"],
        "d": 1
    },
    {
        "q": "What was Kendrick Lamar's first Billboard Hot 100 #1 single as a solo lead artist, topping the chart in April 2017?",
        "correct": "Humble",
        "wrong": ["DNA.", "Loyalty", "King Kunta"],
        "d": 1
    },
    {
        "q": "Which Halsey solo single topped the Billboard Hot 100 for two non-consecutive weeks in early 2019, singing 'I'm the one who put you up there'?",
        "correct": "Without Me",
        "wrong": ["Bad at Love", "Now or Never", "Graveyard"],
        "d": 2
    },
    {
        "q": "Which Justin Timberlake track from the animated movie 'Trolls' debuted at #1 on the Billboard Hot 100 in May 2016?",
        "correct": "Can't Stop the Feeling!",
        "wrong": ["Suit & Tie", "Mirrors", "Filthy"],
        "d": 1
    },
    {
        "q": "Which Bruno Mars retro-funk jam peaked at #4 on the Billboard Hot 100 in late 2016 and gave its name to his third studio album?",
        "correct": "24K Magic",
        "wrong": ["Chunky", "Finesse", "Perm"],
        "d": 2
    },
    {
        "q": "Which Bruno Mars and Cardi B remix of a 90s-style New Jack Swing track peaked at #3 on the Billboard Hot 100 in 2018?",
        "correct": "Finesse",
        "wrong": ["Please Me", "24K Magic", "Blow"],
        "d": 2
    }
]

if __name__ == "__main__":
    formatted = assemble_batch(QUESTIONS, 7)
    save_batch(formatted, 7)
