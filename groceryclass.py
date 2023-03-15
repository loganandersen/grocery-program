##groceryclass
"""groceryclass"""
import random
import datetime
import os
import webbrowser
import time
import random
##List of things I need to do
#test everything
#change fruits to take account of spoilage and ammount in a fruit (ie don't make it add only one cup of cantalope, Make it add 4 cups into the fruits meals instead. Read idea archives 8/18/2020 for more info)

#NOTE A constant variable called DEFAULTLINK IS DEFINED BELOW
WEEKNAMES = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
today = datetime.date.today()
def _repr_tester(obj,method:str='__repr__'):
    """tests if an object equals the eval return of the calling of an atribute and return true or false, default method is __repr__""" 
    return obj == eval(getattr(obj,method)())
def getname(instance):
    """returns the class name of an instance"""
    return type(instance).__name__
def raise_different_name_error(obj1,obj2):
    """raises a specific TypeError for objects where names are important"""
    raise TypeError(f"Attribute 'name':{obj1.name} of {obj1!r} is Different than Attribute: 'name':{obj2.name} of {obj2!r}")
def sum_foodammounts(ammountlist):
    """takes many foodammounts and combines them into one food ammout"""
    if len(ammountlist) == 0:
        return
    elif len(ammountlist) == 1:
        return ammountlist[0]
    else:
        main = ammountlist[0]
        for i in ammountlist[1:]:
            main += i
        return main
class Link:
    """class used to store link data for ordering things online

    Keyword Arguments:
    link = a string that contains a link to a website
    portions = a number that holds the data for the portions (ie 100 grams) inside a container of food that has been linked

    Attributes:
    link : str
        an html link stored as a string
    portions : number
        the ammount of food in the link attribute
    """
    #maybe add a function specifyer that can be used in the buy function that lets you buy something on wallmart
    def __init__(self,link,portions):
        """takes a string 'link' and a number 'portions' and sets them to self.link and self.portions"""
        self.link = link
        self.portions = portions
    def __repr__(self):
        return f'{getname(self)}(link = {self.link!r},portions = {self.portions!r}'

#Constant variable DEFAULT LINK
###############################################
DEFAULTLINK= Link('https://www.walmart.com/grocery/?veh=wmt',1)
###############################################
class FoodAmmount:
    """used to store information about a food to be put in the grocery list.

    Keyword arguments:
    -----------------
    foodunit = A FoodUnit like instance used to construct the FoodClass.
    ammount = A number identifying the ammount of units of food contained.

    Attributes:
    -----------
    unit : dict
        a dictionary taken directly from the foodunit.unit argument, meant to contain the ammount for one serving, and the unit the dictionary is using.
        
        WARNING THIS DICTIONARY SHOULD NOT BE CHANGED THIS MAY BE REPLACED BY AN IMMUTABLE DICTIONARY AT SOME LATER TIME.
        
    parent : str
        A string that denotes the class.parent attribute of the foodunit argument.
        
    ammount : dict
        a dictionary containing ammount['ammount'] = the ammount argument and ammount['unit'] as the units the ammount is in.
        
        WARNING THIS DICTIONARY SHOULD NOT BE CHANGED THIS MAY BE REPLACED BY AN IMMUTABLE DICTIONARY AT SOME LATER TIME.
        
    name : str
        the name of the food item (ie bread) taken from the foodunit argument taken as a string.

    link : Link
        a Link object taken from the foodunit argument.

    group : string
        the name of the foodgroup (FDA) that the food attribute belongs to 
    """
    def __init__(self,foodunit,ammount:'number'):
        """uses a FoodUnit like object and a number to create an instance of FoodAmmount"""
        self.unit = foodunit.unit
        self.group = foodunit.group
        self.parent = foodunit.parent
        #do not change this dictionary
        self.ammount = {
            'number': ammount,
            'unit'  : foodunit.unit['unit']
        }
        self.name = foodunit.name
        self.link = foodunit.link
    def __repr__(self):
        """returns a string representation of the FoodAmount instance that if ran through eval() will return a FoodAmount Object with the same values."""
        return f'{getname(self)}(foodunit={self.parent},ammount={self.ammount["number"]})'
    def __str__(self):
        """"returns a string equal to 'self.name self.ammount["number"]["unit"]'"""
        return f"{self.name} {self.ammount['number']} {self.ammount['unit']}"
    def __add__(self,other):
        """returns a FoodAmmount object with self as the 'foodunit' argument, and with self.ammount['number'] + other.ammount['number'] as the ammount if other.name and self.name are equal otherwise raise DifferentNameError""" 
        if self.name == other.name:
            return FoodAmmount(self,self.ammount['number']+other.ammount['number'])
        else:
            raise_different_name_error(self,other)
    def buy(self):
        """"go to item link and add the item to a the wallmart grocery list""" #update this once you are done
        webbrowser.open(self.link.link,autoraise=False) 
        print(f"buy {self.ammount['number'] / self.link.portions} containers ({self.ammount['number']} {self.ammount['unit']}) of {self.name}",end=' ')
        input()



