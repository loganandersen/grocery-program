#grocerydata.py
from groceryclass import FoodGroupSet,Link,FoodUnit
fruitstr = 'fruit'
defaultfruitunit = (1,'cups') 
fruitgroup = FoodGroupSet(fruitstr,
                          FoodUnit('apple',fruitstr,defaultfruitunit,Link('https://www.walmart.com/grocery/ip/Honeycrisp-Apples-Bulk/44390950',1)),
                          FoodUnit('applesauce',fruitstr,defaultfruitunit,Link('https://www.walmart.com/grocery/ip/Great-Value-Unsweetened-Applesauce-46-oz/14122646',5.5)),
                          FoodUnit('banana',fruitstr,defaultfruitunit,Link('https://www.walmart.com/grocery/ip/Bananas-each/44390948',1)),
                          FoodUnit('cantaloupe',fruitstr,defaultfruitunit,Link('https://www.walmart.com/grocery/ip/Cantaloupe-each/44390974',4)),
                          FoodUnit('grapes',fruitstr,defaultfruitunit,Link('https://www.walmart.com/grocery/ip/Fresh-Red-Seedless-Grapes/47770140',4.5)) ,
                          FoodUnit('grapefruit',fruitstr,defaultfruitunit,Link('https://www.walmart.com/grocery/ip/Red-Grapefruit-each/51259387',1)),
                          FoodUnit('mixedfruit',fruitstr,defaultfruitunit,),
                          FoodUnit('orange',fruitstr,defaultfruitunit,Link('https://www.walmart.com/grocery/ip/Navel-Oranges-each/162577028',1)),
                          FoodUnit('mandarin orange',fruitstr,defaultfruitunit,Link('https://www.walmart.com/grocery/ip/Dole-Mandarin-Oranges-in-100-Fruit-Juice-Jarred-Oranges-23-5-Oz-Plastic-Jar/10304408',2.5)),
                          FoodUnit('peach',fruitstr,defaultfruitunit,Link('https://www.walmart.com/grocery/ip/Yellow-Peaches-each/216218066',1/2)),
                          FoodUnit('pear',fruitstr,defaultfruitunit,Link('https://www.walmart.com/grocery/ip/Anjou-Pears-Each/51259204',1)),
                          FoodUnit('pineapple',fruitstr,defaultfruitunit,Link('https://www.walmart.com/grocery/ip/Pineapple/44391200',4.5)),
                          FoodUnit('plum',fruitstr,(3,'small plums'),Link('https://www.walmart.com/grocery/ip/Black-Plums-each/44391147',1/3)),
                          FoodUnit('strawberries',fruitstr,defaultfruitunit,Link('https://www.walmart.com/grocery/ip/Fresh-Strawberries-1-lb/44391605',3)),
                          FoodUnit('watermellon',fruitstr,defaultfruitunit,Link('https://www.walmart.com/grocery/ip/Seedless-Watermelon-Each/44391101',10)),
                          FoodUnit('dried fruit',fruitstr,(1/2,'cups'),Link('https://www.walmart.com/grocery/ip/Pineapple/44391200',7)),
                    )
grainstr = 'grain'
defaultgrainunit = (1,'oz') 
graingroup = FoodGroupSet(grainstr,
                          FoodUnit('bread',grainstr,(1,'slice'),Link('https://www.walmart.com/grocery/ip/Dave-s-Killer-Bread-Powerseed-Organic-Bread-Loaf-25-oz-17-Count/51436119',15)),
                          FoodUnit('crackers',grainstr,defaultgrainunit,Link('https://www.walmart.com/grocery/ip/Triscuit-Reduced-Fat-Whole-Grain-Wheat-Crackers-11-5-oz/442691722',12)),
                          FoodUnit('oatmeal',grainstr,(1/3,'cup uncooked'),Link('https://www.walmart.com/grocery/ip/Quaker-Oats-Old-Fashioned-Oatmeal-42-oz-Canister/10312439',45)),
                          FoodUnit('popcorn',grainstr,(40,'grams'),Link('https://www.walmart.com/grocery/ip/Orville-Redenbacher-s-Original-Gourmet-Yellow-Popcorn-Kernels-45-Oz/10312395',32)),
                          FoodUnit('cereal',grainstr,(1/4,'cup'),Link('https://www.walmart.com/grocery/ip/Post-Grape-Nuts-Cereal-Original-Grape-Nuts-Breakfast-Cereal-Low-Fat-High-Fiber-Kosher-29-Ounce-1-count/35044567',28)),
                          FoodUnit('rice',grainstr,(1/2,'cup cooked'),Link('https://www.walmart.com/grocery/ip/Great-Value-Natural-Brown-Long-Grain-Rice-32-oz/10898755',20)),
                          FoodUnit('pasta',grainstr,defaultgrainunit,Link('https://www.walmart.com/grocery/ip/Great-Value-Whole-Wheat-Penne-16-oz/173699635',16)),
                    )
