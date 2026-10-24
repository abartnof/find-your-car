import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from utils import assemble_batch, save_json

raw_questions = [
    # --- SEASON 8 (1-50) ---
    {
        "q": "In 'The Foundation', what board is George reluctantly appointed to honor his deceased fiancé?",
        "correct": "The Susan Ross Foundation board of directors",
        "wrong": ["The Manhattan Children's Memorial Trust committee", "The New York Philharmonic endowment review panel", "The Upper West Side Historical Preservation council"],
        "d": 2
    },
    {
        "q": "What martial arts class does Kramer proudly boast about dominating in 'The Foundation'?",
        "correct": "A children's beginner karate class",
        "wrong": ["A senior citizen's judo self-defense program", "An advanced adult Brazilian jiu-jitsu academy", "A teenage Olympic taekwondo training session"],
        "d": 1
    },
    {
        "q": "In 'The Soul Mate', who falls madly in love with Jerry's girlfriend Pam?",
        "correct": "Newman",
        "wrong": ["David Puddy", "Kenny Bania", "Mickey Abbott"],
        "d": 2
    },
    {
        "q": "In 'The Bizarro Jerry', what are the names of the three courteous, intellectual counterparts to Jerry, George, and Kramer?",
        "correct": "Kevin, Gene, and Feldman",
        "wrong": ["Kenneth, Glenn, and Franklin", "Keith, Gordon, and Forrest", "Kyle, Gregory, and Fletcher"],
        "d": 1
    },
    {
        "q": "What striking physical trait does Jerry's date Gillian have in 'The Bizarro Jerry'?",
        "correct": "\"Man-hands\" (enormous, powerful hands)",
        "wrong": ["A deep, booming baritone speaking voice", "A towering six-foot-six athletic stature", "Uncontrollable twitching whenever nervous"],
        "d": 1
    },
    {
        "q": "In 'The Little Kicks', how is Elaine's dancing at the J. Peterman staff party described?",
        "correct": "A full-body dry heave with frantic thumbs and little kicks",
        "wrong": ["An erratic robotic jerk with flailing elbows and jumps", "A wild flamenco stomp with exaggerated hip swings and hand clapping", "An uncoordinated tap dance with awkward hand gestures"],
        "d": 1
    },
    {
        "q": "What nickname does George earn at the staff party in 'The Little Kicks' after getting emotional?",
        "correct": "\"Cryin' George\"",
        "wrong": ["\"Weepin' Costanza\"", "\"Tearful George\"", "\"Sobbin' Costanza\""],
        "d": 3
    },
    {
        "q": "In 'The Package', what provocative pose does George strike in his boudoir photo shoot?",
        "correct": "Lounging on a velvet chaise lounge in his underwear",
        "wrong": ["Posing shirtless while wearing an unbuttoned black leather motorcycle vest", "Leaning against a marble fireplace holding a rose", "Sitting wrapped in a silk bathrobe smoking a cigar"],
        "d": 2
    },
    {
        "q": "In 'The Fatigues', what traumatic event caused Frank Costanza's cooking PTSD during the Korean War?",
        "correct": "Accidentally poisoning his entire military platoon with spoiled meat",
        "wrong": ["A heavy mortar shell completely destroying his field mess tent during dinner", "Running out of rations during a brutal two-week mountain siege", "Being captured by enemy scouts while foraging for wild mushrooms"],
        "d": 1
    },
    {
        "q": "In 'The Checks', what song by The Eagles causes Elaine's boyfriend Brett to enter a trance-like state?",
        "correct": "\"Desperado\"",
        "wrong": ["\"Hotel California\"", "\"Tequila Sunrise\"", "\"Peaceful Easy Feeling\""],
        "d": 2
    },
    {
        "q": "How much are the royalty checks Jerry receives from a Japanese television broadcast in 'The Checks'?",
        "correct": "Twelve cents each",
        "wrong": ["Fifty cents each check", "Two dollars each", "Five cents each"],
        "d": 3
    },
    {
        "q": "In 'The Chicken Roaster', what fast-food franchise opens across from Kramer's apartment, shining an intense red neon light?",
        "correct": "Kenny Rogers Roasters",
        "wrong": ["Boston Market", "Roy Rogers Restaurants", "Popeyes Famous Fried Chicken"],
        "d": 1
    },
    {
        "q": "What happens to Jerry and Kramer after they swap apartments to escape the red neon light in 'The Chicken Roaster'?",
        "correct": "They gradually adopt each other's distinct personalities and habits",
        "wrong": ["They get into a massive physical feud over apartment maintenance", "Jerry's comedy career thrives while Kramer becomes a recluse", "Kramer's apartment catches fire from an unattended electric hot plate appliance"],
        "d": 1
    },
    {
        "q": "What vegetable does Newman famously spit out in disgust when Jerry tests him in 'The Chicken Roaster'?",
        "correct": "Broccoli (\"Vile weed!\")",
        "wrong": ["Asparagus (\"Repulsive stalks!\")", "Brussels sprouts (\"Poison cabbage!\")", "Cauliflower (\"Disgusting fungus!\")"],
        "d": 1
    },
    {
        "q": "In 'The Abstinence', what extraordinary mental transformation happens to George when he stops having sex?",
        "correct": "He becomes an absolute intellectual genius with vast knowledge",
        "wrong": ["He develops photographic memory and masters five foreign languages simultaneously", "He predicts stock market fluctuations with pinpoint accuracy", "He composes an entire classical symphony in forty-eight hours"],
        "d": 1
    },
    {
        "q": "Which New York Yankees baseball star does a genius George teach physics and hitting mechanics to in 'The Abstinence'?",
        "correct": "Derek Jeter and Bernie Williams",
        "wrong": ["Paul O'Neill and Tino Martinez", "Don Mattingly and Wade Boggs", "Mariano Rivera and Andy Pettitte"],
        "d": 3
    },
    {
        "q": "In 'The Andrea Doria', what tragic historical event does George use to compete for a tenant co-op apartment?",
        "correct": "Recounting the pathetic, misery-filled failures of his entire life",
        "wrong": ["Claiming his ancestors perished aboard the Titanic in 1912", "Faking a severe disability suffered during a volunteer rescue effort", "Pretending he survived the catastrophic sinking of the Andrea Doria"],
        "d": 1
    },
    {
        "q": "Who is George's apartment rival who actually survived the 1956 Andrea Doria shipwreck?",
        "correct": "Alan Grayson",
        "wrong": ["Arthur Blank", "Harold Lieberman", "Martin van Nostrand"],
        "d": 3
    },
    {
        "q": "In 'The Little Jerry', what kind of animal is 'Little Jerry Seinfeld', purchased by Kramer at an auction?",
        "correct": "A champion fighting rooster",
        "wrong": ["A miniature show greyhound", "A prize-winning racing pigeon", "A pedigree French bulldog puppy"],
        "d": 1
    },
    {
        "q": "Why does Marcelino, the bodega owner, force Little Jerry into illegal cockfights?",
        "correct": "To settle a bounced check Jerry wrote at his store",
        "wrong": ["To pay off Kramer's delinquent bodega grocery tab", "To win exclusive distribution rights to Cuban cigars", "To win ownership of a classic vintage automobile"],
        "d": 3
    },
    {
        "q": "In 'The Comeback', what zinger does George spend days agonizing over after coworker Reilly mocks him for eating shrimp?",
        "correct": "\"The jerk store called, and they're running out of you!\"",
        "wrong": ["\"Your face called, and it wants its ugly features returned!\"", "\"The village idiot society called, and they need a president!\"", "\"The cheap suit warehouse called, and they want their polyester!\""],
        "d": 1
    },
    {
        "q": "Where does George fly at his own expense just to deliver his 'jerk store' comeback line to Reilly?",
        "correct": "Akron, Ohio (to a corporate board meeting)",
        "wrong": ["Cleveland, Ohio (to a sports executive convention)", "Chicago, Illinois (to an architectural seminar)", "Detroit, Michigan (to an industrial manufacturing summit)"],
        "d": 1
    },
    {
        "q": "What crushing counter-comeback does Reilly deliver to George after George says his 'jerk store' line?",
        "correct": "\"What's the difference? You're their all-time best seller!\"",
        "wrong": ["\"Did it take you three whole days on an airplane to think of that?!\"", "\"Nobody in this room has ever heard a more pathetic comeback!\"", "\"Why don't you fly back to Queens where you belong!\""],
        "d": 2
    },
    {
        "q": "In 'The Van Buren Boys', what hand sign protects George from being mugged by the street gang?",
        "correct": "Holding up eight fingers (Martin Van Buren was the 8th president)",
        "wrong": ["Flashing a peace sign followed by a clenched fist", "Tapping both temples with index fingers simultaneously", "Crossing both forearms into an aggressive defensive Roman numeral 'X'"],
        "d": 1
    },
    {
        "q": "In 'The Susie', what fictional coworker does Elaine invent to avoid taking responsibility at J. Peterman?",
        "correct": "Susie",
        "wrong": ["Samantha", "Stephanie", "Sharon"],
        "d": 1
    },
    {
        "q": "What happens when J. Peterman insists on holding a formal memorial service for the fictional Susie?",
        "correct": "Elaine is forced to deliver a heartfelt eulogy for her fictional alter ego",
        "wrong": ["George pretends to be Susie's grieving widower from New Jersey", "Kramer accidentally reveals that Susie never existed to the staff", "Peterman names an entire safari outerwear collection after the departed Susie"],
        "d": 2
    },
    {
        "q": "In 'The Pothole', what section of highway does Kramer adopt and maintain with his own tools?",
        "correct": "Mile 114 of the Arthur Burkhardt Expressway",
        "wrong": ["Mile 42 of the congested Long Island Expressway", "Mile 88 of the Grand Central Parkway", "Mile 15 of the Henry Hudson Parkway"],
        "d": 3
    },
    {
        "q": "What radical redesign does Kramer implement on the adopted expressway in 'The Pothole'?",
        "correct": "Repainting four lanes into two extra-wide luxury comfort lanes",
        "wrong": ["Planting rows of exotic decorative palm trees along the median strip", "Installing wooden toll booths charging fifty cents per vehicle", "Setting up roadside espresso stands at every emergency pull-off"],
        "d": 2
    },
    {
        "q": "In 'The English Patient', what award-winning movie does Elaine absolutely despise while everyone else loves it?",
        "correct": "The English Patient",
        "wrong": ["Dances with Wolves (Extended Director's Cut)", "Schindler's List", "Braveheart"],
        "d": 1
    },
    {
        "q": "What does Elaine scream inside a crowded movie theater during 'The English Patient'?",
        "correct": "\"Quit telling your stupid story about the stupid desert and just die already!\"",
        "wrong": ["\"This is the most painfully boring romantic melodrama ever filmed!\"", "\"Somebody please turn the projector off and end this absolute misery!\"", "\"I cannot endure another second of this pretentious drivel!\""],
        "d": 2
    },
    {
        "q": "In 'The Nap', what secret renovation does George have built under his desk at Yankee Stadium?",
        "correct": "A custom enclosed sleeping compartment with shelves and alarm",
        "wrong": ["A concealed mini-refrigerator stocked with pastrami and beer", "A hidden flat-screen television connected to cable sports", "A subterranean secret trapdoor leading directly out to the visitor's dugout"],
        "d": 1
    },
    {
        "q": "What does George Steinbrenner assume when he hears ticking coming from under George's desk in 'The Nap'?",
        "correct": "He believes there is a live terrorist bomb under the desk",
        "wrong": ["He thinks George has installed an illegal sports ticker wire", "He assumes George is building a high-tech espionage bugging system", "He believes George has a defective mechanical pacemaker"],
        "d": 2
    },
    {
        "q": "In 'The Yada Yada', what catchphrase does George's girlfriend Marcy repeatedly use to gloss over key details?",
        "correct": "\"Yada yada yada\"",
        "wrong": ["\"Et cetera, et cetera\"", "\"And so on and so forth\"", "\"Blah blah blah\""],
        "d": 1
    },
    {
        "q": "What critical life detail does Marcy skip using 'yada yada yada' that shocks George?",
        "correct": "Her ex-boyfriend visiting and sleeping with her",
        "wrong": ["Her secret past marriage and three children in New Jersey", "Her criminal conviction for grand larceny embezzlement", "Her resignation from her corporate vice president position"],
        "d": 2
    },
    {
        "q": "In 'The Yada Yada', why does dentist Tim Whatley convert to Judaism, according to an infuriated Jerry?",
        "correct": "Purely for the jokes, allowing him to make Jewish jokes freely",
        "wrong": ["To qualify for an exclusive dental society medical grant", "To marry a wealthy Manhattan socialite heiress", "To win over an influential dental equipment supplier with business connections"],
        "d": 1
    },
    {
        "q": "What label does Jerry earn when he complains about Tim Whatley's conversion to Father Curtis?",
        "correct": "An \"anti-dentite\"",
        "wrong": ["A \"dental bigot\"", "A \"hygiene skeptic\"", "A \"tooth persecutor\""],
        "d": 2
    },
    {
        "q": "In 'The Millennium', what year does Newman book the Rainbow Room for his millennium party?",
        "correct": "The year 2001 (the actual mathematical start of the millennium)",
        "wrong": ["The year 2000 (New Year's Eve 1999)", "The year 1999 (New Year's Eve 1998)", "The year 2002 (to avoid peak Manhattan holiday reservation surcharges)"],
        "d": 3
    },
    {
        "q": "In 'The Muffin Tops', what is the culinary premise of the bakery Elaine and Mr. Lippman open?",
        "correct": "Selling exclusively the tops of muffins and discarding the stumps",
        "wrong": ["Baking oversized savory muffins stuffed with artisanal imported European cheeses", "Serving gluten-free muffins paired with imported teas", "Offering twenty varieties of organic whole grain breakfast loaves"],
        "d": 1
    },
    {
        "q": "What is the slogan of Elaine and Lippman's muffin bakery in 'The Muffin Tops'?",
        "correct": "\"Top of the Muffin to You!\"",
        "wrong": ["\"Just the Tops, Never the Bottom!\"", "\"Muffin Tops and Nothing Else!\"", "\"The Crown of the Muffin!\""],
        "d": 2
    },
    {
        "q": "Who aggressively refuses to accept the discarded muffin stumps at the local homeless shelter?",
        "correct": "Rebecca DeMornay",
        "wrong": ["Mabel Choate", "Manhattan socialite Mrs. Ross", "Estelle Costanza"],
        "d": 3
    },
    {
        "q": "What memorable complaint does Rebecca DeMornay shout about the muffin stumps?",
        "correct": "\"They're just stumps! Why don't you drop off some chicken skins and lobster shells?!\"",
        "wrong": ["\"We are a community shelter, not a commercial compost dumping ground!\"", "\"If you won't eat the bottom of the muffin, don't dump it on the poor!\"", "\"We need real nutritional meals, not discarded pastry trash from the rich!\""],
        "d": 2
    },
    {
        "q": "In 'The Summer of George', what financial windfall allows George to plan an entire summer of relaxation?",
        "correct": "A massive three-month severance package from the New York Yankees",
        "wrong": ["A substantial inheritance from a distant great-uncle in Florida", "A lucrative court settlement from a slip-and-fall accident at a Manhattan bank", "Winning twenty-five thousand dollars on an off-track horse wager"],
        "d": 1
    },
    {
        "q": "What physical accident brings 'The Summer of George' to an abrupt, tragic halt?",
        "correct": "Tripping over his own discarded clothes and tumbling down the stairs",
        "wrong": ["Getting struck by a speeding bicycle messenger in Central Park", "Falling straight through a rotten wooden floorboard on his parents' front porch", "Dislocating his shoulder while playing recreational frisbee"],
        "d": 2
    },
    {
        "q": "In 'The Soul Mate', what medical procedure does Kramer undergo to please his new romantic interest?",
        "correct": "A vasectomy reversal procedure",
        "wrong": ["Laser eye corrective surgery", "A holistic spine realignment therapy", "A sinus reduction surgery"],
        "d": 3
    },
    {
        "q": "In 'The Fatigues', who does Bania hire as his professional comedy mentor?",
        "correct": "Kenny Bania hires Jerry, who passes him to George",
        "wrong": ["Kenny Bania hires Jerry's stand-up rival Pat Buckles", "Kenny Bania pays George Costanza five hundred dollars for joke punchlines", "Kenny Bania enrolls in an intensive improv conservatory in Chicago"],
        "d": 3
    },
    {
        "q": "In 'The Package', what illegal action does Kramer attempt at the post office with a package?",
        "correct": "Insuring an empty box and then claiming it was damaged in transit",
        "wrong": ["Mailing a live poisonous desert tarantula to Newman's boss", "Shipping counterfeit luxury watches overseas through diplomatic mail", "Stealing official pre-stamped priority parcels from behind the counter"],
        "d": 3
    },
    {
        "q": "In 'The Little Jerry', what bodega item does Jerry pay for with a check that bounces, humiliating him?",
        "correct": "A carton of milk and a pastry snack",
        "wrong": ["A six-pack of imported mineral water and magazines", "A jar of gourmet roasted peanuts and laundry detergent", "A container of orange juice and a morning newspaper"],
        "d": 3
    },
    {
        "q": "In 'The Checks', why does Jerry suffer severe wrist cramps that prevent him from performing?",
        "correct": "Endorsing hundreds of twelve-cent royalty checks by hand",
        "wrong": ["Signing thousands of promotional headshot photographs for an agency", "Playing four consecutive games of competitive racquetball with George", "Carrying Morty Seinfeld's heavy executive sample cases across town"],
        "d": 3
    },
    {
        "q": "In 'The Millennium', what ranking does Jerry's girlfriend assign him on her phone speed dial, causing drama?",
        "correct": "Speed dial position number 7",
        "wrong": ["Speed dial position number 3 on the phone keypad", "Speed dial position number 9", "Speed dial position number 5"],
        "d": 3
    },
    {
        "q": "In 'The Pothole', what prized possession of Jerry's girlfriend Jenna falls into the toilet bowl?",
        "correct": "Her toothbrush, which Jerry secretly fails to discard",
        "wrong": ["Her vintage diamond engagement ring from a past fiancé", "Her designer prescription horn-rimmed eyeglasses", "Her gold heirloom locket necklace containing family portraits"],
        "d": 2
    },

    # --- SEASON 9 & THE FINALE (51-100) ---
    {
        "q": "In 'The Butter Shave', what household condiment does Kramer use as a luxurious shaving cream alternative?",
        "correct": "Pure dairy butter",
        "wrong": ["Extra virgin olive oil", "Whipped marshmallow cream", "Pure organic mayonnaise"],
        "d": 1
    },
    {
        "q": "What happens to Kramer when he falls asleep while sunbathing on the apartment roof coated in butter?",
        "correct": "He literally bakes in the sun and Newman smells cooked poultry",
        "wrong": ["A flock of aggressive urban park pigeons pecks at his buttered face and arms", "His skin breaks out in an acute allergic dermatological rash", "He gets locked out on the rooftop in ninety-degree summer heat"],
        "d": 1
    },
    {
        "q": "In 'The Voice', what sound effect does Jerry invent to mock his girlfriend Claire's belly button?",
        "correct": "\"Helloooo! La la la!\"",
        "wrong": ["\"Heyyyy there! Ha ha ha!\"", "\"Good morning! Cha cha cha!\"", "\"Look at me! Tra la la!\""],
        "d": 1
    },
    {
        "q": "Who is Kramer's dedicated college intern at Kramerica Industries in 'The Voice'?",
        "correct": "Darren from NYU",
        "wrong": ["Todd from Columbia", "Bradley from Fordham", "Arthur from Cornell"],
        "d": 1
    },
    {
        "q": "What revolutionary maritime safety invention does Kramerica Industries test by dropping from a window?",
        "correct": "A giant oil tanker bladder filled with synthetic motor oil",
        "wrong": ["A self-inflating multi-passenger high-seas life raft", "A puncture-proof buoyant neoprene hull lining safety blanket for cargo vessels", "A pressurized chemical fire suppressant foam sphere"],
        "d": 2
    },
    {
        "q": "What happens when the Kramerica oil bladder is dropped out of a high-story window in 'The Voice'?",
        "correct": "It lands directly on Jerry's girlfriend Claire, completely covering her in oil",
        "wrong": ["It explodes across five parked luxury vehicles on West 81st Street", "It crushes an expensive antique street vendor pretzel cart to splinters", "It bounces fifty feet into the air and crashes through a luxury boutique storefront window"],
        "d": 2
    },
    {
        "q": "In 'The Serenity Now', what mantra does Frank Costanza scream at the top of his lungs to lower his blood pressure?",
        "correct": "\"Serenity now!\"",
        "wrong": ["\"Tranquility now!\"", "\"Peace of mind now!\"", "\"Calmness now!\""],
        "d": 1
    },
    {
        "q": "What warning does Lloyd Braun give to George about Frank's 'Serenity now' relaxation method?",
        "correct": "\"Serenity now, insanity later!\"",
        "wrong": ["\"Repression today brings destruction tomorrow!\"", "\"You cannot scream your way to emotional tranquility!\"", "\"Anger bottled up will shatter your entire psyche!\""],
        "d": 2
    },
    {
        "q": "What merchandise are George and Lloyd Braun competing to sell over the phone from Frank's garage?",
        "correct": "Outdated personal desktop computers",
        "wrong": ["Industrial grade water filtration systems", "Subscription sets of encyclopedia volumes", "Discounted commercial cellular telephone units"],
        "d": 2
    },
    {
        "q": "In 'The Blood', what bodily fluid does Jerry receive from Kramer during an emergency hospital procedure?",
        "correct": "Three pints of Kramer's personal blood",
        "wrong": ["A bone marrow transplant donation", "A plasma transfusion enriched with vitamins", "An experimental blood serum developed abroad"],
        "d": 2
    },
    {
        "q": "In 'The Junk Mail', what drastic action does Kramer take against the United States Postal Service?",
        "correct": "Demanding that the postal service permanently cancel all of his mail",
        "wrong": ["Dumping thousands of promotional flyers into a street sewer drain", "Supergluing his apartment mail slot shut with industrial epoxy", "Chain-locking the main entrance doors of the neighborhood post office"],
        "d": 2
    },
    {
        "q": "Which actor plays intimidating Postmaster General Henry Atkins in 'The Junk Mail'?",
        "correct": "Wilford Brimley",
        "wrong": ["R. Lee Ermey", "Veteran actor Brian Dennehy", "Ned Beatty"],
        "d": 3
    },
    {
        "q": "In 'The Merv Griffin Show', where does Kramer find the vintage talk show set that he rebuilds in his apartment?",
        "correct": "Discarded in a commercial dumpster behind a television studio",
        "wrong": ["At an eccentric prop warehouse liquidation auction in Brooklyn", "In an abandoned basement storage room of an NBC broadcast facility", "At an estate sale held at a retired television producer's estate"],
        "d": 2
    },
    {
        "q": "Who serves as Kramer's loyal sidekick and announcer on his apartment talk show set?",
        "correct": "Newman",
        "wrong": ["Mickey Abbott", "David Puddy", "Kenny Bania"],
        "d": 2
    },
    {
        "q": "What dangerous live predator does animal expert Jim Fowler bring onto Kramer's talk show?",
        "correct": "A vicious, screeching red-tailed hawk",
        "wrong": ["A six-foot South American boa constrictor", "A pair of aggressive Australian honey badgers", "A juvenile spotted leopard from an animal sanctuary"],
        "d": 3
    },
    {
        "q": "In 'The Slicer', what commercial appliance does Kramer install in his apartment kitchen?",
        "correct": "A heavy-duty commercial deli meat slicer",
        "wrong": ["An industrial rotary cheese grating machine", "A high-capacity commercial soft-serve ice cream freezer", "A restaurant-grade stainless steel deep fat fryer"],
        "d": 2
    },
    {
        "q": "What industrial company does George get hired by in 'The Slicer', run by an incompetent, careless boss?",
        "correct": "Kruger Industrial Smoothing",
        "wrong": ["Pendant Engineering Logistics", "Sanfilippo Surface Finishing", "Vandelay Industrial Polishing"],
        "d": 2
    },
    {
        "q": "What is the relaxed catchphrase of company president Mr. Kruger at Kruger Industrial Smoothing?",
        "correct": "\"K-UGER!\"",
        "wrong": ["\"Smooth sailing!\"", "\"No worries at all!\"", "\"Take it easy!\""],
        "d": 3
    },
    {
        "q": "In 'The Betrayal', which takes place in reverse chronological order, where does the gang travel for a wedding?",
        "correct": "India (for Sue Ellen Mischke's wedding)",
        "wrong": ["Italy (for Bob Cobb's destination villa wedding)", "Greece (for an international publisher's reception)", "Mexico (for a high-society fashion boutique event)"],
        "d": 2
    },
    {
        "q": "What is the name of Sue Ellen Mischke's groom in 'The Betrayal'?",
        "correct": "Preeyan",
        "wrong": ["Architect Rajesh", "Vikram", "Sanjay"],
        "d": 3
    },
    {
        "q": "In 'The Apology', which actor guest stars as recovering alcoholic Jason Hanke, who refuses to apologize to George?",
        "correct": "James Spader",
        "wrong": ["Bryan Cranston", "William H. Macy", "Robert Downey Jr."],
        "d": 2
    },
    {
        "q": "What past incident does George insist Jason Hanke must formally apologize for under Step 9 of AA?",
        "correct": "Refusing to lend George an oversized cashmere sweater at a party",
        "wrong": ["Mocking George's early hair loss in front of their high school peers", "Spilling red punch down the front of George's favorite tailored dress shirt", "Taking credit for an architectural joke George whispered to him at dinner"],
        "d": 3
    },
    {
        "q": "In 'The Strike', what holiday did Frank Costanza invent as an alternative to the commercialism of Christmas?",
        "correct": "Festivus (\"A Festivus for the rest of us!\")",
        "wrong": ["Costanzamas (\"The True Winter Holiday\")", "Antimas (\"Peace Without Commercial Products\")", "Franktivus (\"The Celebration of Real Strength\")"],
        "d": 1
    },
    {
        "q": "What unadorned symbol is displayed in the living room during the celebration of Festivus?",
        "correct": "A plain, unadorned aluminum pole",
        "wrong": ["A decorated wooden coat rack with brass hooks", "A stainless steel kitchen utensil hanging rack", "A bare evergreen pine branch in a ceramic jar"],
        "d": 1
    },
    {
        "q": "What are the two core participatory traditions of the Festivus celebration dinner?",
        "correct": "The Airing of Grievances and the Feats of Strength",
        "wrong": ["The Sharing of Regrets and the Arm Wrestling Tournament", "The Listing of Insults and the Living Room Tug-of-War", "The Confession of Blunders and the Midnight Footrace"],
        "d": 1
    },
    {
        "q": "What fake charity does George invent to avoid spending money on Christmas gifts for coworkers?",
        "correct": "\"The Human Fund\" (\"Money for People\")",
        "wrong": ["\"The Costanza Benevolent Trust\"", "\"The Manhattan Society for Needy Families\"", "\"The Greater Urban Welfare Foundation\""],
        "d": 3
    },
    {
        "q": "In 'The Dealership', what chocolate candy bar gets stuck in the vending machine, driving George insane with hunger?",
        "correct": "A Twix candy bar",
        "wrong": ["A Snickers candy bar", "A Kit Kat wafer bar", "A 100 Grand caramel bar"],
        "d": 2
    },
    {
        "q": "What candy slogan does George passionately argue proves Twix is unique in 'The Dealership'?",
        "correct": "\"Twix is the only candy with the cookie crunch!\"",
        "wrong": ["\"Twix delivers double the caramel satisfaction!\"", "\"Twix gives you two bars of pure perfection!\"", "\"Twix satisfies your chocolate hunger every time!\""],
        "d": 3
    },
    {
        "q": "What celebratory gesture does car salesman David Puddy obsessively perform in 'The Dealership'?",
        "correct": "Aggressive, enthusiastic high-fives",
        "wrong": ["Loud rhythmic knuckles fist-bumps", "Enthusiastic two-handed shoulder claps", "Snapping his fingers followed by finger-guns"],
        "d": 2
    },
    {
        "q": "In 'The Reverse Peephole', why does Kramer install his apartment door peephole backwards?",
        "correct": "To see if anyone is waiting inside his apartment before entering",
        "wrong": ["To allow hallway neighbors to check on his health easily", "Because building management installed the optical hardware in reverse", "To prevent light from escaping into the communal hallway at night"],
        "d": 2
    },
    {
        "q": "What distinctive jacket does David Puddy wear that Elaine finds utterly mortifying in 'The Reverse Peephole'?",
        "correct": "A leather 8-ball jacket and a full-length fur coat",
        "wrong": ["A bright neon yellow NASCAR racing windbreaker", "A studded punk rock biker leather vest with chains", "A silver metallic astronaut bomber flight jacket with authentic patches"],
        "d": 3
    },
    {
        "q": "In 'The Cartoon', what publication prints a cartoon that Elaine finds completely incomprehensible?",
        "correct": "The New Yorker magazine",
        "wrong": ["The Atlantic Monthly", "The New York Times Magazine", "Esquire Magazine"],
        "d": 2
    },
    {
        "q": "What animals are depicted in The New Yorker cartoon that baffles Elaine in 'The Cartoon'?",
        "correct": "A pig standing at a complaint department desk",
        "wrong": ["Two dogs drinking martinis at a cocktail lounge", "A cat wearing spectacles operating a typewriter", "An elephant sitting in an executive swivel chair"],
        "d": 3
    },
    {
        "q": "Which comedian guest stars as Sally Weaver, who builds an entire stand-up routine mocking Jerry in 'The Cartoon'?",
        "correct": "Kathy Griffin",
        "wrong": ["Sandra Bernhard", "Janeane Garofalo", "Judy Tenuta"],
        "d": 2
    },
    {
        "q": "In 'The Strongbox', what does Kramer hide inside the cemetery grave of Jerry's pet bird Fred?",
        "correct": "The key to his apartment strongbox safe",
        "wrong": ["A stash of five thousand dollars in unmarked currency", "A vintage cassette tape recording of Jerry's earliest stand-up", "A signed autographed baseball from Mickey Mantle"],
        "d": 3
    },
    {
        "q": "In 'The Wizard', what knockoff electronic organizer does George purchase for Morty Seinfeld instead of a PalmPilot?",
        "correct": "\"The Willard\"",
        "wrong": ["\"The PalmWizard\"", "\"The HandyMate\"", "\"The CompuOrganizer\""],
        "d": 3
    },
    {
        "q": "In 'The Burning', what musical genre does David Puddy listen to in his car that alarms Elaine?",
        "correct": "Christian rock radio stations",
        "wrong": ["Traditional Bavarian polka accordion broadcasts", "Harsh underground death metal radio stations", "Avant-garde twelve-tone electronic synthesizer noise"],
        "d": 2
    },
    {
        "q": "What meeting technique does George adopt at Kruger Industrial Smoothing to appear brilliant in 'The Burning'?",
        "correct": "Leaving the room immediately after delivering a funny or sharp remark",
        "wrong": ["Nodding thoughtfully while taking copious notes on legal pads", "Asking complex rhetorical questions before anyone at the meeting can answer", "Standing during all executive discussions to dominate the table"],
        "d": 2
    },
    {
        "q": "In 'The Bookstore', what happens to the expensive French art book after George takes it into the restroom?",
        "correct": "The bookstore flags the barcode as 'bathroom contaminated' and forces him to buy it",
        "wrong": ["He accidentally drops the book into the sink filled with soapy water", "The store security alarms sound as he attempts to exit the restroom", "An employee confiscates the art book and bans George from all Manhattan retail locations"],
        "d": 2
    },
    {
        "q": "What title does the French art book have that George gets stuck purchasing in 'The Bookstore'?",
        "correct": "French Impressionist Paintings by Brentano's",
        "wrong": ["Monet and Modern Light by Abrams Publishing", "Masterpieces of the Louvre by Thames & Hudson", "The Art of Post-Impressionism by Rizzoli"],
        "d": 3
    },
    {
        "q": "Who does Jerry catch brazenly shoplifting books at Brentano's bookstore in 'The Bookstore'?",
        "correct": "Uncle Leo",
        "wrong": ["Jack Klompus", "Newman", "Kenny Bania"],
        "d": 2
    },
    {
        "q": "In 'The Frogger', what video arcade cabinet does George buy to preserve his legendary high score?",
        "correct": "A vintage Frogger arcade machine",
        "wrong": ["A classic Pac-Man arcade cabinet", "An original Space Invaders cabinet", "A Donkey Kong arcade console"],
        "d": 2
    },
    {
        "q": "What three-letter initials mark George's unbeatable high score on the Frogger machine?",
        "correct": "\"GLC\" (George Louis Costanza)",
        "wrong": ["\"GMC\" (George Michael Costanza)", "\"GCC\" (George Christopher Costanza)", "\"GEC\" (George Edward Costanza)"],
        "d": 2
    },
    {
        "q": "What eccentric rogue electrician does Kramer hire to help George transport the Frogger machine without losing power?",
        "correct": "Slippery Pete",
        "wrong": ["Eccentric electrician Shifty Jack", "Greasy Joe", "Sparky Bob"],
        "d": 3
    },
    {
        "q": "How is the Frogger machine tragically destroyed at the conclusion of 'The Frogger'?",
        "correct": "It is crushed by a Mack truck while George navigates across 8th Avenue",
        "wrong": ["The battery backup drains five seconds before reaching the wall outlet", "Slippery Pete accidentally spills a cup of hot coffee into the main circuit board", "It tumbles down the basement staircase of Jerry's apartment building"],
        "d": 3
    },
    {
        "q": "In 'The Maid', what cool nickname does George desperately try to bestow upon himself at work?",
        "correct": "\"T-Bone\"",
        "wrong": ["\"The Hammer\"", "\"Razor\"", "\"Maverick\""],
        "d": 2
    },
    {
        "q": "What demeaning nickname does Mr. Kruger give George instead of 'T-Bone' in 'The Maid'?",
        "correct": "\"Koko\" (the gorilla)",
        "wrong": ["\"Chimp\"", "\"Peanut\"", "\"Bubbles\""],
        "d": 3
    },
    {
        "q": "In 'The Puerto Rican Day', what alias does Kramer use when viewing a luxury apartment during the traffic gridlock?",
        "correct": "H.E. Pennypacker (wealthy industrialist)",
        "wrong": ["Dr. Martin van Nostrand (noted pediatrician)", "Art Vandelay (real estate magnate)", "Kel Varnsen (international importer)"],
        "d": 2
    },
    {
        "q": "In 'The Finale', what small Massachusetts town does Jerry's private jet make an emergency landing in?",
        "correct": "Latham, Massachusetts",
        "wrong": ["Stockbridge, Massachusetts", "Pittsfield, Massachusetts", "Great Barrington, Massachusetts"],
        "d": 3
    },
    {
        "q": "What local statute are Jerry, George, Elaine, and Kramer arrested for violating in 'The Finale'?",
        "correct": "The Good Samaritan Law (failing to assist a carjacking victim)",
        "wrong": ["Reckless criminal endangerment of innocent municipal bystanders in public", "Disorderly conduct and public harassment of emergency officers", "Filing a fraudulent aviation incident report with authorities"],
        "d": 1
    }
]

if __name__ == "__main__":
    out = assemble_batch(raw_questions, 4)
    save_json(out, "tools/staging/seinfeld_batch4.json")