class FoodUnit:
    """Intermedite class used to make food items

    KeywordArguments:
    -----------------
    name = the name of the food item you want as a string.
    group = the foodgroup that the FoodUnit is a part of (ie grains) it should be an FDA foodgroup.
    unit = a tuple with a number as the first element and a string denoting a unit as the second argument.
    link = a Link instance that is used to to denote the link.

    Attributes:
    -----------
    name : str
        a string used to indicate the name of the food (ie: potatoes).

    group : str
        the name of the foodgroup (FDA) that the name attribute belongs to.

    unit : dict
        a dictionary where unit['number'] returns a certain ammount for an fda serving of a food item,
        and where unit['unit'] specifies a string meant to denote the units that the number is measured in.

    parent : string
        equal to repr(self)
    """
    #do not mutate
    def __init__(self,name:str,group:str,unit:tuple,link:Link=DEFAULTLINK):
        """creates attributes self.(arg name) for args name,group,link. translatess unit arg into a dictionary attribute called self.unit , and creates attribute self.parent .

        takes a name string, a group string, a unit tuple, and a link.
        sets every argument, exept for unit, to self.arg = arg . 
        for unit it makes a dictionary equal to {'number' : unit[0], 'unit' : unit[1]'}
        it also sets an an attribute called self.parent = repr(self)
        """
        self.name = name
        self.group = group
        self.link = link
        self.unit = {
            'number': unit[0],
            'unit'  : unit[1]
        }
        self.parent = repr(self)                      
    def __repr__(self):
        """creates a representation of an instance of foodunit that if ran through eval(repr(self))) would equal self"""
        return f'{getname(self)}({self.name!r},{self.group!r},{(self.unit["number"],self.unit["unit"])},{self.link!r}))'
    def __mul__(self,other:int):
        """returns a FoodAmmount instance that is has other*unit['number'] as the ammount and self as the 'foodunit' arg"""
        return (FoodAmmount(self,self.unit['number']*other))
    def to_food_amount(self):
        """returns a FoodAmmount instance with an ammount equal to self.unit['number'].
            
        equivalent to self*1
        """
        return FoodAmmount(self,self.unit['number'])
    def __eq__(self,other):
        """returns repr(self) == repr(other)"""
        return repr(self) == repr(other)
    def __hash__(self):
        """returns hash(repr(self))"""
        return hash(repr(self))
class BaseFoodGroup:
    """Used as a Base class for different Food Group classes

    Attributes : NOTE All Attributes are defined in the init_helper method rather than in __init__
    ------------
    foods :
        An iterable that is used to contain many instances that are like FoodUnit.

    groupname : str
        A string used to store the FDA foodgroup name of the foodgroup.
    """
    #immutable
    def __init__(self):
        """Raises NotImplementedError

        Must be overwritten in inherited class."""
        raise NotImplementedError
        #note, default vars are:
        #obj.foods , and obj.groupname
        #refer to init helper to create a class easily
    def __eq__(self,other):
        """Returns True if other has the same groupname and foods attributes, returns False otherwise."""
        return (self.groupname,self.foods) == (other.groupname,other.foods)
    def __hash__(self):
        """Returns the hash value of a tuple containing self.groupname and self.foods"""
        return hash((self.groupname,self.foods))
    def take_item(self):
        """returns a random item in self.foods"""
        return random.choice(tuple(self.foods))
    def __repr__(self):
        """creates a representation of an instance of foodunit that if ran through eval(repr(self)) would equal self"""
        return f'{getname(self)}({self.groupname!r},*{self.foods!r})'
    def fancy_repr(self,brackets:str='()'):
        """creates a version of repr that is expanded with whitespace and tabs

        the brackets must be changed for different objects, for instance : frozenset({set}) would need '{}' instead of '()'"""
        foodstxt = (',\n'+' '*12).join(map(repr,self.foods))
        return f'''
{getname(self)}(
    {self.groupname!r},
    *{getname(self.foods)}(
        {brackets[0]}
            {foodstxt},
        {brackets[1]}
    )
)
'''
    @staticmethod
    def init_helper(obj,groupname,foods,foodstype):
        """static method that is used to define init functions of child classes"""
        #side effects
        obj.foods = foodstype(foods)
        obj.groupname = groupname
