#!/usr/bin/env python3
"""
Generate Batch 7: Latin American, Caribbean, African & Fusion Specialties (100 questions).
30 Easy (d=1), 40 Medium (d=2), 30 Hard (d=3).
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ingredients_builder import build_batch

raw_questions = [
    # --- EASY (d=1, 30 questions) ---
    {
        "q": "Which fruit is the mandatory citrus juice used to 'cook' raw fresh fish in authentic Peruvian Ceviche?",
        "correct": "Lime juice",
        "distractors": ["Orange juice", "Grapefruit juice", "Pineapple juice"],
        "d": 1
    },
    {
        "q": "Which thin raw allium is sliced into fine julienne strips and tossed with fresh fish in Peruvian Ceviche?",
        "correct": "Red onion",
        "distractors": ["Yellow onion", "Shallot", "Leek"],
        "d": 1
    },
    {
        "q": "Which sweet root vegetable is boiled and served alongside fresh Peruvian ceviche to balance the acid and heat?",
        "correct": "Sweet potato (Camote)",
        "distractors": ["Carrot", "Cassava", "Beet"],
        "d": 1
    },
    {
        "q": "What cooking fat is traditionally used to slow-simmer pork until succulent and golden-crisp in Mexican Carnitas?",
        "correct": "Rendered pork lard (Manteca)",
        "distractors": ["Vegetable oil", "Olive oil", "Butter"],
        "d": 1
    },
    {
        "q": "Which fruit juice and sliced fruit is classically mounted atop a spit-roasted trompo for Mexican Tacos al Pastor?",
        "correct": "Pineapple",
        "distractors": ["Mango", "Papaya", "Orange"],
        "d": 1
    },
    {
        "q": "What brick-red seed paste from the annatto tree provides the vibrant red color and earthy spice for Tacos al Pastor and Cochinita Pibil?",
        "correct": "Achiote paste",
        "distractors": ["Paprika paste", "Chili paste", "Tomato paste"],
        "d": 1
    },
    {
        "q": "Which large, mild green chili pepper is roasted, peeled, and stuffed to make Mexican Chiles Rellenos?",
        "correct": "Poblano chili",
        "distractors": ["Jalapeño chili", "Habanero chili", "Serrano chili"],
        "d": 1
    },
    {
        "q": "Which dough made of nixtamalized corn flour (masa) and lard is wrapped in corn husks and steamed to make Mexican Tamales?",
        "correct": "Masa",
        "distractors": ["Polenta", "Cornstarch dough", "Semolina"],
        "d": 1
    },
    {
        "q": "What protective wrapping is most commonly used to steam traditional Mexican street tamales?",
        "correct": "Dried corn husks",
        "distractors": ["Parchment paper", "Aluminum foil", "Cabbage leaves"],
        "d": 1
    },
    {
        "q": "Which smoky dried and canned chili pepper in adobo sauce gives Mexican Tinga de Pollo its signature chipotle heat?",
        "correct": "Chipotle chilies in adobo",
        "distractors": ["Ancho chilies", "Guajillo chilies", "Poblano chilies"],
        "d": 1
    },
    {
        "q": "Which fiery chili pepper, rated up to 350,000 Scoville units, provides the signature heat in authentic Jamaican Jerk seasoning?",
        "correct": "Scotch bonnet pepper",
        "distractors": ["Jalapeño pepper", "Poblano pepper", "Bell pepper"],
        "d": 1
    },
    {
        "q": "Which fragrant whole berry spice, also known as pimento, is the indispensable backbone of Jamaican Jerk seasoning?",
        "correct": "Allspice berries",
        "distractors": ["Black peppercorns", "Juniper berries", "Coriander seeds"],
        "d": 1
    },
    {
        "q": "Which national fruit of Jamaica, when boiled, resembles scrambled eggs and is cooked with salted codfish in Jamaica's national dish?",
        "correct": "Ackee",
        "distractors": ["Breadfruit", "Soursop", "Plantain"],
        "d": 1
    },
    {
        "q": "Which preserved seafood meat is sautéed with boiled ackee fruit to create the national dish of Jamaica?",
        "correct": "Salted codfish (Saltfish)",
        "distractors": ["Canned tuna", "Smoked salmon", "Dried shrimp"],
        "d": 1
    },
    {
        "q": "Which Cuban shredded flank steak dish, whose name translates poetically to 'old clothes', is simmered in a rich tomato-pepper sofrito?",
        "correct": "Ropa Vieja",
        "distractors": ["Vaca Frita", "Picadillo", "Boliche"],
        "d": 1
    },
    {
        "q": "Which beef cut is braised until tender and shredded into ribbons to prepare classic Cuban Ropa Vieja?",
        "correct": "Flank steak",
        "distractors": ["Beef tenderloin", "Ribeye steak", "Ground chuck"],
        "d": 1
    },
    {
        "q": "Which savory Cuban ground beef comfort dish is flavored with tomatoes, raisins, green olives, and capers?",
        "correct": "Picadillo",
        "distractors": ["Ropa Vieja", "Vaca Frita", "Tasajo"],
        "d": 1
    },
    {
        "q": "Which green, unripe fruit is fried and mashed in a wooden pilón with garlic, broth, and crispy pork cracklings to make Puerto Rican Mofongo?",
        "correct": "Green plantains",
        "distractors": ["Green bananas", "Breadfruit", "Cassava roots"],
        "d": 1
    },
    {
        "q": "Which crunchy fried pork skin cracklings are pounded directly into the plantains in Puerto Rican Mofongo?",
        "correct": "Chicharrón",
        "distractors": ["Bacon lardons", "Prosciutto bits", "Pork rillettes"],
        "d": 1
    },
    {
        "q": "Which small, starchy legume is cooked with long-grain rice and sofrito to make Puerto Rican Arroz con Gandules?",
        "correct": "Pigeon peas (Gandules)",
        "distractors": ["Black beans", "Chickpeas", "Lentils"],
        "d": 1
    },
    {
        "q": "Which Dominican breakfast dish consists of mashed boiled green plantains topped with butter and pickled red onions?",
        "correct": "Mangú",
        "distractors": ["Mofongo", "Tostones", "Fufú"],
        "d": 1
    },
    {
        "q": "Which dense, double-fried crispy green plantain slices, smashed flat with a tostonera, are served with garlic mojo across the Caribbean?",
        "correct": "Tostones (Patacones)",
        "distractors": ["Maduros", "Mangú", "Mofongo"],
        "d": 1
    },
    {
        "q": "Which sweet, ripe plantain slices are pan-fried until caramelized and deeply browned with golden-brown edges?",
        "correct": "Maduros",
        "distractors": ["Tostones", "Mangú", "Chifles"],
        "d": 1
    },
    {
        "q": "Which Brazilian baked cheese rolls made from tapioca starch and cheese have a crisp crust and chewy, elastic interior?",
        "correct": "Pão de Queijo",
        "distractors": ["Coxinha", "Empada", "Pastel"],
        "d": 1
    },
    {
        "q": "What root starch gives Brazilian Pão de Queijo cheese breads their unique elastic, chewy chewiness?",
        "correct": "Tapioca starch (Manioc starch)",
        "distractors": ["Cornstarch", "Potato starch", "Wheat flour"],
        "d": 1
    },
    {
        "q": "Which teardrop-shaped Brazilian street food consists of seasoned shredded chicken encased in dough, battered and deep-fried?",
        "correct": "Coxinha",
        "distractors": ["Pastel", "Kibe", "Acarajé"],
        "d": 1
    },
    {
        "q": "Which red oil, extracted from the fruit of the African oil palm, gives Bahian Brazilian cooking its bright orange color and earthy flavor?",
        "correct": "Dendê oil (Red palm oil)",
        "distractors": ["Achiote oil", "Sesame oil", "Avocado oil"],
        "d": 1
    },
    {
        "q": "Which celebrated West African rice dish simmers long-grain rice in a reduced, concentrated stew of roasted red bell peppers, scotch bonnets, and tomatoes?",
        "correct": "Jollof Rice",
        "distractors": ["Waakye", "Thieboudienne", "Fried rice"],
        "d": 1
    },
    {
        "q": "Which spongy, sour sourdough fermented flatbread serves as the edible platter and utensil for Ethiopian cuisine?",
        "correct": "Injera",
        "distractors": ["Naan", "Roti", "Lavash"],
        "d": 1
    },
    {
        "q": "Which tiny, ancient gluten-free grain is fermented with water over several days to create the batter for authentic Ethiopian Injera?",
        "correct": "Teff grain",
        "distractors": ["Sorghum", "Millet", "Buckwheat"],
        "d": 1
    },

    # --- MEDIUM (d=2, 40 questions) ---
    {
        "q": "What is the potent, acidic, citrus-and-chili marinade drained from Peruvian ceviche, celebrated as a restorative hangover cure, called?",
        "correct": "Leche de Tigre (Tiger's Milk)",
        "distractors": ["Chicha Morada", "Salsa Criolla", "Aguachile"],
        "d": 2
    },
    {
        "q": "Which Peruvian stir-fry dish created by Chinese immigrants (Chifa) combines beef tenderloin, red onions, and tomatoes sautéed with soy sauce and served with French fries and rice?",
        "correct": "Lomo Saltado",
        "distractors": ["Ají de Gallina", "Seco de Res", "Arroz Chaufa"],
        "d": 2
    },
    {
        "q": "Which vibrant yellow Peruvian chili pepper paste provides the mild fruity heat and color for Lomo Saltado, Papa a la Huancaína, and Causa?",
        "correct": "Ají Amarillo",
        "distractors": ["Ají Panca", "Ají Limo", "Rocoto"],
        "d": 2
    },
    {
        "q": "Which shredded chicken dish in Peru features a rich, creamy yellow sauce made with ají amarillo, evaporated milk, walnuts, and white bread soaked in milk?",
        "correct": "Ají de Gallina",
        "distractors": ["Lomo Saltado", "Causa Limeña", "Seco de Pollo"],
        "d": 2
    },
    {
        "q": "Which chilled Peruvian terrine layers smooth mashed yellow potatoes seasoned with lime juice and ají amarillo with shredded chicken or tuna salad and avocado?",
        "correct": "Causa Rellena (Causa Limeña)",
        "distractors": ["Papa Rellena", "Papa a la Huancaína", "Pastel de Papa"],
        "d": 2
    },
    {
        "q": "Which popular Peruvian street food appetizer consists of skewered, grilled beef hearts marinated in ají panca paste, vinegar, garlic, and cumin?",
        "correct": "Anticuchos",
        "distractors": ["Churrasco", "Pinchos", "Corazón asado"],
        "d": 2
    },
    {
        "q": "Which dark red, mildly spicy Peruvian chili pepper paste with a sweet, smoky, berry-like aroma is used to marinate beef heart Anticuchos?",
        "correct": "Ají Panca",
        "distractors": ["Ají Amarillo", "Ají Limo", "Rocoto"],
        "d": 2
    },
    {
        "q": "Which Peruvian cold potato appetizer smothers boiled yellow potato slices in a velvety cheese sauce made from ají amarillo, evaporated milk, queso fresco, and saltine crackers?",
        "correct": "Papa a la Huancaína",
        "distractors": ["Causa Limeña", "Papa Rellena", "Ocopa"],
        "d": 2
    },
    {
        "q": "Which Arequipa potato dish resembles Papa a la Huancaína but features a green sauce made with the aromatic herb huacatay, peanuts, and queso fresco?",
        "correct": "Ocopa Arequipeña",
        "distractors": ["Papa a la Huancaína", "Causa Limeña", "Solterito"],
        "d": 2
    },
    {
        "q": "Which Peruvian black mint herb (Tagetes minuta) imparts a unique herbal, citrusy, and minty flavor to Ocopa sauce and Pachamanca?",
        "correct": "Huacatay",
        "distractors": ["Paico", "Muña", "Culantro"],
        "d": 2
    },
    {
        "q": "Which Mexican dish from Puebla, created to celebrate Mexican independence, consists of poblano chilies stuffed with picadillo, walnut sauce (nogada), and pomegranate seeds?",
        "correct": "Chiles en Nogada",
        "distractors": ["Chiles Rellenos", "Manchamanteles", "Mole Poblano"],
        "d": 2
    },
    {
        "q": "Which nut is soaked in milk, peeled, and blended with Mexican crema and goat cheese to make the velvety nogada sauce for Chiles en Nogada?",
        "correct": "Castilla walnuts",
        "distractors": ["Pecans", "Almonds", "Pine nuts"],
        "d": 2
    },
    {
        "q": "Which ruby-red fruit seeds are sprinkled over Mexican Chiles en Nogada along with fresh green parsley to represent the Mexican tricolor flag?",
        "correct": "Pomegranate seeds (Arils)",
        "distractors": ["Cranberries", "Red currants", "Raspberries"],
        "d": 2
    },
    {
        "q": "Which traditional Jalisco stewed meat dish, cooked with dried guajillo and ancho chilies, cinnamon, and cumin, is served with its flavorful spiced braising broth (consomé)?",
        "correct": "Birria",
        "distractors": ["Barbacoa", "Carnitas", "Pozole"],
        "d": 2
    },
    {
        "q": "Which animal meat is the traditional historic protein used for authentic Mexican Birria in Jalisco before beef became common?",
        "correct": "Goat meat (Chivo)",
        "distractors": ["Duck", "Pork belly", "Turkey"],
        "d": 2
    },
    {
        "q": "Which Mexican dish of fried corn tortilla quarters simmered in green or red salsa until softened is topped with crema, queso fresco, sliced onion, and eggs?",
        "correct": "Chilaquiles",
        "distractors": ["Enchiladas", "Totopos", "Flautas"],
        "d": 2
    },
    {
        "q": "Which Mexican culinary technique involves soaking and cooking dried field corn in an alkaline solution of water and food-grade slaked lime (calcium hydroxide)?",
        "correct": "Nixtamalization",
        "distractors": ["Parboiling", "Fermentation", "Malting"],
        "d": 2
    },
    {
        "q": "Which traditional alkaline compound (calcium hydroxide) is dissolved in water to nixtamalize field corn for tortillas?",
        "correct": "Slaked lime (Cal)",
        "distractors": ["Baking soda", "Potassium carbonate", "Wood ash only"],
        "d": 2
    },
    {
        "q": "Which Yucatecan slow-roasted pork dish is marinated in bitter Seville orange juice and achiote paste, wrapped in banana leaves, and cooked in an underground pit oven?",
        "correct": "Cochinita Pibil",
        "distractors": ["Poc Chuc", "Carnitas", "Tinga de cerdo"],
        "d": 2
    },
    {
        "q": "Which citrus juice provides the crucial acidic marinade for Yucatecan Cochinita Pibil?",
        "correct": "Bitter Seville orange (Naranja agria)",
        "distractors": ["Sweet Valencia orange", "Key lime juice", "Grapefruit juice"],
        "d": 2
    },
    {
        "q": "Which broad tropical leaves are wrapped around Cochinita Pibil and Oaxacan tamales before steaming or pit roasting?",
        "correct": "Banana leaves",
        "distractors": ["Ti leaves", "Corn husks", "Avocado leaves"],
        "d": 2
    },
    {
        "q": "Which Mexican herb with serrated leaves, used to season black beans and quesadillas, has an unmistakable pungent aroma reminiscent of petroleum and citrus?",
        "correct": "Epazote",
        "distractors": ["Cilantro", "Culantro", "Papalo"],
        "d": 2
    },
    {
        "q": "Which fresh, broad-leafed Mexican herb, commonly eaten raw in tacos in Puebla, is known for its intense floral, rue-like aromatic profile?",
        "correct": "Pápalo (Pápaloquelite)",
        "distractors": ["Epazote", "Hoja santa", "Pipicha"],
        "d": 2
    },
    {
        "q": "Which Bahian seafood stew from northeastern Brazil simmers white fish and shrimp in a broth of coconut milk, dendê red palm oil, tomatoes, onions, and cilantro?",
        "correct": "Moqueca Baiana",
        "distractors": ["Moqueca Capixaba", "Bobó de Camarão", "Vatapá"],
        "d": 2
    },
    {
        "q": "How does Moqueca Capixaba from the state of Espírito Santo differ fundamentally from Bahian Moqueca?",
        "correct": "It uses olive oil and urucum (annatto) without coconut milk or dendê oil",
        "distractors": ["It uses beef instead of seafood", "It uses heavy cow cream and potatoes", "It is cooked dry without broth"],
        "d": 2
    },
    {
        "q": "Which Bahian dish features black-eyed pea dough peeled, whipped, and deep-fried in bubbling red dendê palm oil, then split open and filled with vatapá and dried shrimp?",
        "correct": "Acarajé",
        "distractors": ["Abará", "Coxinha", "Pastel de feijão"],
        "d": 2
    },
    {
        "q": "Which steamed version of Acarajé wraps the seasoned black-eyed pea paste in banana leaves and steams it rather than frying in dendê oil?",
        "correct": "Abará",
        "distractors": ["Acarajé", "Pamonha", "Maniçoba"],
        "d": 2
    },
    {
        "q": "Which rich Bahian paste made by blending breadcrumbs, dried shrimp, ground cashews, peanuts, coconut milk, and dendê oil is spooned into acarajé?",
        "correct": "Vatapá",
        "distractors": ["Caruru", "Bobó", "Farofa"],
        "d": 2
    },
    {
        "q": "Which traditional Bahian dish simmers sliced okra with dried shrimp, ground peanuts, cashews, palm oil, and dende oil?",
        "correct": "Caruru",
        "distractors": ["Vatapá", "Moqueca", "Bobó de camarão"],
        "d": 2
    },
    {
        "q": "Which creamy Brazilian chowder features large shrimp cooked in a velvety puree of manioc (cassava), coconut milk, and dendê palm oil?",
        "correct": "Bobó de Camarão",
        "distractors": ["Moqueca Baiana", "Vatapá", "Tacacá"],
        "d": 2
    },
    {
        "q": "Which street food from Trinidad and Tobago consists of two small turmeric-spiced fried flatbreads (bara) filled with curried chickpeas (channa) and mango kuchela?",
        "correct": "Doubles",
        "distractors": ["Roti canai", "Bake and Shark", "Pholourie"],
        "d": 2
    },
    {
        "q": "Which Trinidadian seaside beach snack consists of deep-fried shark meat seasoned with green seasoning stuffed into a fried yeast bread bake with condiments?",
        "correct": "Bake and Shark",
        "distractors": ["Doubles", "Pelau", "Callaloo"],
        "d": 2
    },
    {
        "q": "Which one-pot Trinidadian rice dish caramelizes chicken in burnt brown sugar before simmering with pigeon peas, rice, pumpkin, and coconut milk?",
        "correct": "Pelau",
        "distractors": ["Jollof rice", "Cook-up rice", "Arroz con pollo"],
        "d": 2
    },
    {
        "q": "Which Caribbean green soup or stew, considered the national dish of Dominica and Trinidad, is made by simmering dasheen (taro) bush leaves with okra and coconut milk?",
        "correct": "Callaloo",
        "distractors": ["Pepperpot", "Oil Down", "Souse"],
        "d": 2
    },
    {
        "q": "Which national dish of Grenada is a one-pot stew of salted meat, breadfruit, callaloo leaves, and dumplings simmered down in coconut milk until oil remains?",
        "correct": "Oil Down",
        "distractors": ["Callaloo", "Pepperpot", "Cou-cou"],
        "d": 2
    },
    {
        "q": "Which Guyanese Amerindian holiday meat stew is slow-cooked in a dark sauce derived from boiled bitter cassava juice called cassareep?",
        "correct": "Guyanese Pepperpot",
        "distractors": ["Oil Down", "Cook-up Rice", "Metemgee"],
        "d": 2
    },
    {
        "q": "What thick, black, molasses-like syrup made by boiling down the juice of bitter cassava roots is the preservative base for Guyanese Pepperpot?",
        "correct": "Cassareep",
        "distractors": ["Molasses", "Tamarind syrup", "Pekmez"],
        "d": 2
    },
    {
        "q": "Which national dish of Barbados pairs flying fish poached in aromatic broth with a porridge of yellow cornmeal and chopped okra called:",
        "correct": "Cou-cou and Flying Fish",
        "distractors": ["Fungi and Fish", "Polenta and Saltfish", "Callaloo and Bakes"],
        "d": 2
    },
    {
        "q": "Which complex Ethiopian spice blend featuring chili peppers, ginger, garlic, korarima, rue, and fenugreek is the foundation of red wot stews?",
        "correct": "Berbere",
        "distractors": ["Mitmita", "Ras el hanout", "Dukkah"],
        "d": 2
    },
    {
        "q": "Which fiery Ethiopian spice powder made primarily of African bird's eye chilies, cardamom, cloves, and salt is served as a dipping condiment for raw beef (kitfo)?",
        "correct": "Mitmita",
        "distractors": ["Berbere", "Makalesha", "Awaze"],
        "d": 2
    },

    # --- HARD (d=3, 30 questions) ---
    {
        "q": "Which spiced clarified butter infused with ginger, garlic, fenugreek, korarima, and nigella seeds is the essential fat in Ethiopian cooking?",
        "correct": "Niter Kibbeh",
        "distractors": ["Ghee", "Samneh", "Smen"],
        "d": 3
    },
    {
        "q": "Which celebratory Ethiopian national dish features chicken pieces and whole hard-boiled eggs simmered in a dense, caramelized onion and berbere sauce?",
        "correct": "Doro Wat",
        "distractors": ["Sega Wat", "Tibs", "Shiro Wat"],
        "d": 3
    },
    {
        "q": "Which traditional Ethiopian dish consists of raw minced lean beef seasoned with warm niter kibbeh and fiery mitmita spice powder, served with ayib cheese?",
        "correct": "Kitfo",
        "distractors": ["Gored Gored", "Doro Wat", "Tibs"],
        "d": 3
    },
    {
        "q": "Which Ethiopian vegetarian stew is made of slow-simmered powdered dried chickpeas or broad beans cooked with minced onions, garlic, and berbere?",
        "correct": "Shiro Wat",
        "distractors": ["Misir Wat", "Kik Alicha", "Gomen Wat"],
        "d": 3
    },
    {
        "q": "Which mild Ethiopian vegetarian stew features split red lentils simmered gently with berbere, garlic, and ginger until tender and creamy?",
        "correct": "Misir Wat",
        "distractors": ["Shiro Wat", "Kik Alicha", "Atakilt Wat"],
        "d": 3
    },
    {
        "q": "Which West African soup is thickened with the protein-rich ground white seeds of wild melon or gourd plants, cooked with leafy greens and palm oil?",
        "correct": "Egusi Soup",
        "distractors": ["Ogbono Soup", "Banga Soup", "Afang Soup"],
        "d": 3
    },
    {
        "q": "Which Nigerian soup gets its unique mucilaginous, drawing (slippery) texture from ground wild mango seeds (bush mango seeds)?",
        "correct": "Ogbono Soup",
        "distractors": ["Egusi Soup", "Efo Riro", "Banga Soup"],
        "d": 3
    },
    {
        "q": "Which rich Delta Nigerian soup is made from the fresh oily extract of oil palm nuts, simmered with dried seafood, smoked catfish, and aromatic oburunbebe stick?",
        "correct": "Banga Soup (Ofe Akwu)",
        "distractors": ["Ogbono Soup", "Egusi Soup", "Bitterleaf Soup"],
        "d": 3
    },
    {
        "q": "Which Nigerian rich vegetable stew from Yorubaland features shredded shoko or tete greens, palm oil, locust beans (iru), bell pepper puree, and assorted meats?",
        "correct": "Efo Riro",
        "distractors": ["Afang Soup", "Edikang Ikong", "Okra Soup"],
        "d": 3
    },
    {
        "q": "Which fermented African locust bean condiment (Parkia biglobosa), known as Iru or Dawadawa, provides a deep pungent umami funk to West African soups?",
        "correct": "Iru (Dawadawa)",
        "distractors": ["Ogiri", "Crayfish powder", "Potash"],
        "d": 3
    },
    {
        "q": "Which traditional fermented condiment used in Igbo soups like Ofe Onugbu is made by fermenting melon seeds or castor oil seeds?",
        "correct": "Ogiri",
        "distractors": ["Iru", "Dawadawa", "Uda"],
        "d": 3
    },
    {
        "q": "Which Nigerian grilled beef skewer street food is dusted generously in Yaji spice blend containing ground defatted roasted peanuts, ginger, garlic, and chili?",
        "correct": "Suya",
        "distractors": ["Kilishi", "Asun", "Tsire"],
        "d": 3
    },
    {
        "q": "Which paper-thin, sun-dried jerky-like meat snack from Northern Nigeria is dipped in peanut paste, seasoned with spices, and dried on rush mats?",
        "correct": "Kilishi",
        "distractors": ["Suya", "Biltong", "Droëwors"],
        "d": 3
    },
    {
        "q": "Which South African cured, air-dried meat delicacy is marinated in vinegar, toasted coriander seeds, black pepper, and coarse salt before hanging?",
        "correct": "Biltong",
        "distractors": ["Droëwors", "Kilishi", "Pastirma"],
        "d": 3
    },
    {
        "q": "Which traditional South African dried sausage is made from spiced minced beef and mutton seasoned with toasted coriander seeds?",
        "correct": "Droëwors",
        "distractors": ["Boerewors", "Biltong", "Braaiwors"],
        "d": 3
    },
    {
        "q": "Which spiral-coiled South African fresh sausage made of coarsely minced beef and pork is spiced with toasted coriander seeds, nutmeg, cloves, and vinegar for the braai?",
        "correct": "Boerewors",
        "distractors": ["Droëwors", "Bratwurst", "Kielbasa"],
        "d": 3
    },
    {
        "q": "Which baked South African Cape Malay comfort dish consists of spiced minced meat topped with an egg-and-milk savory custard and bay leaves?",
        "correct": "Bobotie",
        "distractors": ["Potjiekos", "Sosaties", "Bunny Chow"],
        "d": 3
    },
    {
        "q": "Which Durban street food dish consists of a hollowed-out loaf of white sandwich bread filled to the brim with rich, spicy mutton or chicken curry?",
        "correct": "Bunny Chow",
        "distractors": ["Gatsby", "Bobotie", "Vetkoek"],
        "d": 3
    },
    {
        "q": "Which Cape Town giant submarine sandwich is layered with sliced meats, polony or steak, lettuce, piri-piri sauce, and a massive portion of hot French fries (slap chips)?",
        "correct": "Gatsby sandwich",
        "distractors": ["Bunny Chow", "Kota", "Vetkoek"],
        "d": 3
    },
    {
        "q": "Which South African deep-fried yeast dough bread pocket, meaning 'fat cake', is typically stuffed with savory curried ground beef mince?",
        "correct": "Vetkoek",
        "distractors": ["Koeksister", "Gatsby", "Potbrood"],
        "d": 3
    },
    {
        "q": "Which Cape Malay deep-fried braided pastry is soaked in ice-cold ginger-and-cinnamon sugar syrup immediately after frying to achieve a syrupy, crisp shell?",
        "correct": "Koeksister",
        "distractors": ["Vetkoek", "Malva pudding", "Melktert"],
        "d": 3
    },
    {
        "q": "Which classic South African baked dessert tart consists of a sweet pastry crust filled with a creamy cooked milk, egg, and flour custard, dusted generously with cinnamon?",
        "correct": "Melktert (Milk Tart)",
        "distractors": ["Malva pudding", "Koeksister", "Hertzoggie"],
        "d": 3
    },
    {
        "q": "Which spongy, caramelized South African baked pudding contains apricot jam and a touch of vinegar, drenched in a warm sweet cream sauce while hot?",
        "correct": "Malva Pudding",
        "distractors": ["Melktert", "Sticky toffee pudding", "Queen of Puddings"],
        "d": 3
    },
    {
        "q": "Which national dish of Senegal, widely regarded as the ancestor of Jollof rice, features fresh fish stuffed with herb paste, cooked with broken rice and vegetables in tomato broth?",
        "correct": "Thieboudienne (Ceebu Jën)",
        "distractors": ["Yassa Poulet", "Maafe", "Soupou Kandja"],
        "d": 3
    },
    {
        "q": "Which Senegalese chicken dish is marinated in a massive quantity of caramelized onions, Dijon mustard, garlic, and fresh lemon juice before braising?",
        "correct": "Yassa Poulet",
        "distractors": ["Thieboudienne", "Maafe", "Dibi"],
        "d": 3
    },
    {
        "q": "Which West and Central African stew features meat simmered in a rich, creamy sauce made from roasted ground peanut (groundnut) paste and tomato paste?",
        "correct": "Maafe (Groundnut Stew)",
        "distractors": ["Yassa", "Thieboudienne", "Ndole"],
        "d": 3
    },
    {
        "q": "Which national dish of Cameroon consists of stewed bitterleaf greens simmered with ground blanched peanuts, crayfish, beef, and shrimp?",
        "correct": "Ndolé",
        "distractors": ["Maafe", "Koki", "Saka Saka"],
        "d": 3
    },
    {
        "q": "Which Central African stew is prepared by pounding and cooking tender cassava leaves with palm oil, garlic, and smoked fish or peanut butter?",
        "correct": "Saka Saka (Pondu)",
        "distractors": ["Ndolé", "Matoke", "Maboké"],
        "d": 3
    },
    {
        "q": "Which national dish of Uganda consists of green cooking bananas steamed in banana leaves and mashed into a smooth, golden mound?",
        "correct": "Matoke",
        "distractors": ["Ugali", "Saka Saka", "Sukuma Wiki"],
        "d": 3
    },
    {
        "q": "Which East African staple vegetable dish, whose Swahili name translates to 'stretch the week', consists of braised collard greens sautéed with onions and tomatoes?",
        "correct": "Sukuma Wiki",
        "distractors": ["Ugali", "Matoke", "Kachumbari"],
        "d": 3
    }
]

if __name__ == "__main__":
    out_path = "tools/staging/ingredients_batch7.json"
    build_batch(raw_questions, out_path, batch_num=7)
