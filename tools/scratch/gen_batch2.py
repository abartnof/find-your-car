import json

# 100 questions for Batch 2 (Seasons 5-7 Classic Golden Era Lore & Quotes)
# Distribution: 25 answer 0, 25 answer 1, 25 answer 2, 25 answer 3
# Difficulty: 30 d1, 40 d2, 30 d3

raw_questions = [
    # --- Group 0: Answer index 0 (25 questions) ---
    {
        "q": "In 'Cape Feare', what word tattooed on Sideshow Bob's fingers does he claim is German for 'The Bart, The'?",
        "options": ["Die Bart, Die", "Kill Bart Now", "Bart Must Die", "End Bart End"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In 'Homer's Barbershop Quartet', what was the name of Homer, Apu, Barney, and Principal Skinner's Grammy-winning barbershop group?",
        "options": ["The Be Sharps", "The Four Duffs", "The Harmony Four", "The Springfield Four"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In 'Rosebud', what was the beloved childhood teddy bear that Mr. Burns spent decades searching for?",
        "options": ["Bobo", "Teddy", "Banjo", "Pogo"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In 'Deep Space Homer', what humble object in the space shuttle is credited with saving the crew and named 'Worker of the Week'?",
        "options": ["An inanimate carbon rod", "A Swiss Army knife", "A titanium bolt", "A bag of ruffled chips"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In 'Bart Gets an Elephant', what name does Bart choose for the full-grown African elephant he wins in a radio contest?",
        "options": ["Stampy", "Tuskie", "Trunky", "Jumbo"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In 'Bart of Darkness', what classic Alfred Hitchcock thriller is parodied when a leg-cast-bound Bart suspects Ned Flanders of murder?",
        "options": ["Rear Window", "Vertigo", "Psycho", "North by Northwest"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In 'Itchy & Scratchy Land', what novelty souvenir vanity license plate is perpetually sold out in the gift shop?",
        "options": ["Bort", "Bart", "Mort", "Bert"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In 'Homer Badman', what rare candy confection at the candy convention does Homer obsessively steal?",
        "options": ["The Gummi Venus de Milo", "The Marshmallow Man", "The Chocolate Taj Mahal", "The Licorice Lincoln"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In 'Homer the Great', what secret fraternal organization does Homer join that secretly controls world events?",
        "options": ["The Stonecutters", "The Freemasons", "The Skull and Bones", "The Order of the Moose"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In 'And Maggie Makes Three', what inspiring phrase does Homer create on his workstation wall using photos of Maggie?",
        "options": ["Do It For Her", "Remember You Love Her", "Smile For Her", "Work For Her"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In 'Bart vs. Australia', what native Australian pest do the Simpsons accidentally introduce that devastates the continent's ecosystem?",
        "options": ["Bullfrogs (chazzwazzers)", "Cane toads", "Koalas", "Rabbits"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In 'Who Shot Mr. Burns? (Part 2)', who is ultimately revealed to have pulled the trigger on Mr. Burns?",
        "options": ["Maggie Simpson", "Waylon Smithers", "Homer Simpson", "Tito Puente"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In 'King-Size Homer', what garment does Homer wear around the house after intentionally gaining weight to work from home?",
        "options": ["A floral muumuu", "A giant bathrobe", "A bedsheet toga", "Overalls"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In 'A Fish Called Selma', what Broadway musical starring Troy McClure features the song 'Dr. Zaius'?",
        "options": ["Stop the Planet of the Apes, I Want to Get Off!", "Planet of the Apes: The Musical", "Going Ape on Broadway", "Return to the Forbidden Planet"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In '22 Short Films About Springfield', what does Principal Skinner claim the smoke billowing from his kitchen actually is to Superintendent Chalmers?",
        "options": ["Aurora Borealis", "Steam from steamed clams", "A kitchen grill fire", "A volcanic vent"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In 'Bart on the Road', what landmark do Bart, Milhouse, Nelson, and Martin travel to visit at the World's Fair in Knoxville, Tennessee?",
        "options": ["The Sunsphere", "The Space Needle", "The Gateway Arch", "The Astrodome"],
        "answer": 0,
        "d": 2
    },
    {
        "q": "In 'Summer of 4 Ft. 2', what cool nickname does Bart get stuck with in the beach house while Lisa becomes the popular kid?",
        "options": ["Little Poot", "Stinky", "Dorkus", "Captain Squirt"],
        "answer": 0,
        "d": 2
    },
    {
        "q": "In 'Much Apu About Nothing', what anti-immigration legislation causes Apu to fear deportation from Springfield?",
        "options": ["Proposition 24", "Proposition 13", "Measure 9", "Amendment 4"],
        "answer": 0,
        "d": 2
    },
    {
        "q": "In 'Treehouse of Horror V', what parody of The Shining features Homer losing his mind due to lack of TV and beer?",
        "options": ["The Shinning", "The Glooming", "The Screaming", "The Haunting"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In 'Lisa on Ice', what youth ice hockey team does Bart play for before Lisa joins the rival squad?",
        "options": ["The Mighty Pigs", "The Springfield Blades", "The Ice Hogs", "The Pucksters"],
        "answer": 0,
        "d": 2
    },
    {
        "q": "In 'Grampa vs. Sexual Inadequacy', what brand name is given to the tonic brewed by Homer and Grampa?",
        "options": ["Simpson & Son Revitalizing Tonic", "Old Abe's Elixir", "Springfield Miracle Draught", "Simpson Secret Sauce"],
        "answer": 0,
        "d": 2
    },
    {
        "q": "In 'The Boy Who Knew Too Much', how does the snooty French waiter Monsieur Lacouche pronounce the word 'chowder'?",
        "options": ["Shaud-air", "Chow-da", "Chow-durr", "Tchaw-dare"],
        "answer": 0,
        "d": 3
    },
    {
        "q": "In 'Sweet Seymour Skinner's Baadasssss Song', what dog running through the vents leads to Principal Skinner being fired?",
        "options": ["Santa's Little Helper", "Laddie", "Colt", "Buster"],
        "answer": 0,
        "d": 2
    },
    {
        "q": "In 'Marge Be Not Proud', what violent video game does Bart attempt to shoplift from the Try-N-Save store?",
        "options": ["Bonestorm", "Bloodstorm", "Mortal Mayhem", "Lee Carvallo's Putting Challenge"],
        "answer": 0,
        "d": 1
    },
    {
        "q": "In 'The Day the Violence Died', who is revealed to be the true original creator of Itchy the Mouse?",
        "options": ["Chester J. Lampwick", "Roger Meyers Sr.", "June Bellamy", "Kirk Douglas"],
        "answer": 0,
        "d": 2
    },

    # --- Group 1: Answer index 1 (25 questions) ---
    {
        "q": "In 'Cape Feare', what Gilbert and Sullivan operetta does Bart convince Sideshow Bob to perform in its entirety to stall for time?",
        "options": ["The Pirates of Penzance", "H.M.S. Pinafore", "The Mikado", "Iolanthe"],
        "answer": 1,
        "d": 1
    },
    {
        "q": "In 'Homer Goes to College', what college mascot pig do Homer's nerdy roommates kidnap to pull a prank on Springfield A&M?",
        "options": ["Lord Porkington", "Sir Oinks-A-Lot", "Porky Prime", "Hammy the Boar"],
        "answer": 1,
        "d": 2
    },
    {
        "q": "In '$Springfield (Legalized Gambling in Springfield)', what Howard Hughes-like eccentric behavior does Mr. Burns develop in his penthouse?",
        "options": ["Refusing to touch silverware", "Wearing tissue boxes as shoes and saving jars of urine", "Collecting wooden model trains", "Refusing to wear clothing on Tuesdays"],
        "answer": 1,
        "d": 2
    },
    {
        "q": "In 'Lisa vs. Malibu Stacy', what feminist talking doll does Lisa develop to counter Malibu Stacy's sexist catchphrases?",
        "options": ["Smart Sally", "Lisa Lionheart", "Empowered Emma", "Knowledgeable Kelly"],
        "answer": 1,
        "d": 1
    },
    {
        "q": "In 'Bart Gets Famous', what catchphrase catapults Bart into instant celebrity status on Krusty's show?",
        "options": ["Eat my shorts!", "I didn't do it", "Don't have a cow!", "Ay caramba!"],
        "answer": 1,
        "d": 1
    },
    {
        "q": "In 'Two Dozen and One Greyhounds', what catchy showtune parodying 'Be Our Guest' does Mr. Burns sing about turning puppies into clothing?",
        "options": ["Wear My Fur", "See My Vest", "Puppy Coat Blues", "Skin the Hounds"],
        "answer": 1,
        "d": 1
    },
    {
        "q": "In 'The Springfield Connection', what illegal business operation does Marge discover Herman running out of the Simpsons' garage?",
        "options": ["Moonshine brewing", "Counterfeit designer jeans", "Illegal gambling rings", "Smuggled fireworks"],
        "answer": 1,
        "d": 2
    },
    {
        "q": "In 'Lemon of Troy', what neighboring rival town steals Springfield's beloved sacred lemon tree?",
        "options": ["North Haverbrook", "Shelbyville", "Ogdenville", "Capital City"],
        "answer": 1,
        "d": 1
    },
    {
        "q": "In 'Bart Sells His Soul', what rock song does Bart trick Reverend Lovejoy's congregation into singing as the opening hymn?",
        "options": ["Stairway to Heaven by Led Zeppelin", "In the Garden of Eden by I. Ron Butterfly", "Smoke on the Water by Deep Purple", "Sympathy for the Devil by the Rolling Stones"],
        "answer": 1,
        "d": 1
    },
    {
        "q": "In 'Lisa the Vegetarian', which former Beatle and his wife guest star to help Lisa maintain her vegetarian convictions?",
        "options": ["George Harrison", "Paul and Linda McCartney", "Ringo Starr", "John Lennon"],
        "answer": 1,
        "d": 1
    },
    {
        "q": "In 'Mother Simpson', what activist group did Homer's mother Mona Simpson belong to in the 1960s when she sabotaged Mr. Burns' germ lab?",
        "options": ["Earth First", "Hippie activists (Mothers for Peace)", "The Black Panthers", "Students for a Democratic Society"],
        "answer": 1,
        "d": 2
    },
    {
        "q": "In 'Two Bad Neighbors', which former US President moves into the house directly across the street from the Simpsons?",
        "options": ["Jimmy Carter", "George H.W. Bush", "Bill Clinton", "Richard Nixon"],
        "answer": 1,
        "d": 1
    },
    {
        "q": "In 'Lisa the Iconoclast', what pirate and murderer is revealed to be the true identity of Springfield founder Jebediah Springfield?",
        "options": ["Edward Teach", "Hans Sprungfeld", "William Kidd", "Calico Jack"],
        "answer": 1,
        "d": 2
    },
    {
        "q": "In 'A Star Is Burns', what independent black-and-white film by Barney Gumble wins top honors at the Springfield Film Festival?",
        "options": ["Man Getting Hit by Football", "Pukahontas", "Bright Lights, Beef City", "The Last Pilsner"],
        "answer": 1,
        "d": 2
    },
    {
        "q": "In 'Raging Abe Simpson and His Grumbling Grandson', what World War II military unit did Grampa Simpson lead alongside Mr. Burns?",
        "options": ["The Screaming Eagles", "The Flying Hellfish", "The Mud Dogs", "The Iron Troopers"],
        "answer": 1,
        "d": 2
    },
    {
        "q": "In 'Treehouse of Horror IV', what food item does Homer sell his soul to the Devil (Ned Flanders) for?",
        "options": ["A pepperoni pizza", "A forbidden donut", "A bucket of fried chicken", "A pork chop"],
        "answer": 1,
        "d": 1
    },
    {
        "q": "In 'Homer Loves Flanders', what vegetable hedge does Homer famously melt backwards into after Flanders rejects him?",
        "options": ["A rose bush", "A laurel hedge", "A boxwood shrub", "A ivy trellis"],
        "answer": 1,
        "d": 1
    },
    {
        "q": "In 'Lisa's Rival', what business does Homer start using a massive pile of sugar he finds abandoned after a truck accident?",
        "options": ["A candy factory", "Selling door-to-door sugar", "A bakery", "A moonshine still"],
        "answer": 1,
        "d": 2
    },
    {
        "q": "In 'Bart's Comet', what does Principal Skinner make Bart do before dawn as punishment for launching a weather balloon with Skinner's face?",
        "options": ["Mow the football field", "Amateur astronomy observations", "Clean school chalkboards", "Scrub cafeteria pots"],
        "answer": 1,
        "d": 2
    },
    {
        "q": "In 'Homie the Clown', what famous comedy school does Homer enroll in to become a local Krusty the Clown impersonator?",
        "options": ["Barnum & Bailey Institute", "Krusty's Clown College", "The Ringling Academy", "Bozo's School of Laughs"],
        "answer": 1,
        "d": 1
    },
    {
        "q": "In 'Team Homer', what was the team name of Homer, Moe, Apu, and Otto's bowling squad?",
        "options": ["The Holy Rollers", "The Pin Pals", "The Alley Cats", "The Strike Masters"],
        "answer": 1,
        "d": 1
    },
    {
        "q": "In 'Scenes from the Class Struggle in Springfield', what high-end designer suit does Marge purchase at a discount outlet for $90?",
        "options": ["Gucci", "Chanel", "Prada", "Armani"],
        "answer": 1,
        "d": 2
    },
    {
        "q": "In 'Radioactive Man', what signature line does Rainier Wolfcastle deliver when a tidal wave of real acid destroys his costume?",
        "options": ["It burns like hell!", "The goggles do nothing!", "My eyes, they bleed!", "Up and atom!"],
        "answer": 1,
        "d": 1
    },
    {
        "q": "In 'Homerpalooza', what odd talent earns Homer a spot on the traveling alternative rock festival Lollapalooza?",
        "options": ["Swallowing live goldfish", "Taking cannonballs directly to the stomach", "Burping the alphabet", "Juggling flaming bowling pins"],
        "answer": 1,
        "d": 2
    },
    {
        "q": "In 'Homer the Smithers', what breakfast appliance causes Mr. Burns immense frustration when Homer leaves him alone?",
        "options": ["The waffle iron", "The toaster", "The coffee percolator", "The microwave oven"],
        "answer": 1,
        "d": 3
    },

    # --- Group 2: Answer index 2 (25 questions) ---
    {
        "q": "In 'Cape Feare', what witness protection surname does the Simpson family adopt when relocating to Terror Lake?",
        "options": ["The Johnsons", "The Hendersons", "The Thompsons", "The Jacksons"],
        "answer": 2,
        "d": 1
    },
    {
        "q": "In 'Treehouse of Horror IV', what mythical creature does Bart claim to see on the side of the school bus, terrifying the students?",
        "options": ["A vampire", "A werewolf", "A gremlin", "A goblin"],
        "answer": 2,
        "d": 1
    },
    {
        "q": "In 'Marge on the Lam', what is the name of the new neighbor and friend Marge goes on a wild 'Thelma and Louise' joyride with?",
        "options": ["Luann Van Houten", "Helen Lovejoy", "Ruth Powers", "Agnes Skinner"],
        "answer": 2,
        "d": 2
    },
    {
        "q": "In 'Boy-Scoutz 'n the Hood', what sugary convenience store drink concoction gives Bart and Milhouse an all-night sugar rush?",
        "options": ["Buzz Cola Double Caffeinated", "Slurpee Super Supreme", "An all-syrup Super-Squishee", "Duff Free Sugar Blast"],
        "answer": 2,
        "d": 2
    },
    {
        "q": "In 'Homer the Vigilante', what smooth-talking cat burglar, voiced by Sam Neill, steals Springfield's prized museum treasures?",
        "options": ["Frankie Five Angels", "Jack the Fox", "Molloy", "Arthur Fortune"],
        "answer": 2,
        "d": 2
    },
    {
        "q": "In 'Homer and Apu', which Hollywood actor shadows Apu at the Kwik-E-Mart to prepare for an upcoming convenience store clerk role?",
        "options": ["Alec Baldwin", "Dustin Hoffman", "James Woods", "Michael Keaton"],
        "answer": 2,
        "d": 1
    },
    {
        "q": "In 'Sideshow Bob Roberts', who is the conservative radio talk show host who rallies Springfield voters to elect Sideshow Bob mayor?",
        "options": ["Rush Limbaugh", "Geraldo Rivera", "Birch Barlow", "Bill O'Reilly"],
        "answer": 2,
        "d": 2
    },
    {
        "q": "In 'Bart's Girlfriend', which church elder's daughter steals the Sunday collection plate and lets Bart take the blame?",
        "options": ["Maude Flanders", "Helen Lovejoy", "Jessica Lovejoy", "Allison Taylor"],
        "answer": 2,
        "d": 1
    },
    {
        "q": "In 'Fear of Flying', what childhood revelation explains Marge's deep-rooted phobia of airplane travel?",
        "options": ["A turbulent flight over Chicago", "Her father was a pilot who crashed", "Her father was an airline flight attendant, not a pilot", "She dropped an ice cream cone on a runway"],
        "answer": 2,
        "d": 2
    },
    {
        "q": "In 'Lisa's Wedding', what English fiancé does a fortune teller predict twenty-three-year-old Lisa will fall in love with in the year 2010?",
        "options": ["Colin", "Arthur", "Hugh Parkfield", "George Harrison"],
        "answer": 2,
        "d": 2
    },
    {
        "q": "In 'The PTA Disbands', who replaces Mrs. Krabappel as Bart's temporary substitute teacher during the teachers' strike?",
        "options": ["Principal Skinner", "Ned Flanders", "Marge Simpson", "Grampa Simpson"],
        "answer": 2,
        "d": 2
    },
    {
        "q": "In 'Round Springfield', what does Bart swallow in a bowl of Krusty-O's cereal that causes appendicitis?",
        "options": ["A plastic whistle", "A metal coin", "A jagged metal Krusty-O", "A miniature action figure"],
        "answer": 2,
        "d": 2
    },
    {
        "q": "In 'Home Sweet Homediddly-Dum-Doodily', what religious ceremony does Ned Flanders attempt to perform on Bart and Lisa at the river?",
        "options": ["First Communion", "Confirmation", "Baptism", "Exorcism"],
        "answer": 2,
        "d": 2
    },
    {
        "q": "In 'Treehouse of Horror VI', which nightmare villain slashes Springfield Elementary children in their sleep with rakes and hedge trimmers?",
        "options": ["Sideshow Bob", "Homer Simpson", "Groundskeeper Willie", "Principal Skinner"],
        "answer": 2,
        "d": 1
    },
    {
        "q": "In 'Sideshow Bob's Last Gleaming', from where does Sideshow Bob steal an authentic 10-megaton nuclear warhead?",
        "options": ["Springfield Nuclear Power Plant", "Fort Springfield", "An Air Force base during an air show", "The naval reserve submarine"],
        "answer": 2,
        "d": 2
    },
    {
        "q": "In 'Bart the Fink', what tax evasion scandal exposes Krusty the Clown after Bart has his check stamped?",
        "options": ["Swiss bank accounts", "Bribing IRS agents", "An offshore holding company named Cayman Islands Krusty Corp", "Using illegal tax write-offs for monkeys"],
        "answer": 2,
        "d": 3
    },
    {
        "q": "In '22 Short Films About Springfield', what fast food franchise meal does Skinner secretly substitute for his burnt roast and call 'steamed hams'?",
        "options": ["McDonald's burgers", "Wendy's patties", "Krusty Burgers", "White Castle sliders"],
        "answer": 2,
        "d": 1
    },
    {
        "q": "In 'Who Shot Mr. Burns? (Part 1)', what natural energy deposit does Mr. Burns drill beneath Springfield Elementary School?",
        "options": ["Natural gas pocket", "Uranium deposit", "Crude oil reservoir", "Geothermal hot spring"],
        "answer": 2,
        "d": 1
    },
    {
        "q": "In 'The Last Temptation of Homer', what is the name of Homer's attractive new coworker at the nuclear plant who shares all his eating habits?",
        "options": ["Lurleen Lumpkin", "Ruth Powers", "Mindy Simmons", "Princess Kashmir"],
        "answer": 2,
        "d": 1
    },
    {
        "q": "In 'Lisa vs. Malibu Stacy', who created the original Malibu Stacy doll whom Lisa tracks down in her dollhouse mansion?",
        "options": ["Amber Dempsey", "Ruth Powers", "Stacy Lovell", "Luann Van Houten"],
        "answer": 2,
        "d": 2
    },
    {
        "q": "In 'Burns' Heir', how does Mr. Burns test Bart's cruelty by asking him to fire an employee at the power plant?",
        "options": ["He makes him fire Carl Carlson", "He makes him fire Lenny Leonard", "He makes him fire Homer Simpson", "He makes him fire Charlie"],
        "answer": 2,
        "d": 2
    },
    {
        "q": "In 'Treehouse of Horror V', in 'Time and Punishment', what kitchen appliance does Homer turn into a time machine?",
        "options": ["The microwave", "The blender", "The toaster", "The garbage disposal"],
        "answer": 2,
        "d": 1
    },
    {
        "q": "In 'Bart's Inner Child', which motivational self-help guru holds an arena seminar urging Springfieldians to 'do what you feel like'?",
        "options": ["Tony Robbins", "Dr. Nick", "Brad Goodman", "Dr. Marvin Monroe"],
        "answer": 2,
        "d": 2
    },
    {
        "q": "In 'Secrets of a Successful Marriage', what adult education course does Homer Simpson teach at the Springfield Learning Center?",
        "options": ["Nuclear Physics for Beginners", "How to Eat Donuts", "Secrets of a Successful Marriage", "Car Maintenance Made Simple"],
        "answer": 2,
        "d": 2
    },
    {
        "q": "In 'The Simpsons 138th Episode Spectacular', who hosts the retrospective special featuring deleted scenes and outtakes?",
        "options": ["Krusty the Clown", "Lionel Hutz", "Troy McClure", "Matt Groening"],
        "answer": 2,
        "d": 1
    },

    # --- Group 3: Answer index 3 (25 questions) ---
    {
        "q": "In 'Cape Feare', what does Sideshow Bob step on repeatedly outside the Simpsons' houseboat that flips up and hits him in the face?",
        "options": ["Brooms", "Shovels", "Mops", "Garden rakes"],
        "answer": 3,
        "d": 1
    },
    {
        "q": "In 'Homer's Barbershop Quartet', which Beatle does Homer encounter on a rooftop who tells him 'It's been done'?",
        "options": ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
        "answer": 3,
        "d": 1
    },
    {
        "q": "In 'Treehouse of Horror IV', who serves on the 'Jury of the Damned' presiding over Homer's contract with the Devil?",
        "options": ["Nero, Dracula, and Bluebeard", "Attila the Hun, Judas, and Genghis Khan", "Richard Nixon, John Wilkes Booth, and Lizzie Borden", "Benedict Arnold, Lizzie Borden, John Wilkes Booth, Blackbeard, John Dillinger, and the 1976 Philadelphia Flyers"],
        "answer": 3,
        "d": 2
    },
    {
        "q": "In '$Springfield (Legalized Gambling in Springfield)', what legendary casino magician duo's tiger attacks them on stage?",
        "options": ["Penn and Teller", "David Copperfield and Claudia Schiffer", "Houdini and Thurston", "Gunter and Ernst"],
        "answer": 3,
        "d": 2
    },
    {
        "q": "In 'Lisa's Rival', what young prodigy girl outplays Lisa on the saxophone and builds an elaborate 'Tell-Tale Heart' diorama?",
        "options": ["Janey Powell", "Sherri Mackleberry", "Terri Mackleberry", "Allison Taylor"],
        "answer": 3,
        "d": 2
    },
    {
        "q": "In 'Sideshow Bob Roberts', what is the name of the dead pet whose vote Sideshow Bob's campaign used to win the election?",
        "options": ["Blinky the Fish", "Laddie", "Santa's Little Helper", "Snowball I"],
        "answer": 3,
        "d": 2
    },
    {
        "q": "In 'Homer Badman', what sensationalist tabloid television news program airs a grossly edited interview portraying Homer as an ogre?",
        "options": ["Hard Copy", "Inside Edition", "A Current Affair", "Rock Bottom"],
        "answer": 3,
        "d": 1
    },
    {
        "q": "In 'Homer the Great', what ancient secret title does Homer hold after a birthmark proves he is the chosen one?",
        "options": ["The Supreme Grandmaster", "The Great Mason", "The All-Seeing Builder", "The Chosen One"],
        "answer": 3,
        "d": 2
    },
    {
        "q": "In 'Bart vs. Australia', what bizarre punishment is Bart sentenced to undergo by the Australian Parliament?",
        "options": ["One year in prison", "Exile to Tasmania", "Cleaning Sydney Harbor", "A kick in the posterior with a giant boot (The Boot)"],
        "answer": 3,
        "d": 1
    },
    {
        "q": "In 'A Star Is Burns', what short film created by Hans Moleman loses the film festival to Barney's masterpiece?",
        "options": ["A Day in the Life of a Mole", "The Agony of Old Age", "Autumn Leaves", "Man Getting Hit by Football"],
        "answer": 3,
        "d": 1
    },
    {
        "q": "In 'Lisa the Vegetarian', what barbecue food does Homer desperately pursue down a hill, chanting that it is 'still good'?",
        "options": ["A rack of ribs", "A giant beef brisket", "A plate of sausages", "A roasted whole roast pig"],
        "answer": 3,
        "d": 1
    },
    {
        "q": "In 'Treehouse of Horror VI', into what bizarre computer-animated dimension does Homer accidentally step behind a bookcase?",
        "options": ["The 8-bit arcade world", "A claymation landscape", "A cyberspace highway", "The third dimension (3D CGI realm)"],
        "answer": 3,
        "d": 1
    },
    {
        "q": "In 'Two Bad Neighbors', what prank does Bart pull on George Bush that ruins the former President's expensive memoirs?",
        "options": ["Pouring soda on his typewriter", "Stealing his presidential seal", "Egging his limousine", "Shredding his manuscript pages with a motor"],
        "answer": 3,
        "d": 2
    },
    {
        "q": "In 'Lisa the Iconoclast', what two obscure words coined in the episode became famous cultural catchphrases for validity and growth?",
        "options": ["Kwyjibo and D'oh", "Craptacular and Meh", "Yoink and Chazzwazzer", "Cromulent and Embiggen"],
        "answer": 3,
        "d": 1
    },
    {
        "q": "In 'The Day the Violence Died', what luxury item does Chester J. Lampwick demand and receive after winning his $800 billion lawsuit?",
        "options": ["A private jet filled with cash", "A personal bowling alley", "A yacht made of platinum", "A house made of solid gold"],
        "answer": 3,
        "d": 3
    },
    {
        "q": "In 'A Fish Called Selma', what strange romantic rumor plagues Troy McClure's Hollywood career before he marries Selma?",
        "options": ["He refuses to learn scripts", "He stole movie studio props", "He was never an actual actor", "A bizarre sexual fetish involving fish and marine life"],
        "answer": 3,
        "d": 2
    },
    {
        "q": "In '22 Short Films About Springfield', what restaurant does Snake hold up while Chief Wiggum is having lunch, leading to a Pulp Fiction homage?",
        "options": ["Luigi's Italian Restaurant", "The Frying Dutchman", "The Gilded Truffle", "Herman's Military Antiques"],
        "answer": 3,
        "d": 2
    },
    {
        "q": "In 'Much Apu About Nothing', what absurd tax levy does Mayor Quimby blame on illegal immigrants after citizens complain?",
        "options": ["The Pothole Tax", "The Snowplow Surcharge", "The Garbage Fee", "The $5 Bear Patrol Tax"],
        "answer": 3,
        "d": 2
    },
    {
        "q": "In 'Homerpalooza', which 1990s alternative rock group accidentally orders the London Symphony Orchestra while high?",
        "options": ["Smashing Pumpkins", "Sonic Youth", "Peter Frampton", "Cypress Hill"],
        "answer": 3,
        "d": 1
    },
    {
        "q": "In 'Summer of 4 Ft. 2', what does Lisa place in the back of the family station wagon that Homer drives all the way to Little Poot's beach house?",
        "options": ["A collection of seashells", "Her beloved saxophone", "Her encyclopedia collection", "A yearbook with no signatures"],
        "answer": 3,
        "d": 3
    },
    {
        "q": "In 'Lady Bouvier's Lover', what famous 1960s film ending is parodied when Grampa crashes Jacqueline Bouvier's wedding and escapes on a bus?",
        "options": ["Midnight Cowboy", "Easy Rider", "Bonnie and Clyde", "The Graduate"],
        "answer": 3,
        "d": 2
    },
    {
        "q": "In 'The Boy Who Knew Too Much', who is accused of assaulting French waiter Monsieur Lacouche at Mayor Quimby's nephew's birthday party?",
        "options": ["Snake Jailbird", "Sideshow Mel", "Fat Tony", "Freddy Quimby"],
        "answer": 3,
        "d": 2
    },
    {
        "q": "In 'Marge on the Lam', what musical instrument does Homer get both arms stuck inside in the supermarket snack vending machines?",
        "options": ["A claw prize machine and an arcade game", "A bowling ball return and an oven", "A jukebox and a payphone", "A candy vending machine and a soda vending machine"],
        "answer": 3,
        "d": 2
    },
    {
        "q": "In 'Who Shot Mr. Burns? (Part 1)', what device does Mr. Burns construct to block out the sun and force Springfield to consume electricity 24 hours a day?",
        "options": ["A giant umbrella", "An orbital mirror", "A smoke-generating tower", "A giant mechanical sun blocker"],
        "answer": 3,
        "d": 1
    },
    {
        "q": "In 'Mother Simpson', what does Homer do after waving goodbye to his fugitive mother Mona at the end of the episode?",
        "options": ["Drives home in complete silence", "Weeps openly with Marge in bed", "Drinks beer with Moe until sunrise", "Sits on the hood of his car staring up at the night stars as the credits roll"],
        "answer": 3,
        "d": 1
    }
]

# Ensure formatting
output = []
for q in raw_questions:
    output.append({
        "show": "The Simpsons",
        "q": q["q"],
        "options": q["options"],
        "answer": q["answer"],
        "d": q["d"]
    })

with open("tools/staging/simpsons_batch2.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=1)

print(f"Generated {len(output)} questions for batch 2.")
