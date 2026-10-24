import sys
import os
sys.path.append(os.path.dirname(__file__))
from utils import assemble_batch, save_batch

QUESTIONS = [
    # 1-10
    {
        "q": "Which Usher single spent 12 consecutive weeks at #1 on the Billboard Hot 100 in 2004, featuring Lil Jon and Ludacris?",
        "correct": "Yeah!",
        "wrong": ["Burn", "Confessions Part II", "Caught Up"],
        "d": 1
    },
    {
        "q": "Which Usher album sold over 1.09 million copies in its first week in 2004 and spent nine weeks at #1 on the Billboard 200?",
        "correct": "Confessions",
        "wrong": ["8701", "Raymond v. Raymond", "Here I Stand"],
        "d": 1
    },
    {
        "q": "Usher held the #1 spot on the Billboard Hot 100 for how many total weeks in the calendar year 2004, an all-time record for a solo artist?",
        "correct": "28 weeks",
        "wrong": ["18 weeks", "22 weeks", "34 weeks"],
        "d": 2
    },
    {
        "q": "Which OutKast double album won Album of the Year at the 2004 Grammys and topped the Billboard 200 for seven weeks?",
        "correct": "Speakerboxxx/The Love Below",
        "wrong": ["Stankonia", "Aquemini", "Idlewild"],
        "d": 1
    },
    {
        "q": "Which André 3000 track spent nine weeks at #1 on the Billboard Hot 100 in 2003-2004, advising dancers to 'shake it like a Polaroid picture'?",
        "correct": "Hey Ya!",
        "wrong": ["Roses", "Prototype", "She Lives in My Lap"],
        "d": 1
    },
    {
        "q": "Which OutKast song replaced 'Hey Ya!' at #1 on the Billboard Hot 100 in February 2004, performed by Big Boi featuring Sleepy Brown?",
        "correct": "The Way You Move",
        "wrong": ["Ms. Jackson", "So Fresh, So Clean", "Ghettomusick"],
        "d": 2
    },
    {
        "q": "What was OutKast's first Billboard Hot 100 #1 hit, reaching the summit in February 2001 with an apology to an ex-partner's mother?",
        "correct": "Ms. Jackson",
        "wrong": ["Bombs Over Baghdad", "Rosa Parks", "Elevators (Me & You)"],
        "d": 1
    },
    {
        "q": "Which Eminem song from the '8 Mile' soundtrack spent 12 weeks at #1 on the Billboard Hot 100 and won an Academy Award for Best Original Song?",
        "correct": "Lose Yourself",
        "wrong": ["Without Me", "The Real Slim Shady", "Cleanin' Out My Closet"],
        "d": 1
    },
    {
        "q": "Eminem's 2000 album 'The Marshall Mathers LP' sold how many copies in its first week in the US, setting a record for a solo artist?",
        "correct": "1.76 million copies",
        "wrong": ["950,000 copies", "1.25 million copies", "2.4 million copies"],
        "d": 2
    },
    {
        "q": "Which British singer's song 'Thank You' was sampled for the hook and rain-sound effects in Eminem's 2000 hit 'Stan'?",
        "correct": "Dido",
        "wrong": ["Imogen Heap", "Sarah McLachlan", "Beth Orton"],
        "d": 1
    },

    # 11-20
    {
        "q": "Which 50 Cent single spent nine weeks at #1 on the Billboard Hot 100 in 2003, produced by Dr. Dre and Mike Elizondo?",
        "correct": "In da Club",
        "wrong": ["21 Questions", "P.I.M.P.", "Wanksta"],
        "d": 1
    },
    {
        "q": "What was the Billboard Year-End #1 single of 2003 on the Hot 100?",
        "correct": "In da Club by 50 Cent",
        "wrong": ["Crazy in Love by Beyoncé", "Ignition (Remix) by R. Kelly", "Get Busy by Sean Paul"],
        "d": 2
    },
    {
        "q": "Which 50 Cent debut major-label album debuted at #1 on the Billboard 200 in 2003, selling 872,000 copies in its first shortened week?",
        "correct": "Get Rich or Die Tryin'",
        "wrong": ["The Massacre", "Curtis", "Guess Who's Back?"],
        "d": 1
    },
    {
        "q": "Which Beyoncé solo debut single featuring Jay-Z spent eight consecutive weeks at #1 on the Billboard Hot 100 in summer 2003?",
        "correct": "Crazy in Love",
        "wrong": ["Baby Boy", "Me, Myself and I", "Naughty Girl"],
        "d": 1
    },
    {
        "q": "Which 1970 Chi-Lites soul song provided the triumphant brass horn riff for Beyoncé's 'Crazy in Love'?",
        "correct": "Are You My Woman? (Tell Me So)",
        "wrong": ["Have You Seen Her", "Oh Girl", "Give It Away"],
        "d": 2
    },
    {
        "q": "What was Beyoncé's second consecutive solo Billboard Hot 100 #1 hit, featuring Jamaican dancehall artist Sean Paul in late 2003?",
        "correct": "Baby Boy",
        "wrong": ["Naughty Girl", "Check on It", "Déjà Vu"],
        "d": 2
    },
    {
        "q": "Which Beyoncé ballad spent 10 consecutive weeks at #1 on the Billboard Hot 100 in late 2006 and early 2007, declaring 'to the left, to the left'?",
        "correct": "Irreplaceable",
        "wrong": ["Halo", "Listen", "If I Were a Boy"],
        "d": 1
    },
    {
        "q": "Who co-wrote Beyoncé's #1 smash 'Irreplaceable' alongside Norwegian production duo Stargate?",
        "correct": "Ne-Yo",
        "wrong": ["The-Dream", "Sean Garrett", "Johntá Austin"],
        "d": 2
    },
    {
        "q": "Which Beyoncé dance-pop anthem topped the Billboard Hot 100 for four weeks in late 2008, featuring an iconic black-and-white trio music video?",
        "correct": "Single Ladies (Put a Ring on It)",
        "wrong": ["Diva", "Sweet Dreams", "Video Phone"],
        "d": 1
    },
    {
        "q": "Which Nelly party anthem topped the Billboard Hot 100 for seven weeks in summer 2002, repeating 'it's getting hot in herre'?",
        "correct": "Hot in Herre",
        "wrong": ["Dilemma", "Country Grammar", "Ride wit Me"],
        "d": 1
    },

    # 21-30
    {
        "q": "Which Nelly duet featuring Kelly Rowland replaced his own 'Hot in Herre' at #1 on the Billboard Hot 100 in August 2002?",
        "correct": "Dilemma",
        "wrong": ["Air Force Ones", "Pimp Juice", "Over and Over"],
        "d": 1
    },
    {
        "q": "Which 1982 Patti LaBelle song was sampled and interpolated in the chorus of Nelly and Kelly Rowland's 'Dilemma'?",
        "correct": "Love, Need and Want You",
        "wrong": ["If Only You Knew", "New Attitude", "On My Own"],
        "d": 3
    },
    {
        "q": "What Alicia Keys debut single spent six weeks at #1 on the Billboard Hot 100 in 2001, winning Song of the Year at the Grammys?",
        "correct": "Fallin'",
        "wrong": ["A Woman's Worth", "If I Ain't Got You", "You Don't Know My Name"],
        "d": 1
    },
    {
        "q": "Which Alicia Keys album debuted at #1 on the Billboard 200 in June 2001, selling over 6.2 million copies in the US?",
        "correct": "Songs in A Minor",
        "wrong": ["The Diary of Alicia Keys", "As I Am", "The Element of Freedom"],
        "d": 1
    },
    {
        "q": "What Alicia Keys power ballad spent five weeks at #1 on the Billboard Hot 100 in late 2007, leading her album 'As I Am'?",
        "correct": "No One",
        "wrong": ["Like You'll Never See Me Again", "Superwoman", "Teenage Love Affair"],
        "d": 1
    },
    {
        "q": "Which 2002 Kelly Clarkson debut single jumped from #52 to #1 on the Billboard Hot 100, breaking a 38-year-old Beatles record?",
        "correct": "A Moment Like This",
        "wrong": ["Miss Independent", "Since U Been Gone", "Breakaway"],
        "d": 2
    },
    {
        "q": "Which pop-rock anthem by Kelly Clarkson spent 20 weeks in the Hot 100 top 10 in 2005, co-written and produced by Max Martin and Dr. Luke?",
        "correct": "Since U Been Gone",
        "wrong": ["Behind These Hazel Eyes", "Because of You", "Walk Away"],
        "d": 1
    },
    {
        "q": "Which Gwen Stefani cheerleader-chant track became the first single in US digital history to sell one million downloads, hitting #1 in 2005?",
        "correct": "Hollaback Girl",
        "wrong": ["Rich Girl", "What You Waiting For?", "Cool"],
        "d": 1
    },
    {
        "q": "Who produced Gwen Stefani's chart-topping 2005 digital blockbuster 'Hollaback Girl'?",
        "correct": "The Neptunes (Pharrell Williams and Chad Hugo)",
        "wrong": ["Timbaland", "Dr. Luke", "will.i.am"],
        "d": 2
    },
    {
        "q": "What was Justin Timberlake's first solo #1 single on the Billboard Hot 100, spending seven weeks at the summit in 2006?",
        "correct": "SexyBack",
        "wrong": ["Cry Me a River", "Rock Your Body", "My Love"],
        "d": 1
    },

    # 31-40
    {
        "q": "Who was Justin Timberlake's primary collaborator and producer on the 2006 multi-platinum album 'FutureSex/LoveSounds'?",
        "correct": "Timbaland",
        "wrong": ["The Neptunes", "Max Martin", "Scott Storch"],
        "d": 1
    },
    {
        "q": "Which Justin Timberlake track featuring T.I. hit #1 on the Billboard Hot 100 in late 2006 with its distinctive beatboxing and synth arpeggios?",
        "correct": "My Love",
        "wrong": ["SexyBack", "What Goes Around... Comes Around", "Summer Love"],
        "d": 2
    },
    {
        "q": "Which Justin Timberlake ballad reached #1 on the Billboard Hot 100 in March 2007, accompanied by an extended dramatic short-film video starring Scarlett Johansson?",
        "correct": "What Goes Around... Comes Around",
        "wrong": ["Cry Me a River", "Not a Bad Thing", "Mirrors"],
        "d": 2
    },
    {
        "q": "What was Rihanna's first Billboard Hot 100 #1 hit, which sampled Soft Cell's 'Tainted Love' in 2006?",
        "correct": "SOS",
        "wrong": ["Pon de Replay", "Unfaithful", "Umbrella"],
        "d": 2
    },
    {
        "q": "Which Rihanna megahit featuring Jay-Z spent seven consecutive weeks at #1 on the Billboard Hot 100 in the summer of 2007?",
        "correct": "Umbrella",
        "wrong": ["Take a Bow", "Disturbia", "Don't Stop the Music"],
        "d": 1
    },
    {
        "q": "Which hip-hop/pop group set a Billboard Hot 100 record by holding the #1 spot for 26 consecutive weeks in 2009 with back-to-back hits?",
        "correct": "The Black Eyed Peas",
        "wrong": ["OutKast", "Boyz II Men", "Destiny's Child"],
        "d": 1
    },
    {
        "q": "Which Black Eyed Peas single spent 12 weeks at #1 on the Hot 100 in 2009 before being replaced by their own 'I Gotta Feeling'?",
        "correct": "Boom Boom Pow",
        "wrong": ["Imma Be", "Meet Me Halfway", "Let's Get It Started"],
        "d": 1
    },
    {
        "q": "Which French DJ and producer co-wrote and produced The Black Eyed Peas' record-breaking 14-week #1 hit 'I Gotta Feeling'?",
        "correct": "David Guetta",
        "wrong": ["Calvin Harris", "Bob Sinclar", "Martin Solveig"],
        "d": 2
    },
    {
        "q": "Which Kanye West single featuring Jamie Foxx spent 10 weeks at #1 on the Billboard Hot 100 in 2005, sampling Ray Charles's 'I Got a Woman'?",
        "correct": "Gold Digger",
        "wrong": ["Slow Jamz", "Stronger", "All Falls Down"],
        "d": 1
    },
    {
        "q": "Which French electronic duo's track 'Harder, Better, Faster, Stronger' was sampled by Kanye West for his 2007 #1 hit 'Stronger'?",
        "correct": "Daft Punk",
        "wrong": ["Justice", "Air", "Cassius"],
        "d": 1
    },

    # 41-50
    {
        "q": "What was Kanye West's very first single, which peaked at #11 on the Hot 100 in 2003, famously recorded while his jaw was wired shut after a car crash?",
        "correct": "Through the Wire",
        "wrong": ["Jesus Walks", "All Falls Down", "Slow Jamz"],
        "d": 2
    },
    {
        "q": "Which Twista track featuring Kanye West and Jamie Foxx reached #1 on the Billboard Hot 100 in February 2004?",
        "correct": "Slow Jamz",
        "wrong": ["Overnight Celebrity", "Girl Tonite", "Hope"],
        "d": 2
    },
    {
        "q": "Which Avril Lavigne pop-punk single peaked at #2 on the Billboard Hot 100 in 2002, introducing her skater-tie style to the world?",
        "correct": "Complicated",
        "wrong": ["Sk8er Boi", "I'm with You", "My Happy Ending"],
        "d": 1
    },
    {
        "q": "What was Avril Lavigne's only Billboard Hot 100 #1 hit, reaching the summit in May 2007?",
        "correct": "Girlfriend",
        "wrong": ["Complicated", "Sk8er Boi", "When You're Gone"],
        "d": 2
    },
    {
        "q": "What was Maroon 5's first Billboard Hot 100 #1 single, which jumped from #64 to #1 in May 2007?",
        "correct": "Makes Me Wonder",
        "wrong": ["This Love", "She Will Be Loved", "Moves Like Jagger"],
        "d": 2
    },
    {
        "q": "Which Linkin Park debut album peaked at #2 on the Billboard 200 and became the best-selling album in the US for 2001?",
        "correct": "Hybrid Theory",
        "wrong": ["Meteora", "Minutes to Midnight", "A Thousand Suns"],
        "d": 1
    },
    {
        "q": "What peak position did Linkin Park's signature nu-metal anthem 'In the End' reach on the Billboard Hot 100 in 2002?",
        "correct": "#2",
        "wrong": ["#1", "#5", "#9"],
        "d": 2
    },
    {
        "q": "Which rock band spent 43 weeks on the Billboard Hot 100 with 'How You Remind Me', which was named the #1 rock song of the 2000s decade?",
        "correct": "Nickelback",
        "wrong": ["Creed", "3 Doors Down", "Puddle of Mudd"],
        "d": 1
    },
    {
        "q": "Which Canadian band's 2005 album 'All the Right Reasons' spent 156 weeks on the Billboard 200 and was certified Diamond?",
        "correct": "Nickelback",
        "wrong": ["Simple Plan", "Sum 41", "Theory of a Deadman"],
        "d": 2
    },
    {
        "q": "Which Green Day punk rock opera album debuted at #1 on the Billboard 200 in 2004 and won the Grammy for Best Rock Album?",
        "correct": "American Idiot",
        "wrong": ["21st Century Breakdown", "Warning", "Shenanigans"],
        "d": 1
    },

    # 51-60
    {
        "q": "Which Green Day power ballad spent 14 weeks at #1 on the Mainstream Rock chart and peaked at #2 on the Billboard Hot 100 in 2005?",
        "correct": "Boulevard of Broken Dreams",
        "wrong": ["Wake Me Up When September Ends", "Holiday", "American Idiot"],
        "d": 1
    },
    {
        "q": "Which Ciara debut single featuring Petey Pablo topped the Billboard Hot 100 for seven weeks in the summer of 2004?",
        "correct": "Goodies",
        "wrong": ["1, 2 Step", "Oh", "Promise"],
        "d": 1
    },
    {
        "q": "What 16-year-old artist hit #1 on the Billboard Hot 100 in 2005 with his debut single 'Run It!'?",
        "correct": "Chris Brown",
        "wrong": ["Bow Wow", "Soulja Boy", "Mario"],
        "d": 2
    },
    {
        "q": "Which Mario R&B ballad spent nine consecutive weeks at #1 on the Billboard Hot 100 in early 2005, co-written by Ne-Yo?",
        "correct": "Let Me Love You",
        "wrong": ["Just a Friend 2002", "How Could You", "Music for Love"],
        "d": 2
    },
    {
        "q": "Which T-Pain single featuring Yung Joc topped the Billboard Hot 100 for one week in May 2007, solidifying auto-tune in pop rap?",
        "correct": "Buy U a Drank (Shawty Snappin')",
        "wrong": ["Bartender", "I'm 'n Luv (wit a Stripper)", "Can't Believe It"],
        "d": 2
    },
    {
        "q": "Which Flo Rida debut single featuring T-Pain spent 10 consecutive weeks at #1 on the Billboard Hot 100 in early 2008?",
        "correct": "Low",
        "wrong": ["Right Round", "Sugar", "Club Can't Handle Me"],
        "d": 1
    },
    {
        "q": "In Flo Rida's #1 hit 'Low', what footwear was famously matched with 'boots with the fur'?",
        "correct": "Apple Bottom jeans",
        "wrong": ["True Religion jeans", "Baby Phat pants", "Guess jeans"],
        "d": 1
    },
    {
        "q": "Which Lady Gaga debut single featuring Colby O'Donis reached #1 on the Billboard Hot 100 in January 2009 after a 22-week climb?",
        "correct": "Just Dance",
        "wrong": ["Poker Face", "Paparazzi", "LoveGame"],
        "d": 1
    },
    {
        "q": "What was Lady Gaga's second consecutive Billboard Hot 100 #1 hit, becoming the best-selling single of 2009 worldwide?",
        "correct": "Poker Face",
        "wrong": ["Bad Romance", "Telephone", "Alejandro"],
        "d": 1
    },
    {
        "q": "Who produced Lady Gaga's breakthrough #1 pop smashes 'Just Dance' and 'Poker Face'?",
        "correct": "RedOne",
        "wrong": ["Max Martin", "Rob Fusari", "Mark Ronson"],
        "d": 2
    },

    # 61-70
    {
        "q": "Which Soulja Boy track topped the Billboard Hot 100 for seven non-consecutive weeks in 2007, accompanied by an instructional viral dance?",
        "correct": "Crank That (Soulja Boy)",
        "wrong": ["Kiss Me Thru the Phone", "Turn My Swag On", "Yahhh!"],
        "d": 1
    },
    {
        "q": "Which Katy Perry pop-rock single spent seven weeks at #1 on the Billboard Hot 100 in the summer of 2008, sparking cultural conversation?",
        "correct": "I Kissed a Girl",
        "wrong": ["Hot n Cold", "Waking Up in Vegas", "Teenage Dream"],
        "d": 1
    },
    {
        "q": "Which Lil Wayne album sold over one million copies in its first week in June 2008, becoming the top-selling US album of the year?",
        "correct": "Tha Carter III",
        "wrong": ["Tha Carter II", "Tha Carter IV", "I Am Not a Human Being"],
        "d": 1
    },
    {
        "q": "What was Lil Wayne's first solo #1 single on the Billboard Hot 100, topping the chart for five weeks in 2008 featuring Static Major?",
        "correct": "Lollipop",
        "wrong": ["A Milli", "Got Money", "6 Foot 7 Foot"],
        "d": 1
    },
    {
        "q": "Which Alicia Keys and Jay-Z anthem about New York City spent five weeks at #1 on the Billboard Hot 100 in late 2009?",
        "correct": "Empire State of Mind",
        "wrong": ["Run This Town", "Heart of the City", "New York, New York"],
        "d": 1
    },
    {
        "q": "Surprisingly, 'Empire State of Mind' in 2009 gave Jay-Z what chart milestone as a lead artist?",
        "correct": "His very first #1 hit on the Billboard Hot 100 as a lead artist",
        "wrong": ["His tenth #1 single", "His first Top 10 single", "His longest-running single in chart history"],
        "d": 2
    },
    {
        "q": "Which Coldplay ballad from their 2008 album 'Viva la Vida or Death and All His Friends' was the band's first US Billboard Hot 100 #1?",
        "correct": "Viva la Vida",
        "wrong": ["Yellow", "Clocks", "The Scientist"],
        "d": 1
    },
    {
        "q": "Who produced Coldplay's chart-topping 2008 art-rock album 'Viva la Vida or Death and All His Friends'?",
        "correct": "Brian Eno",
        "wrong": ["Ken Nelson", "Rick Rubin", "Nigel Godrich"],
        "d": 2
    },
    {
        "q": "Which Leona Lewis ballad spent four non-consecutive weeks at #1 on the Billboard Hot 100 in spring 2008?",
        "correct": "Bleeding Love",
        "wrong": ["Better in Time", "Run", "Forgive Me"],
        "d": 2
    },
    {
        "q": "Who co-wrote Leona Lewis's international #1 smash 'Bleeding Love' alongside Jesse McCartney?",
        "correct": "Ryan Tedder of OneRepublic",
        "wrong": ["Max Martin", "Ne-Yo", "Danja"],
        "d": 2
    },

    # 71-80
    {
        "q": "Which Timbaland remix featuring OneRepublic peaked at #2 on the Billboard Hot 100 in late 2007 and set North American airplay records?",
        "correct": "Apologize",
        "wrong": ["Stop and Stare", "Say (All I Need)", "Secrets"],
        "d": 1
    },
    {
        "q": "Which Nelly Furtado single featuring Timbaland spent six weeks at #1 on the Billboard Hot 100 in 2006, leading her album 'Loose'?",
        "correct": "Promiscuous",
        "wrong": ["Maneater", "Say It Right", "All Good Things (Come to an End)"],
        "d": 1
    },
    {
        "q": "What was Nelly Furtado's second #1 single from 'Loose', topping the Billboard Hot 100 in early 2007?",
        "correct": "Say It Right",
        "wrong": ["Maneater", "Do It", "In God's Hands"],
        "d": 2
    },
    {
        "q": "Which James Blunt acoustic ballad reached #1 on the Billboard Hot 100 in 2006, the first British artist to top the chart since Elton John in 1997?",
        "correct": "You're Beautiful",
        "wrong": ["Goodbye My Lover", "High", "Wisemen"],
        "d": 1
    },
    {
        "q": "Which Daughtry single peaked at #2 on the Billboard Hot 100 in 2007, becoming the Billboard Year-End #1 single of the year?",
        "correct": "It's Not Over",
        "wrong": ["Home", "Over You", "Feels Like Tonight"],
        "d": 3
    },
    {
        "q": "Which band formed by Chris Daughtry saw their debut album spend two weeks at #1 on the Billboard 200 in 2007?",
        "correct": "Daughtry",
        "wrong": ["Fuel", "Theory of a Deadman", "Default"],
        "d": 2
    },
    {
        "q": "Which Daniel Powter piano-pop song topped the Billboard Hot 100 for three weeks in 2006 and was the Billboard Year-End #1 single?",
        "correct": "Bad Day",
        "wrong": ["Free Loop", "Jimmy Gets High", "Crazy All My Life"],
        "d": 2
    },
    {
        "q": "What popular reality TV show used Daniel Powter's 'Bad Day' as its emotional elimination song during its fifth season?",
        "correct": "American Idol",
        "wrong": ["Survivor", "Dancing with the Stars", "The Voice"],
        "d": 1
    },
    {
        "q": "Which Sean Paul dancehall single reached #1 on the Billboard Hot 100 for three weeks in 2003, chanting 'Can you feel the rhythm?'",
        "correct": "Get Busy",
        "wrong": ["Temperature", "Like Glue", "Gimme the Light"],
        "d": 2
    },
    {
        "q": "What Sean Paul track gave him a second solo #1 hit on the Billboard Hot 100 in spring 2006?",
        "correct": "Temperature",
        "wrong": ["Give It Up to Me", "We Be Burnin'", "So Fine"],
        "d": 2
    },

    # 81-90
    {
        "q": "Which Akon single featuring Snoop Dogg topped the Billboard Hot 100 for two weeks in late 2006?",
        "correct": "I Wanna Love You",
        "wrong": ["Smack That", "Don't Matter", "Locked Up"],
        "d": 2
    },
    {
        "q": "Which Akon reggae-infused ballad reached #1 on the Billboard Hot 100 in April 2007, singing 'Nobody wanna see us together'?",
        "correct": "Don't Matter",
        "wrong": ["Lonely", "Right Now (Na Na Na)", "Sorry, Blame It on Me"],
        "d": 2
    },
    {
        "q": "Which Britney Spears single marked her dramatic chart return by reaching #1 on the Billboard Hot 100 in October 2008?",
        "correct": "Womanizer",
        "wrong": ["Circus", "Gimme More", "Piece of Me"],
        "d": 1
    },
    {
        "q": "What record did Britney Spears' 'Womanizer' break when it vaulted to #1 on the Billboard Hot 100 in 2008?",
        "correct": "Largest jump to #1, vaulting from #96 to #1 in a single week",
        "wrong": ["Fastest-selling physical CD single of the decade", "Longest radio recurrent run", "Most digital plays in three hours"],
        "d": 2
    },
    {
        "q": "What Danity Kane album debuted at #1 on the Billboard 200 in 2006, making them the first female group in history to debut at #1 with their first two albums?",
        "correct": "Danity Kane",
        "wrong": ["Welcome to the Dollhouse", "Making the Band", "Show Stopper"],
        "d": 3
    },
    {
        "q": "Which Jonas Brothers album debuted at #1 on the Billboard 200 in August 2008, selling over 525,000 copies in its first week?",
        "correct": "A Little Bit Longer",
        "wrong": ["Jonas Brothers", "Lines, Vines and Trying Times", "It's About Time"],
        "d": 2
    },
    {
        "q": "Which Taylor Swift single from her 2008 album 'Fearless' peaked at #4 on the Billboard Hot 100 and crossed over to pop radio dominance?",
        "correct": "Love Story",
        "wrong": ["You Belong with Me", "Teardrops on My Guitar", "White Horse"],
        "d": 1
    },
    {
        "q": "What peak position did Taylor Swift's high school anthem 'You Belong with Me' reach on the Billboard Hot 100 in 2009?",
        "correct": "#2",
        "wrong": ["#1", "#4", "#7"],
        "d": 2
    },
    {
        "q": "Taylor Swift's 2008 album 'Fearless' spent how many non-consecutive weeks at #1 on the Billboard 200, winning Album of the Year?",
        "correct": "11 weeks",
        "wrong": ["6 weeks", "16 weeks", "22 weeks"],
        "d": 2
    },
    {
        "q": "Which Miley Cyrus track reached #2 on the Billboard Hot 100 in 2009, declaring 'and the Jay-Z song was on'?",
        "correct": "Party in the U.S.A.",
        "wrong": ["The Climb", "See You Again", "7 Things"],
        "d": 1
    },

    # 91-100
    {
        "q": "Who co-wrote Miley Cyrus's multi-platinum pop anthem 'Party in the U.S.A.' alongside Dr. Luke and Claude Kelly?",
        "correct": "Jessie J",
        "wrong": ["Katy Perry", "Kesha", "Charli XCX"],
        "d": 2
    },
    {
        "q": "Which Kesha debut party anthem spent nine consecutive weeks at #1 on the Billboard Hot 100 starting in late 2009?",
        "correct": "TiK ToK",
        "wrong": ["Your Love Is My Drug", "Blow", "Die Young"],
        "d": 1
    },
    {
        "q": "Which Owl City synth-pop track reached #1 on the Billboard Hot 100 for two weeks in November 2009?",
        "correct": "Fireflies",
        "wrong": ["Good Time", "Vanilla Twilight", "Hello Seattle"],
        "d": 1
    },
    {
        "q": "Which Jason Mraz acoustic pop song spent a then-record 76 weeks on the Billboard Hot 100, peaking at #6 in 2008-2009?",
        "correct": "I'm Yours",
        "wrong": ["Lucky", "I Won't Give Up", "The Remedy (I Won't Worry)"],
        "d": 2
    },
    {
        "q": "Which Colbie Caillat breakthrough acoustic hit peaked at #5 on the Billboard Hot 100 in 2007, starting on MySpace?",
        "correct": "Bubbly",
        "wrong": ["Realize", "Fallin' for You", "Brighter Than the Sun"],
        "d": 2
    },
    {
        "q": "Which Sara Bareilles empowering piano-pop anthem peaked at #4 on the Billboard Hot 100 in 2008?",
        "correct": "Love Song",
        "wrong": ["Brave", "King of Anything", "Gravity"],
        "d": 2
    },
    {
        "q": "Why did Sara Bareilles write 'Love Song'?",
        "correct": "In response to her record label pressuring her to write a marketable radio hit",
        "wrong": ["To apologize after a painful romantic breakup", "As a theme for a major motion picture", "To celebrate her high school sweetheart"],
        "d": 2
    },
    {
        "q": "Which Plain White T's acoustic ballad topped the Billboard Hot 100 for two weeks in July 2007?",
        "correct": "Hey There Delilah",
        "wrong": ["1, 2, 3, 4", "Rhythm of Love", "Hate (I Really Don't Like You)"],
        "d": 1
    },
    {
        "q": "Who was the real-life steeplechase runner Delilah DiCrescenzo that inspired Plain White T's frontman Tom Higgenson to write 'Hey There Delilah'?",
        "correct": "An American Olympic-trials steeplechaser he met through a mutual friend",
        "wrong": ["His college girlfriend", "An actress in Chicago theatre", "A radio program director in New York"],
        "d": 3
    },
    {
        "q": "Which Snow Patrol power ballad peaked at #5 on the Billboard Hot 100 in 2006, propelled by its climax in the season finale of 'Grey's Anatomy'?",
        "correct": "Chasing Cars",
        "wrong": ["Run", "Signal Fire", "Open Your Eyes"],
        "d": 2
    }
]

if __name__ == "__main__":
    formatted = assemble_batch(QUESTIONS, 6)
    save_batch(formatted, 6)