class FoodGroup(BaseFoodGroup):
    """Class used to represent an FDA foodgroup.

    Stores the foods atr as a tuple"""
    #immutable
    def __init__(self,groupname:str,*foods):
        """Uses the init helper function to set self.groupname equal to groupname, and self.foods to tuple(foods)."""
        super().init_helper(self,groupname,foods,tuple)
    def __add__(self,other):
        """returns a FoodGroup object with its groupname equal to self.groupname and its foods equal to self.foods + other.foods, or self.foods + other. depending on the type of other.

        If self.name and other.name are equal and other is a FoodGroup like object then it returns FoodGroup(self.name,*(self.foods + other.foods)).
        Otherwise it will raise DifferentNameError (if other is a Foodgroup like object with a different name).
        If other is a tuple instead of a FoodGroup like object then It will return A FoodGroup object with self.name as its name annd self.foods + other as its foods.
        if other is anything else then it will raise TypeError.
        """
        #if the list is like a FoodGroup Object
        if hasattr(other,'foods') and hasattr(other,'groupname'):
            if self.groupname == other.groupname:
                return FoodGroup(self.groupname,*(self.foods + other.foods))
            else:
                raise_different_name_error(self,other)
        elif isinstance(other,tuple):
            return FoodGroup(self.name,*(self.foods + other))
        else:
            raise TypeError(f"Cannot add {type(other)} to FoodGroup")
class FoodGroupSet(BaseFoodGroup):
    """Used to represent an FDA foodgroup.

    Stores foods attribute as tuple
    """
    #immutable
    def __init__(self,groupname:str,*foods):
        super().init_helper(self,groupname,foods,frozenset)
    def __or__(self,other):
        """returns a FoodGroupSet object with its groupname equal to self.groupname and its foods equal to self.foods | other.foods, or self.foods | other. depending on the type of other.

        If self.name and other.name are equal and other is a FoodGroupSet like object then it returns FoodGroup(self.name,*(self.foods | other.foods)).
        Otherwise it will raise DifferentNameError (if other is a Foodgroup like object with a different name).
        If other is a frozenset instead of a FoodGroupSet like object then It will return A FoodGroupSet object with self.name as its name annd self.foods | other as its foods.
        if other is anything else then it will raise TypeError.
        """
        #if the list is like a FoodGroup Object
        if hasattr(other,'foods') and hasattr(other,'groupname'):
            if self.groupname == other.groupname:
                return FoodGroupSet(self.groupname,*(self.foods | other.foods))
            else:
                raise_different_name_error(self,other)
        elif isinstance(other,frozenset):
            return FoodGroupSet(self.name,*(self.foods | other))
        else:
            raise TypeError(f"Cannot Or {type(other)} to {getname(self)}")
    def fancy_repr(self):
        """same as BaseFoodGroups fancy_repr but with the 'brackets' keyword argument set to '{}'"""
        return super().fancy_repr('{}')
