#!/usr/bin/env python3
"""
Generate Batch 4: Iconic Regional American Foods & Sandwiches (100 questions).
30 Easy (d=1), 40 Medium (d=2), 30 Hard (d=3).
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ingredients_builder import build_batch

raw_questions = [
    # --- EASY (d=1, 30 questions) ---
    {
        "q": "Which ingredient is famously and strictly forbidden on an authentic Chicago-style hot dog?",
        "correct": "Tomato ketchup",
        "distractors": ["Yellow mustard", "Celery salt", "Sport peppers"],
        "d": 1
    },
    {
        "q": "Which type of bun is the mandatory bakery standard for an authentic Chicago-style hot dog?",
        "correct": "Poppy seed bun",
        "distractors": ["Brioche bun", "Sesame seed bun", "Potato roll"],
        "d": 1
    },
    {
        "q": "What seasoned salt blend is dusted over the top of a fully loaded Chicago hot dog as the final touch?",
        "correct": "Celery salt",
        "distractors": ["Garlic salt", "Onion salt", "Old Bay seasoning"],
        "d": 1
    },
    {
        "q": "Which processed cheese sauce is a classic topping ordered on a Philadelphia cheesesteak ('whiz wit')?",
        "correct": "Cheez Whiz",
        "distractors": ["Velveeta dip", "Nacho cheese", "Queso blanco"],
        "d": 1
    },
    {
        "q": "Which cut of thinly sliced beef is the gold standard meat used in a classic Philly cheesesteak?",
        "correct": "Ribeye",
        "distractors": ["Beef brisket", "Chuck roast", "Flank steak"],
        "d": 1
    },
    {
        "q": "Which cured beef meat is the traditional star filling of a classic Reuben sandwich?",
        "correct": "Corned beef",
        "distractors": ["Roast beef", "Bologna", "Prosciutto"],
        "d": 1
    },
    {
        "q": "Which fermented cabbage condiment is layered into a grilled Reuben sandwich?",
        "correct": "Sauerkraut",
        "distractors": ["Coleslaw", "Kimchi", "Chow chow"],
        "d": 1
    },
    {
        "q": "Which type of bread is the mandatory traditional vehicle for a classic Reuben sandwich?",
        "correct": "Rye bread",
        "distractors": ["Sourdough", "White bread", "Ciabatta"],
        "d": 1
    },
    {
        "q": "Which cheese is melted inside a classic grilled Reuben sandwich?",
        "correct": "Swiss cheese",
        "distractors": ["Cheddar cheese", "American cheese", "Provolone"],
        "d": 1
    },
    {
        "q": "Which two sauces are commonly spread on a classic Reuben sandwich?",
        "correct": "Russian or Thousand Island dressing",
        "distractors": ["Mayonnaise or Ranch", "Dijon mustard or Aioli", "Tartar or Remoulade"],
        "d": 1
    },
    {
        "q": "What three fresh ingredients comprise the letters of the beloved American 'BLT' sandwich?",
        "correct": "Bacon, lettuce, and tomato",
        "distractors": ["Beef, leek, and tarragon", "Brie, lettuce, and truffle", "Basil, lamb, and tomato"],
        "d": 1
    },
    {
        "q": "Which seafood meat is tossed in light mayonnaise and served in a buttered split-top bun in Maine?",
        "correct": "Chilled lobster meat",
        "distractors": ["Fried clams", "Smoked trout", "Crab meat"],
        "d": 1
    },
    {
        "q": "In contrast to Maine lobster rolls, how is lobster meat served in a traditional Connecticut-style lobster roll?",
        "correct": "Warm with melted butter",
        "distractors": ["Chilled with mayonnaise", "Deep-fried with tartar sauce", "Blackened with remoulade"],
        "d": 1
    },
    {
        "q": "Which three vegetables make up the foundational 'holy trinity' of Cajun and Louisiana Creole cooking?",
        "correct": "Onions, celery, and green bell peppers",
        "distractors": ["Onions, carrots, and celery", "Garlic, onions, and tomatoes", "Poblano peppers, onions, and corn"],
        "d": 1
    },
    {
        "q": "Which smoked pork sausage originating in France is an essential ingredient in Louisiana gumbo and jambalaya?",
        "correct": "Andouille sausage",
        "distractors": ["Bratwurst", "Kielbasa", "Chorizo español"],
        "d": 1
    },
    {
        "q": "What Southern staple made from ground dried sassafras leaves is stirred into gumbo as a traditional thickener and aromatic?",
        "correct": "Filé powder",
        "distractors": ["Arrowroot powder", "Gumbo herb", "Chicory root"],
        "d": 1
    },
    {
        "q": "What green mucilaginous pod vegetable is frequently used in Creole cooking to thicken gumbos?",
        "correct": "Okra",
        "distractors": ["Zucchini", "Green bean", "Chayote"],
        "d": 1
    },
    {
        "q": "What grain is cooked directly inside the seasoned meat and seafood broth of a Louisiana Jambalaya?",
        "correct": "Long-grain rice",
        "distractors": ["Cornmeal grits", "Couscous", "Pearl barley"],
        "d": 1
    },
    {
        "q": "Which Maryland seasoning blend containing celery salt, red and black pepper, and paprika is famous for steamed blue crabs?",
        "correct": "Old Bay Seasoning",
        "distractors": ["Tony Chachere's", "Slap Ya Mama", "Cavender's"],
        "d": 1
    },
    {
        "q": "Which sweet and savory spread made of grated cheddar, sweet pickled red peppers, and mayonnaise is dubbed the 'Pâté of the South'?",
        "correct": "Pimento cheese",
        "distractors": ["Beer cheese", "Queso fundido", "Pub cheese"],
        "d": 1
    },
    {
        "q": "Which two ingredients form the simple two-ingredient sauce tossed with fried chicken wings to make original Buffalo wings?",
        "correct": "Frank's RedHot sauce and melted butter",
        "distractors": ["Ketchup and brown sugar", "Sriracha and honey", "Tabasco and blue cheese"],
        "d": 1
    },
    {
        "q": "Which dipping sauce and vegetable combination is the mandatory traditional accompaniment to authentic Buffalo wings?",
        "correct": "Blue cheese dressing and celery sticks",
        "distractors": ["Ranch dressing and carrot sticks", "Honey mustard and pickles", "Barbecue sauce and coleslaw"],
        "d": 1
    },
    {
        "q": "Which warm dip consisting of shredded cooked chicken, cream cheese, hot wing sauce, and melted cheddar is a game-day staple?",
        "correct": "Buffalo chicken dip",
        "distractors": ["Spinach artichoke dip", "Seven-layer dip", "Queso dip"],
        "d": 1
    },
    {
        "q": "Which pork cut is slow-smoked over hickory or oak and shredded to make Carolina pulled pork barbecue?",
        "correct": "Pork shoulder (pork butt)",
        "distractors": ["Pork tenderloin", "Pork belly", "Pork chops"],
        "d": 1
    },
    {
        "q": "Which key condiment base distinguishes Eastern North Carolina barbecue sauce from western styles?",
        "correct": "Cider vinegar with crushed red pepper",
        "distractors": ["Tomato paste and molasses", "Yellow mustard and honey", "Mayonnaise and horseradish"],
        "d": 1
    },
    {
        "q": "Which condiment forms the bright yellow base of South Carolina-style 'Carolina Gold' barbecue sauce?",
        "correct": "Yellow mustard",
        "distractors": ["Mayonnaise", "Apple cider", "Brown sugar molasses"],
        "d": 1
    },
    {
        "q": "Which dairy condiment forms the creamy white base of Northern Alabama-style barbecue sauce popularized by Big Bob Gibson?",
        "correct": "Mayonnaise",
        "distractors": ["Sour cream", "Buttermilk", "Yogurt"],
        "d": 1
    },
    {
        "q": "Which sweet bread roll made with pineapple juice and potato flour originated in Hawaii and is popular across the US for sliders?",
        "correct": "Hawaiian sweet rolls (King's Hawaiian)",
        "distractors": ["Parker House rolls", "Brioche buns", "Amoroso rolls"],
        "d": 1
    },
    {
        "q": "What type of pickled peppers are essential to the assembly of an authentic Chicago-style hot dog?",
        "correct": "Sport peppers",
        "distractors": ["Jalapeño slices", "Pepperoncini", "Banana peppers"],
        "d": 1
    },
    {
        "q": "What vibrant relish with an artificial bright blue-green hue is a famous signature of the Chicago hot dog?",
        "correct": "Neon green sweet pickle relish",
        "distractors": ["Dill pickle relish", "Chow chow relish", "Piccalilli relish"],
        "d": 1
    },

    # --- MEDIUM (d=2, 40 questions) ---
    {
        "q": "Which pickled vegetable mixture, containing cauliflower, carrots, celery, and serrano chilies in oil, tops Chicago Italian beef sandwiches?",
        "correct": "Chicago-style Giardiniera",
        "distractors": ["Chow chow", "Kimchi", "Sauerkraut"],
        "d": 2
    },
    {
        "q": "What term describes the ordering style for an Italian beef sandwich submerged entirely into hot roast beef roasting juices (gravy)?",
        "correct": "Dipped (or Juicy)",
        "distractors": ["Wet", "Soaked", "Drowned"],
        "d": 2
    },
    {
        "q": "Which round, sesame-seeded Sicilian loaf is the mandatory vehicle for the New Orleans Muffuletta sandwich?",
        "correct": "Muffuletta bread",
        "distractors": ["Brioche bun", "Baguette", "Focaccia"],
        "d": 2
    },
    {
        "q": "Which tangy, garlicky chopped condiment spread is the definitive layer inside a New Orleans Muffuletta sandwich?",
        "correct": "Marinated green and black olive salad",
        "distractors": ["Giardiniera", "Tapenade", "Chow chow"],
        "d": 2
    },
    {
        "q": "Which three Italian cured meats are traditionally layered into a classic New Orleans Muffuletta?",
        "correct": "Genoa salami, ham, and mortadella",
        "distractors": ["Prosciutto, pancetta, and pepperoni", "Capicola, bresaola, and speck", "Bologna, pastrami, and roast beef"],
        "d": 2
    },
    {
        "q": "Which airy, crispy-crusted French bread produced in New Orleans by bakeries like Leidenheimer is essential for a Po' Boy?",
        "correct": "New Orleans French bread",
        "distractors": ["Parisian baguette", "Sourdough batard", "Ciabatta loaf"],
        "d": 2
    },
    {
        "q": "What does ordering a New Orleans Po' Boy sandwich 'dressed' mean it will be topped with?",
        "correct": "Mayonnaise, shredded lettuce, sliced tomatoes, and pickles",
        "distractors": ["Mustard, sauerkraut, and Swiss cheese", "Olive salad, provolone, and hot peppers", "Barbecue sauce, coleslaw, and onions"],
        "d": 2
    },
    {
        "q": "What flavorful liquid meat trimmings and gravy are used to make a classic New Orleans roast beef Po' Boy?",
        "correct": "Debris (gravy with braised roast beef shreds)",
        "distractors": ["Au jus broth", "Pot roast jus", "Béchamel sauce"],
        "d": 2
    },
    {
        "q": "Which open-faced hot sandwich created at the Brown Hotel in Louisville consists of sliced turkey and bacon smothered in Mornay sauce and broiled?",
        "correct": "Hot Brown",
        "distractors": ["Horseshoe sandwich", "Welsh rarebit", "Monte Cristo"],
        "d": 2
    },
    {
        "q": "Which Springfield, Illinois open-faced specialty features toasted thick bread, hamburger or meat patty, a pile of French fries, and melted cheese sauce?",
        "correct": "Horseshoe sandwich",
        "distractors": ["Hot Brown", "Gerber sandwich", "Slavic burger"],
        "d": 2
    },
    {
        "q": "Which classic American triple-decker sandwich, often held together with frilled toothpicks, layers turkey, bacon, lettuce, tomato, and mayonnaise?",
        "correct": "Club sandwich",
        "distractors": ["Dagwood sandwich", "Patty melt", "Monte Cristo"],
        "d": 2
    },
    {
        "q": "Which sandwich made with sliced ham, turkey, and Swiss cheese is dipped entirely in beaten egg batter and deep-fried, then dusted with powdered sugar?",
        "correct": "Monte Cristo sandwich",
        "distractors": ["Croque Monsieur", "Reuben", "Patty melt"],
        "d": 2
    },
    {
        "q": "Which fruit jam is traditionally served as a sweet dipping accompaniment to a deep-fried Monte Cristo sandwich?",
        "correct": "Red currant or raspberry jam",
        "distractors": ["Orange marmalade", "Grape jelly", "Apple butter"],
        "d": 2
    },
    {
        "q": "Which sandwich created in Los Angeles (at Philippe the Original or Cole's) consists of roast beef on a French roll served with a bowl of pan jus for dipping?",
        "correct": "French Dip",
        "distractors": ["Italian Beef", "Cheesesteak", "Pastrami on Rye"],
        "d": 2
    },
    {
        "q": "Which American diner hybrid sandwich combines a ground beef burger patty, melted Swiss cheese, and caramelized onions on toasted rye bread?",
        "correct": "Patty melt",
        "distractors": ["Reuben sandwich", "Frisco melt", "Chopped cheese"],
        "d": 2
    },
    {
        "q": "Which New York City bodega specialty features ground beef and onions chopped on the griddle with melted American cheese in a hero roll?",
        "correct": "Chopped Cheese",
        "distractors": ["Patty melt", "Cheesesteak", "Sloppy Joe"],
        "d": 2
    },
    {
        "q": "Which sweet and tangy ground beef mixture simmered with onions, peppers, tomato sauce, Worcestershire, and brown sugar is served on a hamburger bun?",
        "correct": "Sloppy Joe",
        "distractors": ["Manwich", "Loose meat sandwich", "Tavern sandwich"],
        "d": 2
    },
    {
        "q": "Which Midwestern sandwich, famous at Maid-Rite restaurants in Iowa, features unseasoned ground beef cooked loose without tomato binders on a steamed bun?",
        "correct": "Loose meat sandwich (Tavern sandwich)",
        "distractors": ["Sloppy Joe", "Chopped cheese", "Runza"],
        "d": 2
    },
    {
        "q": "Which Nebraska yeast dough pocket stuffed with ground beef, shredded cabbage, onions, and black pepper was brought by Volga German immigrants?",
        "correct": "Runza (Bierock)",
        "distractors": ["Pasty", "Kolache", "Kreplach"],
        "d": 2
    },
    {
        "q": "Which Cornish meat and vegetable hand pie with a crimped crust became a staple lunch for iron and copper miners in Michigan's Upper Peninsula?",
        "correct": "Pasty",
        "distractors": ["Runza", "Empanada", "Pot pie"],
        "d": 2
    },
    {
        "q": "Which classic filling is crimped inside a traditional Upper Peninsula Michigan Cornish pasty?",
        "correct": "Beef, sliced potatoes, rutabaga, and onions",
        "distractors": ["Chicken, carrots, peas, and gravy", "Pork, apples, cabbage, and cheddar", "Ground lamb, sweet potato, and corn"],
        "d": 2
    },
    {
        "q": "Which spice blend gives Nashville hot chicken its tongue-scorching heat, brushed on as a paste of rendered chicken fat, brown sugar, and chili spices?",
        "correct": "Cayenne pepper paste",
        "distractors": ["Ghost pepper extract", "Habanero puree", "Paprika and black pepper only"],
        "d": 2
    },
    {
        "q": "Which two humble items are the mandatory serving base and garnish for authentic Nashville hot chicken?",
        "correct": "Plain white sandwich bread and dill pickle slices",
        "distractors": ["Brioche bun and coleslaw", "Cornbread muffin and honey", "Waffles and maple syrup"],
        "d": 2
    },
    {
        "q": "Which Southern breakfast dish features rich white stone-ground hominy porridge topped with pan-seared shrimp, bacon drippings, and scallions?",
        "correct": "Shrimp and grits",
        "distractors": ["Grits and grillades", "Crawfish étouffée", "Lowcountry boil"],
        "d": 2
    },
    {
        "q": "What Southern dish features tender medallions of beef or pork braised in a rich Creole tomato-based roux, served over creamy grits?",
        "correct": "Grillades and grits",
        "distractors": ["Shrimp and grits", "Country fried steak", "Beef debris"],
        "d": 2
    },
    {
        "q": "Which Southern New Year's Day lucky dish consists of black-eyed peas cooked with pork (fatback or ham hock), served over rice with greens?",
        "correct": "Hoppin' John",
        "distractors": ["Red beans and rice", "Brunswick stew", "Frogmore stew"],
        "d": 2
    },
    {
        "q": "Which New Orleans Monday tradition consists of slow-simmered kidney beans cooked with the holy trinity, smoked ham hocks, and served over steamed rice?",
        "correct": "Red beans and rice",
        "distractors": ["Hoppin' John", "Jambalaya", "Crawfish Monica"],
        "d": 2
    },
    {
        "q": "What thick, spicy seafood stew made with crawfish tails smothered in a rich butter-and-flour roux and the holy trinity is called:",
        "correct": "Crawfish Étouffée",
        "distractors": ["Crawfish bisque", "Gumbo ya-ya", "Jambalaya"],
        "d": 2
    },
    {
        "q": "What type of roux provides the base for a crawfish étouffée, differing from the dark chocolate-brown roux of seafood gumbo?",
        "correct": "Blond or peanut butter-colored roux",
        "distractors": ["Black roux", "Raw white roux", "No roux (cornstarch only)"],
        "d": 2
    },
    {
        "q": "Which traditional Texas chili dish, officially the state dish of Texas, strictly forbids the inclusion of which two ingredients?",
        "correct": "Beans and tomato chunks",
        "distractors": ["Onions and garlic", "Beef and cumin", "Chili peppers and beef stock"],
        "d": 2
    },
    {
        "q": "Which fragrant spice gives Texas 'bowl of red' chili its signature earthy aromatic depth?",
        "correct": "Ground cumin (comino)",
        "distractors": ["Cinnamon", "Cardamom", "Nutmeg"],
        "d": 2
    },
    {
        "q": "Which unique Mediterranean spices give Cincinnati-style chili its recognizable Greek-influenced flavor profile?",
        "correct": "Cinnamon, allspice, and cloves",
        "distractors": ["Curry powder, turmeric, and ginger", "Saffron, rosemary, and fennel", "Star anise, Szechuan pepper, and lemongrass"],
        "d": 2
    },
    {
        "q": "What does a '5-way' order of Cincinnati chili at Skyline Chili include?",
        "correct": "Spaghetti, chili, kidney beans, chopped onions, and shredded cheddar cheese",
        "distractors": ["Hot dog, chili, mustard, onions, and cheese", "Fries, chili, bacon, jalapeños, and sour cream", "Spaghetti, chili, sour cream, guacamole, and salsa"],
        "d": 2
    },
    {
        "q": "Which Hawaiian comfort food dish consists of a bed of white rice topped with a hamburger patty, fried sunny-side-up egg, and brown gravy?",
        "correct": "Loco Moco",
        "distractors": ["Poke bowl", "Spam Musubi", "Kalua Pork plate"],
        "d": 2
    },
    {
        "q": "Which canned spiced pork product is glazed in teriyaki sauce, placed atop a block of sushi rice, and wrapped in nori in Hawaii?",
        "correct": "Spam",
        "distractors": ["Vienna sausage", "Corned beef hash", "Canned ham"],
        "d": 2
    },
    {
        "q": "Which Hawaiian traditional main dish is made by roasting a whole pig in an underground imu pit lined with banana and ti leaves?",
        "correct": "Kalua pig (Kalua pork)",
        "distractors": ["Laulau", "Pipikaula", "Char siu pork"],
        "d": 2
    },
    {
        "q": "Which Hawaiian dish features pork and salted butterfish wrapped tightly in taro leaves and ti leaves, then steamed until tender?",
        "correct": "Laulau",
        "distractors": ["Kalua pig", "Poi", "Lomi salmon"],
        "d": 2
    },
    {
        "q": "Which traditional Hawaiian side dish consists of diced salted raw salmon massaged and tossed with fresh tomatoes, sweet Maui onions, and crushed ice?",
        "correct": "Lomi-lomi salmon",
        "distractors": ["Ahi poke", "Pipikaula", "Tako poke"],
        "d": 2
    },
    {
        "q": "What ancient Hawaiian staple starch paste is made by steaming and mashing the underground corm of the taro plant with water?",
        "correct": "Poi",
        "distractors": ["Ulu mash", "Kulolo", "Haupia"],
        "d": 2
    },
    {
        "q": "Which Hawaiian sweet dessert pudding is made by simmering rich coconut milk with sugar and cornstarch or pia arrowroot until set?",
        "correct": "Haupia",
        "distractors": ["Kulolo", "K butter mochi", "Pao doce"],
        "d": 2
    },

    # --- HARD (d=3, 30 questions) ---
    {
        "q": "Which traditional Virginia and North Carolina stew, historically made with squirrel or rabbit, combines lima beans, sweet corn, tomatoes, and shredded poultry or pork?",
        "correct": "Brunswick stew",
        "distractors": ["Kentucky burgoo", "Mulligan stew", "Campfire chili"],
        "d": 3
    },
    {
        "q": "Which spicy communal Kentucky hunter's stew is slow-cooked in outdoor iron kettles with three or more meats, cabbage, potatoes, corn, and lima beans?",
        "correct": "Kentucky Burgoo",
        "distractors": ["Brunswick stew", "Booya", "Frogmore stew"],
        "d": 3
    },
    {
        "q": "Which Upper Midwestern community stew (popular in Minnesota and Wisconsin) is cooked outdoors in giant cauldrons using beef, chicken, pork, and rutabagas for church fundraisers?",
        "correct": "Booya",
        "distractors": ["Burgoo", "Brunswick stew", "Goulash"],
        "d": 3
    },
    {
        "q": "Which Pennsylvania Dutch breakfast loaf is made by boiling pork scrap trimmings with cornmeal, buckwheat flour, and spices, then sliced and fried crisp in butter?",
        "correct": "Scrapple (Pannhaas)",
        "distractors": ["Livermush", "Goetta", "Head cheese"],
        "d": 3
    },
    {
        "q": "Which Cincinnati breakfast meat loaf of German origin combines ground pork and beef with pinhead steel-cut oats, bay leaves, and rosemary, fried crisp?",
        "correct": "Goetta",
        "distractors": ["Scrapple", "Livermush", "Kishke"],
        "d": 3
    },
    {
        "q": "Which North Carolina pork loaf product features pork liver, pork head parts, cornmeal, and sage, traditionally pan-fried with grits and eggs?",
        "correct": "Livermush",
        "distractors": ["Scrapple", "Goetta", "Souse meat"],
        "d": 3
    },
    {
        "q": "Which Rhode Island clam chowder variation differs from New England and Manhattan chowders by featuring which type of broth?",
        "correct": "Clear, unthickened clam broth",
        "distractors": ["Thickened tomato puree", "Heavy saffron cream", "Beer-cheddar broth"],
        "d": 3
    },
    {
        "q": "Which Rhode Island deep-fried clam fritter made with chopped quahog clams, flour, eggs, and milk is traditionally served with tartar sauce at seaside shacks?",
        "correct": "Clam cake",
        "distractors": ["Crab cake", "Hushpuppy", "Conch fritter"],
        "d": 3
    },
    {
        "q": "Which large hard-shell Atlantic clam (Mercenaria mercenaria) native to the eastern seaboard of North America is prized for stuffed clams ('stuffies')?",
        "correct": "Quahog clam",
        "distractors": ["Geoduck", "Razor clam", "Soft-shell steamer clam"],
        "d": 3
    },
    {
        "q": "What Rhode Island baked appetizer consists of a minced quahog clam meat mixture with breadcrumbs, spicy Portuguese linguiça or chouriço, garlic, and butter baked in the clam shell?",
        "correct": "Stuffies (Stuffed quahogs)",
        "distractors": ["Clams Casino", "Oysters Rockefeller", "Clams Oreganata"],
        "d": 3
    },
    {
        "q": "Which baked clam dish created at the Little Casino in Narragansett Pier, Rhode Island, is topped with bacon, breadcrumbs, minced bell peppers, and shallots?",
        "correct": "Clams Casino",
        "distractors": ["Oysters Rockefeller", "Stuffies", "Clams Posillipo"],
        "d": 3
    },
    {
        "q": "Which iconic New Orleans baked oyster dish created at Antoine's Restaurant features oysters on the half shell topped with an intensely green, rich herb-and-butter sauce?",
        "correct": "Oysters Rockefeller",
        "distractors": ["Oysters Bienville", "Oysters Kirkpatrick", "Oysters En Brochette"],
        "d": 3
    },
    {
        "q": "Which classic New Orleans baked oyster dish created at Arnaud's features oysters baked with shrimp, minced mushrooms, shallots, white wine, and breadcrumbs?",
        "correct": "Oysters Bienville",
        "distractors": ["Oysters Rockefeller", "Oysters Casino", "Oysters Mosca"],
        "d": 3
    },
    {
        "q": "Which decadent New Orleans oyster casserole invented at Mosca's Restaurant bakes plump shucked oysters with breadcrumbs, copious garlic, olive oil, and rosemary?",
        "correct": "Oysters Mosca",
        "distractors": ["Oysters Bienville", "Oysters Rockefeller", "Oysters Vanderbilt"],
        "d": 3
    },
    {
        "q": "Which historic New Orleans dish created at Brennan's features poached eggs and Canadian bacon on toasted English muffins topped with hollandaise and a rich creamed spinach bed?",
        "correct": "Eggs Sardou",
        "distractors": ["Eggs Benedict", "Eggs Hussarde", "Eggs Neptune"],
        "d": 3
    },
    {
        "q": "Which New Orleans egg specialty served at Brennan's layers poached eggs atop rusks of Holland rusks, Marchand de Vin red wine sauce, and rich hollandaise?",
        "correct": "Eggs Hussarde",
        "distractors": ["Eggs Sardou", "Eggs Benedict", "Eggs Florentine"],
        "d": 3
    },
    {
        "q": "Which traditional New Orleans pan-roasted dish features whole peeled shrimp simmered in a cast-iron skillet with Worcestershire sauce, lemon juice, garlic, black pepper, and massive sticks of cold butter?",
        "correct": "New Orleans BBQ Shrimp",
        "distractors": ["Shrimp Creole", "Shrimp Remoulade", "Crawfish Monica"],
        "d": 3
    },
    {
        "q": "Which spicy and sweet pasta dish created for the New Orleans Jazz & Heritage Festival tossed rotini pasta with crawfish tails, heavy cream, garlic, and Creole spices?",
        "correct": "Crawfish Monica",
        "distractors": ["Crawfish Fettuccine", "Pasta Jambalaya", "Pastalaya"],
        "d": 3
    },
    {
        "q": "Which Charleston, South Carolina specialty soup created by Mayor Rhett's chef William Deas is enriched with orange crab roe, blue crab meat, cream, and dry sherry?",
        "correct": "She-crab soup",
        "distractors": ["Crab bisque", "Chesapeake chowder", "Charleston gumbo"],
        "d": 3
    },
    {
        "q": "What specific culinary ingredient gives authentic She-crab soup its subtle orange hue and richer seafood essence?",
        "correct": "Female blue crab roe",
        "distractors": ["Saffron threads", "Tomato paste", "Lobster tomalley"],
        "d": 3
    },
    {
        "q": "Which coastal Georgia and South Carolina Gullah Geechee rice dish is cooked with fresh red tomatoes, bacon fat, onions, and long-grain rice?",
        "correct": "Charleston red rice",
        "distractors": ["Jambalaya", "Dirty rice", "Hoppin' John"],
        "d": 3
    },
    {
        "q": "Which Louisiana side dish, also known as 'rice dressing', gets its dirty speckled appearance from minced chicken livers, gizzards, and ground pork cooked with the holy trinity?",
        "correct": "Dirty rice",
        "distractors": ["Cajun jambalaya", "Charleston red rice", "Calas rice"],
        "d": 3
    },
    {
        "q": "Which crisp yeast-leavened deep-fried sweet rice fritter dusted with confectioners' sugar was historically sold by African American street vendors in New Orleans?",
        "correct": "Calas",
        "distractors": ["Beignets", "Hushpuppies", "Funnel cakes"],
        "d": 3
    },
    {
        "q": "Which deep-fried round cornmeal dumpling seasoned with minced onions and buttermilk is the mandatory partner to Southern fried catfish?",
        "correct": "Hushpuppy",
        "distractors": ["Corn fritter", "Johnnycake", "Spoonbread"],
        "d": 3
    },
    {
        "q": "Which historic flatbread made from a simple batter of stone-ground Rhode Island white cap flint cornmeal, boiling water, and salt is griddled on cast iron?",
        "correct": "Johnnycake (Jonny cake)",
        "distractors": ["Hushpuppy", "Cornbread", "Spoonbread"],
        "d": 3
    },
    {
        "q": "Which delicate, soufflé-like cornmeal pudding baked in a casserole dish with butter, milk, and whipped egg whites is a Virginian Thanksgiving tradition?",
        "correct": "Spoonbread",
        "distractors": ["Johnnycake", "Corn pone", "Hasty pudding"],
        "d": 3
    },
    {
        "q": "Which traditional North Carolina side dish is made by simmering dried corn kernels that have been soaked in wood ash lye to remove hulls and germs?",
        "correct": "Hominy",
        "distractors": ["Grits", "Cornmeal mush", "Polenta"],
        "d": 3
    },
    {
        "q": "Which Pennsylvania Dutch sweet molasses crumb pie features a gooey wet-bottom filling of dark molasses topped with cinnamon-sugar flour crumbs?",
        "correct": "Shoofly pie",
        "distractors": ["Chess pie", "Sugar cream pie", "Whoopie pie"],
        "d": 3
    },
    {
        "q": "Which Southern custard pie made without fruit features a filling of butter, sugar, eggs, and a small splash of vinegar and cornmeal to balance the sweetness?",
        "correct": "Chess pie",
        "distractors": ["Shoofly pie", "Sugar cream pie", "Buttermilk pie"],
        "d": 3
    },
    {
        "q": "Which official state pie of Indiana, also known as 'Hoosier pie', is filled with a cooked custard of heavy cream, brown sugar, vanilla, and flour, dusted with nutmeg?",
        "correct": "Sugar cream pie",
        "distractors": ["Chess pie", "Shoofly pie", "Buttermilk pie"],
        "d": 3
    }
]

if __name__ == "__main__":
    out_path = "tools/staging/ingredients_batch4.json"
    build_batch(raw_questions, out_path, batch_num=4)
