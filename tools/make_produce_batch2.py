#!/usr/bin/env python3
"""
Generate Batch 2 of Fruits & Veggies trivia (100 questions):
Plant Physiology, Science, Ripening Hormones, Pollination, Biochemistry & Genetics.
Target: ~30 d1, ~40 d2, ~30 d3.
"""

from produce_batch_builder import build_batch

BATCH_2 = [
    # 1-15: Ripening & Plant Hormones (d1-d3)
    {
        "q": "Which gaseous plant hormone is primarily responsible for triggering the ripening process in climacteric fruits?",
        "correct": "Ethylene",
        "distractors": ["Auxin", "Gibberellin", "Abscisic acid"],
        "d": 1
    },
    {
        "q": "What simple chemical formula represents the fruit-ripening hormone ethylene?",
        "correct": "C2H4",
        "distractors": ["CH4", "CO2", "C2H6O"],
        "d": 2
    },
    {
        "q": "Why does placing an unripe avocado inside a paper bag with a ripe banana accelerate its softening?",
        "correct": "The banana emits ethylene gas which is trapped inside the bag",
        "distractors": ["The banana absorbs ambient moisture from the avocado skin", "The banana emits high levels of carbon monoxide", "The paper bag generates frictional thermal heat"],
        "d": 1
    },
    {
        "q": "Which category of fruits undergoes a sharp rise in respiration and ethylene production during ripening?",
        "correct": "Climacteric fruits",
        "distractors": ["Non-climacteric fruits", "Apomictic fruits", "Parthenocarpic fruits"],
        "d": 1
    },
    {
        "q": "Which of the following is a non-climacteric fruit that does NOT continue to ripen or become sweeter after being harvested?",
        "correct": "Strawberry",
        "distractors": ["Banana", "Apple", "Tomato"],
        "d": 1
    },
    {
        "q": "Which of these fruits is climacteric and can be harvested mature-green to ripen off the vine?",
        "correct": "Tomato",
        "distractors": ["Grape", "Watermelon", "Lemon"],
        "d": 1
    },
    {
        "q": "Why are citrus fruits like oranges and lemons classified as non-climacteric?",
        "correct": "They do not experience a post-harvest respiration burst or accumulate sugars after picking",
        "distractors": ["They produce excessive ethylene that destroys their peel", "Their seeds are destroyed if picked early", "They only ripen underground"],
        "d": 3
    },
    {
        "q": "Which compound is commercially applied in apple storage facilities under the trade name SmartFresh to block ethylene receptors and delay softening?",
        "correct": "1-Methylcyclopropene (1-MCP)",
        "distractors": ["Calcium carbide", "Indole-3-acetic acid", "Sodium benzoate"],
        "d": 3
    },
    {
        "q": "What agricultural practice uses low oxygen, elevated carbon dioxide, and precise chilling to store apples for up to a year?",
        "correct": "Controlled atmosphere (CA) storage",
        "distractors": ["Vacuum desiccation", "Gamma radiation preservation", "Osmotic flash curing"],
        "d": 2
    },
    {
        "q": "What enzyme breaks down pectin in the middle lamella of plant cell walls, causing fruits to soften as they ripen?",
        "correct": "Polygalacturonase",
        "distractors": ["Amylase", "Lipase", "Pepsin"],
        "d": 3
    },
    {
        "q": "During the ripening of bananas, amylase enzymes convert insoluble starch primarily into what sweet soluble sugars?",
        "correct": "Glucose, fructose, and sucrose",
        "distractors": ["Lactose and maltose", "Cellulose and lignin", "Galactose and glycogen"],
        "d": 1
    },
    {
        "q": "Which fruit continues to accumulate oil in its mesocarp rather than high concentrations of sugar as it matures?",
        "correct": "Avocado",
        "distractors": ["Peach", "Plum", "Pineapple"],
        "d": 1
    },
    {
        "q": "Why won't an avocado ripen while it remains attached to the tree?",
        "correct": "The tree transmits an inhibitor through the stem that suppresses ethylene sensitivity",
        "distractors": ["Sunlight neutralizes the sugars in the peel", "The roots draw out all internal gases", "The tree requires frost before triggering fruit maturity"],
        "d": 3
    },
    {
        "q": "Which gas was historically used by farmers to artificially trigger ripening before ethylene was scientifically identified?",
        "correct": "Kerosene lamp fumes (containing trace ethylene)",
        "distractors": ["Pure nitrogen", "Argon gas", "Sulfur hexafluoride"],
        "d": 3
    },
    {
        "q": "Which of the following fruits is climacteric?",
        "correct": "Kiwi",
        "distractors": ["Grapefruit", "Pineapple", "Blackberry"],
        "d": 2
    },

    # 16-30: Enzymatic Browning & Plant Pigments (d1-d3)
    {
        "q": "What enzyme is responsible for the rapid browning of sliced apples, bananas, and potatoes exposed to air?",
        "correct": "Polyphenol oxidase (PPO)",
        "distractors": ["Amylase", "Cellulase", "Nitrogenase"],
        "d": 2
    },
    {
        "q": "Why does sprinkling lemon juice on freshly cut apple slices prevent them from turning brown?",
        "correct": "The citric acid lowers the pH and ascorbic acid acts as an antioxidant, inhibiting polyphenol oxidase",
        "distractors": ["The sugar in lemon juice coats the surface with an airtight glaze", "Lemon juice chemically bleaches all plant pigments", "Lemon juice instantly evaporates surface moisture"],
        "d": 1
    },
    {
        "q": "Which red carotenoid pigment gives ripe tomatoes, watermelons, and pink grapefruits their distinctive color?",
        "correct": "Lycopene",
        "distractors": ["Anthocyanin", "Lutein", "Chlorophyll"],
        "d": 1
    },
    {
        "q": "Cooking tomatoes in olive oil increases the dietary absorption of lycopene because lycopene is:",
        "correct": "Fat-soluble (lipophilic)",
        "distractors": ["Water-soluble", "Destroyed by cold temperatures", "A heavy metal complex"],
        "d": 2
    },
    {
        "q": "Which provitamin A carotenoid pigment gives carrots, sweet potatoes, and butternut squash their vibrant orange color?",
        "correct": "Beta-carotene",
        "distractors": ["Betalain", "Chlorophyll b", "Zeaxanthin"],
        "d": 1
    },
    {
        "q": "Water-soluble flavonoid pigments responsible for the red, purple, and blue hues in blueberries, blackberries, and red cabbage are called:",
        "correct": "Anthocyanins",
        "distractors": ["Carotenoids", "Betalains", "Chlorophylls"],
        "d": 2
    },
    {
        "q": "How does red cabbage juice behave when mixed with an acidic solution like vinegar?",
        "correct": "It turns bright pink or red",
        "distractors": ["It turns deep blue or green", "It turns completely clear", "It turns murky brown"],
        "d": 2
    },
    {
        "q": "What unique class of nitrogen-containing pigments gives red beets and Swiss chard their deep crimson color?",
        "correct": "Betalains",
        "distractors": ["Anthocyanins", "Carotenes", "Xanthophylls"],
        "d": 3
    },
    {
        "q": "What harmless condition causes a person's urine to turn pink or red after eating a large serving of beets?",
        "correct": "Beeturia",
        "distractors": ["Carotenodermia", "Solanism", "Hypercalcemia"],
        "d": 2
    },
    {
        "q": "Excessive consumption of carrots and pumpkins can cause a harmless yellow-orange tint on the skin known as:",
        "correct": "Carotenodermia",
        "distractors": ["Jaundice", "Argyria", "Cyanosis"],
        "d": 2
    },
    {
        "q": "What green photosynthetic pigment breaks down during ripening, allowing underlying yellow, orange, and red pigments to show?",
        "correct": "Chlorophyll",
        "distractors": ["Hemoglobin", "Melanin", "Flavone"],
        "d": 1
    },
    {
        "q": "The yellow pigment that gives sweet corn and yellow bell peppers their sunny color belongs primarily to which xanthophyll class?",
        "correct": "Lutein and zeaxanthin",
        "distractors": ["Betanin", "Porphyrin", "Anthocyanin"],
        "d": 3
    },
    {
        "q": "Genetically modified 'Arctic Apples' resist browning when cut because scientists used RNA interference to suppress which enzyme?",
        "correct": "Polyphenol oxidase",
        "distractors": ["Pectinase", "Sucrose synthase", "Catalase"],
        "d": 3
    },
    {
        "q": "Why does blanching vegetables in boiling water before freezing preserve their bright color and texture?",
        "correct": "The heat denatures enzymes that cause degradation and browning",
        "distractors": ["It dissolves outer cuticle waxes entirely", "It saturates cells with nitrogen gas", "It caramelizes surface starches into protective enamel"],
        "d": 2
    },
    {
        "q": "What compound in blueberries and purple sweet potatoes is widely studied for its potent antioxidant flavonoid activity?",
        "correct": "Anthocyanin",
        "distractors": ["Oxalic acid", "Capsaicin", "Solanine"],
        "d": 1
    },

    # 31-45: Sulfur Chemistry & Pungency (d1-d3)
    {
        "q": "What chemical compound is released when cutting an onion that reacts with moisture in the eyes to produce tears?",
        "correct": "Syn-propanethial-S-oxide (lachrymatory factor)",
        "distractors": ["Allyl isothiocyanate", "Capsaicin", "Acetic acid"],
        "d": 2
    },
    {
        "q": "Which enzyme converts sulfoxides into the lachrymatory factor that makes people cry when slicing onions?",
        "correct": "Lachrymatory factor synthase (LFS)",
        "distractors": ["Alliinase", "Myrosinase", "Lipoxygenase"],
        "d": 3
    },
    {
        "q": "Why does chilling an onion in the refrigerator before cutting reduce tear production?",
        "correct": "Lower temperature slows down enzymatic reaction rates and reduces vapor volatility",
        "distractors": ["Freezing temperature converts sulfur into solid inert crystals", "Cold air neutralizes all cellular water", "The cold destroys the onion's allicin permanently"],
        "d": 1
    },
    {
        "q": "In intact garlic cloves, the amino acid alliin is kept separate from which enzyme until the cloves are crushed or chopped?",
        "correct": "Alliinase",
        "distractors": ["Amylase", "Bromelain", "Papain"],
        "d": 3
    },
    {
        "q": "What potent antimicrobial organosulfur compound is formed when alliin is catalyzed by alliinase in crushed garlic?",
        "correct": "Allicin",
        "distractors": ["Curcumin", "Resveratrol", "Piperine"],
        "d": 2
    },
    {
        "q": "What pungent chemical gives freshly grated horseradish and wasabi their sharp, nasal-clearing bite?",
        "correct": "Allyl isothiocyanate",
        "distractors": ["Capsaicin", "Menthol", "Cinnamaldehyde"],
        "d": 2
    },
    {
        "q": "Why does the sharp kick of wasabi strike the nasal passages immediately, unlike the burning heat of chili peppers on the tongue?",
        "correct": "Isothiocyanates are highly volatile vapors that stimulate TRPA1 receptors in the nasal cavity",
        "distractors": ["Wasabi contains acidic vapors that dissolve nasal mucus instantly", "Wasabi binds exclusively to olfactory smell nerves rather than taste buds", "Wasabi produces microscopic sparks upon oxidation"],
        "d": 3
    },
    {
        "q": "Which botanical plant family is famous for producing sulfurous glucosinolates that convert to pungent isothiocyanates?",
        "correct": "Brassicaceae (Cruciferae)",
        "distractors": ["Rosaceae", "Cucurbitaceae", "Asteraceae"],
        "d": 1
    },
    {
        "q": "Why does cooked garlic taste sweet and nutty rather than sharp and pungent?",
        "correct": "Heat denatures alliinase before allicin can form, and caramelizes natural sugars",
        "distractors": ["Cooking replaces sulfur atoms with carbon dioxide", "Cooking converts allicin directly into capsanthin", "Heat causes garlic cloves to ferment into alcohol"],
        "d": 2
    },
    {
        "q": "What organosulfur metabolite excreted in urine after eating asparagus causes its distinct sulfurous odor?",
        "correct": "Asparagusic acid metabolites (such as methanethiol and dimethyl sulfide)",
        "distractors": ["Uric acid stones", "Bilirubin crystals", "Hippuric acid"],
        "d": 3
    },
    {
        "q": "Why can only a portion of the human population smell the characteristic odor in urine after eating asparagus?",
        "correct": "A genetic polymorphism in olfactory receptor genes determines the ability to detect it",
        "distractors": ["Only blood type O individuals metabolize asparagus into sulfur", "Age completely eliminates the digestive enzymes required", "Only people with diabetes produce the odor"],
        "d": 3
    },
    {
        "q": "Which compound is primarily responsible for the distinctive earthy aroma of garden soil and freshly dug beets?",
        "correct": "Geosmin",
        "distractors": ["Limonene", "Eugenol", "Vanillin"],
        "d": 1
    },
    {
        "q": "What volatile compound gives freshly crushed cucumber its classic cooling green aroma?",
        "correct": "(E,Z)-3,6-nonadien-1-ol (cucumber aldehyde)",
        "distractors": ["Methyl salicylate", "Benzaldehyde", "Ethyl butyrate"],
        "d": 3
    },
    {
        "q": "What causes the bitter taste in lettuce that has 'bolted' in warm weather?",
        "correct": "Accumulation of sesquiterpene lactones in the milky latex",
        "distractors": ["High concentrations of starch", "Conversion of glucose into oxalic acid", "Infestation by symbiotic rhizobia"],
        "d": 3
    },
    {
        "q": "What term describes a leafy vegetable prematurely producing a flowering stem and going to seed due to heat or day length?",
        "correct": "Bolting",
        "distractors": ["Bletting", "Etiolation", "Tillering"],
        "d": 1
    },

    # 46-60: Pollination & Reproductive Biology (d1-d3)
    {
        "q": "What insect is required to pollinate Smyrna figs in the wild through a specialized obligate mutualism?",
        "correct": "Fig wasp (Blastophaga psenes)",
        "distractors": ["Honeybee", "Bumblebee", "Hoverfly"],
        "d": 2
    },
    {
        "q": "What enzyme inside a ripening fig digests the body of the tiny pollinating fig wasp so no insect remains?",
        "correct": "Ficin",
        "distractors": ["Papain", "Pepsin", "Amylase"],
        "d": 3
    },
    {
        "q": "How must vanilla orchid flowers be pollinated on commercial plantations outside of their native Mexico?",
        "correct": "By hand using a small bamboo splinter or needle",
        "distractors": ["Using motorized acoustic leaf blowers", "By releasing swarms of imported European honeybees", "By dusting pollen through aircraft sprinklers"],
        "d": 1
    },
    {
        "q": "Who was the 12-year-old enslaved boy on the island of Réunion who revolutionized vanilla production in 1841 by inventing practical hand-pollination?",
        "correct": "Edmond Albius",
        "distractors": ["Toussaint Louverture", "Henri Christophe", "Aimé Césaire"],
        "d": 2
    },
    {
        "q": "Which native Mexican bee is the primary natural pollinator of the vanilla orchid?",
        "correct": "Melipona bee",
        "distractors": ["Africanized killer bee", "Leafcutter bee", "Carpenter bee"],
        "d": 3
    },
    {
        "q": "What term describes plant species like asparagus and kiwifruit where individual plants are strictly male or female?",
        "correct": "Dioecious",
        "distractors": ["Monoecious", "Hermaphroditic", "Parthenocarpic"],
        "d": 1
    },
    {
        "q": "Why do commercial asparagus growers strongly prefer planting all-male hybrids over female crowns?",
        "correct": "Male plants produce higher yields of thicker spears because they expend no energy producing berries",
        "distractors": ["Female spears are mildly toxic to humans", "Male plants resist all fungal rust diseases", "Female plants only sprout spears in late autumn"],
        "d": 3
    },
    {
        "q": "What botanical term describes a plant that has separate male and female flowers on the same individual plant, like corn and squash?",
        "correct": "Monoecious",
        "distractors": ["Dioecious", "Gynodioecious", "Synoecious"],
        "d": 2
    },
    {
        "q": "In cucurbits like pumpkins and zucchini, how can a home gardener distinguish a female flower from a male flower?",
        "correct": "The female flower has a miniature swollen fruit ovary at the base of its petals",
        "distractors": ["The female flower is bright blue while the male is yellow", "The female flower only opens at midnight", "The male flower has three layers of petals instead of one"],
        "d": 1
    },
    {
        "q": "What type of pollination is required by tomatoes and blueberries, where bumblebees rapidly vibrate their flight muscles to shake pollen loose?",
        "correct": "Buzz pollination (sonication)",
        "distractors": ["Anemophily (wind pollination)", "Hydrophily (water pollination)", "Ornithophily (bird pollination)"],
        "d": 2
    },
    {
        "q": "Why are standard European honeybees ineffective at buzz-pollinating tomato flowers?",
        "correct": "Honeybees cannot vibrate their flight muscles at the specific resonant frequency required to release the pollen",
        "distractors": ["Tomato pollen is fatal to European honeybees", "Honeybees cannot see yellow tomato flowers", "Tomato leaves produce a sticky glue that traps honeybees"],
        "d": 2
    },
    {
        "q": "Sweet corn is pollinated primarily by which mechanism?",
        "correct": "Wind pollination (anemophily)",
        "distractors": ["Insect pollination (entomophily)", "Bird pollination", "Self-pollination inside closed buds"],
        "d": 1
    },
    {
        "q": "Wild ancestral bananas and durians in Southeast Asia rely heavily on which nocturnal animals for pollination?",
        "correct": "Bats (nectarivorous fruit bats)",
        "distractors": ["Moths", "Nightjars", "Tree frogs"],
        "d": 2
    },
    {
        "q": "What is parthenocarpy in commercial fruit crops?",
        "correct": "The production of fruit without fertilization, resulting in seedless fruit",
        "distractors": ["The self-pruning of unpollinated flowers", "The absorption of nitrogen directly through leaves", "The shedding of bark during winter"],
        "d": 2
    },
    {
        "q": "What causes navel oranges to form the small secondary 'navel' at the fruit's apex?",
        "correct": "A genetic mutation causing a secondary, undeveloped twin fruit to grow within the primary fruit",
        "distractors": ["A puncture scar left by parasitic citrus wasps", "Incomplete closure of the stem calyx during freeze", "A grafting scar at the blossom end"],
        "d": 2
    },

    # 61-75: Genetics, Ploidy & Breeding Science (d1-d3)
    {
        "q": "Why are commercially cultivated Cavendish bananas seedless and sterile?",
        "correct": "They are triploid (3n), having three sets of chromosomes which prevents normal meiosis",
        "distractors": ["They are treated with gamma radiation after harvest", "They are harvested before seeds can form", "They are grown in sterile hydroponic solutions without soil microbes"],
        "d": 2
    },
    {
        "q": "How are seedless watermelons commercially created?",
        "correct": "By crossing a tetraploid (4n) female line with a diploid (2n) male line to produce sterile triploid (3n) seeds",
        "distractors": ["By genetically splicing tomato genes into melon seedlings", "By treating pollinated flowers with concentrated chlorine bleach", "By removing immature seeds by hand with microneedles"],
        "d": 2
    },
    {
        "q": "What chemical is commonly applied to watermelon seedlings to double their chromosome number from diploid (2n) to tetraploid (4n)?",
        "correct": "Colchicine",
        "distractors": ["Penicillin", "Ethylene glycol", "Gibberellic acid"],
        "d": 3
    },
    {
        "q": "The modern commercial garden strawberry (Fragaria × ananassa) possesses how many sets of chromosomes?",
        "correct": "Eight (octoploid, 8n)",
        "distractors": ["Two (diploid, 2n)", "Three (triploid, 3n)", "Four (tetraploid, 4n)"],
        "d": 3
    },
    {
        "q": "The commercial garden strawberry (Fragaria × ananassa) was created in 18th-century Europe by accidental hybridization between species from Virginia and which country?",
        "correct": "Chile",
        "distractors": ["Japan", "Madagascar", "South Africa"],
        "d": 2
    },
    {
        "q": "Why must commercial apple varieties be propagated by grafting rather than grown from seed?",
        "correct": "Apples are extreme heterozygotes; seeds produce trees with fruit drastically different from the parent",
        "distractors": ["Apple seeds never germinate in temperate soils", "Seed-grown apples produce lethal levels of cyanide in their flesh", "Seed-grown apple trees take over 100 years to bear fruit"],
        "d": 3
    },
    {
        "q": "In fruit tree grafting, what is the lower rooted portion called that controls tree vigor and disease resistance?",
        "correct": "Rootstock",
        "distractors": ["Scion", "Interstock", "Cambium"],
        "d": 1
    },
    {
        "q": "In fruit tree grafting, what is the upper branch cutting called that determines the specific fruit cultivar harvested?",
        "correct": "Scion",
        "distractors": ["Rootstock", "Bulbil", "Stolon"],
        "d": 1
    },
    {
        "q": "What British research station developed the famous 'Malling' series of dwarfing rootstocks (like M9) for apple trees?",
        "correct": "East Malling Research Station",
        "distractors": ["Kew Royal Botanic Gardens", "Rothamsted Experimental Station", "John Innes Centre"],
        "d": 3
    },
    {
        "q": "What physiological requirement must temperate fruit trees (like apples and peaches) satisfy in winter before they can break dormancy and flower in spring?",
        "correct": "Chill hours (cumulative hours between 32°F and 45°F / 0°C and 7.2°C)",
        "distractors": ["Thermal degree days above 90°F", "Photoperiod darkness exceeding 18 hours daily", "Sub-zero freezing soil days"],
        "d": 2
    },
    {
        "q": "What happens if a high-chill peach variety is planted in a tropical, frost-free climate with insufficient winter chill hours?",
        "correct": "The tree exhibits erratic, delayed foliation and fails to produce normal flowers or fruit",
        "distractors": ["The tree immediately grows into a giant evergreen bush that fruits continuously", "The tree dies from extreme root rot within two weeks", "The tree produces seedless citrus-like fruits"],
        "d": 2
    },
    {
        "q": "What is the phenomenon where a single branch on an established fruit tree spontaneously mutates to produce fruit with distinct traits?",
        "correct": "Sport (or bud sport)",
        "distractors": ["Chimera blight", "Epigenetic wilt", "Somatic lysis"],
        "d": 2
    },
    {
        "q": "Both the Pink Lady and Gala apples trace their lineage back as offspring of which famous American apple cultivar?",
        "correct": "Golden Delicious",
        "distractors": ["Red Delicious", "McIntosh", "Granny Smith"],
        "d": 3
    },
    {
        "q": "The tangelo is a citrus hybrid produced by crossing a tangerine (mandarin) with which other citrus fruit?",
        "correct": "Pomelo or grapefruit",
        "distractors": ["Kumquat", "Key lime", "Meyer lemon"],
        "d": 3
    },
    {
        "q": "A Meyer lemon is a natural hybrid between a true lemon and which other citrus?",
        "correct": "Mandarin or sweet orange",
        "distractors": ["Grapefruit", "Citron", "Lime"],
        "d": 2
    },

    # 76-90: Photosynthesis, Metabolism & Mineral Nutrition (d1-d3)
    {
        "q": "Pineapples and vanilla orchids use which specialized type of photosynthesis that opens stomata at night to minimize water loss?",
        "correct": "Crassulacean Acid Metabolism (CAM)",
        "distractors": ["C3 photosynthesis", "C4 photosynthesis", "Chemosynthesis"],
        "d": 3
    },
    {
        "q": "Sweet corn and sugarcane utilize which efficient photosynthetic pathway adapted to high temperatures and intense sunlight?",
        "correct": "C4 pathway",
        "distractors": ["C3 pathway", "CAM pathway", "Glycolytic pathway"],
        "d": 2
    },
    {
        "q": "Most common vegetables like lettuce, spinach, tomatoes, and potatoes utilize which photosynthetic pathway?",
        "correct": "C3 pathway",
        "distractors": ["C4 pathway", "CAM pathway", "Bacterial rhodopsin pathway"],
        "d": 3
    },
    {
        "q": "What physiological disorder in tomatoes and bell peppers causes a sunken, black leathery patch on the blossom end of the fruit?",
        "correct": "Blossom end rot",
        "distractors": ["Early blight", "Fusarium wilt", "Anthracnose"],
        "d": 1
    },
    {
        "q": "Blossom end rot in tomatoes is caused by a localized deficiency of which essential plant nutrient during fruit expansion?",
        "correct": "Calcium",
        "distractors": ["Nitrogen", "Iron", "Potassium"],
        "d": 2
    },
    {
        "q": "Why does inconsistent watering trigger blossom end rot even when soil calcium is plentiful?",
        "correct": "Calcium moves exclusively through the plant via transpiration in the xylem; water stress halts calcium uptake",
        "distractors": ["Excess water leaches calcium into the atmosphere", "Drying soil transforms calcium into gaseous neon", "Water stress causes roots to absorb nitrogen instead of calcium"],
        "d": 3
    },
    {
        "q": "What physiological condition causes tomato skins to suddenly crack or split concentrically near the stem?",
        "correct": "Rapid uptake of water (such as heavy rain after a dry spell) expanding the fruit pulp faster than the skin can stretch",
        "distractors": ["Severe potassium toxicity in the sap", "Fungal spores puncturing the cuticle", "Frost damage to chloroplasts"],
        "d": 1
    },
    {
        "q": "What physiological disorder in heads of lettuce or cabbage manifests as brown, dying leaf margins caused by localized calcium deficiency?",
        "correct": "Tipburn",
        "distractors": ["Bitter rot", "Black leg", "Scab"],
        "d": 3
    },
    {
        "q": "What beneficial soil microorganisms form mutualistic associations with the roots of most fruit trees, expanding water and phosphorus absorption?",
        "correct": "Mycorrhizal fungi",
        "distractors": ["Cyanobacteria", "Nematodes", "Slime molds"],
        "d": 2
    },
    {
        "q": "Legumes like peas and beans can fix atmospheric nitrogen into the soil because of symbiotic bacteria residing in their root nodules called:",
        "correct": "Rhizobia",
        "distractors": ["Spirilla", "Streptomyces", "Bacillus"],
        "d": 1
    },
    {
        "q": "What enzyme inside nitrogen-fixing rhizobia breaks the strong triple bond of atmospheric nitrogen gas (N2)?",
        "correct": "Nitrogenase",
        "distractors": ["Urease", "Rubisco", "Amylase"],
        "d": 3
    },
    {
        "q": "Why is the interior of an active, healthy nitrogen-fixing legume root nodule pink or reddish?",
        "correct": "It contains leghemoglobin, which binds oxygen to protect oxygen-sensitive nitrogenase",
        "distractors": ["It accumulates high concentrations of anthocyanin pigments", "The plant stores oxidized iron rust in its cortex", "It produces lycopene to ward off underground pests"],
        "d": 3
    },
    {
        "q": "What primary mineral nutrient is represented by the 'K' in standard N-P-K commercial fertilizer bags?",
        "correct": "Potassium (from Kalium)",
        "distractors": ["Phosphorus", "Krypton", "Calcium"],
        "d": 1
    },
    {
        "q": "Which mineral nutrient deficiency in leafy greens causes interveinal chlorosis (yellowing between leaf veins) while veins remain green?",
        "correct": "Magnesium (or Iron)",
        "distractors": ["Sodium", "Chlorine", "Silicon"],
        "d": 2
    },
    {
        "q": "Magnesium is an essential atom positioned at the precise molecular center of which vital plant pigment?",
        "correct": "Chlorophyll",
        "distractors": ["Beta-carotene", "Lycopene", "Anthocyanin"],
        "d": 2
    },

    # 91-100: Botanical Taxonomy & Chemistry Milestones (d1-d3)
    {
        "q": "What Swedish botanist formalized binomial nomenclature and classified hundreds of fruits and vegetables in 'Species Plantarum' (1753)?",
        "correct": "Carl Linnaeus",
        "distractors": ["Gregor Mendel", "Charles Darwin", "Jean-Baptiste Lamarck"],
        "d": 1
    },
    {
        "q": "Gregor Mendel discovered the foundational laws of genetic inheritance in the 1860s through experiments on which plant?",
        "correct": "Garden pea (Pisum sativum)",
        "distractors": ["Sweet corn (Zea mays)", "Common bean (Phaseolus vulgaris)", "Tomato (Solanum lycopersicum)"],
        "d": 1
    },
    {
        "q": "Why was the garden pea an ideal model organism for Mendel's genetic experiments?",
        "correct": "It has distinct binary traits, short generation time, and can easily self-pollinate or be cross-pollinated",
        "distractors": ["It has no cell walls, making DNA extraction simple", "It reproduces exclusively through asexual stolons", "It produces thousands of seeds within 24 hours of planting"],
        "d": 2
    },
    {
        "q": "What crystalline organic acid is responsible for the crisp, tart flavor of green apples?",
        "correct": "Malic acid",
        "distractors": ["Citric acid", "Tartaric acid", "Acetic acid"],
        "d": 1
    },
    {
        "q": "Which organic acid provides the primary sharp, sour taste in lemons, limes, and oranges?",
        "correct": "Citric acid",
        "distractors": ["Malic acid", "Tartaric acid", "Lactic acid"],
        "d": 1
    },
    {
        "q": "Which organic acid is the dominant acid found in wine grapes, giving wine much of its tart acidity?",
        "correct": "Tartaric acid",
        "distractors": ["Citric acid", "Malic acid", "Oxalic acid"],
        "d": 2
    },
    {
        "q": "Potassium bitartrate, a cooking byproduct that crystallizes in wine barrels, is commonly sold in grocery spice aisles as:",
        "correct": "Cream of tartar",
        "distractors": ["Baking powder", "Citric salt", "Pickling lime"],
        "d": 2
    },
    {
        "q": "What term describes the degree of dissolved sugar solids in fruit juice, measured using a refractometer?",
        "correct": "Degrees Brix (°Bx)",
        "distractors": ["Scoville units", "Baumé scale", "MacMichael degrees"],
        "d": 2
    },
    {
        "q": "How does a refractometer determine the sugar content (Brix) of a single drop of fruit juice?",
        "correct": "By measuring the bending (refraction) of light passing through the liquid",
        "distractors": ["By measuring electrical conductivity across electrodes", "By combusting trace sugar and recording heat release", "By counting dissolved carbon atoms with laser fluorescence"],
        "d": 2
    },
    {
        "q": "Which tree fruit contains the cyanogenic glycoside amygdalin in its seeds, which can release toxic hydrogen cyanide when digested?",
        "correct": "Apricot (and bitter almond)",
        "distractors": ["Fig", "Pomegranate", "Banana"],
        "d": 2
    }
]

if __name__ == "__main__":
    build_batch(BATCH_2, "tools/staging/produce_batch2.json", batch_num=2)