protienstr = 'protien'
defaultprotienunit = (1,'oz')
halfdefaultprotienunit = (1/2,'oz')
quartercupprotienunit = (1/4,'cups')
protiengroupseafood = FoodGroupSet(protienstr,
                                   FoodUnit('salmon',protienstr,defaultprotienunit),
                                   FoodUnit('tuna',protienstr,defaultprotienunit),
                                   FoodUnit('shrimp',protienstr,defaultprotienunit,Link('https://www.walmart.com/grocery/ip/Great-Vlaue-Frozen-Raw-Peeled-Deveined-Tail-On-Extra-Large-Shrimp-12-oz-26-30-count-per-lb/44391099',6)),
                                   #FoodUnit('oisters',protienstr,defaultprotienunit),
                                   #FoodUnit('trout',protienstr,defaultprotienunit),
                                   FoodUnit('herring',protienstr,defaultprotienunit,Link('https://www.walmart.com/grocery/ip/MW-Polar-Smoked-Boneless-Herring-Kipper-Snacks-3-53-Oz/19276169',3.5)),
                                   FoodUnit('anchovies',protienstr,defaultprotienunit,Link('https://www.walmart.com/grocery/ip/Crown-Prince-Flat-Anchovies-in-Olive-Oil-2-Oz/10313706',1)),
                                   FoodUnit('Atlantic mackrel',protienstr,defaultprotienunit,Link('https://www.walmart.com/grocery/ip/Pampa-Mackerel-in-Brine-15-oz-Can/21909818',8)),
                                   #FoodUnit('Pacific mackrel',protienstr,defaultprotienunit),
                            )

#DONE UNTIL HERE
#TODO Write the rest of the links
beancancups = 1.75

blackbeanlink        = Link('https://www.walmart.com/grocery/ip/Bush-s-Black-Beans-15-oz/10306800',beancancups)
kidneybeanlink       = Link('https://www.walmart.com/grocery/ip/Great-Value-Light-Red-Kidney-Beans-15-5-Oz/10534039',beancancups)
pintobeanlink        = Link('https://www.walmart.com/grocery/ip/Great-Value-Pinto-Beans-15-5-oz/10534043',beancancups)
garbanzobeanlink     = Link('https://www.walmart.com/grocery/ip/Bush-s-Garbanzo-Beans-16-oz/10306783',beancancups)
lentillink           = Link('https://www.walmart.com/grocery/ip/Great-Value-Organic-Lentils-15-oz/169639264',beancancups)
blackeyedpeaslink    = Link('https://www.walmart.com/grocery/ip/Great-Value-Black-Eyed-Peas-15-5-oz/10451547',beancancups)

