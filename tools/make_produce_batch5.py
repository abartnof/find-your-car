#!/usr/bin/env python3
"""
Generate Batch 5 of Fruits & Veggies trivia (100 questions):
Trivia, World Records, Scoville Heat Scale, Legal Rulings, Produce Festivals & Cultural Lore.
Target: ~30 d1, ~40 d2, ~30 d3.
"""

from produce_batch_builder import build_batch

BATCH_5 = [
    # 1-20: World Records & Giant Produce (d1-d3)
    {
        "q": "What variety of pumpkin, bred by Nova Scotia farmer Howard Dill, is the genetic ancestor of virtually all modern world-record giant pumpkins?",
        "correct": "Atlantic Giant",
        "distractors": ["Big Max", "Cinderella Pumpkin", "Connecticut Field"],
        "d": 2
    },
    {
        "q": "In 2023, Minnesota horticulture teacher Travis Gienger set a world record by growing an Atlantic Giant pumpkin weighing how much?",
        "correct": "2,749 pounds (1,246.9 kg)",
        "distractors": ["1,120 pounds (508 kg)", "1,850 pounds (839 kg)", "3,890 pounds (1,764 kg)"],
        "d": 2
    },
    {
        "q": "What Northern California coastal town hosts the prestigious World Championship Pumpkin Weigh-Off every October?",
        "correct": "Half Moon Bay",
        "distractors": ["Mendocino", "Carmel-by-the-Sea", "Bodega Bay"],
        "d": 2
    },
    {
        "q": "Why do giant vegetables grown in the Matanuska Valley of Alaska frequently break world weight records (such as a 138-pound cabbage)?",
        "correct": "Subarctic summer daylight reaches up to 19 to 20 hours per day, driving continuous photosynthesis",
        "distractors": ["The soil is naturally warmed by geothermal volcanic vents", "Farmers inject plants with liquid nitrogen fertilizers daily", "Continuous sub-zero night frosts cause cell walls to quadruple in size"],
        "d": 2
    },
    {
        "q": "What is the largest tree-borne fruit in the world, capable of reaching weights over 80 to 100 pounds?",
        "correct": "Jackfruit",
        "distractors": ["Breadfruit", "Durian", "Papaya"],
        "d": 1
    },
    {
        "q": "What is the smallest flowering plant on Earth, which produces a microscopic one-seeded fruit called a utricle?",
        "correct": "Wolffia (Watermeal)",
        "distractors": ["Duckweed", "Spirulina", "Sphagnum"],
        "d": 3
    },
    {
        "q": "Pairs of which prized Japanese cantaloupe hybrid grown in Hokkaido regularly fetch tens of thousands of dollars at luxury fruit auctions?",
        "correct": "Yubari King melon",
        "distractors": ["Hami melon", "Galia melon", "Santa Claus melon"],
        "d": 2
    },
    {
        "q": "What ruby-red table grape variety developed in Ishikawa Prefecture, Japan, is famous for selling at auction for over $10,000 per bunch?",
        "correct": "Ruby Roman",
        "distractors": ["Kyoho", "Red Globe", "Crimson Seedless"],
        "d": 2
    },
    {
        "q": "Which rare black-skinned watermelon grown exclusively on the island of Hokkaido, Japan, can sell for thousands of dollars apiece?",
        "correct": "Densuke watermelon",
        "distractors": ["Moon and Stars", "Sugar Baby", "Carolina Cross"],
        "d": 2
    },
    {
        "q": "Why do farmers in Zentsuji, Japan, grow square and cubic watermelons inside tempered glass boxes?",
        "correct": "They fit efficiently into Japanese refrigerators and stack easily for shipping (though they are sold mostly as luxury decorative novelties)",
        "distractors": ["Square shape doubles the sugar content of the melon flesh", "It prevents bees from laying eggs in the rind", "It makes the seeds grow in straight geometric lines"],
        "d": 2
    },
    {
        "q": "According to Guinness World Records, the heaviest watermelon on record weighed over 350 pounds and was grown in which U.S. state?",
        "correct": "Tennessee",
        "distractors": ["Georgia", "Texas", "Florida"],
        "d": 3
    },
    {
        "q": "What British grower held the world record for the heaviest onion, weighing over 19 pounds, in Harrogate, England?",
        "correct": "Tony Glover (and Gareth Griffin)",
        "distractors": ["Alan Titchmarsh", "Monty Don", "David Austin"],
        "d": 3
    },
    {
        "q": "Which fruit or vegetable was the first genetically modified whole food approved by the U.S. FDA for commercial sale in 1994?",
        "correct": "Flavr Savr tomato",
        "distractors": ["Golden Rice", "Bt Sweet Corn", "Roundup Ready Soy"],
        "d": 1
    },
    {
        "q": "What trait was engineered into the groundbreaking Flavr Savr tomato by Calgene scientists?",
        "correct": "Antisense RNA suppressed polygalacturonase, allowing the tomato to remain firm longer without rotting",
        "distractors": ["Bacterial genes caused the plant to produce its own insecticide", "It contained jellyfish genes that made the skin glow green", "It produced twice the sucrose of standard table grapes"],
        "d": 3
    },
    {
        "q": "Which vegetable was the first to be grown in outer space aboard the Space Shuttle Columbia in 1995?",
        "correct": "Potato",
        "distractors": ["Radish", "Lettuce", "Tomato"],
        "d": 2
    },
    {
        "q": "What leafy vegetable became the first fresh crop harvested and eaten by astronauts aboard the International Space Station in 2015?",
        "correct": "Red romaine lettuce ('Outredgeous')",
        "distractors": ["Baby spinach", "Watercress", "Arugula"],
        "d": 2
    },
    {
        "q": "Cotton Candy grapes, which taste remarkably like spun carnival sugar, were developed through which plant breeding method?",
        "correct": "Traditional cross-hybridization of wild and cultivated grape species over years",
        "distractors": ["Injecting high-fructose corn syrup into the grapevine roots", "Soaking grape bunches in artificial cotton candy flavoring baths", "Direct CRISPR genetic editing of sucrose genes"],
        "d": 2
    },
    {
        "q": "What horticulturist and fruit breeder at International Fruit Genetics in California created the Cotton Candy grape and TearDrops grape?",
        "correct": "David Cain",
        "distractors": ["Floyd Zaiger", "Luther Burbank", "Ed Currie"],
        "d": 3
    },
    {
        "q": "What famed fruit breeder in Modesto, California created patented stone fruit interspecific hybrids including the Pluot, Aprium, and Peacotum?",
        "correct": "Floyd Zaiger",
        "distractors": ["David Fairchild", "Rudolph Hass", "Jesse Hiatt"],
        "d": 3
    },
    {
        "q": "What is the genetic difference between a Pluot and an Aprium?",
        "correct": "A Pluot is predominantly plum in parentage, while an Aprium is predominantly apricot in parentage",
        "distractors": ["A Pluot has white flesh while an Aprium has green skin", "A Pluot is sterile while an Aprium produces viable seeds", "A Pluot is a citrus cross while an Aprium is a stone fruit"],
        "d": 3
    },

    # 21-45: Scoville Heat Scale & Chili Pepper Lore (d1-d3)
    {
        "q": "What unit of measurement, established in 1912 by an American pharmacist, measures the pungency and heat of chili peppers?",
        "correct": "Scoville Heat Units (SHU)",
        "distractors": ["Brix Scale", "Mohs Hardness Scale", "Baumé Scale"],
        "d": 1
    },
    {
        "q": "How was the original Scoville Organoleptic Test conducted by Wilbur Scoville in 1912?",
        "correct": "Chili extract was progressively diluted with sugar water until heat was no longer detectable by a trained panel of five human tasters",
        "distractors": ["Chili oil was burned in a calorimeter to measure thermal heat output", "Drops of pepper juice were placed on human eyelids to time blinking reactions", "Extract was mixed with litmus paper to record color change"],
        "d": 2
    },
    {
        "q": "What modern analytical laboratory method has replaced human tasting panels to objectively measure capsaicinoid concentrations in chili peppers?",
        "correct": "High-Performance Liquid Chromatography (HPLC)",
        "distractors": ["Gas flame mass spectrometry", "Nuclear magnetic resonance imaging", "Centrifugal refractometry"],
        "d": 2
    },
    {
        "q": "Pure crystalline capsaicin rates at approximately how many Scoville Heat Units?",
        "correct": "16,000,000 SHU",
        "distractors": ["1,000,000 SHU", "5,000,000 SHU", "100,000,000 SHU"],
        "d": 1
    },
    {
        "q": "What ultra-hot pepper, bred by Ed Currie of PuckerButt Pepper Company, was officially certified by Guinness in 2023 as the world's hottest at 2,693,000 SHU?",
        "correct": "Pepper X",
        "distractors": ["Carolina Reaper", "Dragon's Breath", "Apollo Pepper"],
        "d": 1
    },
    {
        "q": "Prior to Pepper X, which pepper held the Guinness World Record for hottest chili pepper from 2013 to 2023 at an average of 1.64 million SHU?",
        "correct": "Carolina Reaper",
        "distractors": ["Trinidad Moruga Scorpion", "Ghost Pepper", "Naga Viper"],
        "d": 2
    },
    {
        "q": "The Carolina Reaper was originally created in South Carolina by crossing a red habanero with which other pepper?",
        "correct": "Ghost Pepper (Bhut Jolokia)",
        "distractors": ["Scotch Bonnet", "Jalapeño", "Serrano"],
        "d": 3
    },
    {
        "q": "Which pepper from Assam, India, became the first pepper in history to be scientifically verified at over 1,000,000 Scoville Heat Units in 2007?",
        "correct": "Bhut Jolokia (Ghost Pepper)",
        "distractors": ["Bird's eye chili", "Cayenne", "Habanero"],
        "d": 2
    },
    {
        "q": "What is the typical Scoville rating of a standard grocery store jalapeño pepper?",
        "correct": "2,500 to 8,000 SHU",
        "distractors": ["50 to 200 SHU", "30,000 to 50,000 SHU", "100,000 to 350,000 SHU"],
        "d": 1
    },
    {
        "q": "Which pepper scores a flat zero (0 SHU) on the Scoville heat scale?",
        "correct": "Bell pepper",
        "distractors": ["Poblano pepper", "Banana pepper", "Anaheim pepper"],
        "d": 1
    },
    {
        "q": "What is a smoked, dried jalapeño pepper called in Mexican cuisine?",
        "correct": "Chipotle",
        "distractors": ["Ancho", "Guajillo", "Pasilla"],
        "d": 1
    },
    {
        "q": "When a poblano pepper is dried, what is it called?",
        "correct": "Ancho chili",
        "distractors": ["Chipotle", "Chipotle morita", "Cascabel"],
        "d": 2
    },
    {
        "q": "Where inside a hot chili pepper is capsaicin predominantly synthesized and concentrated?",
        "correct": "The placenta (the inner white pith and ribs holding the seeds)",
        "distractors": ["The outer skin (exocarp)", "The seeds themselves", "The green stem and calyx"],
        "d": 3
    },
    {
        "q": "Why do the seeds of chili peppers often taste spicy when eaten?",
        "correct": "They absorb surface oils by being in physical contact with the adjacent placental membrane",
        "distractors": ["The seed embryo synthesizes pure capsaicin crystals in its cotyledons", "Seeds contain hydrochloric acid to prevent insects from cracking them", "The seed shell is coated in volatile sulfur compounds"],
        "d": 3
    },
    {
        "q": "Which sensory receptor on human tongue nerve endings binds capsaicin, tricking the brain into perceiving scorching physical heat?",
        "correct": "TRPV1 (transient receptor potential vanilloid 1)",
        "distractors": ["TRPM8", "TRPA1", "CB1 cannabinoid receptor"],
        "d": 3
    },
    {
        "q": "Why can wild birds consume scorching hot chili peppers without feeling any burning pain?",
        "correct": "The avian TRPV1 receptor has a slight amino acid variation that prevents capsaicin from binding",
        "distractors": ["Birds lack pain nerves in their beaks entirely", "Bird saliva contains neutralizing sodium bicarbonate", "Birds swallow peppers whole into an acidic gizzard before tasting them"],
        "d": 3
    },
    {
        "q": "From an evolutionary standpoint, why did wild chili peppers evolve capsaicin to deter mammals while attracting birds?",
        "correct": "Mammalian molar teeth crush seeds destroying them, while birds disperse intact seeds widely in their droppings",
        "distractors": ["Birds pollinate chili flowers directly while mammals eat the entire plant", "Mammals transmit leaf blight viruses through their fur", "Bird droppings provide potassium fertilizer required by seedlings"],
        "d": 3
    },
    {
        "q": "Why is drinking whole milk or eating yogurt the most effective home remedy to relieve a severe chili pepper burn in the mouth?",
        "correct": "Casein proteins in dairy bind to hydrophobic capsaicin molecules and wash them off nerve receptors",
        "distractors": ["Cold milk freezes nerve endings instantly into numbness", "Lactose chemically neutralizes the alkalinity of capsaicin", "Calcium ions permanently block the human salivary glands"],
        "d": 1
    },
    {
        "q": "Why does chugging cold water do almost nothing to soothe a mouth burning from hot peppers?",
        "correct": "Capsaicin is a fat-soluble oil that is insoluble in water; water merely spreads the oil around the mouth",
        "distractors": ["Water activates water-reactive enzymes that quadruple the capsaicin heat", "Water dilutes saliva, making the mouth five times more sensitive to pain", "Water triggers an allergic histamine reaction against pepper oils"],
        "d": 1
    },
    {
        "q": "What Japanese small green pepper is notoriously known for the roulette-like trait where roughly one out of every ten peppers is unexpectedly spicy?",
        "correct": "Shishito pepper",
        "distractors": ["Padrón pepper", "Bird's eye pepper", "Serrano pepper"],
        "d": 2
    },
    {
        "q": "What famous Spanish heirloom frying pepper from Galicia shares the same trait as the shishito, summarized by the saying 'Some are hot, some are not'?",
        "correct": "Padrón pepper",
        "distractors": ["Piquillo pepper", "Ñora pepper", "Guindilla pepper"],
        "d": 3
    },
    {
        "q": "Which chili species includes the habanero, ghost pepper, Carolina Reaper, and Scotch bonnet?",
        "correct": "Capsicum chinense",
        "distractors": ["Capsicum annuum", "Capsicum frutescens", "Capsicum baccatum"],
        "d": 3
    },
    {
        "q": "Tabasco peppers, used to make the iconic Avery Island Louisiana hot sauce, belong to which Capsicum species?",
        "correct": "Capsicum frutescens",
        "distractors": ["Capsicum annuum", "Capsicum pubescens", "Capsicum baccatum"],
        "d": 3
    },
    {
        "q": "Which unique South American chili pepper species (such as the Rocoto) is identified by having hairy leaves, purple flowers, and black seeds?",
        "correct": "Capsicum pubescens",
        "distractors": ["Capsicum chinense", "Capsicum annuum", "Capsicum baccatum"],
        "d": 3
    },
    {
        "q": "Avery Island, Louisiana, the ancestral manufacturing home of Tabasco sauce, is geologically what structure?",
        "correct": "A natural salt dome",
        "distractors": ["A volcanic caldera", "A limestone barrier reef", "An alluvial mangrove swamp"],
        "d": 3
    },

    # 46-65: Supreme Court Cases & Legal Produce Classifications (d1-d3)
    {
        "q": "In the landmark 1893 case Nix v. Hedden, what did the United States Supreme Court unanimously rule regarding tomatoes?",
        "correct": "Tomatoes must be classified and taxed as vegetables under customs tariff law, based on ordinary culinary use",
        "distractors": ["Tomatoes are legally fruits and therefore exempt from all agricultural import duties", "Tomatoes are poisonous nightshades and barred from inter-state transit", "Tomatoes may only be sold when fully ripened on the vine"],
        "d": 2
    },
    {
        "q": "What federal statute was at the center of the dispute in Nix v. Hedden (1893)?",
        "correct": "The Tariff Act of 1883, which imposed a 10% duty on imported vegetables but none on fruit",
        "distractors": ["The Pure Food and Drug Act of 1906", "The Agricultural Marketing Agreement Act", "The Smoot-Hawley Tariff Act"],
        "d": 3
    },
    {
        "q": "Which Supreme Court Justice authored the unanimous opinion in Nix v. Hedden, noting that tomatoes are served at dinner with meat or fish, not as dessert?",
        "correct": "Justice Horace Gray",
        "distractors": ["Justice Oliver Wendell Holmes Jr.", "Chief Justice Melville Fuller", "Justice John Marshall Harlan"],
        "d": 3
    },
    {
        "q": "In the 1888 Supreme Court case Robertson v. Salomon, what produce item was ruled to be a vegetable rather than a seed under customs law?",
        "correct": "White beans",
        "distractors": ["Lentils", "Soybeans", "Chickpeas"],
        "d": 3
    },
    {
        "q": "In 2007, the Oklahoma state legislature created a humorous culinary stir by passing a bill designating which produce item as the official state vegetable?",
        "correct": "Watermelon",
        "distractors": ["Pumpkin", "Okra", "Sweet potato"],
        "d": 2
    },
    {
        "q": "What is the official state fruit of Georgia?",
        "correct": "Peach",
        "distractors": ["Watermelon", "Blueberry", "Apple"],
        "d": 1
    },
    {
        "q": "What is the official state vegetable of Georgia, celebrated for its mild, sweet flavor due to low soil sulfur?",
        "correct": "Vidalia onion",
        "distractors": ["Collard greens", "Sweet potato", "Okra"],
        "d": 1
    },
    {
        "q": "Which fruit is the official state fruit of Washington State?",
        "correct": "Apple",
        "distractors": ["Cherry", "Pear", "Blackberry"],
        "d": 1
    },
    {
        "q": "What is the official state fruit of New York, designated in 1976?",
        "correct": "Apple",
        "distractors": ["Concord grape", "Blueberry", "Strawberry"],
        "d": 2
    },
    {
        "q": "What is the official state vegetable of Idaho, the leading producer of this crop in the nation?",
        "correct": "Potato",
        "distractors": ["Sugar beet", "Sweet corn", "Lentil"],
        "d": 1
    },
    {
        "q": "Which vegetable is designated as the official state vegetable of North Carolina?",
        "correct": "Sweet potato",
        "distractors": ["Cabbage", "Green bean", "Cucumber"],
        "d": 2
    },
    {
        "q": "What are the two co-official state vegetables of New Mexico, forming the foundation of regional cuisine?",
        "correct": "Chile pepper and frijoles pintos (pinto beans)",
        "distractors": ["Sweet corn and squash", "Tomatillo and cactus pads", "Jalapeño and sweet potato"],
        "d": 2
    },
    {
        "q": "What is the official state fruit of New Jersey, honoring the pioneering domestication work of Elizabeth White in the Pine Barrens?",
        "correct": "Highbush blueberry",
        "distractors": ["Cranberry", "Jersey tomato", "Peach"],
        "d": 2
    },
    {
        "q": "What is the official state fruit of Florida?",
        "correct": "Orange",
        "distractors": ["Grapefruit", "Key lime", "Mango"],
        "d": 1
    },
    {
        "q": "What unique state law did Vermont pass in 1999 regarding the consumption of its official state pie (apple pie)?",
        "correct": "It encourages serving apple pie with a glass of cold milk, a slice of cheddar cheese, or a scoop of vanilla ice cream",
        "distractors": ["Apple pie must be baked exclusively with Granny Smith apples", "It is illegal to serve apple pie after sunset on Sundays", "All apple pies sold in diners must have double crusts"],
        "d": 2
    },
    {
        "q": "Which fruit is recognized as the national fruit of India, Pakistan, and the Philippines?",
        "correct": "Mango",
        "distractors": ["Papaya", "Banana", "Coconut"],
        "d": 1
    },
    {
        "q": "What is the national fruit of Jamaica, traditionally paired with salted cod in the island's beloved national dish?",
        "correct": "Ackee",
        "distractors": ["Breadfruit", "Soursop", "Guava"],
        "d": 1
    },
    {
        "q": "Why is it dangerous to eat ackee fruit before it opens naturally on the tree?",
        "correct": "Unripe ackee contains high levels of hypoglycin A, causing severe Jamaican Vomiting Sickness and hypoglycemia",
        "distractors": ["It contains concentrated strychnine that paralyzes muscles", "It causes permanent kidney stones within 24 hours", "It produces hydrocyanic acid that burns the throat"],
        "d": 3
    },
    {
        "q": "The ackee tree (Blighia sapida) was scientifically named after which notorious British naval captain of HMS Bounty?",
        "correct": "Captain William Bligh",
        "distractors": ["Captain James Cook", "Admiral Horatio Nelson", "Sir Francis Drake"],
        "d": 3
    },
    {
        "q": "What is the national fruit of Mexico?",
        "correct": "Avocado (and Prickly Pear cactus fruit)",
        "distractors": ["Papaya", "Guava", "Lime"],
        "d": 2
    },

    # 66-85: Produce Festivals & Global Celebrations (d1-d3)
    {
        "q": "In which Spanish town does the world-famous 'La Tomatina' festival take place every August, featuring a massive food fight with over 100 metric tons of tomatoes?",
        "correct": "Buñol (Valencia)",
        "distractors": ["Pamplona", "Seville", "Toledo"],
        "d": 2
    },
    {
        "q": "What is the safety rule enforced for participants before throwing a tomato during La Tomatina in Buñol?",
        "correct": "Tomatoes must be squashed or crushed by hand before throwing to prevent injury",
        "distractors": ["Tomatoes must be chilled in ice water for one hour", "Participants must wear fencing armor", "Tomatoes must be sliced in half with plastic knives"],
        "d": 2
    },
    {
        "q": "What fruit is thrown between rival teams in the historic northern Italian town of Ivrea during its annual carnival battle?",
        "correct": "Oranges",
        "distractors": ["Lemons", "Apples", "Watermelons"],
        "d": 2
    },
    {
        "q": "The historic Battle of the Oranges (Battaglia delle Arance) in Ivrea commemorates which historical event?",
        "correct": "A medieval rebellion where townsfolk overthrew an abusive local tyrant count",
        "distractors": ["The Roman conquest of Gaul", "A miraculous end to a citrus famine in 1600", "A border treaty signed with Napoleon"],
        "d": 3
    },
    {
        "q": "What vegetable is carved into intricate, elaborate nativity scenes and folk art every December 23 in Oaxaca, Mexico during 'La Noche de los Rábanos'?",
        "correct": "Radish",
        "distractors": ["Pumpkin", "Turnip", "Carrot"],
        "d": 2
    },
    {
        "q": "Why are the radishes used in Oaxaca's Night of the Radishes specially grown for the festival?",
        "correct": "They are heavily fertilized and left in the ground for months to grow up to two feet long and weigh several pounds",
        "distractors": ["They are bred with bioluminescent genes to glow at night", "They are soaked in red dye to match holiday colors", "They are harvested entirely from subterranean caves"],
        "d": 3
    },
    {
        "q": "The town of Menton on the French Riviera hosts an annual festival in February featuring gigantic floats and architectural statues constructed from thousands of tons of which fruits?",
        "correct": "Lemons and oranges (Fête du Citron)",
        "distractors": ["Apples and pears", "Grapes and plums", "Pineapples and bananas"],
        "d": 2
    },
    {
        "q": "What bizarre water sport is the headline event at the biennial Chinchilla Melon Festival in Queensland, Australia?",
        "correct": "Melon skiing (strapping hollowed-out watermelons to your feet and sliding across a slippery tarp)",
        "distractors": ["Melon canoeing through whitewater rapids", "Melon bowling down a sand dune", "Melon scuba diving in a beer tank"],
        "d": 2
    },
    {
        "q": "In which German state does the annual spring 'Spargelzeit' (asparagus season) trigger nationwide celebrations, festivals, and specialized restaurant menus dedicated to white asparagus?",
        "correct": "Baden-Württemberg, Lower Saxony, and across Germany",
        "distractors": ["Tyrol", "Alsace", "Wallonia"],
        "d": 2
    },
    {
        "q": "Which fruit festival in the Okanagan Valley of British Columbia celebrates the regional harvest with fruit pie competitions and parades?",
        "correct": "Penticton Peach Festival (Peach Fest)",
        "distractors": ["Kelowna Cherry Carnival", "Vancouver Apple Fair", "Victoria Berry Jubilee"],
        "d": 3
    },
    {
        "q": "What Ohio city calls itself the 'Bratwurst and Sauerkraut Capital' and hosts an annual Ohio Sauerkraut Festival drawing over 300,000 visitors to Waynesville?",
        "correct": "Waynesville",
        "distractors": ["Akron", "Canton", "Sandusky"],
        "d": 3
    },
    {
        "q": "What West African fruit contains the glycoprotein miraculin, which temporarily alters taste buds so that sour foods taste intensely sweet?",
        "correct": "Miracle fruit (Synsepalum dulcificum)",
        "distractors": ["Monk fruit", "Ackee", "Baobab fruit"],
        "d": 1
    },
    {
        "q": "How does the protein miraculin from the miracle berry work biochemically on human taste buds?",
        "correct": "It binds to sweetness receptors (hT1R2-hT1R3) and activates them specifically when exposed to low, acidic pH",
        "distractors": ["It numbs sour taste buds completely while injecting fructose into saliva", "It dissolves the tongue's outer cuticle so sugar can be absorbed faster", "It converts saliva into sucrose solution through catalytic synthesis"],
        "d": 3
    },
    {
        "q": "Which Chinese fruit, also known as Luo Han Guo, contains sweet mogrosides roughly 250 times sweeter than table sugar with zero calories?",
        "correct": "Monk fruit (Siraitia grosvenorii)",
        "distractors": ["Goji berry", "Jujube", "Lychee"],
        "d": 2
    },
    {
        "q": "What is the primary natural zero-calorie sweetener extracted from the leaves of the South American plant Stevia rebaudiana?",
        "correct": "Steviol glycosides (such as Stevioside and Rebaudioside A)",
        "distractors": ["Aspartame", "Sucralose", "Saccharin"],
        "d": 2
    },
    {
        "q": "What Roman statesman and author of 'De Agri Cultura' wrote passionately that cabbage was the greatest of all vegetables, curing every human disease?",
        "correct": "Cato the Elder",
        "distractors": ["Julius Caesar", "Cicero", "Pliny the Younger"],
        "d": 2
    },
    {
        "q": "According to ancient accounts by Pliny the Elder, which Roman Emperor was obsessed with eating leeks every day to preserve and strengthen his singing voice?",
        "correct": "Nero",
        "distractors": ["Augustus", "Caligula", "Commodus"],
        "d": 2
    },
    {
        "q": "What nickname was given to Roman Emperor Nero by mocking citizens due to his daily diet of leeks with oil?",
        "correct": "Porrophagus (Leek-eater)",
        "distractors": ["Cabbagemonger", "Onion-breather", "The Radish King"],
        "d": 3
    },
    {
        "q": "In Greek mythology, what golden fruit, inscribed 'To the Fairest' by the goddess Eris, sparked the rivalry that led to the Trojan War?",
        "correct": "The Apple of Discord",
        "distractors": ["The Pomegranate of the Underworld", "The Golden Pear of Hera", "The Fig of Olympus"],
        "d": 1
    },
    {
        "q": "In Greek mythology, Hades deceived Persephone into remaining in the Underworld for part of each year by getting her to eat seeds of which fruit?",
        "correct": "Pomegranate",
        "distractors": ["Apple", "Fig", "Grape"],
        "d": 1
    },

    # 86-100: Folklore, Myths & Popular Culture (d1-d3)
    {
        "q": "What English proverb recommending daily fruit consumption first appeared in 1866 as a Welsh saying: 'Eat an apple on going to bed, and you'll keep the doctor from earning his bread'?",
        "correct": "An apple a day keeps the doctor away",
        "distractors": ["A bad apple spoils the bunch", "The apple doesn't fall far from the tree", "Forbidden fruit tastes sweetest"],
        "d": 1
    },
    {
        "q": "At which historic English country manor did Sir Isaac Newton observe a falling apple that allegedly helped inspire his universal law of gravitation?",
        "correct": "Woolsthorpe Manor",
        "distractors": ["Blenheim Palace", "Highclere Castle", "Chatsworth House"],
        "d": 2
    },
    {
        "q": "What specific heritage apple cultivar was the tree at Woolsthorpe Manor that inspired Sir Isaac Newton?",
        "correct": "Flower of Kent",
        "distractors": ["Cox's Orange Pippin", "Bramley's Seedling", "Ribston Pippin"],
        "d": 3
    },
    {
        "q": "In the Brothers Grimm fairy tale, what poisoned fruit does the wicked queen offer to Snow White?",
        "correct": "Apple",
        "distractors": ["Peach", "Plum", "Pear"],
        "d": 1
    },
    {
        "q": "In the fairy tale Cinderella, the Fairy Godmother famously transforms which garden vegetable into a magnificent royal carriage?",
        "correct": "Pumpkin",
        "distractors": ["Watermelon", "Gourd", "Butternut squash"],
        "d": 1
    },
    {
        "q": "In the traditional English nursery rhyme, what fruit did Little Jack Horner pull out of his Christmas pie with his thumb?",
        "correct": "Plum",
        "distractors": ["Cherry", "Fig", "Currant"],
        "d": 1
    },
    {
        "q": "What classic American cartoon sailor derived superhuman strength by downing a can of spinach?",
        "correct": "Popeye the Sailor",
        "distractors": ["Bluto", "Captain Caveman", "Underdog"],
        "d": 1
    },
    {
        "q": "What persistent myth explains why spinach was originally believed to have ten times more iron than it actually contains?",
        "correct": "A German chemist in 1870 misplaced a decimal point when transcribing spinach's iron content in a notebook",
        "distractors": ["A deliberate marketing conspiracy by the US Canning Syndicate", "Spinach grown near iron mines absorbed metallic ore", "Popeye cartoonists forged laboratory records to secure sponsorships"],
        "d": 2
    },
    {
        "q": "What fruit was originally named the 'Chinese gooseberry' before New Zealand marketers rebranded it in 1959 to boost global export appeal?",
        "correct": "Kiwifruit",
        "distractors": ["Passion fruit", "Dragon fruit", "Starfruit"],
        "d": 1
    },
    {
        "q": "Why did New Zealand exporters select the name 'Kiwifruit' for the Chinese gooseberry in 1959?",
        "correct": "Its small, fuzzy brown exterior bore a striking resemblance to New Zealand's native flightless Kiwi bird",
        "distractors": ["Kiwi birds feed exclusively on the fruit in native forests", "The fruit was discovered on Mount Kiwi in South Island", "Kiwi was the Maori word for sweet emerald pulp"],
        "d": 1
    },
    {
        "q": "What is the national vegetable of Wales, worn proudly on St. David's Day on March 1?",
        "correct": "Leek",
        "distractors": ["Parsnip", "Cabbage", "Turnip"],
        "d": 1
    },
    {
        "q": "According to legend, why do Welsh soldiers wear a leek in their caps to commemorate victory over Saxon invaders in the 6th century?",
        "correct": "Saint David advised Welsh warriors to wear leeks from a garden field in their helmets to identify each other during battle",
        "distractors": ["The smell of raw leeks blinded Saxon war horses", "King Arthur carried a sacred golden leek into battle", "Leek soup was the only food available during a 40-day siege"],
        "d": 2
    },
    {
        "q": "In Jewish tradition on Rosh Hashanah, what fruit is eaten because its many seeds are traditionally said to symbolize the 613 mitzvot (commandments) of the Torah?",
        "correct": "Pomegranate",
        "distractors": ["Fig", "Date", "Olive"],
        "d": 1
    },
    {
        "q": "Which fruit is featured alongside the date, grape, fig, and olive as the 'Seven Species' of agricultural produce listed in the Hebrew Bible?",
        "correct": "Pomegranate",
        "distractors": ["Apple", "Orange", "Peach"],
        "d": 2
    },
    {
        "q": "What traditional Halloween custom, popular in the UK and Ireland before pumpkins became widespread, involved carving scary faces into which root vegetable?",
        "correct": "Turnip (or Rutabaga)",
        "distractors": ["Potato", "Beetroot", "Parsnip"],
        "d": 1
    }
]

if __name__ == "__main__":
    build_batch(BATCH_5, "tools/staging/produce_batch5.json", batch_num=5)
