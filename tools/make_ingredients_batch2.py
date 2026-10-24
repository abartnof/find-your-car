#!/usr/bin/env python3
"""
Generate Batch 2: Classic Salads, Soups, Stews & Chowders (100 questions).
30 Easy (d=1), 40 Medium (d=2), 30 Hard (d=3).
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ingredients_builder import build_batch

raw_questions = [
    # --- EASY (d=1, 30 questions) ---
    {
        "q": "Which leafy green is the mandatory crisp lettuce base of a classic Caesar salad?",
        "correct": "Romaine lettuce",
        "distractors": ["Iceberg lettuce", "Arugula", "Butterhead lettuce"],
        "d": 1
    },
    {
        "q": "Which cheese is traditionally grated over a classic Caesar salad?",
        "correct": "Parmesan",
        "distractors": ["Cheddar", "Feta", "Gouda"],
        "d": 1
    },
    {
        "q": "Which small, salty cured fish is traditionally blended into authentic Caesar salad dressing?",
        "correct": "Anchovies",
        "distractors": ["Sardines", "Mackerel", "Trout"],
        "d": 1
    },
    {
        "q": "Which three fresh ingredients are layered in a traditional Italian Caprese salad alongside olive oil and salt?",
        "correct": "Ripe tomatoes, fresh mozzarella, and basil",
        "distractors": ["Tomatoes, goat cheese, and oregano", "Cucumbers, feta, and dill", "Tomatoes, burrata, and parsley"],
        "d": 1
    },
    {
        "q": "Which crunchy nut is a signature ingredient in a classic Waldorf salad?",
        "correct": "Walnuts",
        "distractors": ["Pistachios", "Almonds", "Cashews"],
        "d": 1
    },
    {
        "q": "Which crisp fruit is diced along with celery and walnuts in a traditional Waldorf salad?",
        "correct": "Apples",
        "distractors": ["Pears", "Peaches", "Melons"],
        "d": 1
    },
    {
        "q": "Which dressing traditionally coats the apples, celery, and walnuts in a Waldorf salad?",
        "correct": "Mayonnaise",
        "distractors": ["Vinaigrette", "Ranch dressing", "Italian dressing"],
        "d": 1
    },
    {
        "q": "Which root vegetable gives traditional Eastern European Borscht its vibrant deep ruby-red color?",
        "correct": "Beets",
        "distractors": ["Red cabbage", "Radishes", "Red carrots"],
        "d": 1
    },
    {
        "q": "Which creamy dairy product is traditionally dolloped on top of a hot bowl of Borscht?",
        "correct": "Sour cream",
        "distractors": ["Cream cheese", "Heavy cream", "Cottage cheese"],
        "d": 1
    },
    {
        "q": "Which type of clam broth base distinguishes New England clam chowder from Manhattan clam chowder?",
        "correct": "Heavy cream or milk",
        "distractors": ["Tomato broth", "Beef stock", "Soy sauce broth"],
        "d": 1
    },
    {
        "q": "What base gives Manhattan clam chowder its characteristic red color and acidic tang?",
        "correct": "Tomatoes",
        "distractors": ["Beets", "Red bell peppers", "Paprika paste"],
        "d": 1
    },
    {
        "q": "What kind of caramelized allium is the central star of classic French onion soup?",
        "correct": "Yellow onions",
        "distractors": ["Garlic cloves", "Leeks", "Scallions"],
        "d": 1
    },
    {
        "q": "Which melted cheese is broiled on a slice of bread atop traditional French onion soup?",
        "correct": "Gruyère",
        "distractors": ["Brie", "Cheddar", "Feta"],
        "d": 1
    },
    {
        "q": "Which herb is the dominant green foundation of traditional Levantine Tabbouleh salad?",
        "correct": "Flat-leaf parsley",
        "distractors": ["Cilantro", "Basil", "Oregano"],
        "d": 1
    },
    {
        "q": "Which cracked wheat grain is soaked and mixed with parsley, mint, and tomatoes in classic Tabbouleh?",
        "correct": "Bulgur",
        "distractors": ["Couscous", "Quinoa", "Barley"],
        "d": 1
    },
    {
        "q": "Which brined curd cheese is the hallmark topping of a traditional Greek salad (Horiatiki)?",
        "correct": "Feta",
        "distractors": ["Gouda", "Parmesan", "Swiss"],
        "d": 1
    },
    {
        "q": "Which cured meat is traditionally cubed and included in a classic American Cobb salad?",
        "correct": "Crispy bacon",
        "distractors": ["Prosciutto", "Pastrami", "Bologna"],
        "d": 1
    },
    {
        "q": "Which crumbly, pungent cheese is typically arranged in the rows of a classic Cobb salad?",
        "correct": "Roquefort or blue cheese",
        "distractors": ["Cheddar cheese", "Brie cheese", "Mozzarella cheese"],
        "d": 1
    },
    {
        "q": "Which green, creamy fruit is diced into rows in a classic Cobb salad?",
        "correct": "Avocado",
        "distractors": ["Kiwi", "Cucumber", "Green apple"],
        "d": 1
    },
    {
        "q": "Which cold Spanish soup from Andalusia is made by blending ripe raw tomatoes, cucumbers, bell peppers, garlic, and stale bread with olive oil and vinegar?",
        "correct": "Gazpacho",
        "distractors": ["Salmorejo", "Ajo Blanco", "Bouillabaisse"],
        "d": 1
    },
    {
        "q": "Which poultry meat is traditionally simmered in red Burgundy wine, mushrooms, and lardons to make Coq au Vin?",
        "correct": "Chicken",
        "distractors": ["Duck", "Turkey", "Pork"],
        "d": 1
    },
    {
        "q": "Which red wine is the traditional braising liquid for authentic French Beef Bourguignon?",
        "correct": "Burgundy Pinot Noir",
        "distractors": ["Bordeaux Cabernet", "Chianti", "Rioja"],
        "d": 1
    },
    {
        "q": "Which hearty green vegetable is shredded as the primary base for traditional coleslaw?",
        "correct": "Cabbage",
        "distractors": ["Kale", "Spinach", "Swiss chard"],
        "d": 1
    },
    {
        "q": "Which protein cooked in duck fat or pork fat, along with white beans and sausages, is the anchor of French Cassoulet?",
        "correct": "Duck confit",
        "distractors": ["Ground beef", "Salmon fillets", "Rabbit kidneys"],
        "d": 1
    },
    {
        "q": "Which type of bean forms the hearty legume base of French Cassoulet?",
        "correct": "White beans (Tarbes or cannellini)",
        "distractors": ["Black beans", "Kidney beans", "Chickpeas"],
        "d": 1
    },
    {
        "q": "Which vegetable broth loaded with diced tomatoes, zucchini, pasta or rice, and seasonal greens is the quintessential Italian vegetable soup?",
        "correct": "Minestrone",
        "distractors": ["Ribollita", "Stracciatella", "Pasta e Fagioli"],
        "d": 1
    },
    {
        "q": "Which dumplings made from matzo meal, beaten eggs, and chicken fat (schmaltz) are served in classic Jewish chicken soup?",
        "correct": "Matzo balls",
        "distractors": ["Kreplach", "Pierogi", "Gnocchi"],
        "d": 1
    },
    {
        "q": "Which spicy and sour Thai soup is famously flavored with lemongrass, kaffir lime leaves, galangal, chili peppers, and shrimp?",
        "correct": "Tom Yum Goong",
        "distractors": ["Tom Kha Gai", "Massaman", "Gaeng Som"],
        "d": 1
    },
    {
        "q": "Which rich liquid extracted from grated mature coconut meat provides the creamy base for Thai Tom Kha Gai soup?",
        "correct": "Coconut milk",
        "distractors": ["Heavy cream", "Almond milk", "Evaporated milk"],
        "d": 1
    },
    {
        "q": "Which cured black olive from the French Riviera is an essential garnishing ingredient in Salade Niçoise?",
        "correct": "Niçoise olives",
        "distractors": ["Kalamata olives", "Castelvetrano olives", "Manzanilla olives"],
        "d": 1
    },

    # --- MEDIUM (d=2, 40 questions) ---
    {
        "q": "Which cold, silky leek and potato soup, traditionally thickened with cream, was popularized by chef Louis Diat at the Ritz-Carlton in New York?",
        "correct": "Vichyssoise",
        "distractors": ["Velouté de poireaux", "Bisque de homard", "Potage Parmentier"],
        "d": 2
    },
    {
        "q": "Which thick Andalusian cold tomato soup from Córdoba differs from gazpacho by containing more stale bread, olive oil, and no cucumbers or bell peppers?",
        "correct": "Salmorejo",
        "distractors": ["Ajo Blanco", "Porra Antequerana", "Gazpachuelo"],
        "d": 2
    },
    {
        "q": "Which cold Andalusian soup, often called 'white gazpacho', is made from blended blanched almonds, garlic, stale bread, olive oil, and vinegar, garnished with green grapes?",
        "correct": "Ajo Blanco",
        "distractors": ["Salmorejo", "Menestra", "Sopa de ajo"],
        "d": 2
    },
    {
        "q": "Which fragrant rhizome, closely related to ginger but with a sharper, citrusy, and pine-like bite, is vital to authentic Tom Yum and Tom Kha soups?",
        "correct": "Galangal",
        "distractors": ["Turmeric", "Horseradish", "Wasabi"],
        "d": 2
    },
    {
        "q": "Which citrus tree leaf with a double-lobed shape gives Southeast Asian broths their distinct floral-citrus aroma?",
        "correct": "Kaffir lime leaf (makrut lime)",
        "distractors": ["Lemon verbena leaf", "Curry leaf", "Bay leaf"],
        "d": 2
    },
    {
        "q": "Which Tuscan bread salad features chunks of stale crusty bread soaked in vinegar and juices from ripe tomatoes, cucumbers, red onion, and basil?",
        "correct": "Panzanella",
        "distractors": ["Fattoush", "Caponata", "Ribollita"],
        "d": 2
    },
    {
        "q": "Which crispy fried pieces of flatbread are tossed into Levantine Fattoush salad for crunch?",
        "correct": "Pita bread chips",
        "distractors": ["Lavash croutons", "Tortilla strips", "Baguette toasts"],
        "d": 2
    },
    {
        "q": "Which tangy, dark red ground spice derived from dried sumac berries gives Fattoush salad its sour lemony flavor?",
        "correct": "Sumac",
        "distractors": ["Paprika", "Za'atar", "Mahlab"],
        "d": 2
    },
    {
        "q": "Which famous seafood stew from Marseille, France, is traditionally cooked with rockfish, fennel, saffron, garlic, and served with rouille?",
        "correct": "Bouillabaisse",
        "distractors": ["Bourride", "Cioppino", "Cotriade"],
        "d": 2
    },
    {
        "q": "Which spice, harvested from the stigmas of Crocus sativus, gives Bouillabaisse broth its vibrant golden color and pungent aroma?",
        "correct": "Saffron",
        "distractors": ["Turmeric", "Annatto", "Safflower"],
        "d": 2
    },
    {
        "q": "Which garlic and saffron mayonnaise-based sauce is spread on toasts and floated in authentic Bouillabaisse?",
        "correct": "Rouille",
        "distractors": ["Aioli", "Remoulade", "Romesco"],
        "d": 2
    },
    {
        "q": "Which San Francisco fisherman's seafood stew created by Italian immigrants combines Dungeness crab, clams, shrimp, and fish in a tomato-wine broth?",
        "correct": "Cioppino",
        "distractors": ["Bouillabaisse", "Cacciucco", "Caldeirada"],
        "d": 2
    },
    {
        "q": "Which hearty Tuscan stewed soup, meaning 'reboiled', is made with leftover crusty bread, cannellini beans, and black Tuscan kale (cavolo nero)?",
        "correct": "Ribollita",
        "distractors": ["Acquacotta", "Pasta e fagioli", "Zuppa toscana"],
        "d": 2
    },
    {
        "q": "Which Hungarian meat stew is richly flavored with large quantities of sweet and spicy Hungarian paprika, onions, and beef shank?",
        "correct": "Goulash (Gulyás)",
        "distractors": ["Pörkölt", "Paprikash", "Bigos"],
        "d": 2
    },
    {
        "q": "What variety of sour pickled fermented cabbage is the key foundational ingredient of Polish hunter's stew (Bigos)?",
        "correct": "Sauerkraut",
        "distractors": ["Kimchi", "Pickled red cabbage", "Fermented mustard greens"],
        "d": 2
    },
    {
        "q": "Which Belgian beef stew is slow-cooked with caramelized onions, aromatics, and dark Abbey or Trappist ale, often sweetened with gingerbread and mustard?",
        "correct": "Carbonnade Flamande",
        "distractors": ["Boeuf Bourguignon", "Waterzooi", "Sauerbraten"],
        "d": 2
    },
    {
        "q": "Which national dish of Brazil is a slow-simmered stew of black beans, various cuts of salted pork, beef, and smoked sausages, served with farofa?",
        "correct": "Feijoada",
        "distractors": ["Moqueca", "Vatapá", "Bobó de camarão"],
        "d": 2
    },
    {
        "q": "What toasted manioc (cassava) flour mixture is traditionally sprinkled over Brazilian Feijoada for texture?",
        "correct": "Farofa",
        "distractors": ["Polenta", "Fufu", "Couscous"],
        "d": 2
    },
    {
        "q": "Which Portuguese soup features finely shredded collard greens or kale swimming in a potato broth seasoned with sliced chouriço sausage?",
        "correct": "Caldo Verde",
        "distractors": ["Sopa da pedra", "Caldeirada", "Açorda"],
        "d": 2
    },
    {
        "q": "Which protein is traditionally sliced into Portuguese Caldo Verde soup right before serving?",
        "correct": "Chouriço sausage",
        "distractors": ["Prosciutto", "Salt cod (bacalhau)", "Pork belly"],
        "d": 2
    },
    {
        "q": "Which traditional Mexican soup is made from nixtamalized corn kernels (hominy) simmered with pork or chicken in a red, green, or white chili broth?",
        "correct": "Pozole",
        "distractors": ["Menudo", "Birria", "Sopa de tortilla"],
        "d": 2
    },
    {
        "q": "What treated corn ingredient, soaked in an alkaline slaked-lime solution, gives Mexican Pozole its chewy puffed texture and distinctive flavor?",
        "correct": "Hominy",
        "distractors": ["Polenta grits", "Sweet corn kernels", "Masa harina paste"],
        "d": 2
    },
    {
        "q": "Which Mexican restorative stew features beef tripe simmered in a red chili broth with lime, onions, oregano, and cilantro?",
        "correct": "Menudo",
        "distractors": ["Pozole", "Carne en su jugo", "Caldo tlalpeño"],
        "d": 2
    },
    {
        "q": "Which aromatic dried herb is crushed between palms as a traditional table seasoning for Mexican Pozole and Menudo?",
        "correct": "Mexican oregano",
        "distractors": ["Rosemary", "Tarragon", "Sage"],
        "d": 2
    },
    {
        "q": "Which thick soup made from crustaceans (like lobster, shrimp, or crab) relies on roasting the pulverized shells to extract depth, thickened with rice or cream?",
        "correct": "Bisque",
        "distractors": ["Chowder", "Velouté", "Consommé"],
        "d": 2
    },
    {
        "q": "What perfectly clear, amber-hued French soup is clarified using a raft of egg whites, ground lean meat, and mirepoix?",
        "correct": "Consommé",
        "distractors": ["Bouillon", "Court-bouillon", "Brodo"],
        "d": 2
    },
    {
        "q": "Which spicy shredded green papaya salad from Northeastern Thailand (Isan) is pounded in a mortar with chilies, garlic, lime, fish sauce, and peanuts?",
        "correct": "Som Tum",
        "distractors": ["Larb", "Yam Wun Sen", "Nam Tok"],
        "d": 2
    },
    {
        "q": "What crunchy, unripened fruit is shredded as the primary vessel for flavors in traditional Thai Som Tum?",
        "correct": "Green papaya",
        "distractors": ["Green mango", "Green apple", "Chayote squash"],
        "d": 2
    },
    {
        "q": "Which Lao and Northern Thai minced meat salad is seasoned with fresh herbs, lime juice, fish sauce, chilies, and toasted ground sticky rice (khao khua)?",
        "correct": "Larb (Laab)",
        "distractors": ["Som Tum", "Pad Krapow", "Massaman"],
        "d": 2
    },
    {
        "q": "What roasted ingredient provides the distinctive nutty aroma and crunch in authentic Thai Larb?",
        "correct": "Toasted sticky rice powder (khao khua)",
        "distractors": ["Crushed toasted peanuts", "Sesame seeds", "Fried shallots"],
        "d": 2
    },
    {
        "q": "Which famous Scottish soup is prepared with chicken, leeks, and traditionally simmered with dried prunes?",
        "correct": "Cock-a-leekie",
        "distractors": ["Cullen skink", "Scotch broth", "Partan bree"],
        "d": 2
    },
    {
        "q": "Which thick Scottish soup is made of smoked haddock, potatoes, onions, and milk or cream?",
        "correct": "Cullen skink",
        "distractors": ["Cock-a-leekie", "Scotch broth", "Stovies"],
        "d": 2
    },
    {
        "q": "Which Anglo-Indian spiced soup, whose name translates from Tamil as 'pepper water', includes curry powder, lentils, apples, and chicken?",
        "correct": "Mulligatawny",
        "distractors": ["Rasam", "Sambar", "Dal makhani"],
        "d": 2
    },
    {
        "q": "Which South Indian hot, sour, and spiced broth relies heavily on tamarind water, tomatoes, black pepper, and curry leaves?",
        "correct": "Rasam",
        "distractors": ["Sambar", "Avial", "Kootu"],
        "d": 2
    },
    {
        "q": "Which sour, tangy paste extracted from the pods of a tropical legume tree is the essential souring agent in Indian Rasam and Thai Pad Thai?",
        "correct": "Tamarind paste",
        "distractors": ["Amchur (mango powder)", "Kokum", "Pomegranate molasses"],
        "d": 2
    },
    {
        "q": "Which Russian salad, invented in Moscow by Belgian chef Lucien Olivier, features boiled diced potatoes, carrots, peas, pickles, and hard-boiled eggs in mayonnaise?",
        "correct": "Olivier salad (Russian salad)",
        "distractors": ["Shuba (Herring under a fur coat)", "Vinegret", "Mimosa salad"],
        "d": 2
    },
    {
        "q": "Which layered Russian festive salad, nicknamed 'Herring under a fur coat', features salted herring covered by layers of grated beets, carrots, potatoes, and mayonnaise?",
        "correct": "Dressed Herring (Shuba)",
        "distractors": ["Olivier salad", "Vinegret", "Kholodets"],
        "d": 2
    },
    {
        "q": "Which Russian beet salad dressed in sunflower oil features diced boiled beets, potatoes, sauerkraut, brined pickles, and peas?",
        "correct": "Vinegret",
        "distractors": ["Olivier salad", "Borscht", "Solianka"],
        "d": 2
    },
    {
        "q": "Which sour, salty, and spicy Russian soup features brined cucumbers, capers, olives, mushrooms, and assorted meats or fish?",
        "correct": "Solyanka",
        "distractors": ["Rassolnik", "Ukha", "Shchi"],
        "d": 2
    },
    {
        "q": "Which traditional Russian soup made with pork or beef broth is defined primarily by brined pickled cucumbers and pearl barley?",
        "correct": "Rassolnik",
        "distractors": ["Solyanka", "Shchi", "Ukha"],
        "d": 2
    },

    # --- HARD (d=3, 30 questions) ---
    {
        "q": "Which clear Russian fish soup is traditionally simmered with freshwater fish such as sterlet, ruffe, or pike, flavored simply with parsley, leek, and bay leaves?",
        "correct": "Ukha",
        "distractors": ["Solyanka", "Botvinya", "Okroshka"],
        "d": 3
    },
    {
        "q": "Which cold Russian summer soup consists of raw diced vegetables and cooked meats poured over fermented bread kvass?",
        "correct": "Okroshka",
        "distractors": ["Botvinya", "Svekolnik", "Tyurya"],
        "d": 3
    },
    {
        "q": "Which Livorno-style Tuscan seafood stew is famously cooked with five different types of fish and shellfish to represent the five letters in its name?",
        "correct": "Cacciucco",
        "distractors": ["Brodetto", "Buridda", "Cioppino"],
        "d": 3
    },
    {
        "q": "Which dense, collagen-rich Japanese ramen broth is created by boiling pork marrow bones and trotters at a rolling boil for over 12 hours until emulsified?",
        "correct": "Tonkotsu broth",
        "distractors": ["Tori paitan broth", "Chintan broth", "Gyukotsu broth"],
        "d": 3
    },
    {
        "q": "What fermented soybean paste, dissolved at the very end of cooking to preserve probiotics, forms the seasoning tare for Sapporo-style ramen?",
        "correct": "Miso",
        "distractors": ["Gochujang", "Doubanjiang", "Tianmianjiang"],
        "d": 3
    },
    {
        "q": "Which dried, smoked, and fermented skipjack tuna flakes provide the smoky umami base of Japanese dashi broth alongside kombu kelp?",
        "correct": "Katsuobushi (bonito flakes)",
        "distractors": ["Niboshi (dried sardines)", "Shiitake powder", "Nori strips"],
        "d": 3
    },
    {
        "q": "Which broad, thick species of dried kelp harvested off Hokkaido is soaked in cold water to form the glutamic acid base of Japanese dashi?",
        "correct": "Kombu",
        "distractors": ["Wakame", "Hijiki", "Arame"],
        "d": 3
    },
    {
        "q": "Which whole dried baby sardines or anchovies are simmered to create a robust, punchy dashi stock common in rustic Japanese home cooking and udon broth?",
        "correct": "Niboshi (Iriko)",
        "distractors": ["Katsuobushi", "Sababushi", "Mentaiko"],
        "d": 3
    },
    {
        "q": "Which traditional Japanese protein-packed hot pot stew is consumed in massive quantities by professional sumo wrestlers to build bulk?",
        "correct": "Chanko Nabe",
        "distractors": ["Yosenabe", "Sukiyaki", "Shabu-shabu"],
        "d": 3
    },
    {
        "q": "Which hot pot dish involves thinly sliced beef simmered at the table in a sweet and savory sauce made of soy sauce, sugar, and mirin?",
        "correct": "Sukiyaki",
        "distractors": ["Shabu-shabu", "Chanko Nabe", "Oden"],
        "d": 3
    },
    {
        "q": "Which Japanese winter stew features daikon radish, boiled eggs, konjac cakes, and fish cakes simmered in a light soy-dashi broth?",
        "correct": "Oden",
        "distractors": ["Nikujaga", "Sukiyaki", "Motsunabe"],
        "d": 3
    },
    {
        "q": "Which gelatinous gray block made from the corm of the elephant yam (konnyaku) is simmered in Japanese oden stews?",
        "correct": "Konjac (Konnyaku)",
        "distractors": ["Yuba (tofu skin)", "Aburaage", "Chikuwa"],
        "d": 3
    },
    {
        "q": "Which traditional Vietnamese beef noodle soup broth (Pho Bo) is perfumed primarily with which charred spice blend containing star anise, cloves, cinnamon, and cardamon?",
        "correct": "Pho spice aromatics",
        "distractors": ["Curry masala", "Five spice and cumin", "Galangal and lemongrass"],
        "d": 3
    },
    {
        "q": "Which large pod from the ginger family, known as 'thao qua' in Vietnam, imparts a deep smoky camphor note to authentic northern Pho Bo broth?",
        "correct": "Black cardamom",
        "distractors": ["Green cardamom", "Star anise", "Coriander pod"],
        "d": 3
    },
    {
        "q": "Which spicy, lemongrass-forward central Vietnamese noodle soup features beef shank, pork trotters, and congealed pig's blood cubes?",
        "correct": "Bún bò Huế",
        "distractors": ["Bún riêu", "Hủ tiếu Nam Vang", "Mi Quang"],
        "d": 3
    },
    {
        "q": "Which Vietnamese noodle soup features a distinctive tomato-based crab broth topped with fluffy patties of freshwater crab paste and eggs?",
        "correct": "Bún riêu cua",
        "distractors": ["Bún chả", "Bún bò Huế", "Canh chua"],
        "d": 3
    },
    {
        "q": "Which sour and sweet Mekong Delta fish soup features catfish simmered with tamarind, pineapple, tomatoes, okra, and spongy elephant ear stems (bac ha)?",
        "correct": "Canh chua",
        "distractors": ["Bún mắm", "Kho tộ", "Cháo cá"],
        "d": 3
    },
    {
        "q": "Which French fish stew from Brittany is made by layering potatoes, onions, and various firm fish cooked in butter and cider without saffron?",
        "correct": "Cotriade",
        "distractors": ["Bouillabaisse", "Bourride", "Pôchouse"],
        "d": 3
    },
    {
        "q": "Which traditional freshwater fish stew from Burgundy is prepared with pike, perch, and eel simmered in Aligoté dry white wine?",
        "correct": "Pôchouse",
        "distractors": ["Cotriade", "Bourride", "Matelote"],
        "d": 3
    },
    {
        "q": "Which French stew features freshwater eels or fish simmered in rich red wine and aromatics, thickened with butter and flour?",
        "correct": "Matelote",
        "distractors": ["Pôchouse", "Waterzooi", "Blanquette"],
        "d": 3
    },
    {
        "q": "Which Flemish stew originated in Ghent as a freshwater fish or chicken soup thickened with egg yolks, cream, and vegetable julienne in rich broth?",
        "correct": "Waterzooi",
        "distractors": ["Carbonnade", "Stoemp", "Hochepot"],
        "d": 3
    },
    {
        "q": "Which classic French braised veal dish is cooked in a light stock without browning the meat, finished with a velvety velouté enriched with cream and egg yolk?",
        "correct": "Blanquette de veau",
        "distractors": ["Boeuf Bourguignon", "Osso Buco", "Fricassée de volaille"],
        "d": 3
    },
    {
        "q": "Which traditional slow-cooked Moroccan stew, cooked in a conical earthenware vessel, relies on preserved lemons and cured green olives for its signature acidity?",
        "correct": "Tagine with preserved lemons and olives",
        "distractors": ["Couscous tfaya", "Harira", "Pastilla"],
        "d": 3
    },
    {
        "q": "Which hearty Moroccan soup served during Ramadan to break the fast is made with lamb, tomatoes, chickpeas, lentils, cilantro, celery, and vermicelli?",
        "correct": "Harira",
        "distractors": ["Chorba frik", "Lablabi", "Bissara"],
        "d": 3
    },
    {
        "q": "Which Tunisian breakfast soup consists of a rich cumin-spiced chickpea broth poured over stale crusty bread, topped with a soft-poached egg, tuna, and harissa?",
        "correct": "Lablabi",
        "distractors": ["Harira", "Shakshuka", "Bissara"],
        "d": 3
    },
    {
        "q": "Which North African thick, creamy fava bean soup seasoned with cumin, garlic, and drizzled with olive oil is a winter street food staple in Morocco?",
        "correct": "Bissara",
        "distractors": ["Lablabi", "Chorba", "Harira"],
        "d": 3
    },
    {
        "q": "Which Georgian meat soup is famous for its sour plum paste (tkemali), fatty beef, rice, walnut paste, and a liberal amount of fresh cilantro?",
        "correct": "Kharcho",
        "distractors": ["Chakapuli", "Khash", "Chikhirtma"],
        "d": 3
    },
    {
        "q": "Which Georgian spring stew features lamb chops braised with sour unripe green mirabelle plums, tarragon leaves, and dry white wine?",
        "correct": "Chakapuli",
        "distractors": ["Kharcho", "Chanakhi", "Satsivi"],
        "d": 3
    },
    {
        "q": "Which ancient Caucasian restorative hangover soup is made simply by boiling cleaned cow hooves and stomach for many hours, served unseasoned with raw garlic and salt on the side?",
        "correct": "Khash",
        "distractors": ["Kharcho", "Bozbash", "Khashlama"],
        "d": 3
    },
    {
        "q": "Which Iranian herb stew, widely regarded as the national dish of Iran, is defined by slow-simmered sautéed fresh herbs, kidney beans, lamb, and dried Persian limes (limoo amani)?",
        "correct": "Ghormeh Sabzi",
        "distractors": ["Fesenjan", "Gheimeh", "Ash Reshteh"],
        "d": 3
    }
]

if __name__ == "__main__":
    out_path = "tools/staging/ingredients_batch2.json"
    build_batch(raw_questions, out_path, batch_num=2)
