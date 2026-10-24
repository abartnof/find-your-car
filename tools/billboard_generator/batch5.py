import sys
import os
sys.path.append(os.path.dirname(__file__))
from utils import assemble_batch, save_batch

QUESTIONS = [
    # 1-10
    {
        "q": "Which Nirvana album knocked Michael Jackson's 'Dangerous' from the #1 spot on the Billboard 200 in January 1992?",
        "correct": "Nevermind",
        "wrong": ["In Utero", "Bleach", "Incesticide"],
        "d": 1
    },
    {
        "q": "What peak position did Nirvana's grunge anthem 'Smells Like Teen Spirit' reach on the Billboard Hot 100 in early 1992?",
        "correct": "#6",
        "wrong": ["#1", "#2", "#10"],
        "d": 2
    },
    {
        "q": "Who produced Nirvana's monumental 1991 album 'Nevermind' at Sound City Studios?",
        "correct": "Butch Vig",
        "wrong": ["Steve Albini", "Rick Rubin", "Jack Endino"],
        "d": 2
    },
    {
        "q": "Which Pearl Jam album sold over 950,000 copies in its first week in 1993, setting a Billboard 200 record at the time?",
        "correct": "Vs.",
        "wrong": ["Ten", "Vitalogy", "No Code"],
        "d": 2
    },
    {
        "q": "What 1994 Pearl Jam single reached #2 on the Billboard Mainstream Rock chart and was the first song to reach #1 on the Modern Rock chart without being commercially available as a US physical single?",
        "correct": "Better Man",
        "wrong": ["Daughter", "Corduroy", "Spin the Black Circle"],
        "d": 3
    },
    {
        "q": "Which Pearl Jam song from 'Ten' tells the tragic story of a bullied high school student and earned four MTV Video Music Awards in 1993?",
        "correct": "Jeremy",
        "wrong": ["Alive", "Even Flow", "Black"],
        "d": 1
    },
    {
        "q": "Which Soundgarden hit from their 1994 Billboard 200 #1 album 'Superunknown' won a Grammy for Best Hard Rock Performance?",
        "correct": "Black Hole Sun",
        "wrong": ["Spoonman", "Fell on Black Days", "The Day I Tried to Live"],
        "d": 2
    },
    {
        "q": "Which 1994 Alice in Chains release became the first EP in Billboard chart history to debut at #1 on the Billboard 200?",
        "correct": "Jar of Flies",
        "wrong": ["Sap", "Dirt", "Facelift"],
        "d": 2
    },
    {
        "q": "Which Green Day album sold over 10 million copies in the US and peaked at #2 on the Billboard 200 in 1994?",
        "correct": "Dookie",
        "wrong": ["Insomniac", "Nimrod", "American Idiot"],
        "d": 1
    },
    {
        "q": "Which acoustic Green Day ballad from 1997 became an inescapable graduation anthem, subtitled 'Time of Your Life'?",
        "correct": "Good Riddance",
        "wrong": ["Wake Me Up When September Ends", "Basket Case", "Boulevard of Broken Dreams"],
        "d": 1
    },

    # 11-20
    {
        "q": "Which Red Hot Chili Peppers ballad peaked at #2 on the Billboard Hot 100 in 1992, recounting Anthony Kiedis's struggles with addiction in Los Angeles?",
        "correct": "Under the Bridge",
        "wrong": ["Give It Away", "Soul to Squeeze", "Breaking the Girl"],
        "d": 1
    },
    {
        "q": "Who produced the Red Hot Chili Peppers' breakthrough 1991 album 'Blood Sugar Sex Magik'?",
        "correct": "Rick Rubin",
        "wrong": ["George Clinton", "Michael Beinhorn", "Brendan O'Brien"],
        "d": 2
    },
    {
        "q": "Which Red Hot Chili Peppers track won the Grammy for Best Rock Song in 2000 and spent 16 consecutive weeks at #1 on the Modern Rock Tracks chart?",
        "correct": "Scar Tissue",
        "wrong": ["Otherside", "Californication", "Around the World"],
        "d": 2
    },
    {
        "q": "What was 2Pac's first Billboard Hot 100 #1 single, a double A-side featuring Dr. Dre and Roger Troutman that topped the chart in 1996?",
        "correct": "California Love / How Do U Want It",
        "wrong": ["Dear Mama", "Keep Ya Head Up", "I Get Around"],
        "d": 1
    },
    {
        "q": "Which 2Pac double album debuted at #1 on the Billboard 200 in February 1996, becoming one of hip-hop's definitive releases?",
        "correct": "All Eyez on Me",
        "wrong": ["Me Against the World", "The Don Killuminati", "Strictly 4 My N.I.G.G.A.Z."],
        "d": 1
    },
    {
        "q": "What 1995 2Pac tribute to Afeni Shakur peaked at #9 on the Billboard Hot 100 and was added to the National Recording Registry?",
        "correct": "Dear Mama",
        "wrong": ["Brenda's Got a Baby", "Keep Ya Head Up", "So Many Tears"],
        "d": 2
    },
    {
        "q": "What was The Notorious B.I.G.'s first single to hit #1 on the Billboard Hot 100, reaching the top posthumously in May 1997?",
        "correct": "Hypnotize",
        "wrong": ["Mo Money Mo Problems", "Juicy", "Big Poppa"],
        "d": 1
    },
    {
        "q": "Which The Notorious B.I.G. smash hit replaced 'Hypnotize' at #1 in 1997, featuring Puff Daddy and Mase?",
        "correct": "Mo Money Mo Problems",
        "wrong": ["Going Back to Cali", "Sky's the Limit", "Juicy"],
        "d": 1
    },
    {
        "q": "Which 1980 Diana Ross disco song was sampled as the foundational backing track for 'Mo Money Mo Problems'?",
        "correct": "I'm Coming Out",
        "wrong": ["Upside Down", "Love Hangover", "My Old Piano"],
        "d": 2
    },
    {
        "q": "The Notorious B.I.G.'s 1997 double album debuted at #1 on the Billboard 200 just weeks after his murder. What was its title?",
        "correct": "Life After Death",
        "wrong": ["Ready to Die", "Born Again", "Duets: The Final Chapter"],
        "d": 1
    },

    # 21-30
    {
        "q": "Which Puff Daddy and Faith Evans collaboration spent 11 weeks at #1 on the Billboard Hot 100 in 1997 as a tribute to The Notorious B.I.G.?",
        "correct": "I'll Be Missing You",
        "wrong": ["Can't Nobody Hold Me Down", "Been Around the World", "Come with Me"],
        "d": 1
    },
    {
        "q": "Which 1983 song by The Police was sampled and replayed in Puff Daddy's 'I'll Be Missing You'?",
        "correct": "Every Breath You Take",
        "wrong": ["Roxanne", "Message in a Bottle", "King of Pain"],
        "d": 1
    },
    {
        "q": "Which Coolio song featuring L.V. spent three weeks at #1 on the Billboard Hot 100 and was the Billboard Year-End #1 single of 1995?",
        "correct": "Gangsta's Paradise",
        "wrong": ["Fantastic Voyage", "1, 2, 3, 4 (Sumpin' New)", "C U When U Get There"],
        "d": 1
    },
    {
        "q": "Which 1976 Stevie Wonder song from 'Songs in the Key of Life' was reworked by Coolio for 'Gangsta's Paradise'?",
        "correct": "Pastime Paradise",
        "wrong": ["Village Ghetto Land", "Living for the City", "Joy Inside My Tears"],
        "d": 2
    },
    {
        "q": "In which Michelle Pfeiffer movie was Coolio's 'Gangsta's Paradise' the lead soundtrack single?",
        "correct": "Dangerous Minds",
        "wrong": ["Boyz n the Hood", "Juice", "Menace II Society"],
        "d": 1
    },
    {
        "q": "Which Sir Mix-a-Lot rap ode to curvy women spent five weeks at #1 on the Billboard Hot 100 in 1992?",
        "correct": "Baby Got Back",
        "wrong": ["Posse on Broadway", "My Hooptie", "Testarossa"],
        "d": 1
    },
    {
        "q": "What MC Hammer album spent 21 consecutive weeks at #1 on the Billboard 200 in 1990, the first rap album to achieve Diamond status?",
        "correct": "Please Hammer Don't Hurt 'Em",
        "wrong": ["Let's Get It Started", "Too Legit to Quit", "The Funky Headhunter"],
        "d": 1
    },
    {
        "q": "Which Rick James funk classic was heavily sampled in MC Hammer's 1990 hit 'U Can't Touch This'?",
        "correct": "Super Freak",
        "wrong": ["Give It to Me Baby", "Mary Jane", "You and I"],
        "d": 1
    },
    {
        "q": "What Vanilla Ice track was the first hip-hop single to top the Billboard Hot 100, reaching the summit in November 1990?",
        "correct": "Ice Ice Baby",
        "wrong": ["Play That Funky Music", "Ninja Rap", "Cool as Ice"],
        "d": 1
    },
    {
        "q": "Which Queen and David Bowie song provided the bassline loop for Vanilla Ice's 'Ice Ice Baby'?",
        "correct": "Under Pressure",
        "wrong": ["Another One Bites the Dust", "Radio Ga Ga", "Fame"],
        "d": 1
    },

    # 31-40
    {
        "q": "Which hip-hop trio's 1996 album 'The Score' reached #1 on the Billboard 200 and won Best Rap Album at the Grammys?",
        "correct": "Fugees",
        "wrong": ["A Tribe Called Quest", "De La Soul", "Digable Planets"],
        "d": 1
    },
    {
        "q": "Which member of Fugees released the landmark 1998 solo album 'The Miseducation of Lauryn Hill'?",
        "correct": "Lauryn Hill",
        "wrong": ["Wyclef Jean", "Pras Michel", "John Forté"],
        "d": 1
    },
    {
        "q": "What Lauryn Hill single debuted at #1 on the Billboard Hot 100 in November 1998, the first solo rap track by a female artist to do so?",
        "correct": "Doo Wop (That Thing)",
        "wrong": ["Ex-Factor", "Everything Is Everything", "Lost Ones"],
        "d": 1
    },
    {
        "q": "Which Bone Thugs-N-Harmony song spent eight weeks at #1 on the Billboard Hot 100 in 1996, dedicated to the late Eazy-E?",
        "correct": "Tha Crossroads",
        "wrong": ["1st of Tha Month", "Foe Tha Love of $", "Thuggish Ruggish Bone"],
        "d": 1
    },
    {
        "q": "Which No Doubt album reached #1 on the Billboard 200 in December 1996, buoyed by the smash hit 'Don't Speak'?",
        "correct": "Tragic Kingdom",
        "wrong": ["Return of Saturn", "Rock Steady", "No Doubt"],
        "d": 1
    },
    {
        "q": "How many consecutive weeks did No Doubt's 'Don't Speak' spend at #1 on the Billboard Hot 100 Airplay chart in 1996-1997?",
        "correct": "16 weeks",
        "wrong": ["10 weeks", "12 weeks", "20 weeks"],
        "d": 2
    },
    {
        "q": "Why was No Doubt's 'Don't Speak' ineligible to chart on the Billboard Hot 100 during its initial 1996 peak run?",
        "correct": "It was never commercially released as a physical retail single in the US",
        "wrong": ["Billboard banned ska-punk songs from the chart", "Interscope Records failed to register the barcode", "It was released only as an import vinyl"],
        "d": 2
    },
    {
        "q": "Which Smash Mouth single reached #4 on the Billboard Hot 100 in 1999 and became universally known through the movie 'Shrek'?",
        "correct": "All Star",
        "wrong": ["Walkin' on the Sun", "Then the Morning Comes", "I'm a Believer"],
        "d": 1
    },
    {
        "q": "Which ska-punk band's self-titled 1996 album reached #13 on the Billboard 200 and produced the posthumous #1 Modern Rock hit 'What I Got'?",
        "correct": "Sublime",
        "wrong": ["Rancid", "Reel Big Fish", "The Mighty Mighty Bosstones"],
        "d": 2
    },
    {
        "q": "Who was the frontman of Sublime who tragically passed away shortly before the band's breakthrough album was released in 1996?",
        "correct": "Bradley Nowell",
        "wrong": ["Eric Wilson", "Bud Gaugh", "Rome Ramirez"],
        "d": 2
    },

    # 41-50
    {
        "q": "Which Counting Crows single reached #5 on the Billboard Hot 100 Airplay chart in 1994, propelled by heavy MTV rotation?",
        "correct": "Mr. Jones",
        "wrong": ["Round Here", "A Long December", "Rain King"],
        "d": 1
    },
    {
        "q": "What Irish rock band fronted by Dolores O'Riordan reached #8 on the Hot 100 with 'Linger' and had their album reach the Top 10?",
        "correct": "The Cranberries",
        "wrong": ["The Corrs", "Sinéad O'Connor & The Band", "Clannad"],
        "d": 2
    },
    {
        "q": "Which Matchbox 20 hit from 2000 spent 25 weeks in the Billboard Hot 100 top 10 and reached #1 for one week?",
        "correct": "Bent",
        "wrong": ["Push", "3AM", "Real World"],
        "d": 2
    },
    {
        "q": "What Goo Goo Dolls power ballad from the 'City of Angels' soundtrack spent a record 18 weeks at #1 on the Hot 100 Airplay chart in 1998?",
        "correct": "Iris",
        "wrong": ["Slide", "Name", "Black Balloon"],
        "d": 1
    },
    {
        "q": "What peak position did the Goo Goo Dolls' 'Iris' reach on the Hot 100 once Billboard changed rules to allow airplay-only tracks in December 1998?",
        "correct": "#9",
        "wrong": ["#1", "#3", "#15"],
        "d": 3
    },
    {
        "q": "Which Third Eye Blind track reached #4 on the Billboard Hot 100 in 1997, featuring upbeat pop melodies masking lyrics about crystal meth?",
        "correct": "Semi-Charmed Life",
        "wrong": ["Jumper", "How's It Going to Be", "Never Let You Go"],
        "d": 2
    },
    {
        "q": "Which Collective Soul single reached #11 on the Hot 100 and topped the Album Rock Tracks chart for eight weeks in 1994?",
        "correct": "Shine",
        "wrong": ["December", "The World I Know", "Gel"],
        "d": 2
    },
    {
        "q": "Which rock band's album 'Throwing Copper' reached #1 on the Billboard 200 in 1995 behind singles like 'Lightning Crashes'?",
        "correct": "Live",
        "wrong": ["Bush", "Candlebox", "Silverchair"],
        "d": 2
    },
    {
        "q": "Which Beastie Boys album debuted at #1 on the Billboard 200 in 1998, featuring the vocoder-driven hit 'Intergalactic'?",
        "correct": "Hello Nasty",
        "wrong": ["Ill Communication", "Check Your Head", "Paul's Boutique"],
        "d": 2
    },
    {
        "q": "Who directed the iconic 1970s police-parody music video for Beastie Boys' 1994 single 'Sabotage'?",
        "correct": "Spike Jonze",
        "wrong": ["David Fincher", "Michel Gondry", "Mark Romanek"],
        "d": 2
    },

    # 51-60
    {
        "q": "Which Dr. Dre debut solo album peaked at #3 on the Billboard 200 in 1993, pioneering the West Coast G-funk sound?",
        "correct": "The Chronic",
        "wrong": ["2001", "Compton", "Straight Outta Compton"],
        "d": 1
    },
    {
        "q": "Which single by Dr. Dre featuring Snoop Doggy Dogg reached #2 on the Billboard Hot 100 in early 1993?",
        "correct": "Nuthin' but a 'G' Thang",
        "wrong": ["Fuck wit Dre Day", "Let Me Ride", "Gin and Juice"],
        "d": 1
    },
    {
        "q": "What Snoop Doggy Dogg 1993 debut album became the first debut album in Billboard history to enter the Billboard 200 at #1?",
        "correct": "Doggystyle",
        "wrong": ["Tha Doggfather", "No Limit Top Dogg", "The Chronic"],
        "d": 1
    },
    {
        "q": "Which Warren G and Nate Dogg track reached #2 on the Billboard Hot 100 in 1994, sampling Michael McDonald's 'I Keep Forgettin''?",
        "correct": "Regulate",
        "wrong": ["This D.J.", "Do You See", "Ain't No Fun"],
        "d": 1
    },
    {
        "q": "Which Jay-Z single from 1998 sampled 'It's the Hard Knock Life' from the musical 'Annie' and peaked at #15 on the Hot 100?",
        "correct": "Hard Knock Life (Ghetto Anthem)",
        "wrong": ["Can I Get A...", "Big Pimpin'", "Dead Presidents"],
        "d": 2
    },
    {
        "q": "Which 1998 Jay-Z album became his first of 14 albums to reach #1 on the Billboard 200 chart?",
        "correct": "Vol. 2... Hard Knock Life",
        "wrong": ["Reasonable Doubt", "In My Lifetime, Vol. 1", "The Blueprint"],
        "d": 2
    },
    {
        "q": "Which rock band reached #2 on the Billboard Hot 100 in 1998 with 'Iris' and also scored a #8 hit with 'Slide'?",
        "correct": "Goo Goo Dolls",
        "wrong": ["Matchbox 20", "Third Eye Blind", "Semisonic"],
        "d": 2
    },
    {
        "q": "Which Semisonic alt-rock track reached #1 on the Modern Rock chart in 1998, famously closing bars with 'You don't have to go home but you can't stay here'?",
        "correct": "Closing Time",
        "wrong": ["Singing in My Sleep", "Secret Smile", "Chemistry"],
        "d": 1
    },
    {
        "q": "Which Fastball song reached #1 on the Modern Rock Tracks chart in 1998, inspired by the true disappearance of an elderly Texas couple?",
        "correct": "The Way",
        "wrong": ["Fire Escape", "Out of My Head", "Warm Fuzzy Feeling"],
        "d": 2
    },
    {
        "q": "Which Marcy Playground single spent 15 weeks at #1 on the Modern Rock chart and reached #8 on the Billboard Hot 100 in 1998?",
        "correct": "Sex and Candy",
        "wrong": ["Saint Joe on the School Bus", "Sherry Fraser", "Opium"],
        "d": 2
    },

    # 61-70
    {
        "q": "Which alternative rock band hit #1 on the Billboard 200 in 1994 with their album 'Purple', featuring 'Interstate Love Song'?",
        "correct": "Stone Temple Pilots",
        "wrong": ["Soundgarden", "Alice in Chains", "Bush"],
        "d": 2
    },
    {
        "q": "How many consecutive weeks did Stone Temple Pilots' 'Interstate Love Song' spend at #1 on the Mainstream Rock Tracks chart?",
        "correct": "15 weeks",
        "wrong": ["8 weeks", "11 weeks", "20 weeks"],
        "d": 3
    },
    {
        "q": "Which British rock band fronted by Gavin Rossdale reached #1 on the Billboard 200 in 1996 with 'Razorblade Suitcase'?",
        "correct": "Bush",
        "wrong": ["Oasis", "Blur", "Silverchair"],
        "d": 2
    },
    {
        "q": "Which Oasis anthem reached #8 on the Billboard Hot 100 in 1996, becoming the band's highest-charting US single?",
        "correct": "Wonderwall",
        "wrong": ["Don't Look Back in Anger", "Champagne Supernova", "Live Forever"],
        "d": 1
    },
    {
        "q": "Which Oasis album reached #4 on the Billboard 200 in 1996 and sold over four million copies in the US?",
        "correct": "(What's the Story) Morning Glory?",
        "wrong": ["Definitely Maybe", "Be Here Now", "Standing on the Shoulder of Giants"],
        "d": 2
    },
    {
        "q": "Which Foo Fighters song from their 1997 album 'The Colour and the Shape' peaked at #3 on the Modern Rock chart and became their signature song?",
        "correct": "Everlong",
        "wrong": ["My Hero", "Monkey Wrench", "Big Me"],
        "d": 1
    },
    {
        "q": "Which former Nirvana drummer formed Foo Fighters in late 1994 following the death of Kurt Cobain?",
        "correct": "Dave Grohl",
        "wrong": ["Krist Novoselic", "Pat Smear", "Taylor Hawkins"],
        "d": 1
    },
    {
        "q": "Which Offspring album sold over six million copies in the US in 1994, peaking at #4 on the Billboard 200 as an independent release?",
        "correct": "Smash",
        "wrong": ["Americana", "Ignition", "Ixnay on the Hombre"],
        "d": 2
    },
    {
        "q": "Which The Offspring comedic novelty track peaked at #5 on the Hot 100 Airplay chart in 1998, mocking wannabe gangstas?",
        "correct": "Pretty Fly (For a White Guy)",
        "wrong": ["The Kids Aren't Alright", "Why Don't You Get a Job?", "Self Esteem"],
        "d": 1
    },
    {
        "q": "Which Nine Inch Nails album debuted at #2 on the Billboard 200 in March 1994, certified 4x Platinum by the RIAA?",
        "correct": "The Downward Spiral",
        "wrong": ["Pretty Hate Machine", "The Fragile", "With Teeth"],
        "d": 2
    },

    # 71-80
    {
        "q": "What Nine Inch Nails single from 'The Downward Spiral' reached #8 on the Modern Rock chart, featuring an infamously graphic chorus?",
        "correct": "Closer",
        "wrong": ["Hurt", "March of the Pigs", "Head Like a Hole"],
        "d": 2
    },
    {
        "q": "Which country music icon covered Nine Inch Nails' 'Hurt' in 2002, earning widespread acclaim and a Grammy Award?",
        "correct": "Johnny Cash",
        "wrong": ["Willie Nelson", "Kris Kristofferson", "Waylon Jennings"],
        "d": 1
    },
    {
        "q": "Which Smashing Pumpkins double album debuted at #1 on the Billboard 200 in 1995 and was certified Diamond?",
        "correct": "Mellon Collie and the Infinite Sadness",
        "wrong": ["Siamese Dream", "Gish", "Adore"],
        "d": 1
    },
    {
        "q": "What was the highest-charting Billboard Hot 100 single from 'Mellon Collie and the Infinite Sadness', peaking at #4?",
        "correct": "1979",
        "wrong": ["Bullet with Butterfly Wings", "Tonight, Tonight", "Zero"],
        "d": 2
    },
    {
        "q": "Which Smashing Pumpkins song opens with the iconic line 'The world is a vampire'?",
        "correct": "Bullet with Butterfly Wings",
        "wrong": ["Zero", "1979", "Tonight, Tonight"],
        "d": 1
    },
    {
        "q": "Which Marilyn Manson album debuted at #1 on the Billboard 200 in September 1998?",
        "correct": "Mechanical Animals",
        "wrong": ["Antichrist Superstar", "Holy Wood", "Portrait of an American Family"],
        "d": 3
    },
    {
        "q": "Which Rage Against the Machine album debuted at #1 on the Billboard 200 in November 1999, featuring 'Guerilla Radio'?",
        "correct": "The Battle of Los Angeles",
        "wrong": ["Rage Against the Machine", "Evil Empire", "Renegades"],
        "d": 2
    },
    {
        "q": "Which Korn album debuted at #1 on the Billboard 200 in 1998, featuring the hit 'Freak on a Leash'?",
        "correct": "Follow the Leader",
        "wrong": ["Issues", "Life Is Peachy", "Korn"],
        "d": 2
    },
    {
        "q": "Which Limp Bizkit album debuted at #1 on the Billboard 200 in 1999, selling over 640,000 copies in its first week?",
        "correct": "Significant Other",
        "wrong": ["Three Dollar Bill, Y'all$", "Chocolate Starfish and the Hot Dog Flavored Water", "Results May Vary"],
        "d": 2
    },
    {
        "q": "What Limp Bizkit cover of a George Michael classic hit #1 on the Modern Rock Tracks chart in 1998?",
        "correct": "Faith",
        "wrong": ["Father Figure", "Careless Whisper", "Freedom! '90"],
        "d": 2
    },

    # 81-90
    {
        "q": "Which Kid Rock album reached #4 on the Billboard 200 in 1999 and was certified Diamond, blending rap and Southern rock?",
        "correct": "Devil Without a Cause",
        "wrong": ["Cocky", "Early Mornin' Stoned Pimp", "Rock n Roll Jesus"],
        "d": 2
    },
    {
        "q": "Which Blink-182 album reached #9 on the Billboard 200 in 1999 and sold over 4 million copies in the US?",
        "correct": "Enema of the State",
        "wrong": ["Dude Ranch", "Take Off Your Pants and Jacket", "Blink-182"],
        "d": 2
    },
    {
        "q": "What Blink-182 single peaked at #2 on the Modern Rock chart in 1999, accompanied by a video of the band running nude through Los Angeles?",
        "correct": "What's My Age Again?",
        "wrong": ["All the Small Things", "Adam's Song", "Dammit"],
        "d": 1
    },
    {
        "q": "What peak position did Blink-182's pop-punk anthem 'All the Small Things' reach on the Billboard Hot 100 in 2000?",
        "correct": "#6",
        "wrong": ["#1", "#3", "#12"],
        "d": 2
    },
    {
        "q": "Which Barenaked Ladies novelty pop-rock track reached #1 on the Billboard Hot 100 for one week in October 1998?",
        "correct": "One Week",
        "wrong": ["If I Had $1000000", "Pinch Me", "The Old Apartment"],
        "d": 1
    },
    {
        "q": "Which Chumbawamba drinking anthem reached #6 on the Billboard Hot 100 in 1997, repeating 'I get knocked down, but I get up again'?",
        "correct": "Tubthumping",
        "wrong": ["Amnesia", "Drip, Drip, Drip", "Enough Is Enough"],
        "d": 1
    },
    {
        "q": "Which Lou Bega mambo-pop hit spent 20 weeks in the Hot 100 top 10 and reached #3 in 1999, listing numerous women's names?",
        "correct": "Mambo No. 5 (A Little Bit Of...)",
        "wrong": ["I Got a Girl", "Tricky, Tricky", "Sweet Like Cola"],
        "d": 1
    },
    {
        "q": "Who originally recorded the instrumental 'Mambo No. 5' in 1949 that Lou Bega sampled and added lyrics to?",
        "correct": "Pérez Prado",
        "wrong": ["Tito Puente", "Xavier Cugat", "Desi Arnaz"],
        "d": 3
    },
    {
        "q": "Which Eagle-Eye Cherry acoustic pop track reached #3 on the Billboard Hot 100 Airplay chart in 1998?",
        "correct": "Save Tonight",
        "wrong": ["Falling in Love Again", "Permanent Tears", "Feels So Right"],
        "d": 2
    },
    {
        "q": "Which New Radicals hit reached #36 on the Hot 100 in 1998 but topped charts worldwide with 'You've got the music in you'?",
        "correct": "You Get What You Give",
        "wrong": ["Someday We'll Know", "Mother We Just Can't Get Enough", "I Hope I Didn't Just Give Away the Ending"],
        "d": 2
    },

    # 91-100
    {
        "q": "Which DMX debut album entered the Billboard 200 at #1 in May 1998, featuring 'Ruff Ryders' Anthem'?",
        "correct": "It's Dark and Hell Is Hot",
        "wrong": ["Flesh of My Flesh, Blood of My Blood", "...And Then There Was X", "The Great Depression"],
        "d": 2
    },
    {
        "q": "DMX achieved which unprecedented Billboard chart feat in the calendar year 1998?",
        "correct": "Two different albums debuted at #1 on the Billboard 200 in the same year",
        "wrong": ["Four #1 Hot 100 singles in six months", "Spent 40 weeks at #1 on the rap chart", "Replaced himself at #1 three times"],
        "d": 2
    },
    {
        "q": "Which DMX album was his second #1 album of 1998, released just seven months after his debut?",
        "correct": "Flesh of My Flesh, Blood of My Blood",
        "wrong": ["...And Then There Was X", "Grand Champ", "Year of the Dog... Again"],
        "d": 2
    },
    {
        "q": "Which Pras Michel single featuring Ol' Dirty Bastard and Mýa peaked at #2 on the Billboard Hot 100 in 1998 from the 'Bulworth' soundtrack?",
        "correct": "Ghetto Supastar (That Is What You Are)",
        "wrong": ["Blue Angels", "Avenues", "Another One Bites the Dust"],
        "d": 2
    },
    {
        "q": "Which Kenny Rogers and Dolly Parton 1983 #1 duet was interpolated in Pras's 'Ghetto Supastar'?",
        "correct": "Islands in the Stream",
        "wrong": ["Real Love", "You Can't Make Old Friends", "Love Is Strange"],
        "d": 2
    },
    {
        "q": "Which Master P album debuted at #1 on the Billboard 200 in 1998, certified 4x Platinum on No Limit Records?",
        "correct": "MP Da Last Don",
        "wrong": ["Ghetto D", "Only God Can Judge Me", "Ghetto Postage"],
        "d": 3
    },
    {
        "q": "Which Juvenile single reached #19 on the Hot 100 in 1999 and popularized the phrase 'Back That Azz Up' nationwide for Cash Money Records?",
        "correct": "Back That Azz Up",
        "wrong": ["Ha", "Slow Motion", "Rodeo"],
        "d": 2
    },
    {
        "q": "Which Cash Money Records in-house producer created the beats for Juvenile's '400 Degreez' and B.G.'s 'Chopper City in the Ghetto'?",
        "correct": "Mannie Fresh",
        "wrong": ["Swizz Beatz", "Timbaland", "Just Blaze"],
        "d": 2
    },
    {
        "q": "Which 1998 album by OutKast reached #2 on the Billboard 200 and featured 'Rosa Parks'?",
        "correct": "Aquemini",
        "wrong": ["ATLiens", "Southernplayalisticadillacmuzik", "Stankonia"],
        "d": 2
    },
    {
        "q": "What was the civil rights pioneer Rosa Parks' reaction to OutKast's 1998 hit song named after her?",
        "correct": "She filed a lawsuit for unauthorized use of her name that settled in 2005",
        "wrong": ["She appeared in the music video", "She performed with them at the Grammys", "She presented them with an NAACP Image Award"],
        "d": 2
    }
]

if __name__ == "__main__":
    formatted = assemble_batch(QUESTIONS, 5)
    save_batch(formatted, 5)
