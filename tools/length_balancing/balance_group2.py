#!/usr/bin/env python3
"""
Length-Bias Balancer for Group 2
(80s TV, Standup, Late Night, Podcasts & SNL)
"""

import json
import re
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GROUP2_IN = os.path.join(BASE_DIR, "tools", "length_balancing", "group2.json")
GROUP2_OUT = os.path.join(BASE_DIR, "tools", "length_balancing", "group2_balanced.json")

# Import curated name expansions
from name_dict import NAME_DICT

# Curated custom phrase expansions for items that need rich natural wording
CUSTOM_MAP = {
    # Late Night TV
    "11:00 p.m.": "11:00 p.m. Eastern / 10:00 p.m. Central standard time",
    "Afraid": "Deeply bitter or cynical about the future of comedy",
    "Late Night with Jon": "Late Night with Jon Stewart on MTV and Comedy Central",
    "Radio City Music Hall": "Radio City Music Hall (located in Rockefeller Center)",
    "The Daily Dozen": "The Daily Dozen (Twelve Points of View and Sarcastic Observations)",
    "Hip replacement": "Total bilateral hip replacement surgery and physical therapy",
    "Animal Antics": "Animal Antics and Wild Critter Parade",
    "Threw a drink at Dave": "Threw a tall glass of ice water directly into Dave's face",
    "In Living Color and Frasier": "In Living Color sketches and the writers' room of Frasier",
    "Sir Barks-a-Lot": "Sir Barks-a-Lot (The Aristocratic Sarcastic Hound)",
    "Conan Goes Global": "Conan Goes Global: Adventures Without Cultural Borders",
    "Motor Mondays": "Motor Mondays with Jay Leno and Special Guests",
    "Throwing an egg at the host": "Throwing a cracked raw egg directly at Jimmy Fallon's face",
    "About four years": "About four full broadcast television seasons",
    "The Beacon Theatre": "The Historic Beacon Theatre on Broadway in Manhattan",
    "Final Joke": "Final Joke of the Evening and Goodbye",
    "Friday Letters": "Friday Letters to Viewer Correspondents",
    "Notes to Self": "Notes to Self and Reminders for the Weekend",
    "Wyatt Cenac": "Wyatt Cenac (former Daily Show correspondent and stand-up)",
    "Tom Snyder": "Tom Snyder (inaugural host of The Late Late Show on CBS)",
    "David Spade": "David Spade (The Hollywood Minute on Saturday Night Live)",

    # How Did This Get Made?
    "Krasnovia": "The fictional Soviet-bloc territory of Krasnovia",
    "800-PAUL-NOW": "1-800-PAUL-NOW (toll-free listener hotline)",
    "Missing in Action": "Missing in Action (Chuck Norris Vietnam rescue vehicle)",
    "Prayer of the Rollerboys": "Prayer of the Rollerboys (Corey Haim futuristic roller-skating movie)",
    "Out for Justice": "Out for Justice (Steven Seagal Brooklyn action film)",
    "Slapshot the Beaver": "Slapshot the Beaver (costumed sports mascot)",
    "Cotton strips and molten wax": "Cotton fabric strips soaked in scalding molten paraffin wax",
    "A ghost infant": "A supernatural ghost infant haunting the premises",
    "An explosion sound": "A deafening cinematic explosion sound effect",
    "Dynasty Typewriter": "Dynasty Typewriter at the Hayworth Theatre in Los Angeles",
    "The Banzai Blaster": "The Banzai Blaster High-Velocity Laser Gun",
    "Season of the Witch": "Season of the Witch (starring Nicolas Cage)",
    "A swordfish named \"Moby\"": "A massive great swordfish named \"Moby Dick\"",
    "Transformers": "Transformers (directed by Michael Bay and produced by Steven Spielberg)",
    "\"Hi everyone, I'm thrilled to be here.\"": "\"Hi everyone, I am absolutely thrilled, overjoyed, and delighted to be here today!\"",
    "Their skin turns into peanut brittle": "Their entire skin surface turns into crunchy edible peanut brittle",
    "He swaps bodies with Danny DeVito": "He inexplicably swaps biological bodies with Danny DeVito for the weekend",
    "A poison dart frog": "A deadly tropical neon-colored poison dart tree frog",
    "They were mutated by radiation from Atlantis": "They were heavily mutated by radioactive toxic waste from the lost sunken city of Atlantis",
    "The Cutting Room Floor": "The Cutting Room Floor (unreleased outtakes and extended mailbag)",
    "Fifty Shades of Grey": "Fifty Shades of Grey (the feature film adaptation of the romance novel)",
    "\"TAKE THE MASK OFF!\"": "\"TAKE THE MASK OFF RIGHT NOW! TAKE IT OFF!\"",
    "\"Can't talk, gotta take a dump!\"": "\"Can't talk right now, I really gotta take a massive urgent dump!\"",
    "\"Shut your mouths!\"": "\"Shut your mouths right now and please settle down, ladies!\"",
    "The Apology Corner": "The Apology Corner and Corrections Segment",
    "\"Why are you poor?\"": "\"Why are you all so incredibly poor up there in the rafters?\"",
    "Chilled monkey brains": "Chilled monkey brains served in a coconut shell",
    "An inflatable reindeer": "An oversized illuminated inflatable holiday reindeer lawn decoration",
    "Mark Wahlberg": "Mark Wahlberg (Marky Mark and the Funky Bunch)",
    "\"Call the police!\"": "\"Call the local police and emergency services right now!\"",
    "Government experiments": "Secret top-level government genetic military experiments",
    "An origami flower": "A delicate folded paper origami lotus flower",
    "Tennis rackets": "Vintage wooden Dunlop tennis rackets",
    "Street Fighter": "Street Fighter (the live-action video game adaptation)",
    "A giant snail": "A colossal slimy prehistoric garden snail",
    "Judgment Night": "Judgment Night (action thriller with the rock/rap soundtrack)",
    "Conan the Destroyer": "Conan the Destroyer (starring Arnold Schwarzenegger)",
    "Black and white tinting": "High-contrast monochromatic black and white sepia tinting",
    "Rocky IV": "Rocky IV (directed by and starring Sylvester Stallone)",
    "Twisted Pair": "Twisted Pair (independent film written and directed by Neil Breen)",

    # Comedy Bang! Bang!
    "Floor creaks and floorboard squeaks": "Floor creaks, floorboard squeaks, and rattling chains sound effect",
    "Neither informative nor entertaining!": "Neither particularly informative nor especially entertaining in any conceivable way!",
    "\"That's a callback!\"": "\"That is an uncredited brilliant comedic callback!\"",
    "Dalton Wilcox": "Dalton Wilcox (Poet Laureate of the West & author of You Must Buy Your Wife at Least as Much Jewelry as You Buy Your Horse)",
    "\"Honk If You're A Truck\"": "\"Honk If You Love Big Country Diesel Trucks and Honking on the Open Highway\"",
    "\"The Hey Nongman\"": "\"The Hey Nongman (classic catchphrase coined by Jason Mantzoukas)\"",
    "The Pranksters*": "The Pranksters (Gil Faizon and George St. Geegland from Oh, Hello)*",
    "A broken bottle": "A jagged broken green glass tavern beer bottle",
    "Three": "Three brand new episodes released every single week without fail",
    "Soccer matches in London": "Premier League professional soccer matches played live in London",
    "Guests are forced to repeat it three times": "Guests are immediately forced to repeat the statement aloud three consecutive times",
    "No questions are allowed; Scott closes the floor immediately": "No questions are allowed whatsoever; Scott immediately bangs the gavel and closes the floor to inquiries",
    "Red Velvet Cupcakes": "Gourmet freshly baked cream-cheese frosted Red Velvet Cupcakes",
    "\"We're already at an hour and fifteen.\"": "\"We're already at an hour and fifteen minutes, folks, wrap it up!\"",
    "He undergoes radical voice surgery": "He undergoes radical vocal cord reconstruction surgery in Switzerland",
    "They drove sports cars": "They drove souped-up vintage sports cars through the graveyard",
    "The Christmas Special": "The Annual Holiday Christmas Spectacular Multi-Part Special",
    "Extreme horse-riding": "Extreme cross-country equestrian obstacle horse-riding",
    "The Pastry Prince": "The Pastry Prince of Hoboken, New Jersey",
    "\"Oh, dio mio!\"": "\"Oh, dio mio! Santa Maria and holy cannoli!\"",
    "The Hollywood Roosevelt Hotel": "The Historic Hollywood Roosevelt Hotel Penthouse Suite",
    "A plate of unpeeled potatoes": "A massive overflowing wooden plate of raw unpeeled russet potatoes",
    "\"The 500th Anniversary\"": "\"The 500th Anniversary Golden Jubilee Gala Spectacular\"",
    "Classical ballerina": "Professional world-renowned classical concert ballerina",
    "\"Bone of contention, Queef of the night!\"": "\"Bone of contention, Queef of the howling moonlight midnight night!\"",
    "Sent him to boarding school": "Sent him far away to an elite strict Swiss boarding school",
    "Mary Phillips": "Mary Phillips (long-time listener from Northern California)",
    "Coach Little": "Coach Little (varsity assistant wrestling coach)",
    "The Terminator": "The Terminator (cybernetic organism sent back in time)",
    "Rodney Dangerfield": "Rodney Dangerfield (famed stand-up comic who got no respect)",
    "Cactus Jack": "Cactus Jack (notorious frontier outlaw and gunslinger)",
    "Bizness Girl": "Bizness Girl (aspiring corporate entrepreneur)",
    "Chief Donahue": "Chief Donahue (local municipal police captain)",
    "Peanuts Holmes": "Peanuts Holmes (unlicensed private investigator)",
    "The Diesel Brothers": "The Diesel Brothers (country rock harmony duo)",
    "\"Open door, shut door\"": "\"Open door, shut door, lock the lock forever\"",
    "Milwaukee": "Milwaukee, Wisconsin (on the shores of Lake Michigan)",
    "Captain Bubble": "Captain Bubble (children's party entertainer)",
    "\"Hot dog thumb\"": "\"Permanent hot dog thumb infection\"",
    "Fabrice Fabrice": "Fabrice Fabrice (the craft services coordinator extraordinaire)",
    "\"What the hell?!\"": "\"What on earth and what the hell is happening?!\"",
    "\"Time waits for no man!\"": "\"Time and the tides wait for no mortal man!\"",
    "Stacy Keibler": "Stacy Keibler (former professional wrestling valet and model)",
    "The Staten Island Ferry": "The Staten Island Ferry commuting across New York Harbor",

    # Taskmaster UK
    "0": "A total score of zero points (disqualified)",
    "1": "Exactly one point awarded by Greg",
    "12": "A total of 12 complete task assignments",
    "164": "A grand total of 164 series points",
    "Series 1": "Series 1 (the inaugural five-episode broadcast run)",
    "Series 4": "Series 4 (the first full ten-episode series run)",
    "397 beans": "Approximately 397 individual baked beans",
    "The kitchen": "The kitchen inside the main Taskmaster cottage",
    "Guy Montgomery": "Guy Montgomery (Taskmaster New Zealand contestant)",
    "A single tea cup": "A delicate antique porcelain single tea cup with saucer",
    "The Supreme Ruler": "The Supreme Ruler and Master of Ceremonies",
    "\"Rubies in the dust\"": "\"Rubies and emeralds scattered in the roadside dust\"",
    "A bag of potting soil": "A heavy fifty-pound bag of organic enriched garden potting soil",
    "A woolen crown for Greg": "An elaborately hand-knitted woolen royal crown for Greg Davies",
    "A plastic duck on a turntable": "A squeaking yellow rubber duck spinning on an electric DJ turntable",
    "A toy dinosaur from his childhood": "A green plastic Tyrannosaurus Rex toy from his early childhood",
    "Joe Lycett, Lolly Adefope, and Noel Fielding": "Joe Lycett, Lolly Adefope, and Noel Fielding (The Magnificent Three)",
    "Operation": "Operation (classic electronic board game with buzzing red nose)",
    "Do not look at Alex.": "Do not look directly at Little Alex Horne under any circumstances.",
    "A plastic spider on a doll": "A terrifying glow-in-the-dark plastic spider perched on a doll",
    "He pierced the container with a stick": "He punctured the sealed plastic container using a sharpened wooden garden stick",
    "Hugged him while whispering Swedish poetry": "Hugged Alex tightly from behind while whispering 18th-century Swedish romantic poetry into his ear",
    "Asking repeatedly about his favorite color": "Asking Alex Horne repeatedly and incessantly about his favorite primary color",
    "Drank a whole pint without swallowing visibly": "Drank an entire pint of warm British bitter without moving his throat or swallowing visibly",
    "Channel 5": "Channel 5 (UK terrestrial free-to-air television network)",
    "Garden shears": "Heavy-duty outdoor iron garden pruning shears",
    "The Housemates": "The Housemates (team of competitive rivals)",
    "An upside-down pineapple": "A prickly tropical upside-down fresh Dole pineapple",
    "A real poisonous tarantula": "A hairy live venomous Brazilian bird-eating tarantula",
    "A clown suit with flippers": "A bright polka-dot circus clown suit paired with yellow scuba diving flippers",
    "Associate Producer & Umpire": "Associate Taskmaster Producer & Head Match Umpire",
    "He missed by three centimeters": "He missed the circular target opening by just barely three centimeters",
    "Kerry Godliman and Liza Tarbuck": "Kerry Godliman and Liza Tarbuck (former series champions)",
    "A shiny metallic superhero jumpsuit": "An eye-catching shiny metallic superhero jumpsuit complete with flowing gold cape",
    "He talks to his reflection every morning": "He holds detailed thirty-minute motivational pep talks with his bathroom mirror reflection every morning",
    "Romesh Ranganathan, Jon Richardson, Al Murray, Hugh Dennis, Mark Watson": "Romesh Ranganathan, Jon Richardson, Al Murray, Hugh Dennis, and Mark Watson (The Taskmaster All-Star Contenders)",
    "Paul Wheeler": "Paul Wheeler (long-time British television and comedy director)",
    "His lucky penny": "A polished 1971 decimalization lucky copper penny",
    "Kerry Godliman's mother": "Kerry Godliman's mother (special mystery guest)",
    "\"Rosalind, She Loves to Swim\"": "\"Rosalind, She Truly Loves to Swim in the Ocean Waves\"",
    "He dressed as a strawberry on a cake": "He dressed up head-to-toe as a giant red glazed strawberry on top of a wedding cake",
    "How many days there are in a weekend": "How many days and hours there are in a standard working weekend",
    "Pop 20 balloons using only household utensils": "Pop 20 colorful rubber balloons using only standard household kitchen utensils",
    "Lou Sanders, Richard Herring, Sarah Kendall, Morgana Robinson, Dara Ó Briain": "Lou Sanders, Richard Herring, Sarah Kendall, Morgana Robinson, and Dara Ó Briain (Champions of Champions Team)",
    "\"Innits and whatsits\"": "\"Innits, whatsits, and whatever elses you want to call it, bro\"",
    "The Retirement Village": "The Retirement Village (team of experienced veteran contestants)",
    "An enormous slab of marble": "A towering three-ton rectangular slab of Italian Carrara white marble",
    "An upside-down monster in a bush": "A terrifying upside-down hairy papier-mâché monster concealed in a blackberry bush",
    "Walked directly across the forbidden zone": "Walked in a straight uninterrupted line directly across the brightly marked forbidden red zone",
    "\"Quack!\"": "\"Quack! Quack! Quack like an angry goose!\"",
    "A giant golden statue of Greg's head": "An oversized gilded golden statue depicting Greg Davies' regal head and shoulders",
    "Hid inside it while rolling down a steep hill": "Hid curled up tightly inside the wheelie bin while rolling uncontrollably down a steep grassy hill",
    "A hollowed-out pumpkin": "A freshly carved hollowed-out Halloween pumpkin with jagged eyeholes",
    "Slicing it with a pizza cutter": "Carefully slicing through the middle with a revolving stainless steel pizza cutter wheel",
    "An authentic 18th-century violin": "A masterfully crafted authentic 18th-century Italian concert violin in a velvet case",
    "Showing off his natural dentistry": "Showing off his gleaming all-natural orthodontic dentistry and pristine molars",
    "Jamali Maddix and Charlotte Ritchie": "Jamali Maddix and Charlotte Ritchie (The Cool & Chaotic Duo)",
    "Big Man Asim": "Big Man Asim Chaudhry (The Undefeated Champion)",
    "Ceramic plates": "Delicate hand-glazed Portuguese ceramic dinner plates",
    "David Baddiel (Series 9)": "David Baddiel (Series 9 contestant & Three Lions writer)",
    "Melbourne Comedy Festival (2012)": "Melbourne International Comedy Festival Gala in Australia (2012)",
    "An endorsement video from Courtney Love": "An exclusive personalized video endorsement recorded by Courtney Love from Hole",
    "Jessica Knappett kicked over Greg's throne": "Jessica Knappett accidentally tripped and kicked over Greg Davies' gilded velvet throne",
    "Filming another sitcom": "Filming a leading role in a major prime-time BBC television sitcom",
    "The Optimist and the Realist": "The Optimist and the Cynical Hard-Nosed Realist",
    "Cut it in half with garden shears": "Carefully cut the tie in half using heavy-duty rusted iron garden shears",
    "He drew Alex's face instead of the subject": "He insisted on drawing Little Alex Horne's face over and over instead of the actual assigned subject",
    "Huw Edwards": "Huw Edwards (former BBC News at Ten chief news presenter)",
    "An engraved silver teapot": "An antique Victorian hand-engraved Sterling silver four-cup teapot with claw feet",
    "\"It's an absolute shambles\"": "\"It is an absolute, unmitigated, catastrophic shambles from top to bottom\"",
    "Carefully measuring with a ruler": "Carefully and methodically measuring each centimeter with a clear plastic school ruler",
    "All contestants participated together": "All five contestants participated simultaneously together as a united ensemble",
    "Completely ignoring his physical presence": "Completely and utterly ignoring Alex's physical presence and refusing eye contact",

    # Why Won't You Date Me?
    "Horse ranch in Texas": "A sprawling five-hundred-acre horse ranch outside Austin, Texas",
    "Stopped releasing episodes for a year": "Completely stopped releasing any new podcast episodes for an entire calendar year",
    "Glass shattering followed by screaming": "Loud sound of shattering tavern glass followed by bloodcurdling hysterical screaming",
    "Classical baroque music": "18th-century classical baroque harpsichord concerto movements",
    "Completely ignoring the guest and ending the episode": "Completely turning her back on the guest, going silent, and abruptly ending the episode immediately",
    "Swipe Right Confessions": "Swipe Right Confessions and Disaster Date Recaps",
    "He unplugged it because of electricity noise": "He unplugged her refrigerator because he claimed the ambient electricity hum gave him bad spiritual vibrations",
    "Ferrets": "Domestic pet rescue ferrets named Barnaby and Clementine",
    "Downtown LA Arts District": "A renovated converted industrial brick loft in the Downtown LA Arts District",
    "Her Instagram aesthetic grid": "Her meticulously curated pastel Instagram photo grid aesthetic",
    "Bitterly scolding them and telling them to unsubscribe": "Bitterly scolding the happy couple on air and screaming at them to immediately unsubscribe from the podcast feed",
    "Melbourne Comedy Festival": "The Melbourne International Comedy Festival Roadshow in Australia",
    "Banning the guest from ever working in comedy again": "Vowing to blacklist the guest and ban them from ever booking another comedy gig in Los Angeles",
    "The champion's choice": "The champion's undisputed choice for romantic greatness",
    "Madison Square Garden": "The main sports arena at Madison Square Garden in New York City",
    "A true sign of mystery and cool": "A true, unquestioned badge of aloof masculine mystery and classic cool",
    "Her collection of vintage comic books": "Her prized multi-thousand-dollar collection of vintage Silver Age superhero comic books",
    "North Korea": "The Democratic People's Republic of Korea (North Korea)",
    "Heavy metal screamo": "Underground Swedish heavy metal guttural screamo vocals",
    "A companion comic strip in daily newspapers": "A syndicated weekly four-panel companion comic strip published in major metropolitan daily newspapers",
    "Formal, conservative relationship counseling": "Traditional, hyper-conservative, religious pre-marital relationship therapy and counseling",
    "Ordering tap water at an ultra-exclusive bar": "Ordering lukewarm municipal tap water with no ice at an ultra-exclusive VIP Hollywood cocktail lounge",
    "Only communicating via voice memos recorded in French": "Exclusively communicating via three-minute theatrical voice memos recorded in broken, pretentious French",
    "\"Thirst trapping\"": "\"Aggressive algorithmic thirst trapping on TikTok and Instagram\"",
    "80s heavy metal guitar solo": "A screeching, distorted 1980s heavy metal electric guitar solo with double-kick drums",
    "The head table with the bride and groom": "The glamorous head table seated directly between the radiant bride and groom",
    "A Tesla Model 3": "A brand new electric midnight-silver metallic Tesla Model 3 with self-driving capabilities",
    "Diet ginger ale": "A tall icy glass of diet sparkling Canada Dry ginger ale with a squeeze of lime",
    "\"Crypto brokers\"": "\"Self-proclaimed decentralized cryptocurrency brokers and NFT peddlers\"",
    "Def Jam Recordings": "Def Jam Recordings and Russell Simmons Enterprises",
    "Calls the listener live on air without warning": "Dials the listener's mobile phone live on the air and confronts them on speakerphone without prior warning",
    "Proof they should pay for the whole meal": "Irrefutable legal proof that they should be obligated to pay for every course of the expensive meal",
    "Seeking an arch-nemesis": "Seeking a diabolical comic-book arch-nemesis to challenge my worldview",
    "A husband, a million dollars, and someone to clean my gutters!": "A loving faithful husband, ten million dollars in bearer bonds, and a full-time staff to clean my gutters and detail my car!",
    "He carried fake Grammy awards in his backpack": "He proudly carried three golden spray-painted fake Grammy statues inside his leather backpack to impress strangers",
    "It is her absolute favorite venue for conversation": "It is her unquestioned favorite venue for intimate acoustic storytelling and deep romantic psychological evaluation",
    "High school guidance counselors": "Certified professional high school career and guidance counselors from her former teenage school district",
    "Advice on adopting twelve puppies at once": "A serious strategic lecture outlining the logistical benefits of adopting twelve golden retriever puppies all at once",
    "Absolutely forbidden under any circumstances": "Strictly forbidden and punishable by immediate excommunication from polite society under any circumstances",
    "That the app is only matching her with royalty": "That the algorithm has mistakenly assumed she is an aristocratic Duchess and is only matching her with European royalty",
    "\"Step away from the table!\"": "\"Step completely away from the dining table right now, sweetie, before something breaks!\"",
    "Getting locked out on fire escapes": "Accidentally getting locked outside on a narrow, rusty high-rise fire escape in the freezing winter rain",
    "Deleted the app from their phone forever": "Permanently deleted the dating profile and threw the guest's smartphone into the Pacific Ocean",
    "She fell asleep and woke up with face paint": "She accidentally fell fast asleep in the chair and woke up wearing full professional carnival face paint",
    "\"Hardcore History\"": "\"Dan Carlin's Hardcore History (Supernova in the East Multi-Part Series)\"",
    "Learning Japanese calligraphy": "Mastering traditional ancient Japanese calligraphy and building Zen rock gardens",
    "A canned laugh track from a 1950s sitcom": "A booming automated canned laugh track ripped directly from an obscure black-and-white 1950s sitcom",
    "Getting abandoned in the middle of a desert hike": "Getting completely stranded and abandoned without water in the middle of a scorching desert mountain hike",
    "Retiring from show business for romance": "Permanently retiring from show business entirely to become a reclusive homemaker in rural Vermont",
    "Why men should always pay for three years of dates": "A non-negotiable decree that men should always pay for every single meal for the first three consecutive years of dating",
    "Commercial refrigeration": "Heavy industrial commercial refrigeration walk-in meat storage lockers",
    "\"They must be doing heart surgery around the clock\"": "\"They must be performing emergency open-heart surgery around the clock with zero bathroom breaks!\"",
    "Patreon-exclusive radio plays": "Exclusive subscriber-only full-cast theatrical radio plays produced for Patreon supporters",
    "Demanding he return a stolen sweatshirt from 2008": "Aggressively demanding that he immediately return a favorite vintage college hooded sweatshirt stolen back in 2008",
    "Offering him a job as her assistant": "Offering him an immediate full-time salaried job as her personal executive assistant and dog walker",
    "Leading a 45-minute guided meditation on air": "Leading an uninterrupted forty-five-minute guided transcendental silent meditation session live on air",
    "The ultimate sign of romantic sophistication": "The unquestioned ultimate sign of luxurious five-star high-society romantic sophistication and wealth",
    "Being forced to fly first class every weekend": "Being continuously forced to fly first class on international airlines every single weekend",
    "Live streaming video games": "Live streaming competitive multiplayer battle-royale video games on Twitch for twelve hours",
    "Her sister being an international secret agent": "Her sister secretly working as an undercover international espionage operative for foreign intelligence agencies",
    "Forgive them immediately and buy them platform shoes": "Forgive them immediately on the spot and buy them customized three-inch wooden platform disco dancing shoes",
    "The entire episode was recorded while running on treadmills": "The entire marathon episode was recorded in real time while sprinting on steeply inclined commercial gym treadmills",
    "\"The Matriarch of Manhattan\"": "\"The Grand Imperial Matriarch of Manhattan, demanding absolute subservience from suitors\"",

    # Don't Tell Comedy
    "~1.2 Million": "Approximately ~1.2 Million verified YouTube subscribers",
    "~7.5 Million": "Approximately ~7.5 Million verified YouTube subscribers",
    "~500,000": "Approximately ~500,000 verified YouTube subscribers",
    "Don't Get Married": "Don't Ever Get Married (veteran marriage advice bit)",
    "Scared of Everything": "Permanently Terrified and Scared of Absolutely Everything",
    "Italian-Jewish Neurosis": "Growing Up with Extreme Italian-Jewish Cultural Neurosis",
    "The Volunteer": "The Volunteer Firefighter and Community First Responder",
    "Awkward Charity": "Awkward Charity Donations and Non-Profit Volunteering",
    "Over 50": "Over 50 major urban metropolitan centers worldwide",
    "Over 100": "Over 100 major urban metropolitan centers worldwide",
    "The Emotional Guy": "The Overly Emotional and Vulnerable Modern Guy",
    "Crying in Public": "Crying Uncontrollably in Public Places and Transit",
    "Dating an Overthinker": "Dating a Chronic Anxious Overthinker and Neurotic",
    "College Tuition": "Skyrocketing College Tuition and Predatory Student Debt",
    "Corporate Jobs": "Soul-Crushing Corporate Office Jobs and Zoom Meetings",
    "Public Transit": "Navigating Public Transit and Subway Delays in Big Cities",
    "The Masters of Comedy": "The Masters of Modern Underground Stand-Up Comedy",
    "Secret Set Hall of Fame": "The Secret Set Hall of Fame and Legends Showcase",
    "The Pioneers": "The Early Pioneers and Trailblazers of Stand-Up Comedy",
    "Tech Bro Struggles": "Tech Bro Struggles, Crypto Losses, and Startup Culture",
    "Silicon Valley Tales": "Silicon Valley Tales and Venture Capitalist Meetings",
    "The Future is Weird": "The Technological Future is Incredibly Bizarre and Strange",
    "Cultural Clashes": "Hilarious Cultural Clashes and First-Generation Expectations",
    "First Generation Blues": "First Generation Immigrant Family Pressure and Guilt",
    "The Apology Tour": "The Universal Apology Tour and Public Statements",
    "Roast Battles": "Underground Comedy Roast Battles and Insult Tournaments",
    "Extended Podcast Edition": "Extended Multi-Host Comedy Podcast and Roundtable Edition",
    "Backstage Raw": "Backstage Raw, Green Room Antics, and Uncut Footage",
    "Abbey Road Digital": "Abbey Road Digital Mastering and Sound Studios",
    "Laugh Factory Soundworks": "Laugh Factory Soundworks and Live Audio Productions",
    "ATC Audio": "All Things Comedy (ATC) Digital Audio Network",
    "Moving to Bushwick": "Moving to an Overpriced Hipster Loft in Bushwick, Brooklyn",
    "Paying Off Debt": "Desperately Paying Off Crushing Student Loan Debt",
    "Living with Parents": "Living in Your Childhood Bedroom with Your Boomer Parents",
    "Link to buy DTC branded merch": "Link to buy official DTC branded streetwear apparel and trucker hats",
    "Link to apply to be a comedian": "Link to submit audition tapes and apply to perform on future secret pop-up shows",
    "Link to donate to a comedy foundation": "Link to donate directly to the independent touring comedians healthcare foundation",
    "Jordan Peele & Dave Chappelle": "Jordan Peele & Dave Chappelle (Monkeypaw Productions)",
    "Judd Apatow & Lorne Michaels": "Judd Apatow & Lorne Michaels (Apatow Productions / Broadway Video)",
    "Tony Hinchcliffe & Joe Rogan": "Tony Hinchcliffe & Joe Rogan (Kill Tony / Deathsquad)",

    # SNL
    "A beaver": "A chatty wild woodland beaver building dams in the stream",
    "Maurice's": "Maurice's Exclusive European Haute Couture Boutique of Beverly Hills",
    "Baked potato": "Jumbo Idaho baked potato loaded with chives and sour cream",
    "Meat cleaver": "Heavy stainless-steel butcher's cleaver sharpened to a razor edge",
    "Melmac": "The distant alien planet of Melmac (home of ALF)",
    "Krypton": "The doomed crystal-covered planet of Krypton (birthplace of Superman)",
    "Ork": "The far-off peaceful planet of Ork (homeworld of Mork)",
    "Dentist": "Pediatric certified dental surgeon and root canal specialist",
    "Mail carrier": "United States Postal Service uniform mail carrier",
    "Bank teller": "Commercial bank teller and foreign currency exchange clerk",
    "Yugoslavia": "The former Balkan socialist republic of Yugoslavia",
    "Hungary": "The central European nation of Hungary and Budapest",
    "Poland": "The historic European republic of Poland and Warsaw",
    "Gork and Verna": "Gork and Verna (extraterrestrial travelers from outer galaxies)",
    "Zonker and Marsha": "Zonker and Marsha (counterculture cartoon personalities)",
    "Klaatu and Barada": "Klaatu and Barada (space emissaries from classic sci-fi)",
    "Fixing a broken television set": "Repairing a broken vintage cathode-ray wooden television console in the corner",
    "Auditioning a lounge singer": "Auditioning a tacky polyester-suited lounge singer at a grand piano",
    "Tuning an acoustic guitar": "Carefully tuning a six-string wooden acoustic folk guitar on stage",
    "The rain in Spain falls mainly on the plain": "The rain in Spain falls mainly on the grassy plain and rolling hills",
    "Never look a gift horse in the mouth": "Never look an unfamiliar gift horse in the mouth when entering town",
    "Give me liberty or give me death": "Give me absolute unyielding liberty or give me immediate noble death",
    "Frankie and Johnny Blues": "Frankie and Johnny Blues (traditional Mississippi blues duo)",
    "Big Joe and Blind Boy Blues": "Big Joe and Blind Boy Blues (legendary Chicago delta blues players)",
    "Mack and Buster Blues": "Mack and Buster Blues (traveling acoustic blues brothers)",
    "Lou Malnati's": "Lou Malnati's Pizzeria (famous Chicago deep-dish franchise)",
    "Wieners Circle": "The Wieners Circle (notorious late-night abusive hot dog stand in Lincoln Park)",
    "Pizzeria Uno": "Pizzeria Uno (historic birthplace of Chicago-style deep dish pizza)",
    "Nunchucks": "Hardwood martial arts nunchucks joined by steel chain links",
    "Bo staff": "Six-foot polished Japanese hardwood martial arts bo staff",
    "Buck Henry wore a full suit of armor": "Buck Henry wore an authentic medieval European knight's suit of polished armor",
    "Belushi was placed in handcuffs": "Belushi was dramatically placed in real metal police handcuffs by armed officers",
    "A doctor stood on stage taking pulses": "An emergency medical doctor stood prominently on stage taking cast members' pulses",
    "Instant Degree College": "Instant Degree Accredited Online Correspondence College",
    "Speed Seminary": "Accelerated Speed Seminary and Quick Pastoral Theological School",
    "Two-Hour Academy": "Two-Hour Express Professional Learning Academy and Institute",
    "Fish-O-Grinder 3000": "The Electric Fish-O-Grinder 3000 Industrial Stainless Steel Food Processor",
    "Aqua-Puree Supreme": "The Aqua-Puree Supreme Multi-Speed Kitchen Blender and Emulsifier",
    "Trout Master Deluxe": "The Trout Master Deluxe Commercial Whole-Fish Chopping Appliance",
    "Watch us now and marvel later": "Watch our magnificent bulging pecs now and marvel in complete awe later",
    "Look at us and weep later": "Look closely at our muscular thighs now and weep tears of joy later",
    "Praise us now and thank us later": "Praise our Austrian god-like bodies now and thank us profusely later",

    # 80s TV Shows
    "6 times": "A total of 6 separate consecutive prime-time broadcast seasons",
    "3 times": "A total of 3 separate consecutive prime-time broadcast seasons",
    "2 times": "Exactly 2 separate consecutive prime-time broadcast seasons",
    "Season 3": "Season 3 (the acclaimed sophomore and junior renewal run)",
    "Season 4": "Season 4 (the pivotal mid-run broadcast television season)",
    "Season 6": "Season 6 (the major transition broadcast television season)",
    "42": "42 total Primetime Emmy nominations and guild awards",
    "37": "37 total Primetime Emmy nominations and guild awards",
    "14": "14 total Primetime Emmy nominations and guild awards",
    "IRS auditor": "Federal Internal Revenue Service (IRS) tax auditor and forensic accountant",
    "Plumbing contractor": "Licensed residential plumbing contractor, pipefitter, and master drain specialist",
    "Transit bus driver": "Metropolitan municipal transit district city bus and trolley driver",
    "U.S. Presidents' Dogs": "Beloved Domestic Dogs of Historic United States Presidents in the White House",
    "Famous Postage Stamps": "Rare and Valuable Commemorative Postage Stamps of the Western Hemisphere",
    "Postal Codes of Western Europe": "International Postal and Zip Routing Codes of the Major Western European Nations",
    "McNally's Irish Pub": "McNally's Traditional South Boston Irish Drinking Pub and Taproom",
    "The King's Arms": "The King's Arms Traditional British Royal Tavern on Beacon Hill",
    "The Bull & Finch": "The Historic Bull & Finch Pub (the real-life Boston architectural inspiration)",
    "Alan Thicke": "Alan Thicke (prolific television theme songwriter, host, and actor)",
    "Mike Post": "Mike Post (iconic television composer behind Law & Order and Hill Street Blues)",
    "Allee Willis": "Allee Willis (Grammy-winning songwriter behind the Friends theme and Earth Wind & Fire)",
    "45th out of 77 prime-time programs": "45th place out of 77 prime-time network television programs that season",
    "Last place out of 102 programs": "Dead last place out of 102 network prime-time television programs broadcast",
    "12th out of 77 prime-time programs": "12th place out of 77 prime-time network television programs that season",
    "Martin": "Martin (in honor of Dr. Frasier Crane's retired detective father Martin)",
    "David": "David (in honor of Frasier Crane's esteemed psychiatrist colleague David)",
    "Niles": "Niles (in honor of Frasier Crane's pretentious younger brother Dr. Niles)",
    "Dan Fielding": "Assistant District Attorney Dan Fielding (the narcissistic womanizer)",
    "Bull Shannon": "Bailiff Nostradamus 'Bull' Shannon (the towering, gentle giant bailiff)",
    "Mac Robinson": "Court Clerk Mac Robinson (the pragmatic, sensible Vietnam veteran court administrator)",
}

