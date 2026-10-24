import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from utils import assemble_batch, save_json

raw_questions = [
    # --- METATEXTUAL: DIRECTORS, WRITERS & SHOWRUNNERS (1-35) ---
    {
        "q": "Out of 275 total episodes of Cheers, approximately how many were directed by James Burrows?",
        "correct": "243 episodes",
        "wrong": ["115 episodes", "175 episodes", "275 episodes"],
        "d": 3
    },
    {
        "q": "Which core cast member directed four episodes of Cheers in later seasons?",
        "correct": "John Ratzenberger (Cliff Clavin)",
        "wrong": ["Ted Danson (Sam Malone)", "George Wendt (Norm Peterson)", "Woody Harrelson (Woody Boyd)"],
        "d": 2
    },
    {
        "q": "Which future director of Seinfeld directed several acclaimed Cheers episodes in Seasons 7 through 10?",
        "correct": "Andy Ackerman",
        "wrong": ["David Steinberg", "Rob Reiner", "Tom Cherones"],
        "d": 2
    },
    {
        "q": "Which prolific writing and producing duo penned classic Cheers episodes like 'Showdown' and 'The Heart Is a Lonely Snipehunter'?",
        "correct": "Ken Levine and David Isaacs",
        "wrong": ["Marta Kauffman and David Crane", "Larry David and Jerry Seinfeld", "Matt Groening and Sam Simon"],
        "d": 2
    },
    {
        "q": "Which trio of Cheers writer-producers went on to co-create the spin-off Frasier?",
        "correct": "Peter Casey, David Lee, and David Angell",
        "wrong": ["Ken Levine, David Isaacs, and Rob Long", "Glen Charles, Les Charles, and James Burrows", "Phoef Sutton, Dan O'Shannon, and Tom Anderson"],
        "d": 1
    },
    {
        "q": "What tragedy struck Cheers and Frasier co-creator David Angell and his wife Lynn in 2001?",
        "correct": "They were passengers aboard American Airlines Flight 11 on September 11",
        "wrong": ["They died in a private plane crash in the Rockies", "They perished in a California wildfire", "They were killed in an automobile accident in London"],
        "d": 3
    },
    {
        "q": "Which writer-producer served as showrunner for Cheers' acclaimed middle seasons and won two Emmys for writing?",
        "correct": "Phoef Sutton",
        "wrong": ["Chuck Lorre", "David E. Kelley", "Steven Bochco"],
        "d": 3
    },
    {
        "q": "Which married writing team wrote iconic Cheers episodes including 'I Do, Adieu' and 'Thanksgiving Orphans'?",
        "correct": "Cheri Eichen and Bill Steinkellner",
        "wrong": ["Richard Levinson and William Link", "Joshua Brand and John Falsey", "Bob Weiskopf and Bob Schiller"],
        "d": 3
    },
    {
        "q": "What notable secondary career did Cheers writer Ken Levine pursue outside of television comedy?",
        "correct": "Major League Baseball play-by-play radio announcer",
        "wrong": ["Professional poker champion", "United States federal judge", "Classical symphony conductor"],
        "d": 3
    },
    {
        "q": "Which baseball teams did Cheers writer Ken Levine broadcast for during and after the show's run?",
        "correct": "Baltimore Orioles, Seattle Mariners, and San Diego Padres",
        "wrong": ["Boston Red Sox and New York Yankees", "Chicago Cubs and White Sox", "Los Angeles Dodgers and Angels"],
        "d": 3
    },
    {
        "q": "What writing technique did the Cheers writers famously utilize during table reads and script rewrites?",
        "correct": "Pitching multiple 'alts' (alternative jokes) written directly in the margins of scripts",
        "wrong": ["Testing jokes on random Paramount studio tour guests", "Using an electronic laugh-meter machine", "Letting the cast ad-lib all punchlines on the rehearsal stage"],
        "d": 2
    },
    {
        "q": "In which season did co-creators Glen and Les Charles step back from day-to-day showrunning to let other writers lead?",
        "correct": "Season 4",
        "wrong": ["Season 2", "Season 7", "Season 10"],
        "d": 3
    },
    {
        "q": "Who took over as primary head writers/showrunners starting in Season 8 through the end of the series?",
        "correct": "Cheri Eichen, Bill Steinkellner, and Phoef Sutton",
        "wrong": ["David Crane and Marta Kauffman", "Garry Marshall and Lowell Ganz", "Ken Levine and David Isaacs"],
        "d": 3
    },
    {
        "q": "What writer, who later wrote 'Conversations with My Agent', started his television career in the Cheers writers' room?",
        "correct": "Rob Long",
        "wrong": ["Dan Fogelman", "David Chase", "Aaron Sorkin"],
        "d": 3
    },
    {
        "q": "What was unique about the pacing of dialogue in Cheers compared to traditional 1970s multi-camera sitcoms?",
        "correct": "Fast-paced, character-driven repartee with overlapping lines and sophisticated wit",
        "wrong": ["Extended slapstick pantomimes without spoken dialogue", "Sing-song rhyming couplets in every scene", "Heavy reliance on catchphrases and canned studio effects"],
        "d": 2
    },

    # --- METATEXTUAL: SPINOFFS, CROSSOVERS & THE CHEERS UNIVERSE (16-45) ---
    {
        "q": "What was the very first spin-off series created from Cheers, debuting in 1987?",
        "correct": "The Tortellis",
        "wrong": ["Frasier", "The Clavins", "Boston Nights"],
        "d": 1
    },
    {
        "q": "Which characters starred in the short-lived 1987 spin-off 'The Tortellis'?",
        "correct": "Nick and Loretta Tortelli",
        "wrong": ["Carla Tortelli and Eddie LeBec", "Anthony and Annie Tortelli", "Norm and Vera Peterson"],
        "d": 1
    },
    {
        "q": "In which city was the spin-off 'The Tortellis' set?",
        "correct": "Las Vegas, Nevada",
        "wrong": ["Atlantic City, New Jersey", "Miami, Florida", "Providence, Rhode Island"],
        "d": 2
    },
    {
        "q": "How many episodes of 'The Tortellis' aired before NBC canceled the series?",
        "correct": "13 episodes",
        "wrong": ["6 episodes", "22 episodes", "30 episodes"],
        "d": 3
    },
    {
        "q": "What legendary spin-off series debuted in autumn 1993, months after Cheers concluded?",
        "correct": "Frasier",
        "wrong": ["Woody's World", "Boston Public", "Becker"],
        "d": 1
    },
    {
        "q": "In which city is the spin-off series Frasier set?",
        "correct": "Seattle, Washington",
        "wrong": ["Chicago, Illinois", "San Francisco, California", "Portland, Oregon"],
        "d": 1
    },
    {
        "q": "How many Primetime Emmy Awards did the spin-off Frasier win during its 11-season run?",
        "correct": "37",
        "wrong": ["28", "45", "52"],
        "d": 1
    },
    {
        "q": "Which Cheers cast member was the first to make a guest appearance on Frasier?",
        "correct": "Ted Danson (Sam Malone)",
        "wrong": ["Shelley Long (Diane Chambers)", "Woody Harrelson (Woody Boyd)", "Rhea Perlman (Carla Tortelli)"],
        "d": 2
    },
    {
        "q": "In which airport sitcom created by Cheers producers did Norm and Cliff make a guest appearance?",
        "correct": "Wings",
        "wrong": ["Night Court", "Coach", "NewsRadio"],
        "d": 1
    },
    {
        "q": "On which fictional island in Massachusetts was the sitcom 'Wings' set?",
        "correct": "Nantucket",
        "wrong": ["Martha's Vineyard", "Cape Cod", "Block Island"],
        "d": 2
    },
    {
        "q": "Which Cheers characters visited Nantucket in the Season 2 Wings episode 'The Storyteller'?",
        "correct": "Cliff Clavin and Norm Peterson",
        "wrong": ["Sam Malone and Carla Tortelli", "Woody Boyd and Kelly Gaines", "Frasier Crane and Lilith Sternin"],
        "d": 2
    },
    {
        "q": "Which critically acclaimed medical drama featured a famous 1985 crossover episode set inside Cheers?",
        "correct": "St. Elsewhere",
        "wrong": ["ER", "Trapper John, M.D.", "Chicago Hope"],
        "d": 1
    },
    {
        "q": "In the St. Elsewhere crossover, which hospital doctors visit Cheers for a drink after work?",
        "correct": "Dr. Donald Westphall, Dr. Mark Craig, and Dr. Victor Auschlander",
        "wrong": ["Dr. Mark Greene and Dr. Doug Ross", "Dr. John Becker and Dr. Leonard McCoy", "Dr. Joe Gannon and Dr. Paul Lochner"],
        "d": 3
    },
    {
        "q": "In St. Elsewhere's crossover, what does Dr. Westphall remark about Cheers' bartender and atmosphere?",
        "correct": "He finds the service rude and the atmosphere thoroughly uninviting",
        "wrong": ["He praises Sam's sobriety program", "He attempts to recruit Diane as a hospital nurse", "He recognizes Coach as his former high school baseball coach"],
        "d": 3
    },
    {
        "q": "In The Simpsons Season 6 episode 'Fear of Flying', what happens when Homer Simpson walks into Cheers?",
        "correct": "The gang acts unwelcoming and Norm flees from Homer",
        "wrong": ["Homer drinks all the draft beer and passes out on Norm's stool", "Sam offers Homer a job as an assistant bartender", "Carla challenges Homer to a doughnut-eating contest"],
        "d": 2
    },
    {
        "q": "Which Cheers cast members lent their voices to the parody scene in The Simpsons 'Fear of Flying'?",
        "correct": "Ted Danson, Woody Harrelson, Rhea Perlman, George Wendt, and John Ratzenberger",
        "wrong": ["Only Ted Danson and George Wendt", "Only Kelsey Grammer and Bebe Neuwirth", "Kirstie Alley, Ted Danson, and Shelley Long"],
        "d": 2
    },
    {
        "q": "Which prominent Cheers cast member did NOT voice their character in The Simpsons parody?",
        "correct": "Kelsey Grammer (who was already voicing Sideshow Bob on the show)",
        "wrong": ["Ted Danson", "George Wendt", "Woody Harrelson"],
        "d": 1
    },
    {
        "q": "Which famous NBC promo featured the cast of Cheers interacting with the cast of other NBC shows?",
        "correct": "\"Let's All Be There\" / \"Come Home to NBC\"",
        "wrong": ["\"Must See Magic\"", "\"NBC All-Stars Live\"", "\"Thursday Night Fever\""],
        "d": 3
    },
    {
        "q": "What British television sitcom remade Cheers for UK television in 2011, which flopped immediately?",
        "correct": "No official UK remake was produced, but a Spanish remake titled 'Cheers' was broadcast in 2011",
        "wrong": ["The Pub", "Down the Local", "Boston Arms"],
        "d": 3
    },
    {
        "q": "In which European country did an official licensed remake of Cheers air in 2011 on Telecinco?",
        "correct": "Spain",
        "wrong": ["Italy", "Germany", "France"],
        "d": 3
    },

    # --- METATEXTUAL: PRODUCTION DESIGN, PROPS & TECHNICAL DETAILS (36-70) ---
    {
        "q": "What was the simulated beer served to the actors on the set of Cheers made of?",
        "correct": "Non-alcoholic near-beer (Moussy/Kaliber) sprinkled with salt to maintain head foam",
        "wrong": ["Carbonated iced tea mixed with club soda", "Apple cider with dish soap foam", "Ginger ale colored with caramel food dye"],
        "d": 2
    },
    {
        "q": "Why was table salt added to the actors' beer steins during filming?",
        "correct": "To release carbonation and keep the foamy beer head alive under hot studio lights",
        "wrong": ["To prevent the beer from fermenting on stage", "To make the actors drink slower during long takes", "To enhance the golden color on 35mm color film"],
        "d": 2
    },
    {
        "q": "What wood was used to construct the iconic Cheers bar counter on Paramount Stage 25?",
        "correct": "Solid mahogany and oak trim",
        "wrong": ["Pine with walnut stain", "Teak and cherry laminate", "Plywood with fiberglass finish"],
        "d": 2
    },
    {
        "q": "What day of the week was Cheers traditionally filmed in front of the live studio audience?",
        "correct": "Friday evenings",
        "wrong": ["Tuesday afternoons", "Wednesday evenings", "Saturday nights"],
        "d": 3
    },
    {
        "q": "How many audience seats were in the bleachers on Paramount Stage 25 for Cheers tapings?",
        "correct": "Approximately 200 to 250 seats",
        "wrong": ["50 seats", "500 seats", "1,000 seats"],
        "d": 3
    },
    {
        "q": "What was located immediately through the swinging doors stage right behind the bar?",
        "correct": "Sam Malone's private back office",
        "wrong": ["The commercial kitchen", "The liquor supply cellar", "The fire escape to the alley"],
        "d": 1
    },
    {
        "q": "What was located stage left of the main bar area?",
        "correct": "The pool table room and secondary seating area",
        "wrong": ["The main street entrance stairs", "Melville's kitchen entrance", "The jukebox and coat check"],
        "d": 1
    },
    {
        "q": "Where were the restrooms located on the Cheers set layout?",
        "correct": "Down a small hallway near the back pool room",
        "wrong": ["Directly behind the bar counter", "At the top of the entrance stairs", "Inside Sam's private office"],
        "d": 2
    },
    {
        "q": "What famous prop hung on the wall of Sam's office throughout the entire run of the series?",
        "correct": "A framed photograph of Apache leader Geronimo",
        "wrong": ["A framed photograph of Ted Williams", "A pair of antique crossed fencing swords", "A nautical ship's steering wheel"],
        "d": 2
    },
    {
        "q": "Whose dressing room originally held the Geronimo photograph before it was moved to the Cheers set?",
        "correct": "Nicholas Colasanto (Coach)",
        "wrong": ["Ted Danson (Sam)", "James Burrows (Director)", "Shelley Long (Diane)"],
        "d": 2
    },
    {
        "q": "What wooden Native American figure stood near the front stairs of Cheers?",
        "correct": "A traditional cigar store wooden Indian statue",
        "wrong": ["A carved totem pole from Alaska", "A wooden carved black bear", "A mahogany ship figurehead"],
        "d": 1
    },
    {
        "q": "What brass instrument behind the bar did bartenders ring to celebrate large tips or special occasions?",
        "correct": "A polished brass ship's bell",
        "wrong": ["A copper dinner gong", "A bicycle horn", "A silver service chime"],
        "d": 1
    },
    {
        "q": "What kind of lighting did director of photography John Finger and James Burrows establish for Cheers?",
        "correct": "Warm, amber, low-key lighting reminiscent of a real cozy neighborhood pub",
        "wrong": ["Bright, high-key fluorescent wash common to 1980s network sitcoms", "Stark, high-contrast black-and-white noir lighting", "Vibrant neon-tinted pastel hues"],
        "d": 2
    },
    {
        "q": "What color was the neon sign in the front window visible from the street entrance?",
        "correct": "Red neon spelling 'Cheers'",
        "wrong": ["Blue neon spelling 'Cold Beer'", "Green neon shamrock sign", "Yellow neon spelling 'Tavern'"],
        "d": 2
    },
    {
        "q": "What brand of draft beer taps were visible on the central counter of Cheers?",
        "correct": "Fictional and generic craft taps along with regional New England labels",
        "wrong": ["Coors Light exclusively", "Guinness Stout exclusively", "Heineken and Corona exclusively"],
        "d": 3
    },
    {
        "q": "What did the studio crew do with the original mahogany bar set after Cheers concluded in 1993?",
        "correct": "Preserved parts for the Smithsonian Institution and museum exhibits",
        "wrong": ["Destroyed it with sledgehammers in a studio wrap party", "Sold it at auction to a private collector in Tokyo", "Installed it permanently in Ted Danson's home"],
        "d": 2
    },
    {
        "q": "Which prestigious national museum acquired pieces of the original Cheers set and costumes?",
        "correct": "The Smithsonian National Museum of American History in Washington, D.C.",
        "wrong": ["The Metropolitan Museum of Art in New York", "The Museum of Fine Arts in Boston", "The Rock and Roll Hall of Fame in Cleveland"],
        "d": 1
    },
    {
        "q": "What specific item from Cheers is permanently displayed at the Smithsonian National Museum of American History?",
        "correct": "A section of the bar, barstools, and Sam Malone's Red Sox baseball jacket",
        "wrong": ["The neon front sign and front door stairs", "Cliff Clavin's postal delivery pouch only", "Carla's serving tray and apron only"],
        "d": 2
    },
    {
        "q": "How long did a typical Friday night filming session of Cheers take in front of the studio audience?",
        "correct": "3 to 4 hours",
        "wrong": ["90 minutes", "7 to 8 hours", "12 hours"],
        "d": 3
    },
    {
        "q": "What did warm-up comedians and the cast do to keep audience energy high during filming delays?",
        "correct": "Performed stand-up comedy, tossed candy, and let the cast chat with the crowd",
        "wrong": ["Screened bloopers from previous seasons on overhead monitors", "Gave away free kegs of beer to bleacher attendees", "Held impromptu karaoke competitions among audience members"],
        "d": 3
    },
    {
        "q": "How many cameras were typically used simultaneously in the Cheers multi-camera setup?",
        "correct": "Four 35mm film cameras",
        "wrong": ["Two videotape cameras", "Three 16mm film cameras", "Six digital high-definition cameras"],
        "d": 3
    },
    {
        "q": "What was the purpose of the fourth camera in the Cheers multi-camera system?",
        "correct": "Capturing close-up reaction shots of barflies like Norm, Cliff, and Carla",
        "wrong": ["Filming wide overhead establishing shots of the audience", "Recording continuous wide masters for foreign dubbing", "Filming behind-the-scenes promotional footage"],
        "d": 3
    },
    {
        "q": "Who was the legendary production designer responsible for creating the look and floor plan of the Cheers set?",
        "correct": "Richard Sylbert",
        "wrong": ["Ken Adam", "Dean Tavoularis", "Dante Ferretti"],
        "d": 3
    },
    {
        "q": "What did the production designer intentionally do with the bar to encourage interaction among actors?",
        "correct": "Built a circular, island-style bar so characters could face one another while talking",
        "wrong": ["Made the bar extraordinarily long to allow walking tracking shots", "Added multiple levels with raised catwalks for servers", "Installed a revolving turntable in the center of the tavern floor"],
        "d": 2
    },
    {
        "q": "What real Boston architectural feature inspired the stairs descending into Cheers?",
        "correct": "Traditional Beacon Hill basement-level brownstone entranceways",
        "wrong": ["Old North Church underground crypts", "Boston Harbor wharf dry-docks", "Back Bay carriage house cellars"],
        "d": 2
    },
    {
        "q": "What was the name of the sound engineer who recorded Cheers' pristine dialogue and live studio laughter?",
        "correct": "Sam Black (and production sound mixers)",
        "wrong": ["Ben Burtt", "Gary Rydstrom", "Walter Murch"],
        "d": 3
    },
    {
        "q": "What was the policy regarding canned laughter / laugh tracks on Cheers?",
        "correct": "The show used authentic live audience reactions, with minimal sweetening only when edits required",
        "wrong": ["100% synthetic canned laughter recorded in the 1950s by Desilu", "No laughter was ever permitted on the audio soundtrack", "Audience laughter was stripped and replaced with European studio laughs"],
        "d": 2
    },
    {
        "q": "What did the studio audience often do spontaneously when Norm Peterson entered the set during tapings?",
        "correct": "Scream \"Norm!\" along with the cast members",
        "wrong": ["Stand up and give a standing ovation", "Applaud politely after his joke was delivered", "Stomp their feet on the bleachers"],
        "d": 1
    },
    {
        "q": "What did the cue cards show when George Wendt walked into the bar on set?",
        "correct": "The scripted entrance joke response for George to deliver after the shout of 'Norm!'",
        "wrong": ["Instructions for the audience to remain silent", "The list of beer brands to recite", "The camera number to look directly into"],
        "d": 2
    },
    {
        "q": "What happened to the physical set of Cheers after the series ended in 1993?",
        "correct": "It was carefully dismantled and placed into Paramount studio storage and museum archives",
        "wrong": ["It was immediately repainted and reused as Central Perk in Friends", "It was shipped to Boston and reassembled as a working pub in Beacon Hill", "It was sold on the Home Shopping Network in pieces"],
        "d": 2
    },
    {
        "q": "What parent corporate logo was shown after Charles-Burrows-Charles Productions at the end of 1980s Cheers episodes?",
        "correct": "Paramount Television / Gulf+Western Company",
        "wrong": ["Columbia Pictures Television", "Universal MCA Television", "20th Century Fox Television"],
        "d": 1
    },
    {
        "q": "In what year did Cheers enter off-network broadcast syndication, airing nightly on local stations?",
        "correct": "1987",
        "wrong": ["1982", "1993", "1998"],
        "d": 1
    },
    {
        "q": "Which co-composer of the Cheers theme song also co-wrote the popular theme song for 'Growing Pains' and 'Mr. Belvedere'?",
        "correct": "Judy Hart Angelo (with Gary Portnoy)",
        "wrong": ["Mike Post", "Charles Fox", "Alan Thicke"],
        "d": 1
    },
    {
        "q": "What was the characteristic casual attire frequently worn by Ted Danson as Sam Malone behind the bar?",
        "correct": "Layered collared shirts, open casual button-downs, and rolled-up sleeves",
        "wrong": ["Formal tuxedo with black bow tie", "All-black turtleneck and leather vest", "Red Boston Red Sox jersey every episode"],
        "d": 1
    },
    {
        "q": "When Cheers entered off-network syndication in 1987, what financial milestone did it achieve?",
        "correct": "It set record-breaking syndication licensing prices of over 1.5 million dollars per episode in major markets",
        "wrong": ["It became the first television show syndicated internationally in live satellite feeds", "It was offered completely free of charge to public television stations", "It sold only to independent cable networks without local affiliate broadcasts"],
        "d": 3
    },

    # --- EXTRA-TEXTUAL: THE REAL BULL & FINCH PUB & BOSTON LANDMARKS (71-100) ---
    {
        "q": "What is the street address of the real Boston pub whose exterior was used for Cheers?",
        "correct": "84 Beacon Street, Boston, Massachusetts",
        "wrong": ["104 Tremont Street, Boston, Massachusetts", "12 Hanover Street, Boston, Massachusetts", "500 Boylston Street, Boston, Massachusetts"],
        "d": 1
    },
    {
        "q": "What was the original real-life name of the Boston pub that served as the exterior of Cheers?",
        "correct": "The Bull & Finch Pub",
        "wrong": ["The Black Rose", "The Red Lion Inn", "The Hampshire Ale House"],
        "d": 1
    },
    {
        "q": "In which historic Boston neighborhood is the real Bull & Finch Pub located?",
        "correct": "Beacon Hill",
        "wrong": ["North End", "Back Bay", "South Boston (Southie)"],
        "d": 1
    },
    {
        "q": "Which famous Boston public park is located directly across Beacon Street from the real pub?",
        "correct": "The Boston Public Garden",
        "wrong": ["Boston Common", "The Esplanade", "Franklin Park"],
        "d": 1
    },
    {
        "q": "Who was the Boston restaurateur and owner of the Bull & Finch Pub when Cheers scouted it in 1981?",
        "correct": "Thomas A. Kershaw",
        "wrong": ["Patrick O'Malley", "Francis Fitzgerald", "Arthur McGinty"],
        "d": 2
    },
    {
        "q": "In what year was the real Bull & Finch Pub originally founded inside the Hampshire House mansion?",
        "correct": "1969",
        "wrong": ["1955", "1975", "1982"],
        "d": 3
    },
    {
        "q": "What Georgian Revival mansion houses the real Bull & Finch Pub in its lower level?",
        "correct": "The Hampshire House",
        "wrong": ["The Gibson House", "The Somerset Club", "The Ames Mansion"],
        "d": 2
    },
    {
        "q": "How much money did the producers of Cheers reportedly pay the Bull & Finch owner in 1981 for rights to photograph the exterior?",
        "correct": "One dollar (nominal fee for location rights)",
        "wrong": ["10,000 dollars", "50,000 dollars", "100,000 dollars plus 1% syndication royalties"],
        "d": 2
    },
    {
        "q": "Why were many tourists visiting the real Bull & Finch Pub in the 1980s and 1990s surprised or disappointed upon entering?",
        "correct": "The real pub was tiny, narrow, and looked completely different from the spacious Hollywood set",
        "wrong": ["The real pub did not sell alcoholic beer", "The pub had been converted into an Italian dry-cleaner", "The pub was closed to anyone who wasn't a Massachusetts resident"],
        "d": 1
    },
    {
        "q": "What was the most common question tourists asked bartenders at the real Bull & Finch Pub?",
        "correct": "\"Where are the stairs leading down to the big bar?\"",
        "wrong": ["\"Is Sam Malone in the back office?\"", "\"Can I pour my own draft beer?\"", "\"Where is the upstairs seafood restaurant?\""],
        "d": 1
    },
    {
        "q": "In what year was the Bull & Finch Pub officially renamed 'Cheers Beacon Hill'?",
        "correct": "2001",
        "wrong": ["1987", "1993", "2010"],
        "d": 2
    },
    {
        "q": "In 2001, where in Boston was a second 'Cheers' location built that featured an exact replica of the Hollywood TV set?",
        "correct": "Faneuil Hall Marketplace",
        "wrong": ["Prudential Center", "Harvard Square", "Boston Seaport"],
        "d": 1
    },
    {
        "q": "What happened to the replica Cheers bar at Faneuil Hall Marketplace in August 2020?",
        "correct": "It closed permanently due to the COVID-19 pandemic and economic lease terms",
        "wrong": ["It was destroyed by an accidental fire", "It was purchased by Ted Danson and moved to Los Angeles", "It was converted into a sports museum"],
        "d": 2
    },
    {
        "q": "What souvenir retail store was opened directly above the real Bull & Finch Pub to accommodate millions of tourists?",
        "correct": "The Cheers Gift Shop / Souvenir Store",
        "wrong": ["The Sam Malone Baseball Pro Shop", "The Norm Peterson Beer Emporium", "The Cliff Clavin Postal Museum"],
        "d": 1
    },
    {
        "q": "Approximately how many tourists visited the real Bull & Finch Pub annually at the height of Cheers' popularity?",
        "correct": "Nearly 1 million visitors per year",
        "wrong": ["50,000 visitors per year", "250,000 visitors per year", "5 million visitors per year"],
        "d": 2
    },
    {
        "q": "Where did the real pub rank among Boston's most visited tourist attractions in the late 1980s?",
        "correct": "Among the top three most-visited tourist sites in Boston, rivaling the Freedom Trail and Faneuil Hall",
        "wrong": ["In 25th place behind modern art galleries", "It was never tracked as an official tourist attraction", "It was ranked below local high school sporting fields"],
        "d": 2
    },
    {
        "q": "What iconic decorative items framed the real entrance at 84 Beacon Street in the series opening credits?",
        "correct": "Black wrought-iron railings, a classic brass lantern, and window flower boxes",
        "wrong": ["Two stone gargoyles and an American flag banner", "A large wooden barrel and neon shamrock", "A granite archway with carved Celtic knots"],
        "d": 2
    },
    {
        "q": "In real life, what restaurant is located on the upper floors of the Hampshire House above the pub (parallel to Melville's)?",
        "correct": "The Hampshire House private dining and banquet facility",
        "wrong": ["A seafood restaurant named Melville's", "A French steakhouse named Bistro du Midi", "A private gentlemen's athletic lounge"],
        "d": 3
    },
    {
        "q": "Did the real Bull & Finch Pub ever employ a bartender named Sam Malone in its history?",
        "correct": "No, Sam Malone was a completely fictional character created by the writers",
        "wrong": ["Yes, the character was based on an Irish bartender who worked there in 1972", "Yes, Tom Kershaw hired a real former Red Sox pitcher named Sam", "Yes, but he was a dishwasher rather than a bartender"],
        "d": 1
    },
    {
        "q": "Which Cheers cast members traveled to Boston in 1993 to attend the series finale celebration at the Bull & Finch Pub?",
        "correct": "Virtually the entire main cast including Ted Danson, Kelsey Grammer, Woody Harrelson, and George Wendt",
        "wrong": ["Only John Ratzenberger and George Wendt", "Only Shelley Long and Ted Danson", "None of the actors attended due to filming commitments in Los Angeles"],
        "d": 2
    },
    {
        "q": "What happened to traffic in Boston's Beacon Hill during the live finale broadcast outside the Bull & Finch Pub?",
        "correct": "Tens of thousands of fans flooded Beacon Street, gridlocking the entire neighborhood",
        "wrong": ["Police banned all pedestrians and kept the street completely deserted", "A blizzard shut down the city and cancelled the street gathering", "Fans staged a peaceful candlelit vigil across the Public Garden"],
        "d": 2
    },
    {
        "q": "What cocktail on the real Bull & Finch menu was named after Carla Tortelli?",
        "correct": "Carla's Revenge / Spiked Hurricane concoction",
        "wrong": ["Carla's Espresso Martini", "Tortelli Chianti Spritzer", "Carla's Lemon Drop"],
        "d": 3
    },
    {
        "q": "What food item on the real Cheers Beacon Hill menu is named in honor of Norm Peterson?",
        "correct": "The 'Norm Burger' / Peterson Giant Bacon Cheeseburger",
        "wrong": ["\"Norm's Barbecue Rib Platter\"", "\"Norm's Deep-Fried Clam Basket\"", "\"Norm's Loaded Buffalo Wings\""],
        "d": 2
    },
    {
        "q": "What real Boston landmark can be seen in exterior transition shots when establishing Boston's skyline?",
        "correct": "The John Hancock Tower and the Custom House Tower",
        "wrong": ["The Empire State Building", "The Gateway Arch", "The Willis Tower"],
        "d": 2
    },
    {
        "q": "In the exterior establishing shots, which famous body of water is occasionally shown with rowers or sailboats?",
        "correct": "The Charles River",
        "wrong": ["Boston Harbor", "Mystic River", "Walden Pond"],
        "d": 1
    },
    {
        "q": "What historic Boston athletic venue is frequently shown in background establishing clips before sports discussions?",
        "correct": "Fenway Park",
        "wrong": ["Boston Garden", "Foxboro Stadium", "Harvard Stadium"],
        "d": 1
    },
    {
        "q": "What statue inside the Boston Public Garden across from the real pub became a favorite photo stop for Cheers fans?",
        "correct": "The 'Make Way for Ducklings' bronze statue and the George Washington equestrian monument",
        "wrong": ["The Benjamin Franklin bronze statue", "The Paul Revere equestrian statue", "The Samuel Adams granite memorial"],
        "d": 3
    },
    {
        "q": "In 1983, what did the real Bull & Finch Pub do when customers began swarming the pub after Cheers won its first Emmys?",
        "correct": "Quickly added Cheers merchandise, T-shirts, and glassware for purchase behind the bar",
        "wrong": ["Sued Paramount for trademark infringement", "Banned tourists from photographing the entrance", "Painted over the brick facade with white paint"],
        "d": 2
    },
    {
        "q": "What real Boston street leads directly to the Cheers Beacon Hill front entrance?",
        "correct": "Beacon Street (between Arlington and Charles Streets)",
        "wrong": ["Newbury Street", "Boylston Street", "Commonwealth Avenue"],
        "d": 2
    },
    {
        "q": "Why did the city of Boston grant special commemorative status to the Bull & Finch Pub building in 2000?",
        "correct": "For its cultural contribution to Boston tourism and global recognition as an American television icon",
        "wrong": ["Because George Washington held military meetings in the tavern basement", "Because the Boston Tea Party was planned on the second floor", "Because it was the oldest continuously operated pub in the United States"],
        "d": 3
    }
]

assert len(raw_questions) == 100, f"Expected 100, got {len(raw_questions)}"

d_counts = {1: 0, 2: 0, 3: 0}
for q in raw_questions:
    d_counts[q["d"]] += 1

print(f"DEBUG Batch 4 d_counts: {d_counts}")
assert d_counts[1] == 30, f"Expected 30 d1, got {d_counts[1]}"
assert d_counts[2] == 40, f"Expected 40 d2, got {d_counts[2]}"
assert d_counts[3] == 30, f"Expected 30 d3, got {d_counts[3]}"

formatted = assemble_batch(raw_questions, 4)
save_json(formatted, "tools/staging/cheers_batch4.json")
print("Saved tools/staging/cheers_batch4.json successfully!")
