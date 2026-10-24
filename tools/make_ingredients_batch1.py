#!/usr/bin/env python3
"""
Generate Batch 1: Cocktails, Spirits, Mixed Drinks & Bar Beverages (100 questions).
30 Easy (d=1), 40 Medium (d=2), 30 Hard (d=3).
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ingredients_builder import build_batch

raw_questions = [
    # --- EASY (d=1, 30 questions) ---
    {
        "q": "Which primary spirit forms the base of a classic Margarita?",
        "correct": "Tequila",
        "distractors": ["Rum", "Vodka", "Gin"],
        "d": 1
    },
    {
        "q": "Which spirit is the traditional primary base of a classic Martini?",
        "correct": "Gin",
        "distractors": ["Bourbon", "Tequila", "Rum"],
        "d": 1
    },
    {
        "q": "Which fresh herb is muddled with sugar and lime in a classic Cuban Mojito?",
        "correct": "Mint",
        "distractors": ["Basil", "Cilantro", "Rosemary"],
        "d": 1
    },
    {
        "q": "Which spirit provides the alcoholic foundation for a Moscow Mule?",
        "correct": "Vodka",
        "distractors": ["Gin", "Tequila", "Bourbon"],
        "d": 1
    },
    {
        "q": "Which non-alcoholic effervescent beverage is mixed with vodka and lime juice to make a Moscow Mule?",
        "correct": "Ginger beer",
        "distractors": ["Tonic water", "Club soda", "Cola"],
        "d": 1
    },
    {
        "q": "Which liquor is traditionally used to make a classic Daiquiri along with lime juice and simple syrup?",
        "correct": "White rum",
        "distractors": ["Tequila", "Vodka", "Bourbon"],
        "d": 1
    },
    {
        "q": "Which bitter red Italian liqueur is an essential component of a classic Negroni?",
        "correct": "Campari",
        "distractors": ["Aperol", "Fernet-Branca", "Amaretto"],
        "d": 1
    },
    {
        "q": "Which type of wine is traditionally fortified and flavored with botanicals to produce sweet and dry vermouth?",
        "correct": "Grape wine",
        "distractors": ["Apple cider", "Rice wine", "Mead"],
        "d": 1
    },
    {
        "q": "Which primary spirit is combined with sweet vermouth and Angostura bitters to create a Manhattan?",
        "correct": "Rye whiskey",
        "distractors": ["White rum", "Tequila blanco", "Vodka"],
        "d": 1
    },
    {
        "q": "Which citrus juice is an essential fresh ingredient in a traditional Whiskey Sour?",
        "correct": "Lemon juice",
        "distractors": ["Grapefruit juice", "Orange juice", "Cranberry juice"],
        "d": 1
    },
    {
        "q": "Which classic brunch cocktail consists of chilled Champagne mixed with fresh orange juice?",
        "correct": "Mimosa",
        "distractors": ["Bellini", "French 75", "Kir Royale"],
        "d": 1
    },
    {
        "q": "Which fruit puree is blended with Prosecco to make a traditional Venetian Bellini?",
        "correct": "White peach puree",
        "distractors": ["Strawberry puree", "Mango puree", "Raspberry puree"],
        "d": 1
    },
    {
        "q": "Which dark soda is mixed with dark rum to prepare the registered highball cocktail known as a Dark 'n Stormy?",
        "correct": "Ginger beer",
        "distractors": ["Root beer", "Cola", "Dr Pepper"],
        "d": 1
    },
    {
        "q": "Which spirit is mixed with ginger ale and grenadine to turn a Shirley Temple into a Dirty Shirley?",
        "correct": "Vodka",
        "distractors": ["Tequila", "Scotch", "Brandy"],
        "d": 1
    },
    {
        "q": "Which botanical flavor characterizes tonic water and gives it its distinctive bitterness?",
        "correct": "Quinine",
        "distractors": ["Juniper", "Wormwood", "Anise"],
        "d": 1
    },
    {
        "q": "Which plant extract gives traditional gin its unmistakable pine-forward aroma and flavor?",
        "correct": "Juniper berries",
        "distractors": ["Coriander seeds", "Angelica root", "Orris root"],
        "d": 1
    },
    {
        "q": "Which red fruit syrup is traditionally used to sweeten cocktails like the Tequila Sunrise and Shirley Temple?",
        "correct": "Grenadine",
        "distractors": ["Orgeat", "Falernum", "Cassis"],
        "d": 1
    },
    {
        "q": "Which spirit forms the base of a classic Mint Julep served at the Kentucky Derby?",
        "correct": "Bourbon",
        "distractors": ["Vodka", "Gin", "Rum"],
        "d": 1
    },
    {
        "q": "Which fruit juice is the primary mixer combined with vodka in a classic Screwdriver?",
        "correct": "Orange juice",
        "distractors": ["Pineapple juice", "Apple juice", "Grapefruit juice"],
        "d": 1
    },
    {
        "q": "Which Mexican cocktail is traditionally made with tequila, grapefruit soda, and fresh lime juice?",
        "correct": "Paloma",
        "distractors": ["Michelada", "Margarita", "Vampiro"],
        "d": 1
    },
    {
        "q": "Which creamy Irish liqueur is made from a blend of Irish whiskey, dairy cream, and cocoa?",
        "correct": "Baileys Irish Cream",
        "distractors": ["Kahlúa", "Frangelico", "Disaronno"],
        "d": 1
    },
    {
        "q": "Which Mexican coffee liqueur is a primary ingredient in a White Russian and Black Russian?",
        "correct": "Kahlúa",
        "distractors": ["Tia Maria", "Midori", "Galliano"],
        "d": 1
    },
    {
        "q": "What dairy product is floated atop a Black Russian to transform it into a White Russian?",
        "correct": "Heavy cream",
        "distractors": ["Sour cream", "Condensed milk", "Coconut milk"],
        "d": 1
    },
    {
        "q": "Which tropical juice is blended with white rum and cream of coconut to make a classic Piña Colada?",
        "correct": "Pineapple juice",
        "distractors": ["Guava juice", "Mango juice", "Passion fruit juice"],
        "d": 1
    },
    {
        "q": "Which savoury ingredient gives a Bloody Mary its signature red color and savory vegetable base?",
        "correct": "Tomato juice",
        "distractors": ["Beet juice", "Carrot juice", "Pomegranate juice"],
        "d": 1
    },
    {
        "q": "What carbonated wine is combined with Aperol and club soda to create a classic Aperol Spritz?",
        "correct": "Prosecco",
        "distractors": ["Champagne", "Cava", "Moscato"],
        "d": 1
    },
    {
        "q": "Which fermented apple beverage serves as the alcoholic base of traditional hard cider?",
        "correct": "Fermented apple juice",
        "distractors": ["Distilled pear brandy", "Fermented honey water", "Malted barley wash"],
        "d": 1
    },
    {
        "q": "Which spirit is mixed with tomato juice, Worcestershire sauce, and spices to make a Bloody Mary?",
        "correct": "Vodka",
        "distractors": ["Gin", "Tequila", "Rum"],
        "d": 1
    },
    {
        "q": "What sweetener made from equal parts water and granulated sugar is a staple simple syrup in cocktail making?",
        "correct": "Simple syrup",
        "distractors": ["Molasses", "Agave nectar", "Corn syrup"],
        "d": 1
    },
    {
        "q": "Which citrus peel is traditionally expressed over an Old Fashioned before serving?",
        "correct": "Orange peel",
        "distractors": ["Lime peel", "Grapefruit peel", "Kumquat peel"],
        "d": 1
    },

    # --- MEDIUM (d=2, 40 questions) ---
    {
        "q": "Which almond-flavored syrup with a hint of rose or orange blossom water is a critical ingredient in a classic Mai Tai?",
        "correct": "Orgeat syrup",
        "distractors": ["Falernum", "Grenadine", "Demerara syrup"],
        "d": 2
    },
    {
        "q": "Which orange-flavored French liqueur made from Cognac and bitter orange essence is commonly used in high-end Margaritas and Sidecars?",
        "correct": "Grand Marnier",
        "distractors": ["Cointreau", "Triple Sec", "Blue Curaçao"],
        "d": 2
    },
    {
        "q": "Which aromatic spirit from France or Switzerland, traditionally flavored with wormwood and anise, is famously used to rinse the glass for a Sazerac?",
        "correct": "Absinthe",
        "distractors": ["Chartreuse", "Pastis", "Sambuca"],
        "d": 2
    },
    {
        "q": "Which type of bitters, formulated by an apothecary in New Orleans, is essential to a traditional Sazerac cocktail?",
        "correct": "Peychaud's Bitters",
        "distractors": ["Angostura Bitters", "Orange Bitters", "Walnut Bitters"],
        "d": 2
    },
    {
        "q": "What component provides the signature frothy foam atop a classic Pisco Sour or Gin Fizz?",
        "correct": "Raw egg white",
        "distractors": ["Heavy cream", "Gelatin powder", "Aquafaba"],
        "d": 2
    },
    {
        "q": "Which spirit is distilled from fermented sugarcane juice (rather than molasses) and forms the base of Brazil's national cocktail, the Caipirinha?",
        "correct": "Cachaça",
        "distractors": ["Aguardiente", "Pisco", "Mezcal"],
        "d": 2
    },
    {
        "q": "Which three ingredients are muddled and combined in equal balance to create a traditional Brazilian Caipirinha?",
        "correct": "Cachaça, lime, and sugar",
        "distractors": ["Rum, mint, and soda", "Tequila, lime, and salt", "Pisco, lemon, and egg white"],
        "d": 2
    },
    {
        "q": "Which French herbal liqueur, made by Carthusian monks using a secret blend of 130 botanicals, comes in green and yellow varieties?",
        "correct": "Chartreuse",
        "distractors": ["Bénédictine", "Strega", "Drambuie"],
        "d": 2
    },
    {
        "q": "Which cocktail made with gin, lemon juice, simple syrup, and Champagne is named after a World War I field artillery piece?",
        "correct": "French 75",
        "distractors": ["Aviation", "Corpse Reviver #2", "Sidecar"],
        "d": 2
    },
    {
        "q": "Which liqueur made from marasca cherries gives the classic Aviation cocktail its subtle cherry-pit and floral complexity?",
        "correct": "Maraschino liqueur",
        "distractors": ["Kirsch", "Cherry Heering", "Chambord"],
        "d": 2
    },
    {
        "q": "Which floral violet liqueur gives the classic Aviation cocktail its distinctive pale sky-blue or lavender tint?",
        "correct": "Crème de violette",
        "distractors": ["Parfait Amour", "Blue Curaçao", "Crème de cassis"],
        "d": 2
    },
    {
        "q": "Which blackcurrant liqueur from Burgundy is mixed with white wine to produce a traditional Kir?",
        "correct": "Crème de cassis",
        "distractors": ["Chambord", "Sloe gin", "Crème de mûre"],
        "d": 2
    },
    {
        "q": "Which fortified wine from the town of Chambéry, France, is the classic vermouth brand known for its clear, bone-dry profile?",
        "correct": "Dolin Dry Vermouth",
        "distractors": ["Martini & Rossi", "Carpano Antica", "Punt e Mes"],
        "d": 2
    },
    {
        "q": "Which rich, vanilla-forward Italian sweet vermouth is widely considered the gold standard for high-end craft Manhattans and Negronis?",
        "correct": "Carpano Antica Formula",
        "distractors": ["Cinzano Rosso", "Noilly Prat", "Lillet Blanc"],
        "d": 2
    },
    {
        "q": "Which aperitif wine from Podensac, France, made from Bordeaux grapes and macerated citrus liqueurs, is an essential ingredient in the Vesper Martini?",
        "correct": "Lillet Blanc",
        "distractors": ["Dubonnet", "Byrrh", "Cocchi Americano"],
        "d": 2
    },
    {
        "q": "Which Italian bitter liqueur infused with artichoke leaves is classified as a carciofo amaro?",
        "correct": "Cynar",
        "distractors": ["Averna", "Montenegro", "Nonino"],
        "d": 2
    },
    {
        "q": "Which hazelnut-flavored liqueur packaged in a bottle shaped like a monk with a rope belt is produced in Piedmont, Italy?",
        "correct": "Frangelico",
        "distractors": ["Disaronno", "Tuaca", "Galliano"],
        "d": 2
    },
    {
        "q": "Which Italian liqueur flavored with bitter almond apricot kernels is famously produced in Saronno?",
        "correct": "Disaronno Amaretto",
        "distractors": ["Sambuca", "Strega", "Limoncello"],
        "d": 2
    },
    {
        "q": "Which star anise-flavored Italian liqueur is often served with three toasted coffee beans called 'con la mosca'?",
        "correct": "Sambuca",
        "distractors": ["Ouzo", "Anisette", "Pastis"],
        "d": 2
    },
    {
        "q": "Which liqueur flavored with Scotch whisky, heather honey, herbs, and spices was historically associated with Prince Charles Edward Stuart?",
        "correct": "Drambuie",
        "distractors": ["Glayva", "Southern Comfort", "Yukon Jack"],
        "d": 2
    },
    {
        "q": "Which classic gin-based cocktail created in 1915 at the Raffles Hotel in Singapore includes pineapple juice, cherry liqueur, Benedictine, and lime?",
        "correct": "Singapore Sling",
        "distractors": ["Zombie", "Planter's Punch", "Suffering Bastard"],
        "d": 2
    },
    {
        "q": "Which four equal parts make up the classic prohibition-era Last Word cocktail?",
        "correct": "Gin, Green Chartreuse, Maraschino liqueur, and lime juice",
        "distractors": ["Vodka, Blue Curaçao, triple sec, and lemon juice", "Bourbon, Aperol, Amaro Nonino, and lemon juice", "Rye, sweet vermouth, Campari, and orange bitters"],
        "d": 2
    },
    {
        "q": "Which modern classic cocktail created by Sam Ross is made from equal parts bourbon, Aperol, Amaro Nonino Quintessentia, and fresh lemon juice?",
        "correct": "Paper Plane",
        "distractors": ["Penicillin", "Naked and Famous", "Toronto"],
        "d": 2
    },
    {
        "q": "Which peaty spirit is floated atop Sam Ross's famous modern cocktail, the Penicillin?",
        "correct": "Islay single malt Scotch",
        "distractors": ["Irish pot still whiskey", "Rye whiskey", "Mezcal joven"],
        "d": 2
    },
    {
        "q": "Which spicy root syrup is combined with honey syrup, blended Scotch, and lemon juice in a Penicillin cocktail?",
        "correct": "Fresh ginger syrup",
        "distractors": ["Horseradish syrup", "Cinnamon syrup", "Turmeric syrup"],
        "d": 2
    },
    {
        "q": "Which spicy, salted Mexican preparation featuring beer, lime juice, assorted sauces (like Worcestershire and hot sauce), and a chili-salt rim is called a:",
        "correct": "Michelada",
        "distractors": ["Chelada", "Chavela", "Clamato Cooler"],
        "d": 2
    },
    {
        "q": "Which savory, commercially bottled tomato beverage seasoned with clam broth is a mandatory ingredient in the Canadian Caesar cocktail?",
        "correct": "Clamato juice",
        "distractors": ["V8 vegetable juice", "Spiced marinara", "Gazpacho puree"],
        "d": 2
    },
    {
        "q": "Which fruit liqueur made from black raspberries, cognac, and Madagascan vanilla is packaged in an orb-shaped bottle with a golden crown?",
        "correct": "Chambord",
        "distractors": ["Crème de mûre", "Cherry Heering", "Bols Raspberry"],
        "d": 2
    },
    {
        "q": "Which Caribbean spiced syrup or liqueur flavored with almond, ginger, lime, and clove is a cornerstone of Tiki cocktails?",
        "correct": "Falernum",
        "distractors": ["Allspice dram", "Orgeat", "Fassionola"],
        "d": 2
    },
    {
        "q": "Which Jamaican allspice liqueur, also known as pimento dram, provides intense holiday-spice warmth to tropical and autumn drinks?",
        "correct": "Allspice dram",
        "distractors": ["Falernum", "Anisette", "Bénédictine"],
        "d": 2
    },
    {
        "q": "Which fortified wine from Andalusia, Spain, made primarily from Palomino grapes, is used in classic cocktail cobblers and bamboo cocktails?",
        "correct": "Sherry",
        "distractors": ["Port", "Madeira", "Marsala"],
        "d": 2
    },
    {
        "q": "Which fortified wine produced on the Portuguese islands in the Atlantic Ocean is heated repeatedly during the aging process (estufagem)?",
        "correct": "Madeira",
        "distractors": ["Sherry", "Port", "Marsala"],
        "d": 2
    },
    {
        "q": "What unique plant root provides the bittering agent in gentian-based aperitifs like Suze and Salers?",
        "correct": "Yellow gentian root",
        "distractors": ["Licorice root", "Chicory root", "Dandelion root"],
        "d": 2
    },
    {
        "q": "Which grape brandy produced in the Cognac and Gascony regions of France is distilled in column stills and known as Armagnac?",
        "correct": "Armagnac",
        "distractors": ["Calvados", "Grappa", "Pisco"],
        "d": 2
    },
    {
        "q": "Which apple and pear brandy produced in the Normandy region of France is aged in oak casks?",
        "correct": "Calvados",
        "distractors": ["Kirschwasser", "Poire Williams", "Marc de Bourgogne"],
        "d": 2
    },
    {
        "q": "Which clear fruit brandy made from double distillation of fermented morello cherries originated in the Black Forest of Germany?",
        "correct": "Kirschwasser",
        "distractors": ["Slivovitz", "Maraschino", "Framboise"],
        "d": 2
    },
    {
        "q": "Which pomace brandy made from distilling the skins, pulp, and seeds left over from winemaking is famous in Northern Italy?",
        "correct": "Grappa",
        "distractors": ["Ouzo", "Metaxa", "Tsipouro"],
        "d": 2
    },
    {
        "q": "Which ingredient gives the classic Grasshopper cocktail its bright green color and fresh minty flavor?",
        "correct": "Green crème de menthe",
        "distractors": ["Midori", "Absinthe", "Chartreuse verte"],
        "d": 2
    },
    {
        "q": "Which Japanese melon liqueur with a vibrant neon green color is the key flavor component in a Japanese Slipper and Midori Sour?",
        "correct": "Midori",
        "distractors": ["Pisang Ambon", "Green curaçao", "Crème de banane"],
        "d": 2
    },
    {
        "q": "What aromatic tree bark from Trinidad and Tobago is the foundational bittering agent in Angostura bitters?",
        "correct": "Gentian root and aromatic herbs",
        "distractors": ["Cinchona bark", "Birch bark", "Sassafras root"],
        "d": 2
    },

    # --- HARD (d=3, 30 questions) ---
    {
        "q": "Which bitter aperitif wine created by Giulio Cocchi in 1891 is flavored with cinchona bark, gentian, and citrus peel?",
        "correct": "Cocchi Americano",
        "distractors": ["Cardamaro", "Lillet Rosé", "Bonal Gentiane-Quina"],
        "d": 3
    },
    {
        "q": "Which herbal amaro from Bormio in the Italian Alps is flavored with alpine herbs, peppermint, gentian, and wormwood?",
        "correct": "Braulio",
        "distractors": ["Fernet-Branca", "Amaro Lucano", "Amaro Montenegro"],
        "d": 3
    },
    {
        "q": "Which botanical amaro from Bologna, named after Princess Elena of Montenegro, features coriander, sweet orange peel, and oregano?",
        "correct": "Amaro Montenegro",
        "distractors": ["Ramazzotti", "Vecchia Romagna", "Averna"],
        "d": 3
    },
    {
        "q": "Which intensely minty, dark Italian fernet is world-famous in San Francisco and Argentina, where it is commonly mixed with Coca-Cola?",
        "correct": "Fernet-Branca",
        "distractors": ["Fernet del Frate", "Branca Menta", "Meletti"],
        "d": 3
    },
    {
        "q": "Which rare, highly prized bitter vermouth produced in Turin features cinchona bark and is named 'Punt e Mes' (meaning 'a point and a half')?",
        "correct": "Punt e Mes",
        "distractors": ["Carpano Bianco", "Cocchi Vermouth di Torino", "Vermouth del Professore"],
        "d": 3
    },
    {
        "q": "Which French fortified wine aperitif produced in Roussillon uses mistelle combined with cinchona bark and gentian?",
        "correct": "Byrrh",
        "distractors": ["Dubonnet Rouge", "Saint-Raphaël", "Lillet Rouge"],
        "d": 3
    },
    {
        "q": "Which wine-based Italian amaro is infused specifically with cardoon (wild artichoke) and blessed thistle?",
        "correct": "Cardamaro",
        "distractors": ["Cynar", "Nardini Rabarbaro", "Zucca Rabarbaro"],
        "d": 3
    },
    {
        "q": "Which Chinese spirit distilled from fermented sorghum, wheat, or barley is categorized as having 'sauce aroma' or 'strong aroma'?",
        "correct": "Baijiu",
        "distractors": ["Soju", "Shochu", "Huangjiu"],
        "d": 3
    },
    {
        "q": "Which Korean distilled beverage is traditionally made from fermented rice, but modern commercial versions often use sweet potatoes or tapioca?",
        "correct": "Soju",
        "distractors": ["Makgeolli", "Cheongju", "Baekseju"],
        "d": 3
    },
    {
        "q": "Which Japanese distilled beverage is commonly made from barley (mugi), sweet potatoes (imo), or rice (kome) using koji mold for saccharification?",
        "correct": "Shochu",
        "distractors": ["Sake", "Awamori", "Mirin"],
        "d": 3
    },
    {
        "q": "Which unique Okinawan distilled spirit is made exclusively from fermented long-grain Thai indica rice inoculated with black koji mold?",
        "correct": "Awamori",
        "distractors": ["Hon-mirin", "Sake junmai", "Shochu soba"],
        "d": 3
    },
    {
        "q": "Which sweet rice wine containing approximately 14% alcohol is primarily used in Japanese glazes, marinades, and teriyaki sauce?",
        "correct": "Mirin",
        "distractors": ["Cooking sake", "Rice vinegar", "Shaoxing wine"],
        "d": 3
    },
    {
        "q": "Which traditional fermented Chinese rice wine from Zhejiang province is aged in earthenware jars and widely used in Chinese braises and marinades?",
        "correct": "Shaoxing wine",
        "distractors": ["Mijiu", "Baijiu", "Choya umeshu"],
        "d": 3
    },
    {
        "q": "Which Japanese liqueur is made by steeping green, unripe Japanese ume plums in shochu or neutral alcohol and rock sugar?",
        "correct": "Umeshu",
        "distractors": ["Yuzushu", "Midori", "Sakura liqueur"],
        "d": 3
    },
    {
        "q": "Which aniseed-flavored national spirit of Greece turns milky white (the ouzo effect) when water or ice is added due to the louche effect?",
        "correct": "Ouzo",
        "distractors": ["Tsikoudia", "Raki", "Metaxa"],
        "d": 3
    },
    {
        "q": "Which resinous Greek wine has been flavored with Aleppo pine tree sap for over two thousand years?",
        "correct": "Retsina",
        "distractors": ["Assyrtiko", "Agiorgitiko", "Mavrodaphne"],
        "d": 3
    },
    {
        "q": "Which Turkish anise-flavored distilled spirit made from twice-distilled grapes is traditionally known as 'lion's milk' (aslan sütü)?",
        "correct": "Rakı",
        "distractors": ["Arak", "Pastis", "Mastika"],
        "d": 3
    },
    {
        "q": "Which Levantine clear anise-flavored spirit is traditionally distilled from fermented grapes and green aniseeds, and consumed with mezze?",
        "correct": "Arak",
        "distractors": ["Ouzo", "Chacha", "Boukha"],
        "d": 3
    },
    {
        "q": "Which Tunisian eau-de-vie is distilled from fermented Mediterranean figs?",
        "correct": "Boukha",
        "distractors": ["Mahia", "Grappa", "Thibarine"],
        "d": 3
    },
    {
        "q": "Which traditional Moroccan distilled spirit, historically produced by Jewish communities, is flavored with anise and distilled from figs or dates?",
        "correct": "Mahia",
        "distractors": ["Boukha", "Cedratine", "Arak"],
        "d": 3
    },
    {
        "q": "Which fermented dairy drink originating in the Caucasus Mountains is made using symbiotic grain-like colonies of yeasts and lactic acid bacteria?",
        "correct": "Kefir",
        "distractors": ["Kombucha", "Kumis", "Ayran"],
        "d": 3
    },
    {
        "q": "Which Central Asian fermented alcoholic beverage is traditionally produced from mare's milk?",
        "correct": "Kumis",
        "distractors": ["Kefir", "Doogh", "Chal"],
        "d": 3
    },
    {
        "q": "Which Turkish and Persian refreshing cold beverage is made by whisking plain yogurt with chilled water, salt, and sometimes dried mint?",
        "correct": "Ayran",
        "distractors": ["Lassi", "Chaas", "Borhani"],
        "d": 3
    },
    {
        "q": "Which Indian spiced yogurt beverage, often seasoned with roasted cumin, black salt, and coriander, is known in Gujarat and Rajasthan as:",
        "correct": "Chaas",
        "distractors": ["Mango Lassi", "Thandai", "Jal-jeera"],
        "d": 3
    },
    {
        "q": "Which traditional festival beverage prepared during Holi in Northern India is made from milk, almonds, fennel seeds, watermelon seeds, rose petals, and cannabis (bhang)?",
        "correct": "Thandai",
        "distractors": ["Lassi", "Kahwa", "Falooda"],
        "d": 3
    },
    {
        "q": "Which Taiwanese tea-based beverage invented in Taichung in the 1980s features chewy pearls made from cassava root starch?",
        "correct": "Boba bubble tea",
        "distractors": ["Teh tarik", "Chai masala", "Matcha latte"],
        "d": 3
    },
    {
        "q": "Which South American herbal infusion made from the dried leaves of Ilex paraguariensis is traditionally sipped through a metal straw called a bombilla?",
        "correct": "Yerba mate",
        "distractors": ["Guayusa", "Rooibos", "Lapacho"],
        "d": 3
    },
    {
        "q": "Which South African caffeine-free herbal infusion is harvested exclusively from the Aspalathus linearis plant in the Cederberg mountains?",
        "correct": "Rooibos",
        "distractors": ["Honeybush", "Hibiscus", "Moringa"],
        "d": 3
    },
    {
        "q": "Which fermented Russian soft drink with negligible alcohol is traditionally brewed from stale black or rye sourdough bread, sugar, and raisins?",
        "correct": "Kvass",
        "distractors": ["Kompot", "Sbiten", "Medovukha"],
        "d": 3
    },
    {
        "q": "Which historic Slavic hot winter beverage is brewed by simmering water or wine with honey, jam, and aromatic spices such as ginger, clove, and cinnamon?",
        "correct": "Sbiten",
        "distractors": ["Kvass", "Glögg", "Mors"],
        "d": 3
    }
]

if __name__ == "__main__":
    out_path = "tools/staging/ingredients_batch1.json"
    build_batch(raw_questions, out_path, batch_num=1)