def get_candidates_for_show(show, all_qs, target_fixes):
    qs = []
    for idx, q in enumerate(all_qs):
        if q["show"] == show:
            lens = [len(o) for o in q["options"]]
            if lens[q["answer"]] == max(lens):
                qs.append((idx, q))
    def sort_key(item):
        idx, q = item
        c = q["answer"]
        corr_len = len(q["options"][c])
        max_false_len = max(len(o) for i, o in enumerate(q["options"]) if i != c)
        return (corr_len - max_false_len, corr_len)
    return sorted(qs, key=sort_key)[:target_fixes]

def elongate_option(best_f, show, q_text, corr):
    corr_len = len(corr)

    # 1. Exact custom map
    if best_f in CUSTOM_MAP:
        cand = CUSTOM_MAP[best_f]
        if len(cand) > corr_len:
            return cand

    # 2. NAME_DICT
    if best_f in NAME_DICT:
        cand = NAME_DICT[best_f]
        if len(cand) > corr_len:
            return cand

    # 3. Four digit year
    if re.match(r'^(19\d\d|20\d\d)$', best_f):
        cand = f"Autumn of {best_f} broadcast television season"
        if len(cand) > corr_len:
            return cand
        cand = f"The historical {best_f} / {int(best_f)+1} regular broadcast season"
        return cand

    # 4. Specific common strings
    if best_f == "Studio 8G": return "Studio 8G at 30 Rockefeller Plaza"
    if best_f == "Studio 6B": return "Studio 6B at 30 Rockefeller Plaza"
    if best_f == "Fox": return "Fox Broadcasting Company (FOX)"
    if best_f == "ABC": return "American Broadcasting Company (ABC)"
    if best_f == "CBS": return "CBS Television Network (CBS)"
    if best_f == "NBC": return "National Broadcasting Company (NBC)"
    if best_f == "Illinois": return "The Midwestern State of Illinois"
    if best_f == "Ireland": return "The Republic of Ireland (County Dublin)"
    if best_f == "Scotland": return "Scotland (part of the United Kingdom)"
    if best_f == "Wales": return "The historic country of Wales (UK)"
    if best_f == "KROQ 106.7": return "KROQ 106.7 FM Los Angeles Alternative Rock"
    if best_f == "Commitment": return "Total Emotional and Creative Commitment"
    if best_f == "Lin-Manuel Miranda": return "Lin-Manuel Miranda (Hamilton / In the Heights creator)"
    if best_f == "Brenda": return "Brenda the Eccentric Suburban Neighbor"
    if best_f == "McDonald's": return "McDonald's fast-food restaurant chain"
    if best_f == "Mr. Peepers": return "Mr. Peepers the Apple-Eating Monkey Man"
    if best_f == "Jean-Claude Van Damme": return "Jean-Claude Van Damme (Bloodsport / martial arts star)"
    if best_f == "Daniel Day-Lewis": return "Sir Daniel Day-Lewis (three-time Academy Award winner)"
    if best_f == "Chance the Rapper": return "Chance the Rapper (Grammy-winning musician and SNL host)"
    if best_f == "Game of Thrones": return "Game of Thrones (acclaimed HBO fantasy series)"
    if best_f == "Jackie Joyner-Kersee": return "Jackie Joyner-Kersee (Olympic gold medal track star)"
    if best_f == "Ninety minutes": return "Exactly ninety minutes of uninterrupted broadcast television"
    if best_f == "Around 750": return "Around 750 full-length live broadcast episodes"
    if best_f == "17 years old": return "Only 17 years old at the time of hiring"
    if best_f == "18 years old": return "Only 18 years old at the time of auditioning"
    if best_f == "19 years old": return "Only 19 years old when first cast"
    if best_f == "Around 500 sketches": return "Around 500 individual live comedy sketches performed"
    if best_f == "Between 10 and 15 sketches": return "Between 10 and 15 full live sketches per broadcast"
    if best_f == "Thursday afternoon": return "Thursday afternoon during rehearsal and blocking"
    if best_f == "Alfalfa": return "Alfalfa (iconic character from The Little Rascals)"
    if best_f == "Rhythmic gymnastics": return "Competitive Olympic rhythmic ribbon gymnastics"
    if best_f == "Plantain chips": return "Crispy seasoned salted garlic plantain chips"
    if best_f == "Eli the Yeshiva Student": return "Eli the Yeshiva Student (recurring character sketch)"
    if best_f == "Devin": return "Devin (from The Californians soap opera sketch)"
    if best_f == "Terry": return "Terry the Sarcastic Corporate Colleague"
    if best_f == "Fritz": return "Fritz the Eccentric Avant-Garde European Cousin"
    if best_f == "Season 11 (1985-1986)": return "Season 11 (1985-1986) featuring the revamped celebrity cast"
    if best_f == "No way, Jose!": return "No way, Jose! (and don't you ever dare ask again!)"
    if best_f == "www.secretstandup.com": return "www.secretundergroundstandupcomedy.com"

    # URL
    if best_f.startswith("www.") or best_f.startswith("http"):
        return f"{best_f[:-4]}officialcomedywebsite.com"

    # Quotes
    if best_f.startswith('"') and best_f.endswith('"'):
        inner = best_f[1:-1]
        cand = f'"{inner} (and don\'t you ever forget it!)"'
        if len(cand) > corr_len: return cand
        return f'"{inner} (and absolutely nothing else under any circumstances!)"'

    # Video title or book title
    if any(k in q_text.lower() for k in ["title", "called", "named", "release"]):
        cand = f"{best_f}: An Unfiltered Story"
        if len(cand) > corr_len: return cand
        return f"{best_f} and Other Disaster Tales"

    # Punchline / clause with verb
    if any(verb in best_f for verb in [" is ", " are ", " was ", " were ", " call ", " think ", " get ", " take ", " spent ", " spend ", " had ", " have ", " worked ", " lived ", " became ", " made ", " did ", " could "]):
        cand = f"{best_f} on a regular basis"
        if len(cand) > corr_len: return cand
        return f"{best_f} in front of an entire live audience"

    # Noun phrase starting with article
    if best_f.startswith("A ") or best_f.startswith("An ") or best_f.startswith("The "):
        prefix, rest = best_f.split(" ", 1)
        cand = f"{prefix} widely discussed and memorable {rest}"
        if len(cand) > corr_len: return cand
        return f"{prefix} completely separate, widely recognized, and distinct {rest}"

    # Names (2-3 words)
    words = best_f.strip().split()
    if 2 <= len(words) <= 4 and all(w.replace(".", "").replace("'", "").isalpha() and w[0].isupper() for w in words):
        role_map = {
            "Stand-Up Comedy": "(touring stand-up headliner and comedy club veteran)",
            "Late Night TV": "(frequent late-night talk show guest and comedy performer)",
            "Taskmaster UK": "(celebrated British television comedian and panel show star)",
            "Comedy Bang! Bang!": "(frequent podcast improviser, character actor, and comedy guest)",
            "How Did This Get Made?": "(recurring podcast comedy guest, actor, and bad-movie enthusiast)",
            "Why Won't You Date Me?": "(hilarious touring guest comedian, actor, and close personal friend)",
            "Don't Tell Comedy": "(featured headlining stand-up comic and secret set performer)",
            "SNL": "(frequent guest host, musical guest, and comedy sketch performer)",
            "80s TV Shows": "(regular prime-time television series ensemble cast member)",
        }
        cand = f"{best_f} {role_map.get(show, '(touring guest comedy performer and veteran)')}"
        if len(cand) > corr_len:
            return cand
        return f"{best_f} (celebrated entertainment industry professional and guest)"

    # Fallback clean descriptor
    cand = f"{best_f} (in its classic original format)"
    if len(cand) > corr_len: return cand
    return f"{best_f} (as featured in the standard broadcast edition)"

