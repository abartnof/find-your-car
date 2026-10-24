#!/usr/bin/env python3
"""
Generate Batch 4 of Fruits & Veggies trivia (100 questions):
Culinary, Spices, Global Agriculture Statistics & Processing.
Target: ~30 d1, ~40 d2, ~30 d3.
"""

from produce_batch_builder import build_batch

BATCH_4 = [
    # 1-20: Global Agriculture Leaders & Crop Statistics (d1-d3)
    {
        "q": "Which European nation is the world's largest producer of olive oil, accounting for roughly 40% to 50% of global supply?",
        "correct": "Spain",
        "distractors": ["Italy", "Greece", "Portugal"],
        "d": 1
    },
    {
        "q": "Which Spanish province in Andalusia produces more olive oil than the entire country of Italy combined?",
        "correct": "Jaén",
        "distractors": ["Seville", "Granada", "Córdoba"],
        "d": 3
    },
    {
        "q": "Which country is by far the world's largest producer of fresh apples, producing roughly half of the global harvest?",
        "correct": "China",
        "distractors": ["United States", "Poland", "Turkey"],
        "d": 2
    },
    {
        "q": "Which U.S. state produces over 70% of all commercially grown fresh-market apples in the United States?",
        "correct": "Washington",
        "distractors": ["New York", "Michigan", "Pennsylvania"],
        "d": 2
    },
    {
        "q": "Which country produces over 40% of the world's total supply of mangoes?",
        "correct": "India",
        "distractors": ["Mexico", "Thailand", "Brazil"],
        "d": 1
    },
    {
        "q": "Which prized Indian mango cultivar, often dubbed the 'King of Mangoes', is renowned for its saffron sweetness and thin skin?",
        "correct": "Alphonso (Hapus)",
        "distractors": ["Kesar", "Ataulfo", "Kent"],
        "d": 3
    },
    {
        "q": "Which South American nation is the world's leading exporter of fresh bananas?",
        "correct": "Ecuador",
        "distractors": ["Colombia", "Costa Rica", "Brazil"],
        "d": 3
    },
    {
        "q": "Which African island nation produces approximately 80% of the world's commercial Bourbon vanilla?",
        "correct": "Madagascar",
        "distractors": ["Mauritius", "Seychelles", "Comoros"],
        "d": 2
    },
    {
        "q": "Which country produces over 70% of the world's commercial garlic supply?",
        "correct": "China",
        "distractors": ["Spain", "South Korea", "Egypt"],
        "d": 1
    },
    {
        "q": "Which country is the leading producer of both potatoes and fresh tomatoes worldwide?",
        "correct": "China",
        "distractors": ["Russia", "India", "United States"],
        "d": 2
    },
    {
        "q": "Which U.S. state produces more than 90% of the country's processed tomatoes used in tomato paste, ketchup, and canned sauces?",
        "correct": "California (Central Valley)",
        "distractors": ["Florida", "Ohio", "New Jersey"],
        "d": 2
    },
    {
        "q": "Which state's Central Valley grows roughly 80% of the world's commercial almond crop?",
        "correct": "California",
        "distractors": ["Texas", "Arizona", "Georgia"],
        "d": 1
    },
    {
        "q": "What California coastal town bills itself as the 'Artichoke Center of the World' and named Marilyn Monroe its first Artichoke Queen in 1948?",
        "correct": "Castroville",
        "distractors": ["Half Moon Bay", "Gilroy", "Watsonville"],
        "d": 2
    },
    {
        "q": "What California city hosts an annual summer festival celebrating its reputation as the 'Garlic Capital of the World'?",
        "correct": "Gilroy",
        "distractors": ["Modesto", "Fresno", "Bakersfield"],
        "d": 1
    },
    {
        "q": "Which West African nation is the world's largest producer and exporter of cocoa beans?",
        "correct": "Ivory Coast (Côte d'Ivoire)",
        "distractors": ["Ghana", "Nigeria", "Cameroon"],
        "d": 1
    },
    {
        "q": "Which South American country is the world's largest producer of coffee beans?",
        "correct": "Brazil",
        "distractors": ["Colombia", "Vietnam", "Ethiopia"],
        "d": 1
    },
    {
        "q": "Which Canadian province produces more than 70% of the global supply of pure maple syrup?",
        "correct": "Quebec",
        "distractors": ["Ontario", "New Brunswick", "Nova Scotia"],
        "d": 1
    },
    {
        "q": "Which native North American tree species is primarily tapped for its high-sugar sap to produce commercial maple syrup?",
        "correct": "Sugar maple (Acer saccharum)",
        "distractors": ["Red maple (Acer rubrum)", "Silver maple (Acer saccharinum)", "Box elder (Acer negundo)"],
        "d": 3
    },
    {
        "q": "How many gallons of raw maple sap are typically boiled down to produce a single gallon of finished maple syrup?",
        "correct": "Approximately 40 gallons",
        "distractors": ["Approximately 5 gallons", "Approximately 12 gallons", "Approximately 100 gallons"],
        "d": 2
    },
    {
        "q": "Which sweet onion variety is legally protected and must be grown in specific low-sulfur soils across 20 counties in Georgia?",
        "correct": "Vidalia onion",
        "distractors": ["Walla Walla sweet onion", "Maui onion", "Texas 1015 onion"],
        "d": 1
    },

    # 21-45: Botanical Spices & Aromatics (d1-d3)
    {
        "q": "Which spice is the most expensive culinary spice in the world by weight?",
        "correct": "Saffron",
        "distractors": ["Vanilla", "Cardamom", "True cinnamon"],
        "d": 2
    },
    {
        "q": "Saffron consists of the hand-harvested dried stigmas of which purple-flowering autumn plant?",
        "correct": "Crocus sativus",
        "distractors": ["Colchicum autumnale", "Iris germanica", "Lilium candidum"],
        "d": 2
    },
    {
        "q": "Roughly how many Crocus sativus flowers must be harvested by hand to yield a single pound of dried saffron threads?",
        "correct": "Around 75,000 flowers",
        "distractors": ["Around 500 flowers", "Around 5,000 flowers", "Around 1,000,000 flowers"],
        "d": 3
    },
    {
        "q": "Which chemical compound is primarily responsible for the brilliant golden-yellow color saffron imparts to rice dishes?",
        "correct": "Crocin",
        "distractors": ["Safranal", "Curcumin", "Picrocrocin"],
        "d": 3
    },
    {
        "q": "The vanilla bean is botanically the cured seed capsule of an epiphytic climbing vine belonging to which plant family?",
        "correct": "Orchidaceae (Orchid family)",
        "distractors": ["Fabaceae (Legume family)", "Solanaceae (Nightshade family)", "Piperaceae (Pepper family)"],
        "d": 3
    },
    {
        "q": "What is the primary organic aromatic aldehyde that gives cured vanilla beans their characteristic warm flavor?",
        "correct": "Vanillin",
        "distractors": ["Cinnamaldehyde", "Eugenol", "Thymol"],
        "d": 3
    },
    {
        "q": "Black, green, and white peppercorns all originate from which climbing vine species?",
        "correct": "Piper nigrum",
        "distractors": ["Capsicum annuum", "Schinus molle", "Zanthoxylum piperitum"],
        "d": 2
    },
    {
        "q": "How is white pepper produced from the Piper nigrum plant?",
        "correct": "Fully ripe red berries are soaked in water to ferment and scrub off the outer dark fruit skin",
        "distractors": ["Unripe berries are bleached in sulfur dioxide vapor", "Berries are harvested from an albino variety", "Berries are dried under intense ultraviolet lamps"],
        "d": 2
    },
    {
        "q": "What crystalline alkaloid gives black pepper its characteristic pungent, biting heat?",
        "correct": "Piperine",
        "distractors": ["Capsaicin", "Sinigrin", "Menthol"],
        "d": 3
    },
    {
        "q": "Pink peppercorns are not true peppercorns, but rather the dried berries of which tree, carrying allergy risks for people with cashew allergies?",
        "correct": "Brazilian pepper tree (Schinus terebinthifolia)",
        "distractors": ["Tasmanian mountain pepper", "Sichuan prickly ash", "Jamaican pimenta tree"],
        "d": 3
    },
    {
        "q": "What tingling, buzzing, and numbing sensation is produced on the lips and tongue by Sichuan peppercorns?",
        "correct": "Paresthesia caused by hydroxy-alpha-sanshool",
        "distractors": ["Burning inflammation caused by capsaicin", "Sour puckering caused by acetic acid", "Cold numbness caused by synthetic menthol"],
        "d": 3
    },
    {
        "q": "Which plant family do Sichuan peppercorns botanically belong to, sharing close ties to lemons and oranges?",
        "correct": "Rutaceae (Citrus family)",
        "distractors": ["Piperaceae", "Solanaceae", "Myrtaceae"],
        "d": 3
    },
    {
        "q": "True cinnamon ('Ceylon cinnamon') is harvested from the paper-thin inner bark of which botanical species?",
        "correct": "Cinnamomum verum",
        "distractors": ["Cinnamomum cassia", "Cinnamomum loureiroi", "Cinnamomum burmannii"],
        "d": 3
    },
    {
        "q": "Common cassia cinnamon contains significantly higher levels of which natural organic compound that can cause liver damage in high doses?",
        "correct": "Coumarin",
        "distractors": ["Safrole", "Oxalic acid", "Myristicin"],
        "d": 3
    },
    {
        "q": "Cloves are botanically what part of the tropical evergreen tree Syzygium aromaticum?",
        "correct": "Unopened, dried flower buds",
        "distractors": ["Dried berry stones", "Flakes of aromatic bark", "Swollen subterranean corms"],
        "d": 3
    },
    {
        "q": "Which aromatic phenol gives cloves their distinct warm aroma and is widely used in dental medicine as a mild local anesthetic?",
        "correct": "Eugenol",
        "distractors": ["Thymol", "Carvacrol", "Borneol"],
        "d": 3
    },
    {
        "q": "Nutmeg and mace both come from the fruit of the Myristica fragrans tree. What part of the fruit is mace?",
        "correct": "The bright red, lacy aril (netting) that encases the hard seed",
        "distractors": ["The ground inner kernel of the seed", "The dried outer fibrous husk", "The dried flower petals"],
        "d": 3
    },
    {
        "q": "What natural psychoactive and anticholinergic compound present in nutmeg can cause hallucinations and illness if consumed in large quantities?",
        "correct": "Myristicin",
        "distractors": ["Theobromine", "Scopolamine", "Psilocybin"],
        "d": 3
    },
    {
        "q": "What spice, made from the dried unripe berries of Pimenta dioica, was named because its flavor resembles cinnamon, nutmeg, and clove combined?",
        "correct": "Allspice",
        "distractors": ["Five-spice", "Garam masala", "Ras el hanout"],
        "d": 2
    },
    {
        "q": "Which star-shaped spice pericarp contains anethole and is a primary natural botanical source of shikimic acid, used to manufacture the antiviral drug Tamiflu?",
        "correct": "Star anise (Illicium verum)",
        "distractors": ["Green cardamom", "Black cumin", "Juniper berry"],
        "d": 3
    },
    {
        "q": "Cardamom belongs to which botanical plant family, known for aromatic rhizomes like ginger and turmeric?",
        "correct": "Zingiberaceae",
        "distractors": ["Orchidaceae", "Apiaceae", "Lauraceae"],
        "d": 3
    },
    {
        "q": "What bright yellow polyphenolic pigment in turmeric rhizomes is celebrated for its culinary color and anti-inflammatory properties?",
        "correct": "Curcumin",
        "distractors": ["Lutein", "Crocin", "Capsanthin"],
        "d": 1
    },
    {
        "q": "True Japanese wasabi (Eutrema japonicum) is traditionally grated on a textured wooden paddle covered in what material?",
        "correct": "Sharkskin (or rayskin)",
        "distractors": ["Copper wire mesh", "Pumice stone", "Obsidian glass"],
        "d": 3
    },
    {
        "q": "Why is true freshly grated wasabi paste typically consumed within 15 to 20 minutes of preparation?",
        "correct": "Its pungent volatile isothiocyanates oxidize and evaporate rapidly once cells are ruptured",
        "distractors": ["It turns black and toxic upon prolonged exposure to room air", "It absorbs water and liquefies into a tasteless slime", "It rapidly ferments into vinegar"],
        "d": 3
    },
    {
        "q": "Most green 'wasabi' served in Western sushi restaurants is actually a mixture of food coloring, mustard flour, and what root?",
        "correct": "Horseradish (Armoracia rusticana)",
        "distractors": ["Daikon radish", "Parsnip", "Ginger root"],
        "d": 1
    },

    # 46-65: Culinary Produce & Specialty Botany (d1-d3)
    {
        "q": "What is the culinary term for vegetables like carrots, celery, and onions slowly cooked in fat as an aromatic flavor base in French cooking?",
        "correct": "Mirepoix",
        "distractors": ["Bouquet garni", "Roux", "Remoulade"],
        "d": 1
    },
    {
        "q": "In Cajun and Creole cooking, the 'Holy Trinity' of aromatics replaces French mirepoix's carrots with which vegetable?",
        "correct": "Green bell pepper",
        "distractors": ["Okra", "Garlic", "Turnip"],
        "d": 1
    },
    {
        "q": "What botanical phenomenon describes flowers and fruits developing directly from the main trunk or mature woody branches rather than leafy twigs?",
        "correct": "Cauliflory",
        "distractors": ["Geocarpy", "Heterostyly", "Apomixis"],
        "d": 3
    },
    {
        "q": "Which of the following commercially harvested tree crops exhibits prominent cauliflory, with large pods growing straight from the trunk?",
        "correct": "Cacao (Theobroma cacao)",
        "distractors": ["Sweet orange", "Almond", "Peach"],
        "d": 3
    },
    {
        "q": "The Brazilian grape tree (Jabuticaba) is famous for what dramatic visual botanical trait?",
        "correct": "Purplish-black grape-like fruits that encase the entire woody tree trunk",
        "distractors": ["Leaves that change color every hour of daylight", "Underground berries that grow beneath stones", "Fruits that detonate like popcorn when ripe"],
        "d": 2
    },
    {
        "q": "What is the botanical difference between culinary herbs and spices?",
        "correct": "Herbs are the fresh or dried leaves of herbaceous plants, while spices come from seeds, bark, roots, fruits, or flowers",
        "distractors": ["Herbs are always sweet while spices are always savory", "Spices are exclusively grown in temperate climates", "Herbs must be consumed raw while spices must be boiled"],
        "d": 1
    },
    {
        "q": "Cilantro and coriander come from the exact same botanical plant (Coriandrum sativum). In North American culinary parlance, what is the distinction?",
        "correct": "Cilantro refers to the fresh leafy green herb, while coriander refers to the dried spherical seeds",
        "distractors": ["Cilantro is the raw root while coriander is the processed leaf", "Coriander is genetically modified cilantro", "Cilantro is grown in winter while coriander is harvested in summer"],
        "d": 1
    },
    {
        "q": "Why does fresh cilantro taste soapy and unpleasant to a distinct percentage of the human population?",
        "correct": "A variation in an olfactory receptor gene (OR6A2) allows detection of soap-like aldehyde compounds",
        "distractors": ["Residual alkaline dish detergent absorbed during commercial washing", "A genetic inability to digest chlorophyll", "An allergic response to plant histamines"],
        "d": 2
    },
    {
        "q": "What botanical family do mint, basil, rosemary, oregano, thyme, and sage belong to, known for square stems and aromatic foliage?",
        "correct": "Lamiaceae (Labiatae)",
        "distractors": ["Apiaceae", "Brassicaceae", "Solanaceae"],
        "d": 2
    },
    {
        "q": "Bay leaves used to flavor soups and braises are harvested from which Mediterranean evergreen tree?",
        "correct": "Laurus nobilis (Sweet bay)",
        "distractors": ["Ficus carica", "Olea europaea", "Pistacia lentiscus"],
        "d": 1
    },
    {
        "q": "Why are dried bay leaves almost universally removed from stews and stocks before serving?",
        "correct": "They remain rigid and sharp after cooking, posing a choking and gastrointestinal laceration hazard",
        "distractors": ["They turn deadly toxic if kept in liquid longer than an hour", "They dissolve into bitter black sludge if chewed", "They emit intense radioactive isotopes upon cooling"],
        "d": 1
    },
    {
        "q": "Tamarind pods are prized in cuisines of India, Southeast Asia, and Latin America primarily for which taste component?",
        "correct": "Sharp sourness provided by high concentrations of natural tartaric acid",
        "distractors": ["Intense numbness from eugenol", "Heavy bitter astringency from caffeine", "Fiery heat from capsaicinoids"],
        "d": 2
    },
    {
        "q": "What coarse, deep red powder with a tangy lemon flavor is made from ground wild berries of a shrub in the family Anacardiaceae?",
        "correct": "Sumac",
        "distractors": ["Paprika", "Cayenne", "Annatto"],
        "d": 2
    },
    {
        "q": "What reddish-orange natural food coloring and spice, also known as achiote, is extracted from the seeds of the tropical Bixa orellana tree?",
        "correct": "Annatto",
        "distractors": ["Saffron", "Turmeric", "Paprika"],
        "d": 2
    },
    {
        "q": "What botanical structure is grated or steeped to flavor Italian gin, distinct as a modified fleshy seed cone of a conifer?",
        "correct": "Juniper berry",
        "distractors": ["Yew aril", "Cypress nut", "Pine kernel"],
        "d": 2
    },
    {
        "q": "What highly prized subterranean culinary fungi grow in mycorrhizal symbiosis with the roots of oak and hazel trees?",
        "correct": "Truffles",
        "distractors": ["Morels", "Chanterelles", "Shiitake"],
        "d": 1
    },
    {
        "q": "Which Italian city in Piedmont is world-renowned for its annual autumn auction of prized white truffles (Tuber magnatum)?",
        "correct": "Alba",
        "distractors": ["Modena", "Parma", "Bologna"],
        "d": 2
    },
    {
        "q": "What volatile steroid compound present in truffles is identical to a pheromone in pig saliva, explaining why female swine naturally hunt them?",
        "correct": "Androstenol",
        "distractors": ["Estradiol", "Testosterone", "Cholesterol"],
        "d": 3
    },
    {
        "q": "Why do modern commercial truffle hunters overwhelmingly use trained dogs rather than pigs to search for truffles?",
        "correct": "Pigs tend to aggressively devour the truffles they find and damage delicate fungal mycelium in the root bed",
        "distractors": ["Dogs can smell truffles from five miles away while pigs can only smell one foot", "Pigs are banned in all European forests by wildlife authorities", "Truffle spores cause respiratory paralysis in swine"],
        "d": 1
    },
    {
        "q": "What type of vegetable is sea kale (Crambe maritima), historically prized in Victorian Britain by mounding stones or sand over shoots?",
        "correct": "A blanched halophyte (salt-tolerant coastal crucifer)",
        "distractors": ["A type of freshwater green algae", "An edible brown kelp blade", "A root lichen"],
        "d": 3
    },

    # 66-80: Fermentation, Preservation & Culinary Chemistry (d1-d3)
    {
        "q": "Sauerkraut and traditional dill pickles are preserved through which biological fermentation process?",
        "correct": "Lactic acid fermentation by beneficial bacteria (such as Leuconostoc and Lactobacillus)",
        "distractors": ["Acetic acid distillation by acetobacter", "Alcoholic fermentation by baker's yeast", "Propionic acid fermentation by molds"],
        "d": 1
    },
    {
        "q": "Why is salt kneaded into shredded cabbage when making traditional sauerkraut?",
        "correct": "It draws out cabbage juices via osmosis to create brine and inhibits spoilage bacteria while lactic acid bacteria thrive",
        "distractors": ["It chemically bleaches the chlorophyll into carotene", "It sterilizes all microorganisms so no bacteria can grow", "It hydrolyzes cellulose into simple syrup"],
        "d": 2
    },
    {
        "q": "Kimchi, the iconic Korean fermented vegetable side dish, is most commonly made using which variety of cabbage?",
        "correct": "Napa cabbage (Brassica rapa subsp. pekinensis)",
        "distractors": ["Savoy cabbage", "Red cabbage", "Green cannonball cabbage"],
        "d": 1
    },
    {
        "q": "What Korean sun-dried chili pepper powder is the foundational seasoning in traditional kimchi?",
        "correct": "Gochugaru",
        "distractors": ["Shichimi", "Paprika", "Piri piri"],
        "d": 2
    },
    {
        "q": "Traditional balsamic vinegar of Modena (Aceto Balsamico Tradizionale) is produced by aging cooked grape must for a minimum of how long in wooden barrels?",
        "correct": "12 years",
        "distractors": ["6 months", "2 years", "50 years"],
        "d": 2
    },
    {
        "q": "What polysaccharide extracted from citrus peels and apple pomace forms the essential gelling agent in fruit jams and jellies?",
        "correct": "Pectin",
        "distractors": ["Gelatin", "Agar-agar", "Guar gum"],
        "d": 1
    },
    {
        "q": "High-methoxyl commercial pectin requires which two conditions to form a stable gel in fruit preserves?",
        "correct": "High sugar concentration (around 60%) and an acidic pH (around 3.0 to 3.5)",
        "distractors": ["Sub-zero freezing and intense ultrasound vibration", "Complete absence of sugar and highly alkaline pH", "Boiling under high pressure with dissolved calcium chloride"],
        "d": 3
    },
    {
        "q": "Why do unripe green apples make firmer jelly than overripe soft apples?",
        "correct": "Unripe apples contain abundant protopectin and pectin, which break down into non-gelling pectic acid as the fruit overripens",
        "distractors": ["Unripe apples contain twice as much sucrose", "Overripe apples contain enzymes that dissolve glass jars", "Overripe apples have no cell walls"],
        "d": 2
    },
    {
        "q": "What traditional French preservation technique involves poaching whole fruits in increasingly concentrated sugar syrups over weeks until fully candied?",
        "correct": "Glacéing (confiture)",
        "distractors": ["En papillote", "Sous vide", "Flambéing"],
        "d": 3
    },
    {
        "q": "What dried fruit product is made by soaking whole plums in brine and drying them, popular in Mexican and Asian cuisines under names like saladitos or li hing mui?",
        "correct": "Preserved salted plum",
        "distractors": ["Dehydrated fig", "Sun-dried persimmon", "Raisin cluster"],
        "d": 2
    },
    {
        "q": "Prunes are simply dehydrated cultivars of which fruit?",
        "correct": "European plum (Prunus domestica)",
        "distractors": ["Fig", "Date", "Apricot"],
        "d": 1
    },
    {
        "q": "Raisins, sultanas, and currants are all dried varieties of which botanical fruit?",
        "correct": "Grape",
        "distractors": ["Gooseberry", "Plum", "Cranberry"],
        "d": 1
    },
    {
        "q": "Traditional Greek dried Zante currants are not true currants (Ribes), but rather tiny seedless raisins dried from which grape variety?",
        "correct": "Black Corinth grape",
        "distractors": ["Thompson Seedless", "Muscat of Alexandria", "Concord"],
        "d": 3
    },
    {
        "q": "The vast majority of commercial golden and dark raisins in the United States are made from which green seedless grape cultivar?",
        "correct": "Thompson Seedless (Sultana)",
        "distractors": ["Red Globe", "Flame Seedless", "Cotton Candy"],
        "d": 2
    },
    {
        "q": "How are golden raisins treated differently from dark sun-dried raisins to preserve their bright translucent yellow color?",
        "correct": "They are treated with sulfur dioxide gas and dried in temperature-controlled dehydrators rather than in direct sun",
        "distractors": ["They are bleached in chlorine water baths", "They are harvested from albino grapevine mutations", "They are dipped in yellow food dye"],
        "d": 2
    },

    # 81-100: Global Staple Crops & Botanical Curiosities (d1-d3)
    {
        "q": "Which staple root crop contains toxic cyanogenic glucosides (linamarin) that must be removed through peeling, grating, and thorough cooking?",
        "correct": "Cassava (bitter manioc)",
        "distractors": ["Sweet potato", "Beetroot", "Turnip"],
        "d": 2
    },
    {
        "q": "What popular chewy pearls used in bubble tea and gluten-free puddings are manufactured from purified cassava starch?",
        "correct": "Tapioca pearls",
        "distractors": ["Sago", "Arrowroot", "Polenta"],
        "d": 2
    },
    {
        "q": "Taro corms must always be thoroughly cooked before consumption because raw taro contains microscopic, needle-sharp crystals of:",
        "correct": "Calcium oxalate (raphides)",
        "distractors": ["Silicon dioxide", "Uric acid", "Potassium nitrate"],
        "d": 2
    },
    {
        "q": "What traditional Hawaiian fermented staple dish is made by steaming, mashing, and fermenting taro corms with water?",
        "correct": "Poi",
        "distractors": ["Poke", "Lau lau", "Haupia"],
        "d": 2
    },
    {
        "q": "Which fruit is famous across Southeast Asia for its spiky exterior, custard-like texture, and pungent smell likened to rotten onions and gym socks?",
        "correct": "Durian",
        "distractors": ["Jackfruit", "Rambutan", "Mangosteen"],
        "d": 1
    },
    {
        "q": "Why is the durian fruit strictly banned on public subway networks, airports, and hotels throughout Singapore and Thailand?",
        "correct": "Its volatile sulfur compounds produce an intensely lingering, pervasive odor",
        "distractors": ["Its falling fruits are classified as lethal projectiles", "Its spikes harbor venomous caterpillars", "Its sap ruins carpet dye irreversibly"],
        "d": 1
    },
    {
        "q": "What tropical fruit, covered in soft hairy red spines, takes its name from the Malay word for 'hair'?",
        "correct": "Rambutan",
        "distractors": ["Lychee", "Longan", "Durian"],
        "d": 1
    },
    {
        "q": "Which fruit with a thick purple rind and delicate white segmented segments was famously dubbed the 'Queen of Fruits' in Southeast Asia?",
        "correct": "Mangosteen (Garcinia mangostana)",
        "distractors": ["Passion fruit", "Dragon fruit", "Starfruit"],
        "d": 2
    },
    {
        "q": "According to a persistent historical legend, which British monarch offered a reward of 100 pounds sterling to anyone who could bring her a fresh mangosteen?",
        "correct": "Queen Victoria",
        "distractors": ["Queen Elizabeth I", "Queen Anne", "Queen Mary"],
        "d": 2
    },
    {
        "q": "Starfruit is botanically known by which genus, and produces distinct five-pointed star cross-sections when sliced?",
        "correct": "Averrhoa (Averrhoa carambola)",
        "distractors": ["Actinidia", "Carica", "Annona"],
        "d": 2
    },
    {
        "q": "Individuals suffering from chronic kidney disease are strictly advised to avoid eating starfruit because it contains a potent neurotoxin called:",
        "correct": "Caramboxin",
        "distractors": ["Solanine", "Amygdalin", "Myristicin"],
        "d": 3
    },
    {
        "q": "Dragon fruit (pitaya) is the edible fruit produced by climbing cultivars of which plant family?",
        "correct": "Cactaceae (Cactus family)",
        "distractors": ["Bromeliaceae", "Orchidaceae", "Arecaceae"],
        "d": 1
    },
    {
        "q": "What edible cactus pads are widely consumed in Mexican cuisine as a cooked vegetable or in salads?",
        "correct": "Nopales",
        "distractors": ["Chayote", "Jicama", "Tomatillo"],
        "d": 1
    },
    {
        "q": "What sweet, crisp Mexican root vegetable, also known as the yam bean, is traditionally peeled, sliced, and sprinkled with lime juice and chili powder?",
        "correct": "Jicama (Pachyrhizus erosus)",
        "distractors": ["Cassava", "Taro", "Malanga"],
        "d": 1
    },
    {
        "q": "Tomatillos, the essential ingredient in Mexican salsa verde, grow encased in what protective botanical structure?",
        "correct": "An inflated, papery calyx (husk)",
        "distractors": ["A thick woody exocarp", "A spiny floral bract", "A fibrous coconut-like coir"],
        "d": 2
    },
    {
        "q": "What small, sweet orange berry related to the tomatillo grows inside a delicate papery lantern husk and is also known as the ground cherry or goldenberry?",
        "correct": "Cape gooseberry (Physalis peruviana)",
        "distractors": ["Kumquat", "Sea buckthorn", "Miracle berry"],
        "d": 2
    },
    {
        "q": "The cherimoya (Annona cherimola), praised by Mark Twain as 'the most delicious fruit known to men', is colloquially called the:",
        "correct": "Custard apple",
        "distractors": ["Sugar pear", "Cream melon", "Honey peach"],
        "d": 2
    },
    {
        "q": "What large green tropical fruit with soft spines and fibrous sweet-sour pulp is also known as guanábana?",
        "correct": "Soursop (Annona muricata)",
        "distractors": ["Breadfruit", "Jackfruit", "Pawpaw"],
        "d": 2
    },
    {
        "q": "What is the largest edible tree fruit native to the temperate continental United States, possessing a custard-like flavor reminiscent of banana and mango?",
        "correct": "Pawpaw (Asimina triloba)",
        "distractors": ["Osage orange", "American persimmon", "Black walnut"],
        "d": 2
    },
    {
        "q": "Which fruit tree native to the Mediterranean produces dark brown leathery pods whose sweet pulpy seeds were anciently used as units of weight, giving us the word 'carat'?",
        "correct": "Carob tree (Ceratonia siliqua)",
        "distractors": ["Tamarind", "Mesquite", "Locust bean"],
        "d": 2
    }
]

if __name__ == "__main__":
    build_batch(BATCH_4, "tools/staging/produce_batch4.json", batch_num=4)
