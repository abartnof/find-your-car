import sys
import os
sys.path.append(os.path.dirname(__file__))
from utils import assemble_batch, save_batch

QUESTIONS = [
    # 1-10
    {
        "q": "What was Mariah Carey's debut single that reached #1 on the Billboard Hot 100 for four weeks in 1990?",
        "correct": "Vision of Love",
        "wrong": ["Love Takes Time", "Someday", "I Don't Wanna Cry"],
        "d": 1
    },
    {
        "q": "How many consecutive #1 singles did Mariah Carey score on the Billboard Hot 100 from her self-titled 1990 debut album?",
        "correct": "Four",
        "wrong": ["Two", "Three", "Five"],
        "d": 2
    },
    {
        "q": "Which Mariah Carey and Boyz II Men collaboration spent a record-setting 16 weeks at #1 on the Billboard Hot 100 in 1995-1996?",
        "correct": "One Sweet Day",
        "wrong": ["End of the Road", "I'll Make Love to You", "Always Be My Baby"],
        "d": 1
    },
    {
        "q": "Which 1981 Tom Tom Club groove was heavily sampled in Mariah Carey's 1995 #1 hit 'Fantasy'?",
        "correct": "Genius of Love",
        "wrong": ["Wordy Rappinghood", "Pleasure of Love", "Lorelei"],
        "d": 2
    },
    {
        "q": "Who performed the iconic hip-hop remix verse on Mariah Carey's 'Fantasy', bridging mainstream pop and hip-hop?",
        "correct": "Ol' Dirty Bastard",
        "wrong": ["Jay-Z", "Notorious B.I.G.", "Method Man"],
        "d": 1
    },
    {
        "q": "Which Boyz II Men single broke Elvis Presley's 36-year record by spending 13 weeks at #1 on the Hot 100 in 1992?",
        "correct": "End of the Road",
        "wrong": ["It's So Hard to Say Goodbye to Yesterday", "Motownphilly", "In the Still of the Nite"],
        "d": 1
    },
    {
        "q": "Boyz II Men followed up 'End of the Road' with which 1994 ballad that spent 14 weeks at #1 on the Billboard Hot 100?",
        "correct": "I'll Make Love to You",
        "wrong": ["On Bended Knee", "Water Runs Dry", "Song for Mama"],
        "d": 1
    },
    {
        "q": "Which song replaced Boyz II Men's 'I'll Make Love to You' at #1 on the Billboard Hot 100 in December 1994?",
        "correct": "On Bended Knee by Boyz II Men",
        "wrong": ["Creep by TLC", "Take a Bow by Madonna", "Always by Bon Jovi"],
        "d": 2
    },
    {
        "q": "Which TLC anthem spent seven weeks at #1 on the Billboard Hot 100 in 1995, addressing HIV/AIDS and street crime?",
        "correct": "Waterfalls",
        "wrong": ["Creep", "No Scrubs", "Red Light Special"],
        "d": 1
    },
    {
        "q": "What phrase did TLC define in their 1999 #1 hit as 'a guy that thinks he's fly and is also known as a busta'?",
        "correct": "A scrub",
        "wrong": ["A pigeon", "A trick", "A player"],
        "d": 1
    },

    # 11-20
    {
        "q": "Which TLC member delivered the memorable rap verse on 'Waterfalls' and 'No Scrubs'?",
        "correct": "Lisa 'Left Eye' Lopes",
        "wrong": ["Rozonda 'Chilli' Thomas", "Tionne 'T-Boz' Watkins", "Da Brat"],
        "d": 1
    },
    {
        "q": "TLC's 1994 studio album became the first by an American female group to be certified Diamond by the RIAA. What was its title?",
        "correct": "CrazySexyCool",
        "wrong": ["Ooooooohhh... On the TLC Tip", "FanMail", "3D"],
        "d": 2
    },
    {
        "q": "Which Whitney Houston recording spent 14 weeks at #1 on the Billboard Hot 100 in 1992-1993, featured in 'The Bodyguard'?",
        "correct": "I Will Always Love You",
        "wrong": ["I Have Nothing", "Run to You", "I'm Every Woman"],
        "d": 1
    },
    {
        "q": "Who wrote and originally recorded 'I Will Always Love You' in 1973 before Whitney Houston's record-breaking version?",
        "correct": "Dolly Parton",
        "wrong": ["Linda Ronstadt", "Emmylou Harris", "Patsy Cline"],
        "d": 1
    },
    {
        "q": "Whitney Houston's 'The Bodyguard' soundtrack spent how many weeks at #1 on the Billboard 200 album chart?",
        "correct": "20 weeks",
        "wrong": ["12 weeks", "28 weeks", "35 weeks"],
        "d": 2
    },
    {
        "q": "Which Celine Dion power ballad served as the theme to the 1997 film 'Titanic' and debuted at #1 on the Billboard Hot 100?",
        "correct": "My Heart Will Go On",
        "wrong": ["Because You Loved Me", "The Power of Love", "It's All Coming Back to Me Now"],
        "d": 1
    },
    {
        "q": "Who wrote the soaring music for Celine Dion's 'My Heart Will Go On' alongside lyricist Will Jennings?",
        "correct": "James Horner",
        "wrong": ["David Foster", "Hans Zimmer", "John Williams"],
        "d": 2
    },
    {
        "q": "Which Celine Dion single spent six weeks at #1 on the Billboard Hot 100 in 1996, featured in the film 'Up Close & Personal'?",
        "correct": "Because You Loved Me",
        "wrong": ["The Power of Love", "It's All Coming Back to Me Now", "All by Myself"],
        "d": 2
    },
    {
        "q": "Which hit songwriter wrote Celine Dion's 'Because You Loved Me' and LeAnn Rimes' 'How Do I Live'?",
        "correct": "Diane Warren",
        "wrong": ["Carole Bayer Sager", "Cynthia Weil", "Linda Perry"],
        "d": 2
    },
    {
        "q": "What was Britney Spears' debut single, which reached #1 on the Billboard Hot 100 in January 1999?",
        "correct": "...Baby One More Time",
        "wrong": ["Sometimes", "(You Drive Me) Crazy", "Born to Make You Happy"],
        "d": 1
    },

    # 21-30
    {
        "q": "Who wrote and co-produced Britney Spears' breakthrough smash '...Baby One More Time' at Cheiron Studios in Sweden?",
        "correct": "Max Martin",
        "wrong": ["Denniz Pop", "Rami Yacoub", "Dr. Luke"],
        "d": 2
    },
    {
        "q": "Which Backstreet Boys song spent 39 weeks on the Hot 100 and peaked at #6 in 1999, becoming their signature anthem?",
        "correct": "I Want It That Way",
        "wrong": ["Quit Playing Games (with My Heart)", "As Long as You Love Me", "Larger Than Life"],
        "d": 1
    },
    {
        "q": "What Backstreet Boys album sold over 1.13 million copies in its first week in the US in May 1999, debuting at #1 on the Billboard 200?",
        "correct": "Millennium",
        "wrong": ["Backstreet Boys", "Black & Blue", "Never Gone"],
        "d": 2
    },
    {
        "q": "Which *NSYNC album shattered Millennium's first-week sales record by selling 2.4 million copies in March 2000?",
        "correct": "No Strings Attached",
        "wrong": ["*NSYNC", "Celebrity", "Home for Christmas"],
        "d": 1
    },
    {
        "q": "What was *NSYNC's only #1 single on the US Billboard Hot 100, reaching the top in July 2000?",
        "correct": "It's Gonna Be Me",
        "wrong": ["Bye Bye Bye", "This I Promise You", "Tearin' Up My Heart"],
        "d": 1
    },
    {
        "q": "Which Toni Braxton ballad spent 11 weeks at #1 on the Billboard Hot 100 in 1996-1997, becoming one of the biggest hits in chart history?",
        "correct": "Un-Break My Heart",
        "wrong": ["You're Makin' Me High", "Breathe Again", "Another Sad Love Song"],
        "d": 1
    },
    {
        "q": "Which 1996 double A-side single gave Toni Braxton her first Billboard Hot 100 #1 hit?",
        "correct": "You're Makin' Me High / Let It Flow",
        "wrong": ["Breathe Again / Another Sad Love Song", "He Wasn't Man Enough / Spanish Guitar", "How Many Ways / I Belong to You"],
        "d": 2
    },
    {
        "q": "Which Alanis Morissette album spent 12 non-consecutive weeks at #1 on the Billboard 200 and won four Grammy Awards in 1996?",
        "correct": "Jagged Little Pill",
        "wrong": ["Supposed Former Infatuation Junkie", "Under Rug Swept", "Flavors of Entanglement"],
        "d": 1
    },
    {
        "q": "Which Flea and Dave Navarro-assisted single from 'Jagged Little Pill' broke Alanis Morissette into the alternative rock mainstream?",
        "correct": "You Oughta Know",
        "wrong": ["Hand in My Pocket", "Ironic", "You Learn"],
        "d": 2
    },
    {
        "q": "Which Alanis Morissette track peaked at #4 on the Billboard Hot 100 in 1996, despite music critics pointing out its lyrical examples were not actual ironies?",
        "correct": "Ironic",
        "wrong": ["Head over Feet", "Hand in My Pocket", "Thank U"],
        "d": 1
    },

    # 31-40
    {
        "q": "What debut single by the Spice Girls reached #1 on the Billboard Hot 100 for four weeks in early 1997?",
        "correct": "Wannabe",
        "wrong": ["Say You'll Be There", "2 Become 1", "Spice Up Your Life"],
        "d": 1
    },
    {
        "q": "Which Spice Girls member was known as 'Posh Spice'?",
        "correct": "Victoria Beckham",
        "wrong": ["Melanie Brown", "Emma Bunton", "Geri Halliwell"],
        "d": 1
    },
    {
        "q": "What 1997 Shania Twain album became the best-selling studio album by a female artist in history, spending 50 weeks in the Billboard 200 top 10?",
        "correct": "Come On Over",
        "wrong": ["The Woman in Me", "Up!", "Now"],
        "d": 1
    },
    {
        "q": "Which Shania Twain ballad reached #2 on the Billboard Hot 100 for nine weeks in 1998, held back only by 'The Boy Is Mine'?",
        "correct": "You're Still the One",
        "wrong": ["From This Moment On", "That Don't Impress Me Much", "Man! I Feel Like a Woman!"],
        "d": 2
    },
    {
        "q": "Who produced and co-wrote Shania Twain's record-breaking blockbuster album 'Come On Over'?",
        "correct": "Robert John 'Mutt' Lange",
        "wrong": ["David Foster", "Max Martin", "Rick Rubin"],
        "d": 2
    },
    {
        "q": "Which Ricky Martin smash hit sparked the 'Latin Pop explosion' of 1999 by spending five weeks at #1 on the Billboard Hot 100?",
        "correct": "Livin' la Vida Loca",
        "wrong": ["She's All I Ever Had", "The Cup of Life", "Shake Your Bon-Bon"],
        "d": 1
    },
    {
        "q": "What was Destiny's Child's first Billboard Hot 100 #1 hit, topping the chart in July 1999?",
        "correct": "Bills, Bills, Bills",
        "wrong": ["Say My Name", "No, No, No Pt. 2", "Jumpin', Jumpin'"],
        "d": 2
    },
    {
        "q": "Which Destiny's Child song won two Grammy Awards and spent three weeks at #1 on the Billboard Hot 100 in spring 2000?",
        "correct": "Say My Name",
        "wrong": ["Survivor", "Independent Women Part I", "Bootylicious"],
        "d": 1
    },
    {
        "q": "Which Brandy and Monica duet spent 13 consecutive weeks at #1 on the Billboard Hot 100 during the summer of 1998?",
        "correct": "The Boy Is Mine",
        "wrong": ["Have You Ever?", "Angel of Mine", "Almost Doesn't Count"],
        "d": 1
    },
    {
        "q": "Who produced the 1998 R&B smash duet 'The Boy Is Mine' by Brandy and Monica?",
        "correct": "Rodney 'Darkchild' Jerkins",
        "wrong": ["Teddy Riley", "Babyface", "Dallas Austin"],
        "d": 2
    },

    # 41-50
    {
        "q": "Which pop trio of brothers scored a three-week Billboard Hot 100 #1 hit in May 1997 with 'MMMBop'?",
        "correct": "Hanson",
        "wrong": ["The Moffatts", "Jonas Brothers", "BBMak"],
        "d": 1
    },
    {
        "q": "How old was drummer Zac Hanson when 'MMMBop' reached #1 on the Hot 100, making him one of the youngest chart-topping songwriters ever?",
        "correct": "11 years old",
        "wrong": ["8 years old", "14 years old", "16 years old"],
        "d": 3
    },
    {
        "q": "Which Australian duo spent four weeks at #1 on the Billboard Hot 100 in 1998 with the romantic ballad 'Truly Madly Deeply'?",
        "correct": "Savage Garden",
        "wrong": ["Crowded House", "Air Supply", "INXS"],
        "d": 2
    },
    {
        "q": "What was Savage Garden's second #1 single on the US Billboard Hot 100, topping the chart for four weeks in early 2000?",
        "correct": "I Knew I Loved You",
        "wrong": ["To the Moon and Back", "Crash and Burn", "The Animal Song"],
        "d": 2
    },
    {
        "q": "Which Natalie Imbruglia acoustic pop track reached #1 on the Billboard Hot 100 Airplay chart for 14 weeks in 1998?",
        "correct": "Torn",
        "wrong": ["Wishing I Was There", "Smoke", "Big Mistake"],
        "d": 1
    },
    {
        "q": "Which female vocal trio, consisting of Carnie Wilson, Wendy Wilson, and Chynna Phillips, scored three #1 hits from their 1990 debut?",
        "correct": "Wilson Phillips",
        "wrong": ["En Vogue", "Exposé", "The Pointer Sisters"],
        "d": 2
    },
    {
        "q": "What Wilson Phillips hit spent two weeks at #1 and was crowned the Billboard Year-End #1 single of 1990?",
        "correct": "Hold On",
        "wrong": ["Release Me", "Impulsive", "You're in Love"],
        "d": 2
    },
    {
        "q": "Which R&B vocal group scored Top 5 hits in the 1990s with 'Hold On', 'My Lovin' (You're Never Gonna Get It)', and 'Don't Let Go (Love)'?",
        "correct": "En Vogue",
        "wrong": ["SWV", "Total", "Xscape"],
        "d": 2
    },
    {
        "q": "Which vocal quartet spent 11 weeks at #1 on the Billboard Hot 100 in 1994 with their pop cover of John Michael Montgomery's 'I Swear'?",
        "correct": "All-4-One",
        "wrong": ["Boyz II Men", "Color Me Badd", "Shai"],
        "d": 2
    },
    {
        "q": "Which R&B group topped the Billboard Hot 100 in 1991 with 'All 4 Love' after their debut single 'I Wanna Sex You Up' reached #2?",
        "correct": "Color Me Badd",
        "wrong": ["Hi-Five", "Troop", "Jodeci"],
        "d": 2
    },

    # 51-60
    {
        "q": "Which Vanessa Williams ballad spent five consecutive weeks at #1 on the Billboard Hot 100 in early 1992?",
        "correct": "Save the Best for Last",
        "wrong": ["Colors of the Wind", "Love Is", "The Right Stuff"],
        "d": 2
    },
    {
        "q": "Which Bryan Adams power ballad spent seven weeks at #1 on the Billboard Hot 100 in 1991, featured in 'Robin Hood: Prince of Thieves'?",
        "correct": "(Everything I Do) I Do It for You",
        "wrong": ["Please Forgive Me", "Have You Ever Really Loved a Woman?", "All for Love"],
        "d": 1
    },
    {
        "q": "Bryan Adams teamed up with Rod Stewart and Sting for which 1994 #1 hit from 'The Three Musketeers' soundtrack?",
        "correct": "All for Love",
        "wrong": ["(Everything I Do) I Do It for You", "Have You Ever Really Loved a Woman?", "Can't Stop This Thing We Started"],
        "d": 2
    },
    {
        "q": "Which Sinéad O'Connor emotional cover spent four weeks at #1 on the Billboard Hot 100 in 1990, originally written by Prince?",
        "correct": "Nothing Compares 2 U",
        "wrong": ["The Emperor's New Clothes", "Mandinka", "Thank You for Hearing Me"],
        "d": 1
    },
    {
        "q": "In which iconic close-up music video did tears famously roll down Sinéad O'Connor's cheeks as she sang about lost love?",
        "correct": "Nothing Compares 2 U",
        "wrong": ["Torn", "Ironic", "Breathe Again"],
        "d": 1
    },
    {
        "q": "What Roxette power ballad spent two weeks at #1 on the Billboard Hot 100 in June 1990, featured in the film 'Pretty Woman'?",
        "correct": "It Must Have Been Love",
        "wrong": ["Listen to Your Heart", "Joyride", "Fading Like a Flower"],
        "d": 1
    },
    {
        "q": "Which Madonna dance-pop track spent three weeks at #1 on the Billboard Hot 100 in 1990, inspired by Harlem ballroom dance culture?",
        "correct": "Vogue",
        "wrong": ["Justify My Love", "Deeper and Deeper", "Secret"],
        "d": 1
    },
    {
        "q": "Which Madonna single became the first music video banned by MTV due to sexually provocative imagery, later reaching #1 in January 1991?",
        "correct": "Justify My Love",
        "wrong": ["Erotica", "Like a Prayer", "Human Nature"],
        "d": 2
    },
    {
        "q": "Who co-wrote and produced Madonna's controversial #1 single 'Justify My Love'?",
        "correct": "Lenny Kravitz",
        "wrong": ["Shep Pettibone", "Babyface", "Dallas Austin"],
        "d": 2
    },
    {
        "q": "What Janet Jackson single spent eight weeks at #1 on the Billboard Hot 100 in 1993, sampling 'Papa Don't Take No Mess' by James Brown?",
        "correct": "That's the Way Love Goes",
        "wrong": ["Again", "Any Time, Any Place", "If"],
        "d": 2
    },

    # 61-70
    {
        "q": "Which Janet Jackson ballad reached #1 on the Billboard Hot 100 in late 1993, featured in the film 'Poetic Justice' in which she starred?",
        "correct": "Again",
        "wrong": ["That's the Way Love Goes", "Because of Love", "Any Time, Any Place"],
        "d": 2
    },
    {
        "q": "Which Janet Jackson upbeat dance track hit #1 on the Billboard Hot 100 in early 1998, written as a tribute to friends who died of AIDS?",
        "correct": "Together Again",
        "wrong": ["Got 'til It's Gone", "I Get Lonely", "Go Deep"],
        "d": 2
    },
    {
        "q": "Which 1997 Cher dance-pop anthem spent four weeks at #1 on the Billboard Hot 100 and popularized the extreme use of Auto-Tune on pop vocals?",
        "correct": "Believe",
        "wrong": ["Strong Enough", "All or Nothing", "If I Could Turn Back Time"],
        "d": 1
    },
    {
        "q": "How old was Cher when 'Believe' reached #1 in March 1999, making her the oldest female solo artist to top the Hot 100 at age 52?",
        "correct": "52 years old",
        "wrong": ["48 years old", "56 years old", "60 years old"],
        "d": 2
    },
    {
        "q": "Which 1999 smash hit spent 12 weeks at #1 on the Billboard Hot 100 for Santana featuring Rob Thomas of Matchbox 20?",
        "correct": "Smooth",
        "wrong": ["Maria Maria", "Black Magic Woman", "Oye Como Va"],
        "d": 1
    },
    {
        "q": "Which Santana album spent 12 non-consecutive weeks at #1 on the Billboard 200 and won nine Grammy Awards in 2000?",
        "correct": "Supernatural",
        "wrong": ["Abraxas", "Caravanserai", "Shaman"],
        "d": 1
    },
    {
        "q": "What was the second #1 single from Santana's 'Supernatural', featuring The Product G&B and sampling 'Wu-Tang Clan Ain't Nuthing ta F' Wit'?",
        "correct": "Maria Maria",
        "wrong": ["Smooth", "Corazón Espinado", "Put Your Lights On"],
        "d": 2
    },
    {
        "q": "Which Christina Aguilera debut single reached #1 on the Billboard Hot 100 in October 1999, spending five weeks at the top?",
        "correct": "Genie in a Bottle",
        "wrong": ["What a Girl Wants", "I Turn to You", "Come On Over Baby (All I Want Is You)"],
        "d": 1
    },
    {
        "q": "What was Christina Aguilera's second consecutive Billboard Hot 100 #1 single, reaching the summit in January 2000?",
        "correct": "What a Girl Wants",
        "wrong": ["Come On Over Baby", "Genie in a Bottle", "I Turn to You"],
        "d": 2
    },
    {
        "q": "Which teen pop star hit #1 on the Billboard Hot 100 in 1998 with '...Baby One More Time' while her album debuted at #1 on the Billboard 200 the same week?",
        "correct": "Britney Spears",
        "wrong": ["Christina Aguilera", "Jessica Simpson", "Mandy Moore"],
        "d": 1
    },

    # 71-80
    {
        "q": "Which Spanish duo topped the Billboard Hot 100 for 14 weeks in 1996 with the Bayside Boys remix of 'Macarena'?",
        "correct": "Los del Río",
        "wrong": ["Gipsy Kings", "Los Lobos", "Azúcar Moreno"],
        "d": 1
    },
    {
        "q": "Which LeAnn Rimes country-pop crossover spent a тогда-record 69 weeks on the Billboard Hot 100, peaking at #2 in 1997?",
        "correct": "How Do I Live",
        "wrong": ["Blue", "One Way Ticket", "I Need You"],
        "d": 2
    },
    {
        "q": "Which artist released a competing version of 'How Do I Live' on the exact same day as LeAnn Rimes, reaching #7 on the Hot 100 for the movie 'Con Air'?",
        "correct": "Trisha Yearwood",
        "wrong": ["Faith Hill", "Martina McBride", "Reba McEntire"],
        "d": 3
    },
    {
        "q": "Which Faith Hill crossover smash peaked at #2 on the Billboard Hot 100 for four weeks and was the Billboard Year-End #1 single of 2000?",
        "correct": "Breathe",
        "wrong": ["This Kiss", "The Way You Love Me", "There You'll Be"],
        "d": 2
    },
    {
        "q": "Which Jewel acoustic ballad became a multi-format juggernaut, spending 65 weeks on the Hot 100 and peaking at #2 in 1997?",
        "correct": "Foolish Games / You Were Meant for Me",
        "wrong": ["Who Will Save Your Soul", "Hands", "Down So Long"],
        "d": 2
    },
    {
        "q": "What 1994 debut album by Jewel sold over 12 million copies in the US and peaked at #4 on the Billboard 200?",
        "correct": "Pieces of You",
        "wrong": ["Spirit", "This Way", "0304"],
        "d": 2
    },
    {
        "q": "Which Monica ballad spent four weeks at #1 on the Billboard Hot 100 in early 1999, written by Diane Warren?",
        "correct": "Angel of Mine",
        "wrong": ["The First Night", "Before You Walk Out of My Life", "For You I Will"],
        "d": 2
    },
    {
        "q": "What was Monica's first solo Billboard Hot 100 #1 hit, produced by Jermaine Dupri in 1998?",
        "correct": "The First Night",
        "wrong": ["Don't Take It Personal", "Angel of Mine", "So Gone"],
        "d": 2
    },
    {
        "q": "Which Brandy ballad, written by Diane Warren and produced by David Foster, topped the Billboard Hot 100 for two weeks in early 1999?",
        "correct": "Have You Ever?",
        "wrong": ["Baby", "I Wanna Be Down", "Sitting Up in My Room"],
        "d": 2
    },
    {
        "q": "Which R. Kelly ballad from the 1996 film 'Space Jam' peaked at #2 on the Billboard Hot 100 and won three Grammy Awards?",
        "correct": "I Believe I Can Fly",
        "wrong": ["Bump N' Grind", "Ignition (Remix)", "Step in the Name of Love"],
        "d": 1
    },

    # 81-90
    {
        "q": "What 1994 R. Kelly slow jam spent four weeks at #1 on the Billboard Hot 100, opening with the phrase 'My mind is telling me no'?",
        "correct": "Bump N' Grind",
        "wrong": ["Your Body's Callin'", "Sex Me", "Seems Like You're Ready"],
        "d": 2
    },
    {
        "q": "Which Montell Jordan party track reached #1 on the Billboard Hot 100 in 1995, famous for the opening line 'This is how we do it'?",
        "correct": "This Is How We Do It",
        "wrong": ["Somethin' 4 da Honeyz", "Let's Ride", "Get It On Tonite"],
        "d": 1
    },
    {
        "q": "Which Slick Rick classic song was sampled as the foundation for Montell Jordan's #1 hit 'This Is How We Do It'?",
        "correct": "Children's Story",
        "wrong": ["La Di Da Di", "Mona Lisa", "Hey Young World"],
        "d": 2
    },
    {
        "q": "Which Blackstreet hit featuring Dr. Dre and Queen Pen spent four weeks at #1 on the Billboard Hot 100 in late 1996?",
        "correct": "No Diggity",
        "wrong": ["Before I Let You Go", "Don't Leave Me", "Fix"],
        "d": 1
    },
    {
        "q": "Which Bill Withers track was sampled for the unmistakable rhythm and piano loop in Blackstreet's 'No Diggity'?",
        "correct": "Grandma's Hands",
        "wrong": ["Ain't No Sunshine", "Lean on Me", "Use Me"],
        "d": 2
    },
    {
        "q": "Who was the pioneering New Jack Swing producer who founded Blackstreet and co-produced 'No Diggity'?",
        "correct": "Teddy Riley",
        "wrong": ["Babyface", "Dallas Austin", "L.A. Reid"],
        "d": 2
    },
    {
        "q": "Which Deborah Cox R&B ballad spent a then-record 14 weeks at #1 on the Hot R&B Singles chart and peaked at #2 on the Hot 100 in 1998?",
        "correct": "Nobody's Supposed to Be Here",
        "wrong": ["Sentimental", "Where Do We Go from Here", "We Can't Be Friends"],
        "d": 2
    },
    {
        "q": "Which K-Ci & JoJo slow ballad spent three weeks at #1 on the Billboard Hot 100 in 1998, becoming an all-time wedding favorite?",
        "correct": "All My Life",
        "wrong": ["Tell Me It's Real", "Crazy", "Life"],
        "d": 1
    },
    {
        "q": "Before performing as a duo, K-Ci & JoJo were the lead vocalists for which multi-platinum 1990s R&B group?",
        "correct": "Jodeci",
        "wrong": ["Dru Hill", "Guy", "112"],
        "d": 1
    },
    {
        "q": "What 1999 Dru Hill lead singer Sisqó smash reached #3 on the Billboard Hot 100, celebrating female underwear?",
        "correct": "Thong Song",
        "wrong": ["Incomplete", "Got to Get It", "Unleash the Dragon"],
        "d": 1
    },

    # 91-100
    {
        "q": "What Sisqó ballad hit #1 on the Billboard Hot 100 for two weeks in August 2000, following the success of 'Thong Song'?",
        "correct": "Incomplete",
        "wrong": ["How Deep Is Your Love", "Never Make a Promise", "Tell Me"],
        "d": 2
    },
    {
        "q": "Which Next party anthem topped the Billboard Hot 100 for five weeks in 1998, asking 'Too close? Why you all in my ear?'",
        "correct": "Too Close",
        "wrong": ["Wifey", "Butta Love", "I Still Love You"],
        "d": 1
    },
    {
        "q": "What was the Billboard Year-End #1 single of 1998, finishing ahead of 'The Boy Is Mine'?",
        "correct": "Too Close by Next",
        "wrong": ["Truly Madly Deeply by Savage Garden", "You're Still the One by Shania Twain", "My Way by Usher"],
        "d": 2
    },
    {
        "q": "Which Usher single from his 1997 album 'My Way' was his first #1 on the Billboard Hot 100?",
        "correct": "Nice & Slow",
        "wrong": ["You Make Me Wanna...", "My Way", "U Remind Me"],
        "d": 2
    },
    {
        "q": "Which Usher ballad peaked at #2 on the Billboard Hot 100 for seven weeks in 1997 and spent 11 weeks at #1 on the R&B chart?",
        "correct": "You Make Me Wanna...",
        "wrong": ["Nice & Slow", "My Way", "Think of You"],
        "d": 2
    },
    {
        "q": "Which 1990 Mariah Carey Christmas recording became a perennial Billboard Hot 100 #1 hit decades after its initial release?",
        "correct": "All I Want for Christmas Is You",
        "wrong": ["Christmas (Baby Please Come Home)", "O Holy Night", "Miss You Most (At Christmas Time)"],
        "d": 1
    },
    {
        "q": "In which year did Mariah Carey's 'All I Want for Christmas Is You' finally reach #1 on the Billboard Hot 100, 25 years after its debut?",
        "correct": "2019",
        "wrong": ["2015", "2017", "2021"],
        "d": 2
    },
    {
        "q": "Which Sixpence None the Richer pop hit reached #2 on the Billboard Hot 100 in 1999, featured in the teen movie 'She's All That'?",
        "correct": "Kiss Me",
        "wrong": ["There She Goes", "Breathe Your Name", "Don't Dream It's Over"],
        "d": 1
    },
    {
        "q": "Which Shawn Colvin folk-pop story song won Grammy Awards for Record and Song of the Year and peaked at #7 on the Hot 100 in 1997?",
        "correct": "Sunny Came Home",
        "wrong": ["You and the Mona Lisa", "Get Out of This House", "Round of Blues"],
        "d": 2
    },
    {
        "q": "Which Paula Cole song peaked at #7 on the Billboard Hot 100 in 1997, asking where all the happy endings and cowboys had gone?",
        "correct": "Where Have All the Cowboys Gone?",
        "wrong": ["I Don't Want to Wait", "Me", "Feelin' Love"],
        "d": 2
    }
]

if __name__ == "__main__":
    formatted = assemble_batch(QUESTIONS, 4)
    save_batch(formatted, 4)