def balance_group2():
    print(f"Reading input from: {GROUP2_IN}")
    orig = json.load(open(GROUP2_IN))

    TARGET_FIXES = {
        "Stand-Up Comedy": 24,
        "Late Night TV": 50,
        "How Did This Get Made?": 70,
        "Comedy Bang! Bang!": 74,
        "Taskmaster UK": 92,
        "Don't Tell Comedy": 111,
        "Why Won't You Date Me?": 132,
        "SNL": 219,
        "80s TV Shows": 257,
    }

    # Deep copy
    balanced = json.loads(json.dumps(orig))

    total_modified = 0
    errors = []

    for show, target_fixes in TARGET_FIXES.items():
        candidates = get_candidates_for_show(show, orig, target_fixes)
        print(f"Processing show: {show:25s} | Target fixes: {target_fixes:3d} (out of {len(candidates)} selected)")

        for idx, q_orig in candidates:
            c = q_orig["answer"]
            corr = q_orig["options"][c]
            corr_len = len(corr)

            # Pick the false option that is currently the longest false option
            # (or tied with longest)
            max_f_len = max(len(o) for i, o in enumerate(q_orig["options"]) if i != c)
            best_f_indices = [i for i, o in enumerate(q_orig["options"]) if i != c and len(o) == max_f_len]
            f_idx = best_f_indices[0]
            best_f = q_orig["options"][f_idx]

            # Elongate
            elongated = elongate_option(best_f, show, q_orig["q"], corr)

            # Verify it is strictly longer than all other options
            current_opts = list(balanced[idx]["options"])
            current_opts[f_idx] = elongated

            lens = [len(o) for o in current_opts]
            if lens[c] == max(lens):
                errors.append(f"Q{idx} ({show}): Elongation failed to make false option strictly longest! Corr ({corr_len}): '{corr}' vs Elongated ({len(elongated)}): '{elongated}'")

            if len(set(current_opts)) != 4:
                errors.append(f"Q{idx} ({show}): Options not unique after elongation: {current_opts}")

            balanced[idx]["options"] = current_opts
            total_modified += 1

    if errors:
        print(f"\nBalancing encountered {len(errors)} error(s):")
        for err in errors[:10]:
            print(" ", err)
        return False

    print(f"\nSuccessfully modified {total_modified} questions across {len(TARGET_FIXES)} shows.")
    print(f"Writing balanced data to: {GROUP2_OUT}")
    with open(GROUP2_OUT, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)

    return True

if __name__ == "__main__":
    ok = balance_group2()
    sys.exit(0 if ok else 1)
