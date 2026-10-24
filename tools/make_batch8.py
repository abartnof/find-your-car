#!/usr/bin/env python3
"""
Generate Batch 8: Extratextual: Behind-the-Scenes Dramas, Feuds, Firings & Writers' Rooms (100 questions)
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from sitcom_builder import make_batch

q_batch8 = [
    # Roseanne Writers Room & Backstage Drama (20 questions)
    {
        "q": "What humiliating system did Roseanne Barr reportedly introduce to the writers' room to humiliate staff and assert her authority?",
        "correct": "Assigning writers numbers instead of names on their staff T-shirts and scripts",
        "distractors": ["Forcing writers to sit on the floor during table reads", "Making fired writers surrender their shoes before leaving the studio", "Requiring writers to wear dunce caps if jokes bombed at run-throughs"],
        "d": 2
    },
    {
        "q": "Which future mega-producer behind Two and a Half Men and The Big Bang Theory was notoriously fired from Roseanne after clashing with the star?",
        "correct": "Chuck Lorre",
        "distractors": ["Greg Daniels", "Bill Lawrence", "Steven Levitan"],
        "d": 2
    },
    {
        "q": "Which future creator of Buffy the Vampire Slayer got his professional television writing start in the turbulent Roseanne writers' room?",
        "correct": "Joss Whedon",
        "distractors": ["J.J. Abrams", "Damon Lindelof", "Ryan Murphy"],
        "d": 2
    },
    {
        "q": "Why did creator and original showrunner Matt Williams walk off the set and demand that ABC choose between him and Roseanne during Season 1?",
        "correct": "Roseanne refused to say a line of dialogue in an episode ('Well, it's about time') to prove she had veto power over the script",
        "distractors": ["Williams refused to cast John Goodman as Dan Conner", "Roseanne demanded that her then-husband Tom Arnold be named co-showrunner immediately", "Williams secretly tried to rewrite the pilot into a vehicle for Laurie Metcalf"],
        "d": 3
    },
    {
        "q": "How did ABC executives resolve the explosive Season 1 standoff between star Roseanne Barr and creator Matt Williams?",
        "correct": "ABC backed Roseanne and forced Matt Williams out of his own creation, paying him millions in executive producer royalties",
        "distractors": ["ABC suspended Roseanne for six episodes and hired a substitute actress", "ABC cancelled the series for two weeks until both signed a mediation contract", "Matt Williams won the battle and had Roseanne's character written into a coma"],
        "d": 2
    },
    {
        "q": "Which controversial comic married Roseanne in 1990, became an executive producer on the show, and frequently clashed with ABC executives?",
        "correct": "Tom Arnold",
        "distractors": ["Bobcat Goldthwait", "Sam Kinison", "Andrew Dice Clay"],
        "d": 1
    },
    {
        "q": "What did Roseanne famously do to the production company name 'Carsey-Werner' on her parking space during a dispute?",
        "correct": "She defaced and spray-painted over the executives' names on the studio lot",
        "distractors": ["She had their luxury cars towed to a municipal impound lot in Compton", "She cemented a bronze pig onto the asphalt of Marcy Carsey's space", "She hired a marching band to block Tom Werner from parking every morning"],
        "d": 3
    },
    {
        "q": "Which prolific female writer-producer on Roseanne later created Gilmore Girls and The Marvelous Mrs. Maisel?",
        "correct": "Amy Sherman-Palladino",
        "distractors": ["Mindy Kaling", "Jenji Kohan", "Liz Meriwether"],
        "d": 2
    },
    {
        "q": "Why was actress Lecy Goranson (Becky Conner) written off the show in Season 5, leading to her replacement by Sarah Chalke?",
        "correct": "She chose to leave Hollywood to attend Vassar College full-time",
        "distractors": ["She was fired after a bitter salary dispute with Tom Arnold", "She suffered a severe equestrian injury requiring spinal surgery", "She was cast as the lead in a major motion picture trilogy"],
        "d": 1
    },
    {
        "q": "How did the writers of Roseanne acknowledge the bizarre back-and-forth swapping of actresses Lecy Goranson and Sarah Chalke as Becky?",
        "correct": "With running meta-jokes, such as characters looking at Becky and asking 'Where the hell have you been?'",
        "distractors": ["By giving Becky an identical twin sister who moved in from Florida", "By having Dan Conner remark that Becky's plastic surgery had failed", "By pretending nothing had changed and never mentioning it"],
        "d": 2
    },
    {
        "q": "In 1994, which groundbreaking Roseanne episode ('Don't Ask, Don't Tell') sparked massive network anxiety and sponsor pushback?",
        "correct": "An episode in which Mariel Hemingway's character kisses Roseanne in a gay bar",
        "distractors": ["An episode where Dan Conner admits he evaded the Vietnam draft", "An episode where Darlene gets a tattoo of an anarchist symbol", "An episode where Jackie attends a socialist political rally"],
        "d": 2
    },
    {
        "q": "What threat did ABC make regarding the 1994 'gay kiss' episode before Roseanne threatened to take the show to another network?",
        "correct": "ABC executives initially threatened to pull the episode and slap an unprecedented parental warning advisory on it",
        "distractors": ["ABC refused to pay the cast salaries for the broadcast week", "ABC mandated that the kiss be edited out and replaced with a hug", "ABC offered sponsors free ad slots on Monday Night Football to compensate"],
        "d": 2
    },
    {
        "q": "How many different showrunners did Roseanne burn through during its tumultuous nine-season original run?",
        "correct": "Eight different showrunners",
        "distractors": ["Only two showrunners", "Four showrunners", "Twelve showrunners"],
        "d": 3
    },
    {
        "q": "What famous insult did Roseanne allegedly write on the script notes of writers whose jokes she disliked?",
        "correct": "She would write 'Not funny' or physically rip out pages during table reads in front of the entire cast",
        "distractors": ["She stamped red skulls on the title page", "She mailed their drafts back to their agents with pennies taped to the envelopes", "She threw coffee at their keyboards during late-night rewrites"],
        "d": 2
    },
    {
        "q": "What bizarre Season 9 creative direction alienated millions of fans and earned near-universal critical derision?",
        "correct": "The working-class Conners winning a $108 million state lottery jackpot and socializing with royalty and terrorists",
        "distractors": ["The Conners moving to Manhattan and buying a penthouse on Park Avenue", "Dan running for the United States Senate as an independent candidate", "Roseanne opening a luxury fashion boutique in Paris"],
        "d": 1
    },
    {
        "q": "Which veteran actor almost quit Roseanne multiple times due to the exhausting chaos and screaming matches between Barr and Arnold?",
        "correct": "John Goodman",
        "distractors": ["Laurie Metcalf", "Michael Fishman", "Tom Arnold"],
        "d": 2
    },
    {
        "q": "What did Roseanne famously demand in her contract before agreeing to return for the show's ninth and final season?",
        "correct": "Total, absolute creative control and final cut over every single script and casting decision",
        "distractors": ["$3 million per episode and ownership of the studio soundstage", "The firing of John Goodman and Laurie Metcalf", "A guarantee that the series would be converted into an animated cartoon"],
        "d": 2
    },
    {
        "q": "Which acclaimed playwright and future Desperate Housewives writer served as a head writer on Roseanne during its middle seasons?",
        "correct": "Marc Cherry (and also Bob Myer)",
        "distractors": ["David E. Kelley", "Aaron Sorkin", "Alan Ball"],
        "d": 3
    },
    {
        "q": "What did Roseanne do during her 1992 Peabody Award acceptance speech that shocked attendees?",
        "correct": "She delivered a deeply emotional, passionate defense of working-class women and lashed out at sexist TV critics",
        "distractors": ["She walked onto the podium in pajamas and refused to speak", "She announced her candidacy for President of the United States", "She smashed the crystal award on the podium to protest low wages"],
        "d": 3
    },
    {
        "q": "Which actor, who played Roseanne's son D.J. Conner, stayed with the series from age 6 through age 15 across the entire original run?",
        "correct": "Michael Fishman",
        "distractors": ["Sal Barone", "Danny Pintauro", "Jeremy Miller"],
        "d": 2
    },

    # Family Matters & The Urkel Phenomenon (15 questions)
    {
        "q": "How did veteran actor Reginald VelJohnson (Carl Winslow) and the original cast initially react to Steve Urkel's sudden explosion in popularity?",
        "correct": "With intense frustration and resentment, as a show about a warm multi-generational Black family became 'The Steve Urkel Show'",
        "distractors": ["With celebratory relief, as Jaleel White negotiated massive pay increases for all cast members", "They were completely oblivious, as they avoided reading newspapers and ratings reports", "They immediately demanded that their own characters be given comedic catchphrases"],
        "d": 2
    },
    {
        "q": "Why did Jo Marie Payton (Harriette Winslow) famously walk off Family Matters in the middle of Season 9?",
        "correct": "She was deeply dissatisfied with the absurd sci-fi storylines and Urkel-centric scripts, leaving before the finale",
        "distractors": ["She was offered a starring role on Broadway in The Lion King", "She suffered a broken hip during a stunt rehearsal", "A salary dispute with CBS led to her immediate firing"],
        "d": 2
    },
    {
        "q": "Which actress replaced Jo Marie Payton as Harriette Winslow for the second half of Season 9?",
        "correct": "Judyann Elder",
        "distractors": ["Jackée Harry", "Telma Hopkins", "Phylicia Rashad"],
        "d": 3
    },
    {
        "q": "What real-life object did 12-year-old Jaleel White borrow from his dentist father for his first Steve Urkel audition?",
        "correct": "A pair of thick, oversized eyeglasses with a black strap",
        "distractors": ["A set of crooked prosthetic teeth", "A clinical white lab coat with pocket protectors", "An orthopedic back brace"],
        "d": 2
    },
    {
        "q": "What physical ailment did Jaleel White develop in real life from spending nine years playing Steve Urkel?",
        "correct": "Severe vocal cord strain from speaking in an unnatural, high-pitched falsetto for hours each day",
        "distractors": ["Chronic knee damage from performing the awkward Urkel dance hop", "Permanent vision impairment from wearing non-prescription glasses", "Spinal scoliosis from walking with a hunched posture"],
        "d": 2
    },
    {
        "q": "Why did producers invent the suave alter-ego Stefan Urquelle in Season 5 of Family Matters?",
        "correct": "To give Jaleel White an opportunity to act in his natural voice and attractive demeanor, satisfying the actor's desire for range",
        "distractors": ["To fulfill a contractual mandate from network sponsors who wanted a male model character", "Because test audiences expressed disgust at Steve Urkel's nerdy appearance", "To allow another actor to step into the role when White was filming a movie"],
        "d": 2
    },
    {
        "q": "What famous breakfast food product was released nationally by Ralston in 1991 bearing Jaleel White's face?",
        "correct": "Urkel-Os cereal (strawberry and banana flavored)",
        "distractors": ["Steve's Crunchy Suspenders", "Urkel Puffs with Marshmallow Glasses", "Did I Toast That? Waffles"],
        "d": 1
    },
    {
        "q": "What terrifying real-life fan encounter happened to Jaleel White at the height of 'Urkelmania'?",
        "correct": "He had to be escorted by armed security out of shopping malls as thousands of screaming fans mobbed him",
        "distractors": ["A deranged fan broke into his high school classroom and handcuffed herself to his desk", "A man attempted to kidnap him from the Warner Bros. lot disguised as a delivery driver", "He received over 50,000 marriage proposals delivered to his private residence"],
        "d": 2
    },
    {
        "q": "Why did Darius McCrary (Eddie Winslow) reportedly get into heated verbal arguments on set with producers?",
        "correct": "He felt his character's storylines were being systematically reduced to prop feed for Urkel's inventions",
        "distractors": ["He refused to film episodes that aired during Friday evening sporting events", "He demanded that his real-life band perform in every episode", "He wanted to direct half the episodes in Season 6"],
        "d": 2
    },
    {
        "q": "What bizarre sci-fi transformation machines were introduced into the Winslow basement in later seasons as the show jumped the shark?",
        "correct": "A transformation chamber, a teleporter, a shrinking ray, and a time machine",
        "distractors": ["A cybernetic brain scanner, an anti-gravity suit, and a cyborg duplicate", "A weather-controlling machine, an invisibility cloak, and a jetpack", "A mind-reading helmet and a robotic maid"],
        "d": 1
    },
    {
        "q": "What happened to the real-life actor Michelle Thomas (Myra Monkhouse) shortly after Family Matters ended in 1998?",
        "correct": "She tragically passed away from stomach cancer at age 30 in December 1998",
        "distractors": ["She retired from acting to practice veterinary medicine", "She moved to Europe to star in international opera productions", "She became a successful television producer for Nickelodeon"],
        "d": 2
    },
    {
        "q": "Which member of the Winslow family was cast out of the show after Season 4 without any explanation, inspiring a famous TV trope?",
        "correct": "Judy Winslow (Jaimee Foxworth)",
        "distractors": ["Rachel Crawford (Telma Hopkins)", "Richie Crawford (Bryton McClure)", "Mother Winslow (Rosetta LeNoire)"],
        "d": 1
    },
    {
        "q": "What adult career path did Jaimee Foxworth (Judy Winslow) tragically follow years after being unceremoniously erased from the show?",
        "correct": "She entered the adult film industry under the pseudonym Crave before appearing on Celebrity Rehab with Dr. Drew",
        "distractors": ["She became a professional poker player in Las Vegas", "She founded a real estate empire in Dallas", "She joined an ashram in northern India"],
        "d": 3
    },
    {
        "q": "What was the original premise of Family Matters before Steve Urkel was introduced in the twelfth episode of Season 1?",
        "correct": "A grounded blue-collar comedy about an African American police officer raising his family and taking in his widowed sister-in-law",
        "distractors": ["A high-concept sitcom about a family inheriting a million-dollar Chicago jazz club", "A political satire about an urban community board in Cook County", "A teen coming-of-age comedy centered on Eddie's basketball ambitions"],
        "d": 1
    },
    {
        "q": "What did Jaleel White do to keep his growth spurts hidden as he aged from 12 to 21 while playing a nerdy kid?",
        "correct": "He wore tighter, shorter pants and slumped his posture to avoid looking taller than adult co-stars",
        "distractors": ["Producers dug a trench in the soundstage floor for him to walk in", "He wore special weighted flat shoes with no soles", "The adult cast members wore platform shoes to appear taller"],
        "d": 2
    },

    # The Fresh Prince: IRS, Quincy Jones & The Aunt Viv Feud (15 questions)
    {
        "q": "Where did Will Smith's spontaneous audition for NBC executives and Quincy Jones take place in December 1989?",
        "correct": "At Quincy Jones' 56th birthday party in his Bel-Air living room, with Brandon Tartikoff present",
        "distractors": ["In the green room of The Tonight Show Starring Johnny Carson", "At an NBC upfront showcase dinner at the Waldorf Astoria in New York", "In an executive conference room at 30 Rockefeller Plaza"],
        "d": 2
    },
    {
        "q": "Why was Will Smith hesitant to audition for Brandon Tartikoff in Quincy Jones' living room?",
        "correct": "He had zero professional acting experience and asked for three weeks to prepare with an acting coach",
        "distractors": ["He had lost his voice after a concert at the Hollywood Bowl", "He had already signed a development deal with Columbia Pictures", "He didn't want to leave Philadelphia and relocate to California"],
        "d": 2
    },
    {
        "q": "What memorable advice did Quincy Jones give Will Smith when Will asked to delay the audition?",
        "correct": "'Everyone who needs to say yes to make your life change forever is sitting in this room right now. Do it now.'",
        "distractors": [
            "'You can either be a broke rapper in Philly or a rich movie star in Hollywood.'",
            "'If you don't do it today, Tartikoff is flying back to New York and giving it to Kid and Play.'",
            "'Fear is not an option when the IRS is waiting outside with handcuffs.'"
        ],
        "d": 2
    },
    {
        "q": "How much of Will Smith's salary from the first three seasons of The Fresh Prince was garnished directly by the IRS?",
        "correct": "70% of his paycheck",
        "distractors": ["30% of his paycheck", "50% of his paycheck", "90% of his paycheck"],
        "d": 2
    },
    {
        "q": "What was the central cause of the bitter real-life feud between Will Smith and original Aunt Vivian actress Janet Hubert?",
        "correct": "Creative disagreements, Hubert's feeling that Smith received preferential treatment, and a lowball Season 4 contract offer",
        "distractors": ["Hubert demanded that her real-life husband be hired as director", "Smith allegedly demanded that Hubert be replaced by Queen Latifah", "Hubert refused to rehearse with Alfonso Ribeiro"],
        "d": 2
    },
    {
        "q": "What restrictive terms were reportedly offered to Janet Hubert for Season 4 that led to her departure from the series?",
        "correct": "A 10-episode guarantee with a salary cut and a non-compete clause barring her from taking other acting jobs",
        "distractors": ["A requirement that she move into a recurring guest star status with no speaking lines", "A pay cut of 80% to fund Will Smith's music video production", "A clause requiring her to do all her own physical stunts"],
        "d": 3
    },
    {
        "q": "What did Janet Hubert famously say in public interviews for nearly three decades regarding a possible Fresh Prince reunion?",
        "correct": "\"There will never be a reunion... I will never do anything with an asshole like Will Smith.\"",
        "distractors": [
            "\"They couldn't pay me enough money to stand on that stage again.\"",
            "\"Will Smith owes me an apology, but he is too arrogant to ever admit he ruined my career.\"",
            "\"I have erased that show from my memory and moved on with my life.\""
        ],
        "d": 2
    },
    {
        "q": "In what year and setting did Will Smith and Janet Hubert finally sit down, reconcile, and resolve their 27-year feud?",
        "correct": "In 2020 during HBO Max's The Fresh Prince of Bel-Air 30th Anniversary Reunion special",
        "distractors": ["At the 2016 Academy Awards ceremony", "During a live radio interview on The Breakfast Club in 2018", "At James Avery's memorial service in 2014"],
        "d": 1
    },
    {
        "q": "What unusual acting habit did Will Smith display during the first season of Fresh Prince that is visibly noticeable on screen?",
        "correct": "Mouth-syncing his co-stars' dialogue under his breath while waiting for his cue",
        "distractors": ["Looking directly into the camera lens whenever someone delivered a punchline", "Tapping his foot rhythmically to the cadence of the laugh track", "Constantly adjusting his oversized basketball shoes between lines"],
        "d": 1
    },
    {
        "q": "Which actor, who portrayed Uncle Phil, served as a stern yet deeply loving mentor to young Will Smith on set?",
        "correct": "James Avery",
        "distractors": ["Ron Glass", "Bill Cobbs", "John Amos"],
        "d": 1
    },
    {
        "q": "What did James Avery whisper into Will Smith's ear immediately after shooting the emotional 'Papa's Got a Brand New Excuse' scene?",
        "correct": "\"That's acting right there.\"",
        "distractors": [
            "\"You made me proud, son.\"",
            "\"Now you are ready for Hollywood.\"",
            "\"That was the truth, Will.\""
        ],
        "d": 2
    },
    {
        "q": "Why was Season 4 originally planned to be the final season of The Fresh Prince of Bel-Air?",
        "correct": "Will Smith wanted to transition to feature films following the success of Bad Boys",
        "distractors": ["NBC cancelled the series due to declining ratings against Home Improvement", "Quincy Jones shut down production to launch a new record label", "James Avery announced he was leaving the show to teach Shakespeare"],
        "d": 2
    },
    {
        "q": "What brought The Fresh Prince back for Seasons 5 and 6 after NBC initially cancelled it at the end of Season 4?",
        "correct": "Massive fan letter-writing campaigns and impassioned pleas from NBC affiliate station managers",
        "distractors": ["A personal phone call from President Bill Clinton to Warren Littlefield", "A $20 million investment by Sony Pictures to keep the syndication package growing", "Will Smith's contract required two additional seasons"],
        "d": 2
    },
    {
        "q": "Which famous supermodel made her television acting debut on The Fresh Prince in Season 4?",
        "correct": "Tyra Banks",
        "distractors": ["Naomi Campbell", "Iman", "Veronica Webb"],
        "d": 1
    },
    {
        "q": "What was the name of the executive producer who originally conceived the idea of a street-smart kid in Bel-Air based on his own manager Benny Medina?",
        "correct": "Benny Medina (with Jeff Pollack)",
        "distractors": ["Russell Simmons", "Clarence Avant", "Andre Harrell"],
        "d": 2
    },

    # Seinfeld: Larry David, Michael Richards & NBC Battles (15 questions)
    {
        "q": "What was Larry David's famous four-word cardinal rule for writing Seinfeld scripts?",
        "correct": "No hugging, no learning",
        "distractors": ["Keep it completely real", "Never solve the problem", "Always double the misery"],
        "d": 1
    },
    {
        "q": "What did Larry David famously do at the end of almost every single season of Seinfeld?",
        "correct": "Threaten to quit the show, claiming he was completely out of ideas and exhausted",
        "distractors": ["Demand that George Costanza be recast with a younger actor", "Refuse to speak to Jerry Seinfeld for two months", "Burn his contract in front of Warren Littlefield's office"],
        "d": 2
    },
    {
        "q": "When Larry David actually departed Seinfeld as showrunner after Season 7, who took over as sole showrunner for Seasons 8 and 9?",
        "correct": "Jerry Seinfeld",
        "distractors": ["Peter Mehlman", "Spike Feresten", "David Mandel"],
        "d": 2
    },
    {
        "q": "What real-life incident in Larry David's early career as a Saturday Night Live writer inspired George Costanza's Season 2 storyline in 'The Revenge'?",
        "correct": "David quit SNL in a rage on Friday, realized he made a horrible mistake, and showed up to work Monday morning pretending it never happened",
        "distractors": ["David tried to slip a mickey into Dick Ebersol's drink at a holiday party", "David stole an executive's cashmere sweater to pay his rent", "David pretended to be an architect to impress Lorne Michaels' assistant"],
        "d": 1
    },
    {
        "q": "How did Michael Richards prepare for Kramer's famous physical comedy pratfalls, such as sliding through Jerry's apartment door?",
        "correct": "With intense, obsessive rehearsals alone on soundstages, timing every slide with millimeter precision and refusing to socialize between takes",
        "distractors": ["By improvising entirely on the spot without ever rehearsing beforehand", "By drinking five cups of espresso right before the director called action", "By studying vintage Buster Keaton reels on a projector in his dressing room"],
        "d": 2
    },
    {
        "q": "How did Michael Richards famously react whenever fellow cast members broke character and laughed during his physical comedy bits?",
        "correct": "He would become visibly angry, scolding them for ruining the flow and wasting the crew's time",
        "distractors": ["He would laugh hysterically along with them and buy the crew pizza", "He would storm off the stage and refuse to return for the rest of the day", "He would demand that the scene be cut from the final broadcast"],
        "d": 2
    },
    {
        "q": "Why was the landmark Season 2 episode 'The Chinese Restaurant' nearly cancelled by NBC network executives?",
        "correct": "Executives felt an episode where characters just wait in a restaurant lobby with no plot or set change was unbroadcastable",
        "distractors": ["Sponsors objected to the portrayal of restaurant maître d' Mr. Cohen", "The live studio audience didn't laugh during the initial table read", "Jason Alexander refused to film without Julia Louis-Dreyfus being present"],
        "d": 2
    },
    {
        "q": "How did Larry David force NBC to air 'The Chinese Restaurant' despite their deep skepticism?",
        "correct": "He threatened to quit the series immediately if NBC refused to produce the script as written",
        "distractors": ["He offered to pay for the episode's production out of his own pocket", "He agreed to add a celebrity guest star cameo to save the episode", "He promised that Kramer would do an elaborate physical stunt in the next episode"],
        "d": 2
    },
    {
        "q": "Why did Jason Alexander once storm into Larry David's office and threaten to quit the series during Season 3?",
        "correct": "He was written out of the episode 'The Pen' and furious that an episode was produced without George Costanza",
        "distractors": ["He discovered that Julia Louis-Dreyfus was making more money than him", "He was unhappy that George was balding and losing his hair on camera", "He felt Kramer was getting all the funny punchlines"],
        "d": 2
    },
    {
        "q": "What did Jason Alexander tell Larry David during that Season 3 confrontation about 'The Pen'?",
        "correct": "\"If you don't need me, I don't want to be here. If you write another episode without me, do it permanently.\"",
        "distractors": [
            "\"George is the engine of this show, and without me, Jerry has no one to bounce off of.\"",
            "\"I am a Broadway-trained actor and will not be treated like a background extra.\"",
            "\"You either give George an A-story every week or let me go back to New York.\""
        ],
        "d": 2
    },
    {
        "q": "Why was the Season 4 episode 'The Contest' submitted with immense anxiety to NBC Standards and Practices?",
        "correct": "The entire plot centered on masturbation, though the word was never spoken once in the episode",
        "distractors": ["The script contained over twenty instances of profane street slang", "George's mother was depicted in a compromising situation with a neighbor", "Jerry's girlfriend was revealed to be an undercover vice detective"],
        "d": 1
    },
    {
        "q": "What critical reception did the May 1998 Seinfeld series finale receive from prominent media outlets like The New York Times?",
        "correct": "Widespread disappointment and harsh criticism for being cynical, self-indulgent, and putting the beloved characters on trial",
        "distractors": ["Unanimous universal praise hailed as the greatest television conclusion in history", "Indifference, as the broadcast was overshadowed by breaking international news", "A boycott by the U.S. Postal Service over Newman's testimony"],
        "d": 1
    },
    {
        "q": "What did Larry David do in Season 7 of Curb Your Enthusiasm to address the lingering dissatisfaction with the Seinfeld finale?",
        "correct": "He organized a full fictional Seinfeld reunion show with the entire original cast to write a 'proper' finale",
        "distractors": ["He publicly apologized in a full-page advertisement in Variety", "He filmed a documentary dissecting every joke in the 1998 finale", "He released an alternate ending where the characters win their appeal"],
        "d": 1
    },
    {
        "q": "What emergency protocol was enacted by the Los Angeles Fire Department on May 14, 1998, when Frank Sinatra suffered a heart attack during the Seinfeld finale?",
        "correct": "The ambulance reached Cedars-Sinai hospital in record time because the streets and freeways of L.A. were completely deserted",
        "distractors": ["The sirens were disabled so as not to disturb neighborhoods watching the broadcast", "Paramedics parked outside an appliance store to catch the final scene", "The hospital staff delayed Sinatra's intake until the commercial break"],
        "d": 2
    },
    {
        "q": "Which major cast member of Seinfeld notoriously refused to participate in DVD commentary tracks and behind-the-scenes interviews for years?",
        "correct": "Michael Richards (prior to the eventual official DVD box set release)",
        "distractors": ["Jerry Seinfeld", "Jason Alexander", "Julia Louis-Dreyfus"],
        "d": 3
    },

    # Grace Under Fire & The Brett Butler Meltdown (10 questions)
    {
        "q": "What was the primary cause of the chaotic backstage implosion of ABC's hit sitcom Grace Under Fire?",
        "correct": "Star Brett Butler's escalating substance abuse, erratic behavior, and intense paranoia on set",
        "distractors": ["A criminal embezzlement investigation involving the accounting department", "A protracted Writers Guild strike that shut down production for eight months", "A bitter ownership lawsuit between ABC and producer Chuck Lorre"],
        "d": 2
    },
    {
        "q": "Why was creator and executive producer Chuck Lorre forced out of Grace Under Fire during its second season?",
        "correct": "Unrelenting creative battles with star Brett Butler, who demanded complete script control and clashed over jokes",
        "distractors": ["He was fired by ABC for going $10 million over production budget", "He left voluntarily to write for The Tonight Show with Jay Leno", "He was poached by CBS to create a new drama series"],
        "d": 2
    },
    {
        "q": "What shocking incident in 1996 led actress Julie White (who played Grace's best friend Nadine) to abruptly quit the hit show?",
        "correct": "Unbearable tension and erratic abuse from Brett Butler on set",
        "distractors": ["She was offered a lead role in an Oscar-winning feature film", "A salary dispute with production company Carsey-Werner", "She refused to sign a five-year contract extension"],
        "d": 2
    },
    {
        "q": "Why did the mother of 12-year-old actor Jon Paul Steuer (who played Grace's son Quentin) pull him off the show in Season 4?",
        "correct": "Brett Butler reportedly flashed her bare breasts at the young actor in her dressing room",
        "distractors": ["He was injured in a car crash on the studio lot", "Producers demanded he work 16-hour days in violation of child labor laws", "The child actor developed a severe phobia of television cameras"],
        "d": 3
    },
    {
        "q": "How did ABC finally handle the crisis of Grace Under Fire in February 1998 during its fifth season?",
        "correct": "ABC abruptly cancelled the top-20 show mid-season and shut down production permanently after Butler entered rehab again",
        "distractors": ["ABC recast the lead character with Rosanne Barr", "ABC converted the remainder of the season into an animated series", "ABC moved the show to Saturday mornings with a different cast"],
        "d": 2
    },
    {
        "q": "Which acclaimed sitcom producer was brought in as a replacement showrunner on Grace Under Fire, only to quit in frustration after two weeks?",
        "correct": "Bob Myer",
        "distractors": ["Paul Simms", "David Crane", "Garry Shandling"],
        "d": 3
    },
    {
        "q": "In what state did Brett Butler's character Grace Kelly live on Grace Under Fire?",
        "correct": "Missouri",
        "distractors": ["Ohio", "Kentucky", "Tennessee"],
        "d": 2
    },
    {
        "q": "What recovery theme was central to Grace Kelly's character on the show, which mirrored Butler's real-life battles?",
        "correct": "Recovering from alcoholism and escaping an abusive marriage",
        "distractors": ["Recovering from gambling addiction and bankruptcy", "Coping with the loss of a spouse in a military conflict", "Rebuilding life after an occupational disability"],
        "d": 1
    },
    {
        "q": "What major award did Brett Butler receive in 1994 before her personal struggles derailed the series?",
        "correct": "The People's Choice Award for Favorite Female Performer in a New Television Series",
        "distractors": ["The Primetime Emmy for Outstanding Lead Actress", "The Golden Globe for Best Supporting Actress", "The Screen Actors Guild Lifetime Achievement Award"],
        "d": 2
    },
    {
        "q": "Which production company produced Grace Under Fire along with Roseanne, 3rd Rock from the Sun, and That '70s Show?",
        "correct": "Carsey-Werner Productions",
        "distractors": ["Miller-Boyett Productions", "Witt/Thomas/Harris Productions", "Stephen J. Cannell Productions"],
        "d": 2
    },

    # NewsRadio & The Phil Hartman Tragedy (10 questions)
    {
        "q": "What unspeakable real-life tragedy shattered the cast and crew of NewsRadio in May 1998 between Seasons 4 and 5?",
        "correct": "Beloved star Phil Hartman was murdered in his sleep by his wife Brynn, who then committed suicide",
        "distractors": ["Phil Hartman died in a private plane crash in Montana", "Phil Hartman suffered a fatal heart attack during rehearsals on set", "Phil Hartman died of carbon monoxide poisoning at his mountain cabin"],
        "d": 1
    },
    {
        "q": "Which close friend of Phil Hartman from Saturday Night Live agreed to join the NewsRadio cast in Season 5 to honor his memory?",
        "correct": "Jon Lovitz",
        "distractors": ["Dana Carvey", "Kevin Nealon", "Dennis Miller"],
        "d": 1
    },
    {
        "q": "What notorious real-life confrontation occurred between Jon Lovitz and Andy Dick years later regarding Phil Hartman's death?",
        "correct": "Lovitz physically slammed Dick into a restaurant bar after Dick joked about Hartman's murder and re-introducing Brynn to drugs",
        "distractors": ["They engaged in a fistfight during an episode of Saturday Night Live", "Lovitz sued Dick in civil court for defamation of character", "Dick threw a drink at Lovitz during an Emmy Awards gala"],
        "d": 2
    },
    {
        "q": "How did the Season 5 premiere of NewsRadio ('Bill Moves On') handle the death of Phil Hartman's character Bill McNeal?",
        "correct": "The characters return from his funeral, read personal letters Bill left for them, and openly weep on camera",
        "distractors": ["Bill McNeal was revealed to have taken an anchor job in Paris", "Bill's death was never directly explained, but his microphone was retired", "A stand-in actor played Bill from behind in a brief farewell scene"],
        "d": 1
    },
    {
        "q": "Why was filming the Season 5 premiere of NewsRadio reported to be one of the most agonizing experiences in sitcom history?",
        "correct": "Production had to be halted dozens of times because cast members broke down in uncontrollable sobs during takes",
        "distractors": ["The studio audience staged a walkout in protest of the dark tone", "Network executives tried to confiscate the script before filming", "Jon Lovitz forgot his lines and walked off the soundstage"],
        "d": 2
    },
    {
        "q": "What nickname did Phil Hartman earn among the cast and crew of Saturday Night Live and NewsRadio for his unwavering reliability?",
        "correct": "\"The Glue\"",
        "distractors": [
            "\"The Rock\"",
            "\"The Anchor\"",
            "\"The Professional\""
        ],
        "d": 2
    },
    {
        "q": "In 1998, what animated feature film released by DreamWorks was dedicated to the memory of Phil Hartman?",
        "correct": "Small Soldiers (in which he played Phil Fimple)",
        "distractors": ["Antz", "The Prince of Egypt", "Toy Story 2"],
        "d": 2
    },
    {
        "q": "What cartoon character on The Simpsons was officially retired by Matt Groening following Phil Hartman's death?",
        "correct": "Troy McClure and Lionel Hutz",
        "distractors": ["Principal Skinner and Lionel Hutz", "Chief Wiggum and Troy McClure", "Fat Tony and Dr. Nick Riviera"],
        "d": 1
    },
    {
        "q": "Which NewsRadio star, who later achieved podcast superstardom, credited Phil Hartman with teaching him professionalism on set?",
        "correct": "Joe Rogan",
        "distractors": ["Dave Foley", "Stephen Root", "Andy Dick"],
        "d": 1
    },
    {
        "q": "What posthumous honor did Phil Hartman receive from the Television Academy in 1999 for his final season on NewsRadio?",
        "correct": "A Primetime Emmy nomination for Outstanding Supporting Actor in a Comedy Series",
        "distractors": ["The Television Academy Hall of Fame Induction", "The Bob Hope Humanitarian Award", "A special Lifetime Achievement Emmy citation"],
        "d": 2
    },

    # Home Improvement: Off-Screen Facts & Departures (10 questions)
    {
        "q": "Why did Pamela Anderson leave her role as Tool Time girl Lisa on Home Improvement after Season 2?",
        "correct": "To star full-time as C.J. Parker on Baywatch, which became a global phenomenon",
        "distractors": ["She was fired by producers after demanding parity with Tim Allen", "She married rock star Tommy Lee and took an acting hiatus", "She was cast as the lead in the feature film Barb Wire"],
        "d": 1
    },
    {
        "q": "Why did teen heartthrob Jonathan Taylor Thomas (JTT) decline to return for the 1999 Home Improvement series finale?",
        "correct": "Tensions had flared with Tim Allen and producers over his early departure, and he chose to focus on his college studies",
        "distractors": ["He was in Europe filming a major Hollywood blockbuster", "He was hospitalized with a serious sports injury", "A legal injunction barred him from the Disney studio lot"],
        "d": 2
    },
    {
        "q": "What real-life criminal conviction from Tim Allen's past resurfaced in national media during Home Improvement's peak?",
        "correct": "His 1978 arrest at Kalamazoo/Battle Creek airport for possessing over a pound of cocaine, serving over two years in federal prison",
        "distractors": ["A 1982 arrest for grand theft auto in Detroit", "A 1985 federal wire fraud conviction in Chicago", "A 1976 armed robbery charge in Minneapolis"],
        "d": 2
    },
    {
        "q": "How did Home Improvement star Richard Karn (Al Borland) get his legendary audition for the show?",
        "correct": "He received a traffic citation for rolling through a stop sign, attended traffic school, and met an agent who told him about the audition",
        "distractors": ["He was delivering catering sandwiches to Tim Allen's dressing room", "He was working as an actual carpenter on the Disney soundstage", "He won a nationwide lookalike contest for flannel shirt models"],
        "d": 2
    },
    {
        "q": "Why did Earl Hindman (Wilson) carry a small wooden picket fence in front of his face during curtain calls in front of the studio audience?",
        "correct": "To maintain the illusion and mystery of his obscured face for the audience and viewers",
        "distractors": ["He had severe stage fright and couldn't face crowds directly", "He suffered a facial nerve injury during rehearsal", "His contract with Disney prohibited showing his face in live theaters"],
        "d": 1
    },
    {
        "q": "What Disney executive championed Tim Allen and oversaw the creation of Home Improvement based on Allen's stand-up routine?",
        "correct": "Michael Eisner and Jeffrey Katzenberg",
        "distractors": ["Bob Iger and Frank Wells", "Don Ohlmeyer and Warren Littlefield", "Barry Diller and Michael Ovitz"],
        "d": 2
    },
    {
        "q": "What was the original working title of Home Improvement during early script development?",
        "correct": "Hammer Time",
        "distractors": ["Tool Time", "Man's World", "Power Tools"],
        "d": 2
    },
    {
        "q": "Which actress was originally cast as Jill Taylor and shot the original pilot before being replaced by Patricia Richardson?",
        "correct": "Frances Fisher",
        "distractors": ["Geena Davis", "Annette O'Toole", "Jobeth Williams"],
        "d": 3
    },
    {
        "q": "Why did Patricia Richardson initially hesitate to take the role of Jill Taylor just days before production began?",
        "correct": "She had just given birth to twins and did not want the grueling schedule of a weekly network sitcom",
        "distractors": ["She was under contract for an off-Broadway play in Manhattan", "She didn't find Tim Allen's stand-up comedy funny", "She had already signed on to star in a CBS medical drama"],
        "d": 2
    },
    {
        "q": "How much money per episode were Tim Allen and Patricia Richardson reportedly offered by ABC to return for a ninth season, which Richardson turned down?",
        "correct": "Allen was offered $2 million per episode and Richardson $1.25 million, but Richardson refused to return",
        "distractors": ["Allen was offered $1 million and Richardson $500,000", "They were offered $3 million each per episode", "They were offered a 50% ownership stake in ABC"],
        "d": 2
    },

    # Full House & TGIF Behind the Scenes (5 questions)
    {
        "q": "Why did John Stamos famously demand that toddler twins Mary-Kate and Ashley Olsen be fired during Season 1 of Full House?",
        "correct": "They cried constantly during scenes, prompting producers to briefly replace them before realizing the replacements were worse",
        "distractors": ["Their parents demanded executive producer credit on screen", "They were visibly afraid of the Tanner family dog Comet", "Stamos wanted his real-life nephew cast in the role"],
        "d": 2
    },
    {
        "q": "What sharp contrast existed between Bob Saget's wholesome Danny Tanner TV persona and his real-life stand-up comedy career?",
        "correct": "His real-life stand-up act was notoriously filthy, profane, and sexually explicit",
        "distractors": ["He was a serious classical stage actor who refused to tell jokes off camera", "He was a quiet, introverted recluse who practiced silent meditation", "He was a political commentator who debated senators on cable news"],
        "d": 1
    },
    {
        "q": "Which Full House star is widely cited as the real-life ex-boyfriend who inspired Alanis Morissette's biting 1995 rock anthem 'You Oughta Know'?",
        "correct": "Dave Coulier (Joey Gladstone)",
        "distractors": ["John Stamos (Jesse Katsopolis)", "Bob Saget (Danny Tanner)", "Scott Weinger (Steve Hale)"],
        "d": 1
    },
    {
        "q": "What physical styling detail did Rider Strong (Shawn Hunter) reportedly despise throughout seven seasons of Boy Meets World?",
        "correct": "His iconic center-part 'curtains' haircut, which producers strictly forbade him from cutting",
        "distractors": ["The heavy leather motorcycle jackets he was forced to wear in 90-degree heat", "The colored contact lenses he had to wear to look like Ben Savage", "The elevator shoe lifts he was required to wear next to William Daniels"],
        "d": 2
    },
    {
        "q": "What intense rehearsal environment did Boy Meets World creator Michael Jacobs maintain for the young cast?",
        "correct": "Rigorous, high-pressure table reads and intense line notes that treated the adolescent actors like seasoned Broadway professionals",
        "distractors": ["Allowing the kids to improvise all their own dialogue without scripts", "Holding rehearsals on a basketball court where missed lines required running laps", "Requiring the young actors to attend three hours of daily military drills"],
        "d": 2
    }
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "staging", "90s_sitcoms_batch8.json")
    make_batch(q_batch8, 8, out)
