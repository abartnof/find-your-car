#!/usr/bin/env python3
"""
Generate Batch 3 of Fruits & Veggies trivia (100 questions):
Culinary, Global Agriculture & History (Origins, Columbian Exchange, Cultivar Breeding & History).
Target: ~30 d1, ~40 d2, ~30 d3.
"""

from produce_batch_builder import build_batch

BATCH_3 = [
    # 1-20: Columbian Exchange & Domestication Origins (d1-d3)
    {
        "q": "Prior to the Columbian Exchange beginning in 1492, which staple vegetable was entirely unknown in Europe?",
        "correct": "Potato",
        "distractors": ["Cabbage", "Turnip", "Onion"],
        "d": 1
    },
    {
        "q": "In which geographic region were wild potatoes first domesticated by indigenous peoples over 7,000 years ago?",
        "correct": "The Andean highlands of modern Peru and Bolivia",
        "distractors": ["The steppes of Central Asia", "The Nile River valley of Egypt", "The coastal plains of Brazil"],
        "d": 1
    },
    {
        "q": "Where did the cultivated tomato originate before being introduced to Europe and the rest of the world?",
        "correct": "Western South America and Mesoamerica",
        "distractors": ["Southern Italy and Sicily", "The Balkan peninsula", "Southeast Asia"],
        "d": 1
    },
    {
        "q": "Which fruit or vegetable was native to the Old World rather than the Americas?",
        "correct": "Apple",
        "distractors": ["Chili pepper", "Pumpkin", "Corn (maize)"],
        "d": 1
    },
    {
        "q": "The wild ancestor of all modern domestic apple varieties, Malus sieversii, originated in which mountain region?",
        "correct": "Tian Shan mountains of Central Asia (Kazakhstan)",
        "distractors": ["Caucasus mountains of Georgia", "Pyrenees of Spain and France", "Appalachian mountains of North America"],
        "d": 3
    },
    {
        "q": "What city in Kazakhstan literally translates to 'Father of Apples' due to its proximity to wild ancestral apple forests?",
        "correct": "Almaty",
        "distractors": ["Astana", "Tashkent", "Bishkek"],
        "d": 2
    },
    {
        "q": "Citrus fruits such as oranges, lemons, and limes originally evolved in which region of the world?",
        "correct": "Southeast Asia, South Asia, and northeastern Australia",
        "distractors": ["The Mediterranean coast of Italy and Greece", "Sub-Saharan Africa", "Central America"],
        "d": 3
    },
    {
        "q": "Where were wild bananas first domesticated by ancient farmers roughly 7,000 to 10,000 years ago?",
        "correct": "New Guinea and Island Southeast Asia",
        "distractors": ["The Canary Islands", "Central America", "Madagascar"],
        "d": 3
    },
    {
        "q": "Which of the following culinary staples was brought to the Americas by European colonists rather than native to the Americas?",
        "correct": "Garlic",
        "distractors": ["Sweet potato", "Avocado", "Bell pepper"],
        "d": 2
    },
    {
        "q": "Watermelons were originally domesticated thousands of years ago in which continent?",
        "correct": "Africa (northeastern Africa / Sudan)",
        "distractors": ["South America", "Europe", "Australia"],
        "d": 2
    },
    {
        "q": "What ancient civilization cultivated watermelons as portable water storage containers, as evidenced by seeds found in King Tutankhamun's tomb?",
        "correct": "Ancient Egypt",
        "distractors": ["Ancient Rome", "The Maya civilization", "The Indus Valley civilization"],
        "d": 2
    },
    {
        "q": "Where were wild peaches first domesticated by humans over 8,000 years ago?",
        "correct": "The Yangtze River valley of China",
        "distractors": ["The Tigris-Euphrates basin in Mesopotamia", "The Black Sea coast of Turkey", "The Nile Delta in Egypt"],
        "d": 3
    },
    {
        "q": "What color were carrots originally before Dutch growers selectively bred orange varieties in the 17th century?",
        "correct": "Purple and yellow",
        "distractors": ["Bright blue and black", "Neon red and white", "Emerald green"],
        "d": 1
    },
    {
        "q": "In which historical region did wild purple and yellow carrots first originate and undergo domestication?",
        "correct": "Persia and modern Afghanistan",
        "distractors": ["Scandinavia", "The British Isles", "The Caribbean basin"],
        "d": 3
    },
    {
        "q": "Which of these crops is part of the traditional Mesoamerican 'Three Sisters' agricultural companion planting triad?",
        "correct": "Winter squash",
        "distractors": ["Potato", "Tomato", "Wheat"],
        "d": 1
    },
    {
        "q": "In the 'Three Sisters' companion planting system, what role does winter squash play?",
        "correct": "Its broad prickly leaves shade the soil to suppress weeds and retain soil moisture",
        "distractors": ["It fixes atmospheric nitrogen into the root zone", "Its tall stems provide a physical climbing pole for beans", "It emits ethylene to ripen the corn faster"],
        "d": 2
    },
    {
        "q": "Where was the avocado first domesticated by indigenous Mesoamericans?",
        "correct": "South-central Mexico (Puebla valley)",
        "distractors": ["The Amazon rainforest of Brazil", "The Pampas of Argentina", "The Caribbean island of Cuba"],
        "d": 1
    },
    {
        "q": "Pineapples are indigenous to which tropical region of the Americas?",
        "correct": "The Paraná-Paraguay River basin between southern Brazil and Paraguay",
        "distractors": ["The Hawaiian Islands", "The Florida Everglades", "The Sonoran desert"],
        "d": 3
    },
    {
        "q": "Which ancient grain-like crop with edible leaves was domesticated in the Andean altiplano of South America?",
        "correct": "Quinoa",
        "distractors": ["Barley", "Buckwheat", "Spelt"],
        "d": 2
    },
    {
        "q": "Cassava (manioc or yuca), an essential tropical root crop, was originally domesticated in which region?",
        "correct": "The Amazon basin of South America",
        "distractors": ["West Africa", "Southeast Asia", "The Mediterranean basin"],
        "d": 3
    },

    # 21-45: Famous Cultivars & Breeding Breakthroughs (d1-d3)
    {
        "q": "Which popular modern apple variety was developed by the University of Minnesota and patented in 1988 for its exceptional crispness?",
        "correct": "Honeycrisp",
        "distractors": ["Gala", "Fuji", "Granny Smith"],
        "d": 2
    },
    {
        "q": "What unique cellular property gives the Honeycrisp apple its extraordinarily juicy, explosive crunch compared to other varieties?",
        "correct": "Its cells are significantly larger and fracture cleanly rather than tearing apart when bitten",
        "distractors": ["It contains double the amount of crystalline calcium oxalate", "Its cell walls are reinforced with natural latex", "It has air pockets pressurized with carbon dioxide"],
        "d": 3
    },
    {
        "q": "Who was the Southern California amateur horticulturist and mail carrier who discovered and patented the Hass avocado in 1935?",
        "correct": "Rudolph Hass",
        "distractors": ["Luther Burbank", "Charles Hovey", "George Roeding"],
        "d": 2
    },
    {
        "q": "Every Hass avocado tree in the world today is genetically a clone propagated from a single mother tree grown where?",
        "correct": "La Habra Heights, California",
        "distractors": ["Oaxaca, Mexico", "Homestead, Florida", "Kula, Hawaii"],
        "d": 2
    },
    {
        "q": "What variety was the world's dominant export banana until the 1950s, when Panama disease nearly wiped out commercial plantations?",
        "correct": "Gros Michel ('Big Mike')",
        "distractors": ["Cavendish", "Lady Finger", "Red Dacca"],
        "d": 2
    },
    {
        "q": "Which banana variety replaced the Gros Michel as the primary global commercial export banana due to its initial resistance to race 1 Panama disease?",
        "correct": "Cavendish",
        "distractors": ["Gros Michel", "Blue Java", "Plantain"],
        "d": 1
    },
    {
        "q": "After whom is the Cavendish banana cultivar named?",
        "correct": "William Cavendish, 6th Duke of Devonshire",
        "distractors": ["Henry Cavendish, discoverer of hydrogen", "Sir Thomas Cavendish, English privateer", "Lord Richard Cavendish of Kenya"],
        "d": 2
    },
    {
        "q": "What soil-borne fungal pathogen caused Panama disease in Gros Michel bananas and now threatens Cavendish bananas with Tropical Race 4 (TR4)?",
        "correct": "Fusarium oxysporum",
        "distractors": ["Phytophthora infestans", "Botrytis cinerea", "Claviceps purpurea"],
        "d": 3
    },
    {
        "q": "Who discovered the crisp, bright green Granny Smith apple in 1868 as a chance seedling in New South Wales, Australia?",
        "correct": "Maria Ann Smith",
        "distractors": ["Eliza Tibbets", "Beatrix Potter", "Florence Nightingale"],
        "d": 1
    },
    {
        "q": "All commercial Washington Navel orange trees in the United States trace back to budwood sent to California from a spontaneous mutation found where?",
        "correct": "Bahia, Brazil",
        "distractors": ["Seville, Spain", "Valencia, Spain", "Palermo, Sicily"],
        "d": 3
    },
    {
        "q": "Who was the pioneering woman in Riverside, California who received two Brazilian navel orange trees from the USDA in 1873, sparking the California citrus industry?",
        "correct": "Eliza Tibbets",
        "distractors": ["Laura Ingalls Wilder", "Clara Barton", "Julia Morgan"],
        "d": 3
    },
    {
        "q": "Which sweet, easy-to-peel mandarin hybrid was named after Father Clément Rodier, who discovered it in his orphanage garden in Algeria around 1900?",
        "correct": "Clementine",
        "distractors": ["Tangerine", "Satsuma", "Tangelo"],
        "d": 1
    },
    {
        "q": "What agricultural explorer traveled extensively through Asia for the USDA between 1905 and 1918, introducing the Meyer lemon and hundreds of other crops?",
        "correct": "Frank N. Meyer",
        "distractors": ["David Fairchild", "Luther Burbank", "George Washington Carver"],
        "d": 2
    },
    {
        "q": "Which highly anticipated apple variety (WA 38), developed by Washington State University as a cross between Honeycrisp and Enterprise, debuted in 2019?",
        "correct": "Cosmic Crisp",
        "distractors": ["SnapDragon", "Envy", "Sweetango"],
        "d": 1
    },
    {
        "q": "Why was the Cosmic Crisp apple given the name 'Cosmic'?",
        "correct": "The bright yellow lenticels (pores) on its deep red skin resembled stars scattered across the cosmos",
        "distractors": ["It was the first fruit tree bred aboard the International Space Station", "Its DNA was treated with cosmic ray bombardment", "It was named in honor of the Apollo moon landings"],
        "d": 2
    },
    {
        "q": "The trademarked Pink Lady apple is the commercial brand name for which botanical apple cultivar developed in Western Australia?",
        "correct": "Cripps Pink",
        "distractors": ["Lady Williams", "Sundowner", "Pink Pearl"],
        "d": 2
    },
    {
        "q": "The Fuji apple was developed by Japanese agricultural researchers in the 1930s as a cross between Red Delicious and which classic American variety?",
        "correct": "Ralls Janet",
        "distractors": ["Golden Delicious", "Granny Smith", "Northern Spy"],
        "d": 3
    },
    {
        "q": "Who discovered the famous McIntosh apple in 1811 while clearing overgrown brush on his homestead farm in Ontario, Canada?",
        "correct": "John McIntosh",
        "distractors": ["Alexander Graham Bell", "Charles McIntosh", "William Lyon Mackenzie"],
        "d": 1
    },
    {
        "q": "The original Red Delicious apple tree was discovered in Peru, Iowa by farmer Jesse Hiatt, who initially called it what?",
        "correct": "Hawkeye",
        "distractors": ["Cornhusker", "Stark's Gem", "Prairie Queen"],
        "d": 3
    },
    {
        "q": "Where was the Golden Delicious apple discovered as a chance seedling in 1905 before its rights were purchased by Stark Bro's Nurseries?",
        "correct": "Clay County, West Virginia",
        "distractors": ["Yakima Valley, Washington", "Sonoma County, California", "Lancaster County, Pennsylvania"],
        "d": 3
    },
    {
        "q": "What natural mutation gives pink-fleshed Cara Cara navel oranges their distinctive interior hue?",
        "correct": "High accumulation of the red carotenoid lycopene",
        "distractors": ["Anthocyanin synthesis triggered by cold nights", "Extreme levels of vitamin B12", "Excessive chlorophyll degradation"],
        "d": 3
    },
    {
        "q": "Blood oranges (such as Moro and Tarocco) produce their deep crimson interior flesh through high levels of which pigments, stimulated by cool Mediterranean night temperatures?",
        "correct": "Anthocyanins",
        "distractors": ["Carotenoids", "Betalains", "Curcumins"],
        "d": 2
    },
    {
        "q": "What famous American plant breeder in Santa Rosa, California developed the Shasta daisy, the Burbank potato, and the plumcot?",
        "correct": "Luther Burbank",
        "distractors": ["George Washington Carver", "Gregor Mendel", "Norman Borlaug"],
        "d": 1
    },
    {
        "q": "The Russet Burbank potato, the primary potato used for fast-food French fries worldwide, was developed from a seedling of which variety?",
        "correct": "Burbank potato (selected by Luther Burbank)",
        "distractors": ["Yukon Gold", "Kennebec", "Irish Cobbler"],
        "d": 2
    },
    {
        "q": "Which yellow-fleshed potato variety was bred at the University of Guelph in Ontario and officially released in 1980?",
        "correct": "Yukon Gold",
        "distractors": ["Fingerling", "Adirondack Blue", "Red Pontiac"],
        "d": 2
    },

    # 46-65: Horticultural Practices & Cultivation Techniques (d1-d3)
    {
        "q": "What ancient horticultural practice involves training a fruit tree to grow flat against a wall, lattice, or wire trellis?",
        "correct": "Espalier",
        "distractors": ["Topiary", "Pollarding", "Pleaching"],
        "d": 2
    },
    {
        "q": "Why do commercial orchardists heavily favor dwarf apple trees over standard full-sized trees?",
        "correct": "They yield fruit years earlier, produce more fruit per acre, and allow easier pruning and harvesting from the ground",
        "distractors": ["Their fruit contains twice as much vitamin C", "They do not require water after initial planting", "They are immune to all bacterial and fungal diseases"],
        "d": 2
    },
    {
        "q": "What grafting technique uses a single dormant vegetative bud inserted into a T-shaped slit in the bark of a rootstock?",
        "correct": "T-budding (shield budding)",
        "distractors": ["Whip and tongue grafting", "Cleft grafting", "Bridge grafting"],
        "d": 3
    },
    {
        "q": "What is the critical physiological requirement for a successful graft union between a scion and rootstock?",
        "correct": "The vascular cambium layers of both plants must align and make intimate contact",
        "distractors": ["Both plants must have identical leaf surface areas", "The roots of the scion must be kept submerged in fertilizer", "Both branches must be coated in petroleum jelly before cutting"],
        "d": 3
    },
    {
        "q": "Why are commercial fruit trees almost universally propagated via clonal propagation (grafting or cuttings) rather than from seeds?",
        "correct": "Clonal propagation ensures exact genetic copies with predictable fruit quality and flavor",
        "distractors": ["Seed propagation produces plants that cannot photosynthesize", "Seeds from fruit trees are illegal to plant without federal permits", "Fruit seeds can only germinate in pressurized laboratory chambers"],
        "d": 1
    },
    {
        "q": "What agricultural practice involves growing white asparagus by piling mounds of soil over the crowns to exclude all sunlight?",
        "correct": "Blanching (etiolation)",
        "distractors": ["Stratification", "Girdling", "Scarification"],
        "d": 2
    },
    {
        "q": "Why is white asparagus white rather than green?",
        "correct": "Deprived of sunlight, the emerging spears cannot synthesize green chlorophyll",
        "distractors": ["It is treated with sulfur dioxide gas while growing", "It is genetically devoid of all chloroplasts", "It is bleached by calcium carbonate in the soil"],
        "d": 1
    },
    {
        "q": "Belgian endive (witloof) undergoes a secondary forced growing cycle in total darkness to produce its compact, pale yellow heads. What is this process called?",
        "correct": "Forcing (chicon production)",
        "distractors": ["Bletting", "Vernalization", "Scarification"],
        "d": 3
    },
    {
        "q": "What term describes the intentional removal of excess immature fruits from a tree in spring to ensure remaining fruits grow to marketable size?",
        "correct": "Fruit thinning",
        "distractors": ["Topping", "Pinching back", "Debudding"],
        "d": 1
    },
    {
        "q": "If a fruit tree bears an enormous crop of small fruit one year and almost no fruit the following year, it is exhibiting what common habit?",
        "correct": "Biennial bearing (alternate bearing)",
        "distractors": ["Senescence shock", "Dormancy wilt", "Epigenetic collapse"],
        "d": 2
    },
    {
        "q": "What horticultural practice involves cutting a narrow ring of bark and phloem around a tree trunk or branch to trap carbohydrates in the canopy?",
        "correct": "Girdling (cincturing)",
        "distractors": ["Coppicing", "Layering", "Root pruning"],
        "d": 3
    },
    {
        "q": "What system of soil-less cultivation suspends plant roots in air inside a closed chamber and mists them with nutrient solution?",
        "correct": "Aeroponics",
        "distractors": ["Hydroponics", "Aquaponics", "Geoponics"],
        "d": 2
    },
    {
        "q": "What is the primary difference between hydroponics and aquaponics?",
        "correct": "Aquaponics combines hydroponic plant cultivation with aquaculture (raising aquatic animals like fish) in a symbiotic cycle",
        "distractors": ["Hydroponics uses only saltwater while aquaponics uses distilled rain water", "Aquaponics relies entirely on synthetic petrochemical fertilizers", "Hydroponics uses soil mixed with volcanic pumice"],
        "d": 1
    },
    {
        "q": "What cold-temperature exposure triggers winter wheat and certain biennial vegetables (like carrots and cabbages) to flower in their second year?",
        "correct": "Vernalization",
        "distractors": ["Stratification", "Scarification", "Photoperiodism"],
        "d": 3
    },
    {
        "q": "What term describes treating seeds with moisture and chilling to break embryonic dormancy before spring planting?",
        "correct": "Stratification",
        "distractors": ["Scarification", "Vernalization", "Inoculation"],
        "d": 2
    },
    {
        "q": "What process involves nicking or scratching the hard, impermeable seed coat of certain legumes to allow water absorption and germination?",
        "correct": "Scarification",
        "distractors": ["Stratification", "Maceration", "Pelleting"],
        "d": 3
    },
    {
        "q": "Why do commercial orchardists paint the lower trunks of young fruit trees with white latex paint?",
        "correct": "To reflect winter sunlight and prevent southwest injury (sunscald) and bark splitting",
        "distractors": ["To prevent deer from smelling the bark sap", "To seal nitrogen gas inside the wood", "To sterilize viral pathogens from the atmosphere"],
        "d": 2
    },
    {
        "q": "What pruning cut removes an entire branch back to its point of origin on the parent stem or trunk?",
        "correct": "Thinning cut",
        "distractors": ["Heading cut", "Pinching cut", "Shearing cut"],
        "d": 3
    },
    {
        "q": "What pruning system opens the center of stone fruit trees (peaches, plums) into an inverted cone or vase shape to maximize sunlight penetration?",
        "correct": "Open center (vase) system",
        "distractors": ["Central leader system", "Spindle bush system", "Trellis cordons"],
        "d": 2
    },
    {
        "q": "What is the common term for vigorous, upright vegetative shoots that sprout vertically from the rootstock or main branches of fruit trees and sap energy?",
        "correct": "Suckers and water sprouts",
        "distractors": ["Calyx tendrils", "Spur clusters", "Petioles"],
        "d": 1
    },

    # 66-80: Citrus Origins & Hybrids (d1-d3)
    {
        "q": "Genomic studies reveal that almost all cultivated modern citrus varieties derive from hybridization among which three ancestral wild species?",
        "correct": "Citron, Pomelo, and Mandarin",
        "distractors": ["Lemon, Lime, and Orange", "Bergamot, Kumquat, and Grapefruit", "Key lime, Yuzu, and Clementine"],
        "d": 3
    },
    {
        "q": "The sweet orange (Citrus × sinensis) is a hybrid between which two ancestral citrus parents?",
        "correct": "Pomelo and Mandarin",
        "distractors": ["Citron and Kumquat", "Lemon and Lime", "Grapefruit and Tangerine"],
        "d": 3
    },
    {
        "q": "The grapefruit (Citrus × paradisi) originated in the 18th century in Barbados as an accidental cross between which two citrus fruits?",
        "correct": "Sweet orange and Pomelo",
        "distractors": ["Lemon and Lime", "Mandarin and Citron", "Kumquat and Bergamot"],
        "d": 3
    },
    {
        "q": "Why was the grapefruit given the English common name 'grapefruit'?",
        "correct": "Its large fruits grow in clusters on the branches resembling bunches of grapes",
        "distractors": ["It was originally fermented into wine like grapes", "Its wild ancestor had purple skin like Concord grapes", "It was named by grape breeders in California"],
        "d": 1
    },
    {
        "q": "Which thick-rinded, ancient ancestral citrus fruit with very little juice was historically prized for its fragrant peel and Jewish Sukkot rituals?",
        "correct": "Citron (Etrog)",
        "distractors": ["Bergamot", "Pomelo", "Kumquat"],
        "d": 2
    },
    {
        "q": "Which bizarre citron variety produces segmented, elongated finger-like carpels resembling a human hand?",
        "correct": "Buddha's hand (Fingered citron)",
        "distractors": ["Dragon's eye", "Devil's claw", "Monkey orange"],
        "d": 1
    },
    {
        "q": "The bergamot orange, famous for flavoring Earl Grey tea and high-end perfumes, is primarily grown in which Italian coastal region?",
        "correct": "Calabria",
        "distractors": ["Tuscany", "Piedmont", "Veneto"],
        "d": 3
    },
    {
        "q": "Which small oval citrus fruit is eaten whole, including the sweet rind, while the pulp inside is pleasantly tart?",
        "correct": "Kumquat",
        "distractors": ["Meyer lemon", "Calamansi", "Rangpur"],
        "d": 1
    },
    {
        "q": "What aromatic East Asian citrus fruit, widely used in Japanese cuisine and ponzu sauce, can withstand freezing temperatures down to 15°F (-9°C)?",
        "correct": "Yuzu",
        "distractors": ["Kaffir lime", "Blood orange", "Sudachi"],
        "d": 2
    },
    {
        "q": "What distinct feature characterizes the leaves of the makrut (kaffir) lime tree, widely used in Thai curry pastes?",
        "correct": "Double leaves (an hourglass-shaped winged leaf with an attached petiole)",
        "distractors": ["Needle-like foliage like a pine", "Variegated purple and silver stripes", "Serrated triangular margins with stinging hairs"],
        "d": 3
    },
    {
        "q": "What devastating, incurable bacterial disease of citrus trees is spread by the Asian citrus psyllid and turns fruit green, bitter, and misshapen?",
        "correct": "Citrus greening (Huanglongbing / HLB)",
        "distractors": ["Citrus canker", "Tristeza virus", "Black spot blight"],
        "d": 3
    },
    {
        "q": "The Persian lime (Citrus × latifolia), the dominant lime sold in American supermarkets, is seedless because it is:",
        "correct": "A triploid (3n) hybrid",
        "distractors": ["Treated with gamma radiation", "A clone of a diploid orange", "Harvested before ovaries develop"],
        "d": 3
    },
    {
        "q": "Key limes (Citrus aurantiifolia) differ from Persian limes because Key limes are:",
        "correct": "Smaller, spherical, more acidic, aromatic, and contain seeds",
        "distractors": ["Sweet and completely devoid of acid", "Bright blue when fully ripe", "Grown exclusively underground"],
        "d": 1
    },
    {
        "q": "What small, round citrus hybrid native to the Philippines is also known as the Philippine lime or calamondin?",
        "correct": "Calamansi",
        "distractors": ["Yuzu", "Pomelo", "Finger lime"],
        "d": 2
    },
    {
        "q": "What native Australian citrus fruit contains caviar-like spherical juice vesicles that pop in the mouth?",
        "correct": "Australian finger lime",
        "distractors": ["Desert quandong", "Kakadu plum", "Davidson plum"],
        "d": 2
    },

    # 81-100: Historical Agriculture & Botanical Trade Milestones (d1-d3)
    {
        "q": "The Great Famine of Ireland (1845–1852) was triggered by which devastating oomycete pathogen that attacked the potato crop?",
        "correct": "Phytophthora infestans (Late blight)",
        "distractors": ["Fusarium oxysporum", "Puccinia graminis", "Claviceps purpurea"],
        "d": 2
    },
    {
        "q": "Why was the Irish potato crop so uniquely vulnerable to late blight in the 1840s?",
        "correct": "Overwhelming reliance on a genetic monoculture of a single potato variety called the 'Irish Lumper'",
        "distractors": ["Irish farmers refused to use copper fungicides", "Potatoes were planted only in submerged wetlands", "The potato had only been imported that same year"],
        "d": 2
    },
    {
        "q": "What French military pharmacist and agronomist championed the potato in 18th-century France by hosting potato feasts for nobles and intellectuals?",
        "correct": "Antoine-Augustin Parmentier",
        "distractors": ["Louis Pasteur", "Georges Cuvier", "Denis Diderot"],
        "d": 2
    },
    {
        "q": "In classical French culinary terminology, dishes prepared with or containing potatoes are often named in honor of Parmentier, such as:",
        "correct": "Potage Parmentier",
        "distractors": ["Sauce Mornay", "Béchamel", "Consommé Colbert"],
        "d": 2
    },
    {
        "q": "What Prussian monarch issued the famous 'Kartoffelbefehl' (Potato Decrees) in 1756 compelling peasants to plant potatoes to safeguard against famine?",
        "correct": "Frederick the Great (Frederick II)",
        "distractors": ["Otto von Bismarck", "Kaiser Wilhelm II", "Charlemagne"],
        "d": 2
    },
    {
        "q": "According to historical lore, how did Frederick the Great convince suspicious Prussian peasants to cultivate potatoes?",
        "correct": "He planted a royal potato field and posted royal guards around it, tempting curious peasants to steal the 'valuable' crop at night",
        "distractors": ["He banned bread and beer until everyone planted a field", "He paid gold coins for every potato brought to Berlin", "He personally cooked mashed potatoes in public town squares"],
        "d": 2
    },
    {
        "q": "Why were tomatoes feared as 'poison apples' by wealthy European aristocrats throughout the late 1500s and 1600s?",
        "correct": "The tomato's acidity leached toxic lead from the pewter plates used by aristocrats, causing lead poisoning",
        "distractors": ["Early wild tomatoes contained lethal cyanide", "Eating tomatoes was declared a heresy by the Pope", "The red juice was mistaken for arterial blood"],
        "d": 2
    },
    {
        "q": "What botanical family do tomatoes belong to that caused early European herbalists to distrust them due to associations with deadly nightshade (belladonna)?",
        "correct": "Solanaceae",
        "distractors": ["Apocynaceae", "Euphorbiaceae", "Ranunculaceae"],
        "d": 1
    },
    {
        "q": "What American folk legend and nurseryman, born John Chapman, traveled through Ohio, Indiana, and Illinois planting apple orchards from seed?",
        "correct": "Johnny Appleseed",
        "distractors": ["Paul Bunyan", "Davy Crockett", "Daniel Boone"],
        "d": 1
    },
    {
        "q": "Why did Johnny Appleseed grow his apple trees from seed rather than grafting scions of sweet dessert apples?",
        "correct": "His Swedenborgian religious beliefs opposed grafting as unnatural, and settlers needed sour cider apples for making hard alcoholic cider",
        "distractors": ["He did not know how to graft trees", "Grafting was outlawed under the Northwest Ordinance", "Wild animals ate grafted trees faster than seed-grown trees"],
        "d": 2
    },
    {
        "q": "What famous African American agricultural scientist at Tuskegee Institute developed over 300 products from peanuts and 100 from sweet potatoes?",
        "correct": "George Washington Carver",
        "distractors": ["Benjamin Banneker", "Percy Julian", "Norbert Rillieux"],
        "d": 1
    },
    {
        "q": "Why did George Washington Carver promote peanuts and sweet potatoes to Southern sharecroppers?",
        "correct": "To replenish nitrogen-depleted soils and provide nutritious alternatives to cotton monoculture",
        "distractors": ["To make peanut butter the official currency of Alabama", "Because cotton had gone extinct due to a viral epidemic", "To satisfy an exclusive military ration contract"],
        "d": 1
    },
    {
        "q": "What ancient trade route network facilitated the overland exchange of produce like peaches, pomegranates, and garlic across Eurasia?",
        "correct": "The Silk Road",
        "distractors": ["The Amber Road", "The King's Highway", "The Incense Route"],
        "d": 1
    },
    {
        "q": "Which fruit was used by the British Royal Navy beginning in the late 18th century to prevent scurvy among sailors, earning them the nickname 'limeys'?",
        "correct": "Lime (and lemon)",
        "distractors": ["Orange", "Grapefruit", "Pomegranate"],
        "d": 1
    },
    {
        "q": "What Scottish naval surgeon published 'A Treatise of the Scurvy' in 1753 proving that citrus fruits effectively cured scurvy?",
        "correct": "James Lind",
        "distractors": ["Alexander Fleming", "Joseph Lister", "Edward Jenner"],
        "d": 2
    },
    {
        "q": "What essential vitamin is deficient in the human body during the onset of scurvy?",
        "correct": "Vitamin C (Ascorbic acid)",
        "distractors": ["Vitamin A", "Vitamin D", "Vitamin B12"],
        "d": 1
    },
    {
        "q": "Why must humans obtain Vitamin C from fresh fruits and vegetables, unlike most other mammals that produce it endogenously?",
        "correct": "Humans carry a non-functional pseudo-gene for L-gulonolactone oxidase (GULO), the final enzyme in vitamin C synthesis",
        "distractors": ["Humans lack liver cells capable of processing glucose", "Human stomach acid destroys all self-synthesized vitamins", "Humans store too much copper in their bone marrow"],
        "d": 3
    },
    {
        "q": "In the 18th century, pineapples were so extraordinarily rare and expensive in Europe that wealthy elites would:",
        "correct": "Rent them for an evening to carry around at lavish parties as a status symbol of wealth and hospitality",
        "distractors": ["Lock them in bank vaults as collateral for real estate loans", "Offer a single pineapple in exchange for a castle", "Use them exclusively to crown royalty at coronations"],
        "d": 2
    },
    {
        "q": "What architectural ornamentation frequently seen on historic fence posts, stone gates, and doorways depicts a fruit symbolizing warm hospitality?",
        "correct": "Pineapple",
        "distractors": ["Pomegranate", "Grape cluster", "Acorn"],
        "d": 1
    },
    {
        "q": "What British WWII government propaganda campaign claimed that RAF pilots ate excessive carrots to explain their superior night-fighting abilities?",
        "correct": "A cover story designed to conceal the secret military invention of airborne radar",
        "distractors": ["A campaign to boost wartime carrot sales for private farm syndicates", "A psychological warfare plot to convince Germany to ration meat", "A scientific experiment to cure congenital night blindness"],
        "d": 2
    }
]

if __name__ == "__main__":
    build_batch(BATCH_3, "tools/staging/produce_batch3.json", batch_num=3)