class Meal:
    """A class data for a single meal ie. "breakfast"

    Attributes:
    -----------
    name : str
        used to specify the name of the meal ie. "Dinner"

    foodlist : list
        used to store many intances of FoodAmmount 
    """
    def __init__(self,name:str,foodlist:list):
        """sets name to self.name and foodlist to self.foodlist""" 
        self.name = name
        self.foodlist = foodlist
    def fancytext(self):
        """returns a human readable version of self.foodlist nested in self.name"""
        flstring = '        '+'\n        '.join(map(str,self.foodlist)) #the fancy text needs to be fixed in a more fundemental way where it will indent it only when it is called from daymaker.makefood 
        return f'{self.name}\n{flstring}'
    def __repr__(self):
        """creates a representation of an instance of self that if ran through eval(repr(self)) would equal self"""
        return f'{getname(self)}({self.name!r},{self.foodlist!r})'
    def combine(self,other):
        """extends self.foodlist with other.foodlist. This will change self.foodlist"""
        self.foodlist.extend(other.foodlist)
    def __add__(self,other):
        return Meal(self.name, self.foodlist + other.foodlist)
def random_meal(mealmake:'MealMaker like object, or a string for name',foodgroups:dict=None):
    """uses a mealmaker object to return a random meal"""
    if type(mealmake) == str:
        name =  mealmake
    else:
        name = mealmake.name
        foodgroups = mealmake.foodgroups
    meallist = []
    for group in foodgroups:
        meallist.append(group.take_item() * foodgroups[group])
    return Meal(name,meallist)
def random_vegetables(exhaust):
    """Return A tuple of vegetable meal objects, removes items from exhaust"""
    foods = exhaust.foods
    servings = exhaust.foodsservings
    results = []
    for key in servings:
        add = []
        for j in range(servings[key]):
            add.append(foods.pop())
        results.append(Meal(key,add))
    return tuple(results)
class MealMaker:
    """A class that is used to contain the necessary information needed to create Meal instances automatically

    Attributes:
    -----------
    name : str
        a string that is used to denote the name of a certain meal (eg breakfast)

    foodgroups : dict
        a dictionary with a FoodGroup like object as the key and number used to ,
        denote how many items should be taken from the foodgroup like object

    mealfunction : function
        A function used to return a random meal by calling mealfunction(self)
    """
    def __init__(self,name:str,foodgroups:'dict({FoodGroup:servings(int),})',mealfunction=random_meal):
        """makes self.name equal to name, self.foodgroups equal to foodgroups, and self.mealfunction equal to mealfunction"""
        self.name = name
        self.foodgroups = foodgroups
        self.mealfunction = mealfunction
    def __repr__(self):
        """creates a representation of self that if ran through eval(repr(self)) would equal self"""
        return f'MealMaker({self.name},{self.foodgroups},{self.mealfunction})'
    def make_meal(self):
        """returns self.mealfunction(self)"""
        return self.mealfunction(self)
    @classmethod
    def fromtuples(cls,name,foodgroups:tuple,servings:tuple,mealfunction=random_meal):
        """Returns a MealMaker instance from two tuples where the keys for foodgroups are contained in the foodgroups tuple and the servings for the foodgroups dict are contained in the servings tuple"""  
        finaldictionary = dict({})
        for i in range(len(foodgroups)):
            finaldictionary[foodgroups[i]] = servings[i]
        return cls(name,finaldictionary)
class ExhaustableMealMaker(MealMaker):
    """A class used to generate multiple meals where it is nessesary that items are removed from a randomly generated list of foodgroup serving pairs.

    Note: for this class the foodgroups dictionary is used to stock the meallist attribute and,
    then the foodservings dictionary is used to define each of the neccesary servings for any meal
    
    Attributes :
    ------------
    self.foodservings : dict
        A dictionary with a name for a meal as a key (eg , breakfast) and then the ammount of servings needed for creating a meal
        
    self.mealfunction
        default is random_vegetables
    """
    def __init__(self,name:str,foodgroups:'dict({FoodGroup:servings(int),})',foodsservings:'dict({str("mealname"):int(ammount),})',mealfunction=random_vegetables):
        """calls the __init__ function for MealMaker on itself, sets self.foodservings equal to foodservings, and finally calls self.make_foods to give itself the self.foods attribute""" 
        super().__init__(name,foodgroups,mealfunction)
        self.foodsservings = foodsservings
        self.make_foods()
    def make_foods(self):
        """creates a list defined in self.foods that is equal to n random servings of each item in foodgroups, and then shuffles the list"""
        self.foods = []
        foodgroups = self.foodgroups
        for foodgroup in foodgroups:
            self.foods += [foodgroup.take_item().to_food_amount() for i in range(foodgroups[foodgroup])]
        random.shuffle(self.foods)
    def __repr__(self):
        """creates a representation of an instance of self that if ran through eval(repr(self)) would equal self"""
        return f'ExhaustableMealMaker({self.name!r},{self.foodgroups},{self.foodsservings},{self.mealfunction})'
