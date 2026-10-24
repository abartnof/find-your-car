import sys
import os
sys.path.append(os.path.dirname(__file__))
from utils import assemble_batch, save_batch

QUESTIONS = [
    # 1-10
    {
        "q": "Which 1956 Elvis Presley single spent 11 weeks at #1 on the Billboard Best Sellers in Stores chart and was backed with 'Don't Be Cruel'?",
        "correct": "Hound Dog",
        "wrong": ["Heartbreak Hotel", "Love Me Tender", "Jailhouse Rock"],
        "d": 1
    },
    {
        "q": "In The Beatles' 1968 #1 hit 'Hey Jude', what is the advice given in the opening verse to make things better?",
        "correct": "Take a sad song and make it better",
        "wrong": ["Carry that weight a long time", "Listen to the music playing", "Look into your heart and smile"],
        "d": 1
    },
    {
        "q": "Which girl group scored the first of their 12 Billboard Hot 100 #1 hits with 'Where Did Our Love Go' in 1964?",
        "correct": "The Supremes",
        "wrong": ["The Marvelettes", "The Ronettes", "The Shirelles"],
        "d": 1
    },
    {
        "q": "What Beach Boys song, driven by an electro-theremin and complex vocal harmonies, reached #1 on the Billboard Hot 100 in December 1966?",
        "correct": "Good Vibrations",
        "wrong": ["California Girls", "God Only Knows", "Surfin' U.S.A."],
        "d": 1
    },
    {
        "q": "Otis Redding's only Billboard Hot 100 #1 single was released posthumously in early 1968. What was its title?",
        "correct": "(Sittin' On) The Dock of the Bay",
        "wrong": ["Try a Little Tenderness", "I've Been Loving You Too Long", "Respect"],
        "d": 1
    },
    {
        "q": "Which Rolling Stones classic, featuring Keith Richards' iconic fuzz-guitar riff, became the band's first US Billboard Hot 100 #1 in 1965?",
        "correct": "(I Can't Get No) Satisfaction",
        "wrong": ["Paint It Black", "Get Off of My Cloud", "Jumpin' Jack Flash"],
        "d": 1
    },
    {
        "q": "What Aretha Franklin anthem, originally written and recorded by Otis Redding, reached #1 on the Billboard Hot 100 in June 1967?",
        "correct": "Respect",
        "wrong": ["Think", "Chain of Fools", "Natural Woman"],
        "d": 1
    },
    {
        "q": "Which Motown legend topped the Billboard Hot 100 in 1968 with his soul rendition of 'I Heard It Through the Grapevine'?",
        "correct": "Marvin Gaye",
        "wrong": ["Smokey Robinson", "Stevie Wonder", "David Ruffin"],
        "d": 1
    },
    {
        "q": "What song by Simon & Garfunkel was featured prominently in the 1967 film 'The Graduate' and hit #1 in June 1968?",
        "correct": "Mrs. Robinson",
        "wrong": ["The Sound of Silence", "Bridge over Troubled Water", "The Boxer"],
        "d": 1
    },
    {
        "q": "What 1967 psychedelic anthem by The Doors hit #1 on the Billboard Hot 100 after a shortened single edit was released to radio?",
        "correct": "Light My Fire",
        "wrong": ["Touch Me", "Hello, I Love You", "Break On Through"],
        "d": 1
    },

    # 11-20
    {
        "q": "On April 4, 1964, The Beatles accomplished an unprecedented feat by occupying which positions on the Billboard Hot 100?",
        "correct": "All top 5 positions simultaneously",
        "wrong": ["The entire top 10 simultaneously", "Positions 1, 2, and 3 for 12 weeks", "The top 4 positions on both Hot 100 and album charts"],
        "d": 2
    },
    {
        "q": "Which song was #1 on the Billboard Hot 100 when The Beatles swept the entire top 5 in April 1964?",
        "correct": "Can't Buy Me Love",
        "wrong": ["Twist and Shout", "She Loves You", "I Want to Hold Your Hand"],
        "d": 2
    },
    {
        "q": "Which 1965 Bob Dylan track clocked in at over six minutes and peaked at #2 on the Billboard Hot 100, revolutionizing radio length standards?",
        "correct": "Like a Rolling Stone",
        "wrong": ["Subterranean Homesick Blues", "Blowin' in the Wind", "Positively 4th Street"],
        "d": 2
    },
    {
        "q": "Percy Sledge's emotional soul ballad 'When a Man Loves a Woman' reached #1 in 1966 after being recorded at which famous studio?",
        "correct": "Norala Sound Studio in Sheffield, Alabama",
        "wrong": ["Abbey Road Studios in London", "Hitsville U.S.A. in Detroit", "Sun Studio in Memphis"],
        "d": 3
    },
    {
        "q": "What was the first Billboard Hot 100 #1 single recorded by The Monkees in 1966, written by Tommy Boyce and Bobby Hart?",
        "correct": "Last Train to Clarksville",
        "wrong": ["I'm a Believer", "Daydream Believer", "Pleasant Valley Sunday"],
        "d": 2
    },
    {
        "q": "Who wrote The Monkees' smash #1 hit 'I'm a Believer', which topped the Hot 100 for seven weeks starting in late 1966?",
        "correct": "Neil Diamond",
        "wrong": ["Carole King", "Paul Simon", "Brian Wilson"],
        "d": 2
    },
    {
        "q": "Which 1958 hit by Domenico Modugno is the only foreign-language song to win both Record of the Year and Song of the Year at the Grammys after hitting #1 on the Hot 100?",
        "correct": "Nel Blu, Dipinto di Blu (Volare)",
        "wrong": ["La Bamba", "Sukiyaki", "Guantanamera"],
        "d": 3
    },
    {
        "q": "What 1963 single by Japanese singer Kyu Sakamoto reached #1 on the Billboard Hot 100 under an alternative American title named after a dish?",
        "correct": "Sukiyaki",
        "wrong": ["Teriyaki", "Sashimi", "Tempura"],
        "d": 2
    },
    {
        "q": "What 1969 Creedence Clearwater Revival song peaked at #2 on the Billboard Hot 100 and famously contains the misheard line 'there's a bathroom on the right'?",
        "correct": "Bad Moon Rising",
        "wrong": ["Proud Mary", "Fortunate Son", "Down on the Corner"],
        "d": 2
    },
    {
        "q": "How many songs by Creedence Clearwater Revival peaked at #2 on the Billboard Hot 100 without ever reaching #1, setting an all-time record?",
        "correct": "Five",
        "wrong": ["Three", "Seven", "Nine"],
        "d": 3
    },

    # 21-30
    {
        "q": "Which British Invasion band hit #1 in 1964 with a dramatic rock arrangement of the traditional folk song 'The House of the Rising Sun'?",
        "correct": "The Animals",
        "wrong": ["The Kinks", "The Yardbirds", "The Hollies"],
        "d": 2
    },
    {
        "q": "What instrument plays the prominent haunting solo in The Beach Boys' 1966 Top 5 masterpiece 'God Only Knows'?",
        "correct": "French horn",
        "wrong": ["Oboe", "Bassoon", "English horn"],
        "d": 3
    },
    {
        "q": "In 1961, which 16-year-old artist hit #1 on the Billboard Hot 100 with 'Runaway', featuring an electric keyboard called the Musitron?",
        "correct": "Del Shannon",
        "wrong": ["Bobby Vee", "Paul Anka", "Gene Pitney"],
        "d": 3
    },
    {
        "q": "Which Motown group earned the label its very first Billboard Hot 100 #1 hit in late 1961 with 'Please Mr. Postman'?",
        "correct": "The Marvelettes",
        "wrong": ["The Miracles", "The Temptations", "The Vandellas"],
        "d": 2
    },
    {
        "q": "Which iconic Beatles single was originally released as a double A-side with 'Penny Lane' in February 1967, peaking at #8 while Penny Lane hit #1?",
        "correct": "Strawberry Fields Forever",
        "wrong": ["A Day in the Life", "Eleanor Rigby", "Yellow Submarine"],
        "d": 2
    },
    {
        "q": "Which artist sang lead vocals on The Temptations' first Billboard Hot 100 #1 single, 1965's 'My Girl'?",
        "correct": "David Ruffin",
        "wrong": ["Eddie Kendricks", "Paul Williams", "Dennis Edwards"],
        "d": 2
    },
    {
        "q": "Who wrote and produced 'My Girl' for The Temptations after being inspired by his wife Claudette Rogers?",
        "correct": "Smokey Robinson",
        "wrong": ["Berry Gordy", "Norman Whitfield", "Holland-Dozier-Holland"],
        "d": 2
    },
    {
        "q": "What 1967 song by The Turtles knocked The Beatles' 'Penny Lane' out of the #1 spot on the Billboard Hot 100?",
        "correct": "Happy Together",
        "wrong": ["Elenore", "She'd Rather Be with Me", "You Showed Me"],
        "d": 2
    },
    {
        "q": "Which track by The 5th Dimension spent six weeks at #1 on the Billboard Hot 100 in 1969, originating from the musical 'Hair'?",
        "correct": "Aquarius / Let the Sunshine In",
        "wrong": ["Up, Up and Away", "Wedding Bell Blues", "Stoned Soul Picnic"],
        "d": 1
    },
    {
        "q": "What was Stevie Wonder's first Billboard Hot 100 #1 single, recorded live when he was just 12 years old and billed as 'Little Stevie Wonder'?",
        "correct": "Fingertips (Pt. 2)",
        "wrong": ["Uptight (Everything's Alright)", "I Was Made to Love Her", "My Cherie Amour"],
        "d": 2
    },

    # 31-40
    {
        "q": "Which 1969 single by The Archies spent four weeks at #1 and became the Billboard Year-End #1 single of 1969?",
        "correct": "Sugar, Sugar",
        "wrong": ["Jingle Jangle", "Bang-Shang-A-Lang", "Feelin' So Good"],
        "d": 1
    },
    {
        "q": "Who was the studio session singer who provided the lead vocals on The Archies' #1 smash 'Sugar, Sugar'?",
        "correct": "Ron Dante",
        "wrong": ["Tony Orlando", "Tommy Roe", "Andy Kim"],
        "d": 3
    },
    {
        "q": "Which Elvis Presley song, his last Billboard Hot 100 #1 during his lifetime, topped the chart in November 1969?",
        "correct": "Suspicious Minds",
        "wrong": ["In the Ghetto", "Burning Love", "Always on My Mind"],
        "d": 2
    },
    {
        "q": "Who wrote 'Suspicious Minds', which Elvis Presley took to #1 after recording it at American Sound Studio in Memphis?",
        "correct": "Mark James",
        "wrong": ["Mac Davis", "Chips Moman", "Jerry Leiber"],
        "d": 3
    },
    {
        "q": "What was the debut single by Sly and the Family Stone to reach #1 on the Billboard Hot 100, doing so in early 1969?",
        "correct": "Everyday People",
        "wrong": ["Dance to the Music", "Hot Fun in the Summertime", "Thank You (Falettinme Be Mice Elf Agin)"],
        "d": 2
    },
    {
        "q": "Which 1968 instrumental piece by classical composer Paul Mauriat spent five weeks at #1 on the Hot 100?",
        "correct": "Love Is Blue",
        "wrong": ["Theme from A Summer Place", "Telstar", "Classical Gas"],
        "d": 3
    },
    {
        "q": "What 1960 Percy Faith instrumental holds the record as the longest-running instrumental #1 in Billboard Hot 100 history at 9 weeks?",
        "correct": "Theme from A Summer Place",
        "wrong": ["The Poor People of Paris", "Tequila", "Chariots of Fire"],
        "d": 2
    },
    {
        "q": "Which female artist hit #1 in 1963 with 'It's My Party', produced by a young Quincy Jones?",
        "correct": "Lesley Gore",
        "wrong": ["Brenda Lee", "Connie Francis", "Peggy March"],
        "d": 2
    },
    {
        "q": "What is the title of the direct lyrical sequel Lesley Gore released following 'It's My Party', which reached #5 on the Hot 100?",
        "correct": "Judy's Turn to Cry",
        "wrong": ["You Don't Own Me", "Maybe I Know", "She's a Fool"],
        "d": 3
    },
    {
        "q": "Which Lesley Gore feminist anthem peaked at #2 on the Billboard Hot 100 in 1964, held out of #1 only by The Beatles' 'I Want to Hold Your Hand'?",
        "correct": "You Don't Own Me",
        "wrong": ["It's My Party", "Judy's Turn to Cry", "Sunshine, Lollipops and Rainbows"],
        "d": 2
    },

    # 41-50
    {
        "q": "Which classic 1965 Righteous Brothers single, produced by Phil Spector using his famous 'Wall of Sound', reached #1 on the Hot 100?",
        "correct": "You've Lost That Lovin' Feelin'",
        "wrong": ["Unchained Melody", "(You're My) Soul and Inspiration", "Ebb Tide"],
        "d": 1
    },
    {
        "q": "Which song by The Mamas & the Papas reached #1 on the Billboard Hot 100 in May 1966, celebrating Monday mornings?",
        "correct": "Monday, Monday",
        "wrong": ["California Dreamin'", "Creeque Alley", "Dedicated to the One I Love"],
        "d": 2
    },
    {
        "q": "Although it became their signature song, what position did 'California Dreamin'' peak at on the Billboard Hot 100 in 1966?",
        "correct": "#4",
        "wrong": ["#1", "#2", "#8"],
        "d": 2
    },
    {
        "q": "What 1967 song by The Box Tops featured 16-year-old Alex Chilton on gravelly lead vocals and spent four weeks at #1?",
        "correct": "The Letter",
        "wrong": ["Cry Like a Baby", "Soul Deep", "Neon Rainbow"],
        "d": 2
    },
    {
        "q": "Which Tommy James and the Shondells track hit #1 in 1969 after James reportedly saw a neon sign for Mutual of New York while standing on a roof?",
        "correct": "Mony Mony",
        "wrong": ["Crimson and Clover", "I Think We're Alone Now", "Crystal Blue Persuasion"],
        "d": 3
    },
    {
        "q": "What 1968 Tommy James and the Shondells #1 hit featured innovative tremolo vocal effects applied to the singer's microphone?",
        "correct": "Crimson and Clover",
        "wrong": ["Mony Mony", "Mirage", "Draggin' the Line"],
        "d": 2
    },
    {
        "q": "Which 1967 single by Lulu spent five weeks at #1 on the Billboard Hot 100 and was the title song of a film starring Sidney Poitier?",
        "correct": "To Sir with Love",
        "wrong": ["Georgy Girl", "A Groovy Kind of Love", "The Look of Love"],
        "d": 2
    },
    {
        "q": "Which Bobbie Gentry Southern gothic mystery song knocked The Beatles' 'All You Need Is Love' from #1 in August 1967?",
        "correct": "Ode to Billie Joe",
        "wrong": ["Fancy", "Harper Valley P.T.A.", "Me and Bobby McGee"],
        "d": 2
    },
    {
        "q": "In Bobbie Gentry's #1 hit 'Ode to Billie Joe', from which structure did Billie Joe McAllister jump?",
        "correct": "Tallahatchie Bridge",
        "wrong": ["Pecan Bayou Bridge", "Mississippi River Bridge", "Choctaw County Trestle"],
        "d": 1
    },
    {
        "q": "What Jeannie C. Riley country-pop song spent three weeks at #1 in 1968, written by Tom T. Hall about small-town hypocrisy?",
        "correct": "Harper Valley P.T.A.",
        "wrong": ["Stand by Your Man", "Coal Miner's Daughter", "Rose Garden"],
        "d": 3
    },

    # 51-60
    {
        "q": "What was Ray Charles' first #1 single on the Billboard Hot 100, which won four Grammy Awards in 1960?",
        "correct": "Georgia on My Mind",
        "wrong": ["Hit the Road Jack", "I Can't Stop Loving You", "What'd I Say"],
        "d": 2
    },
    {
        "q": "Which 1962 country-western crossover by Ray Charles topped the Billboard Hot 100 for five straight weeks?",
        "correct": "I Can't Stop Loving You",
        "wrong": ["Born to Lose", "You Don't Know Me", "Crying Time"],
        "d": 2
    },
    {
        "q": "Which girl group hit #1 in 1963 with 'He's So Fine', a song later judged in court to have been unconsciously copied in George Harrison's 'My Sweet Lord'?",
        "correct": "The Chiffons",
        "wrong": ["The Crystals", "The Ronettes", "The Shirelles"],
        "d": 2
    },
    {
        "q": "What was the title of The Beatles' first single to officially reach #1 on the US Billboard Hot 100, doing so in February 1964?",
        "correct": "I Want to Hold Your Hand",
        "wrong": ["She Loves You", "Please Please Me", "Love Me Do"],
        "d": 1
    },
    {
        "q": "Which Beatles song holds the distinction of having the longest run at #1 on the Hot 100 of any Beatles single, spending 9 weeks at the top in 1968?",
        "correct": "Hey Jude",
        "wrong": ["I Want to Hold Your Hand", "Get Back", "Yesterday"],
        "d": 2
    },
    {
        "q": "What B-side accompanied The Beatles' 1968 chart-topper 'Hey Jude' and reached #4 on the Billboard Hot 100 in its own right?",
        "correct": "Revolution",
        "wrong": ["Don't Let Me Down", "Lady Madonna", "The Inner Light"],
        "d": 2
    },
    {
        "q": "What 1965 folk-rock classic by The Byrds, adapted from the Book of Ecclesiastes by Pete Seeger, hit #1 on the Hot 100?",
        "correct": "Turn! Turn! Turn! (To Everything There Is a Season)",
        "wrong": ["Mr. Tambourine Man", "Eight Miles High", "So You Want to Be a Rock 'n' Roll Star"],
        "d": 2
    },
    {
        "q": "The Byrds reached #1 on the Billboard Hot 100 earlier in 1965 with their electric cover of which Bob Dylan composition?",
        "correct": "Mr. Tambourine Man",
        "wrong": ["All Along the Watchtower", "Blowin' in the Wind", "It's All Over Now, Baby Blue"],
        "d": 1
    },
    {
        "q": "Which British duo hit #1 on the Hot 100 in 1964 with 'A World Without Love', written by Paul McCartney but credited to Lennon–McCartney?",
        "correct": "Peter and Gordon",
        "wrong": ["Chad & Jeremy", "The Walker Brothers", "The Tremeloes"],
        "d": 3
    },
    {
        "q": "Which Young Rascals song reached #1 on the Billboard Hot 100 in 1966, encouraging listeners to take it easy?",
        "correct": "Good Lovin'",
        "wrong": ["Groovin'", "A Beautiful Morning", "People Got to Be Free"],
        "d": 2
    },

    # 61-70
    {
        "q": "What The Rascals anti-violence anthem, inspired by the assassinations of Martin Luther King Jr. and Robert F. Kennedy, topped the charts for five weeks in 1968?",
        "correct": "People Got to Be Free",
        "wrong": ["Groovin'", "How Can I Be Sure", "A Girl Like You"],
        "d": 3
    },
    {
        "q": "Which 1964 Louis Armstrong single knocked The Beatles off the #1 spot after their 14-week streak at the top?",
        "correct": "Hello, Dolly!",
        "wrong": ["What a Wonderful World", "Mack the Knife", "Dream a Little Dream of Me"],
        "d": 2
    },
    {
        "q": "How old was Louis Armstrong when 'Hello, Dolly!' hit #1 in 1964, making him the oldest artist to top the Hot 100 at that time?",
        "correct": "62",
        "wrong": ["58", "67", "71"],
        "d": 3
    },
    {
        "q": "Which Motown songwriting and production trio was behind dozens of Hot 100 Top 5 hits for The Supremes, Four Tops, and Martha and the Vandellas?",
        "correct": "Holland–Dozier–Holland",
        "wrong": ["Ashford & Simpson", "Gamble & Huff", "Whitfield & Strong"],
        "d": 1
    },
    {
        "q": "Which Four Tops single knocked The Beatles' 'Reach Out I'll Be There' predecessor off the charts and became their second Hot 100 #1 in 1966?",
        "correct": "Reach Out I'll Be There",
        "wrong": ["I Can't Help Myself (Sugar Pie Honey Bunch)", "Bernadette", "Standing in the Shadows of Love"],
        "d": 2
    },
    {
        "q": "What Four Tops hit was their first Billboard Hot 100 #1 single, spending two non-consecutive weeks at the top in June 1965?",
        "correct": "I Can't Help Myself (Sugar Pie Honey Bunch)",
        "wrong": ["Reach Out I'll Be There", "Baby I Need Your Loving", "It's the Same Old Song"],
        "d": 2
    },
    {
        "q": "Which 1966 Simon & Garfunkel song hit #1 on the Hot 100 after producer Tom Wilson overdubbed electric instruments onto an acoustic recording without their knowledge?",
        "correct": "The Sound of Silence",
        "wrong": ["Homeward Bound", "I Am a Rock", "Scarborough Fair"],
        "d": 2
    },
    {
        "q": "Which song gave Johnny Cash his highest-charting Billboard Hot 100 hit when it reached #2 in 1969, recorded live at San Quentin State Prison?",
        "correct": "A Boy Named Sue",
        "wrong": ["Folsom Prison Blues", "Ring of Fire", "I Walk the Line"],
        "d": 2
    },
    {
        "q": "Who wrote Johnny Cash's comedic Top 5 hit 'A Boy Named Sue'?",
        "correct": "Shel Silverstein",
        "wrong": ["Kris Kristofferson", "Waylon Jennings", "Tom T. Hall"],
        "d": 2
    },
    {
        "q": "What was the final Billboard Hot 100 #1 single of the 1960s decade, occupying the summit in the final week of December 1969?",
        "correct": "Someday We'll Be Together by Diana Ross & The Supremes",
        "wrong": ["Raindrops Keep Fallin' on My Head by Billy Joe Thomas", "Leaving on a Jet Plane by Peter, Paul and Mary", "Na Na Hey Hey Kiss Him Goodbye by Steam"],
        "d": 3
    },

    # 71-80
    {
        "q": "Which 1969 track by Steam hit #1 and went on to become one of the most famous taunting chants in North American sports stadiums?",
        "correct": "Na Na Hey Hey Kiss Him Goodbye",
        "wrong": ["We Will Rock You", "Y.M.C.A.", "Shout"],
        "d": 1
    },
    {
        "q": "What Peter, Paul and Mary hit, written by John Denver, reached #1 on the Billboard Hot 100 in December 1969?",
        "correct": "Leaving on a Jet Plane",
        "wrong": ["Blowin' in the Wind", "Puff, the Magic Dragon", "Don't Think Twice, It's All Right"],
        "d": 2
    },
    {
        "q": "Which Burt Bacharach and Hal David composition, featured in 'Butch Cassidy and the Sundance Kid', hit #1 for B.J. Thomas in January 1970?",
        "correct": "Raindrops Keep Fallin' on My Head",
        "wrong": ["Hooked on a Feeling", "I'll Never Fall in Love Again", "What the World Needs Now Is Love"],
        "d": 1
    },
    {
        "q": "Which 1967 song by The Association hit #1 on the Billboard Hot 100, opening with the lyrics 'Along comes Mary'?",
        "correct": "Windy",
        "wrong": ["Cherish", "Never My Love", "Along Comes Mary"],
        "d": 3
    },
    {
        "q": "What 1966 ballad was The Association's very first Billboard Hot 100 #1 hit?",
        "correct": "Cherish",
        "wrong": ["Windy", "Never My Love", "Requiem for the Masses"],
        "d": 2
    },
    {
        "q": "Which 1968 single by Hugh Masekela reached #1 on the Hot 100, popularizing South African instrumental pop in the US?",
        "correct": "Grazing in the Grass",
        "wrong": ["Soulful Strut", "The 'In' Crowd", "Soul Finger"],
        "d": 3
    },
    {
        "q": "What instrument did Hugh Masekela play on his 1968 #1 instrumental hit 'Grazing in the Grass'?",
        "correct": "Flugelhorn",
        "wrong": ["Saxophone", "Trombone", "Electric organ"],
        "d": 3
    },
    {
        "q": "Which 1961 single by Chubby Checker holds the record as the only song in Billboard history to reach #1 in two separate chart runs?",
        "correct": "The Twist",
        "wrong": ["Let's Twist Again", "Limbo Rock", "Pony Time"],
        "d": 1
    },
    {
        "q": "In which two years did Chubby Checker's 'The Twist' reach #1 on the Billboard Hot 100?",
        "correct": "1960 and 1962",
        "wrong": ["1959 and 1961", "1961 and 1963", "1960 and 1964"],
        "d": 2
    },
    {
        "q": "Which instrument provides the iconic opening riff of The Rolling Stones' 1966 #1 hit 'Paint It Black'?",
        "correct": "Sitar",
        "wrong": ["Banjo", "12-string guitar", "Harpsichord"],
        "d": 2
    },

    # 81-90
    {
        "q": "Which Rolling Stones band member played the sitar on their 1966 Billboard Hot 100 #1 single 'Paint It Black'?",
        "correct": "Brian Jones",
        "wrong": ["Keith Richards", "Mick Taylor", "Bill Wyman"],
        "d": 2
    },
    {
        "q": "What 1968 hit by Cream reached #5 on the Billboard Hot 100, featuring a memorable guitar riff played by Eric Clapton?",
        "correct": "Sunshine of Your Love",
        "wrong": ["White Room", "Crossroads", "Badge"],
        "d": 2
    },
    {
        "q": "Which Jimi Hendrix single was his only Top 20 entry on the US Billboard Hot 100, peaking at #20 in 1968?",
        "correct": "All Along the Watchtower",
        "wrong": ["Purple Haze", "Foxy Lady", "Hey Joe"],
        "d": 2
    },
    {
        "q": "Jimi Hendrix's 1968 album 'Electric Ladyland' achieved what peak position on the Billboard 200 album chart?",
        "correct": "#1",
        "wrong": ["#3", "#5", "#10"],
        "d": 2
    },
    {
        "q": "Which Dionne Warwick single, written by Burt Bacharach and Hal David, peaked at #4 on the Billboard Hot 100 in 1968?",
        "correct": "Do You Know the Way to San Jose",
        "wrong": ["Walk On By", "I Say a Little Prayer", "Theme from Valley of the Dolls"],
        "d": 2
    },
    {
        "q": "Who sang the female co-lead vocal with Frank Sinatra on the 1967 father-daughter duet 'Somethin' Stupid', which reached #1 on the Hot 100?",
        "correct": "Nancy Sinatra",
        "wrong": ["Tina Sinatra", "Liza Minnelli", "Barbra Streisand"],
        "d": 1
    },
    {
        "q": "Nancy Sinatra hit #1 on the Billboard Hot 100 in early 1966 with which assertive Lee Hazlewood-penned song?",
        "correct": "These Boots Are Made for Walkin'",
        "wrong": ["Sugar Town", "Bang Bang (My Baby Shot Me Down)", "Some Velvet Morning"],
        "d": 1
    },
    {
        "q": "Which session bassist played the iconic descending double bass line in Nancy Sinatra's 'These Boots Are Made for Walkin''?",
        "correct": "Chuck Berghofer",
        "wrong": ["Carol Kaye", "James Jamerson", "Donald 'Duck' Dunn"],
        "d": 3
    },
    {
        "q": "Which famous collective of Los Angeles session musicians played on dozens of Top 5 hits including 'Good Vibrations', 'Mr. Tambourine Man', and 'These Boots Are Made for Walkin''?",
        "correct": "The Wrecking Crew",
        "wrong": ["The Funk Brothers", "The Swampers", "The Memphis Boys"],
        "d": 1
    },
    {
        "q": "What was the name of the Detroit house band that played uncredited on nearly every Motown Top 5 hit from 1959 through 1972?",
        "correct": "The Funk Brothers",
        "wrong": ["The Wrecking Crew", "The Muscle Shoals Horns", "Booker T. & the M.G.'s"],
        "d": 1
    },

    # 91-100
    {
        "q": "Which bass guitarist was the primary anchor of The Funk Brothers on Motown classics like 'My Girl' and 'I Heard It Through the Grapevine'?",
        "correct": "James Jamerson",
        "wrong": ["Bob Babbitt", "Donald 'Duck' Dunn", "Leland Sklar"],
        "d": 2
    },
    {
        "q": "Which Stax Records house band had a #3 Billboard Hot 100 instrumental hit in 1962 with 'Green Onions'?",
        "correct": "Booker T. & the M.G.'s",
        "wrong": ["The Bar-Kays", "The Mar-Keys", "The Meters"],
        "d": 2
    },
    {
        "q": "What 1966 ballad by Percy Sledge was the first soul record recorded in Muscle Shoals to reach #1 on the Hot 100?",
        "correct": "When a Man Loves a Woman",
        "wrong": ["Warm and Tender Love", "Take Time to Know Her", "It Tears Me Up"],
        "d": 2
    },
    {
        "q": "What 1968 Billboard Hot 100 #1 hit was written by John Lennon and Paul McCartney and was released as Apple Records' first single?",
        "correct": "Hey Jude",
        "wrong": ["Lady Madonna", "Get Back", "Let It Be"],
        "d": 2
    },
    {
        "q": "Which 1969 Beatles song was credited to 'The Beatles with Billy Preston', making Preston the only guest musician to receive label credit on a Beatles single?",
        "correct": "Get Back",
        "wrong": ["Something", "Let It Be", "The Ballad of John and Yoko"],
        "d": 2
    },
    {
        "q": "Which song written by George Harrison reached #1 on the Billboard Hot 100 as a double A-side with 'Come Together' in late 1969?",
        "correct": "Something",
        "wrong": ["Here Comes the Sun", "While My Guitar Gently Weeps", "Taxman"],
        "d": 1
    },
    {
        "q": "What 1969 single by The 5th Dimension spent three weeks at #1 on the Hot 100 and was written by Laura Nyro about marriage?",
        "correct": "Wedding Bell Blues",
        "wrong": ["Stoned Soul Picnic", "Blowing Away", "Save the Country"],
        "d": 3
    },
    {
        "q": "Which singer-songwriter topped the Billboard Hot 100 for three weeks in 1968 with 'Honey', an emotional ballad about a deceased spouse?",
        "correct": "Bobby Goldsboro",
        "wrong": ["Bobby Vinton", "Billy Joe Thomas", "Glen Campbell"],
        "d": 3
    },
    {
        "q": "Which Glen Campbell song peaked at #3 on the Billboard Hot 100 in 1968, written by Jimmy Webb about an overworked telephone lineman?",
        "correct": "Wichita Lineman",
        "wrong": ["By the Time I Get to Phoenix", "Galveston", "Rhinestone Cowboy"],
        "d": 2
    },
    {
        "q": "Who wrote Glen Campbell's Top 5 hits 'Wichita Lineman' and 'Galveston', as well as the Richard Harris epic 'MacArthur Park'?",
        "correct": "Jimmy Webb",
        "wrong": ["Burt Bacharach", "Paul Williams", "Randy Newman"],
        "d": 2
    }
]

if __name__ == "__main__":
    formatted = assemble_batch(QUESTIONS, 1)
    save_batch(formatted, 1)
