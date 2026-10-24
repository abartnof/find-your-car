#!/usr/bin/env python3
"""
Generate Batch 6: Celebrated Asian & Middle Eastern Cuisines (100 questions).
30 Easy (d=1), 40 Medium (d=2), 30 Hard (d=3).
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ingredients_builder import build_batch

raw_questions = [
    # --- EASY (d=1, 30 questions) ---
    {
        "q": "Which crushed nut is the traditional crunchy garnish sprinkled over classic Thai Pad Thai?",
        "correct": "Roasted peanuts",
        "distractors": ["Cashews", "Almonds", "Sesame seeds"],
        "d": 1
    },
    {
        "q": "Which fruit paste provides the essential sour and sweet tang in authentic Thai Pad Thai sauce?",
        "correct": "Tamarind paste",
        "distractors": ["Tomato paste", "Lime pickle", "Plum paste"],
        "d": 1
    },
    {
        "q": "Which green herb is the key aromatic stirred into Thai Green Curry along with kaffir lime leaves?",
        "correct": "Thai sweet basil",
        "distractors": ["Spearmint", "Parsley", "Coriander root"],
        "d": 1
    },
    {
        "q": "Which liquid provides the rich, creamy sauce base for traditional Thai red and green curries?",
        "correct": "Coconut milk",
        "distractors": ["Heavy cow cream", "Soy milk", "Almond milk"],
        "d": 1
    },
    {
        "q": "What type of short-grain rice, seasoned with rice vinegar, sugar, and salt, forms the base of Japanese sushi?",
        "correct": "Sumeshi (seasoned sushi rice)",
        "distractors": ["Jasmine rice", "Basmati rice", "Brown glutinous rice"],
        "d": 1
    },
    {
        "q": "Which sheet of dried edible seaweed is wrapped around sushi rolls and onigiri?",
        "correct": "Nori",
        "distractors": ["Wakame", "Kombu", "Dulse"],
        "d": 1
    },
    {
        "q": "Which Japanese dish consists of seafood and vegetables dipped in a light batter of ice water and flour, then deep-fried crisp?",
        "correct": "Tempura",
        "distractors": ["Karaage", "Tonkatsu", "Katsu"],
        "d": 1
    },
    {
        "q": "Which coarse Japanese breadcrumbs give tonkatsu and fried cutlets their light, airy, extra-crunchy texture?",
        "correct": "Panko",
        "distractors": ["Cornstarch", "Puffed rice", "Bread flour"],
        "d": 1
    },
    {
        "q": "Which meat cut is traditionally breaded in panko and deep-fried to make Japanese Tonkatsu?",
        "correct": "Pork cutlet",
        "distractors": ["Beef short rib", "Chicken drumstick", "Lamb chop"],
        "d": 1
    },
    {
        "q": "Which Japanese skewered chicken pieces grilled over charcoal are brushed with a savory-sweet soy glaze called tare?",
        "correct": "Yakitori",
        "distractors": ["Yakitori-don", "Kushikatsu", "Satay"],
        "d": 1
    },
    {
        "q": "Which classic Chinese dish features roast duck with crisp lacquered skin, served with paper-thin pancakes and sweet bean sauce?",
        "correct": "Peking duck",
        "distractors": ["Cantonese roast duck", "Nanjing salted duck", "Zhangcha tea-smoked duck"],
        "d": 1
    },
    {
        "q": "Which Sichuan tofu dish combines soft tofu cubes and minced meat in a fiery chili oil and fermented bean sauce scented with Sichuan peppercorns?",
        "correct": "Mapo Tofu",
        "distractors": ["Kung Pao Tofu", "Stinky Tofu", "Braised Home-style Tofu"],
        "d": 1
    },
    {
        "q": "Which distinctive spice causes the famous mouth-numbing tingling sensation (ma) in Sichuan Mapo Tofu and Kung Pao chicken?",
        "correct": "Sichuan peppercorn",
        "distractors": ["Black pepper", "White pepper", "Pink peppercorn"],
        "d": 1
    },
    {
        "q": "Which nut is classically tossed into Sichuan Kung Pao Chicken along with dried red chilies and scallions?",
        "correct": "Roasted peanuts",
        "distractors": ["Pistachios", "Walnuts", "Pine nuts"],
        "d": 1
    },
    {
        "q": "What liquid element is sealed inside Shanghainese Xiao Long Bao (soup dumplings) that turns into hot soup when steamed?",
        "correct": "Chilled gelatinized meat aspic broth",
        "distractors": ["Injected chicken bouillon", "Melted cheese", "Soy sauce and vinegar"],
        "d": 1
    },
    {
        "q": "Which French-influenced Vietnamese sandwich is served in an airy baguette spread with pâté and filled with pickled daikon and carrots?",
        "correct": "Bánh Mì",
        "distractors": ["Bánh Xèo", "Bánh Cuốn", "Bao"],
        "d": 1
    },
    {
        "q": "Which pickled root vegetable duo provides the signature crunchy sweet-sour bite inside a Vietnamese Bánh Mì?",
        "correct": "Pickled daikon and carrots (Đồ chua)",
        "distractors": ["Pickled onions and cucumbers", "Sauerkraut and beets", "Pickled ginger and cabbage"],
        "d": 1
    },
    {
        "q": "Which thin, translucent sheets made from rice flour and water are soaked in warm water to roll Vietnamese fresh spring rolls (Gỏi cuốn)?",
        "correct": "Rice paper (Bánh tráng)",
        "distractors": ["Wonton wrappers", "Egg roll wrappers", "Phyllo dough"],
        "d": 1
    },
    {
        "q": "Which long-grain fragrant rice variety native to the foothills of the Himalayas is the benchmark rice for Indian Biryani?",
        "correct": "Basmati rice",
        "distractors": ["Jasmine rice", "Sushi rice", "Bomba rice"],
        "d": 1
    },
    {
        "q": "Which non-melting fresh curd cheese made by curdling heated cow or buffalo milk with lemon juice is standard in Indian cooking?",
        "correct": "Paneer",
        "distractors": ["Halloumi", "Queso fresco", "Tofu"],
        "d": 1
    },
    {
        "q": "Which leafy green vegetable forms the smooth green spiced gravy of Indian Palak Paneer?",
        "correct": "Spinach",
        "distractors": ["Fenugreek", "Mustard greens", "Kale"],
        "d": 1
    },
    {
        "q": "Which clarified butter, heated until water evaporates and milk solids are strained out, is the sacred cooking fat of traditional Indian cuisine?",
        "correct": "Ghee",
        "distractors": ["Lard", "Suet", "Tallow"],
        "d": 1
    },
    {
        "q": "Which Indian curry features tandoori chicken simmered in a velvety sauce of tomatoes, butter, cream, and aromatic spices?",
        "correct": "Butter Chicken (Murgh Makhani)",
        "distractors": ["Chicken Vindaloo", "Chicken Korma", "Chicken Madras"],
        "d": 1
    },
    {
        "q": "Which legume is cooked with spices, ginger, and garlic to prepare the everyday Indian staple known as dal?",
        "correct": "Lentils (or split pulses)",
        "distractors": ["Soybeans", "Lima beans", "Green peas"],
        "d": 1
    },
    {
        "q": "Which crisp, triangular deep-fried pastry pocket is stuffed with spiced potatoes, green peas, and cumin seeds in India?",
        "correct": "Samosa",
        "distractors": ["Pakora", "Bhajji", "Kachori"],
        "d": 1
    },
    {
        "q": "Which deep-fried fritter balls or patties are made of soaked ground chickpeas or fava beans mixed with parsley, cilantro, and garlic?",
        "correct": "Falafel",
        "distractors": ["Kibbeh", "Kofta", "Sambousek"],
        "d": 1
    },
    {
        "q": "Which North African and Middle Eastern skillet dish consists of gently poached whole eggs in a simmering sauce of tomatoes, bell peppers, garlic, and cumin?",
        "correct": "Shakshuka",
        "distractors": ["Menemen", "Huevos rancheros", "Matbucha"],
        "d": 1
    },
    {
        "q": "Which Middle Eastern flatbread baked in hot ovens forms the traditional pocket for shawarma and falafel?",
        "correct": "Pita bread",
        "distractors": ["Naan", "Lavash", "Roti"],
        "d": 1
    },
    {
        "q": "Which roasted ground spice gives Indian curry dishes their earthy flavor and characteristic warm brown undertone?",
        "correct": "Ground cumin",
        "distractors": ["Cardamom", "Vanilla", "Nutmeg"],
        "d": 1
    },
    {
        "q": "Which ground spice root gives Indian curries their intense golden-yellow hue?",
        "correct": "Turmeric",
        "distractors": ["Paprika", "Saffron", "Ginger"],
        "d": 1
    },

    # --- MEDIUM (d=2, 40 questions) ---
    {
        "q": "Which Thai street food dish features minced chicken or pork stir-fried violently with holy basil, garlic, and bird's eye chilies, served with a crispy fried egg?",
        "correct": "Pad Kra Pao",
        "distractors": ["Pad See Ew", "Pad Kee Mao", "Khao Pad"],
        "d": 2
    },
    {
        "q": "Which distinct variety of basil, having a slightly peppery clove-like taste, is strictly required for authentic Thai Pad Kra Pao?",
        "correct": "Thai holy basil (Bai Krapow)",
        "distractors": ["Thai sweet basil (Bai Horapha)", "Lemon basil (Bai Maenglak)", "Genovese sweet basil"],
        "d": 2
    },
    {
        "q": "Which wide, flat rice noodle dish, whose name translates to 'drunken noodles', is stir-fried with meat, holy basil, garlic, and fresh peppercorns?",
        "correct": "Pad Kee Mao",
        "distractors": ["Pad See Ew", "Pad Thai", "Kuay Teow"],
        "d": 2
    },
    {
        "q": "Which Thai stir-fried flat noodle dish combines broad rice noodles with Chinese broccoli (gai lan), egg, and dark sweet soy sauce?",
        "correct": "Pad See Ew",
        "distractors": ["Pad Kee Mao", "Pad Thai", "Rad Na"],
        "d": 2
    },
    {
        "q": "Which rich, peanut-studded Thai curry influenced by Muslim spice traders incorporates whole warm spices like cardamom, cinnamon, cloves, and star anise with potatoes?",
        "correct": "Massaman Curry",
        "distractors": ["Panang Curry", "Green Curry", "Yellow Curry"],
        "d": 2
    },
    {
        "q": "Which Northern Thai noodle soup features egg noodles in a rich coconut-curry broth, topped with fried crispy egg noodles, shallots, and pickled greens?",
        "correct": "Khao Soi",
        "distractors": ["Laksa", "Mohinga", "Khao Man Gai"],
        "d": 2
    },
    {
        "q": "Which Japanese savory pancake, whose name means 'grilled as you like', features shredded cabbage, batter, pork belly, okonomiyaki sauce, and dancing bonito flakes?",
        "correct": "Okonomiyaki",
        "distractors": ["Takoyaki", "Monjayaki", "Taiyaki"],
        "d": 2
    },
    {
        "q": "Which street food balls from Osaka are made by pouring seasoned batter into spherical molds with diced octopus tentacles, pickled ginger, and green onions?",
        "correct": "Takoyaki",
        "distractors": ["Okonomiyaki", "Kushikatsu", "Yakitori"],
        "d": 2
    },
    {
        "q": "Which Japanese comfort food bowl, whose name translates to 'parent and child bowl', simmers chicken pieces, beaten eggs, and sliced onions in sweet dashi broth over rice?",
        "correct": "Oyakodon",
        "distractors": ["Gyudon", "Katsudon", "Tendon"],
        "d": 2
    },
    {
        "q": "Which Japanese rice bowl tops steamed white rice with a crisp deep-fried pork cutlet and sliced onions simmered in egg and sweet dashi?",
        "correct": "Katsudon",
        "distractors": ["Gyudon", "Oyakodon", "Unadon"],
        "d": 2
    },
    {
        "q": "Which Japanese beef bowl tops steamed rice with paper-thin beef slices and onions gently simmered in a sweet soy-mirin-dashi sauce?",
        "correct": "Gyudon",
        "distractors": ["Katsudon", "Butadon", "Oyakodon"],
        "d": 2
    },
    {
        "q": "Which Japanese grilled eel dish served over rice is glazed continuously with a sticky, caramelized sauce made from eel bones, soy sauce, and mirin?",
        "correct": "Unadon (Unagi Kabayaki)",
        "distractors": ["Katsudon", "Anago don", "Tendon"],
        "d": 2
    },
    {
        "q": "Which Chinese roasted pork delicacy from Canton is marinated in fermented red bean curd, hoisin sauce, maltose, five-spice powder, and Shaoxing wine?",
        "correct": "Char Siu",
        "distractors": ["Siu Yuk", "Dongpo Pork", "Twice-Cooked Pork"],
        "d": 2
    },
    {
        "q": "Which Cantonese roast pork dish features tender pork belly roasted until its rind puffs up into intensely crispy, bubbly, golden crackling skin?",
        "correct": "Siu Yuk (Crispy Roast Pork Belly)",
        "distractors": ["Char Siu", "Dongpo Pork", "Sweet and Sour Pork"],
        "d": 2
    },
    {
        "q": "Which Hangzhou braised pork belly dish, named after a famous Song Dynasty poet, is braised in Shaoxing wine, sugar, and soy sauce until melt-in-the-mouth tender?",
        "correct": "Dongpo Pork",
        "distractors": ["Hong Shao Rou", "Char Siu", "Lu Rou Fan"],
        "d": 2
    },
    {
        "q": "Which famous Hunanese red-braised pork dish, famously loved by Chairman Mao, simmers pork belly with caramelized rock sugar, dark soy, and spices?",
        "correct": "Hong Shao Rou (Red-Braised Pork)",
        "distractors": ["Dongpo Pork", "Char Siu", "Mao Tofu"],
        "d": 2
    },
    {
        "q": "Which Sichuan noodle dish features spicy chili oil, toasted sesame paste, Sichuan pepper, and savory ground pork cooked with preserved mustard greens (sui mi ya cai)?",
        "correct": "Dan Dan Noodles",
        "distractors": ["Zha Jiang Mian", "Biang Biang Noodles", "Liangpi"],
        "d": 2
    },
    {
        "q": "Which northern Chinese noodle dish features thick wheat noodles topped with a rich dark sauce made by frying ground pork in sweet bean sauce and fermented bean paste?",
        "correct": "Zha Jiang Mian",
        "distractors": ["Dan Dan Noodles", "Wonton Noodles", "Dapanji"],
        "d": 2
    },
    {
        "q": "Which Shaanxi specialty features thick, wide hand-ripped wheat noodles tossed with hot oil poured over garlic, chili flakes, and scallions to sizzle?",
        "correct": "Biang Biang Noodles",
        "distractors": ["Dan Dan Noodles", "Lamian", "Dao Xiao Mian"],
        "d": 2
    },
    {
        "q": "Which Shaanxi hand-held street food, often called the 'Chinese hamburger', features tender braised spiced pork belly stuffed into a crisp griddled flatbread (baijimo)?",
        "correct": "Rou Jia Mo",
        "distractors": ["Gua Bao", "Baozi", "Shengjianbao"],
        "d": 2
    },
    {
        "q": "Which Taiwanese steamed open bun, resembling a 'tiger bites pig', is filled with braised pork belly, pickled mustard greens, crushed sweetened peanuts, and cilantro?",
        "correct": "Gua Bao",
        "distractors": ["Rou Jia Mo", "Xiaolongbao", "Mantou"],
        "d": 2
    },
    {
        "q": "Which Taiwanese comfort food dish consists of finely minced pork belly braised with fried shallots, soy sauce, five spice, and rock sugar spooned over steamed white rice?",
        "correct": "Lu Rou Fan (Braised Pork Rice)",
        "distractors": ["Gua Bao", "Zongzi", "Minced Beef Rice"],
        "d": 2
    },
    {
        "q": "Which classic Cantonese dim sum dumpling features whole shrimp encased in a translucent, pleated wrapper made from wheat and tapioca starch?",
        "correct": "Har Gow",
        "distractors": ["Shumai", "Wonton", "Potsticker"],
        "d": 2
    },
    {
        "q": "Which open-topped steamed Cantonese dim sum dumpling has a filling of ground pork, diced shrimp, and shiitake mushrooms, wrapped in a thin yellow egg skin?",
        "correct": "Shu Mai (Siu Mai)",
        "distractors": ["Har Gow", "Cheong Fun", "Lo Mai Gai"],
        "d": 2
    },
    {
        "q": "Which Cantonese dim sum dish features glutinous sticky rice filled with chicken, Chinese sausage, salted egg yolk, and shiitake mushrooms, wrapped and steamed in lotus leaves?",
        "correct": "Lo Mai Gai",
        "distractors": ["Zongzi", "Har Gow", "Cheong Fun"],
        "d": 2
    },
    {
        "q": "Which crispy, sizzling Vietnamese crepe made from rice flour, coconut milk, and turmeric is stuffed with sliced pork, shrimp, and bean sprouts?",
        "correct": "Bánh Xèo",
        "distractors": ["Bánh Cuốn", "Bánh Khốt", "Bánh Mì"],
        "d": 2
    },
    {
        "q": "Which Hanoi noodle dish features grilled seasoned pork patties and pork belly strips served in a bowl of warm diluted fish sauce with pickled papaya, herbs, and vermicelli?",
        "correct": "Bún Chả",
        "distractors": ["Bún Bò Huế", "Bún Riêu", "Bún Thịt Nướng"],
        "d": 2
    },
    {
        "q": "Which Southern Vietnamese noodle bowl layers rice vermicelli with char-grilled marinated pork slices, crispy egg rolls, fresh greens, and nước chấm dressing?",
        "correct": "Bún Thịt Nướng",
        "distractors": ["Bún Chả", "Bún Bò Nam Bộ", "Hủ Tiếu"],
        "d": 2
    },
    {
        "q": "Which royal Kashmiri meat stew features braised lamb cooked with Kashmiri red chilies, ground fennel seeds, dried ginger, and yogurt in mustard oil?",
        "correct": "Rogan Josh",
        "distractors": ["Lamb Korma", "Lamb Vindaloo", "Lamb Madras"],
        "d": 2
    },
    {
        "q": "Which spicy Goan curry of Portuguese origin is characterized by pork or meat marinated in garlic, red chilies, and sharp wine vinegar?",
        "correct": "Vindaloo",
        "distractors": ["Xacuti", "Cafreal", "Balchão"],
        "d": 2
    },
    {
        "q": "Which Goan spiced chicken or meat dish features chicken braised in a green paste of fresh coriander, green chilies, mint, garlic, and rum/vinegar?",
        "correct": "Cafreal",
        "distractors": ["Vindaloo", "Xacuti", "Korma"],
        "d": 2
    },
    {
        "q": "Which famous creamy North Indian lentil dish from Delhi is made by slow-cooking whole black lentils (urad dal) and kidney beans with butter, tomato puree, and cream for 24 hours?",
        "correct": "Dal Makhani",
        "distractors": ["Dal Tadka", "Chana Masala", "Sambar"],
        "d": 2
    },
    {
        "q": "What culinary technique in Indian cooking involves frying whole spices (such as mustard seeds, cumin, and dried chilies) in hot oil or ghee before pouring over a dish?",
        "correct": "Tadka (Tempering / Chaunk)",
        "distractors": ["Dum", "Bhunao", "Tandoor"],
        "d": 2
    },
    {
        "q": "Which slow-cooking method in Indian cuisine involves sealing a heavy cooking pot with dough to trap steam while meats and rice cook slowly over embers?",
        "correct": "Dum cooking",
        "distractors": ["Tandoor", "Tadka", "Tawa"],
        "d": 2
    },
    {
        "q": "Which fermented South Indian breakfast crepe is made from a ground, fermented batter of parboiled rice and skinned black gram (urad dal)?",
        "correct": "Dosa",
        "distractors": ["Idli", "Uttapam", "Appam"],
        "d": 2
    },
    {
        "q": "Which steamed, fluffy South Indian savory cakes are made from the same fermented rice and black gram batter as dosas?",
        "correct": "Idli",
        "distractors": ["Dosa", "Vada", "Puttu"],
        "d": 2
    },
    {
        "q": "Which crisp, doughnut-shaped deep-fried savory snack from South India is made from spiced black gram (urad dal) batter?",
        "correct": "Medu Vada",
        "distractors": ["Samosa", "Pakora", "Bonda"],
        "d": 2
    },
    {
        "q": "Which Persian festive stew features chicken or duck simmered gently in a thick, velvety brown sauce made of toasted ground walnuts and tart pomegranate molasses?",
        "correct": "Fesenjān",
        "distractors": ["Ghormeh Sabzi", "Gheimeh", "Abgoosht"],
        "d": 2
    },
    {
        "q": "Which Persian slow-cooked comfort stew consists of lamb cubes, yellow split peas, and dried Persian limes, topped with matchstick fried potatoes?",
        "correct": "Khoresh Gheimeh",
        "distractors": ["Ghormeh Sabzi", "Fesenjān", "Baghali Polo"],
        "d": 2
    },
    {
        "q": "Which fragrant Persian rice pilaf is layered with dill weed and tender young fava beans (broad beans), traditionally served with slow-braised lamb shanks?",
        "correct": "Baghali Polo",
        "distractors": ["Zereshk Polo", "Sabzi Polo", "Tahchin"],
        "d": 2
    },

    # --- HARD (d=3, 30 questions) ---
    {
        "q": "Which prized crisp, golden layer of crust that forms at the bottom of a Persian rice pot is called:",
        "correct": "Tahdig",
        "distractors": ["Socarrat", "Nurungji", "Guoba"],
        "d": 3
    },
    {
        "q": "Which Persian baked saffron rice cake is layered with braised chicken or lamb, egg yolks, thick yogurt, and topped with tart barberries?",
        "correct": "Tahchin",
        "distractors": ["Baghali Polo", "Zereshk Polo", "Chelo Kabab"],
        "d": 3
    },
    {
        "q": "Which tart, tiny dried red berries, sautéed in butter with sugar and saffron, are scattered across Persian basmati rice in Zereshk Polo?",
        "correct": "Barberries (Zereshk)",
        "distractors": ["Pomegranate arils", "Dried cranberries", "Red currants"],
        "d": 3
    },
    {
        "q": "Which traditional Iranian meat and chickpea stew, also known as Dizi, is cooked in clay pots where the broth is strained first and solids mashed with a goosht-koob?",
        "correct": "Abgoosht (Dizi)",
        "distractors": ["Kashk-e Bademjan", "Haleem", "Ash-e Reshteh"],
        "d": 3
    },
    {
        "q": "Which Persian eggplant dip features roasted mashed eggplant topped with fermented drained whey (kashk), crispy fried onions, and bloomed dried mint oil?",
        "correct": "Kashk-e Bademjan",
        "distractors": ["Mirza Ghassemi", "Baba Ghanoush", "Borani"],
        "d": 3
    },
    {
        "q": "Which Northern Iranian eggplant dish from the Caspian province of Gilan features smoked grilled eggplants mashed with ripe tomatoes, copious garlic, and scrambled eggs?",
        "correct": "Mirza Ghassemi",
        "distractors": ["Kashk-e Bademjan", "Shakshuka", "Zaalouk"],
        "d": 3
    },
    {
        "q": "Which national dish of Jordan features bone-in lamb cooked in a rich, tangy broth made from fermented, sun-dried goat's milk yogurt (jameed), served over rice and markook bread?",
        "correct": "Mansaf",
        "distractors": ["Maqluba", "Kabsa", "Mandi"],
        "d": 3
    },
    {
        "q": "What specific stone-hard fermented sheep or goat milk yogurt ball, reconstituted in water, creates the distinctive sour broth for Jordanian Mansaf?",
        "correct": "Jameed",
        "distractors": ["Kashk", "Labneh", "Chanklish"],
        "d": 3
    },
    {
        "q": "Which Palestinian and Levantine upside-down layered rice dish, whose name literally translates to 'upside-down', is cooked with chicken, fried cauliflower, and eggplant?",
        "correct": "Maqluba",
        "distractors": ["Mansaf", "Kabsa", "Musakhan"],
        "d": 3
    },
    {
        "q": "Which national dish of Palestine consists of roast chicken spiced with mountains of tangy red sumac and sweet caramelized onions, served atop taboon flatbread?",
        "correct": "Musakhan",
        "distractors": ["Maqluba", "Mansaf", "Shish Taouk"],
        "d": 3
    },
    {
        "q": "Which national dish of Saudi Arabia features long-grain spiced basmati rice simmered with chicken or meat, tomatoes, dried black limes, cardamom, and toasted nuts?",
        "correct": "Kabsa",
        "distractors": ["Mandi", "Majboos", "Sayadieh"],
        "d": 3
    },
    {
        "q": "Which traditional Yemeni meat and rice dish is cooked inside an underground tandoor-style pit oven, allowing roasting lamb fat to drip onto the smoking rice below?",
        "correct": "Mandi",
        "distractors": ["Kabsa", "Zurbian", "Mansaf"],
        "d": 3
    },
    {
        "q": "Which national dish of Yemen is a bubbling hot meat stew served in a basalt stone bowl (harra), topped with a thick layer of frothy whipped fenugreek paste (hulbah)?",
        "correct": "Saltah",
        "distractors": ["Fahsa", "Mandi", "Zurbian"],
        "d": 3
    },
    {
        "q": "What frothy, whipped paste made from soaked ground fenugreek seeds forms the cooling, frothy crown atop Yemeni Saltah and Fahsa stews?",
        "correct": "Hulbah",
        "distractors": ["Tahini", "Toum", "Zhug"],
        "d": 3
    },
    {
        "q": "Which ancient Levantine and Mesopotamian dish features whole wheat kernels and shredded lamb or chicken slow-beaten together for hours into a porridge consistency?",
        "correct": "Harees (Harissa / Haleem)",
        "distractors": ["Kashk", "Frikeh", "Kousa"],
        "d": 3
    },
    {
        "q": "Which cereal food made from green durum wheat that is roasted while immature and rubbed to remove hulls has a smoky, nutty flavor in Levantine cooking?",
        "correct": "Freekeh",
        "distractors": ["Bulgur", "Farro", "Couscous"],
        "d": 3
    },
    {
        "q": "Which royal Awadhi Mughal dish from Lucknow, India, features melt-in-your-mouth spiced lamb patties tenderized with raw papaya paste, smoked via dhungar?",
        "correct": "Galouti Kebab",
        "distractors": ["Kakori Kebab", "Shami Kebab", "Seekh Kebab"],
        "d": 3
    },
    {
        "q": "Which natural fruit enzyme from unripe raw papayas is classically used to tenderize meat for Awadhi royal kebabs?",
        "correct": "Papain",
        "distractors": ["Bromelain", "Actinidin", "Ficin"],
        "d": 3
    },
    {
        "q": "Which extremely tender skewered minced mutton kebab was historically invented in Awadh for an aging toothless Nawab?",
        "correct": "Kakori Kebab",
        "distractors": ["Seekh Kebab", "Chapli Kebab", "Bihari Kebab"],
        "d": 3
    },
    {
        "q": "Which flat, disc-shaped spicy minced beef patty flavored with pomegranate seeds, coriander seeds, and tomatoes originated in Peshawar, Pakistan?",
        "correct": "Chapli Kebab",
        "distractors": ["Galouti Kebab", "Shami Kebab", "Reshmi Kebab"],
        "d": 3
    },
    {
        "q": "Which royal Kashmiri multi-course feast, consisting of up to 36 elaborate courses prepared by master chefs (wazas), is called:",
        "correct": "Wazwan",
        "distractors": ["Dawat", "Thali", "Langar"],
        "d": 3
    },
    {
        "q": "Which signature dish of Kashmiri Wazwan consists of spongy mutton dumplings pounded by hand on stone slabs, poached in a fragrant saffron and curd yogurt gravy?",
        "correct": "Gushtaba",
        "distractors": ["Rista", "Tabak Maaz", "Aab Gosh"],
        "d": 3
    },
    {
        "q": "Which companion dish to Gushtaba in Kashmiri Wazwan features hand-pounded mutton meatballs simmered in a fiery red gravy colored with maval (cockscomb flower)?",
        "correct": "Rista",
        "distractors": ["Gushtaba", "Rogan Josh", "Dhanyawal Korma"],
        "d": 3
    },
    {
        "q": "Which traditional Kashmiri Wazwan dish consists of tender lamb ribs boiled with spices and then fried crisp in pure ghee until crackling?",
        "correct": "Tabak Maaz",
        "distractors": ["Gushtaba", "Rista", "Marchwangan Korma"],
        "d": 3
    },
    {
        "q": "Which slow-simmered Awadhi stew of shank meat and bone marrow, flavored with over 50 spices, is traditionally eaten for breakfast with kulcha flatbread?",
        "correct": "Nihari",
        "distractors": ["Haleem", "Paya", "Kunna"],
        "d": 3
    },
    {
        "q": "Which rich, gelatinous soup made by slow-cooking goat or sheep trotters and hooves with onions, ginger, and spices is an Indian winter staple?",
        "correct": "Paya (Trotters soup)",
        "distractors": ["Nihari", "Haleem", "Yakhni"],
        "d": 3
    },
    {
        "q": "Which Indian aromatic herb, known in Hindi as 'Kasuri Methi', is crushed between palms as the definitive finishing touch for Butter Chicken and Dal Makhani?",
        "correct": "Dried fenugreek leaves",
        "distractors": ["Dried curry leaves", "Dried coriander", "Dried mint"],
        "d": 3
    },
    {
        "q": "Which pungent resin extracted from the roots of Ferula plants is used in minute quantities in Indian vegetarian cooking to impart an onion-garlic aroma?",
        "correct": "Asafoetida (Hing)",
        "distractors": ["Kalonji", "Ajwain", "Amchur"],
        "d": 3
    },
    {
        "q": "Which small, ribbed seeds tasting strongly of thyme and caraway are commonly added to samosa pastry dough and Indian pakoras for digestion?",
        "correct": "Ajwain (Carom seeds)",
        "distractors": ["Kalonji (Nigella seeds)", "Fennel seeds", "Cumin seeds"],
        "d": 3
    },
    {
        "q": "Which black, tear-shaped seeds, often mistakenly called black cumin or onion seeds, are sprinkled atop traditional tandoori naan bread?",
        "correct": "Kalonji (Nigella sativa)",
        "distractors": ["Black sesame seeds", "Ajwain", "Chia seeds"],
        "d": 3
    }
]

if __name__ == "__main__":
    out_path = "tools/staging/ingredients_batch6.json"
    build_batch(raw_questions, out_path, batch_num=6)
