import sys
import os
sys.path.append(os.path.dirname(__file__))
from utils import assemble_batch, save_batch

QUESTIONS = [
    # 1-10
    {
        "q": "Which Swedish songwriter and producer has written or co-written over 25 Billboard Hot 100 #1 hits, trailing only Paul McCartney and John Lennon?",
        "correct": "Max Martin",
        "wrong": ["Rami Yacoub", "Denniz Pop", "Shellback"],
        "d": 1
    },
    {
        "q": "What legendary Stockholm studio was the creative home where Max Martin, Denniz Pop, and Kristian Lundin forged the late-1990s teen-pop sound?",
        "correct": "Cheiron Studios",
        "wrong": ["Polar Studios", "Abba Sound Studios", "Stockholm Hit Factory"],
        "d": 2
    },
    {
        "q": "What was the very first Billboard Hot 100 #1 single co-written and produced by Max Martin?",
        "correct": "...Baby One More Time by Britney Spears (1999)",
        "wrong": ["Quit Playing Games (with My Heart) by Backstreet Boys", "It's Gonna Be Me by *NSYNC", "Since U Been Gone by Kelly Clarkson"],
        "d": 2
    },
    {
        "q": "Which Swedish producer and frequent Max Martin collaborator co-wrote Taylor Swift hits like 'Shake It Off', 'Blank Space', and 'Bad Blood'?",
        "correct": "Shellback (Johan Schuster)",
        "wrong": ["Bloodshy", "Avicii", "Carl Falk"],
        "d": 2
    },
    {
        "q": "Which legendary producer arranged and produced Michael Jackson's blockbuster trilogy of albums: 'Off the Wall', 'Thriller', and 'Bad'?",
        "correct": "Quincy Jones",
        "wrong": ["Berry Gordy", "Rod Temperton", "Babyface"],
        "d": 1
    },
    {
        "q": "Which British songwriter wrote the title track to Michael Jackson's 'Thriller' as well as 'Rock with You' and 'Off the Wall'?",
        "correct": "Rod Temperton",
        "wrong": ["Bernie Taupin", "Paul Temperton", "Steve Porcaro"],
        "d": 2
    },
    {
        "q": "Which iconic producer co-founded Def Jam Recordings in his NYU dorm room and produced historic albums for Run-DMC, Beastie Boys, and Public Enemy?",
        "correct": "Rick Rubin",
        "wrong": ["Russell Simmons", "Jimmy Iovine", "Clive Davis"],
        "d": 1
    },
    {
        "q": "Which rock band collaborated with Rick Rubin at 'The Mansion' in Laurel Canyon to record their 1991 masterpiece 'Blood Sugar Sex Magik'?",
        "correct": "Red Hot Chili Peppers",
        "wrong": ["Rage Against the Machine", "Jane's Addiction", "System of a Down"],
        "d": 2
    },
    {
        "q": "Which Virginia Beach producer defined the late 1990s and 2000s R&B sound with his syncopated percussion, bird chirps, and stuttering beats?",
        "correct": "Timbaland",
        "wrong": ["Swizz Beatz", "Scott Storch", "Darkchild"],
        "d": 1
    },
    {
        "q": "Which close friend and collaborator released groundbreaking albums with Timbaland, including 'Supa Dupa Fly' and 'Miss E... So Addictive'?",
        "correct": "Missy Elliott",
        "wrong": ["Aaliyah", "Da Brat", "Lil' Kim"],
        "d": 1
    },

    # 11-20
    {
        "q": "What is the name of the acclaimed production duo formed by Pharrell Williams and Chad Hugo?",
        "correct": "The Neptunes",
        "wrong": ["Organized Noize", "Cool & Dre", "Stargate"],
        "d": 1
    },
    {
        "q": "Which 2002 Justin Timberlake debut solo single was produced by The Neptunes and reached #3 on the Billboard Hot 100?",
        "correct": "Like I Love You",
        "wrong": ["Cry Me a River", "Rock Your Body", "Señorita"],
        "d": 2
    },
    {
        "q": "Which recording technique developed by Phil Spector featured multiple instruments playing the same parts in unison in an echo chamber?",
        "correct": "Wall of Sound",
        "wrong": ["Gated Reverb", "Ping-Pong Stereo", "Tape Saturation"],
        "d": 1
    },
    {
        "q": "At which historic Hollywood recording studio did Phil Spector record his famous 'Wall of Sound' hits with The Wrecking Crew?",
        "correct": "Gold Star Studios",
        "wrong": ["Sunset Sound", "Capitol Studios", "Sound City Studios"],
        "d": 2
    },
    {
        "q": "Who was often referred to as the 'Fifth Beatle' for producing, arranging, and conducting virtually all of The Beatles' recordings?",
        "correct": "George Martin",
        "wrong": ["Brian Epstein", "Neil Aspinall", "Mal Evans"],
        "d": 1
    },
    {
        "q": "At which iconic London studio did The Beatles record almost all of their albums, including the 1969 LP named after the studio's street?",
        "correct": "Abbey Road Studios (EMI Studios)",
        "wrong": ["Olympic Studios", "Trident Studios", "Decca Studios"],
        "d": 1
    },
    {
        "q": "Which Beach Boys mastermind wrote, arranged, and produced the acclaimed 1966 album 'Pet Sounds'?",
        "correct": "Brian Wilson",
        "wrong": ["Mike Love", "Carl Wilson", "Dennis Wilson"],
        "d": 1
    },
    {
        "q": "Which former members of The Time founded Flyte Tyme Productions and produced numerous #1 hits for Janet Jackson?",
        "correct": "Jimmy Jam and Terry Lewis",
        "wrong": ["L.A. Reid and Babyface", "Teddy Riley and Gene Griffin", "Darryl Simmons and Kayo"],
        "d": 1
    },
    {
        "q": "Which British synth-pop group topped the Billboard Hot 100 in 1986 with 'Human', written and produced by Jimmy Jam and Terry Lewis?",
        "correct": "The Human League",
        "wrong": ["Heaven 17", "New Order", "Orchestral Manoeuvres in the Dark"],
        "d": 2
    },
    {
        "q": "Which record label founded by L.A. Reid and Babyface launched the careers of TLC, Toni Braxton, and Usher in the 1990s?",
        "correct": "LaFace Records",
        "wrong": ["Bad Boy Records", "So So Def Recordings", "Uptown Records"],
        "d": 1
    },

    # 21-30
    {
        "q": "Which songwriter and producer holds the record for winning the Grammy Award for Producer of the Year, Non-Classical four times in the 1990s?",
        "correct": "Babyface (Kenneth Edmonds)",
        "wrong": ["David Foster", "Quincy Jones", "Don Was"],
        "d": 2
    },
    {
        "q": "Which Norwegian production duo, consisting of Mikkel Storleer Eriksen and Tor Erik Hermansen, produced #1 hits for Rihanna, Ne-Yo, and Beyoncé?",
        "correct": "Stargate",
        "wrong": ["Bloodshy & Avant", "Deep Dish", "Espionage"],
        "d": 2
    },
    {
        "q": "Which Bleachers frontman and fun. guitarist has produced Album of the Year Grammy winners for Taylor Swift, Lana Del Rey, and Lorde?",
        "correct": "Jack Antonoff",
        "wrong": ["Dan Nigro", "Greg Kurstin", "Ariel Rechtshaid"],
        "d": 1
    },
    {
        "q": "What historic converted house in Detroit served as Motown Records' headquarters and recording studio from 1959 to 1968?",
        "correct": "Hitsville U.S.A.",
        "wrong": ["Soulsville U.S.A.", "Rhythm City", "Motown Manor"],
        "d": 1
    },
    {
        "q": "What nickname was given to the tiny converted garage at Hitsville U.S.A. where the Funk Brothers tracked Motown's legendary hits?",
        "correct": "Studio A (The Snakepit)",
        "wrong": ["The Echo Chamber", "The Engine Room", "The Hit Factory"],
        "d": 2
    },
    {
        "q": "Which Memphis studio, operated by Sam Phillips, was the birthplace of rock and roll where Elvis Presley, Johnny Cash, and Jerry Lee Lewis first recorded?",
        "correct": "Sun Studio",
        "wrong": ["Stax Studios", "American Sound Studio", "Ardent Studios"],
        "d": 1
    },
    {
        "q": "Which Sheffield, Alabama studio and its rhythm section 'The Swampers' recorded classic Top 5 hits for Aretha Franklin, Paul Simon, and The Rolling Stones?",
        "correct": "Muscle Shoals Sound Studio",
        "wrong": ["Sun Studio", "Stax Studios", "Royal Studios"],
        "d": 1
    },
    {
        "q": "Which Greenwich Village recording studio was commissioned and built by Jimi Hendrix shortly before his death in 1970?",
        "correct": "Electric Lady Studios",
        "wrong": ["The Record Plant", "The Hit Factory", "Power Station"],
        "d": 1
    },
    {
        "q": "Which Van Nuys studio was renowned for its custom Neve 8028 mixing console, where Fleetwood Mac recorded 'Rumours' and Nirvana recorded 'Nevermind'?",
        "correct": "Sound City Studios",
        "wrong": ["Sunset Sound", "Wally Heider Studios", "Conway Recording"],
        "d": 2
    },
    {
        "q": "Which Hollywood studio, located on Sunset Boulevard, hosted landmark recording sessions for The Beach Boys' 'Pet Sounds' and Prince's 'Purple Rain'?",
        "correct": "Sunset Sound Recorders",
        "wrong": ["Capitol Studios", "Village Studios", "Larrabee Studios"],
        "d": 2
    },

    # 31-40
    {
        "q": "What 1985 synth-pop single by Norwegian band A-ha topped the Billboard Hot 100, celebrated for its pencil-sketch rotoscoped music video?",
        "correct": "Take On Me",
        "wrong": ["The Sun Always Shines on T.V.", "Hunting High and Low", "Cry Wolf"],
        "d": 1
    },
    {
        "q": "Which music video holds the record as the most played video in MTV history, winning nine MTV Video Music Awards in 1987?",
        "correct": "Sledgehammer by Peter Gabriel",
        "wrong": ["Thriller by Michael Jackson", "Take On Me by A-ha", "Smells Like Teen Spirit by Nirvana"],
        "d": 1
    },
    {
        "q": "Who directed Michael Jackson's groundbreaking 14-minute cinematic music video for 'Thriller' in 1983?",
        "correct": "John Landis",
        "wrong": ["Martin Scorsese", "Steven Spielberg", "George Lucas"],
        "d": 1
    },
    {
        "q": "Which acclaimed director directed Michael Jackson's 18-minute short-film music video for his 1987 #1 hit 'Bad'?",
        "correct": "Martin Scorsese",
        "wrong": ["Francis Ford Coppola", "Brian De Palma", "Spike Lee"],
        "d": 2
    },
    {
        "q": "Which young actor made his screen acting debut in Michael Jackson's music video for 'Bad' as a rival gang member named Mini Max?",
        "correct": "Wesley Snipes",
        "wrong": ["Denzel Washington", "Laurence Fishburne", "Giancarlo Esposito"],
        "d": 2
    },
    {
        "q": "Which 1992 Guns N' Roses epic power ballad reached #3 on the Hot 100, accompanied by a lavish high-budget video featuring Stephanie Seymour?",
        "correct": "November Rain",
        "wrong": ["Don't Cry", "Estranged", "Civil War"],
        "d": 1
    },
    {
        "q": "Which 1987 Suzanne Vega a cappella song about a child was remixed by British electronic duo DNA in 1990, hitting #5 on the Billboard Hot 100?",
        "correct": "Tom's Diner",
        "wrong": ["Luka", "Marlene on the Wall", "Left of Center"],
        "d": 2
    },
    {
        "q": "Why is Suzanne Vega's recording of 'Tom's Diner' famous in computer audio history?",
        "correct": "Karlheinz Brandenburg used it as the primary audio reference to fine-tune the MP3 compression algorithm",
        "wrong": ["It was the first digital track encoded onto a CD-ROM", "It was the first ringtone sold on mobile phones", "It was the first file uploaded to Napster"],
        "d": 2
    },
    {
        "q": "Which 1981 soft rock single by Phil Collins featured the famous gated reverb drum sound engineered by Hugh Padgham?",
        "correct": "In the Air Tonight",
        "wrong": ["Against All Odds", "I Don't Care Anymore", "You Can't Hurry Love"],
        "d": 1
    },
    {
        "q": "Which 1980 Peter Gabriel album's opening track 'Intruder' was the first recording where Hugh Padgham and Gabriel discovered the gated reverb drum sound?",
        "correct": "Peter Gabriel (Melt)",
        "wrong": ["Security", "So", "Us"],
        "d": 3
    },

    # 41-50
    {
        "q": "Which 1974 David Bowie soul track, featuring John Lennon on backing guitar, reached #1 on the Billboard Hot 100?",
        "correct": "Fame",
        "wrong": ["Young Americans", "Golden Years", "Station to Station"],
        "d": 2
    },
    {
        "q": "Which British producer produced The Clash's 'Combat Rock', including their Top 10 Hot 100 hit 'Rock the Casbah'?",
        "correct": "Glyn Johns",
        "wrong": ["Mickie Most", "Steve Lillywhite", "Joe Meek"],
        "d": 3
    },
    {
        "q": "Which legendary sound engineer and producer engineered Pink Floyd's 'The Dark Side of the Moon' and The Beatles' 'Abbey Road'?",
        "correct": "Alan Parsons",
        "wrong": ["Geoff Emerick", "Ken Scott", "Norman Smith"],
        "d": 2
    },
    {
        "q": "What Alan Parsons Project instrumental track from 1982 became famous worldwide as the arena entrance music for the Chicago Bulls in the 1990s?",
        "correct": "Sirius",
        "wrong": ["Eye in the Sky", "Time", "Games People Play"],
        "d": 1
    },
    {
        "q": "Which Alan Parsons Project ballad reached #3 on the Billboard Hot 100 in autumn 1982?",
        "correct": "Eye in the Sky",
        "wrong": ["Time", "Don't Answer Me", "Prime Time"],
        "d": 2
    },
    {
        "q": "Which disco producer, known as the 'Father of Disco', produced Donna Summer's 'I Feel Love' using entirely electronic synthesizers in 1977?",
        "correct": "Giorgio Moroder",
        "wrong": ["Nile Rodgers", "Jacques Morali", "Pete Bellotte"],
        "d": 1
    },
    {
        "q": "Which analog modular synthesizer did Giorgio Moroder use to create the mesmerizing sequenced bassline of Donna Summer's 'I Feel Love'?",
        "correct": "Moog modular synthesizer",
        "wrong": ["Roland TB-303", "Korg MS-20", "ARP 2600"],
        "d": 2
    },
    {
        "q": "Which David Bowie single reached #1 on the Billboard Hot 100 in 1983, co-produced by Nile Rodgers of Chic?",
        "correct": "Let's Dance",
        "wrong": ["Modern Love", "China Girl", "Blue Jean"],
        "d": 1
    },
    {
        "q": "Which blues-rock guitar virtuoso was hired by David Bowie and Nile Rodgers to play lead guitar on the 'Let's Dance' album?",
        "correct": "Stevie Ray Vaughan",
        "wrong": ["Eric Clapton", "Jeff Beck", "Robert Cray"],
        "d": 2
    },
    {
        "q": "Which Chic co-founder produced Madonna's landmark 1984 album 'Like a Virgin' and Duran Duran's #1 remix 'The Reflex'?",
        "correct": "Nile Rodgers",
        "wrong": ["Bernard Edwards", "Tony Thompson", "Shep Pettibone"],
        "d": 1
    },

    # 51-60
    {
        "q": "Which Philadelphia soul songwriting and production team created the 'Philadelphia Soul' sound for The O'Jays and Harold Melvin at PIR?",
        "correct": "Kenny Gamble and Leon Huff",
        "wrong": ["Holland-Dozier-Holland", "Ashford & Simpson", "McFadden & Whitehead"],
        "d": 2
    },
    {
        "q": "Which PIR instrumental track by MFSB featuring The Three Degrees topped the Billboard Hot 100 in 1974 as the theme to 'Soul Train'?",
        "correct": "TSOP (The Sound of Philadelphia)",
        "wrong": ["Love's Theme", "Pick Up the Pieces", "Express"],
        "d": 2
    },
    {
        "q": "Which Barry White orchestral instrumental reached #1 on the Billboard Hot 100 in early 1974, credited to The Love Unlimited Orchestra?",
        "correct": "Love's Theme",
        "wrong": ["Can't Get Enough of Your Love, Babe", "You're the First, the Last, My Everything", "I'm Gonna Love You Just a Little More Baby"],
        "d": 2
    },
    {
        "q": "Which 1974 single was Barry White's only solo #1 hit on the Billboard Hot 100?",
        "correct": "Can't Get Enough of Your Love, Babe",
        "wrong": ["You're the First, the Last, My Everything", "Never, Never Gonna Give Ya Up", "It's Ecstasy When You Lay Down Next to Me"],
        "d": 2
    },
    {
        "q": "Which British engineer and producer engineered The Beatles' 'Revolver' and 'Sgt. Pepper's Lonely Hearts Club Band' at Abbey Road?",
        "correct": "Geoff Emerick",
        "wrong": ["Norman Smith", "Alan Parsons", "Ken Scott"],
        "d": 3
    },
    {
        "q": "What Abbey Road innovation invented by Ken Townsend allowed automatic doubling of vocal tracks without singing twice?",
        "correct": "Artificial Double Tracking (ADT)",
        "wrong": ["Direct Injection (DI)", "Phasing flanger", "Tape loop echo"],
        "d": 3
    },
    {
        "q": "Which Tom Petty solo album peaked at #5 on the Billboard 200 in 1989, co-produced by Jeff Lynne of Electric Light Orchestra?",
        "correct": "Full Moon Fever",
        "wrong": ["Wildflowers", "Into the Great Wide Open", "Highway Companion"],
        "d": 2
    },
    {
        "q": "Which Tom Petty classic from 'Full Moon Fever' peaked at #7 on the Billboard Hot 100 in 1989, singing about vampires out in the valley?",
        "correct": "Free Fallin'",
        "wrong": ["I Won't Back Down", "Runnin' Down a Dream", "Yer So Bad"],
        "d": 1
    },
    {
        "q": "Which supergroup featuring George Harrison, Bob Dylan, Tom Petty, Roy Orbison, and Jeff Lynne reached #3 on the Billboard 200 in 1989?",
        "correct": "The Traveling Wilburys",
        "wrong": ["The Dirty Mac", "The Highwaymen", "Blind Faith"],
        "d": 1
    },
    {
        "q": "What was the highest-charting Billboard Hot 100 single by The Traveling Wilburys, reaching #22 in 1989?",
        "correct": "Handle with Care",
        "wrong": ["End of the Line", "Not Alone Any More", "She's My Baby"],
        "d": 2
    },

    # 61-70
    {
        "q": "Which Atlanta producer founded So So Def Recordings in 1993 and produced #1 hits for Kris Kross, Mariah Carey, and Usher?",
        "correct": "Jermaine Dupri",
        "wrong": ["Dallas Austin", "Organized Noize", "Lil Jon"],
        "d": 2
    },
    {
        "q": "Which 12-year-old rap duo had an eight-week #1 hit on the Billboard Hot 100 in 1992 with 'Jump', wearing their clothes backwards?",
        "correct": "Kris Kross",
        "wrong": ["Another Bad Creation", "Immature", "Da Youngsta's"],
        "d": 1
    },
    {
        "q": "Which rap duo's #1 hit 'Jump' was written and produced by an 19-year-old Jermaine Dupri?",
        "correct": "Kris Kross",
        "wrong": ["Kid 'n Play", "Tag Team", "Heavy D & the Boyz"],
        "d": 2
    },
    {
        "q": "Which Miami bass anthem by Tag Team reached #2 on the Billboard Hot 100 in 1993, chanting 'Whoomp! (There It Is)'?",
        "correct": "Whoomp! (There It Is)",
        "wrong": ["Whoot, There It Is", "Tootsee Roll", "C'mon N' Ride It (The Train)"],
        "d": 1
    },
    {
        "q": "Which Quad City DJ's dance track reached #3 on the Billboard Hot 100 in 1996, inviting listeners on a train ride?",
        "correct": "C'mon N' Ride It (The Train)",
        "wrong": ["Space Jam", "Tootsee Roll", "Whoomp! (There It Is)"],
        "d": 2
    },
    {
        "q": "What 1996 Quad City DJ's track served as the theme song for the Michael Jordan movie 'Space Jam', peaking at #37 on the Hot 100?",
        "correct": "Space Jam",
        "wrong": ["Fly Like an Eagle", "Hit 'Em High", "I Believe I Can Fly"],
        "d": 2
    },
    {
        "q": "Which producer produced Green Day's breakthrough 1994 punk album 'Dookie' and went on to produce their rock opera 'American Idiot'?",
        "correct": "Rob Cavallo",
        "wrong": ["Butch Vig", "Jerry Finn", "Brendan O'Brien"],
        "d": 2
    },
    {
        "q": "Which punk rock producer produced landmark 1990s and 2000s albums for Blink-182, Sum 41, and AFI before his untimely death in 2008?",
        "correct": "Jerry Finn",
        "wrong": ["Rob Cavallo", "Howard Benson", "Neal Avron"],
        "d": 3
    },
    {
        "q": "Which producer produced Nirvana's 1993 album 'In Utero' at Pachyderm Studio in Minnesota, known for his raw, unpolished drum sound?",
        "correct": "Steve Albini",
        "wrong": ["Butch Vig", "Jack Endino", "Scott Litt"],
        "d": 2
    },
    {
        "q": "Which producer produced R.E.M.'s multi-platinum albums 'Out of Time', 'Automatic for the People', and 'Monster'?",
        "correct": "Scott Litt",
        "wrong": ["Mitch Easter", "Don Dixon", "Joe Boyd"],
        "d": 3
    },

    # 71-80
    {
        "q": "Which R.E.M. mandolin-driven single reached #4 on the Billboard Hot 100 in 1991, winning two Grammy Awards?",
        "correct": "Losing My Religion",
        "wrong": ["Shiny Happy People", "Man on the Moon", "Everybody Hurts"],
        "d": 1
    },
    {
        "q": "Who directed the baroque, religious-inspired music video for R.E.M.'s 'Losing My Religion', winning six MTV Video Music Awards in 1991?",
        "correct": "Tarsem Singh",
        "wrong": ["David Fincher", "Mark Romanek", "Spike Jonze"],
        "d": 3
    },
    {
        "q": "Which music video director directed Madonna's 'Vogue', Aerosmith's 'Janie's Got a Gun', and went on to direct 'Fight Club' and 'Seven'?",
        "correct": "David Fincher",
        "wrong": ["Michael Bay", "David Kellogg", "Gore Verbinski"],
        "d": 2
    },
    {
        "q": "Which director directed the music videos for Nine Inch Nails' 'Closer', Fiona Apple's 'Criminal', and Michael & Janet Jackson's 'Scream'?",
        "correct": "Mark Romanek",
        "wrong": ["Hype Williams", "F. Gary Gray", "Paul Hunter"],
        "d": 2
    },
    {
        "q": "Michael and Janet Jackson's 1995 music video for 'Scream' was certified by Guinness World Records as what?",
        "correct": "The most expensive music video ever made at \$7 million",
        "wrong": ["The longest music video in history", "The first video shot in zero gravity", "The most visual effects shots in a video"],
        "d": 1
    },
    {
        "q": "What peak position did Michael and Janet Jackson's 'Scream' achieve on the Billboard Hot 100 in 1995, entering directly at #5?",
        "correct": "#5",
        "wrong": ["#1", "#2", "#8"],
        "d": 2
    },
    {
        "q": "Which music video director became legendary in the late 1990s for his signature fisheye lens, glossy colors, and videos for The Notorious B.I.G. and TLC?",
        "correct": "Hype Williams",
        "wrong": ["Director X", "Benny Boom", "Chris Robinson"],
        "d": 1
    },
    {
        "q": "Which 1999 TLC video directed by Bille Woodruff featured futuristic CGI silver outfits and spent weeks at #1 on MTV's 'Total Request Live'?",
        "correct": "No Scrubs",
        "wrong": ["Waterfalls", "Unpretty", "Creep"],
        "d": 2
    },
    {
        "q": "What daily MTV afternoon video countdown show hosted by Carson Daly heavily influenced Billboard Hot 100 sales and airplay from 1998 to 2008?",
        "correct": "Total Request Live (TRL)",
        "wrong": ["120 Minutes", "MTV Jams", "Headbangers Ball"],
        "d": 1
    },
    {
        "q": "Which boy band retired their video for 'I Want It That Way' after it spent 65 days at #1 on MTV's 'Total Request Live'?",
        "correct": "Backstreet Boys",
        "wrong": ["*NSYNC", "98 Degrees", "LFO"],
        "d": 2
    },

    # 81-90
    {
        "q": "Which British producer produced Amy Winehouse's 2006 masterpiece 'Back to Black' and Bruno Mars' #1 smash 'Uptown Funk'?",
        "correct": "Mark Ronson",
        "wrong": ["Paul Epworth", "Stuart Price", "Fraser T. Smith"],
        "d": 1
    },
    {
        "q": "Which Brooklyn funk and soul band served as the backing studio musicians on Amy Winehouse's 'Back to Black' album?",
        "correct": "The Dap-Kings",
        "wrong": ["The Budos Band", "Antibalas", "Menahan Street Band"],
        "d": 2
    },
    {
        "q": "What peak position did Amy Winehouse's signature autobiographical hit 'Rehab' reach on the US Billboard Hot 100 in 2007?",
        "correct": "#9",
        "wrong": ["#1", "#4", "#18"],
        "d": 2
    },
    {
        "q": "Which British producer co-wrote and produced Adele's Grammy-winning singles 'Rolling in the Deep' and 'Skyfall'?",
        "correct": "Paul Epworth",
        "wrong": ["Dan Wilson", "Greg Kurstin", "Fraser T. Smith"],
        "d": 2
    },
    {
        "q": "Which former Semisonic frontman co-wrote Adele's heart-wrenching #1 ballad 'Someone Like You' and The Chicks' 'Not Ready to Make Nice'?",
        "correct": "Dan Wilson",
        "wrong": ["John Shanks", "Max Martin", "Ryan Tedder"],
        "d": 2
    },
    {
        "q": "Which American songwriter and producer produced Kelly Clarkson's 'Stronger', Sia's 'Chandelier', and Adele's 'Hello'?",
        "correct": "Greg Kurstin",
        "wrong": ["Jack Antonoff", "Ricky Reed", "Benny Blanco"],
        "d": 2
    },
    {
        "q": "Which prolific producer and artist released 'Eastside' with Halsey and Khalid in 2018 after producing hits for Katy Perry and Justin Bieber?",
        "correct": "Benny Blanco",
        "wrong": ["Murda Beatz", "Cashmere Cat", "Finneas"],
        "d": 2
    },
    {
        "q": "Which Atlanta producer pioneered the 'trap sound' with Roland TR-808 sub-bass, producing for T.I., Gucci Mane, and Jeezy in the 2000s?",
        "correct": "Shawty Redd",
        "wrong": ["Zaytoven", "Lex Luger", "Mike WiLL Made-It"],
        "d": 3
    },
    {
        "q": "Which Atlanta producer's iconic producer tag asks 'If Young Metro don't trust you, I'm gon' shoot you'?",
        "correct": "Metro Boomin",
        "wrong": ["Wheezy", "Pierre Bourne", "Southside"],
        "d": 1
    },
    {
        "q": "Whose voice speaks the famous line 'If Young Metro don't trust you, I'm gon' shoot you' in Metro Boomin's producer tag?",
        "correct": "Future",
        "wrong": ["Drake", "21 Savage", "Travis Scott"],
        "d": 2
    },

    # 91-100
    {
        "q": "Which producer produced Rae Sremmurd's #1 hit 'Black Beatles', Miley Cyrus's 'We Can't Stop', and Beyoncé's 'Formation'?",
        "correct": "Mike WiLL Made-It",
        "wrong": ["Boi-1da", "Murda Beatz", "Mustard"],
        "d": 2
    },
    {
        "q": "Which West Coast producer is famous for his signature 'Mustard on the beat, ho' tag on hits for YG, Tyga, and Kendrick Lamar?",
        "correct": "Mustard (DJ Mustard)",
        "wrong": ["Hit-Boy", "London on da Track", "Tay Keith"],
        "d": 1
    },
    {
        "q": "Which Mustard-produced single by Kendrick Lamar debuted at #1 on the Billboard Hot 100 in May 2024?",
        "correct": "Not Like Us",
        "wrong": ["Like That", "Humble", "King Kunta"],
        "d": 1
    },
    {
        "q": "Which Toronto hip-hop producer has been Drake's primary sonic architect since 2009, co-founding OVO Sound?",
        "correct": "Noah '40' Shebib",
        "wrong": ["Boi-1da", "T-Minus", "Nineteen85"],
        "d": 2
    },
    {
        "q": "Which Canadian producer produced Drake's #1 hits 'God's Plan' and 'In My Feelings'?",
        "correct": "Cardo and Boi-1da",
        "wrong": ["Murda Beatz and Tay Keith", "Metro Boomin and Wheezy", "Hit-Boy and Mustard"],
        "d": 3
    },
    {
        "q": "Which 1974 song by Labi Siffre provided the opening rhythm and vocal hook for Eminem's breakthrough 1999 hit 'My Name Is'?",
        "correct": "I Got The...",
        "wrong": ["Bless the Telephone", "It Must Be Love", "Crying Laughing Loving Lying"],
        "d": 3
    },
    {
        "q": "Which Aerosmith classic was sampled as the chorus and guitar backbone for Eminem's 2002 #4 Hot 100 hit 'Sing for the Moment'?",
        "correct": "Dream On",
        "wrong": ["Sweet Emotion", "Walk This Way", "Mama Kin"],
        "d": 1
    },
    {
        "q": "Which 1971 Black Sabbath heavy metal ballad was covered and interpolated in Eminem's 2010 #1 hit 'Going Through Changes'?",
        "correct": "Changes",
        "wrong": ["Iron Man", "Paranoid", "War Pigs"],
        "d": 2
    },
    {
        "q": "Which Heart single from 1977 provided the electric guitar riff sample for Eminem's 2024 single 'Houdini'?",
        "correct": "Barracuda",
        "wrong": ["Magic Man", "Crazy on You", "Straight On"],
        "d": 2
    },
    {
        "q": "Which 1982 Steve Miller Band pop-rock hit provided the opening hook 'Abra-cadabra, I wanna reach out and grab ya' for Eminem's 2024 hit 'Houdini'?",
        "correct": "Abracadabra",
        "wrong": ["The Joker", "Fly Like an Eagle", "Rock'n Me"],
        "d": 1
    }
]

if __name__ == "__main__":
    formatted = assemble_batch(QUESTIONS, 10)
    save_batch(formatted, 10)
