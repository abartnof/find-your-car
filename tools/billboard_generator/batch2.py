import sys
import os
sys.path.append(os.path.dirname(__file__))
from utils import assemble_batch, save_batch

QUESTIONS = [
    # 1-10
    {
        "q": "Which Stevie Wonder funk classic from the 1972 album 'Talking Book' reached #1 on the Billboard Hot 100 with its distinctive Hohner Clavinet groove?",
        "correct": "Superstition",
        "wrong": ["Higher Ground", "Living for the City", "Sir Duke"],
        "d": 1
    },
    {
        "q": "What was Fleetwood Mac's only #1 single on the US Billboard Hot 100, written and sung by Stevie Nicks for the 1977 album 'Rumours'?",
        "correct": "Dreams",
        "wrong": ["Go Your Own Way", "Don't Stop", "Rhiannon"],
        "d": 1
    },
    {
        "q": "Fleetwood Mac's blockbuster 1977 album 'Rumours' spent how many non-consecutive weeks at #1 on the Billboard 200?",
        "correct": "31 weeks",
        "wrong": ["15 weeks", "24 weeks", "42 weeks"],
        "d": 2
    },
    {
        "q": "Which Elton John ballad, originally released in 1973 as a tribute to Marilyn Monroe, hit #1 on the Billboard Hot 100 in a revised 1997 version for Princess Diana?",
        "correct": "Candle in the Wind",
        "wrong": ["Rocket Man", "Goodbye Yellow Brick Road", "Tiny Dancer"],
        "d": 1
    },
    {
        "q": "What was Elton John's very first #1 single on the Billboard Hot 100, topping the chart in February 1973?",
        "correct": "Crocodile Rock",
        "wrong": ["Daniel", "Bennie and the Jets", "Your Song"],
        "d": 2
    },
    {
        "q": "Which 1971 Don McLean epic topped the Billboard Hot 100 for four weeks and famously lamented 'the day the music died'?",
        "correct": "American Pie",
        "wrong": ["Vincent", "Castles in the Air", "And I Love You So"],
        "d": 1
    },
    {
        "q": "In Don McLean's 'American Pie', which tragedy is referenced by the line 'the day the music died'?",
        "correct": "The 1959 plane crash that killed Buddy Holly, Ritchie Valens, and the Big Bopper",
        "wrong": ["The assassination of John F. Kennedy", "The breakup of The Beatles", "The Kent State shootings"],
        "d": 1
    },
    {
        "q": "Which Eagles album became the first album certified Platinum by the RIAA and became one of the best-selling albums in US history?",
        "correct": "Their Greatest Hits (1971–1975)",
        "wrong": ["Hotel California", "One of These Nights", "Desperado"],
        "d": 2
    },
    {
        "q": "Which Eagles classic reached #1 on the Billboard Hot 100 in May 1977, featuring an extended dual-guitar interplay between Don Felder and Joe Walsh?",
        "correct": "Hotel California",
        "wrong": ["New Kid in Town", "Life in the Fast Lane", "One of These Nights"],
        "d": 1
    },
    {
        "q": "What song by Queen topped the Billboard Hot 100 in early 1980 after Freddie Mercury wrote it in a bathtub in a rockabilly style?",
        "correct": "Crazy Little Thing Called Love",
        "wrong": ["Another One Bites the Dust", "Bohemian Rhapsody", "Killer Queen"],
        "d": 2
    },

    # 11-20
    {
        "q": "What peak position did Queen's iconic 'Bohemian Rhapsody' reach on the US Billboard Hot 100 during its original 1976 release?",
        "correct": "#9",
        "wrong": ["#1", "#2", "#5"],
        "d": 2
    },
    {
        "q": "Following its appearance in the 1992 film 'Wayne's World', what peak did Queen's 'Bohemian Rhapsody' reach on the Billboard Hot 100?",
        "correct": "#2",
        "wrong": ["#1", "#4", "#7"],
        "d": 2
    },
    {
        "q": "Which disco trio dominated 1977 and 1978 with six consecutive #1 singles on the Billboard Hot 100, including 'Stayin' Alive'?",
        "correct": "Bee Gees",
        "wrong": ["KC and the Sunshine Band", "The Trammps", "Earth, Wind & Fire"],
        "d": 1
    },
    {
        "q": "The soundtrack to which 1977 film spent 24 straight weeks at #1 on the Billboard 200 and won Album of the Year at the Grammys?",
        "correct": "Saturday Night Fever",
        "wrong": ["Grease", "Thank God It's Friday", "A Star Is Born"],
        "d": 1
    },
    {
        "q": "Which Bee Gees ballad from 'Saturday Night Fever' spent 17 weeks in the Billboard Hot 100 top 10, a record at the time?",
        "correct": "How Deep Is Your Love",
        "wrong": ["Stayin' Alive", "Night Fever", "More Than a Woman"],
        "d": 2
    },
    {
        "q": "Who was the youngest Gibb brother who scored three consecutive #1 Billboard Hot 100 hits in 1977 and 1978, including 'I Just Want to Be Your Everything'?",
        "correct": "Andy Gibb",
        "wrong": ["Barry Gibb", "Robin Gibb", "Maurice Gibb"],
        "d": 1
    },
    {
        "q": "Which Swedish pop group scored their sole Billboard Hot 100 #1 hit in April 1977 with 'Dancing Queen'?",
        "correct": "ABBA",
        "wrong": ["Ace of Base", "Roxette", "Boney M."],
        "d": 1
    },
    {
        "q": "Which Donna Summer track spent five weeks at #1 on the Billboard Hot 100 in 1979 and featured a rock guitar solo by Jeff 'Skunk' Baxter?",
        "correct": "Hot Stuff",
        "wrong": ["Bad Girls", "Last Dance", "Love to Love You Baby"],
        "d": 2
    },
    {
        "q": "Which album made Donna Summer the first female artist in the modern era to have three multi-week #1 hits from a single double-album?",
        "correct": "Bad Girls",
        "wrong": ["Once Upon a Time", "Live and More", "The Wanderer"],
        "d": 3
    },
    {
        "q": "What Gloria Gaynor disco anthem reached #1 on the Billboard Hot 100 in 1979 and was originally released as the B-side to a cover of 'Substitute'?",
        "correct": "I Will Survive",
        "wrong": ["Never Can Say Goodbye", "Honey Bee", "Reach Out, I'll Be There"],
        "d": 1
    },

    # 21-30
    {
        "q": "Which Pink Floyd single, featuring a children's choir singing 'We don't need no education', reached #1 on the Hot 100 in 1980?",
        "correct": "Another Brick in the Wall (Part II)",
        "wrong": ["Comfortably Numb", "Money", "Wish You Were Here"],
        "d": 1
    },
    {
        "q": "What 1973 Pink Floyd album spent a record-breaking 741 consecutive weeks on the Billboard 200 from 1973 to 1988?",
        "correct": "The Dark Side of the Moon",
        "wrong": ["The Wall", "Wish You Were Here", "Animals"],
        "d": 1
    },
    {
        "q": "Which Earth, Wind & Fire funk classic hit #1 on both the Billboard Hot 100 and Soul charts simultaneously in May 1975?",
        "correct": "Shining Star",
        "wrong": ["September", "Boogie Wonderland", "Sing a Song"],
        "d": 2
    },
    {
        "q": "What position did Earth, Wind & Fire's timeless celebratory party anthem 'September' peak at on the Billboard Hot 100 in 1979?",
        "correct": "#8",
        "wrong": ["#1", "#2", "#5"],
        "d": 2
    },
    {
        "q": "Which Billy Joel album won the Grammy for Album of the Year and topped the Billboard 200 for eight weeks in late 1978?",
        "correct": "52nd Street",
        "wrong": ["The Stranger", "Glass Houses", "Turnstiles"],
        "d": 2
    },
    {
        "q": "What 1977 Billy Joel ballad earned him two Grammy Awards and peaked at #3 on the Billboard Hot 100?",
        "correct": "Just the Way You Are",
        "wrong": ["Piano Man", "She's Always a Woman", "Scenes from an Italian Restaurant"],
        "d": 2
    },
    {
        "q": "What Rod Stewart track spent eight straight weeks at #1 on the Billboard Hot 100 in late 1976, becoming the top song of 1977?",
        "correct": "Tonight's the Night (Gonna Be Alright)",
        "wrong": ["Maggie May", "Da Ya Think I'm Sexy?", "You're in My Heart"],
        "d": 2
    },
    {
        "q": "Which Rod Stewart breakthrough single reached #1 in October 1971 as a double A-side backed with 'Reason to Believe'?",
        "correct": "Maggie May",
        "wrong": ["Tonight's the Night", "Stay with Me", "Mandolin Wind"],
        "d": 2
    },
    {
        "q": "Which Chic hit spent three separate stints at #1 on the Billboard Hot 100 in 1978-1979 and became Atlantic Records' biggest-selling single ever?",
        "correct": "Le Freak",
        "wrong": ["Good Times", "I Want Your Love", "Dance, Dance, Dance"],
        "d": 2
    },
    {
        "q": "The iconic bass line played by Bernard Edwards in Chic's 1979 #1 hit 'Good Times' was directly sampled in which groundbreaking rap song?",
        "correct": "Rapper's Delight by The Sugarhill Gang",
        "wrong": ["The Message by Grandmaster Flash", "Planet Rock by Afrika Bambaataa", "Push It by Salt-N-Pepa"],
        "d": 1
    },

    # 31-40
    {
        "q": "Which KC and the Sunshine Band dance anthem reached #1 on the Billboard Hot 100 in 1975, repeating the title phrase in the chorus?",
        "correct": "That's the Way (I Like It)",
        "wrong": ["Get Down Tonight", "(Shake, Shake, Shake) Shake Your Booty", "Boogie Shoes"],
        "d": 1
    },
    {
        "q": "Which sibling duo scored their first Billboard Hot 100 #1 in 1970 with '(They Long to Be) Close to You', written by Bacharach and David?",
        "correct": "The Carpenters",
        "wrong": ["Donny & Marie Osmond", "The Osmonds", "The Captain & Tennille"],
        "d": 1
    },
    {
        "q": "Which 1971 Marvin Gaye concept album spent over a year on the Billboard 200 and produced three Top 10 Hot 100 singles?",
        "correct": "What's Going On",
        "wrong": ["Let's Get It On", "I Want You", "Here, My Dear"],
        "d": 1
    },
    {
        "q": "Which seductive 1973 Marvin Gaye single stayed at #1 on the Billboard Hot 100 for two weeks, co-written with Ed Townsend?",
        "correct": "Let's Get It On",
        "wrong": ["What's Going On", "Mercy Mercy Me (The Ecology)", "Inner City Blues"],
        "d": 1
    },
    {
        "q": "Which Paul McCartney and Wings album topped the Billboard 200 in three separate runs during 1974?",
        "correct": "Band on the Run",
        "wrong": ["Venus and Mars", "Wings at the Speed of Sound", "Red Rose Speedway"],
        "d": 2
    },
    {
        "q": "What was the biggest Billboard Hot 100 hit of 1976, spending five weeks at #1 for Paul McCartney and Wings?",
        "correct": "Silly Love Songs",
        "wrong": ["Band on the Run", "My Love", "Listen to What the Man Said"],
        "d": 2
    },
    {
        "q": "Who was the only artist to share lead vocal credit on John Lennon's only Billboard Hot 100 #1 single during his lifetime, 'Whatever Gets You thru the Night'?",
        "correct": "Elton John",
        "wrong": ["Paul McCartney", "David Bowie", "Harry Nilsson"],
        "d": 2
    },
    {
        "q": "Which former Beatle was the first to score a solo Billboard Hot 100 #1 hit, doing so with 'My Sweet Lord' in December 1970?",
        "correct": "George Harrison",
        "wrong": ["Paul McCartney", "John Lennon", "Ringo Starr"],
        "d": 2
    },
    {
        "q": "George Harrison's 1970 triple LP that topped the Billboard 200 for seven weeks was titled what?",
        "correct": "All Things Must Pass",
        "wrong": ["Living in the Material World", "Dark Horse", "Extra Texture"],
        "d": 2
    },
    {
        "q": "What folk ballad by Harry Chapin hit #1 on the Billboard Hot 100 in December 1974, recounting an emotionally distant father and son?",
        "correct": "Cat's in the Cradle",
        "wrong": ["Taxi", "W-O-L-D", "30,000 Pounds of Bananas"],
        "d": 1
    },

    # 41-50
    {
        "q": "Which singer-songwriter reached #1 posthumously in early 1974 with 'Time in a Bottle' after his tragic death in an airplane crash?",
        "correct": "Jim Croce",
        "wrong": ["Harry Chapin", "Gram Parsons", "Tim Buckley"],
        "d": 2
    },
    {
        "q": "What was Jim Croce's other Billboard Hot 100 #1 hit, released earlier in 1973, about a south side Chicago tough guy?",
        "correct": "Bad, Bad Leroy Brown",
        "wrong": ["You Don't Mess Around with Jim", "Operator (That's Not the Way It Feels)", "I'll Have to Say I Love You in a Song"],
        "d": 1
    },
    {
        "q": "Which Roberta Flack hit spent five weeks at #1 on the Billboard Hot 100 in 1973 and won both Record and Song of the Year?",
        "correct": "Killing Me Softly with His Song",
        "wrong": ["The First Time Ever I Saw Your Face", "Feel Like Makin' Love", "Where Is the Love"],
        "d": 1
    },
    {
        "q": "What Roberta Flack song won Record of the Year in 1972 after spending six weeks at #1 on the Hot 100, featured in Clint Eastwood's 'Play Misty for Me'?",
        "correct": "The First Time Ever I Saw Your Face",
        "wrong": ["Killing Me Softly with His Song", "Feel Like Makin' Love", "The Closer I Get to You"],
        "d": 2
    },
    {
        "q": "Which rock band scored a #5 Hot 100 hit in 1976 with 'More Than a Feeling', from an album that set records for fastest-selling debut in US history?",
        "correct": "Boston",
        "wrong": ["Kansas", "Foreigner", "Journey"],
        "d": 2
    },
    {
        "q": "Peter Frampton's 1976 breakthrough live double album spent 10 weeks at #1 on the Billboard 200 under what title?",
        "correct": "Frampton Comes Alive!",
        "wrong": ["Frampton in Concert", "Show Me the Way Live", "Peter Frampton Live at Winterland"],
        "d": 1
    },
    {
        "q": "Which sound-altering device did Peter Frampton popularize on his Top 10 hits 'Show Me the Way' and 'Do You Feel Like We Do'?",
        "correct": "Talk box",
        "wrong": ["Wah-wah pedal", "Ring modulator", "Octaver"],
        "d": 2
    },
    {
        "q": "What hard rock band reached #7 on the Hot 100 in 1976 with the acoustic ballad 'Beth', sung by drummer Peter Criss?",
        "correct": "KISS",
        "wrong": ["Aerosmith", "Alice Cooper", "Cheap Trick"],
        "d": 2
    },
    {
        "q": "What new wave band fronted by Debbie Harry hit #1 on the Billboard Hot 100 in 1979 with the disco-infused track 'Heart of Glass'?",
        "correct": "Blondie",
        "wrong": ["The Pretenders", "Talking Heads", "The Cars"],
        "d": 1
    },
    {
        "q": "Which power-pop group spent six weeks at #1 on the Billboard Hot 100 in 1979 with 'My Sharona', the year's top-selling single?",
        "correct": "The Knack",
        "wrong": ["Cheap Trick", "The Romantics", "The Babys"],
        "d": 1
    },

    # 51-60
    {
        "q": "Which Village People dance hit peaked at #2 on the Billboard Hot 100 in early 1979 and became an enduring stadium staple?",
        "correct": "Y.M.C.A.",
        "wrong": ["In the Navy", "Macho Man", "Go West"],
        "d": 1
    },
    {
        "q": "Which Carly Simon track topped the Billboard Hot 100 for three weeks in 1973, sparking decades of speculation over its subject?",
        "correct": "You're So Vain",
        "wrong": ["Anticipation", "Nobody Does It Better", "Haven't Got Time for the Pain"],
        "d": 1
    },
    {
        "q": "Who sang uncredited backing vocals on the chorus of Carly Simon's 1972 hit 'You're So Vain'?",
        "correct": "Mick Jagger",
        "wrong": ["Warren Beatty", "James Taylor", "Paul McCartney"],
        "d": 2
    },
    {
        "q": "What Carole King album topped the Billboard 200 for 15 consecutive weeks in 1971 and remained on the charts for over 300 weeks?",
        "correct": "Tapestry",
        "wrong": ["Writer", "Music", "Rhymes & Reasons"],
        "d": 1
    },
    {
        "q": "Which song was Carole King's double-sided #1 hit from 'Tapestry' that topped the Billboard Hot 100 for five weeks in 1971?",
        "correct": "It's Too Late / I Feel the Earth Move",
        "wrong": ["You've Got a Friend / So Far Away", "Will You Love Me Tomorrow / Smackwater Jack", "Natural Woman / Beautiful"],
        "d": 2
    },
    {
        "q": "Which James Taylor cover of a Carole King composition reached #1 on the Billboard Hot 100 in July 1971?",
        "correct": "You've Got a Friend",
        "wrong": ["Fire and Rain", "How Sweet It Is (To Be Loved by You)", "Handy Man"],
        "d": 2
    },
    {
        "q": "What Neil Young acoustic folk ballad was his only #1 single on the US Billboard Hot 100, reaching the top in 1972?",
        "correct": "Heart of Gold",
        "wrong": ["Old Man", "Harvest", "Southern Man"],
        "d": 2
    },
    {
        "q": "Which folk-rock trio topped the Billboard Hot 100 in 1972 with their debut single 'A Horse with No Name'?",
        "correct": "America",
        "wrong": ["Crosby, Stills & Nash", "Seals and Crofts", "Bread"],
        "d": 2
    },
    {
        "q": "Which Al Green classic spent one week at #1 on the Billboard Hot 100 in February 1972, recorded with producer Willie Mitchell at Royal Studios?",
        "correct": "Let's Stay Together",
        "wrong": ["Love and Happiness", "Tired of Being Alone", "I'm Still in Love with You"],
        "d": 2
    },
    {
        "q": "Which Bill Withers soul classic topped the Billboard Hot 100 for three weeks in July 1972, inspired by his childhood in a West Virginia coal mining town?",
        "correct": "Lean on Me",
        "wrong": ["Ain't No Sunshine", "Use Me", "Lovely Day"],
        "d": 1
    },

    # 61-70
    {
        "q": "Which Bill Withers ballad peaked at #3 on the Billboard Hot 100 in 1971, famously repeating the phrase 'I know' 26 consecutive times?",
        "correct": "Ain't No Sunshine",
        "wrong": ["Lean on Me", "Grandma's Hands", "Just the Two of Us"],
        "d": 2
    },
    {
        "q": "Which rock band had an eight-minute epic titled 'Free Bird' reach #19 on the Hot 100, while their anthem 'Sweet Home Alabama' reached #8 in 1974?",
        "correct": "Lynyrd Skynyrd",
        "wrong": ["The Allman Brothers Band", "The Marshall Tucker Band", "Molly Hatchet"],
        "d": 2
    },
    {
        "q": "Which 1973 Aerosmith power ballad became a slow-building sleeper hit, finally peaking at #6 on the Hot 100 in 1976?",
        "correct": "Dream On",
        "wrong": ["Walk This Way", "Sweet Emotion", "Mama Kin"],
        "d": 2
    },
    {
        "q": "What song by Led Zeppelin from 'Led Zeppelin IV' was never commercially released as a US single but became one of the most played songs in album-rock radio history?",
        "correct": "Stairway to Heaven",
        "wrong": ["Black Dog", "Rock and Roll", "Going to California"],
        "d": 1
    },
    {
        "q": "What was Led Zeppelin's highest-charting single on the US Billboard Hot 100, peaking at #4 in early 1970?",
        "correct": "Whole Lotta Love",
        "wrong": ["Immigrant Song", "Black Dog", "D'yer Mak'er"],
        "d": 2
    },
    {
        "q": "Which singer reached #1 on the Billboard Hot 100 in 1975 with 'Fame', co-written with John Lennon and Carlos Alomar?",
        "correct": "David Bowie",
        "wrong": ["Iggy Pop", "Mick Jagger", "Lou Reed"],
        "d": 2
    },
    {
        "q": "What was David Bowie's second #1 single on the US Billboard Hot 100, topping the chart eight years after 'Fame' in 1983?",
        "correct": "Let's Dance",
        "wrong": ["Modern Love", "China Girl", "Golden Years"],
        "d": 2
    },
    {
        "q": "Which funk ensemble led by George Clinton had a #1 R&B and Top 15 pop hit in 1978 with 'One Nation Under a Groove'?",
        "correct": "Funkadelic",
        "wrong": ["Parliament", "The Ohio Players", "The Commodores"],
        "d": 3
    },
    {
        "q": "Which Parliament funk anthem reached #16 on the Billboard Hot 100 in 1976 and featured the subtitle '(Tear the Roof off the Sucker)'?",
        "correct": "Give Up the Funk",
        "wrong": ["Flash Light", "P. Funk (Wants to Get Funked Up)", "Mothership Connection"],
        "d": 3
    },
    {
        "q": "Which Lionel Richie-led group topped the Billboard Hot 100 in 1978 with the smooth ballad 'Three Times a Lady'?",
        "correct": "The Commodores",
        "wrong": ["The Spinners", "The O'Jays", "The Stylistics"],
        "d": 2
    },

    # 71-80
    {
        "q": "What Commodores funk track peaked at #5 on the Billboard Hot 100 in 1977, celebrating a woman built like a 'brick outhouse'?",
        "correct": "Brick House",
        "wrong": ["Easy", "Lady (You Bring Me Up)", "Too Hot ta Trot"],
        "d": 1
    },
    {
        "q": "What 1977 ballad by The Commodores peaked at #4 on the Billboard Hot 100 with the opening line 'I know it sounds funny but I just can't stand the pain'?",
        "correct": "Easy",
        "wrong": ["Sail On", "Three Times a Lady", "Still"],
        "d": 2
    },
    {
        "q": "Which John Denver song reached #1 on the Billboard Hot 100 in 1974, inspired by an idyllic ride on a ski lift in Aspen, Colorado?",
        "correct": "Annie's Song",
        "wrong": ["Sunshine on My Shoulders", "Thank God I'm a Country Boy", "Take Me Home, Country Roads"],
        "d": 2
    },
    {
        "q": "What 1971 John Denver anthem peaked at #2 on the Billboard Hot 100, paying homage to West Virginia's Blue Ridge Mountains?",
        "correct": "Take Me Home, Country Roads",
        "wrong": ["Rocky Mountain High", "Annie's Song", "Leaving on a Jet Plane"],
        "d": 1
    },
    {
        "q": "Which Gladys Knight & the Pips classic topped the Billboard Hot 100 in late 1973, describing a train ride departing for the South?",
        "correct": "Midnight Train to Georgia",
        "wrong": ["Neither One of Us", "Best Thing That Ever Happened to Me", "I've Got to Use My Imagination"],
        "d": 1
    },
    {
        "q": "What was the original title of 'Midnight Train to Georgia' before it was altered to suit Gladys Knight?",
        "correct": "Midnight Plane to Houston",
        "wrong": ["Night Bus to Atlanta", "Morning Train to Dallas", "Last Flight to Memphis"],
        "d": 3
    },
    {
        "q": "Which Olivia Newton-John ballad topped the Billboard Hot 100 in 1974, winning Grammy Awards for Record of the Year and Best Pop Vocal Performance?",
        "correct": "I Honestly Love You",
        "wrong": ["Have You Never Been Mellow", "Hopelessly Devoted to You", "Magic"],
        "d": 2
    },
    {
        "q": "Which duet by Olivia Newton-John and John Travolta spent one week at #1 on the Billboard Hot 100 in June 1978 from the 'Grease' soundtrack?",
        "correct": "You're the One That I Want",
        "wrong": ["Summer Nights", "Hopelessly Devoted to You", "Sandy"],
        "d": 1
    },
    {
        "q": "Which Barry Gibb-written title song for the movie 'Grease' hit #1 on the Billboard Hot 100 in 1978, performed by Frankie Valli?",
        "correct": "Grease",
        "wrong": ["Sandy", "Beauty School Dropout", "Born to Hand Jive"],
        "d": 2
    },
    {
        "q": "What 1975 Frankie Valli solo single reached #1 on the Billboard Hot 100, featuring a lush orchestral pop arrangement?",
        "correct": "My Eyes Adored You",
        "wrong": ["Swearin' to God", "Can't Take My Eyes Off You", "Our Day Will Come"],
        "d": 3
    },

    # 81-90
    {
        "q": "Which Four Seasons disco hit topped the Billboard Hot 100 for three weeks in early 1976, celebrating 'late December back in '63'?",
        "correct": "December, 1963 (Oh, What a Night)",
        "wrong": ["Who Loves You", "Silver Star", "Rag Doll"],
        "d": 1
    },
    {
        "q": "Which singer topped the Billboard Hot 100 for three weeks in 1973 with 'The Night the Lights Went Out in Georgia'?",
        "correct": "Vicki Lawrence",
        "wrong": ["Cher", "Tanya Tucker", "Lulu"],
        "d": 3
    },
    {
        "q": "Which Cher single topped the Billboard Hot 100 in 1973, telling the story of a girl whose parents 'called the local preacher'?",
        "correct": "Half-Breed",
        "wrong": ["Gypsys, Tramps & Thieves", "Dark Lady", "The Way of Love"],
        "d": 2
    },
    {
        "q": "What was Cher's very first solo #1 single on the US Billboard Hot 100, topping the chart in November 1971?",
        "correct": "Gypsys, Tramps & Thieves",
        "wrong": ["Half-Breed", "Dark Lady", "Bang Bang (My Baby Shot Me Down)"],
        "d": 2
    },
    {
        "q": "Which Tony Orlando and Dawn pop smash was the Billboard Year-End #1 single of 1973, urging someone to tie a yellow ribbon?",
        "correct": "Tie a Yellow Ribbon Round the Ole Oak Tree",
        "wrong": ["Candida", "Knock Three Times", "He Don't Love You (Like I Love You)"],
        "d": 1
    },
    {
        "q": "Which Barry Manilow romantic ballad was his first #1 single on the Billboard Hot 100, topping the chart in January 1975?",
        "correct": "Mandy",
        "wrong": ["I Write the Songs", "Copacabana", "Can't Smile Without You"],
        "d": 2
    },
    {
        "q": "Who wrote Barry Manilow's 1976 Billboard Hot 100 #1 hit 'I Write the Songs'?",
        "correct": "Bruce Johnston of The Beach Boys",
        "wrong": ["Barry Manilow", "Paul Williams", "Neil Sedaka"],
        "d": 3
    },
    {
        "q": "Which Captain & Tennille cover of a Neil Sedaka song spent four weeks at #1 and was the Billboard Year-End #1 single of 1975?",
        "correct": "Love Will Keep Us Together",
        "wrong": ["Do That to Me One More Time", "Muskrat Love", "The Way I Want to Touch You"],
        "d": 2
    },
    {
        "q": "What 1976 hit by Wild Cherry reached #1 on both the Hot 100 and R&B charts, inspired by a crowd demanding dance music?",
        "correct": "Play That Funky Music",
        "wrong": ["Disco Duck", "The Rubberband Man", "Boogie Fever"],
        "d": 1
    },
    {
        "q": "Which rock band hit #1 on the Billboard Hot 100 in 1973 with 'Frankenstein', an instrumental featuring an ARP 2600 synthesizer?",
        "correct": "The Edgar Winter Group",
        "wrong": ["The Alan Parsons Project", "Focus", "Emerson, Lake & Palmer"],
        "d": 3
    },

    # 91-100
    {
        "q": "Which 1973 soft rock classic by Seals and Crofts reached #6 on the Billboard Hot 100, featuring the opening line 'Summer breeze, makes me feel fine'?",
        "correct": "Summer Breeze",
        "wrong": ["Diamond Girl", "Get Closer", "We May Never Pass This Way Again"],
        "d": 2
    },
    {
        "q": "Which Boz Scaggs single from his 1976 album 'Silk Degrees' peaked at #3 on the Billboard Hot 100 and won a Grammy for Best R&B Song?",
        "correct": "Lowdown",
        "wrong": ["Lido Shuffle", "We're All Alone", "What Can I Say"],
        "d": 3
    },
    {
        "q": "Which band members who played on Boz Scaggs' 'Silk Degrees' went on to form the hit-making group Toto in 1977?",
        "correct": "Jeff Porcaro and David Paich",
        "wrong": ["Donald Fagen and Walter Becker", "Steve Lukather and Michael McDonald", "Kenny Loggins and Jim Messina"],
        "d": 3
    },
    {
        "q": "Which Steely Dan song peaked at #4 on the Billboard Hot 100 in 1974, becoming their highest-charting single of all time?",
        "correct": "Rikki Don't Lose That Number",
        "wrong": ["Do It Again", "Peg", "Hey Nineteen"],
        "d": 2
    },
    {
        "q": "Which Steely Dan album peaked at #3 on the Billboard 200 in 1977 and featured jazz luminaries Wayne Shorter and Larry Carlton?",
        "correct": "Aja",
        "wrong": ["Pretzel Logic", "Gaucho", "Can't Buy a Thrill"],
        "d": 2
    },
    {
        "q": "Which Foreigner hard rock ballad reached #4 on the Billboard Hot 100 in 1977, taken from their self-titled debut album?",
        "correct": "Feels Like the First Time",
        "wrong": ["Cold as Ice", "Double Vision", "Hot Blooded"],
        "d": 2
    },
    {
        "q": "What Foreigner single reached #2 on the Billboard Hot 100 for five weeks in 1981, held back from #1 by Olivia Newton-John's 'Physical'?",
        "correct": "Waiting for a Girl Like You",
        "wrong": ["Urgent", "I Want to Know What Love Is", "Juke Box Hero"],
        "d": 2
    },
    {
        "q": "Which 1976 hit single by Kansas peaked at #11, while their 1977 acoustic-led philosophical anthem 'Dust in the Wind' reached #6 on the Hot 100?",
        "correct": "Dust in the Wind",
        "wrong": ["Carry On Wayward Son", "Point of Know Return", "Hold On"],
        "d": 2
    },
    {
        "q": "Which Sister Sledge anthem, written and produced by Nile Rodgers and Bernard Edwards, peaked at #2 on the Billboard Hot 100 in 1979?",
        "correct": "We Are Family",
        "wrong": ["He's the Greatest Dancer", "Lost in Music", "Thinking of You"],
        "d": 1
    },
    {
        "q": "What Donna Summer ballad featuring Barbra Streisand reached #1 on the Billboard Hot 100 for two weeks in late 1979?",
        "correct": "No More Tears (Enough Is Enough)",
        "wrong": ["The Main Event/Fight", "Evergreen", "Tell Him"],
        "d": 2
    }
]

if __name__ == "__main__":
    formatted = assemble_batch(QUESTIONS, 2)
    save_batch(formatted, 2)
