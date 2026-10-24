#!/usr/bin/env python3
"""
Generate Batch 8: Desserts, Pastries, Bakes & Confections (100 questions).
30 Easy (d=1), 40 Medium (d=2), 30 Hard (d=3).
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ingredients_builder import build_batch

raw_questions = [
    # --- EASY (d=1, 30 questions) ---
    {
        "q": "Which Italian creamy dessert cheese is the mandatory star component in authentic Tiramisu?",
        "correct": "Mascarpone",
        "distractors": ["Ricotta", "Burrata", "Gorgonzola"],
        "d": 1
    },
    {
        "q": "Which beverage are the ladyfinger cookies (savoiardi) dipped into when assembling traditional Tiramisu?",
        "correct": "Espresso coffee",
        "distractors": ["Earl Grey tea", "Hot cocoa", "Red wine"],
        "d": 1
    },
    {
        "q": "Which powder is dusted across the top surface of a finished Tiramisu right before serving?",
        "correct": "Unsweetened cocoa powder",
        "distractors": ["Cinnamon powder", "Powdered sugar", "Matcha powder"],
        "d": 1
    },
    {
        "q": "What dairy cheese forms the sweet, creamy filling inside crisp Sicilian Cannoli shells?",
        "correct": "Sheep's milk ricotta",
        "distractors": ["Cream cheese", "Brie", "Mozzarella"],
        "d": 1
    },
    {
        "q": "What dessert features a rich baked egg custard topped with a brittle sheet of caramelized sugar cracked with a spoon?",
        "correct": "Crème Brûlée",
        "distractors": ["Panna Cotta", "Chocolate Mousse", "Flan"],
        "d": 1
    },
    {
        "q": "Which fruit juice is the defining flavor of authentic Florida Key lime pie?",
        "correct": "Key lime juice",
        "distractors": ["Persian lime juice", "Lemon juice", "Calamansi juice"],
        "d": 1
    },
    {
        "q": "Which canned milk product is whisked with egg yolks and lime juice to create the filling of authentic Key lime pie?",
        "correct": "Sweetened condensed milk",
        "distractors": ["Evaporated milk", "Almond milk", "Coconut milk"],
        "d": 1
    },
    {
        "q": "What crumb crust is the traditional base for classic American Key lime pie and cheesecakes?",
        "correct": "Graham cracker crust",
        "distractors": ["Oreo cookie crust", "Shortbread crust", "Puff pastry crust"],
        "d": 1
    },
    {
        "q": "Which three types of milk soak into the sponge cake of a traditional Latin American Tres Leches cake?",
        "correct": "Evaporated milk, condensed milk, and heavy cream",
        "distractors": ["Whole milk, skim milk, and almond milk", "Buttermilk, sour cream, and butter", "Coconut milk, oat milk, and soy milk"],
        "d": 1
    },
    {
        "q": "Which leavening gas-producing reaction gives traditional Red Velvet cake its tender crumb when vinegar is mixed with which powder?",
        "correct": "Baking soda",
        "distractors": ["Baking powder", "Cornstarch", "Cream of tartar"],
        "d": 1
    },
    {
        "q": "Which sweet and tangy frosting is the classic partner spread across American Red Velvet cake layers?",
        "correct": "Cream cheese frosting",
        "distractors": ["Chocolate ganache", "Royal icing", "Marshmallow fluff"],
        "d": 1
    },
    {
        "q": "Which pastry dough, made by boiling butter and water with flour and beating in eggs, expands into hollow shells for éclairs and cream puffs?",
        "correct": "Choux pastry (Pâte à choux)",
        "distractors": ["Puff pastry", "Shortcrust pastry", "Filo dough"],
        "d": 1
    },
    {
        "q": "Which finely ground nut flour is the mandatory foundation for classic French macarons?",
        "correct": "Almond flour",
        "distractors": ["Coconut flour", "Hazelnut flour", "Walnut flour"],
        "d": 1
    },
    {
        "q": "Which whipped egg white and sugar mixture forms the structural base for French macarons and pavlovas?",
        "correct": "Meringue",
        "distractors": ["Sabayon", "Custard", "Pâte sablée"],
        "d": 1
    },
    {
        "q": "Which nut is the exclusive star topping and filling of the quintessential Southern American Thanksgiving pecan pie?",
        "correct": "Pecan halves",
        "distractors": ["Walnuts", "Almonds", "Macadamias"],
        "d": 1
    },
    {
        "q": "Which viscous corn-derived syrup is blended with eggs, brown sugar, and butter to form the gooey base of classic pecan pie?",
        "correct": "Dark or light corn syrup",
        "distractors": ["Agave nectar", "Maple syrup", "Honey"],
        "d": 1
    },
    {
        "q": "Which Italian dessert translates directly to 'cooked cream' and is set with gelatin without using eggs?",
        "correct": "Panna Cotta",
        "distractors": ["Crème Brûlée", "Zabaglione", "Semifreddo"],
        "d": 1
    },
    {
        "q": "Which setting agent derived from animal collagen is traditionally used to set Italian Panna Cotta?",
        "correct": "Gelatin",
        "distractors": ["Pectin", "Agar-agar", "Cornstarch"],
        "d": 1
    },
    {
        "q": "Which Italian hot espresso and cold gelato dessert translates literally to 'drowned'?",
        "correct": "Affogato",
        "distractors": ["Macchiato", "Corretto", "Marocchino"],
        "d": 1
    },
    {
        "q": "Which sweet caramelized milk spread is sandwiched between tender cornstarch shortbread cookies to make South American Alfajores?",
        "correct": "Dulce de leche",
        "distractors": ["Nutella", "Guava paste", "Fruit jam"],
        "d": 1
    },
    {
        "q": "Which fried dough treat, piped through a star-shaped nozzle and rolled in cinnamon sugar, is served with hot thick chocolate in Spain?",
        "correct": "Churros",
        "distractors": ["Beignets", "Buñuelos", "Sopapillas"],
        "d": 1
    },
    {
        "q": "Which French upside-down caramelized apple tart is baked with pastry dough on top and inverted onto a platter when warm?",
        "correct": "Tarte Tatin",
        "distractors": ["Clafoutis", "Mille-feuille", "Tarte Bourdaloue"],
        "d": 1
    },
    {
        "q": "Which fruit is caramelized in butter and sugar as the classic star of a French Tarte Tatin?",
        "correct": "Apples",
        "distractors": ["Pears", "Plums", "Peaches"],
        "d": 1
    },
    {
        "q": "Which French dessert from the Limousin region consists of black cherries baked in a flan-like batter dusted with powdered sugar?",
        "correct": "Clafoutis",
        "distractors": ["Canelé", "Madeleine", "Financier"],
        "d": 1
    },
    {
        "q": "Which dessert, named after Russian ballerina Anna Pavlova, features a crisp meringue shell with a marshmallow center topped with whipped cream and fresh fruit?",
        "correct": "Pavlova",
        "distractors": ["Charlotte Russe", "Eton Mess", "Baked Alaska"],
        "d": 1
    },
    {
        "q": "Which British dessert created at Eton College combines crushed meringue nests, whipped cream, and sliced macerated strawberries?",
        "correct": "Eton Mess",
        "distractors": ["Trifle", "Knickerbocker Glory", "Cranachan"],
        "d": 1
    },
    {
        "q": "Which fruit puree or sliced fruit is combined with toffee and cream on a buttery biscuit base to create British Banoffee pie?",
        "correct": "Bananas",
        "distractors": ["Apples", "Strawberries", "Pineapples"],
        "d": 1
    },
    {
        "q": "Which Middle Eastern sweet pastry layers dozens of sheets of buttered phyllo dough with chopped nuts, drenched in fragrant honey syrup?",
        "correct": "Baklava",
        "distractors": ["Kadaif", "Halva", "Basbousa"],
        "d": 1
    },
    {
        "q": "Which nut is the premier signature filling in Turkish Gaziantep-style Baklava?",
        "correct": "Green pistachios",
        "distractors": ["Almonds", "Cashews", "Peanuts"],
        "d": 1
    },
    {
        "q": "Which dried fruit is the secret moisture ingredient pureed and baked into British Sticky Toffee Pudding?",
        "correct": "Medjool dates",
        "distractors": ["Figs", "Prunes", "Raisins"],
        "d": 1
    },

    # --- MEDIUM (d=2, 40 questions) ---
    {
        "q": "Which Italian whipped custard dessert is made by vigorously whisking egg yolks, sugar, and Marsala wine over simmering water?",
        "correct": "Zabaione (Zabaglione)",
        "distractors": ["Panna Cotta", "Semifreddo", "Crema pasticcera"],
        "d": 2
    },
    {
        "q": "Which fortified wine from Sicily is the classic alcohol used to flavor authentic Italian Zabaione and Tiramisu?",
        "correct": "Marsala wine",
        "distractors": ["Vin Santo", "Grappa", "Limoncello"],
        "d": 2
    },
    {
        "q": "Which twice-baked Tuscan almond cookies from Prato are traditionally dipped into sweet Vin Santo dessert wine?",
        "correct": "Cantucci (Biscotti di Prato)",
        "distractors": ["Amaretti", "Brutti ma buoni", "Ricciarelli"],
        "d": 2
    },
    {
        "q": "Which Italian soft, chewy almond cookies from Siena are made from ground almonds, sugar, egg whites, and scented with bitter almond oil?",
        "correct": "Ricciarelli di Siena",
        "distractors": ["Cantucci", "Baci di Dama", "Panforte"],
        "d": 2
    },
    {
        "q": "Which dense, chewy Tuscan Christmas fruitcake from Siena is packed with candied citrus peel, honey, nuts, and dusted with powdered sugar?",
        "correct": "Panforte di Siena",
        "distractors": ["Panettone", "Pandoro", "Colomba"],
        "d": 2
    },
    {
        "q": "Which Milanese tall, dome-shaped sweet Christmas bread is enriched with butter, eggs, candied orange peel, and raisins?",
        "correct": "Panettone",
        "distractors": ["Pandoro", "Panforte", "Babà al rum"],
        "d": 2
    },
    {
        "q": "Which Veronese star-shaped Christmas sweet yeast bread is golden with egg yolks and vanilla, served dusted solely with vanilla powdered sugar?",
        "correct": "Pandoro di Verona",
        "distractors": ["Panettone", "Colomba Pasquale", "Brioche"],
        "d": 2
    },
    {
        "q": "Which Neapolitan yeasted cake, soaked in rum-flavored citrus syrup and often filled with pastry cream, originated in Poland and France?",
        "correct": "Babà al Rum",
        "distractors": ["Sfogliatella", "Pastiera Napoletana", "Cannolo"],
        "d": 2
    },
    {
        "q": "Which ridged, shell-shaped Neapolitan pastry, meaning 'thin leaf', is made of dozens of layers of crisp pastry filled with semolina and ricotta?",
        "correct": "Sfogliatella riccia",
        "distractors": ["Sfogliatella frolla", "Cannolo", "Pastiera"],
        "d": 2
    },
    {
        "q": "Which traditional Easter tart from Naples combines cooked wheat berries (grano cotto), ricotta cheese, eggs, and orange blossom water?",
        "correct": "Pastiera Napoletana",
        "distractors": ["Sfogliatella", "Torta Caprese", "Cassata Siciliana"],
        "d": 2
    },
    {
        "q": "Which flourless Italian cake originating on the island of Capri combines dark chocolate, ground almonds or hazelnuts, butter, and eggs?",
        "correct": "Torta Caprese",
        "distractors": ["Torta Mimosa", "Torta della Nonna", "Zuccotto"],
        "d": 2
    },
    {
        "q": "Which Tuscan tart features a sweet shortcrust pastry filled with lemon-scented pastry cream and topped with whole pine nuts and powdered sugar?",
        "correct": "Torta della Nonna",
        "distractors": ["Torta Caprese", "Pastiera", "Crostata"],
        "d": 2
    },
    {
        "q": "Which French dessert, meaning 'a thousand leaves', features three crisp layers of puff pastry alternating with two layers of vanilla pastry cream?",
        "correct": "Mille-Feuille (Napoleon)",
        "distractors": ["Opera Cake", "Paris-Brest", "Saint-Honoré"],
        "d": 2
    },
    {
        "q": "Which wheel-shaped French ring of choux pastry, created to commemorate a bicycle race, is filled with praline buttercream and flaked almonds?",
        "correct": "Paris-Brest",
        "distractors": ["Saint-Honoré", "Mille-Feuille", "Religieuse"],
        "d": 2
    },
    {
        "q": "Which elaborate French cake, named after the patron saint of bakers, features a puff pastry base ringed with caramel-dipped cream puffs and Chiboust cream?",
        "correct": "Gâteau Saint-Honoré",
        "distractors": ["Paris-Brest", "Croquembouche", "Pithiviers"],
        "d": 2
    },
    {
        "q": "Which French showpiece dessert consists of a tall conical tower of choux pastry profiteroles glued together with golden spun caramel sugar?",
        "correct": "Croquembouche",
        "distractors": ["Saint-Honoré", "Religieuse", "Pièce montée"],
        "d": 2
    },
    {
        "q": "Which French choux pastry dessert consists of two stacked choux buns resembling a nun, filled with coffee or chocolate pastry cream and glazed?",
        "correct": "Religieuse",
        "distractors": ["Profiterole", "Éclair", "Paris-Brest"],
        "d": 2
    },
    {
        "q": "Which small, shell-shaped French sponge cakes from Commercy, famously immortalized by Marcel Proust, are flavored with lemon zest and melted butter?",
        "correct": "Madeleines",
        "distractors": ["Financiers", "Canelés", "Macarons"],
        "d": 2
    },
    {
        "q": "Which small French rectangular almond cakes, named because their shape resembles a gold bar, are flavored with nutty brown butter (beurre noisette)?",
        "correct": "Financiers",
        "distractors": ["Madeleines", "Canelés", "Friands"],
        "d": 2
    },
    {
        "q": "Which small French fluted cylinder pastry from Bordeaux features a dark, caramelized crunchy beeswax crust and a soft, custard-like rum-vanilla interior?",
        "correct": "Canelé de Bordeaux",
        "distractors": ["Madeleine", "Financier", "Baba au rhum"],
        "d": 2
    },
    {
        "q": "What unique substance is traditionally brushed onto copper molds along with butter to give Canelés de Bordeaux their glossy, crispy caramelized crust?",
        "correct": "Beeswax",
        "distractors": ["Carnauba wax", "Paraffin", "Cocoa butter"],
        "d": 2
    },
    {
        "q": "Which round, enclosed French puff pastry pie from Pithiviers is filled with rich frangipane almond cream and decorated with spiral score marks?",
        "correct": "Pithiviers (Galette des Rois)",
        "distractors": ["Tourte aux pommes", "Mille-feuille", "Tarte Bourdaloue"],
        "d": 2
    },
    {
        "q": "What rich, nutty filling made from equal parts almond cream and pastry cream is baked inside French Galette des Rois?",
        "correct": "Frangipane",
        "distractors": ["Crème mousseline", "Crème chantilly", "Crème diplomate"],
        "d": 2
    },
    {
        "q": "Which layered French cake features almond sponge cake (Joconde) soaked in coffee syrup, layered with ganache and coffee buttercream, topped with chocolate glaze?",
        "correct": "Opéra Cake",
        "distractors": ["Mille-Feuille", "Forêt-Noire", "Dacquoise"],
        "d": 2
    },
    {
        "q": "Which light French sponge cake made with almond flour and whipped egg whites is the essential structural cake layer in an Opéra cake?",
        "correct": "Joconde sponge (Biscuit Joconde)",
        "distractors": ["Genoise", "Chiffon cake", "Angel food cake"],
        "d": 2
    },
    {
        "q": "Which dessert features thin crêpes flambéed tableside in a sauce of caramelized sugar, fresh orange juice, orange zest, and Grand Marnier liqueur?",
        "correct": "Crêpes Suzette",
        "distractors": ["Crêpes Bretonnes", "Pancakes flambé", "Crêpes Dentelle"],
        "d": 2
    },
    {
        "q": "Which Austrian shortcrust tart from the city of Linz features a nutty ground hazelnut or almond crust spiced with cinnamon and cloves, filled with red currant jam?",
        "correct": "Linzer Torte",
        "distractors": ["Sachertorte", "Apfelstrudel", "Esterházy torte"],
        "d": 2
    },
    {
        "q": "Which famous Viennese chocolate cake created by Franz Sacher features dense chocolate cake coated with a thin layer of apricot jam and dark chocolate glaze?",
        "correct": "Sachertorte",
        "distractors": ["Linzer Torte", "Black Forest Cake", "Dobos Torte"],
        "d": 2
    },
    {
        "q": "Which fruit jam is spread between the layers and over the surface of an authentic Viennese Sachertorte before glazing?",
        "correct": "Apricot jam",
        "distractors": ["Raspberry jam", "Strawberry jam", "Orange marmalade"],
        "d": 2
    },
    {
        "q": "Which Hungarian drum-topped sponge cake features five thin sponge layers filled with chocolate buttercream, topped with a hard caramel slice crust?",
        "correct": "Dobos Torte",
        "distractors": ["Esterházy Torte", "Sachertorte", "Krémes"],
        "d": 2
    },
    {
        "q": "Which Hungarian and Austrian torte features almond meringue layers filled with spiced buttercream, decorated with a distinctive chocolate spiderweb glaze?",
        "correct": "Esterházy Torte",
        "distractors": ["Dobos Torte", "Linzer Torte", "Rigo Jancsi"],
        "d": 2
    },
    {
        "q": "Which German gateau from the Black Forest layers chocolate sponge soaked in Kirschwasser cherry brandy with sour morello cherries and whipped cream?",
        "correct": "Black Forest Cake (Schwarzwälder Kirschtorte)",
        "distractors": ["Sachertorte", "Bienenstich", "Baumkuchen"],
        "d": 2
    },
    {
        "q": "Which German yeast cake, meaning 'bee sting cake', has a baked honey-almond caramelized crunch topping and a rich vanilla custard filling?",
        "correct": "Bienenstich",
        "distractors": ["Donauwelle", "Streuselkuchen", "Stollen"],
        "d": 2
    },
    {
        "q": "Which traditional German Christmas yeast bread is studded with rum-soaked dried fruits, candied peel, and a cylinder of marzipan running through the center?",
        "correct": "Stollen (Christstollen)",
        "distractors": ["Panettone", "Bienenstich", "Lebkuchen"],
        "d": 2
    },
    {
        "q": "Which Nuremberg spiced gingerbread cookies are baked atop thin edible wafer paper discs called Oblaten, glazed with sugar or dark chocolate?",
        "correct": "Lebkuchen",
        "distractors": ["Pfeffernüsse", "Spekulatius", "Printen"],
        "d": 2
    },
    {
        "q": "Which German and Austrian rolled pastry stretches unleavened dough paper-thin before wrapping it around tart apples, rum-soaked raisins, cinnamon, and toasted breadcrumbs?",
        "correct": "Apple Strudel (Apfelstrudel)",
        "distractors": ["Topfenstrudel", "Linzer Torte", "Gugelhupf"],
        "d": 2
    },
    {
        "q": "Which layered British dessert consists of sponge cake soaked in sherry or fruit juice, fruit jam, fresh fruit, custard, and a topping of whipped cream?",
        "correct": "Traditional English Trifle",
        "distractors": ["Eton Mess", "Summer Pudding", "Bread and Butter Pudding"],
        "d": 2
    },
    {
        "q": "Which classic British summer dessert is made by lining a bowl with slices of stale white bread and filling it with stewed red berries until bread is stained crimson?",
        "correct": "Summer Pudding",
        "distractors": ["English Trifle", "Bread and Butter Pudding", "Spotted Dick"],
        "d": 2
    },
    {
        "q": "Which traditional British steamed suet pudding is studded with dried currants and raisins, commonly served hot with custard?",
        "correct": "Spotted Dick",
        "distractors": ["Plum Pudding", "Treacle Sponge", "Roly-Poly"],
        "d": 2
    },
    {
        "q": "Which British tart features a shortcrust pastry shell filled with a mixture of golden syrup, lemon juice, and fresh white breadcrumbs?",
        "correct": "Treacle Tart",
        "distractors": ["Bakewell Tart", "Manchester Tart", "Custard Tart"],
        "d": 2
    },

    # --- HARD (d=3, 30 questions) ---
    {
        "q": "Which Derbyshire English tart consists of a shortcrust pastry shell spread with jam, covered with a spongy frangipane almond paste, and flaked almonds?",
        "correct": "Bakewell Tart",
        "distractors": ["Treacle Tart", "Gypsy Tart", "Eccles Cake"],
        "d": 3
    },
    {
        "q": "Which small, round British flaky pastry cake from Lancashire is stuffed with spiced currants, butter, and brown sugar?",
        "correct": "Eccles Cake",
        "distractors": ["Chorley Cake", "Banbury Cake", "Bakewell Tart"],
        "d": 3
    },
    {
        "q": "Which historic Kentish tart features a blind-baked pastry case filled with an intensely sweet, whipped mixture of evaporated milk and dark muscovado sugar?",
        "correct": "Gypsy Tart",
        "distractors": ["Treacle Tart", "Butter Tart", "Shoofly Pie"],
        "d": 3
    },
    {
        "q": "Which quintessential Canadian pastry consists of small flaky pastry tart shells filled with butter, sugar, syrup, and eggs, often with raisins or pecans?",
        "correct": "Butter Tart",
        "distractors": ["Nanaimo Bar", "Sugar Pie", "Flapper Pie"],
        "d": 3
    },
    {
        "q": "Which no-bake Canadian layered bar originating on Vancouver Island consists of a wafer and coconut crumb base, custard-flavored buttercream, and chocolate ganache?",
        "correct": "Nanaimo Bar",
        "distractors": ["Butter Tart", "Matrimonial Cake", "Pemmican Bar"],
        "d": 3
    },
    {
        "q": "Which famous Scottish dessert features toasted pinhead oatmeal, whipped cream, heather honey, Scotch whisky, and fresh Scottish raspberries folded together?",
        "correct": "Cranachan",
        "distractors": ["Eton Mess", "Atholl Brose", "Clootie Dumpling"],
        "d": 3
    },
    {
        "q": "Which traditional Scottish spiced fruit pudding is wrapped in a floured cloth (cloot) and boiled in a pot for hours, forming a thick skin on the outside?",
        "correct": "Clootie Dumpling",
        "distractors": ["Cranachan", "Spotted Dick", "Black Bun"],
        "d": 3
    },
    {
        "q": "Which Portuguese egg tart pastry from Belém features blistered caramelized custard baked at high heat in a super-crispy laminated puff pastry crust, dusted with cinnamon?",
        "correct": "Pastel de Nata",
        "distractors": ["Queijada", "Travesseiro de Sintra", "Bola de Berlim"],
        "d": 3
    },
    {
        "q": "Which historic Portuguese sweet pillows from Sintra feature light puff pastry filled with sweet almond cream and egg yolks, dusted with granulated sugar?",
        "correct": "Travesseiros de Sintra",
        "distractors": ["Pastéis de Nata", "Pastéis de Tentúgal", "Ovos Moles"],
        "d": 3
    },
    {
        "q": "Which traditional Portuguese conventual sweet from Aveiro consists of a rich, velvety paste of egg yolks and sugar encased in delicate wafer paper shells?",
        "correct": "Ovos Moles de Aveiro",
        "distractors": ["Fios de Ovos", "Toucinho do Céu", "Papoilas"],
        "d": 3
    },
    {
        "q": "Which historic Iberian conventual dessert, meaning 'bacon from heaven', was traditionally made with pork lard, sugar syrup, egg yolks, and ground almonds?",
        "correct": "Toucinho do Céu",
        "distractors": ["Ovos Moles", "Sericaia", "Pão de Ló"],
        "d": 3
    },
    {
        "q": "Which traditional Portuguese sponge cake, dating back to the 15th century, uses only eggs, sugar, and flour, baked so the center remains creamy and gooey?",
        "correct": "Pão de Ló",
        "distractors": ["Bolo de Rolo", "Castella", "Toucinho do Céu"],
        "d": 3
    },
    {
        "q": "Which popular Japanese sponge cake from Nagasaki, adapted from Portuguese merchants in the 16th century, is sweetened with mizuame starch syrup?",
        "correct": "Castella (Kasutera)",
        "distractors": ["Pão de Ló", "Dorayaki", "Taiyaki"],
        "d": 3
    },
    {
        "q": "Which Japanese confection features two small pancake-like patties wrapped around a sweet red adzuki bean paste (anko) filling?",
        "correct": "Dorayaki",
        "distractors": ["Taiyaki", "Imagawayaki", "Dango"],
        "d": 3
    },
    {
        "q": "Which Japanese fish-shaped waffle cake, molded in the shape of a sea bream, is commonly filled with sweet red bean paste or custard?",
        "correct": "Taiyaki",
        "distractors": ["Dorayaki", "Monaka", "Manju"],
        "d": 3
    },
    {
        "q": "Which Japanese traditional confection features a sweet red bean paste filling sandwiched between two delicate, crisp mochi wafer shells?",
        "correct": "Monaka",
        "distractors": ["Daifuku", "Yokan", "Uiro"],
        "d": 3
    },
    {
        "q": "Which dense, jellied Japanese dessert block is made of red bean paste, agar-agar (kanten), and sugar, sliced into glossy rectangles?",
        "correct": "Yōkan",
        "distractors": ["Uiro", "Warabimochi", "Kuzumochi"],
        "d": 3
    },
    {
        "q": "Which jelly-like Japanese summer confection made from bracken starch (warabiko) is dipped in toasted soybean flour (kinako) and black sugar syrup (kuromitsu)?",
        "correct": "Warabimochi",
        "distractors": ["Yōkan", "Daifuku", "Botamochi"],
        "d": 3
    },
    {
        "q": "What roasted yellow soybean flour provides a nutty, peanut-like dusting over Japanese mochi and dango desserts?",
        "correct": "Kinako",
        "distractors": ["Kanten", "Matcha", "Kuromitsu"],
        "d": 3
    },
    {
        "q": "What dense, unrefined black sugar syrup from Okinawa is drizzled over Japanese shaved ice and warabimochi?",
        "correct": "Kuromitsu",
        "distractors": ["Mizuame", "Mirin", "Wasanbon"],
        "d": 3
    },
    {
        "q": "Which highly prized, fine-grained traditional Japanese sugar, made through elaborate hand-pressing processes in Shikoku, is used for luxury wasanbon sweets?",
        "correct": "Wasanbon sugar",
        "distractors": ["Kuromitsu", "Rock sugar", "Palm sugar"],
        "d": 3
    },
    {
        "q": "Which Levantine sweet cheese pastry is made with spun shredded kataifi pastry dough, mild stretchy goat or sheep cheese, soaked in orange blossom sugar syrup?",
        "correct": "Knafeh (Kanafeh)",
        "distractors": ["Baklava", "Basbousa", "Ma'amoul"],
        "d": 3
    },
    {
        "q": "Which shredded, thread-like wheat pastry dough is used to wrap Turkish and Greek desserts like Knafeh and Kataifi?",
        "correct": "Kataifi dough (Kadaif)",
        "distractors": ["Phyllo dough", "Brik dough", "Yufka"],
        "d": 3
    },
    {
        "q": "Which Middle Eastern semolina cake soaked in sweet rosewater or orange blossom syrup is garnished with an almond atop each diamond slice?",
        "correct": "Basbousa (Revani / Harissa)",
        "distractors": ["Knafeh", "Ma'amoul", "Qatayef"],
        "d": 3
    },
    {
        "q": "Which delicate Middle Eastern shortbread cookies, stamped in carved wooden molds, are filled with date paste, pistachios, or walnuts during Eid and Easter?",
        "correct": "Ma'amoul",
        "distractors": ["Basbousa", "Ghorayeba", "Barazek"],
        "d": 3
    },
    {
        "q": "Which melt-in-your-mouth Middle Eastern butter cookies, topped with a single clove or pistachio, are made simply of ghee, powdered sugar, and flour?",
        "correct": "Ghorayeba (Ghraybeh)",
        "distractors": ["Ma'amoul", "Barazek", "Halva"],
        "d": 3
    },
    {
        "q": "Which crisp Syrian cookies from Damascus are dipped on one side in toasted sesame seeds and studded on the other with crushed green pistachios?",
        "correct": "Barazek",
        "distractors": ["Ghorayeba", "Ma'amoul", "Kleicha"],
        "d": 3
    },
    {
        "q": "Which small folded Arab yeasted pancakes, stuffed with sweet cheese or spiced nuts and deep-fried, are eaten hot during the month of Ramadan?",
        "correct": "Qatayef",
        "distractors": ["Luqaimat", "Zalabiya", "Awameh"],
        "d": 3
    },
    {
        "q": "Which golden, crispy deep-fried sweet dough dumplings, drenched in date syrup or honey and sprinkled with sesame seeds, are a favorite Emirati treat?",
        "correct": "Luqaimat",
        "distractors": ["Qatayef", "Gulab Jamun", "Jalebi"],
        "d": 3
    },
    {
        "q": "Which Indian sweet consists of deep-fried reduced milk solids (khoya) dumplings soaked in a warm sugar syrup scented with rosewater and cardamom?",
        "correct": "Gulab Jamun",
        "distractors": ["Rasgulla", "Jalebi", "Rasmalai"],
        "d": 3
    }
]

if __name__ == "__main__":
    out_path = "tools/staging/ingredients_batch8.json"
    build_batch(raw_questions, out_path, batch_num=8)
