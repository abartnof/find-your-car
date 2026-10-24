import sys
import os
sys.path.append(os.path.dirname(__file__))
from utils import assemble_batch, save_batch

QUESTIONS = [
    # 1-10
    {
        "q": "Which Michael Jackson album released in late 1982 spent 37 non-consecutive weeks at #1 on the Billboard 200 and produced seven top 10 singles?",
        "correct": "Thriller",
        "wrong": ["Bad", "Off the Wall", "Dangerous"],
        "d": 1
    },
    {
        "q": "Who performed the legendary electric guitar solo on Michael Jackson's 1983 #1 hit 'Beat It'?",
        "correct": "Eddie Van Halen",
        "wrong": ["Slash", "Steve Lukather", "Carlos Santana"],
        "d": 1
    },
    {
        "q": "Which horror movie legend performed the closing spoken-word rap and sinister laugh on Michael Jackson's 'Thriller'?",
        "correct": "Vincent Price",
        "wrong": ["Christopher Lee", "Peter Cushing", "Bela Lugosi"],
        "d": 1
    },
    {
        "q": "What was Prince's very first #1 single on the Billboard Hot 100, which spent five weeks at the top in the summer of 1984?",
        "correct": "When Doves Cry",
        "wrong": ["Let's Go Crazy", "Purple Rain", "1999"],
        "d": 1
    },
    {
        "q": "What notable musical element did Prince intentionally leave out of the final mix of 'When Doves Cry'?",
        "correct": "Bass guitar line",
        "wrong": ["Snare drum", "Rhythm guitar", "Keyboard synthesizer"],
        "d": 2
    },
    {
        "q": "Which Prince album served as the soundtrack to a film and spent 24 consecutive weeks at #1 on the Billboard 200 in 1984-1985?",
        "correct": "Purple Rain",
        "wrong": ["1999", "Sign o' the Times", "Parade"],
        "d": 1
    },
    {
        "q": "What was Madonna's first single to hit #1 on the Billboard Hot 100, remaining at the top for six weeks in late 1984 and early 1985?",
        "correct": "Like a Virgin",
        "wrong": ["Holiday", "Material Girl", "Crazy for You"],
        "d": 1
    },
    {
        "q": "Who produced Madonna's breakthrough multi-platinum album 'Like a Virgin'?",
        "correct": "Nile Rodgers",
        "wrong": ["Quincy Jones", "Patrick Leonard", "Stephen Bray"],
        "d": 2
    },
    {
        "q": "Which Whitney Houston hit from 1985 made her the first female artist to have a debut album generate three #1 singles on the Hot 100?",
        "correct": "Greatest Love of All",
        "wrong": ["Saving All My Love for You", "How Will I Know", "You Give Good Love"],
        "d": 2
    },
    {
        "q": "How many consecutive #1 singles did Whitney Houston achieve on the Billboard Hot 100 from 1985 to 1988, setting an all-time record?",
        "correct": "Seven",
        "wrong": ["Five", "Six", "Eight"],
        "d": 2
    },

    # 11-20
    {
        "q": "Which 1984 Bruce Springsteen album spawned seven Top 10 Billboard Hot 100 singles, tying Michael Jackson's 'Thriller'?",
        "correct": "Born in the U.S.A.",
        "wrong": ["The River", "Nebraska", "Tunnel of Love"],
        "d": 1
    },
    {
        "q": "Which song from 'Born in the U.S.A.' was Bruce Springsteen's highest-charting single of his career, peaking at #2 on the Hot 100?",
        "correct": "Dancing in the Dark",
        "wrong": ["Born in the U.S.A.", "Glory Days", "I'm on Fire"],
        "d": 2
    },
    {
        "q": "Which actress was pulled out of the crowd to dance with Bruce Springsteen in the music video for 'Dancing in the Dark'?",
        "correct": "Courteney Cox",
        "wrong": ["Meg Ryan", "Demi Moore", "Winona Ryder"],
        "d": 2
    },
    {
        "q": "What Cyndi Lauper ballad topped the Billboard Hot 100 in 1984, later covered famously by Miles Davis?",
        "correct": "Time After Time",
        "wrong": ["Girls Just Want to Have Fun", "She Bop", "True Colors"],
        "d": 2
    },
    {
        "q": "Which Wham! dance hit was the duo's first Billboard Hot 100 #1 single in November 1984, famous for the lyric 'Don't leave me hanging on like a yo-yo'?",
        "correct": "Wake Me Up Before You Go-Go",
        "wrong": ["Careless Whisper", "Freedom", "Everything She Wants"],
        "d": 1
    },
    {
        "q": "Which George Michael saxophone-driven masterpiece was the Billboard Year-End #1 single of 1985?",
        "correct": "Careless Whisper",
        "wrong": ["Faith", "One More Try", "Father Figure"],
        "d": 1
    },
    {
        "q": "Which George Michael solo album won Album of the Year at the Grammys and produced four Billboard Hot 100 #1 singles?",
        "correct": "Faith",
        "wrong": ["Listen Without Prejudice Vol. 1", "Older", "Patience"],
        "d": 1
    },
    {
        "q": "What Phil Collins ballad, written for a 1984 romantic drama of the same name, was his first solo #1 hit on the Hot 100?",
        "correct": "Against All Odds (Take a Look at Me Now)",
        "wrong": ["In the Air Tonight", "One More Night", "Groovy Kind of Love"],
        "d": 2
    },
    {
        "q": "What drum fill made Phil Collins' 1981 song 'In the Air Tonight' famous, helping propel it into the Billboard top 20?",
        "correct": "Gated reverb drum fill",
        "wrong": ["Double bass-drum blast", "Electronic trap fill", "Rototom solo"],
        "d": 2
    },
    {
        "q": "Which Bon Jovi anthem, featuring a talk-box guitar riff by Richie Sambora, spent four weeks at #1 on the Hot 100 in 1987?",
        "correct": "Livin' on a Prayer",
        "wrong": ["You Give Love a Bad Name", "Wanted Dead or Alive", "Bad Medicine"],
        "d": 1
    },

    # 21-30
    {
        "q": "Which Bon Jovi album spent eight weeks at #1 on the Billboard 200 and was the best-selling album of 1987 in the US?",
        "correct": "Slippery When Wet",
        "wrong": ["New Jersey", "Keep the Faith", "7800° Fahrenheit"],
        "d": 2
    },
    {
        "q": "What was Guns N' Roses' only #1 hit on the Billboard Hot 100, topping the chart in September 1988?",
        "correct": "Sweet Child o' Mine",
        "wrong": ["Welcome to the Jungle", "Paradise City", "Patience"],
        "d": 1
    },
    {
        "q": "Which 1987 debut studio album by Guns N' Roses eventually hit #1 on the Billboard 200 after a steady 50-week climb?",
        "correct": "Appetite for Destruction",
        "wrong": ["G N' R Lies", "Use Your Illusion I", "Use Your Illusion II"],
        "d": 2
    },
    {
        "q": "Which Def Leppard power ballad gave the band their only #1 single on the US Billboard Hot 100 in October 1988?",
        "correct": "Love Bites",
        "wrong": ["Pour Some Sugar on Me", "Animal", "Armageddon It"],
        "d": 2
    },
    {
        "q": "What peak position did Def Leppard's signature arena rocker 'Pour Some Sugar on Me' reach on the Billboard Hot 100?",
        "correct": "#2",
        "wrong": ["#1", "#5", "#9"],
        "d": 2
    },
    {
        "q": "Which duo achieved six Billboard Hot 100 #1 singles in the late 1970s and 1980s, including 'Maneater' and 'Private Eyes'?",
        "correct": "Daryl Hall and John Oates",
        "wrong": ["Tears for Fears", "Wham!", "The Righteous Brothers"],
        "d": 1
    },
    {
        "q": "Which 1983 Lionel Richie album sold over 10 million copies in the US and featured the #1 hits 'All Night Long' and 'Hello'?",
        "correct": "Can't Slow Down",
        "wrong": ["Lionel Richie", "Dancing on the Ceiling", "Back to Front"],
        "d": 2
    },
    {
        "q": "In which fictional language did Lionel Richie write several lyrics for the chorus of his #1 hit 'All Night Long (All Night)'?",
        "correct": "Made-up African-sounding dialect",
        "wrong": ["Swahili", "Esperanto", "Yoruba"],
        "d": 2
    },
    {
        "q": "What was U2's first Billboard Hot 100 #1 single, leading their acclaimed 1987 album 'The Joshua Tree'?",
        "correct": "With or Without You",
        "wrong": ["I Still Haven't Found What I'm Looking For", "Where the Streets Have No Name", "Pride (In the Name of Love)"],
        "d": 1
    },
    {
        "q": "Which The Police single spent eight weeks at #1 on the Billboard Hot 100 in 1983 and won the Grammy for Song of the Year?",
        "correct": "Every Breath You Take",
        "wrong": ["King of Pain", "Wrapped Around Your Finger", "Don't Stand So Close to Me"],
        "d": 1
    },

    # 31-40
    {
        "q": "Which Tina Turner single spent three weeks at #1 on the Billboard Hot 100 in 1984, reviving her career at age 44?",
        "correct": "What's Love Got to Do with It",
        "wrong": ["Private Dancer", "Better Be Good to Me", "The Best"],
        "d": 1
    },
    {
        "q": "Which British synth-pop duo topped the Billboard Hot 100 in 1985 with both 'Shout' and 'Everybody Wants to Rule the World'?",
        "correct": "Tears for Fears",
        "wrong": ["Pet Shop Boys", "Eurythmics", "Wham!"],
        "d": 2
    },
    {
        "q": "What Duran Duran track became their first Billboard Hot 100 #1 single in June 1984, remixed by Nile Rodgers?",
        "correct": "The Reflex",
        "wrong": ["Hungry Like the Wolf", "Rio", "A View to a Kill"],
        "d": 2
    },
    {
        "q": "Which Duran Duran song is the only James Bond theme to reach #1 on the US Billboard Hot 100?",
        "correct": "A View to a Kill",
        "wrong": ["Goldfinger", "Live and Let Die", "Skyfall"],
        "d": 1
    },
    {
        "q": "What 1981 Rick Springfield pop-rock anthem reached #1 on the Billboard Hot 100, recounting jealousy over a best friend's girlfriend?",
        "correct": "Jessie's Girl",
        "wrong": ["Don't Talk to Strangers", "I've Done Everything for You", "Affair of the Heart"],
        "d": 1
    },
    {
        "q": "Which Kenny Loggins soundtrack anthem from a Kevin Bacon dance film spent three weeks at #1 on the Hot 100 in 1984?",
        "correct": "Footloose",
        "wrong": ["Danger Zone", "I'm Alright", "Meet Me Half Way"],
        "d": 1
    },
    {
        "q": "Which rock band spent six weeks at #1 on the Billboard Hot 100 in 1982 with 'Eye of the Tiger', written for 'Rocky III'?",
        "correct": "Survivor",
        "wrong": ["Foreigner", "REO Speedwagon", "Asia"],
        "d": 1
    },
    {
        "q": "Which Australian band achieved simultaneous #1 positions on both the US album and singles charts in early 1983 with 'Business as Usual' and 'Down Under'?",
        "correct": "Men at Work",
        "wrong": ["INXS", "Little River Band", "Midnight Oil"],
        "d": 2
    },
    {
        "q": "What synth-driven rocker was Van Halen's only Billboard Hot 100 #1 hit, spending five weeks at the top in 1984?",
        "correct": "Jump",
        "wrong": ["Panama", "Hot for Teacher", "Why Can't This Be Love"],
        "d": 1
    },
    {
        "q": "Which synthesizer provided the iconic opening keyboard chords to Van Halen's #1 smash 'Jump'?",
        "correct": "Oberheim OB-Xa",
        "wrong": ["Yamaha DX7", "Roland Jupiter-8", "Sequential Circuits Prophet-5"],
        "d": 3
    },

    # 41-50
    {
        "q": "Which Huey Lewis and the News track from the 'Back to the Future' soundtrack was the band's first Billboard Hot 100 #1 in 1985?",
        "correct": "The Power of Love",
        "wrong": ["Back in Time", "I Want a New Drug", "Heart and Soul"],
        "d": 1
    },
    {
        "q": "What Journey power ballad from the 1981 album 'Escape' peaked at #2 on the Hot 100 for six weeks, kept out of #1 by 'Physical' and 'Centerfold'?",
        "correct": "Open Arms",
        "wrong": ["Don't Stop Believin'", "Faithfully", "Who's Crying Now"],
        "d": 2
    },
    {
        "q": "What peak position did Journey's iconic rock anthem 'Don't Stop Believin'' reach on the Billboard Hot 100 upon its initial release in 1981?",
        "correct": "#9",
        "wrong": ["#1", "#4", "#15"],
        "d": 2
    },
    {
        "q": "Which Peter Gabriel track from his 1986 album 'So' topped the Hot 100, famously supported by an award-winning stop-motion claymation music video?",
        "correct": "Sledgehammer",
        "wrong": ["Big Time", "In Your Eyes", "Don't Give Up"],
        "d": 1
    },
    {
        "q": "Whose single did Peter Gabriel's 'Sledgehammer' displace from #1 on the Billboard Hot 100 in July 1986?",
        "correct": "Genesis ('Invisible Touch')",
        "wrong": ["Phil Collins ('Against All Odds')", "Peter Cetera ('Glory of Love')", "Madonna ('Papa Don't Preach')"],
        "d": 3
    },
    {
        "q": "What was Genesis's only #1 single on the US Billboard Hot 100, reaching the summit in July 1986?",
        "correct": "Invisible Touch",
        "wrong": ["That's All", "Land of Confusion", "Tonight, Tonight, Tonight"],
        "d": 2
    },
    {
        "q": "Which Steve Winwood track, featuring backing vocals by Chaka Khan, reached #1 on the Billboard Hot 100 in August 1986?",
        "correct": "Higher Love",
        "wrong": ["Roll with It", "Valerie", "Back in the High Life Again"],
        "d": 2
    },
    {
        "q": "What Paul Simon solo album won Album of the Year at the 1987 Grammys and reached #3 on the Billboard 200, fusing American pop with South African rhythms?",
        "correct": "Graceland",
        "wrong": ["There Goes Rhymin' Simon", "Still Crazy After All These Years", "The Rhythm of the Saints"],
        "d": 1
    },
    {
        "q": "Which comedian starred alongside Paul Simon in the music video for the Top 5 hit 'You Can Call Me Al'?",
        "correct": "Chevy Chase",
        "wrong": ["Steve Martin", "Bill Murray", "Dan Aykroyd"],
        "d": 2
    },
    {
        "q": "Which charity supergroup single, written by Michael Jackson and Lionel Richie, topped the Billboard Hot 100 for four weeks in 1985?",
        "correct": "We Are the World",
        "wrong": ["Do They Know It's Christmas?", "That's What Friends Are For", "Tears Are Not Enough"],
        "d": 1
    },

    # 51-60
    {
        "q": "Under what moniker was the supergroup behind 'We Are the World' credited on the Billboard charts?",
        "correct": "USA for Africa",
        "wrong": ["Band Aid", "Artists United Against Apartheid", "Hear 'n Aid"],
        "d": 1
    },
    {
        "q": "Which British charity single, conceived by Bob Geldof and Midge Ure, reached #13 on the Hot 100 in early 1985 after topping charts across Europe?",
        "correct": "Do They Know It's Christmas?",
        "wrong": ["Feed the World", "We Are the World", "Let It Be"],
        "d": 2
    },
    {
        "q": "Which Dionne Warwick-led charity single featuring Elton John, Gladys Knight, and Stevie Wonder was the Billboard Year-End #1 single of 1986?",
        "correct": "That's What Friends Are For",
        "wrong": ["I Say a Little Prayer", "Solid", "Heartbreaker"],
        "d": 2
    },
    {
        "q": "Which Foreigner power ballad, backed by the New Jersey Mass Choir, was the band's sole Billboard Hot 100 #1 hit, in early 1985?",
        "correct": "I Want to Know What Love Is",
        "wrong": ["Waiting for a Girl Like You", "Cold as Ice", "Urgent"],
        "d": 1
    },
    {
        "q": "Which hair metal band hit #1 on the Billboard Hot 100 in 1989 with the power ballad 'When I See You Smile'?",
        "correct": "Bad English",
        "wrong": ["Whitesnake", "Warrant", "Poison"],
        "d": 3
    },
    {
        "q": "Which glam rock group topped the Billboard Hot 100 for three weeks in late 1988 with 'Every Rose Has Its Thorn'?",
        "correct": "Poison",
        "wrong": ["Mötley Crüe", "Cinderella", "Warrant"],
        "d": 1
    },
    {
        "q": "Which Whitesnake power ballad topped the Billboard Hot 100 in October 1987, famous for Tawny Kitaen dancing on cars in the music video?",
        "correct": "Here I Go Again",
        "wrong": ["Is This Love", "Still of the Night", "Slow an' Easy"],
        "d": 2
    },
    {
        "q": "What power ballad gave Whitesnake another Top 5 hit when it reached #2 on the Billboard Hot 100 in late 1987?",
        "correct": "Is This Love",
        "wrong": ["The Deeper the Love", "Here I Go Again", "Fool for Your Loving"],
        "d": 2
    },
    {
        "q": "Which REO Speedwagon power ballad was the band's first Billboard Hot 100 #1 hit in 1981, from their multi-platinum album 'Hi Infidelity'?",
        "correct": "Keep On Loving You",
        "wrong": ["Can't Fight This Feeling", "Take It on the Run", "Time for Me to Fly"],
        "d": 2
    },
    {
        "q": "What was REO Speedwagon's second Billboard Hot 100 #1 single, topping the chart for three weeks in 1985?",
        "correct": "Can't Fight This Feeling",
        "wrong": ["Keep On Loving You", "Keep the Fire Burnin'", "In My Dreams"],
        "d": 2
    },

    # 61-70
    {
        "q": "Which The Bangles single hit #1 on the Billboard Hot 100 in 1986, accompanied by a popular Egyptian-style hand dance?",
        "correct": "Walk Like an Egyptian",
        "wrong": ["Manic Monday", "Eternal Flame", "In Your Room"],
        "d": 1
    },
    {
        "q": "Who wrote The Bangles' 1986 #2 hit 'Manic Monday' under the pseudonym 'Christopher'?",
        "correct": "Prince",
        "wrong": ["Rick Springfield", "Billy Joel", "Tom Petty"],
        "d": 2
    },
    {
        "q": "Which The Bangles ballad topped the Billboard Hot 100 in 1989, inspired by a visit to Elvis Presley's Graceland gravesite?",
        "correct": "Eternal Flame",
        "wrong": ["Walk Like an Egyptian", "Manic Monday", "Hazy Shade of Winter"],
        "d": 2
    },
    {
        "q": "Which a cappella single by Bobby McFerrin spent two weeks at #1 in 1988, becoming the first completely unaccompanied song to top the Hot 100?",
        "correct": "Don't Worry, Be Happy",
        "wrong": ["Good Lovin'", "Thinkin' About Your Body", "Drive My Car"],
        "d": 1
    },
    {
        "q": "Which comedy star danced alongside Bill Irwin in Bobby McFerrin's music video for 'Don't Worry, Be Happy'?",
        "correct": "Robin Williams",
        "wrong": ["Jim Carrey", "Eddie Murphy", "Steve Martin"],
        "d": 2
    },
    {
        "q": "Which Janet Jackson album produced seven Top 5 Billboard Hot 100 singles between 1989 and 1991, an unprecedented feat?",
        "correct": "Janet Jackson's Rhythm Nation 1814",
        "wrong": ["Control", "janet.", "The Velvet Rope"],
        "d": 1
    },
    {
        "q": "What was Janet Jackson's first Billboard Hot 100 #1 hit, reaching the summit in autumn 1986?",
        "correct": "When I Think of You",
        "wrong": ["Nasty", "What Have You Done for Me Lately", "Control"],
        "d": 2
    },
    {
        "q": "Which Minneapolis production duo produced Janet Jackson's breakthrough albums 'Control' and 'Rhythm Nation 1814'?",
        "correct": "Jimmy Jam and Terry Lewis",
        "wrong": ["L.A. Reid and Babyface", "Nile Rodgers and Bernard Edwards", "Quincy Jones and Rod Temperton"],
        "d": 2
    },
    {
        "q": "Which Rick Astley dance-pop hit topped the Billboard Hot 100 for two weeks in 1988, decades before becoming an internet meme?",
        "correct": "Never Gonna Give You Up",
        "wrong": ["Together Forever", "It Would Take a Strong Strong Man", "She Wants to Dance with Me"],
        "d": 1
    },
    {
        "q": "Which British songwriting and production trio created hits for Rick Astley, Bananarama, and Kylie Minogue?",
        "correct": "Stock Aitken Waterman",
        "wrong": ["Holland-Dozier-Holland", "Chinn and Chapman", "Leiber and Stoller"],
        "d": 2
    },

    # 71-80
    {
        "q": "Which Paula Abdul track was her first Billboard Hot 100 #1 hit, holding the top spot for three weeks in early 1989?",
        "correct": "Straight Up",
        "wrong": ["Forever Your Girl", "Cold Hearted", "Opposites Attract"],
        "d": 1
    },
    {
        "q": "Which animated character danced with Paula Abdul in the music video for her 1990 #1 hit 'Opposites Attract'?",
        "correct": "MC Skat Kat",
        "wrong": ["Roger Rabbit", "Cool Cat", "Felix the Cat"],
        "d": 2
    },
    {
        "q": "Which Milli Vanilli song topped the Billboard Hot 100 in 1989 before the duo's lip-syncing scandal led to the revocation of their Grammy?",
        "correct": "Girl You Know It's True",
        "wrong": ["Baby Don't Forget My Number", "Girl I'm Gonna Miss You", "Blame It on the Rain"],
        "d": 2
    },
    {
        "q": "How many Billboard Hot 100 #1 hits did Milli Vanilli officially earn in 1989 before the vocal controversy unfolded?",
        "correct": "Three",
        "wrong": ["One", "Two", "Four"],
        "d": 3
    },
    {
        "q": "Which 1987 Los Lobos cover of a Ritchie Valens standard reached #1 on the Billboard Hot 100 from the biographical film soundtrack?",
        "correct": "La Bamba",
        "wrong": ["Donna", "Come On, Let's Go", "We Belong Together"],
        "d": 1
    },
    {
        "q": "Which Starship pop hit topped the Billboard Hot 100 in late 1985, co-written by Bernie Taupin and Martin Page?",
        "correct": "We Built This City",
        "wrong": ["Sara", "Nothing's Gonna Stop Us Now", "Find Your Way Back"],
        "d": 2
    },
    {
        "q": "Which Starship power ballad from the movie 'Mannequin' reached #1 on the Hot 100 in April 1987?",
        "correct": "Nothing's Gonna Stop Us Now",
        "wrong": ["Sara", "We Built This City", "It's Not Over ('Til It's Over)"],
        "d": 2
    },
    {
        "q": "At age 47, Grace Slick became the oldest woman to reach #1 on the Billboard Hot 100 at the time with which Starship hit?",
        "correct": "Nothing's Gonna Stop Us Now",
        "wrong": ["We Built This City", "Sara", "White Rabbit"],
        "d": 3
    },
    {
        "q": "Which Falco track hit #1 on the Billboard Hot 100 in 1986, becoming the first German-language rap/pop song to reach the summit?",
        "correct": "Rock Me Amadeus",
        "wrong": ["Der Kommissar", "Vienna Calling", "Jeanny"],
        "d": 1
    },
    {
        "q": "Which German singer topped charts around the world and hit #2 on the US Hot 100 in 1984 with the anti-war song '99 Luftballons'?",
        "correct": "Nena",
        "wrong": ["Sandra", "Doro Pesch", "Nina Hagen"],
        "d": 2
    },

    # 81-90
    {
        "q": "What 1988 Beach Boys comeback single reached #1 on the Billboard Hot 100, their first chart-topper in 22 years?",
        "correct": "Kokomo",
        "wrong": ["Getcha Back", "Still Cruisin'", "California Dreamin'"],
        "d": 1
    },
    {
        "q": "In which Tom Cruise film was The Beach Boys' #1 hit 'Kokomo' featured on the soundtrack?",
        "correct": "Cocktail",
        "wrong": ["Top Gun", "Rain Man", "Risky Business"],
        "d": 2
    },
    {
        "q": "Which Belinda Carlisle power ballad topped the Billboard Hot 100 for one week in December 1987?",
        "correct": "Heaven Is a Place on Earth",
        "wrong": ["I Get Weak", "Circle in the Sand", "Mad About You"],
        "d": 2
    },
    {
        "q": "Which female rock group did Belinda Carlisle front before embarking on her successful solo chart career?",
        "correct": "The Go-Go's",
        "wrong": ["The Bangles", "The Runaways", "Heart"],
        "d": 1
    },
    {
        "q": "What 1981 album by The Go-Go's became the first album by an all-female band who wrote their own songs and played their own instruments to reach #1 on the Billboard 200?",
        "correct": "Beauty and the Beat",
        "wrong": ["Vacation", "Talk Show", "God Bless the Go-Go's"],
        "d": 2
    },
    {
        "q": "What was the highest-charting Billboard Hot 100 single from The Go-Go's debut album 'Beauty and the Beat', peaking at #2?",
        "correct": "We Got the Beat",
        "wrong": ["Our Lips Are Sealed", "Vacation", "Head over Heels"],
        "d": 2
    },
    {
        "q": "Which Heart ballad was the band's first Billboard Hot 100 #1 hit, topping the chart in March 1986?",
        "correct": "These Dreams",
        "wrong": ["Alone", "What About Love", "Never"],
        "d": 2
    },
    {
        "q": "Which Ann and Nancy Wilson power ballad for Heart spent three weeks at #1 on the Billboard Hot 100 in July 1987?",
        "correct": "Alone",
        "wrong": ["These Dreams", "All I Wanna Do Is Make Love to You", "Stranded"],
        "d": 2
    },
    {
        "q": "Which John Cougar Mellencamp single spent four weeks at #1 on the Billboard Hot 100 in 1982, telling the story of Jack and Diane?",
        "correct": "Jack & Diane",
        "wrong": ["Hurts So Good", "Pink Houses", "Small Town"],
        "d": 1
    },
    {
        "q": "What John Cougar Mellencamp track peaked at #2 behind 'Jack & Diane' on the Hot 100 in 1982, giving him two songs in the top 2?",
        "correct": "Hurts So Good",
        "wrong": ["Crumblin' Down", "Authority Song", "Lonely Ol' Night"],
        "d": 2
    },

    # 91-100
    {
        "q": "Which Toto soft-rock hit reached #1 on the Billboard Hot 100 in February 1983, featuring the lyric 'I bless the rains down in Africa'?",
        "correct": "Africa",
        "wrong": ["Rosanna", "Hold the Line", "99"],
        "d": 1
    },
    {
        "q": "What Toto song won the Grammy for Record of the Year in 1983 and peaked at #2 on the Billboard Hot 100?",
        "correct": "Rosanna",
        "wrong": ["Africa", "I Won't Hold You Back", "Georgy Porgy"],
        "d": 2
    },
    {
        "q": "Which Steve Perry power ballad peaked at #3 on the Billboard Hot 100 in 1984 during his solo hiatus from Journey?",
        "correct": "Oh Sherrie",
        "wrong": ["Foolish Heart", "Strung Out", "She's Mine"],
        "d": 2
    },
    {
        "q": "Which Cyndi Lauper single was her second #1 on the Billboard Hot 100, topping the chart in October 1986?",
        "correct": "True Colors",
        "wrong": ["Time After Time", "Change of Heart", "All Through the Night"],
        "d": 2
    },
    {
        "q": "Which 1983 Billy Joel doo-wop homage hit #1 on the Hot 100, written about his relationship with supermodel Christie Brinkley?",
        "correct": "Uptown Girl",
        "wrong": ["Tell Her About It", "An Innocent Man", "The Longest Time"],
        "d": 1
    },
    {
        "q": "What Billy Joel single from 'An Innocent Man' preceded 'Uptown Girl' by hitting #1 on the Billboard Hot 100 in September 1983?",
        "correct": "Tell Her About It",
        "wrong": ["The Longest Time", "Keeping the Faith", "Leave a Tender Moment Alone"],
        "d": 2
    },
    {
        "q": "Which Billy Joel historical montage reached #1 on the Billboard Hot 100 in late 1989, chronicling major events from 1949 to 1989?",
        "correct": "We Didn't Start the Fire",
        "wrong": ["I Go to Extremes", "The Downeaster 'Alexa'", "Pressure"],
        "d": 1
    },
    {
        "q": "Which Roxette song from Sweden became the duo's first Billboard Hot 100 #1 hit in April 1989?",
        "correct": "The Look",
        "wrong": ["Listen to Your Heart", "It Must Have Been Love", "Joyride"],
        "d": 2
    },
    {
        "q": "Which Roxette power ballad reached #1 on the Billboard Hot 100 in late 1989 and was later featured in the film 'Pretty Woman'?",
        "correct": "Listen to Your Heart",
        "wrong": ["The Look", "Dressed for Success", "Dangerous"],
        "d": 2
    },
    {
        "q": "Which Madonna dance anthem hit #1 on the Billboard Hot 100 in 1989, courting worldwide controversy for its church-themed music video?",
        "correct": "Like a Prayer",
        "wrong": ["Express Yourself", "Cherish", "Oh Father"],
        "d": 1
    }
]

if __name__ == "__main__":
    formatted = assemble_batch(QUESTIONS, 3)
    save_batch(formatted, 3)
