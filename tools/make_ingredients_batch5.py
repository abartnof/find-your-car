#!/usr/bin/env python3
"""
Generate Batch 5: Celebrated European Dishes (100 questions).
30 Easy (d=1), 40 Medium (d=2), 30 Hard (d=3).
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ingredients_builder import build_batch

raw_questions = [
    # --- EASY (d=1, 30 questions) ---
    {
        "q": "Which cured Italian pork product made from the jowl is the authentic meat for Spaghetti alla Carbonara?",
        "correct": "Guanciale",
        "distractors": ["Prosciutto cotto", "Pancetta affumicata", "Bologna"],
        "d": 1
    },
    {
        "q": "Which ingredient is famously omitted in authentic Roman Spaghetti alla Carbonara, despite common international additions?",
        "correct": "Heavy cream",
        "distractors": ["Egg yolks", "Pecorino Romano", "Black pepper"],
        "d": 1
    },
    {
        "q": "Which hard sheep's milk cheese is the quintessential traditional cheese used in Roman Cacio e Pepe and Carbonara?",
        "correct": "Pecorino Romano",
        "distractors": ["Gorgonzola", "Fontina", "Taleggio"],
        "d": 1
    },
    {
        "q": "What two primary seasoning ingredients, alongside starchy pasta cooking water, define Roman Cacio e Pepe?",
        "correct": "Pecorino Romano cheese and freshly cracked black pepper",
        "distractors": ["Parmesan cheese and heavy cream", "Garlic and olive oil", "Butter and sage"],
        "d": 1
    },
    {
        "q": "Which cured pork jowl cut provides the fat and savory base for authentic Pasta all'Amatriciana?",
        "correct": "Guanciale",
        "distractors": ["Lardo", "Pork loin", "Speck"],
        "d": 1
    },
    {
        "q": "Which vegetable is the star ingredient of the Sicilian pasta dish Pasta alla Norma?",
        "correct": "Fried eggplant (aubergine)",
        "distractors": ["Zucchini", "Artichoke hearts", "Bell peppers"],
        "d": 1
    },
    {
        "q": "Which salted, aged ricotta cheese is grated over Pasta alla Norma before serving?",
        "correct": "Ricotta salata",
        "distractors": ["Fresh ricotta", "Mozzarella di bufala", "Provolone piccante"],
        "d": 1
    },
    {
        "q": "Which meat cut is traditionally used to prepare authentic Italian Osso Buco alla Milanese?",
        "correct": "Cross-cut veal shanks with marrow bone",
        "distractors": ["Beef flank steak", "Pork chops", "Boneless leg of lamb"],
        "d": 1
    },
    {
        "q": "Which zesty Italian herb garnish of minced lemon zest, garlic, and parsley finishes Osso Buco?",
        "correct": "Gremolata",
        "distractors": ["Salsa verde", "Salmoriglio", "Pesto"],
        "d": 1
    },
    {
        "q": "Which precious golden spice gives authentic Risotto alla Milanese its rich golden color and earthy aroma?",
        "correct": "Saffron threads",
        "distractors": ["Turmeric", "Curry powder", "Paprika"],
        "d": 1
    },
    {
        "q": "Which high-starch Italian short-grain rice variety is the most famous choice for cooking creamy risotto?",
        "correct": "Arborio or Carnaroli rice",
        "distractors": ["Basmati rice", "Jasmine rice", "Wild rice"],
        "d": 1
    },
    {
        "q": "Which Roman veal dish features thinly sliced veal topped with prosciutto crudo and fresh sage leaves pinned with a toothpick?",
        "correct": "Saltimbocca alla Romana",
        "distractors": ["Veal Milanese", "Piccata di vitello", "Scaloppine al limone"],
        "d": 1
    },
    {
        "q": "Which aromatic herb leaf is pinned directly onto the veal in traditional Saltimbocca alla Romana?",
        "correct": "Sage leaf",
        "distractors": ["Basil leaf", "Rosemary sprig", "Bay leaf"],
        "d": 1
    },
    {
        "q": "Which famous French dish consists of beef tenderloin wrapped in mushroom duxelles, prosciutto, and baked in puff pastry?",
        "correct": "Beef Wellington",
        "distractors": ["Tournedos Rossini", "Boeuf en croûte", "Chateaubriand"],
        "d": 1
    },
    {
        "q": "Which finely minced seasoned mixture of sautéed mushrooms, shallots, and herbs coats the meat in Beef Wellington?",
        "correct": "Mushroom duxelles",
        "distractors": ["Mushroom velouté", "Tapenade", "Mirepoix"],
        "d": 1
    },
    {
        "q": "Which pastry dough is wrapped around the exterior of a classic Beef Wellington to bake to a golden crisp?",
        "correct": "Puff pastry",
        "distractors": ["Shortcrust pastry", "Filo pastry", "Choux pastry"],
        "d": 1
    },
    {
        "q": "Which summer vegetable medley from Provence combines stewed eggplant, zucchini, bell peppers, tomatoes, onions, and herbs?",
        "correct": "Ratatouille",
        "distractors": ["Piperade", "Tian provençal", "Barigoule"],
        "d": 1
    },
    {
        "q": "Which classic French savory egg tart from northeastern France features a custard of eggs and heavy cream with smoked bacon lardons?",
        "correct": "Quiche Lorraine",
        "distractors": ["Tarte flambée", "Pissaladière", "Gougère"],
        "d": 1
    },
    {
        "q": "Which cooking method involves slowly cooking duck legs completely submerged in rendered duck fat at low temperature?",
        "correct": "Confit",
        "distractors": ["Braising", "Sous vide", "Poaching"],
        "d": 1
    },
    {
        "q": "Which Spanish national dish is a thick, round omelet made by pan-frying sliced potatoes and beaten eggs in olive oil?",
        "correct": "Tortilla Española",
        "distractors": ["Frittata", "Revuelto", "Shakshuka"],
        "d": 1
    },
    {
        "q": "Which Spanish tapa features tender shrimp sizzled in olive oil with generous sliced garlic, dried chili peppers, and parsley?",
        "correct": "Gambas al Ajillo",
        "distractors": ["Boquerones en vinagre", "Calamares a la romana", "Puntillitas"],
        "d": 1
    },
    {
        "q": "Which cephalopod is boiled until tender and sprinkled with coarse salt, sweet pimentón paprika, and olive oil in Pulpo a la Gallega?",
        "correct": "Octopus",
        "distractors": ["Squid", "Cuttlefish", "Scallops"],
        "d": 1
    },
    {
        "q": "Which Greek baked casserole layers spiced ground meat, sliced eggplant, and potatoes beneath a thick baked layer of béchamel sauce?",
        "correct": "Moussaka",
        "distractors": ["Pastitsio", "Spanakopita", "Briami"],
        "d": 1
    },
    {
        "q": "Which paper-thin unleavened pastry dough is layered with butter to encase Greek Spanakopita and Baklava?",
        "correct": "Phyllo pastry (Filo)",
        "distractors": ["Puff pastry", "Shortcrust pastry", "Choux pastry"],
        "d": 1
    },
    {
        "q": "Which leafy green is the essential filling combined with feta cheese and dill inside Greek Spanakopita?",
        "correct": "Spinach",
        "distractors": ["Kale", "Swiss chard", "Grape leaves"],
        "d": 1
    },
    {
        "q": "What type of leaves are stuffed with a mixture of seasoned rice, herbs, and pine nuts to make traditional Greek Dolmades?",
        "correct": "Grape leaves",
        "distractors": ["Cabbage leaves", "Fig leaves", "Beet leaves"],
        "d": 1
    },
    {
        "q": "Which minced meat is the mandatory protein in an authentic British Shepherd's Pie (as opposed to Cottage Pie)?",
        "correct": "Ground lamb",
        "distractors": ["Ground beef", "Ground pork", "Ground turkey"],
        "d": 1
    },
    {
        "q": "What vegetable dish forms the crispy, browned top crust of a classic British Shepherd's Pie?",
        "correct": "Mashed potatoes",
        "distractors": ["Puff pastry crust", "Breadcrumb crumble", "Grated cheddar cheese only"],
        "d": 1
    },
    {
        "q": "Which side dish of dried marrowfat peas boiled into a thick green paste is the iconic partner to British fish and chips?",
        "correct": "Mushy peas",
        "distractors": ["Pea puree with mint", "Split pea soup", "Creamed peas"],
        "d": 1
    },
    {
        "q": "Which classic Irish potato dish blends creamy mashed potatoes with tender chopped boiled cabbage or kale, butter, and scallions?",
        "correct": "Colcannon",
        "distractors": ["Champ", "Boxty", "Coddle"],
        "d": 1
    },

    # --- MEDIUM (d=2, 40 questions) ---
    {
        "q": "Which two meats are the traditional meats simmered in an authentic Paella Valenciana, along with green beans and giant lima beans?",
        "correct": "Rabbit and chicken",
        "distractors": ["Shrimp and mussels", "Pork ribs and chorizo", "Duck and snails only"],
        "d": 2
    },
    {
        "q": "What is the broad, flat large white lima bean variety uniquely essential to authentic Paella Valenciana called?",
        "correct": "Garrofó beans",
        "distractors": ["Cannellini beans", "Fava beans", "Butter beans"],
        "d": 2
    },
    {
        "q": "What is the prized, crispy caramelized crust of toasted rice that forms on the bottom of a proper Spanish paella pan called?",
        "correct": "Socarrat",
        "distractors": ["Tadigo", "Tahdig", "Kruska"],
        "d": 2
    },
    {
        "q": "Which short-grain Spanish rice variety from Valencia, famous for absorbing three times its volume in broth without bursting, is the gold standard for paella?",
        "correct": "Bomba rice",
        "distractors": ["Arborio rice", "Calasparra rice", "Carnaroli rice"],
        "d": 2
    },
    {
        "q": "Which Neapolitan pasta sauce features canned tomatoes, black Gaeta olives, capers, garlic, anchovies, and red chili flakes?",
        "correct": "Pasta alla Puttanesca",
        "distractors": ["Pasta all'Arrabbiata", "Pasta alla Marinara", "Pasta alla Gricia"],
        "d": 2
    },
    {
        "q": "Which spicy Roman tomato sauce is flavored with garlic, tomatoes, and dried red chili peppers cooked in olive oil?",
        "correct": "Sugo all'Arrabbiata",
        "distractors": ["Sugo all'Amatriciana", "Sugo alla Puttanesca", "Sugo alla Nerano"],
        "d": 2
    },
    {
        "q": "Which classic Roman pasta dish, considered the ancestor to Amatriciana and Carbonara, contains only guanciale, pecorino cheese, and black pepper?",
        "correct": "Pasta alla Gricia",
        "distractors": ["Cacio e Pepe", "Pasta al Limone", "Pasta all'Aglione"],
        "d": 2
    },
    {
        "q": "Which Amalfi Coast pasta dish features fried zucchini rounds tossed with spaghetti, provolone del Monaco cheese, and fresh basil?",
        "correct": "Spaghetti alla Nerano",
        "distractors": ["Pasta alla Norma", "Spaghetti alle Vongole", "Pasta al Pesto"],
        "d": 2
    },
    {
        "q": "Which Italian seafood pasta dish features small clams cooked in white wine, garlic, olive oil, and fresh parsley with spaghetti?",
        "correct": "Spaghetti alle Vongole",
        "distractors": ["Spaghetti allo Scoglio", "Spaghetti ai Frutti di Mare", "Calamarata"],
        "d": 2
    },
    {
        "q": "Which Piedmontese dish features thin slices of cold poached veal blanketed in a smooth, creamy sauce made of tuna, capers, anchovies, and mayonnaise?",
        "correct": "Vitello Tonnato",
        "distractors": ["Carpaccio di manzo", "Carne cruda all'albese", "Bresaola della Valtellina"],
        "d": 2
    },
    {
        "q": "Which Venetian appetizer created at Harry's Bar consists of paper-thin raw beef sirloin drizzled with a light mustard-mayonnaise sauce?",
        "correct": "Beef Carpaccio",
        "distractors": ["Vitello Tonnato", "Steak tartare", "Bresaola"],
        "d": 2
    },
    {
        "q": "Which French beef dish features raw high-quality minced beef seasoned with capers, shallots, Worcestershire sauce, Dijon mustard, and topped with a raw egg yolk?",
        "correct": "Steak Tartare",
        "distractors": ["Beef Carpaccio", "Filet Américain", "Tournedos Rossini"],
        "d": 2
    },
    {
        "q": "Which opulent French steak preparation places a seared beef tournedos atop a fried crouton, topped with a slice of pan-seared foie gras and black truffle slices?",
        "correct": "Tournedos Rossini",
        "distractors": ["Steak au Poivre", "Chateaubriand", "Entrecôte bordelaise"],
        "d": 2
    },
    {
        "q": "Which French steak dish features beef steak heavily coated in coarsely crushed whole black peppercorns, flambéed with Cognac and finished with heavy cream?",
        "correct": "Steak au Poivre",
        "distractors": ["Steak Diane", "Tournedos Rossini", "Entrecôte Café de Paris"],
        "d": 2
    },
    {
        "q": "Which complex compound butter seasoned with chicken livers, curry powder, anchovies, herbs, and spices was created in Geneva for steak?",
        "correct": "Café de Paris butter",
        "distractors": ["Beurre Maître d'Hôtel", "Beurre Marchand de Vin", "Beurre d'Anchois"],
        "d": 2
    },
    {
        "q": "Which French sweet-and-sour culinary reduction of caramelized sugar deglazed with vinegar is the foundation for Duck à l'Orange?",
        "correct": "Gastrique",
        "distractors": ["Agrodolce", "Coulis", "Glace de canard"],
        "d": 2
    },
    {
        "q": "Which Alsatian specialty, meaning 'tarte baked in flames', features rolled bread dough topped with crème fraîche, sliced onions, and smoked bacon lardons?",
        "correct": "Tarte Flambée (Flammekueche)",
        "distractors": ["Quiche Lorraine", "Pissaladière", "Fugasse"],
        "d": 2
    },
    {
        "q": "Which savory flatbread tart from Nice, France, features caramelized onions, black Niçoise olives, and salted anchovy fillets baked on bread dough?",
        "correct": "Pissaladière",
        "distractors": ["Tarte Flambée", "Socca", "Fougasse"],
        "d": 2
    },
    {
        "q": "Which thin, unleavened pancake originating in Nice and Liguria is made entirely from chickpea flour, water, olive oil, and coarse black pepper, baked in a copper pan?",
        "correct": "Socca (Farinata)",
        "distractors": ["Panisse", "Pissaladière", "Polenta"],
        "d": 2
    },
    {
        "q": "Which French fries-like finger food from Marseille is made from chilled, sliced chickpea flour polenta deep-fried in oil?",
        "correct": "Panisse",
        "distractors": ["Socca", "Gougères", "Pommes dauphine"],
        "d": 2
    },
    {
        "q": "Which classic French savory baked choux pastry puffs are blended with grated Gruyère or Comté cheese before baking?",
        "correct": "Gougères",
        "distractors": ["Profiteroles", "Gnocchi à la parisienne", "Éclairs"],
        "d": 2
    },
    {
        "q": "Which French potato preparation consists of thinly sliced potatoes layered with garlic, heavy cream, and butter, baked in a shallow gratin dish?",
        "correct": "Gratin Dauphinois",
        "distractors": ["Pommes Anna", "Pommes Aligot", "Pommes Duchesse"],
        "d": 2
    },
    {
        "q": "Which classic French potato cake features thinly sliced potatoes arranged in neat overlapping concentric circles and baked with clarified butter?",
        "correct": "Pommes Anna",
        "distractors": ["Gratin Dauphinois", "Rösti", "Pommes Darphin"],
        "d": 2
    },
    {
        "q": "Which elastic, stretchy potato puree from the Aubrac region of France is made by beating mashed potatoes with garlic, cream, and fresh Tomme de Laguiole cheese?",
        "correct": "Aligot",
        "distractors": ["Truffade", "Gratin Dauphinois", "Pommes puree"],
        "d": 2
    },
    {
        "q": "Which Swiss national dish consists of grated parboiled or raw potatoes pressed into a cake and pan-fried crisp in butter on both sides?",
        "correct": "Rösti",
        "distractors": ["Aligot", "Tartiflette", "Kartoffelpuffer"],
        "d": 2
    },
    {
        "q": "Which Savoyard gratin features sliced potatoes, smoked lardons, onions, and white wine smothered under a whole wheel of creamy Reblochon cheese?",
        "correct": "Tartiflette",
        "distractors": ["Gratin Dauphinois", "Raclette", "Aligot"],
        "d": 2
    },
    {
        "q": "Which semi-hard Swiss cow's milk cheese is traditionally melted under a broiler or open fire and scraped over boiled new potatoes and gherkins?",
        "correct": "Raclette",
        "distractors": ["Gruyère", "Appenzeller", "Emmental"],
        "d": 2
    },
    {
        "q": "Which Swiss hot communal cheese dish combines melted Gruyère and Vacherin Fribourgeois cheeses with dry white wine, garlic, and kirsch in a caquelon?",
        "correct": "Cheese Fondue",
        "distractors": ["Raclette", "Tartiflette", "Aligot"],
        "d": 2
    },
    {
        "q": "Which Spanish Basque salt cod preparation relies on gently swirling salt cod steaks in warm garlic-infused olive oil to create an emulsion with fish gelatin?",
        "correct": "Bacalao al Pil-Pil",
        "distractors": ["Bacalao a la Vizcaína", "Brandade de Morue", "Bacalao al Ajoarriero"],
        "d": 2
    },
    {
        "q": "Which Basque salt cod dish is simmered in a rich red sauce made from sweet red choricero pepper pulp and slow-cooked onions?",
        "correct": "Bacalao a la Vizcaína",
        "distractors": ["Bacalao al Pil-Pil", "Marmitako", "Merluza en salsa verde"],
        "d": 2
    },
    {
        "q": "Which Basque tuna fisherman's stew combines fresh bonito tuna with stewed potatoes, onions, green peppers, and choricero pepper flesh?",
        "correct": "Marmitako",
        "distractors": ["Caldeirada", "Suquet de peix", "Zarzuela"],
        "d": 2
    },
    {
        "q": "Which rich white bean stew from Asturias, Spain, is simmered with the 'compango': smoked chorizo, morcilla blood sausage, and pork shoulder?",
        "correct": "Fabada Asturiana",
        "distractors": ["Cocido Madrileño", "Cassoulet", "Olla podrida"],
        "d": 2
    },
    {
        "q": "Which hearty chickpea-based Madrid stew is eaten in three courses: noodle soup, followed by chickpeas and vegetables, and finally stewed meats?",
        "correct": "Cocido Madrileño",
        "distractors": ["Fabada Asturiana", "Escudella", "Puchero andaluz"],
        "d": 2
    },
    {
        "q": "Which iconic Portuguese sandwich from Porto layers toasted bread with steak, fresh sausage, linguiça, and ham, wrapped in melted cheese and smothered in beer sauce?",
        "correct": "Francesinha",
        "distractors": ["Bifana", "Prego", "Sandes de pernil"],
        "d": 2
    },
    {
        "q": "Which Greek baked pasta dish, often called Greek lasagna, combines tubular pasta, cinnamon-spiced ground beef, and a thick baked béchamel topping?",
        "correct": "Pastitsio",
        "distractors": ["Moussaka", "Giouvetsi", "Kokkinisto"],
        "d": 2
    },
    {
        "q": "Which Greek baked casserole dish consists of tender beef or lamb braised in a rich tomato sauce with orzo pasta (kritharaki) and kefalotyri cheese?",
        "correct": "Giouvetsi",
        "distractors": ["Pastitsio", "Stifado", "Kleftiko"],
        "d": 2
    },
    {
        "q": "Which Greek rustic stew features tender chunks of beef or rabbit braised with whole baby pearl onions, red wine, tomatoes, cinnamon, and allspice?",
        "correct": "Stifado",
        "distractors": ["Giouvetsi", "Kleftiko", "Sofrito"],
        "d": 2
    },
    {
        "q": "Which Greek dish, meaning 'bandit's meat', consists of bone-in lamb marinated with lemon, garlic, and oregano, wrapped tightly in parchment and slow-roasted?",
        "correct": "Kleftiko",
        "distractors": ["Souvlaki", "Gyros", "Kontosouvli"],
        "d": 2
    },
    {
        "q": "Which British savory dish features whole pork sausages baked inside a risen, golden-brown Yorkshire pudding batter, served with onion gravy?",
        "correct": "Toad in the Hole",
        "distractors": ["Bangers and Mash", "Pigs in Blankets", "Lancashire Hotpot"],
        "d": 2
    },
    {
        "q": "Which British slow-cooked lamb and sliced potato casserole originated in northern mill towns, baked with overlapping potato slices on top?",
        "correct": "Lancashire Hotpot",
        "distractors": ["Shepherd's Pie", "Scouse", "Stovies"],
        "d": 2
    },

    # --- HARD (d=3, 30 questions) ---
    {
        "q": "Which ancient Roman sweet and sour braised pork or wild boar dish was prepared with pine nuts, raisins, dark chocolate, and red wine vinegar?",
        "correct": "Cinghiale in Dolceforte",
        "distractors": ["Stracotto di manzo", "Peposo all'Imprunetina", "Brasato al Barolo"],
        "d": 3
    },
    {
        "q": "Which Tuscan peppered beef stew from Impruneta, famously eaten by kiln workers who built the Florence Duomo, uses only beef, Chianti wine, garlic, and copious black peppercorns without oil?",
        "correct": "Peposo all'Imprunetina",
        "distractors": ["Cinghiale in Dolceforte", "Brasato al Barolo", "Stracotto alla fiorentina"],
        "d": 3
    },
    {
        "q": "Which Piedmontese braised beef roast is marinated and slowly simmered for hours in an entire bottle of noble Nebbiolo Barolo wine with spices?",
        "correct": "Brasato al Barolo",
        "distractors": ["Stracotto di manzo", "Bollito Misto", "Carbonnade"],
        "d": 3
    },
    {
        "q": "Which opulent northern Italian feast dish consists of seven different cuts of boiled meats, seven garnish meats, and seven sauces including salsa verde and mostarda?",
        "correct": "Gran Bollito Misto",
        "distractors": ["Cassoeula", "Cotechino con lenticchie", "Porchetta"],
        "d": 3
    },
    {
        "q": "Which winter stew from Lombardy, Italy, cooks pork ribs, pork rind, and verzini sausages with sweet winter savoy cabbage after the first autumn frost?",
        "correct": "Cassoeula",
        "distractors": ["Gran Bollito Misto", "Paniscia novarese", "Pizzoccheri"],
        "d": 3
    },
    {
        "q": "Which flat ribbon pasta from the Valtellina valley in Lombardy is made with buckwheat flour, cooked with Savoy cabbage, potatoes, butter, and Bitto cheese?",
        "correct": "Pizzoccheri",
        "distractors": ["Strangozzi", "Testaroli", "Bigoli"],
        "d": 3
    },
    {
        "q": "Which ancient Tuscan pasta, considered one of the oldest recorded pasta shapes, is cooked as a batter in cast iron pans (testi), cut into diamonds, and tossed with pesto?",
        "correct": "Testaroli",
        "distractors": ["Pizzoccheri", "Garganelli", "Corzetti"],
        "d": 3
    },
    {
        "q": "Which Ligurian stamped coin-shaped pasta discs are embossed with wooden hand stamps depicting family crests or symbols?",
        "correct": "Corzetti (Croxetti)",
        "distractors": ["Testaroli", "Trofie", "Orecchiette"],
        "d": 3
    },
    {
        "q": "Which small, tapered, spiral pasta shape twisted by hand in Liguria is the classic traditional pairing for Pesto Genovese along with boiled green beans and potatoes?",
        "correct": "Trofie",
        "distractors": ["Garganelli", "Fusilli bucati", "Campanelle"],
        "d": 3
    },
    {
        "q": "Which Apulian ear-shaped pasta is traditionally tossed with sautéed cime di rapa (broccoli rabe), garlic, anchovies, and chili flakes?",
        "correct": "Orecchiette",
        "distractors": ["Cavatelli", "Strascinati", "Troccoli"],
        "d": 3
    },
    {
        "q": "Which Sardinian pasta dish features gnocchi-like ridged semolina shells (malloreddus) tossed in a rich saffron-scented pork sausage and tomato ragù?",
        "correct": "Malloreddus alla Campidanese",
        "distractors": ["Culurgiones", "Fregola sarda", "Pasta con le sarde"],
        "d": 3
    },
    {
        "q": "Which distinctive Sardinian handmade dumpling pocket, sealed with a decorative wheat-ear braid, is stuffed with mashed potatoes, pecorino cheese, and fresh mint?",
        "correct": "Culurgiones",
        "distractors": ["Malloreddus", "Seadas", "Panadas"],
        "d": 3
    },
    {
        "q": "Which famous Palermo pasta dish features fresh sardines, wild fennel fronds, pine nuts, raisins, saffron, and toasted seasoned breadcrumbs (muddica)?",
        "correct": "Pasta con le Sarde",
        "distractors": ["Spaghetti alla Bottarga", "Pasta alla Norma", "Spaghetti ai Ricci"],
        "d": 3
    },
    {
        "q": "Which salted and cured fish roe pouch, harvested from grey mullet or bluefin tuna and grated over pasta with olive oil, is known as Sardinian gold?",
        "correct": "Bottarga",
        "distractors": ["Colatura", "Mosciame", "Garum"],
        "d": 3
    },
    {
        "q": "Which Catalan fisherman's stew of assorted rockfish, clams, and prawns is cooked in a terracotta cazuela and thickened with a fried picada of almonds, garlic, and parsley?",
        "correct": "Suquet de Peix",
        "distractors": ["Marmitako", "Zarzuela", "Caldeirada"],
        "d": 3
    },
    {
        "q": "Which traditional Catalan culinary finishing paste, pounded in a mortar with toasted nuts, garlic, fried bread, and parsley, is stirred into stews at the end to thicken?",
        "correct": "Picada",
        "distractors": ["Sofregit", "Samfaina", "Allioli"],
        "d": 3
    },
    {
        "q": "Which Valencian and Catalan noodle dish is cooked identically to seafood paella in a shallow pan, substituting thin fideo noodles for rice to form a crispy top?",
        "correct": "Fideuà",
        "distractors": ["Arroz a banda", "Caldereta", "Escudella"],
        "d": 3
    },
    {
        "q": "Which Balearic lobster stew from Menorca features spiny European lobster cooked with tomatoes, onions, garlic, and a picada made with lobster coral?",
        "correct": "Caldereta de Langosta",
        "distractors": ["Suquet de peix", "Zarzuela", "Arroz caldoso"],
        "d": 3
    },
    {
        "q": "Which classic Portuguese salt cod casserole combines shredded bacalhau with matchstick fried potatoes, onions, and scrambled eggs, garnished with black olives?",
        "correct": "Bacalhau à Brás",
        "distractors": ["Bacalhau com Natas", "Bacalhau à Gomes de Sá", "Bacalhau à Zé do Pipo"],
        "d": 3
    },
    {
        "q": "Which Portuguese baked salt cod casserole layers flaked bacalhau with parboiled sliced potatoes, caramelized onions, and hard-boiled eggs in olive oil?",
        "correct": "Bacalhau à Gomes de Sá",
        "distractors": ["Bacalhau à Brás", "Bacalhau com Natas", "Açorda de Bacalhau"],
        "d": 3
    },
    {
        "q": "Which Portuguese rustic bread soup from the Alentejo region features day-old crusty bread soaked in boiling water infused with garlic, olive oil, copious fresh cilantro, and a poached egg?",
        "correct": "Açorda Alentejana",
        "distractors": ["Caldo Verde", "Migas Alentejanas", "Sopa da Pedra"],
        "d": 3
    },
    {
        "q": "Which traditional Portuguese Alentejo dish uses day-old breadcrumbs soaked in water and fried with pork lard, garlic, and pork spare ribs marinated in red pepper paste (massa de pimentão)?",
        "correct": "Migas Alentejanas",
        "distractors": ["Açorda Alentejana", "Cozido à Portuguesa", "Carne de Porco à Alentejana"],
        "d": 3
    },
    {
        "q": "Which iconic Portuguese surf-and-turf dish from the Alentejo combines cubes of marinated pork with fresh live clams, garlic, cilantro, and fried potato cubes?",
        "correct": "Carne de Porco à Alentejana",
        "distractors": ["Ameijoas à Bulhão Pato", "Bacalhau com Todos", "Feijoada à Transmontana"],
        "d": 3
    },
    {
        "q": "Which popular Portuguese clam appetizer steams fresh clams in olive oil, generous minced garlic, white wine, lemon juice, and a handful of chopped fresh cilantro?",
        "correct": "Amêijoas à Bulhão Pato",
        "distractors": ["Carne de Porco à Alentejana", "Caldeirada de Marisco", "Percebes cozidos"],
        "d": 3
    },
    {
        "q": "Which traditional national dish of Slovakia consists of small boiled potato dumplings tossed with melted sheep milk bryndza cheese and topped with smoked bacon cracklings?",
        "correct": "Bryndzové Halušky",
        "distractors": ["Strapačky", "Pierogi ruskie", "Kluski śląskie"],
        "d": 3
    },
    {
        "q": "Which traditional Silesian potato dumpling has a characteristic thumbprint dimple in the center designed to hold rich meat gravy?",
        "correct": "Kluski Śląskie",
        "distractors": ["Bryndzové halušky", "Knedlíky", "Pampuchy"],
        "d": 3
    },
    {
        "q": "Which Czech and Slovak steamed bread or potato dumplings are sliced with a wire cutter and served alongside roast pork, sauerkraut, and svíčková?",
        "correct": "Knedlíky",
        "distractors": ["Bryndzové halušky", "Kluski", "Uszka"],
        "d": 3
    },
    {
        "q": "Which Czech culinary national treasure features larded beef sirloin braised with root vegetables (carrots, celeriac, parsley root), pureed into a rich cream sauce with cranberries?",
        "correct": "Svíčková na Smetaně",
        "distractors": ["Guláš", "Vepřo knedlo zelo", "Moravský vrabec"],
        "d": 3
    },
    {
        "q": "Which traditional Scottish dish, celebrated on Burns Night, minces sheep's heart, liver, and lungs with oatmeal, suet, onions, and spices, simmered in a sheep's stomach?",
        "correct": "Haggis",
        "distractors": ["Black pudding", "White pudding", "Lorne sausage"],
        "d": 3
    },
    {
        "q": "Which two side vegetable mashes, colloquially called 'neeps and tatties', are the mandatory traditional accompaniment to Scottish haggis?",
        "correct": "Mashed yellow turnips (rutabaga) and mashed potatoes",
        "distractors": ["Mashed peas and parsnips", "Mashed carrots and sweet potatoes", "Mashed cabbage and onions"],
        "d": 3
    }
]

if __name__ == "__main__":
    out_path = "tools/staging/ingredients_batch5.json"
    build_batch(raw_questions, out_path, batch_num=5)