class DayOfFood:
    """A class used to hold A tuple of meals

    Attributes :
    ------------
    self.meals : tuple
        A tuple of many insteances of Meal that is used to hold the foods in Day Of Food

    date :
        An object used to give the date of the day of foods, Could be a string or a datetime object.
        Might also be a relitive date like "wednesday" 
    """
    def __init__(self,meals:'tupleofmeals',date=today):
        """sets the arguments to self.(argument name)"""
        self.date = date
        self.meals = meals
    def __repr__(self):
        """creates a representation of an instance of self that if ran through eval(repr(self)) would equal self"""
        return f'{getname(self)}({self.meals!r},{self.date!r})'
    def __str__(self):
        """Creates a string with the names of the meals in foodlist meal's foodlist"""
        endstring = ""
        for meal in self.meals:
            endstring += f'{meal.name} = {meal.foodlist} '
        return endstring
    def fancystring(self):
        """returns a string that has meals.name tab nested in date and meals.foodlist nested in meals.name"""
        foodstrings = map(lambda x : getattr(x,'fancytext')(),self.meals)
        foodstring = "\n    ".join(foodstrings)
        return f'{self.date}\n    {foodstring} \n' #the fancy text needs to be fixed in a more fundemental way where it will indent it only when it is called from daymaker.makefood I think there is a wrapper module that would work fine in this situation.
    def collapsed (self):
        """returns the meals' foodlists concatinated together"""
        endlist = []
        for meal in self.meals:
            endlist.extend(meal.foodlist)
        return endlist
def make_day_of_food(foodobj,date=today):
    """Creates an instance of DayOfFood from a DayOfFoodmaker like object

    len(exhaustables) must be equal to one
    It calls the .makemeal attribute of the exhaust and the mealmake objects It combines a tuple returned by exhaustable.make_meal -
    with the individual meal instances from mealmakers
    len(foodobj.mealmakers) must be equal to len(self.exhausts's tuple) for this to work properly
    """
    mealmakers,exhaustable = foodobj.mealmakers,foodobj.exhaustables
    #unpack tuple if it is a tuple
    if type(exhaustable) == tuple:
        if len(exhaustable) == 1:
            exhaustable = exhaustable[0]
        else:
            raise Exception(f'{exhaustable} is not of size one')
    exhaustmeal = exhaustable.make_meal()
    if len(exhaustmeal) != len(mealmakers):
        raise Exception('the length of exhaust meal is not equal to the length of the mealmakers tuple, please change exhaust.makefoods function or change the ammount of mealmakers in foodobj.mealmakers')  
    g = (mealmakers[i].make_meal() + (exhaustmeal[i]) for i in range(len(exhaustmeal)))
    return DayOfFood(tuple(g),date)
class DayOfFoodMaker:
    """A class used to make many different days of food

    Attributes :
    ------------
    mealmakers : tuple
        A tuple of MealMaker like objects that will be used to make the many meals neccesary in a day

    exhaustables : tuple
        A tuple of ExhaustableMealMaker like objects that will be usssed to make the many meals necessesary in a day

    mealfunction
        A function that uses the mealmakers tuple and the exhaustables tuple to create a DayOfFood like object

    """
    def __init__(self,mealmakers:tuple,exhaustables:tuple,*,mealfunction=make_day_of_food):
        """sets the arguments taken to self.(argument name)"""
        self.mealmakers = mealmakers
        self.exhaustables = exhaustables
        self.mealfunction = mealfunction
    def __repr__(self):
        """creates a representation of an instance of self that if ran through eval(repr(self)) would equal self"""
        return f'{getname(self)}({self.mealmakers},{self.exhaustables},mealfunction={self.mealfunction}'
    def make_food(self,date=today):
        """returns the result of mealfunction(self)"""
        return self.mealfunction(self,date)
    def refresh_exhaustables(self):
        """resets the exhaustables tuple to have new foods inside of them"""
        #side effects
        for i in self.exhaustables:
            i.make_foods()
