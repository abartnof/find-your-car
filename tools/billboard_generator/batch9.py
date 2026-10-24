import sys
import os
sys.path.append(os.path.dirname(__file__))
from utils import assemble_batch, save_batch

QUESTIONS = [
    # 1-10
    {
        "q": "On August 4, 1958, Billboard launched the official Hot 100 chart. What was the very first #1 single on the chart?",
        "correct": "Poor Little Fool by Ricky Nelson",
        "wrong": ["Hound Dog by Elvis Presley", "All I Have to Do Is Dream by The Everly Brothers", "Peggy Sue by Buddy Holly"],
        "d": 1
    },
    {
        "q": "What was the very first album to reach #1 on Billboard's newly established Best-Selling Pop Albums chart in 1956?",
        "correct": "Calypso by Harry Belafonte",
        "wrong": ["Elvis Presley by Elvis Presley", "My Fair Lady Original Cast Recording", "Songs for Swingin' Lovers! by Frank Sinatra"],
        "d": 2
    },
    {
        "q": "Which revolutionary electronic point-of-sale tracking system was adopted by Billboard in November 1991, ending manual phone surveys?",
        "correct": "Nielsen SoundScan",
        "wrong": ["BDS Radio Monitor", "Mediabase", "Arbitron Data"],
        "d": 1
    },
    {
        "q": "What major music genre saw an immediate and dramatic surge on the Billboard charts as a direct result of SoundScan data?",
        "correct": "Country music and hip-hop",
        "wrong": ["Classical and jazz", "Heavy metal and disco", "Folk and polka"],
        "d": 2
    },
    {
        "q": "Which electronic system did Billboard adopt in 1990 to monitor actual radio station broadcasts using digital acoustic fingerprinting?",
        "correct": "Broadcast Data Systems (BDS)",
        "wrong": ["Airplay Monitor", "SoundScan", "Mediaguide"],
        "d": 2
    },
    {
        "q": "In December 1998, Billboard changed Hot 100 rules to allow which type of songs to chart for the first time?",
        "correct": "Radio album cuts and airplay-only tracks without physical commercial singles",
        "wrong": ["Instrumental tracks without vocals", "Songs with non-English lyrics", "Songs released exclusively on digital MP3"],
        "d": 2
    },
    {
        "q": "Which song became the first single in Billboard Hot 100 history to debut at #1 upon release, doing so on September 2, 1995?",
        "correct": "You Are Not Alone by Michael Jackson",
        "wrong": ["Fantasy by Mariah Carey", "One Sweet Day by Mariah Carey and Boyz II Men", "Candle in the Wind 1997 by Elton John"],
        "d": 2
    },
    {
        "q": "Who wrote and co-produced Michael Jackson's historic chart-topping debut single 'You Are Not Alone'?",
        "correct": "R. Kelly",
        "wrong": ["Quincy Jones", "Teddy Riley", "Babyface"],
        "d": 2
    },
    {
        "q": "Which Mariah Carey track became the second song in Hot 100 history to debut at #1, just three weeks after Michael Jackson's feat in September 1995?",
        "correct": "Fantasy",
        "wrong": ["Always Be My Baby", "One Sweet Day", "Honey"],
        "d": 2
    },
    {
        "q": "How many total songs debuted at #1 on the Billboard Hot 100 during the entire 20th century (1958 through 1999)?",
        "correct": "14 songs",
        "wrong": ["3 songs", "28 songs", "52 songs"],
        "d": 3
    },

    # 11-20
    {
        "q": "Which musical act holds the all-time record for the most #1 hits on the Billboard Hot 100, with 20 chart-toppers?",
        "correct": "The Beatles",
        "wrong": ["Mariah Carey", "Elvis Presley", "Michael Jackson"],
        "d": 1
    },
    {
        "q": "Which solo artist holds the record for the most #1 hits on the Billboard Hot 100, with 19 chart-topping singles?",
        "correct": "Mariah Carey",
        "wrong": ["Elvis Presley", "Rihanna", "Michael Jackson"],
        "d": 1
    },
    {
        "q": "Which hit single holds the record for the longest continuous run at #1 in Billboard Hot 100 history at 19 weeks?",
        "correct": "Old Town Road by Lil Nas X feat. Billy Ray Cyrus",
        "wrong": ["Despacito by Luis Fonsi & Daddy Yankee", "One Sweet Day by Mariah Carey & Boyz II Men", "Last Night by Morgan Wallen"],
        "d": 1
    },
    {
        "q": "In 2021, Billboard updated its official 'Greatest of All Time Hot 100 Songs' ranking. Which song took the #1 spot?",
        "correct": "Blinding Lights by The Weeknd",
        "wrong": ["The Twist by Chubby Checker", "Smooth by Santana feat. Rob Thomas", "Mack the Knife by Bobby Darin"],
        "d": 1
    },
    {
        "q": "Which artist has accumulated the most total entries on the Billboard Hot 100 in chart history, with over 300 charted songs?",
        "correct": "Drake",
        "wrong": ["Taylor Swift", "Glee Cast", "Lil Wayne"],
        "d": 1
    },
    {
        "q": "What artist holds the record for the most top 10 hits in Billboard Hot 100 history, with over 75 songs?",
        "correct": "Drake",
        "wrong": ["Taylor Swift", "Madonna", "The Beatles"],
        "d": 2
    },
    {
        "q": "Prior to Drake, which female pop icon held the record for the most Billboard Hot 100 top 10 hits with 38?",
        "correct": "Madonna",
        "wrong": ["Mariah Carey", "Whitney Houston", "Aretha Franklin"],
        "d": 2
    },
    {
        "q": "What record did Kelly Clarkson set in February 2009 with 'My Life Would Suck Without You' on the Billboard Hot 100?",
        "correct": "Biggest jump to #1 in chart history, leaping from #97 to #1",
        "wrong": ["Fastest selling digital single in 24 hours", "Longest title of a #1 song", "First American Idol song to reach #1 without a video"],
        "d": 2
    },
    {
        "q": "Whose jump from #96 to #1 with 'Womanizer' in 2008 had previously held the record for biggest jump to #1 before Kelly Clarkson?",
        "correct": "Britney Spears",
        "wrong": ["Rihanna", "Beyoncé", "Katy Perry"],
        "d": 2
    },
    {
        "q": "What album holds the all-time record for the most total weeks spent at #1 on the Billboard 200 album chart at 54 weeks?",
        "correct": "West Side Story soundtrack (1961)",
        "wrong": ["Thriller by Michael Jackson", "Rumours by Fleetwood Mac", "21 by Adele"],
        "d": 2
    },

    # 21-30
    {
        "q": "Among non-soundtrack studio albums, which record holds the modern Billboard 200 record with 37 non-consecutive weeks at #1?",
        "correct": "Thriller by Michael Jackson",
        "wrong": ["Rumours by Fleetwood Mac", "21 by Adele", "The Bodyguard by Whitney Houston"],
        "d": 1
    },
    {
        "q": "What Pink Floyd album holds the record for the most total weeks spent on the Billboard 200, exceeding 980 weeks?",
        "correct": "The Dark Side of the Moon",
        "wrong": ["The Wall", "Wish You Were Here", "Animals"],
        "d": 1
    },
    {
        "q": "Which artist has the most #1 albums in Billboard 200 history for any solo artist, with 14 chart-topping albums?",
        "correct": "Jay-Z",
        "wrong": ["Bruce Springsteen", "Elvis Presley", "Eminem"],
        "d": 2
    },
    {
        "q": "Which overall group holds the record for the most #1 albums in Billboard 200 history, with 19 chart-toppers?",
        "correct": "The Beatles",
        "wrong": ["The Rolling Stones", "Led Zeppelin", "U2"],
        "d": 1
    },
    {
        "q": "Which female artist holds the record for the most #1 albums on the Billboard 200, surpassing Barbra Streisand in 2023?",
        "correct": "Taylor Swift",
        "wrong": ["Madonna", "Mariah Carey", "Beyoncé"],
        "d": 1
    },
    {
        "q": "How many #1 albums did Barbra Streisand achieve on the Billboard 200 across six different decades?",
        "correct": "11",
        "wrong": ["8", "14", "16"],
        "d": 3
    },
    {
        "q": "Under Billboard's 'recurrent rule', a song that falls below which chart position after 20 weeks is automatically removed from the Hot 100?",
        "correct": "Below #50",
        "wrong": ["Below #40", "Below #25", "Below #75"],
        "d": 2
    },
    {
        "q": "Under Billboard's revised recurrent rule, a song that has charted for 52 or more weeks is removed if it falls below which position?",
        "correct": "Below #25",
        "wrong": ["Below #10", "Below #50", "Below #75"],
        "d": 3
    },
    {
        "q": "In which month and year did Billboard officially incorporate YouTube video streaming views into the Hot 100 formula?",
        "correct": "February 2013",
        "wrong": ["January 2010", "March 2015", "September 2017"],
        "d": 3
    },
    {
        "q": "Which viral novelty instrumental immediately benefited from the YouTube streaming formula change to debut at #1 on the Hot 100 in 2013?",
        "correct": "Harlem Shake by Baauer",
        "wrong": ["Gangnam Style by PSY", "What Does the Fox Say? by Ylvis", "Turn Down for What by DJ Snake & Lil Jon"],
        "d": 2
    },

    # 31-40
    {
        "q": "In which year did Billboard begin incorporating paid and ad-supported audio on-demand streaming (e.g., Spotify, Rhapsody) into the Hot 100?",
        "correct": "2012",
        "wrong": ["2008", "2010", "2016"],
        "d": 3
    },
    {
        "q": "In 2014, Billboard modernized the Billboard 200 album chart by creating SEA and TEA units. What does SEA stand for?",
        "correct": "Streaming Equivalent Albums",
        "wrong": ["Single Equivalent Airplay", "Standard Electronic Audio", "Systemic Engagement Analytics"],
        "d": 2
    },
    {
        "q": "What does TEA stand for in Billboard 200 chart methodology?",
        "correct": "Track Equivalent Albums",
        "wrong": ["Total Electronic Audio", "Total Engagement Airplay", "Track Electronic Analytics"],
        "d": 2
    },
    {
        "q": "How many individual paid track downloads originally equaled one Track Equivalent Album (TEA) unit on the Billboard 200?",
        "correct": "10 track sales",
        "wrong": ["5 track sales", "15 track sales", "20 track sales"],
        "d": 2
    },
    {
        "q": "Under current Billboard 200 methodology, approximately how many paid subscription streams of songs from an album equal one SEA unit?",
        "correct": "1,250 streams",
        "wrong": ["500 streams", "2,500 streams", "3,750 streams"],
        "d": 3
    },
    {
        "q": "How many ad-supported (free tier) audio streams equal one SEA unit on the Billboard 200?",
        "correct": "3,750 streams",
        "wrong": ["1,500 streams", "2,500 streams", "5,000 streams"],
        "d": 3
    },
    {
        "q": "Which 1958 Christmas holiday classic by Brenda Lee hit #1 on the Billboard Hot 100 for the first time in December 2023, 65 years after its debut?",
        "correct": "Rockin' Around the Christmas Tree",
        "wrong": ["Jingle Bell Rock", "A Holly Jolly Christmas", "Run Rudolph Run"],
        "d": 1
    },
    {
        "q": "How old was Brenda Lee when 'Rockin' Around the Christmas Tree' reached #1 on the Hot 100 in 2023, making her the oldest artist to top the chart?",
        "correct": "78 years old",
        "wrong": ["72 years old", "81 years old", "85 years old"],
        "d": 2
    },
    {
        "q": "Whose record as the oldest living artist to top the Hot 100 did Brenda Lee break in 2023?",
        "correct": "Cher (52 years old with 'Believe')",
        "wrong": ["Louis Armstrong (62 years old)", "Frank Sinatra (51 years old)", "Tina Turner (44 years old)"],
        "d": 2
    },
    {
        "q": "Which holiday classic holds the record as the longest gap between releases and reaching #1 on the Hot 100 at 65 years?",
        "correct": "Rockin' Around the Christmas Tree by Brenda Lee",
        "wrong": ["All I Want for Christmas Is You by Mariah Carey", "White Christmas by Bing Crosby", "The Twist by Chubby Checker"],
        "d": 2
    },

    # 41-50
    {
        "q": "Which Motown legend had a 26-year gap between their Billboard Hot 100 #1 hits with 'Little Stevie Wonder' (1963) and 'Part-Time Lover' (1985)?",
        "correct": "Stevie Wonder",
        "wrong": ["Marvin Gaye", "Smokey Robinson", "Diana Ross"],
        "d": 3
    },
    {
        "q": "Who holds the record for the longest span between an artist's first and last #1 on the Billboard Hot 100, spanning over 59 years?",
        "correct": "The Beatles (1964 with 'I Want to Hold Your Hand' to 2023 with 'Now and Then')",
        "wrong": ["Cher (1965 to 1999)", "Elvis Presley (1956 to 2002)", "Brenda Lee (1960 to 2023)"],
        "d": 2
    },
    {
        "q": "Which Beatles single released in November 2023, utilizing AI audio restoration on John Lennon's vocal demo, peaked at #7 on the Hot 100?",
        "correct": "Now and Then",
        "wrong": ["Free as a Bird", "Real Love", "Grow Old with Me"],
        "d": 2
    },
    {
        "q": "Which artist holds the record for the most simultaneous entries on the Billboard Hot 100 in a single week, with 32 songs?",
        "correct": "Taylor Swift",
        "wrong": ["Drake", "Morgan Wallen", "Lil Wayne"],
        "d": 2
    },
    {
        "q": "How many songs from Morgan Wallen's 36-track album 'One Thing at a Time' charted on the Billboard Hot 100 simultaneously in March 2023?",
        "correct": "36 songs",
        "wrong": ["24 songs", "30 songs", "18 songs"],
        "d": 3
    },
    {
        "q": "What song holds the record for the longest climb to reach the top 10 of the Billboard Hot 100, taking 35 weeks?",
        "correct": "Radioactive by Imagine Dragons",
        "wrong": ["Before He Cheats by Carrie Underwood", "Heat Waves by Glass Animals", "Sail by AWOLNATION"],
        "d": 3
    },
    {
        "q": "What song spent a then-record 54 weeks in the Billboard Hot 100 top 40 between 2019 and 2021?",
        "correct": "Blinding Lights by The Weeknd",
        "wrong": ["Circles by Post Malone", "Levitating by Dua Lipa", "Stay by The Kid LAROI & Justin Bieber"],
        "d": 2
    },
    {
        "q": "Which Fleetwood Mac album spent 31 non-consecutive weeks at #1 on the Billboard 200 in 1977-1978?",
        "correct": "Rumours",
        "wrong": ["Fleetwood Mac", "Tusk", "Mirage"],
        "d": 1
    },
    {
        "q": "How many #1 singles did Fleetwood Mac's 31-week chart-topping album 'Rumours' generate on the Billboard Hot 100?",
        "correct": "One ('Dreams')",
        "wrong": ["Two", "Three", "Four"],
        "d": 2
    },
    {
        "q": "Which Canadian rock band had their 1999 single 'Smooth' with Santana spend 30 weeks in the Billboard Hot 100 top 10?",
        "correct": "Matchbox 20 (featuring singer Rob Thomas)",
        "wrong": ["The Tragically Hip", "Barenaked Ladies", "Our Lady Peace"],
        "d": 2
    },

    # 51-60
    {
        "q": "Which R&B vocal group was the first musical act in Billboard history to spend at least 10 weeks at #1 with three separate singles?",
        "correct": "Boyz II Men",
        "wrong": ["TLC", "Destiny's Child", "Blackstreet"],
        "d": 2
    },
    {
        "q": "What were the three Boyz II Men singles that each spent 12 or more weeks at #1 on the Hot 100 in the 1990s?",
        "correct": "End of the Road, I'll Make Love to You, and One Sweet Day",
        "wrong": ["Motownphilly, On Bended Knee, and Water Runs Dry", "End of the Road, In the Still of the Nite, and 4 Seasons of Loneliness", "I'll Make Love to You, A Song for Mama, and Please Don't Go"],
        "d": 2
    },
    {
        "q": "Which artist was the first woman in Billboard Hot 100 history to replace herself at the #1 position?",
        "correct": "Taylor Swift (with 'Blank Space' replacing 'Shake It Off' in 2014)",
        "wrong": ["Mariah Carey", "Beyoncé", "Madonna"],
        "d": 2
    },
    {
        "q": "Which artist became the second woman in Hot 100 history to replace herself at #1 when '7 Rings' replaced 'Thank U, Next' in 2019?",
        "correct": "Ariana Grande",
        "wrong": ["Cardi B", "Billie Eilish", "Dua Lipa"],
        "d": 2
    },
    {
        "q": "Which hip-hop artist replaced himself at #1 on the Billboard Hot 100 in 2004 with 'Burn' replacing 'Yeah!'?",
        "correct": "Usher",
        "wrong": ["50 Cent", "Nelly", "Ludacris"],
        "d": 2
    },
    {
        "q": "Which rap icon replaced himself at #1 in 2018 when 'Nice for What' replaced 'God's Plan', and later 'In My Feelings' replaced 'Nice for What'?",
        "correct": "Drake",
        "wrong": ["Kendrick Lamar", "Travis Scott", "Post Malone"],
        "d": 2
    },
    {
        "q": "In what year did Billboard debut the official Hot Country Songs chart under its modern format?",
        "correct": "1958",
        "wrong": ["1944", "1965", "1972"],
        "d": 3
    },
    {
        "q": "Which song holds the record for the most total weeks spent at #1 on the Hot Country Songs chart at 50 weeks?",
        "correct": "Meant to Be by Bebe Rexha & Florida Georgia Line",
        "wrong": ["Body Like a Back Road by Sam Hunt", "Cruise by Florida Georgia Line", "Last Night by Morgan Wallen"],
        "d": 2
    },
    {
        "q": "Which Sam Hunt single previously held the record for most weeks at #1 on Hot Country Songs at 34 weeks in 2017?",
        "correct": "Body Like a Back Road",
        "wrong": ["Take Your Time", "House Party", "Leave the Night On"],
        "d": 2
    },
    {
        "q": "What is the only song to spend at least 50 weeks at #1 on any Billboard genre chart?",
        "correct": "Meant to Be by Bebe Rexha & Florida Georgia Line",
        "wrong": ["Old Town Road by Lil Nas X", "Despacito by Luis Fonsi", "Radioactive by Imagine Dragons"],
        "d": 3
    },

    # 61-70
    {
        "q": "Which Luis Fonsi smash holds the record for the most weeks at #1 on the Hot Latin Songs chart at 56 weeks?",
        "correct": "Despacito",
        "wrong": ["Bailando", "Ginza", "Dákiti"],
        "d": 2
    },
    {
        "q": "Whose 41-week run at #1 with 'Bailando' on the Hot Latin Songs chart was shattered by 'Despacito'?",
        "correct": "Enrique Iglesias",
        "wrong": ["Daddy Yankee", "Ricky Martin", "Marc Anthony"],
        "d": 2
    },
    {
        "q": "Which Panic! At The Disco pop-rock song holds the record for the most weeks at #1 on the Hot Rock & Alternative Songs chart at 76 weeks?",
        "correct": "High Hopes",
        "wrong": ["Hey Look Ma, I Made It", "Death of a Bachelor", "I Write Sins Not Tragedies"],
        "d": 2
    },
    {
        "q": "Which Imagine Dragons hit previously spent 30 weeks at #1 on the Hot Rock Songs chart in 2017-2018?",
        "correct": "Believer",
        "wrong": ["Radioactive", "Thunder", "Demons"],
        "d": 2
    },
    {
        "q": "Which soundtrack holds the record for the most consecutive weeks at #1 on the Billboard 200 during the rock era, at 31 weeks in 1967-1968?",
        "correct": "The Sound of Music",
        "wrong": ["Mary Poppins", "Doctor Zhivago", "The Graduate"],
        "d": 3
    },
    {
        "q": "What 1997 soundtrack album spent 16 consecutive weeks at #1 on the Billboard 200, driven by an orchestral score and a single pop ballad?",
        "correct": "Titanic: Music from the Motion Picture",
        "wrong": ["The Lion King", "Armageddon", "City of Angels"],
        "d": 1
    },
    {
        "q": "Which Disney soundtrack spent 13 non-consecutive weeks at #1 on the Billboard 200 in 2014, led by the anthem 'Let It Go'?",
        "correct": "Frozen",
        "wrong": ["Moana", "The Lion King", "Tarzan"],
        "d": 1
    },
    {
        "q": "Which Disney soundtrack from 2021-2022 spent nine weeks at #1 on the Billboard 200, featuring the hit 'We Don't Talk About Bruno'?",
        "correct": "Encanto",
        "wrong": ["Coco", "Moana", "Frozen II"],
        "d": 1
    },
    {
        "q": "What peak position did the ensemble song 'We Don't Talk About Bruno' reach on the Billboard Hot 100 in January 2022?",
        "correct": "#1",
        "wrong": ["#2", "#5", "#10"],
        "d": 1
    },
    {
        "q": "Whose 1993 ballad 'A Whole New World' from 'Aladdin' was the only other Disney animated film song to hit #1 on the Hot 100 before 'We Don't Talk About Bruno'?",
        "correct": "Peabo Bryson and Regina Belle",
        "wrong": ["Elton John", "Phil Collins", "Celine Dion and Peabo Bryson"],
        "d": 2
    },

    # 71-80
    {
        "q": "Who wrote all the original songs for the 2021 Disney blockbuster soundtrack 'Encanto', including 'We Don't Talk About Bruno'?",
        "correct": "Lin-Manuel Miranda",
        "wrong": ["Alan Menken", "Robert Lopez and Kristen Anderson-Lopez", "Stephen Schwartz"],
        "d": 1
    },
    {
        "q": "What Lin-Manuel Miranda Broadway cast album spent over 400 weeks on the Billboard 200 and peaked at #2 following its Disney+ release in 2020?",
        "correct": "Hamilton: An American Musical",
        "wrong": ["In the Heights", "Dear Evan Hansen", "Wicked"],
        "d": 2
    },
    {
        "q": "Which 1978 movie soundtrack featured two different songs that hit #1 on the Hot 100: the title track and 'You're the One That I Want'?",
        "correct": "Grease",
        "wrong": ["Saturday Night Fever", "Footloose", "Fame"],
        "d": 1
    },
    {
        "q": "Which 1984 movie soundtrack spawned two #1 hits on the Hot 100: Kenny Loggins' title track and Deniece Williams' 'Let's Hear It for the Boy'?",
        "correct": "Footloose",
        "wrong": ["Flashdance", "Ghostbusters", "Top Gun"],
        "d": 2
    },
    {
        "q": "Which 1986 soundtrack album topped the Billboard 200 for five weeks, featuring Berlin's 'Take My Breath Away' and Kenny Loggins' 'Danger Zone'?",
        "correct": "Top Gun",
        "wrong": ["Beverly Hills Cop", "Miami Vice", "St. Elmo's Fire"],
        "d": 2
    },
    {
        "q": "Which Berlin love theme from 'Top Gun' won the Oscar for Best Original Song and reached #1 on the Hot 100 in September 1986?",
        "correct": "Take My Breath Away",
        "wrong": ["The Metro", "No More Words", "Sex (I'm A...)"],
        "d": 2
    },
    {
        "q": "Who co-wrote and produced Berlin's 'Take My Breath Away' alongside lyricist Tom Whitlock?",
        "correct": "Giorgio Moroder",
        "wrong": ["Harold Faltermeyer", "David Foster", "Arthur Baker"],
        "d": 2
    },
    {
        "q": "Which Harold Faltermeyer instrumental synthesizer theme from 'Beverly Hills Cop' reached #3 on the Billboard Hot 100 in 1985?",
        "correct": "Axel F",
        "wrong": ["Miami Vice Theme", "The Heat Is On", "Chariots of Fire"],
        "d": 2
    },
    {
        "q": "Which Jan Hammer instrumental theme from a television crime drama reached #1 on the Billboard Hot 100 in November 1985?",
        "correct": "Miami Vice Theme",
        "wrong": ["Axel F", "Magnum, P.I. Theme", "Hill Street Blues Theme"],
        "d": 2
    },
    {
        "q": "Which 1991 movie soundtrack by Michael Kamen produced Bryan Adams' 7-week #1 hit '(Everything I Do) I Do It for You'?",
        "correct": "Robin Hood: Prince of Thieves",
        "wrong": ["Lethal Weapon 3", "Die Hard with a Vengeance", "The Three Musketeers"],
        "d": 2
    },

    # 81-90
    {
        "q": "What was the very first Rap album to reach #1 on the Billboard 200 album chart, doing so in March 1987?",
        "correct": "Licensed to Ill by Beastie Boys",
        "wrong": ["Raising Hell by Run-D.M.C.", "Radio by LL Cool J", "It Takes a Nation of Millions by Public Enemy"],
        "d": 2
    },
    {
        "q": "How many weeks did Beastie Boys' 'Licensed to Ill' spend at #1 on the Billboard 200 in 1987?",
        "correct": "Seven weeks",
        "wrong": ["Two weeks", "Four weeks", "Twelve weeks"],
        "d": 3
    },
    {
        "q": "Who was the legendary producer who co-founded Def Jam Recordings and produced 'Licensed to Ill' and Run-D.M.C.'s 'Raising Hell'?",
        "correct": "Rick Rubin",
        "wrong": ["Russell Simmons", "Arthur Baker", "Marley Marl"],
        "d": 2
    },
    {
        "q": "What Run-D.M.C. rock-rap collaboration with Aerosmith reached #4 on the Billboard Hot 100 in 1986, breaking rap onto MTV?",
        "correct": "Walk This Way",
        "wrong": ["King of Rock", "It's Tricky", "Peter Piper"],
        "d": 1
    },
    {
        "q": "Which heavy metal album became the first to reach #1 on the Billboard 200, topping the chart in November 1983?",
        "correct": "Metal Health by Quiet Riot",
        "wrong": ["Pyromania by Def Leppard", "Shout at the Devil by Mötley Crüe", "1984 by Van Halen"],
        "d": 2
    },
    {
        "q": "What Slade cover song on Quiet Riot's 'Metal Health' peaked at #5 on the Billboard Hot 100, driving the album to #1?",
        "correct": "Cum On Feel the Noize",
        "wrong": ["Metal Health (Bang Your Head)", "Mama Weer All Crazee Now", "Slick Black Cadillac"],
        "d": 2
    },
    {
        "q": "Which 1983 Def Leppard album peaked at #2 on the Billboard 200 for multiple weeks, held out of #1 exclusively by Michael Jackson's 'Thriller'?",
        "correct": "Pyromania",
        "wrong": ["High 'n' Dry", "Hysteria", "Adrenalize"],
        "d": 2
    },
    {
        "q": "What Alanis Morissette record set the mark in 1996 for the best-selling debut album by a female artist in US history?",
        "correct": "Jagged Little Pill",
        "wrong": ["...Baby One More Time by Britney Spears", "Whitney Houston by Whitney Houston", "Come On Over by Shania Twain"],
        "d": 2
    },
    {
        "q": "Which album holds the record for the biggest jump to #1 on the Billboard 200, leaping from #181 to #1 in 2008 after a 62-cent sales promotion?",
        "correct": "Life in Cartoon Motion by Mika",
        "wrong": ["Fearless by Taylor Swift", "Radiohead's In Rainbows", "Noel by Josh Groban"],
        "d": 3
    },
    {
        "q": "Which artist holds the record for the most top 10 debuts on the Billboard Hot 100, with over 50 songs entering directly in the top 10?",
        "correct": "Drake",
        "wrong": ["Taylor Swift", "Eminem", "Justin Bieber"],
        "d": 2
    },

    # 91-100
    {
        "q": "What was the first instrumental track to reach #1 on the Billboard Hot 100 during the rock era?",
        "correct": "Tequila by The Champs (1958)",
        "wrong": ["The Poor People of Paris by Les Baxter", "Theme from A Summer Place by Percy Faith", "Telstar by The Tornados"],
        "d": 3
    },
    {
        "q": "Which British sci-fi instrumental became the first US #1 hit by a British group on the Billboard Hot 100 in December 1962?",
        "correct": "Telstar by The Tornados",
        "wrong": ["Apache by The Shadows", "Stranger on the Shore by Mr. Acker Bilk", "Pipeline by The Chantays"],
        "d": 3
    },
    {
        "q": "Who produced the futuristic 1962 #1 instrumental hit 'Telstar' in his London home studio using electronic oscillators?",
        "correct": "Joe Meek",
        "wrong": ["George Martin", "Mickie Most", "Shel Talmy"],
        "d": 3
    },
    {
        "q": "Which Jan & Dean surf-pop classic was co-written by Brian Wilson and reached #1 on the Billboard Hot 100 in July 1963?",
        "correct": "Surf City",
        "wrong": ["Dead Man's Curve", "The Little Old Lady from Pasadena", "Drag City"],
        "d": 2
    },
    {
        "q": "What 1963 single by The Kingsmen reached #2 on the Hot 100 and was investigated by the FBI for allegedly obscene, unintelligible lyrics?",
        "correct": "Louie Louie",
        "wrong": ["Surfin' Bird", "Wipe Out", "Wooly Bully"],
        "d": 2
    },
    {
        "q": "What was the conclusion of the FBI's multi-year investigation into the lyrics of The Kingsmen's 'Louie Louie'?",
        "correct": "The recording was unintelligible at any speed and therefore legally not obscene",
        "wrong": ["The band was fined $10,000", "The single was banned from interstate commerce", "The singer admitted to inserting obscene jokes"],
        "d": 2
    },
    {
        "q": "Which Sam the Sham & the Pharaohs party rocker was named the Billboard Year-End #1 single of 1965 despite never reaching #1 on the weekly Hot 100?",
        "correct": "Wooly Bully",
        "wrong": ["Li'l Red Riding Hood", "Hang On Sloopy", "Help Me, Rhonda"],
        "d": 2
    },
    {
        "q": "What peak position did Sam the Sham's 'Wooly Bully' reach on the Billboard Hot 100 in 1965?",
        "correct": "#2",
        "wrong": ["#3", "#4", "#5"],
        "d": 2
    },
    {
        "q": "Which song holds the record for the most total non-consecutive runs at #1 on the Billboard Hot 100, having reached #1 in five separate holiday seasons?",
        "correct": "All I Want for Christmas Is You by Mariah Carey",
        "wrong": ["Rockin' Around the Christmas Tree by Brenda Lee", "The Twist by Chubby Checker", "Jingle Bell Rock by Bobby Helms"],
        "d": 1
    },
    {
        "q": "In total, how many weeks has Mariah Carey's 'All I Want for Christmas Is You' spent at #1 on the Billboard Hot 100 through January 2024?",
        "correct": "14 weeks",
        "wrong": ["8 weeks", "10 weeks", "18 weeks"],
        "d": 2
    }
]

if __name__ == "__main__":
    formatted = assemble_batch(QUESTIONS, 9)
    save_batch(formatted, 9)
