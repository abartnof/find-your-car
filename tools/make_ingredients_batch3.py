#!/usr/bin/env python3
"""
Generate Batch 3: Master Sauces, Dressings, Marinades, Condiments & Spreads (100 questions).
30 Easy (d=1), 40 Medium (d=2), 30 Hard (d=3).
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ingredients_builder import build_batch

raw_questions = [
    # --- EASY (d=1, 30 questions) ---
    {
        "q": "Which green fruit is the essential mashed base of Mexican guacamole?",
        "correct": "Avocado",
        "distractors": ["Tomatillo", "Green bell pepper", "Zucchini"],
        "d": 1
    },
    {
        "q": "Which fresh green herb is the signature primary ingredient in classic Pesto Genovese?",
        "correct": "Genovese sweet basil",
        "distractors": ["Cilantro", "Mint", "Oregano"],
        "d": 1
    },
    {
        "q": "Which type of nut is traditionally ground with basil, garlic, and cheese in classic Pesto Genovese?",
        "correct": "Pine nuts",
        "distractors": ["Walnuts", "Almonds", "Pecans"],
        "d": 1
    },
    {
        "q": "Which French mother sauce is made by whisking warm melted butter into egg yolks and lemon juice?",
        "correct": "Hollandaise",
        "distractors": ["Béchamel", "Velouté", "Espagnole"],
        "d": 1
    },
    {
        "q": "Which French mother sauce consists of milk thickened with a white roux (butter and flour)?",
        "correct": "Béchamel",
        "distractors": ["Velouté", "Hollandaise", "Allemande"],
        "d": 1
    },
    {
        "q": "Which legume is cooked and pureed to form the smooth base of traditional Middle Eastern Hummus?",
        "correct": "Chickpeas (Garbanzo beans)",
        "distractors": ["Lentils", "Black beans", "Fava beans"],
        "d": 1
    },
    {
        "q": "Which sesame seed paste is blended with chickpeas, lemon juice, and garlic to make Hummus?",
        "correct": "Tahini",
        "distractors": ["Halva", "Za'atar", "Gomasio"],
        "d": 1
    },
    {
        "q": "Which roasted vegetable is pureed with tahini, garlic, and lemon juice to create Levantine Baba Ghanoush?",
        "correct": "Eggplant (Aubergine)",
        "distractors": ["Zucchini", "Cauliflower", "Sweet potato"],
        "d": 1
    },
    {
        "q": "Which dairy product forms the creamy foundation of traditional Greek Tzatziki sauce?",
        "correct": "Greek yogurt (strained yogurt)",
        "distractors": ["Sour cream", "Ricotta", "Feta brine"],
        "d": 1
    },
    {
        "q": "Which grated vegetable is salted, drained, and stirred into yogurt and garlic to make Tzatziki?",
        "correct": "Cucumber",
        "distractors": ["Zucchini", "Radish", "Celery"],
        "d": 1
    },
    {
        "q": "Which fresh green herb gives Argentinian Chimichurri its characteristic herbal taste and vibrant color?",
        "correct": "Flat-leaf parsley",
        "distractors": ["Dill", "Rosemary", "Tarragon"],
        "d": 1
    },
    {
        "q": "Which two ingredients form the classic foundation of mayonnaise via steady emulsification?",
        "correct": "Egg yolks and oil",
        "distractors": ["Milk and flour", "Butter and stock", "Cream and vinegar"],
        "d": 1
    },
    {
        "q": "Which French mother sauce is made by thickening a white stock (veal, chicken, or fish) with a blond roux?",
        "correct": "Velouté",
        "distractors": ["Béchamel", "Espagnole", "Hollandaise"],
        "d": 1
    },
    {
        "q": "Which classic French sauce derived from Hollandaise is flavored with tarragon, chervil, and a white wine vinegar reduction?",
        "correct": "Béarnaise sauce",
        "distractors": ["Maltese sauce", "Mornay sauce", "Soubise sauce"],
        "d": 1
    },
    {
        "q": "Which herb is the definitive seasoning in a classic Béarnaise sauce?",
        "correct": "Tarragon",
        "distractors": ["Cilantro", "Rosemary", "Sage"],
        "d": 1
    },
    {
        "q": "Which grated cheese is melted into béchamel sauce to create a classic Mornay sauce?",
        "correct": "Gruyère (or Parmesan)",
        "distractors": ["Mozzarella", "Brie", "Blue cheese"],
        "d": 1
    },
    {
        "q": "Which pickled vegetable is finely chopped and mixed with mayonnaise to make classic tartar sauce for fish?",
        "correct": "Pickled cucumbers (gherkins/capers)",
        "distractors": ["Pickled beets", "Pickled turnips", "Pickled garlic"],
        "d": 1
    },
    {
        "q": "What fermented condiment made from soybeans, roasted wheat, water, and salt is a pillar of East Asian cuisine?",
        "correct": "Soy sauce",
        "distractors": ["Fish sauce", "Oyster sauce", "Hoisin sauce"],
        "d": 1
    },
    {
        "q": "Which pungent green root paste is served alongside pickled ginger and soy sauce for sushi?",
        "correct": "Wasabi",
        "distractors": ["Matcha paste", "Guacamole", "Green harissa"],
        "d": 1
    },
    {
        "q": "What sweet and savory Asian brown sauce is commonly served with Peking duck and Moo Shu pork?",
        "correct": "Hoisin sauce",
        "distractors": ["Fish sauce", "Teriyaki sauce", "Ponzu"],
        "d": 1
    },
    {
        "q": "Which acidic red condiment made from cooked tomatoes, vinegar, sugar, and seasonings is America's favorite table sauce?",
        "correct": "Tomato ketchup",
        "distractors": ["Marinara", "Salsa roja", "Barbecue sauce"],
        "d": 1
    },
    {
        "q": "Which seed gives prepared table mustard, such as Dijon or American yellow mustard, its sharp pungency?",
        "correct": "Mustard seeds",
        "distractors": ["Coriander seeds", "Fenugreek seeds", "Caraway seeds"],
        "d": 1
    },
    {
        "q": "Which French city is world-famous for its smooth, tangy mustard made with brown mustard seeds and white wine or verjuice?",
        "correct": "Dijon",
        "distractors": ["Bordeaux", "Lyon", "Marseille"],
        "d": 1
    },
    {
        "q": "Which cultured dairy beverage provides the tangy base for classic homemade buttermilk ranch dressing?",
        "correct": "Buttermilk",
        "distractors": ["Evaporated milk", "Almond milk", "Coconut milk"],
        "d": 1
    },
    {
        "q": "Which small, salty, unripened flower buds pickled in brine are common in tartar sauce and piccata sauces?",
        "correct": "Capers",
        "distractors": ["Peppercorns", "Juniper berries", "Clove buds"],
        "d": 1
    },
    {
        "q": "Which allium gives authentic French aioli its indispensable pungent bite?",
        "correct": "Garlic",
        "distractors": ["Ginger", "Shallot", "Horseradish"],
        "d": 1
    },
    {
        "q": "Which small green fruit encased in a papery husk is the primary acidic ingredient in Mexican salsa verde?",
        "correct": "Tomatillo",
        "distractors": ["Green bell pepper", "Jalapeño", "Poblano"],
        "d": 1
    },
    {
        "q": "What sweet beehive product is paired with prepared mustard to make classic honey mustard dressing?",
        "correct": "Honey",
        "distractors": ["Maple syrup", "Agave nectar", "Molasses"],
        "d": 1
    },
    {
        "q": "Which spicy North African red pepper paste is seasoned with garlic, caraway seeds, coriander, and olive oil?",
        "correct": "Harissa",
        "distractors": ["Ajika", "Samba Oelek", "Sriracha"],
        "d": 1
    },
    {
        "q": "Which herb gives Green Goddess dressing its signature green hue along with tarragon, chives, and parsley?",
        "correct": "Chervil or parsley",
        "distractors": ["Oregano", "Lemongrass", "Rosemary"],
        "d": 1
    },

    # --- MEDIUM (d=2, 40 questions) ---
    {
        "q": "Which Catalan sauce is traditionally made by pounding roasted tomatoes, garlic, toasted almonds, hazelnuts, nyora peppers, and olive oil?",
        "correct": "Romesco sauce",
        "distractors": ["Salsa brava", "Mojo picón", "Xató"],
        "d": 2
    },
    {
        "q": "Which Spanish dried sweet pepper variety is essential to authentic Catalan Romesco sauce?",
        "correct": "Nyora pepper (ñora)",
        "distractors": ["Piquillo pepper", "Padrón pepper", "Guernica pepper"],
        "d": 2
    },
    {
        "q": "Which Provençal olive spread is made by finely chopping or blending cured black olives, capers, anchovies, and olive oil?",
        "correct": "Tapenade",
        "distractors": ["Anchoïade", "Rouille", "Pissalat"],
        "d": 2
    },
    {
        "q": "What French term describes a 1:1 mixture by weight of flour and fat (usually butter) cooked together to thicken sauces?",
        "correct": "Roux",
        "distractors": ["Beurre manié", "Slurry", "Liaison"],
        "d": 2
    },
    {
        "q": "What culinary thickener consists of equal parts soft uncooked butter and flour kneaded together and whisked into simmering sauces at the end?",
        "correct": "Beurre manié",
        "distractors": ["Roux", "Panade", "Velouté"],
        "d": 2
    },
    {
        "q": "What culinary term describes a thickening mixture of egg yolks and heavy cream whisked into hot sauces or soups?",
        "correct": "Liaison",
        "distractors": ["Emulsion", "Monté au beurre", "Roux blond"],
        "d": 2
    },
    {
        "q": "Which classic French butter sauce, originating in the Loire Valley, is made by emulsifying cold butter cubes into a white wine and shallot reduction?",
        "correct": "Beurre Blanc",
        "distractors": ["Hollandaise", "Beurre Noisette", "Beurre Rouge"],
        "d": 2
    },
    {
        "q": "What French culinary sauce, translating to 'hazelnut butter', consists of butter cooked until the milk solids turn golden brown with an aroma of toasted nuts?",
        "correct": "Beurre Noisette",
        "distractors": ["Beurre Blanc", "Beurre Noir", "Ghee"],
        "d": 2
    },
    {
        "q": "Which classic French brown mother sauce is prepared from roasted brown veal stock, browned mirepoix, and brown roux?",
        "correct": "Espagnole sauce",
        "distractors": ["Demi-glace", "Velouté", "Sauce Robert"],
        "d": 2
    },
    {
        "q": "Which concentrated sauce is made by combining equal parts Espagnole sauce and rich veal stock, then simmering until reduced by half?",
        "correct": "Demi-glace",
        "distractors": ["Glace de viande", "Jus lié", "Sauce Bordelaise"],
        "d": 2
    },
    {
        "q": "Which French red wine sauce named after a southwestern region is flavored with shallots, thyme, bay leaf, and poached beef bone marrow?",
        "correct": "Bordelaise sauce",
        "distractors": ["Sauce Robert", "Sauce Chasseur", "Sauce Périgueux"],
        "d": 2
    },
    {
        "q": "Which luxurious French brown sauce is perfumed with finely minced black truffles and Madeira wine?",
        "correct": "Sauce Périgueux",
        "distractors": ["Sauce Bordelaise", "Sauce Mornay", "Sauce Chasseur"],
        "d": 2
    },
    {
        "q": "Which classic hunter's sauce (Sauce Chasseur) features sautéed mushrooms, shallots, white wine, and demi-glace, finished with fresh parsley and tarragon?",
        "correct": "Mushrooms and shallots",
        "distractors": ["Capers and lemon", "Tomatoes and basil", "Truffles and cream"],
        "d": 2
    },
    {
        "q": "Which French cold emulsion sauce is made by emulsifying hard-boiled egg yolks with oil and vinegar, folded with chopped egg whites, capers, and herbs?",
        "correct": "Sauce Gribiche",
        "distractors": ["Sauce Ravigote", "Sauce Tartare", "Sauce Remoulade"],
        "d": 2
    },
    {
        "q": "Which Greek garlic and potato (or stale bread) dip is emulsified with copious amounts of extra virgin olive oil and lemon juice?",
        "correct": "Skordalia",
        "distractors": ["Tzatziki", "Taramosalata", "Melitzanosalata"],
        "d": 2
    },
    {
        "q": "Which creamy Greek meze dip is made from cured roe of cod, carp, or grey mullet mashed with stale bread or potatoes, olive oil, and lemon juice?",
        "correct": "Taramosalata",
        "distractors": ["Skordalia", "Tirokafteri", "Fava"],
        "d": 2
    },
    {
        "q": "Which spicy Greek meze spread is made by whipping feta cheese with roasted red peppers, chili peppers, olive oil, and lemon juice?",
        "correct": "Tirokafteri",
        "distractors": ["Taramosalata", "Melitzanosalata", "Ktipiti"],
        "d": 2
    },
    {
        "q": "Which Middle Eastern red pepper and walnut dip originated in Aleppo, Syria, seasoned with pomegranate molasses and cumin?",
        "correct": "Muhammara",
        "distractors": ["Baba Ghanoush", "Ajika", "Matbucha"],
        "d": 2
    },
    {
        "q": "Which Lebanese condiment consists solely of fresh raw garlic cloves and oil emulsified vigorously into a thick, fluffy white garlic spread?",
        "correct": "Toum",
        "distractors": ["Tarator", "Tzatziki", "Aioli"],
        "d": 2
    },
    {
        "q": "Which spicy Yemenite green hot sauce, made with green serrano or jalapeño chilies, garlic, coriander, cardamom, and caraway, is ubiquitous in Israeli cuisine?",
        "correct": "Zhug (Schug)",
        "distractors": ["Harissa", "Chermoula", "Shatta"],
        "d": 2
    },
    {
        "q": "Which North African marinade and sauce, particularly revered in Morocco for fish, is made of cilantro, garlic, cumin, paprika, preserved lemon, and olive oil?",
        "correct": "Chermoula",
        "distractors": ["Harissa", "Zhug", "Shakshuka"],
        "d": 2
    },
    {
        "q": "Which Maghrebi cooked salad or relish made of stewed tomatoes, roasted bell peppers, garlic, and chili peppers is served cold with bread?",
        "correct": "Matbucha",
        "distractors": ["Taktouka", "Muhammara", "Za'alouk"],
        "d": 2
    },
    {
        "q": "Which Moroccan cooked eggplant and tomato warm salad or spread is seasoned with garlic, paprika, cumin, and fresh cilantro?",
        "correct": "Za'alouk",
        "distractors": ["Matbucha", "Taktouka", "Bissara"],
        "d": 2
    },
    {
        "q": "Which fermented condiment made from salted anchovies, tamarind, vinegar, molasses, and garlic was created in the English county of Worcestershire?",
        "correct": "Worcestershire sauce",
        "distractors": ["Marmite", "Henderson's Relish", "HP Sauce"],
        "d": 2
    },
    {
        "q": "Which famous British 'brown sauce' contains tomatoes, malt vinegar, dates, tamarind extract, rye flour, and spices?",
        "correct": "HP Sauce",
        "distractors": ["Worcestershire sauce", "Colman's mustard", "Branston Pickle"],
        "d": 2
    },
    {
        "q": "Which classic British sweet, chunky pickle relish features diced rutabaga, carrots, onions, and cauliflower pickled in a dark, spiced, malted vinegar sauce?",
        "correct": "Branston Pickle",
        "distractors": ["Piccalilli", "Chow chow", "Gentleman's Relish"],
        "d": 2
    },
    {
        "q": "Which bright yellow British relish made of chopped pickled vegetables flavored with mustard powder and turmeric was adapted from Indian achaar?",
        "correct": "Piccalilli",
        "distractors": ["Branston Pickle", "Chow chow", "Remoulade"],
        "d": 2
    },
    {
        "q": "Which Japanese citrus-flavored soy dipping sauce combines soy sauce, mirin, bonito flakes, kombu, and yuzu or sudachi juice?",
        "correct": "Ponzu",
        "distractors": ["Tare", "Tsuyu", "Goma dare"],
        "d": 2
    },
    {
        "q": "Which Japanese sesame dipping sauce made from ground roasted white sesame seeds, dashi, soy sauce, and mirin is commonly served with shabu-shabu?",
        "correct": "Goma dare",
        "distractors": ["Ponzu", "Tare", "Tonkatsu sauce"],
        "d": 2
    },
    {
        "q": "Which Japanese thick, fruity brown sauce, similar to Worcestershire but sweeter, is specifically served over breaded pork cutlets?",
        "correct": "Tonkatsu sauce",
        "distractors": ["Teriyaki sauce", "Unagi tare", "Okonomiyaki sauce"],
        "d": 2
    },
    {
        "q": "Which Korean fermented condiment made of red chili powder, glutinous rice powder, fermented soybean powder (meju), and salt provides sweet heat?",
        "correct": "Gochujang",
        "distractors": ["Doenjang", "Ssamjang", "Ganjang"],
        "d": 2
    },
    {
        "q": "Which savory Korean dipping paste for lettuce wraps (ssam) is made by blending doenjang (soybean paste) and gochujang with sesame oil, garlic, and scallions?",
        "correct": "Ssamjang",
        "distractors": ["Chochujang", "Ganjang", "Cheonggukjang"],
        "d": 2
    },
    {
        "q": "Which fermented Indonesian chili paste consisting simply of crushed red chili peppers, salt, and vinegar or lime juice is called:",
        "correct": "Sambal Oelek",
        "distractors": ["Sambal Terasi", "Sambal Matah", "Sambal Bajak"],
        "d": 2
    },
    {
        "q": "Which Indonesian sweet soy sauce, sweetened with thick palm sugar and infused with star anise and cloves, has a syrupy molasses consistency?",
        "correct": "Kecap Manis",
        "distractors": ["Kecap Asin", "Tamari", "Sweet soy glaze"],
        "d": 2
    },
    {
        "q": "Which Vietnamese all-purpose dipping sauce is made from fish sauce, water, sugar, lime juice, finely minced garlic, and bird's eye chilies?",
        "correct": "Nước chấm",
        "distractors": ["Nước mắm", "Tương đen", "Mắm tôm"],
        "d": 2
    },
    {
        "q": "Which pungent Vietnamese fermented purple paste made from crushed sea krill or shrimp is used to flavor Bún riêu and Bún đậu?",
        "correct": "Mắm tôm",
        "distractors": ["Nước mắm", "Mắm ruốc", "Tương bần"],
        "d": 2
    },
    {
        "q": "Which Thai spicy dipping sauce made with toasted dried chili flakes, fish sauce, lime juice, shallots, and toasted rice powder is served with grilled meats?",
        "correct": "Nam Jim Jaew",
        "distractors": ["Nam Jim Gai", "Nam Prik Pao", "Sriracha"],
        "d": 2
    },
    {
        "q": "Which Thai roasted chili jam contains roasted shallots, garlic, dried shrimp, tamarind, palm sugar, and chilies fried in oil?",
        "correct": "Nam Prik Pao",
        "distractors": ["Nam Jim Jaew", "Nam Jim Seafood", "Prik Nam Pla"],
        "d": 2
    },
    {
        "q": "Which Canarian cold sauce comes in a red version (with dried red peppers and cumin) and a green version (with coriander and green peppers)?",
        "correct": "Mojo sauce (Mojo picón / Mojo verde)",
        "distractors": ["Salsa brava", "Alioli", "Romesco"],
        "d": 2
    },
    {
        "q": "Which classic Mexican chocolate-infused rich brown sauce from Puebla incorporates dried ancho, pasilla, and mulato chilies, raisins, spices, and Mexican chocolate?",
        "correct": "Mole Poblano",
        "distractors": ["Mole Verde", "Mole Amarillo", "Mole Manchamanteles"],
        "d": 2
    },

    # --- HARD (d=3, 30 questions) ---
    {
        "q": "Which Oaxacan green mole sauce gets its emerald hue from pumpkin seeds, tomatillos, and fresh leaves like epazote, hoja santa, and parsley?",
        "correct": "Mole Verde",
        "distractors": ["Mole Negro", "Mole Coloradito", "Mole Chichilo"],
        "d": 3
    },
    {
        "q": "Which unique herb, also known as Mexican pepperleaf or Piper auritum, lends an essential sassafras-anise flavor to Oaxacan Mole Verde?",
        "correct": "Hoja santa",
        "distractors": ["Epazote", "Papalo", "Culantro"],
        "d": 3
    },
    {
        "q": "Which ancient Mexican sauce or stew category takes its name from the Spanish word for pumpkin seeds (pepitas), which form its thickened nutty base?",
        "correct": "Pipián",
        "distractors": ["Mole", "Encacahuatado", "Adobo"],
        "d": 3
    },
    {
        "q": "Which French derivative of Hollandaise incorporates blood orange juice reduction and grated zest along with the egg yolks and butter?",
        "correct": "Sauce Maltaise",
        "distractors": ["Sauce Mousseline", "Sauce Choron", "Sauce Noisette"],
        "d": 3
    },
    {
        "q": "Which derivative of Béarnaise sauce is created by whisking in tomato paste or pureed tomato coulis?",
        "correct": "Sauce Choron",
        "distractors": ["Sauce Foyot", "Sauce Colbert", "Sauce Paloise"],
        "d": 3
    },
    {
        "q": "Which derivative of Béarnaise sauce substitutes fresh garden mint for the traditional tarragon, commonly served with roast lamb?",
        "correct": "Sauce Paloise",
        "distractors": ["Sauce Choron", "Sauce Foyot", "Sauce Béarn"],
        "d": 3
    },
    {
        "q": "Which sauce made by adding melted meat glaze (glace de viande) to Béarnaise sauce is named after a 19th-century French food writer?",
        "correct": "Sauce Foyot (Sauce Valois)",
        "distractors": ["Sauce Choron", "Sauce Paloise", "Sauce Colbert"],
        "d": 3
    },
    {
        "q": "Which classic French onion-puree sauce, named after the 18th-century Duke of Soubise, is made by sweating pureed onions in béchamel sauce?",
        "correct": "Sauce Soubise",
        "distractors": ["Sauce Lyonnaise", "Sauce Mornay", "Sauce Dugléré"],
        "d": 3
    },
    {
        "q": "Which classic French fish sauce is created by poaching white fish in white wine, shallots, and diced tomatoes, then finishing the cooking liquor with velouté and cold butter?",
        "correct": "Sauce Dugléré",
        "distractors": ["Sauce Bercy", "Sauce Cardinal", "Sauce Joinville"],
        "d": 3
    },
    {
        "q": "Which classic fish sauce named after a Paris neighborhood reduces white wine, fish stock, and chopped shallots, finished with butter, lemon, and parsley?",
        "correct": "Sauce Bercy",
        "distractors": ["Sauce Dugléré", "Sauce Nantua", "Sauce Dieppoise"],
        "d": 3
    },
    {
        "q": "Which luxurious French seafood velouté sauce is enriched with heavy cream and flavored with crayfish butter (beurre d'écrevisse)?",
        "correct": "Sauce Nantua",
        "distractors": ["Sauce Homard", "Sauce Dugléré", "Sauce Joinville"],
        "d": 3
    },
    {
        "q": "Which Sicilian pesto originating in Trapani replaces pine nuts and heavy basil with blanched almonds, ripe fresh tomatoes, and garlic?",
        "correct": "Pesto alla Trapanese",
        "distractors": ["Pesto Modenese", "Pesto Calabrese", "Pesto Rosso"],
        "d": 3
    },
    {
        "q": "Which Modena specialty spread, known as 'cunza' or Pesto Modenese, is made of finely beaten pork lard, rosemary, and garlic, spread over warm tigelle?",
        "correct": "Pesto Modenese (Cunza)",
        "distractors": ["Lardo di Colonnata", "Pesto alla Trapanese", "Nduja"],
        "d": 3
    },
    {
        "q": "Which Southern Italian citrus dressing, used across Sicily and Calabria for grilled swordfish, consists of olive oil, lemon juice, hot water, oregano, and minced garlic whisked vigorously?",
        "correct": "Salmoriglio",
        "distractors": ["Salsa Verde", "Gremolata", "Agrodolce"],
        "d": 3
    },
    {
        "q": "Which Piedmontese warm bath dip made with garlic, salted anchovies, butter, and olive oil is served in a terracotta burner (fujot) for dipping raw cardoons and peppers?",
        "correct": "Bagna Càuda",
        "distractors": ["Salsa Verde", "Agliata", "Fonduta"],
        "d": 3
    },
    {
        "q": "Which classic Italian sweet-and-sour glaze is prepared by simmering caramelized sugar with vinegar, often infused with red wine, dried fruit, or onions?",
        "correct": "Agrodolce",
        "distractors": ["Saba", "Vincotto", "Mostarda"],
        "d": 3
    },
    {
        "q": "Which Northern Italian condiment from Cremona features whole candied fruits preserved in a transparent sugar syrup spiced with spicy mustard oil?",
        "correct": "Mostarda di Cremona",
        "distractors": ["Cotognata", "Mostaccioli", "Amarena"],
        "d": 3
    },
    {
        "q": "Which ancient Roman fermented fish sauce, produced by fermenting fish entrails in sea salt in large open vats under the Mediterranean sun, was called:",
        "correct": "Garum (Liquamen)",
        "distractors": ["Hallex", "Colatura", "Murri"],
        "d": 3
    },
    {
        "q": "Which modern artisanal Italian amber liquid from the Amalfi Coast village of Cetara is the direct historical descendant of ancient Roman garum, made from salted anchovies fermented in chestnut barrels?",
        "correct": "Colatura di Alici",
        "distractors": ["Garum di tonno", "Bottarga liquida", "Aceto Balsamico"],
        "d": 3
    },
    {
        "q": "Which spicy and aromatic Georgian seasoning paste is made by pounding hot red peppers, garlic, blue fenugreek, coriander seeds, and dill with salt?",
        "correct": "Ajika",
        "distractors": ["Tkemali", "Satsivi", "Khmeli suneli"],
        "d": 3
    },
    {
        "q": "Which tart and tangy Georgian fruit sauce is made from wild sour cherry plums, flavored with cilantro, dill, garlic, and pennyroyal?",
        "correct": "Tkemali",
        "distractors": ["Ajika", "Narsharab", "Kizil"],
        "d": 3
    },
    {
        "q": "Which rich Azerbaijani and Russian reduced pomegranate syrup sauce is simmered until dense and glossy, traditionally spooned over grilled sturgeon or lamb?",
        "correct": "Narsharab",
        "distractors": ["Tkemali", "Robb", "Pekmez"],
        "d": 3
    },
    {
        "q": "Which Sichuan fermented seasoning paste made from broad beans (fava beans), fermented chili peppers, salt, and wheat flour is hailed as the 'soul of Sichuan cuisine'?",
        "correct": "Pixian Doubanjiang",
        "distractors": ["Tianmianjiang", "Gochujang", "Douchi"],
        "d": 3
    },
    {
        "q": "Which fermented Chinese sweet bean sauce made from fermented wheat flour and yellow soybeans is an indispensable base for Zha Jiang Mian?",
        "correct": "Tianmianjiang (Sweet Bean Sauce)",
        "distractors": ["Doubanjiang", "Hoisin sauce", "Shahe paste"],
        "d": 3
    },
    {
        "q": "Which Cantonese umami-bomb condiment invented in the 1980s by chefs at the Peninsula Hotel is made of dried scallops (conpoy), dried shrimp, Jinhua ham, shallots, garlic, and chilies?",
        "correct": "XO Sauce",
        "distractors": ["Shacha sauce", "Hao You", "Douban sauce"],
        "d": 3
    },
    {
        "q": "Which Chinese savory and slightly seafood-forward barbecue condiment, adapted from Southeast Asian satay sauce and popular in Chaoshan hot pots, is called:",
        "correct": "Shacha sauce (Sa Cha)",
        "distractors": ["XO Sauce", "Hoisin sauce", "Char siu sauce"],
        "d": 3
    },
    {
        "q": "Which spicy, intensely aromatic condiment from the Japanese island of Kyushu is made by mashing spicy green or red chili peppers with fragrant unripened yuzu citrus zest and salt?",
        "correct": "Yuzukosho",
        "distractors": ["Shichimi Togarashi", "Kanzuri", "Sansho"],
        "d": 3
    },
    {
        "q": "Which artisanal fermented chili paste from Niigata Prefecture, Japan, is made by exposing salted red chili peppers to winter snowdrifts before fermenting with yuzu, koji, and malt?",
        "correct": "Kanzuri",
        "distractors": ["Yuzukosho", "Momiji oroshi", "Rayu"],
        "d": 3
    },
    {
        "q": "Which Japanese condiment made from finely grated daikon radish infused with red chili pepper gives the appearance of autumn maple leaves?",
        "correct": "Momiji Oroshi",
        "distractors": ["Daikon oroshi", "Kanzuri", "Beni shoga"],
        "d": 3
    },
    {
        "q": "Which traditional Indonesian fermented shrimp paste, packed into dense dark blocks with an intense pungent aroma, is toasted over coals before pounding into sambals?",
        "correct": "Terasi (Belacan)",
        "distractors": ["Petis udang", "Bagoong", "Kapi"],
        "d": 3
    }
]

if __name__ == "__main__":
    out_path = "tools/staging/ingredients_batch3.json"
    build_batch(raw_questions, out_path, batch_num=3)
