#!/usr/bin/env python3
"""
Generate Batch 1 of Fruits & Veggies trivia (100 questions):
Botanical Classifications & Plant Anatomy.
Target: 30 d1, 40 d2, 30 d3.
"""

from produce_batch_builder import build_batch

BATCH_1 = [
    # 1-10: Berries vs False Berries (d1-d2)
    {
        "q": "Botanically speaking, which of the following is classified as a true berry?",
        "correct": "Banana",
        "distractors": ["Strawberry", "Raspberry", "Blackberry"],
        "d": 1
    },
    {
        "q": "Why is a strawberry not considered a true botanical berry?",
        "correct": "It is an aggregate accessory fruit derived from an enlarged receptacle",
        "distractors": ["It contains multiple woody pits like a stone fruit", "It develops from a single seed within a hard shell", "It is classified as a modified subterranean tuber"],
        "d": 2
    },
    {
        "q": "What are the tiny seed-like specks on the exterior surface of a strawberry botanically called?",
        "correct": "Achenes",
        "distractors": ["Arils", "Drupelets", "Pips"],
        "d": 2
    },
    {
        "q": "Raspberries and blackberries are botanically classified as aggregates of what?",
        "correct": "Drupelets",
        "distractors": ["Achenes", "Capsules", "Samaras"],
        "d": 2
    },
    {
        "q": "Which common salad ingredient is botanically classified as a berry?",
        "correct": "Tomato",
        "distractors": ["Carrot", "Celery", "Radish"],
        "d": 1
    },
    {
        "q": "Watermelons, cantaloupes, and cucumbers are classified under which specialized type of berry?",
        "correct": "Pepo",
        "distractors": ["Hesperidium", "Pome", "Syconium"],
        "d": 2
    },
    {
        "q": "Which fruit is a specialized berry with a leathery rind and aromatic oil glands called a hesperidium?",
        "correct": "Orange",
        "distractors": ["Pomegranate", "Apple", "Avocado"],
        "d": 2
    },
    {
        "q": "Botanically, an avocado is categorized as which type of fruit?",
        "correct": "Single-seeded berry",
        "distractors": ["Stone fruit or drupe", "Accessory pome", "Dehiscent legume"],
        "d": 1
    },
    {
        "q": "Which of these kitchen vegetables is technically a botanical berry?",
        "correct": "Eggplant",
        "distractors": ["Rhubarb", "Asparagus", "Broccoli"],
        "d": 1
    },
    {
        "q": "Bell peppers and chili peppers belong to which botanical fruit classification?",
        "correct": "Berry",
        "distractors": ["Drupe", "Pepo", "Pod"],
        "d": 1
    },

    # 11-20: Drupes / Stone Fruits (d1-d3)
    {
        "q": "Which term describes fleshy fruits with a thin skin and a central stony pit enclosing the seed?",
        "correct": "Drupe",
        "distractors": ["Pome", "Legume", "Pepo"],
        "d": 1
    },
    {
        "q": "In a stone fruit such as a peach, what is the hardened shell of the pit botanically called?",
        "correct": "Endocarp",
        "distractors": ["Mesocarp", "Exocarp", "Pericarp"],
        "d": 3
    },
    {
        "q": "Which edible tree nut is technically the seed of a drupe, rather than a true botanical nut?",
        "correct": "Almond",
        "distractors": ["Acorn", "Chestnut", "Hazelnut"],
        "d": 2
    },
    {
        "q": "Botanically, which of the following is classified as a drupe?",
        "correct": "Olive",
        "distractors": ["Grape", "Blueberry", "Currant"],
        "d": 2
    },
    {
        "q": "What type of fruit is a coconut botanically classified as?",
        "correct": "Fibrous drupe",
        "distractors": ["True nut", "Legume pod", "Woody pome"],
        "d": 2
    },
    {
        "q": "Which tropical fruit with a large flattened stone pit is classified as a drupe?",
        "correct": "Mango",
        "distractors": ["Papaya", "Guava", "Pineapple"],
        "d": 1
    },
    {
        "q": "A nectarine is genetically a smooth-skinned variant of which fruit?",
        "correct": "Peach",
        "distractors": ["Plum", "Apricot", "Apple"],
        "d": 1
    },
    {
        "q": "Cashews develop attached to the bottom of an accessory fruit known as what?",
        "correct": "Cashew apple",
        "distractors": ["Cashew pod", "Cashew cone", "Cashew melon"],
        "d": 2
    },
    {
        "q": "Which of these fruits is a hybrid cross between an apricot and a plum?",
        "correct": "Pluot",
        "distractors": ["Tangelo", "Boysenberry", "Kumquat"],
        "d": 1
    },
    {
        "q": "Cherries, peaches, plums, and apricots all belong to which genus of flowering plants?",
        "correct": "Prunus",
        "distractors": ["Malus", "Citrus", "Ribes"],
        "d": 2
    },

    # 21-30: Pomes and Accessory Fruits (d1-d3)
    {
        "q": "Which botanical fruit type develops from an inferior ovary where the edible flesh is derived mostly from the hypanthium?",
        "correct": "Pome",
        "distractors": ["Drupe", "Berry", "Silique"],
        "d": 3
    },
    {
        "q": "Which of the following is a classic example of a pome fruit?",
        "correct": "Pear",
        "distractors": ["Cherry", "Pecan", "Pomegranate"],
        "d": 1
    },
    {
        "q": "Quince belongs to which botanical category of fruit?",
        "correct": "Pome",
        "distractors": ["Drupe", "Pepo", "Aggregate fruit"],
        "d": 3
    },
    {
        "q": "In an apple, what part of the flower expands to form the bulk of the crisp, edible flesh?",
        "correct": "Hypanthium or floral tube",
        "distractors": ["Ovary wall endocarp", "Embryo sac", "Stigma"],
        "d": 3
    },
    {
        "q": "The medlar (Mespilus germanica), an ancient European fruit eaten after bletting, is classified as a:",
        "correct": "Pome",
        "distractors": ["Drupe", "Legume", "True nut"],
        "d": 3
    },
    {
        "q": "Which small orange fruit native to China is a pome closely related to apples and pears?",
        "correct": "Loquat",
        "distractors": ["Kumquat", "Persimmon", "Cape gooseberry"],
        "d": 3
    },
    {
        "q": "Apples belong to which broad botanical plant family?",
        "correct": "Rosaceae",
        "distractors": ["Solanaceae", "Cucurbitaceae", "Brassicaceae"],
        "d": 1
    },
    {
        "q": "What term describes the softening and decaying process required before medlars and persimmons become sweet and palatable?",
        "correct": "Bletting",
        "distractors": ["Scarification", "Stratification", "Blanching"],
        "d": 3
    },
    {
        "q": "Botanically, the core of an apple surrounding the seeds represents which layer?",
        "correct": "Endocarp",
        "distractors": ["Exocarp", "Epidermis", "Mesocarp"],
        "d": 3
    },
    {
        "q": "Pears are known for their slightly gritty texture, which is caused by the presence of what structures?",
        "correct": "Sclereids or stone cells",
        "distractors": ["Crystalline calcium oxalate", "Undeveloped ovules", "Silica trichomes"],
        "d": 3
    },

    # 31-40: Pepos and Cucurbits (d1-d2)
    {
        "q": "Which plant family includes cucumbers, melons, squash, and pumpkins?",
        "correct": "Cucurbitaceae",
        "distractors": ["Solanaceae", "Asteraceae", "Fabaceae"],
        "d": 1
    },
    {
        "q": "A pepo is distinguished from a typical berry primarily by which feature?",
        "correct": "A hard, thick outer rind or exocarp",
        "distractors": ["A central woody stone", "Seeds displayed on the exterior skin", "A papery floral capsule"],
        "d": 1
    },
    {
        "q": "Which vegetable is botanically an immature pepo fruit harvested before its rind hardens?",
        "correct": "Zucchini",
        "distractors": ["Turnip", "Carrot", "Beetroot"],
        "d": 1
    },
    {
        "q": "What botanical structure allows climbing cucurbits like gourds and squashes to cling to supports?",
        "correct": "Tendrils",
        "distractors": ["Aerial taproots", "Thorns", "Petioles"],
        "d": 1
    },
    {
        "q": "Which fruit is classified as a pepo with sweet, aromatic green or orange flesh?",
        "correct": "Cantaloupe",
        "distractors": ["Papaya", "Guava", "Mango"],
        "d": 1
    },
    {
        "q": "What dried vegetable fiber, often used as an exfoliating bath sponge, comes from the fibrous skeleton of a cucurbit fruit?",
        "correct": "Luffa",
        "distractors": ["Coir", "Jute", "Kapok"],
        "d": 3
    },
    {
        "q": "Winter squashes like butternut and acorn differ from summer squashes because they are harvested when:",
        "correct": "The rind is fully hardened and mature",
        "distractors": ["The plant is dormant in midwinter", "The seeds are still microscopic", "The skin is thin and edible raw"],
        "d": 2
    },
    {
        "q": "Which cucurbit fruit is famous for having an intensely bitter flavor due to momordicines?",
        "correct": "Bitter melon",
        "distractors": ["Spaghetti squash", "Chayote", "Honeydew"],
        "d": 2
    },
    {
        "q": "Chayote, a pear-shaped cucurbit common in Latin American cuisine, is notable because each fruit contains:",
        "correct": "Only a single seed",
        "distractors": ["Hundreds of loose seeds", "No ovary walls", "A woody pit"],
        "d": 3
    },
    {
        "q": "Cucurbitacin compounds in pumpkins and squashes can occasionally cause them to taste excessively:",
        "correct": "Bitter",
        "distractors": ["Sour", "Salty", "Spicy"],
        "d": 2
    },

    # 41-50: Multiple and Aggregate Fruits (d1-d3)
    {
        "q": "What is the botanical term for a fruit that develops from the coalescence of many individual flowers in an inflorescence?",
        "correct": "Multiple fruit",
        "distractors": ["Aggregate fruit", "Simple fruit", "Accessory fruit"],
        "d": 2
    },
    {
        "q": "Which tropical fruit is a classic example of a multiple fruit formed from fused flower ovaries?",
        "correct": "Pineapple",
        "distractors": ["Avocado", "Kiwi", "Banana"],
        "d": 1
    },
    {
        "q": "Botanically, a fig is what specialized inverted floral structure?",
        "correct": "Syconium",
        "distractors": ["Silique", "Hesperidium", "Samara"],
        "d": 2
    },
    {
        "q": "The crunchy seeds inside a ripe fig are actually what botanical structures?",
        "correct": "Individual achenes produced by tiny internal flowers",
        "distractors": ["Glandular hairs", "Unfertilized pollen sacs", "Fleshy arils"],
        "d": 3
    },
    {
        "q": "Which of the following is a multiple fruit, rather than an aggregate fruit?",
        "correct": "Mulberry",
        "distractors": ["Blackberry", "Raspberry", "Strawberry"],
        "d": 3
    },
    {
        "q": "Jackfruit and breadfruit belong to which family of plants, known for multiple fruits?",
        "correct": "Moraceae",
        "distractors": ["Rutaceae", "Solanaceae", "Arecaceae"],
        "d": 3
    },
    {
        "q": "The edible juicy red jewels inside a pomegranate are called what?",
        "correct": "Arils",
        "distractors": ["Drupelets", "Pomes", "Achenes"],
        "d": 1
    },
    {
        "q": "Botanically, the fruit of a pomegranate is categorized as a thick-skinned berry known as a:",
        "correct": "Balausta",
        "distractors": ["Hesperidium", "Pepo", "Legume"],
        "d": 3
    },
    {
        "q": "In a pineapple, what does the woody central core represent botanically?",
        "correct": "The central stem axis of the inflorescence",
        "distractors": ["A coalesced mega-seed", "The fibrous ovary wall", "An elongated taproot"],
        "d": 3
    },
    {
        "q": "Which tree produces a large, bumpy green multiple fruit nicknamed the 'hedge apple' or 'monkey ball'?",
        "correct": "Osage orange",
        "distractors": ["Pawpaw", "Breadfruit", "Persimmon"],
        "d": 2
    },

    # 51-65: Brassica oleracea Cultivars & Brassicas (d1-d3)
    {
        "q": "Broccoli, cauliflower, kale, cabbage, and Brussels sprouts are all cultivated varieties of which single wild species?",
        "correct": "Brassica oleracea",
        "distractors": ["Brassica rapa", "Brassica napus", "Brassica juncea"],
        "d": 1
    },
    {
        "q": "What part of the plant is primarily harvested and consumed in broccoli?",
        "correct": "Immature unopened flower buds and thick stems",
        "distractors": ["Underground root nodules", "Modified leaf petioles", "Swollen cotyledons"],
        "d": 1
    },
    {
        "q": "In cauliflower, the white edible head (the 'curd') is botanically composed of:",
        "correct": "Hypertrophied, proliferated floral meristem tissue",
        "distractors": ["Mature dried seed capsules", "Swollen leaf blade mesophyll", "Underground hypocotyl"],
        "d": 3
    },
    {
        "q": "What part of the plant are Brussels sprouts botanically?",
        "correct": "Enlarged lateral or axillary buds",
        "distractors": ["Swollen root tubers", "Terminal flower inflorescences", "Modified hypocotyls"],
        "d": 2
    },
    {
        "q": "Which Brassica oleracea variety is specifically selected for its swollen, bulbous stem above ground?",
        "correct": "Kohlrabi",
        "distractors": ["Rutabaga", "Turnip", "Parsnip"],
        "d": 2
    },
    {
        "q": "Romanesco broccoli is celebrated in mathematics and botany for displaying what visual geometric pattern?",
        "correct": "Fractal self-similarity following Fibonacci spirals",
        "distractors": ["Bilateral tessellation", "Concentric hexagonal tiling", "Golden section hyperbolic nodes"],
        "d": 2
    },
    {
        "q": "Which Brassica oleracea cultivar was bred through artificial selection emphasizing large, tightly packed terminal buds?",
        "correct": "Cabbage",
        "distractors": ["Kale", "Broccoli", "Kohlrabi"],
        "d": 3
    },
    {
        "q": "Kale was bred from wild cabbage through selective cultivation favoring which plant part?",
        "correct": "Enlarged leaves",
        "distractors": ["Swollen roots", "Massive flower buds", "Thickened stems"],
        "d": 1
    },
    {
        "q": "Turnips and bok choy (pak choi) belong to which species of Brassica?",
        "correct": "Brassica rapa",
        "distractors": ["Brassica oleracea", "Brassica nigra", "Brassica carinata"],
        "d": 2
    },
    {
        "q": "Rutabaga (swede) originated as a natural allotetraploid hybrid between cabbage (Brassica oleracea) and which plant?",
        "correct": "Turnip (Brassica rapa)",
        "distractors": ["Black mustard (Brassica nigra)", "Radish (Raphanus sativus)", "Horseradish (Armoracia rusticana)"],
        "d": 3
    },
    {
        "q": "What sulfur-containing secondary metabolites give cruciferous vegetables like broccoli and cabbage their pungent aroma and bitter notes?",
        "correct": "Glucosinolates",
        "distractors": ["Carotenoids", "Betalains", "Anthocyanins"],
        "d": 3
    },
    {
        "q": "When cruciferous plant tissues are crushed or chewed, glucosinolates are enzymatically converted by myrosinase into:",
        "correct": "Isothiocyanates",
        "distractors": ["Polyphenols", "Tannins", "Flavonoids"],
        "d": 3
    },
    {
        "q": "What diagram in plant genetics illustrates the genomic relationships and hybridization of six Brassica species?",
        "correct": "The Triangle of U",
        "distractors": ["The Punnett Wheel", "The Calvin Hexagon", "The Krebs Octagon"],
        "d": 3
    },
    {
        "q": "Collard greens are botanically classified under which cultivar group of Brassica oleracea?",
        "correct": "Acephala group (meaning 'headless')",
        "distractors": ["Capitata group", "Botrytis group", "Gemmifera group"],
        "d": 3
    },
    {
        "q": "Napa cabbage and Chinese cabbage are cultivars of which species?",
        "correct": "Brassica rapa",
        "distractors": ["Brassica oleracea", "Brassica napus", "Brassica juncea"],
        "d": 2
    },

    # 66-80: Plant Anatomy - Roots, Tubers, Bulbs, Stems (d1-d3)
    {
        "q": "Which part of the plant is consumed when eating a carrot?",
        "correct": "Taproot",
        "distractors": ["Stolon", "Rhizome", "Corm"],
        "d": 1
    },
    {
        "q": "A white potato is botanically classified as which specialized plant organ?",
        "correct": "Stem tuber",
        "distractors": ["Root tuber", "Bulb", "Taproot"],
        "d": 2
    },
    {
        "q": "In contrast to a white potato, a sweet potato is botanically classified as a:",
        "correct": "Storage root or root tuber",
        "distractors": ["Stem tuber", "Rhizome", "Corm"],
        "d": 2
    },
    {
        "q": "What are the 'eyes' of a common white potato botanically?",
        "correct": "Axillary buds or nodes from which new shoots grow",
        "distractors": ["Mycorrhizal fungi access ports", "Root caps for nutrient intake", "Gas exchange stomata"],
        "d": 2
    },
    {
        "q": "Which culinary aromatic is botanically an underground creeping horizontal stem known as a rhizome?",
        "correct": "Ginger",
        "distractors": ["Turnip", "Garlic", "Parsnip"],
        "d": 1
    },
    {
        "q": "What botanical structure forms the edible layers of an onion bulb?",
        "correct": "Fleshy modified leaves or leaf bases",
        "distractors": ["Swollen primary taproot tissue", "Compressed woody stems", "Fused pedicels"],
        "d": 2
    },
    {
        "q": "Garlic cloves are botanically individual:",
        "correct": "Bulblets or secondary storage buds",
        "distractors": ["Dried seeds", "Underground berries", "Root nodules"],
        "d": 2
    },
    {
        "q": "The edible stalk of celery is botanically which plant part?",
        "correct": "Petiole (leaf stalk)",
        "distractors": ["Main stem axis", "Taproot", "Floral peduncle"],
        "d": 2
    },
    {
        "q": "Like celery, rhubarb stalks are eaten for which anatomical plant structure?",
        "correct": "Petioles",
        "distractors": ["Stolons", "Roots", "True stems"],
        "d": 2
    },
    {
        "q": "Why are rhubarb leaf blades strictly avoided and considered toxic for human consumption?",
        "correct": "They contain dangerously high concentrations of oxalic acid and oxalates",
        "distractors": ["They produce lethal amounts of cyanide glycosides", "They contain extreme amounts of solanine alkaloid", "They are coated with concentrated capsaicin"],
        "d": 1
    },
    {
        "q": "Asparagus spears harvested in the spring are botanically:",
        "correct": "Young emergent stems or shoots",
        "distractors": ["Flower petals", "Taproots", "Swollen leaf midribs"],
        "d": 1
    },
    {
        "q": "What plant part is eaten when consuming a globe artichoke?",
        "correct": "Immature composite flower bud including the fleshy receptacle and involucral bracts",
        "distractors": ["Swollen underground corm", "Fleshy petiole bundle", "Mature seed pod"],
        "d": 2
    },
    {
        "q": "Capers used in Mediterranean cooking are botanically:",
        "correct": "Unopened flower buds of Capparis spinosa",
        "distractors": ["Dried berries of an evergreen shrub", "Fermented immature seeds", "Pickled root nodules"],
        "d": 2
    },
    {
        "q": "Taro and water chestnuts are edible examples of which swollen underground stem base?",
        "correct": "Corm",
        "distractors": ["Taproot", "Haustorium", "Bulbil"],
        "d": 3
    },
    {
        "q": "A Jerusalem artichoke (sunchoke) is the edible tuber of a plant belonging to which family?",
        "correct": "Asteraceae (Sunflower family)",
        "distractors": ["Solanaceae (Nightshade family)", "Apiaceae (Carrot family)", "Liliaceae (Lily family)"],
        "d": 3
    },

    # 81-100: Legumes, Nightshades, & Botanical Oddities (d1-d3)
    {
        "q": "Which botanical fruit type splits open along two seams at maturity and is characteristic of the Fabaceae family?",
        "correct": "Legume or pod",
        "distractors": ["Silique", "Capsule", "Follicle"],
        "d": 2
    },
    {
        "q": "What unique botanical phenomenon causes peanut pods to mature underground?",
        "correct": "Geocarpy",
        "distractors": ["Vivipary", "Parthenocarpy", "Epigeal germination"],
        "d": 3
    },
    {
        "q": "After peanut flowers are pollinated, what elongated stalk pushes the developing pod into the soil?",
        "correct": "Peg",
        "distractors": ["Stolon", "Tendril", "Rachis"],
        "d": 3
    },
    {
        "q": "Potatoes, tomatoes, eggplants, and peppers all belong to which flowering plant family?",
        "correct": "Solanaceae",
        "distractors": ["Brassicaceae", "Cucurbitaceae", "Rosaceae"],
        "d": 1
    },
    {
        "q": "What toxic glycoalkaloid develops in potatoes when exposed to light, turning them green?",
        "correct": "Solanine",
        "distractors": ["Capsaicin", "Amygdalin", "Myristicin"],
        "d": 1
    },
    {
        "q": "The green color that appears on sun-exposed potatoes is due to harmless chlorophyll, but indicates the simultaneous synthesis of:",
        "correct": "Solanine and chaconine",
        "distractors": ["Cyanogenic glucosides", "Ricin", "Aconitine"],
        "d": 2
    },
    {
        "q": "Carrots, parsnips, celery, fennel, and parsley belong to which botanical family characterized by umbrella-like flower clusters?",
        "correct": "Apiaceae (Umbelliferae)",
        "distractors": ["Asteraceae", "Fabaceae", "Amaranthaceae"],
        "d": 2
    },
    {
        "q": "Which member of the Apiaceae family produces an enlarged, bulb-like base of overlapping leaf sheaths with an anise flavor?",
        "correct": "Florence fennel",
        "distractors": ["Parsnip", "Celeriac", "Dill"],
        "d": 3
    },
    {
        "q": "Celeriac is a variety of celery specifically cultivated for its:",
        "correct": "Swollen hypocotyl and taproot",
        "distractors": ["Crisp leafy petioles", "Edible seeds", "Aromatic flower buds"],
        "d": 2
    },
    {
        "q": "Spinach, Swiss chard, and beetroot belong to which plant family?",
        "correct": "Amaranthaceae",
        "distractors": ["Brassicaceae", "Solanaceae", "Lamiaceae"],
        "d": 2
    },
    {
        "q": "What type of individual fruit is a single kernel of sweet corn botanically classified as?",
        "correct": "Caryopsis (grain)",
        "distractors": ["Achene", "Berry", "Drupelet"],
        "d": 3
    },
    {
        "q": "In an ear of corn, what botanical structures are the long silky strands?",
        "correct": "Elongated styles and stigmas of female flowers",
        "distractors": ["Male pollen filaments", "Modified protective bract hairs", "Fibrous vascular bundles"],
        "d": 2
    },
    {
        "q": "Okra pods belong to which botanical plant family, famous for hibiscus and cotton?",
        "correct": "Malvaceae",
        "distractors": ["Solanaceae", "Fabaceae", "Cucurbitaceae"],
        "d": 2
    },
    {
        "q": "The slimy, gelatinous texture produced when cooking okra is caused by high levels of:",
        "correct": "Mucilage",
        "distractors": ["Pectin", "Latex", "Starch"],
        "d": 2
    },
    {
        "q": "Which vegetable consists of swollen, crisp subterranean leaf petiole bases and is often eaten in salads?",
        "correct": "Endive",
        "distractors": ["Rutabaga", "Daikon", "Horseradish"],
        "d": 3
    },
    {
        "q": "What part of the leek is primarily used in fine cuisine?",
        "correct": "The blanched, tender lower leaf sheath cylinder",
        "distractors": ["The tough fibrous taproot", "The flowering umbel", "The woody seed capsule"],
        "d": 2
    },
    {
        "q": "Which fruit is known for containing actinidain, an enzyme that breaks down protein and curdles dairy?",
        "correct": "Kiwi",
        "distractors": ["Apple", "Orange", "Grape"],
        "d": 2
    },
    {
        "q": "Pineapples contain which proteolytic enzyme mixture widely used as a meat tenderizer?",
        "correct": "Bromelain",
        "distractors": ["Papain", "Ficin", "Actinidain"],
        "d": 1
    },
    {
        "q": "Papaya latex contains which commercial enzyme used in digestive aids and meat tenderizers?",
        "correct": "Papain",
        "distractors": ["Bromelain", "Ptyalin", "Pepsin"],
        "d": 1
    },
    {
        "q": "The scientific name for the common cultivated apple tree is:",
        "correct": "Malus domestica",
        "distractors": ["Pyrus communis", "Prunus persica", "Cydonia oblonga"],
        "d": 1
    }
]

if __name__ == "__main__":
    build_batch(BATCH_1, "tools/staging/produce_batch1.json", batch_num=1)
