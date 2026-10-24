#!/usr/bin/env python3
"""
Generate SNL Batch 8: Extratextual 2 - Bans, Controversies, Live Blunders & Production Lore
100 questions: exactly 30 d1, 40 d2, 30 d3.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from builder import build_batch

questions = [
    # 1
    {
        "q": "What object did musical guest Sinéad O'Connor tear up on live television in October 1992 while shouting 'Fight the real enemy!'?",
        "correct": "A photograph of Pope John Paul II",
        "distractors": ["An American flag", "A Bible", "A copy of the United States Constitution"],
        "d": 1
    },
    # 2
    {
        "q": "What a cappella Bob Marley song was Sinéad O'Connor performing when she tore up the Pope's photo in 1992?",
        "correct": "War",
        "distractors": ["Redemption Song", "Get Up, Stand Up", "Exodus"],
        "d": 2
    },
    # 3
    {
        "q": "Which host appeared the week after Sinéad O'Connor's protest and held up the taped-together photo of the Pope, declaring he would have given her 'such a smack'?",
        "correct": "Joe Pesci",
        "distractors": ["Robert De Niro", "Alec Baldwin", "Harvey Keitel"],
        "d": 1
    },
    # 4
    {
        "q": "Why was the rock band Rage Against the Machine banned for life after their April 1996 performance?",
        "correct": "They hung inverted American flags from their amplifiers in protest of host Steve Forbes",
        "distractors": ["They smashed the camera equipment with sledgehammers", "They threw burning flares into the live studio audience", "They refused to play their hit song and stood in silence"],
        "d": 1
    },
    # 5
    {
        "q": "Which billionaire political candidate was hosting SNL on the night Rage Against the Machine staged their flag protest?",
        "correct": "Steve Forbes",
        "distractors": ["Ross Perot", "Donald Trump", "Michael Bloomberg"],
        "d": 2
    },
    # 6
    {
        "q": "What martial arts actor was declared the 'worst host ever' by Lorne Michaels and banned for his arrogance and pitch about a predatory therapist?",
        "correct": "Steven Seagal",
        "distractors": ["Jean-Claude Van Damme", "Chuck Norris", "Jackie Chan"],
        "d": 1
    },
    # 7
    {
        "q": "Why was Martin Lawrence banned from Saturday Night Live following his February 1994 monologue?",
        "correct": "He launched into an unscripted, graphic rant about female feminine hygiene",
        "distractors": ["He walked off stage after thirty seconds", "He physically pushed a camera operator off the riser", "He endorsed a brand that violated NBC commercial agreements"],
        "d": 1
    },
    # 8
    {
        "q": "What appears in syndication and streaming reruns in place of Martin Lawrence's controversial 1994 opening monologue?",
        "correct": "A text title card explaining that NBC censored the monologue to protect broadcast licenses",
        "distractors": ["A prerecorded comedy sketch starring Phil Hartman", "A musical number from the SNL Band", "A commercial parody from Season 12"],
        "d": 2
    },
    # 9
    {
        "q": "Why was Oscar-winning actor Adrien Brody banned from hosting SNL after his May 2003 appearance?",
        "correct": "He wore fake dreadlocks and improvised a faux-Jamaican patois for 45 seconds to introduce Sean Paul",
        "distractors": ["He refused to shake hands with musical guest Sean Paul", "He vandalized his dressing room mirror with red paint", "He cursed repeatedly during the cold open"],
        "d": 1
    },
    # 10
    {
        "q": "Which hip-hop group was banned from SNL after member DJ Muggs lit and smoked a marijuana joint on stage in October 1993?",
        "correct": "Cypress Hill",
        "distractors": ["A Tribe Called Quest", "Beastie Boys", "House of Pain"],
        "d": 1
    },
    # 11
    {
        "q": "What infamous live lip-sync blunder occurred during pop singer Ashlee Simpson's performance on October 23, 2004?",
        "correct": "The backing vocal track for 'Pieces of Me' played while her microphone was at her waist",
        "distractors": ["She tripped over the drum riser and knocked down the backdrop", "Her earpiece exploded with sparks during the chorus", "She started singing the wrong verse of a Christmas carol"],
        "d": 1
    },
    # 12
    {
        "q": "What did Ashlee Simpson do immediately after the wrong vocal track played before she walked off stage in October 2004?",
        "correct": "She performed an awkward, frantic hoedown jig",
        "distractors": ["She collapsed into tears on the floor", "She yelled at the audio engineer over the microphone", "She bowed and pretended the song was finished"],
        "d": 1
    },
    # 13
    {
        "q": "Who was the celebrity host on the night of Ashlee Simpson's lip-sync incident in October 2004?",
        "correct": "Jude Law",
        "distractors": ["Ben Affleck", "Colin Farrell", "Liam Neeson"],
        "d": 2
    },
    # 14
    {
        "q": "What medical excuse did Ashlee Simpson offer during the goodnights for why she had used a backing vocal track?",
        "correct": "Severe acid reflux",
        "distractors": ["A burst eardrum", "Strep throat", "A broken rib"],
        "d": 2
    },
    # 15
    {
        "q": "Which British post-punk musician was banned in 1977 after stopping his band mid-song and launching into the forbidden anti-media anthem 'Radio Radio'?",
        "correct": "Elvis Costello",
        "distractors": ["Joe Strummer", "Paul Weller", "Johnny Rotten"],
        "d": 2
    },
    # 16
    {
        "q": "In 1999, during the 25th Anniversary Special, which rap-rock group was interrupted mid-performance by Elvis Costello reprising his 'Radio Radio' stunt?",
        "correct": "Beastie Boys",
        "distractors": ["Red Hot Chili Peppers", "Rage Against the Machine", "Green Day"],
        "d": 2
    },
    # 17
    {
        "q": "Which punk rock band was booked on Halloween 1981 at John Belushi's insistence, resulting in $20,000 in studio damage and a lifetime ban?",
        "correct": "Fear",
        "distractors": ["Black Flag", "Dead Kennedys", "The Germs"],
        "d": 2
    },
    # 18
    {
        "q": "What famous DC punk singer and future Minor Threat/Fugazi frontman danced in the mosh pit during Fear's riotous 1981 performance?",
        "correct": "Ian MacKaye",
        "distractors": ["Henry Rollins", "Jello Biafra", "Glenn Danzig"],
        "d": 3
    },
    # 19
    {
        "q": "Which Minneapolis alt-rock band was banned from SNL in 1986 after performing drunk, swapping clothes mid-show, and shouting obscenities?",
        "correct": "The Replacements",
        "distractors": ["Hüsker Dü", "Soul Asylum", "R.E.M."],
        "d": 2
    },
    # 20
    {
        "q": "Which Golden Age television icon hosted SNL in April 1979 and was banned for shamelessly mugging, choreographing fake standing ovations, and crying on camera?",
        "correct": "Milton Berle",
        "distractors": ["Bob Hope", "Jackie Gleason", "Sid Caesar"],
        "d": 2
    },
    # 21
    {
        "q": "Which actor from 'Mary Hartman, Mary Hartman' hosted in 1976, broke down crying in her dressing room, and refused to perform in sketches with the cast?",
        "correct": "Louise Lasser",
        "distractors": ["Mary Kay Place", "Shelley Duvall", "Dyan Cannon"],
        "d": 2
    },
    # 22
    {
        "q": "Which experimental rock icon hosted in October 1978 and infuriated the cast by constantly announcing to the audience that he was reading cue cards?",
        "correct": "Frank Zappa",
        "distractors": ["Captain Beefheart", "Lou Reed", "Iggy Pop"],
        "d": 2
    },
    # 23
    {
        "q": "Which television actor and future murder suspect hosted in November 1982 and crumpled up a sketch script to shove it in Gary Kroeger's face?",
        "correct": "Robert Blake",
        "distractors": ["Robert Conrad", "Telly Savalas", "David Soul"],
        "d": 3
    },
    # 24
    {
        "q": "Why was Chevy Chase banned from ever hosting SNL again following his February 1997 hosting gig?",
        "correct": "He slapped Cheri Oteri on the back of the head and insulted cast and writers",
        "distractors": ["He refused to appear on Weekend Update with Norm Macdonald", "He threw a coffee mug through Lorne Michaels' office window", "He leaked the sketch lineup to the New York Post"],
        "d": 2
    },
    # 25
    {
        "q": "Which two cast members engaged in an infamous backstage fistfight minutes before the broadcast on February 18, 1978?",
        "correct": "Bill Murray and Chevy Chase",
        "distractors": ["John Belushi and Chevy Chase", "Dan Aykroyd and Bill Murray", "Chevy Chase and Garrett Morris"],
        "d": 1
    },
    # 26
    {
        "q": "Who physically pulled Bill Murray and Chevy Chase apart in John Belushi's dressing room right before Chevy walked onto the home base stage?",
        "correct": "John Belushi and Dan Aykroyd",
        "distractors": ["Lorne Michaels and Don Pardo", "Jane Curtin and Gilda Radner", "Paul Shaffer and Howard Shore"],
        "d": 2
    },
    # 27
    {
        "q": "What insult did Bill Murray famously scream at Chevy Chase during their 1978 backstage brawl?",
        "correct": "Medium talent!",
        "distractors": ["Pretentious hack!", "Hollywood sellout!", "Plastic phony!"],
        "d": 2
    },
    # 28
    {
        "q": "Which featured player accidentally uttered the F-word on live television in her very first sketch on September 26, 2009?",
        "correct": "Jenny Slate",
        "distractors": ["Nasim Pedrad", "Abby Elliott", "Michaela Watkins"],
        "d": 1
    },
    # 29
    {
        "q": "What word was Jenny Slate supposed to say instead of the F-word in that 2009 'Biker Chick' sketch?",
        "correct": "Freaking",
        "distractors": ["Frigging", "Flippin'", "Fudging"],
        "d": 2
    },
    # 30
    {
        "q": "Which musician and musical director was the first person ever to say the F-word on SNL in a 1980 sketch starring Bob Newhart?",
        "correct": "Paul Shaffer",
        "distractors": ["Howard Shore", "G.E. Smith", "Lenny Pickett"],
        "d": 3
    },
    # 31
    {
        "q": "Which actress slipped up and dropped an accidental F-word during her February 2017 monologue after declaring she was 'so gay'?",
        "correct": "Kristen Stewart",
        "distractors": ["Dakota Johnson", "Anne Hathaway", "Brie Larson"],
        "d": 1
    },
    # 32
    {
        "q": "In a 2012 'What Up with That?' sketch, which guest star appeared to drop two obscenities when Kenan Thompson cut him off, prompting Kenan to say 'That costs money!'?",
        "correct": "Samuel L. Jackson",
        "distractors": ["Tracy Morgan", "Charles Barkley", "Jamie Foxx"],
        "d": 2
    },
    # 33
    {
        "q": "What condition did NBC executives impose on Season 1 host Richard Pryor in 1975 because they feared he would use profanity on live air?",
        "correct": "A mandatory five-second broadcast delay",
        "distractors": ["A security guard stationed next to the stage switch", "A $50,000 cash bond held in escrow", "All his monologues had to be pre-screened by censors"],
        "d": 2
    },
    # 34
    {
        "q": "What famous sketch did Richard Pryor and Chevy Chase perform in that December 1975 episode, written by comedy writer Paul Mooney?",
        "correct": "Word Association (a racially charged job interview)",
        "distractors": ["The Samurai Job", "The Waiting Room", "The Police Lineup"],
        "d": 1
    },
    # 35
    {
        "q": "What was the final word delivered by Richard Pryor in the explosive 1975 'Word Association' sketch?",
        "correct": "Dead!",
        "distractors": ["Fired!", "Out!", "None!"],
        "d": 2
    },
    # 36
    {
        "q": "What controversial sketch written by Bob Odenkirk in 1990 featured Wayne and Garth visiting a high school locker room with Aerosmith?",
        "correct": "Wayne's World: Aerosmith roadies / Tom Hanks as Garth's cousin",
        "distractors": ["Rock 'n' Roll High School", "Backstage with Wayne", "Headbangers Ball"],
        "d": 3
    },
    # 37
    {
        "q": "In March 1995, what major magazine published an exposé branding SNL 'dysfunctional, unfunny, and bloated', triggering Lorne Michaels' Season 21 cast purge?",
        "correct": "New York Magazine",
        "distractors": ["Vanity Fair", "Rolling Stone", "Time Magazine"],
        "d": 2
    },
    # 38
    {
        "q": "What was the cover headline of the infamous March 1995 New York Magazine article attacking SNL?",
        "correct": "Comedy Isn't Funny",
        "distractors": ["Saturday Night Dead", "The Fall of 8H", "Lorne's Empire in Ruins"],
        "d": 3
    },
    # 39
    {
        "q": "How many cast members were replaced between the end of Season 20 and the start of Season 21 in 1995?",
        "correct": "Nearly the entire cast (over 10 cast members)",
        "distractors": ["Only three cast members", "Five cast members", "No cast members were replaced"],
        "d": 2
    },
    # 40
    {
        "q": "Which two cast members survived the 1995 purge to anchor the newly revitalized Season 21 cast?",
        "correct": "Norm Macdonald and Tim Meadows (and Mark McKinney)",
        "distractors": ["Chris Farley and David Spade", "Adam Sandler and Rob Schneider", "Kevin Nealon and Julia Sweeney"],
        "d": 2
    },
    # 41
    {
        "q": "How did Adam Sandler and Chris Farley learn they were being fired from SNL in the spring of 1995?",
        "correct": "Through their agents and managers after network pressure, rather than Lorne telling them directly",
        "distractors": ["During a live meeting in Lorne Michaels' office", "Via a certified letter delivered to 30 Rock", "On the air during the season finale goodnights"],
        "d": 2
    },
    # 42
    {
        "q": "When Adam Sandler returned to host SNL in 2019, what song did he perform in his monologue celebrating his 1995 departure?",
        "correct": "I Was Fired",
        "distractors": ["Goodbye 30 Rock", "NBC Can't Stop Me", "Sandler's Revenge"],
        "d": 1
    },
    # 43
    {
        "q": "Which beloved former cast member did Adam Sandler honor with an emotional tribute song at the piano on that 2019 episode?",
        "correct": "Chris Farley",
        "distractors": ["Phil Hartman", "John Belushi", "Norm Macdonald"],
        "d": 1
    },
    # 44
    {
        "q": "During the 2007-2008 Writers Guild of America strike, where did the SNL cast perform a live, unbroadcast stage show to support crew members?",
        "correct": "The Upright Citizens Brigade (UCB) Theatre in New York",
        "distractors": ["The Beacon Theatre", "Radio City Music Hall", "The Comedy Cellar"],
        "d": 2
    },
    # 45
    {
        "q": "Which host and musical guest were scheduled for the November 10, 2007 episode that was abruptly cancelled by the WGA strike?",
        "correct": "Dwayne 'The Rock' Johnson and Amy Winehouse",
        "distractors": ["Steve Carell and Foo Fighters", "Jonah Hill and Mariah Carey", "Ben Affleck and Jay-Z"],
        "d": 3
    },
    # 46
    {
        "q": "To comply with New York State COVID-19 health regulations in the fall of 2020, how did SNL legally seat a live audience in Studio 8H?",
        "correct": "They paid each audience member $5 in cash, making them legally classified as temporary show employees",
        "distractors": ["They only invited vaccinated doctors and nurses", "They filled the seats with cardboard cutouts equipped with speakers", "They held the show outdoors on the Rockefeller ice rink"],
        "d": 2
    },
    # 47
    {
        "q": "Which musical guest was uninvited from an October 2020 episode after video surfaced of him violating COVID quarantine protocols at a college party?",
        "correct": "Morgan Wallen",
        "distractors": ["Machine Gun Kelly", "Jack Harlow", "Lil Nas X"],
        "d": 1
    },
    # 48
    {
        "q": "Who replaced Morgan Wallen on short notice as musical guest for that October 2020 episode hosted by Bill Burr?",
        "correct": "Jack White",
        "distractors": ["Coldplay", "The Strokes", "Foo Fighters"],
        "d": 2
    },
    # 49
    {
        "q": "In December 2020, what sketch did Morgan Wallen perform in when he was invited back to make amends for his quarantine blunder?",
        "correct": "A time-travel sketch where past versions of Morgan Wallen and Jason Bateman warned him not to party",
        "distractors": ["A church choir sketch with the Church Lady", "A press conference parody apologizing to Dr. Fauci", "A digital short with Pete Davidson"],
        "d": 2
    },
    # 50
    {
        "q": "What color ink markers are used exclusively to write the dialogue on SNL's paper cue cards?",
        "correct": "Dark blue ink (with red ink for stage directions and character names)",
        "distractors": ["Black ink only", "Black ink for dialogue and green ink for cues", "Purple ink for dialogue and black ink for directions"],
        "d": 2
    },
    # 51
    {
        "q": "Why is dark blue ink preferred over black ink for writing SNL cue cards?",
        "correct": "It produces less glare and is sharper to read under harsh studio lights",
        "distractors": ["Blue ink was cheaper in bulk in 1975", "Lorne Michaels' favorite color is navy blue", "NBC technical monitors distort black ink"],
        "d": 3
    },
    # 52
    {
        "q": "What is the name of the Manhattan restaurant where Lorne Michaels has traditionally taken the guest host to dinner on Tuesday nights?",
        "correct": "Elaine's (historically) and various upscale Italian restaurants",
        "distractors": ["The 21 Club", "Kats's Delicatessen", "Peter Luger Steakhouse"],
        "d": 2
    },
    # 53
    {
        "q": "Which host hosted in 1982 while under the influence of drugs, causing Lorne's successor Dick Ebersol to keep him isolated backstage?",
        "correct": "John Belushi (visiting) / Howard Hesseman",
        "distractors": ["Robin Williams", "Chevy Chase", "Peter Cook"],
        "d": 3
    },
    # 54
    {
        "q": "In 1986, which host arrived at Studio 8H in a state of exhaustion and memorably fell asleep on the stage couch during rehearsal?",
        "correct": "Francis Ford Coppola",
        "distractors": ["George Lucas", "Oliver Stone", "Martin Scorsese"],
        "d": 3
    },
    # 55
    {
        "q": "Which acclaimed director hosted an episode in Season 11 (1986) where the running gag of the entire show was that he couldn't direct live TV?",
        "correct": "Francis Ford Coppola",
        "distractors": ["David Lynch", "Woody Allen", "Spike Lee"],
        "d": 2
    },
    # 56
    {
        "q": "Which legendary singer-songwriter hosted in December 1988 and got into a physical confrontation backstage with musical director G.E. Smith?",
        "correct": "Paul Simon / Neil Young",
        "distractors": ["Bob Dylan", "James Taylor", "Billy Joel"],
        "d": 3
    },
    # 57
    {
        "q": "What was the name of the controversial late-1990s animated recurring short that Lorne Michaels pulled from reruns because it mocked NBC corporate owners General Electric?",
        "correct": "'Conspiracy Theory Rock' (by Robert Smigel)",
        "distractors": ["'Corporate Shills'", "'The Peacock Mafia'", "'The GE Machine'"],
        "d": 2
    },
    # 58
    {
        "q": "In 'Conspiracy Theory Rock', what did Robert Smigel's cartoon accuse NBC parent company GE of doing?",
        "correct": "Influencing media news reporting to downplay nuclear plant safety concerns and military contracts",
        "distractors": ["Underpaying television writers", "Using cheap light bulbs in studios", "Rigging the Emmy awards voting"],
        "d": 2
    },
    # 59
    {
        "q": "Which cast member infamously broke character during a 1999 live sketch called 'The Doctor Is In', sending Will Ferrell and Molly Shannon into hysterics?",
        "correct": "Jimmy Fallon",
        "distractors": ["Horatio Sanz", "Chris Kattan", "Cheri Oteri"],
        "d": 2
    },
    # 60
    {
        "q": "What did Lorne Michaels famously say about performers who break character and laugh during sketches?",
        "correct": "He disliked it, believing that maintaining the illusion of the character is essential to true comedy",
        "distractors": ["He encouraged it because it boosts live ratings", "He fined every actor $1,000 per break", "He demanded that the sketch immediately end"],
        "d": 2
    },
    # 61
    {
        "q": "Which cast member was the most notorious character-breaker of the early 2000s, often giggling uncontrollably alongside Jimmy Fallon?",
        "correct": "Horatio Sanz",
        "distractors": ["Chris Parnell", "Darrell Hammond", "Will Forte"],
        "d": 1
    },
    # 62
    {
        "q": "In contrast to Fallon and Sanz, which cast member was renowned for almost never breaking character, famously staying stone-faced through 'More Cowbell'?",
        "correct": "Will Ferrell",
        "distractors": ["Jimmy Fallon", "Horatio Sanz", "Tracy Morgan"],
        "d": 1
    },
    # 63
    {
        "q": "Which cast member was affectionately nicknamed 'The Ice Queen' by writers because she virtually never broke character on air?",
        "correct": "Jane Curtin",
        "distractors": ["Laraine Newman", "Gilda Radner", "Ana Gasteyer"],
        "d": 2
    },
    # 64
    {
        "q": "Which cast member was known for his steel resolve during sketches, playing the straight man opposite Farley's Matt Foley without cracking a smile?",
        "correct": "Phil Hartman",
        "distractors": ["David Spade", "Chris Farley", "Adam Sandler"],
        "d": 1
    },
    # 65
    {
        "q": "What did David Spade do during Chris Farley's 'Matt Foley' debut that showed he was breaking character?",
        "correct": "Covered his mouth with his hand to hide his uncontrollable laughter",
        "distractors": ["Turned his back completely to the audience", "Walked off the set behind the sofa", "Dropped to his knees on the carpet"],
        "d": 1
    },
    # 66
    {
        "q": "Which guest host in Season 43 couldn't stop giggling during an alien abduction sketch with Kate McKinnon, burying his head in a prop bag?",
        "correct": "Ryan Gosling",
        "distractors": ["Chris Hemsworth", "Adam Driver", "Bradley Cooper"],
        "d": 1
    },
    # 67
    {
        "q": "What was the title of the famous 1980 mock commercial featuring Dan Aykroyd and Chevy Chase that mocked toxic chemical waste?",
        "correct": "Super Slugger / Toxic Waste Parodies",
        "distractors": ["Love Canal Water", "Industrial Glow", "Pure Sludge"],
        "d": 3
    },
    # 68
    {
        "q": "In October 1996, which musical guest performed with fake blood streaming down their bodies, causing network standards to scramble?",
        "correct": "Marilyn Manson",
        "distractors": ["Nine Inch Nails", "Alice Cooper", "Rob Zombie"],
        "d": 2
    },
    # 69
    {
        "q": "What happened to cast member Chris Parnell in the spring of 2001, making his subsequent rehiring later that fall unprecedented?",
        "correct": "He was fired due to budget cutbacks and then rehired mid-season when Lorne realized how essential he was",
        "distractors": ["He was traded to MADtv in an entertainment deal", "He quit to pursue Broadway and returned after a month", "He was hospitalized with pneumonia for four months"],
        "d": 2
    },
    # 70
    {
        "q": "Which two cast members lobbied Lorne Michaels aggressively to bring Chris Parnell back to the cast in late 2001?",
        "correct": "Will Ferrell and Colin Quinn",
        "distractors": ["Jimmy Fallon and Tina Fey", "Darrell Hammond and Tracy Morgan", "Molly Shannon and Cheri Oteri"],
        "d": 3
    },
    # 71
    {
        "q": "Which cast member was fired from SNL in 1986 along with most of the Season 11 cast, only to be rehired years later for a movie special?",
        "correct": "Damon Wayans",
        "distractors": ["Terry Sweeney", "Danitra Vance", "Jon Lovitz"],
        "d": 2
    },
    # 72
    {
        "q": "Why was Damon Wayans abruptly fired by Lorne Michaels live on air during the March 15, 1986 broadcast?",
        "correct": "He went completely off-script during a sketch, portraying a straight police officer as flamboyant and gay",
        "distractors": ["He refused to wear his assigned costume", "He walked off stage before his lines were finished", "He threw his badge at host Griffin Dunne"],
        "d": 2
    },
    # 73
    {
        "q": "Which sketch did Damon Wayans sabotage by going off-script as a flamboyant cop, leading to his immediate termination?",
        "correct": "'Mr. Monopoly' / Police interrogation sketch",
        "distractors": ["The Subway Cop", "The Lineup", "Precinct 8H"],
        "d": 3
    },
    # 74
    {
        "q": "What happened when Damon Wayans returned to host SNL in 1995, nine years after being fired?",
        "correct": "He performed his popular characters and received a warm welcome from Lorne",
        "distractors": ["He walked off the stage during the monologue", "He brought the In Living Color cast with him", "He mocked Lorne Michaels in song"],
        "d": 2
    },
    # 75
    {
        "q": "Which host hosted in 1977 and caused chaos when he refused to look at cue cards or rehearse, wandering the studio during sketches?",
        "correct": "Broderick Crawford",
        "distractors": ["Milton Berle", "Peter Finch", "Robert Mitchum"],
        "d": 3
    },
    # 76
    {
        "q": "Which country music legend hosted and performed in 1986 while suffering from such severe stage fright that he couldn't leave his dressing room until minutes before air?",
        "correct": "George Jones / Willie Nelson",
        "distractors": ["Johnny Cash", "Waylon Jennings", "Kris Kristofferson"],
        "d": 3
    },
    # 77
    {
        "q": "In 1982, who hosted the Christmas show via satellite from a prison cell while serving time for tax evasion?",
        "correct": "Don Novello (as Father Guido Sarducci)",
        "distractors": ["Larry Flynt", "Timothy Leary", "Abbie Hoffman"],
        "d": 3
    },
    # 78
    {
        "q": "Which musical guest was banned in 1995 after their drummer played completely nude during rehearsals and the band behaved destructively?",
        "correct": "Green Day (temporary ban) / The Replacements",
        "distractors": ["Blink-182", "The Offspring", "No Doubt"],
        "d": 3
    },
    # 79
    {
        "q": "What was the name of the satirical short film created by Albert Brooks in Season 1 where he offered heart surgery tips to viewers?",
        "correct": "The Operation",
        "distractors": ["Open Heart Live", "Doctor Brooks", "Surgical Precision"],
        "d": 3
    },
    # 80
    {
        "q": "How many short films did filmmaker Albert Brooks supply during the first season of Saturday Night Live in 1975-1976?",
        "correct": "Six short films",
        "distractors": ["Ten short films", "Two short films", "Twelve short films"],
        "d": 3
    },
    # 81
    {
        "q": "Which puppeteer and creator of the Muppets supplied a recurring dark fantasy segment titled 'The Land of Gorch' during Season 1?",
        "correct": "Jim Henson",
        "distractors": ["Frank Oz", "Shari Lewis", "Bil Baird"],
        "d": 2
    },
    # 82
    {
        "q": "Why did the SNL writers famously despise writing for Jim Henson's 'Land of Gorch' Muppet characters in Season 1?",
        "correct": "They felt the puppet segments were childish, alien to the show's hip aesthetic, and imposed by NBC",
        "distractors": ["Henson refused to let anyone touch his puppets", "The puppets caught fire under studio lights", "The puppets required five extra cameras"],
        "d": 2
    },
    # 83
    {
        "q": "What did head writer Michael O'Donoghue notoriously do to a Jim Henson puppet in the SNL writers room?",
        "correct": "Hanged it from the ceiling with a wire noose and a blindfold",
        "distractors": ["Lit it on fire in a trash can", "Threw it out of the 17th-floor window", "Ran it through an office paper shredder"],
        "d": 3
    },
    # 84
    {
        "q": "Which host appeared in Season 50 (2024) and performed a sketch dressed as an oversized hot dog vendor arguing with patrons?",
        "correct": "John Mulaney",
        "distractors": ["Nate Bargatze", "Bill Burr", "Woody Harrelson"],
        "d": 2
    },
    # 85
    {
        "q": "What legendary comedy club in New York City is frequented by SNL cast members and writers on Saturday nights after the afterparty?",
        "correct": "The Comedy Cellar",
        "distractors": ["The Stand", "Carolines on Broadway", "Gotham Comedy Club"],
        "d": 1
    },
    # 86
    {
        "q": "What is the traditional post-show celebration held immediately after every live SNL broadcast called?",
        "correct": "The SNL Afterparty",
        "distractors": ["The 8H Gala", "The Rockefeller Reception", "The Midnight Ball"],
        "d": 1
    },
    # 87
    {
        "q": "What famous photograph hanging outside Lorne Michaels' office commemorates the entire original 1975 cast and crew?",
        "correct": "The Season 1 group portrait in black and white",
        "distractors": ["The Beatles with Lorne", "The first Emmy celebration photo", "The NBC studio blueprint"],
        "d": 2
    },
    # 88
    {
        "q": "Which famous actress hosted in 1985 and was involved in a backstage confrontation when she demanded rewrites thirty minutes before air?",
        "correct": "Rosanna Arquette",
        "distractors": ["Madonna", "Sigourney Weaver", "Anjelica Huston"],
        "d": 3
    },
    # 89
    {
        "q": "In 1990, which controversial stand-up comedian hosted, leading cast member Nora Dunn and musical guest Sinéad O'Connor to boycott the episode in protest?",
        "correct": "Andrew Dice Clay",
        "distractors": ["Sam Kinison", "Eddie Murphy", "Bill Hicks"],
        "d": 1
    },
    # 90
    {
        "q": "Why did Nora Dunn and Sinéad O'Connor boycott Andrew Dice Clay's May 1990 episode?",
        "correct": "They objected to his notoriously misogynistic and vulgar nursery-rhyme stand-up routines",
        "distractors": ["He refused to rehearse sketches with female cast members", "He demanded a higher salary than the rest of the cast", "He brought unapproved live animals into the studio"],
        "d": 1
    },
    # 91
    {
        "q": "Who stepped in as the musical replacement for Sinéad O'Connor on that controversial May 1990 Andrew Dice Clay episode?",
        "correct": "Julee Cruise (and Spanic Boys)",
        "distractors": ["Madonna", "Chaka Khan", "Bonnie Raitt"],
        "d": 3
    },
    # 92
    {
        "q": "What happened to Nora Dunn's contract on SNL following her boycott of Andrew Dice Clay?",
        "correct": "Her contract was not renewed, ending her five-year tenure on the show",
        "distractors": ["She was immediately promoted to head writer", "She was fined by the network but stayed three more seasons", "She won an Emmy the following month"],
        "d": 2
    },
    # 93
    {
        "q": "Which cast member played opposite host Andrew Dice Clay during that 1990 show and defended his appearance?",
        "correct": "Jon Lovitz (and Jan Hooks)",
        "distractors": ["Dana Carvey", "Phil Hartman", "Kevin Nealon"],
        "d": 3
    },
    # 94
    {
        "q": "Which host appeared in October 2000 and accidentally cut his finger on a glass prop on live television, bleeding through the rest of the sketch?",
        "correct": "Val Kilmer",
        "distractors": ["Christian Slater", "Bruce Willis", "Russell Crowe"],
        "d": 3
    },
    # 95
    {
        "q": "In 1989, which musical guest had their performance disrupted when stage invaders ran across the set during their song?",
        "correct": "Fine Young Cannibals / R.E.M.",
        "distractors": ["U2", "The Cure", "Depeche Mode"],
        "d": 3
    },
    # 96
    {
        "q": "What happens in the control room when an unscripted expletive slips through on live television?",
        "correct": "The tape operator marks the timecode so it can be bleeped on West Coast and rerun feeds",
        "distractors": ["The broadcast is automatically shut down for 30 seconds", "A siren sounds across the studio floor", "The director is immediately replaced by an associate"],
        "d": 2
    },
    # 97
    {
        "q": "Which host in 1981 delivered an unscripted political endorsement during his monologue that angered network brass?",
        "correct": "Bill Murray",
        "distractors": ["Elliott Gould", "Buck Henry", "Chevy Chase"],
        "d": 3
    },
    # 98
    {
        "q": "What was the title of the mockumentary short directed by Tom Schiller featuring an elderly John Belushi dancing on his castmates' graves?",
        "correct": "Don't Look Back in Anger",
        "distractors": ["The Last Survivor", "Old Man Belushi", "Dancing with the Ghosts"],
        "d": 2
    },
    # 99
    {
        "q": "In Tom Schiller's eerie 1978 short 'Don't Look Back in Anger', which cast member was portrayed as the sole survivor of the original Not Ready for Prime Time Players?",
        "correct": "John Belushi (who tragically was the first to die in real life)",
        "distractors": ["Dan Aykroyd", "Chevy Chase", "Bill Murray"],
        "d": 2
    },
    # 100
    {
        "q": "What phrase is displayed in lights on the marquee at the entrance of Studio 8H greeting the cast and audience before every live show?",
        "correct": "Saturday Night Live / Studio 8H",
        "distractors": ["Live from New York", "The House That Toscanini Built", "The World's Most Famous Studio"],
        "d": 1
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "staging", "snl_batch8.json")
    build_batch(questions, out, batch_num=8)