class GroceryList :
    """A class used to hold a grocery list of foods, It can be used to open links
    
    Attributes :
    -------------
    groceries : tuple
        A tuple of many food ammounts 

    Properties : 
    ------------
    grocerystr : str
        A string version of the grocery tuple 
    """ 

    def __init__(self,groceries:tuple) : 
        """Sets self.groceries to groceries""" 
        self.groceries = groceries 

    @property 
    def grocerystr(self) : 
        """A string representation of the groceries tuple"""
        return '\n'.join(map(str,self.groceries))

    def __str__(self) : 
        return self.grocerystr 

    def order(self) :
        for manyfood in self.groceries : 
            manyfood.buy() 



class ManyDaysOfFood:
    """A class used to hold and get information from many DayOfFood instances

    Instances of this classs can be used write a list of all the foods you need to buy
    and print out individual days of food

    Attributes :
    ------------
    daysoffood : tuple
        A tuple of many different days of food

    grocerylist : 
        A GroceryList object that has all of the groceries that you need to buy all of the foods in ManyDaysOfFood

    """
    def __init__(self,*daysoffood):
        self.daysoffood = daysoffood
        self.grocerylist = self.make_grocerylist()
    def make_grocerylist(self):
        """turns a ManyDaysOfFood instance into a grocery list"""
        storagelist = []
        for i in self.daysoffood:
            storagelist.extend(i.collapsed())
        #sort so that we only have to run through the method once
        storagelist.sort(key=lambda foodamnt : getattr(foodamnt,'name'))
        def deduplicate(storagelist):
            """sums the duplicates of food ammounts together"""
            endlist = []
            addlist = []
            key = storagelist[0].name
            for i in storagelist:
                if i.name == key:
                    addlist.append(i)
                else:
                    key = i.name
                    endlist.append(sum_foodammounts(addlist))
                    addlist.clear()
                    addlist.append(i)
            endlist.append(sum_foodammounts(addlist))
            endlist = list(filter(lambda x : x != None,endlist))
            endlist.sort(key = lambda foodamnt : getattr(foodamnt,'group'))
            return endlist
        final = tuple(deduplicate(storagelist))
        return GroceryList(final)
    def write_foods(self,where:"directory"=str(today)) :
        """writes all of the foods in daysoffood and creates them in a specified directory

        By default the spefified directory will be called date and will be put in where the file was ran
        Each individual day of food will be titled as (food.date).txt
        The grocery list will be called grocerylist.txt
        """
        os.mkdir(where)
        for foodday in self.daysoffood:
            with open(os.path.join(where,str(foodday.date)+'.txt'),'w') as f :
                f.write(foodday.fancystring())
        with open(os.path.join(where,'grocery_list.txt'),'w') as f:
            f.write(self.grocerylist.grocerystr)
        print(f'foods have been written to {where}')
class WeekOfFoodMaker:
    """A class who's instances can be used to create ManyDaysOfFood instances

    Attributes :
    ------------
    day : DayOfFoodMaker
        An attribute used to store the DayOfFoodMaker to be called repeatedly

    mealsmade : int
        An intiger used to count how many DaysOfFood instances have been made
    """
    def __init__(self,dayoffood:DayOfFoodMaker):
        """sets dayoffood to self.day and sets self.mealsmade to zero."""
        self.day = dayoffood
        self.mealsmade = 0
    def make_week_of_meals(self,length=-1):
        """Calls self.day.makefood length ammount of times and then puts it in an instance of ManyDaysOfFood

        The date in self.day.makefood will be determened one of two ways; 
        If length equals -1 then it will give the dates the names of the week
        Otherwise the dates will be today + 0 , today + 1, ... today + 6
        This may be changed so that you can add in a tuple of custom names some time"""
        meallist = []
        if length == -1 :
            datenames = WEEKNAMES
        else :
            datenames = tuple(map(lambda x : today + datetime.timedelta(x), range(length)))
        for i in datenames:
            self.mealsmade += 1
            meallist.append(self.day.make_food(i))
            if self.mealsmade % 7 == 0:
                self.refresh_day()
        print(f'created {len(datenames)} meals this session, total meals made: {self.mealsmade}')
        return ManyDaysOfFood(*meallist)
    def refresh_day(self):
        """refreshes the exhaustables in self.day"""
        self.day.refresh_exhaustables()