protiengroup = FoodGroupSet(protienstr,
                            FoodUnit('cooked lean beef',protienstr,defaultprotienunit,Link('https://www.walmart.com/grocery/ip/Beef-Bottom-Round-Steak-Thin-0-34-2-0-lb/150293351',16)),
                            FoodUnit('cooked lean pork or ham',protienstr,defaultprotienunit,Link('https://www.walmart.com/grocery/ip/Pork-Center-Cut-Loin-Chops-Boneless-0-9-2-01-lb/37342910',20)),
                            FoodUnit('egg',protienstr,(1,'egg'),Link('https://www.walmart.com/grocery/ip/Great-Value-Extra-Large-Grade-AA-Eggs-12-Count/102842271',12)),
                            FoodUnit('cooked chicken without skin',protienstr,defaultprotienunit),
                            FoodUnit('cooked turkey without skin',protienstr,defaultprotienunit,Link('https://www.walmart.com/grocery/ip/Oscar-Mayer-Deli-Fresh-Oven-Roasted-Turkey-Breast-Sliced-Deli-Lunch-Meat-9-oz-Tray/10292749',9)),
                            FoodUnit('nuts',protienstr,halfdefaultprotienunit),
                            FoodUnit('seeds',protienstr,halfdefaultprotienunit,),
                            FoodUnit('almonds',protienstr,halfdefaultprotienunit,Link('https://www.walmart.com/grocery/ip/Great-Value-Whole-Natural-Almonds-16-oz/406969697',12)),
                            FoodUnit('pistacios',protienstr,halfdefaultprotienunit,Link('https://www.walmart.com/grocery/ip/Wonderful-Pistachios-No-Shell-Roasted-Salted-12-Oz/109915691',12)),
                            FoodUnit('peanuts',protienstr,halfdefaultprotienunit,Link('https://www.walmart.com/grocery/ip/Great-Value-Dry-Roasted-Unsalted-Peanuts-16-oz/10448400',16)),
                            FoodUnit('wallnuts',protienstr,halfdefaultprotienunit,Link('https://www.walmart.com/grocery/ip/Great-Value-Walnuts-Halves-Pieces-16-oz/124188737',32)),
                            FoodUnit('pumpkin seeds',protienstr,halfdefaultprotienunit,Link('https://www.walmart.com/grocery/ip/BIGS-Simply-Salted-Homestyle-Roast-Pumpkin-Seeds-Keto-Friendly-Snack-Low-Carb-Lifestyle-5-oz-Bag/46460974',5)),
                            FoodUnit('sunflower seeds',protienstr,halfdefaultprotienunit,Link('https://www.walmart.com/grocery/ip/Freshness-Guaranteed-Roasted-Salted-Sunflower-Kernels-11-Oz/771389438',11)),
                            FoodUnit('squash seeds',protienstr,halfdefaultprotienunit),
                            FoodUnit('cooked beans black',protienstr,quartercupprotienunit,blackbeanlink),
                            FoodUnit('cooked beans kidney',protienstr,quartercupprotienunit,kidneybeanlink),
                            FoodUnit('cooked beans pinto',protienstr,quartercupprotienunit,pintobeanlink),
                            FoodUnit('white beans',protienstr,quartercupprotienunit),
                            FoodUnit('chickpeas',protienstr,quartercupprotienunit,garbanzobeanlink),
                            FoodUnit('cowpeas',protienstr,quartercupprotienunit,garbanzobeanlink),
                            FoodUnit('lentils',protienstr,quartercupprotienunit,lentillink),
                            FoodUnit('split peas',protienstr,quartercupprotienunit,blackeyedpeaslink),
                            FoodUnit('tofu',protienstr,(2,'oz'),Link('https://www.walmart.com/grocery/ip/Nasoya-Organic-Super-Firm-Tofu-16-oz/134768563',8)),
                            FoodUnit('tempeh',protienstr,defaultprotienunit),
                    ) | protiengroupseafood
dairystr = 'dairy'
defaultdairyserving = (1,'cup')
dairygroup = FoodGroupSet(dairystr,
                          FoodUnit('milk',dairystr,defaultdairyserving,Link('https://www.walmart.com/grocery/ip/Great-Value-Fat-Free-Milk-1-Gallon-128-fl-oz/10450117',16)),
                          FoodUnit('yogurt',dairystr,defaultdairyserving,Link('https://www.walmart.com/grocery/ip/FAGE-Total-0-Milk-Fat-Greek-Strained-Yogurt-35-3-Oz/19857845',4.5)),
                          FoodUnit('Hard cheese (cheddar,motzerella,swiss,parmesan',dairystr,(1.5,'oz'),Link('https://www.walmart.com/grocery/ip/Great-Value-Sharp-Cheddar-Cheese-16-oz/10452385',10)),
                          FoodUnit('cottage cheeze',dairystr,(2,'cups'),Link('https://www.walmart.com/grocery/ip/Great-Value-1-Milkfat-Lowfat-Small-Curd-Cottage-Cheese-16-oz/10315023',1)),
                          FoodUnit('calcium fortified soy milk',dairystr,(1,'cups'),Link('https://www.walmart.com/grocery/ip/Silk-Organic-Unsweetened-Soymilk-Half-Gallon/10295041',8))
                    )
vegstring = 'vegetables'
defaultvegserv = (1,'cup')
darkvegserv = (2,'cups')
darkgreenvegetables = FoodGroupSet(vegstring,
                                   FoodUnit('broccoli',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Broccoli-Crowns-per-lb/51259378',5)),
                                   FoodUnit('cooked collard greens',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Fresh-Turnip-Greens-bunch/189452883',4)),
                                   FoodUnit('cooked mustard greens',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Fresh-Mustard-Greens-bunch/44391401',4)),
                                   FoodUnit('cooked turnip greens',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Fresh-Turnip-Greens-bunch/189452883',4)),
                                   FoodUnit('cooked kale',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Fresh-Kale-Greens-bunch/40347953',4)),
                                   FoodUnit('spinach raw',vegstring,darkvegserv),
                                   FoodUnit('romane lettuce',vegstring,darkvegserv,Link('https://www.walmart.com/grocery/ip/Romaine-Lettuce-Hearts-3-Pack/10532755',6)),
                                #   FoodUnit('watercress lettuce',vegstring,darkvegserv,Link(),
                                   FoodUnit('dark green leafy lettuce',vegstring,darkvegserv),
                                #  FoodUnit('endive',vegstring,darkvegserv),
                                #  FoodUnit('escarole',vegstring,darkvegserv),
                                   FoodUnit('bok choy',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Bok-Choy-Fresh/44391289',6)),
                            )

redvegetables = FoodGroupSet(vegstring,
                                      FoodUnit('carrots',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Whole-Carrots-1lb-bag/44391515',3)),
                                      FoodUnit('pumpkin',vegstring,defaultvegserv),
                                      FoodUnit('red pepper',vegstring,(1,'medium pepper'),Link('https://www.walmart.com/grocery/ip/Mucci-Farms-Red-Bell-Pepper-1-Each/44391581',1)),
                                      FoodUnit('tomato',vegstring,(1,'large raw'),Link('https://www.walmart.com/grocery/ip/Tomatoes-On-The-Vine-Per-lb/44390955',2)),
                                      FoodUnit('sweet potato',vegstring,(1,'large cooked'),Link('https://www.walmart.com/grocery/ip/Sweet-Potatoes-each/44390964',2)),
                                      FoodUnit('Acorn squash',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Acorn-Squash-Fresh-1-Each/44391565',3)),
                                      FoodUnit('butternut squash',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Butternut-Squash-each/44391159',5)),
                                    # FoodUnit('hubbard squash',vegstring,defaultvegserv),
                            )
beansandpeas = FoodGroupSet(vegstring,
                            FoodUnit('black beans cooked',vegstring,defaultvegserv,blackbeanlink),
                            FoodUnit('garbanzo beans cooked',vegstring,defaultvegserv,garbanzobeanlink),
                            FoodUnit('kidney beans cooked',vegstring,defaultvegserv,kidneybeanlink),
                            FoodUnit('pinto beans cooked',vegstring,defaultvegserv,pintobeanlink),
                            FoodUnit('soy beans cooked',vegstring,defaultvegserv),
                            FoodUnit('black eyed peas cooked',vegstring,defaultvegserv,blackeyedpeaslink),
                            FoodUnit('split peas cooked',vegstring,defaultvegserv,blackeyedpeaslink),
                    )
starchyvegetables = FoodGroupSet(vegstring,
                                 FoodUnit('corn',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Great-Value-Whole-Kernel-Corn-12-oz/659879040',2.5)),
                                 FoodUnit('grean peas',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Great-Value-Sweet-Peas-12-oz/443429457',2.5)),
                                 FoodUnit('white potato',vegstring,(1,'medium baked')),
                            )
othervegetables = FoodGroupSet(vegstring,
                             # FoodUnit('bean sprouts',vegstring,defaultvegserv),
                               FoodUnit('cabbage cooked',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Green-Cabbage-Head/44391042',6)),
                               FoodUnit('cauliflower',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Great-Value-Cauliflower-12-oz/242699420',4)),
                               FoodUnit('celery',vegstring,(2,'large stalks'),Link('https://www.walmart.com/grocery/ip/Celery-Stalk/51259411',4)),
                               FoodUnit('cucumber',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Cucumber-1-Each/44390954',2)),
                               FoodUnit('cooked green or wax beans',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Great-Value-Cut-Green-Beans-14-5-oz/10448318',beancancups)),
                               FoodUnit('green peppers',vegstring,(1,'large pepper'),Link('https://www.walmart.com/grocery/ip/Fresh-Green-Bell-Pepper-1-Each/44390945',1)),
                               FoodUnit('lettuce',vegstring,darkvegserv),
                               FoodUnit('mushrooms',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Fresh-Whole-Baby-Bella-Mushrooms-16-oz/22210681',2)),
                               FoodUnit('onions',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Yellow-Onions-Each/51259212',1)),
                               FoodUnit('summer squash',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Yellow-Squash-1-Each/44391040',1)),
                               FoodUnit('zucchini',vegstring,defaultvegserv,Link('https://www.walmart.com/grocery/ip/Organic-Zucchini-2-Pack/46521533',2)),
                        )
