#!/usr/bin/python3
#grocerylistv3.py
from groceryclass import MealMaker,ExhaustableMealMaker,DayOfFoodMaker,WeekOfFoodMaker,today
from grocerydata import othervegetables,starchyvegetables,beansandpeas,redvegetables,darkgreenvegetables
from grocerydata import fruitgroup,graingroup,protiengroup,dairygroup,protiengroupseafood
from time import time
import pickle 
version = 'v3'
#This program was based on the myplate.gov, Before using it you should enter the reccomended servings for your caloric needs in the below dictionaries  
#the default values are for the 3200 calorie diet as I am a very active and large person  

#define the servings tuples here
#it should have a foodgroup like object as the key and the servings for the foodgroup as servings you need for the meal
#fruits are represented by cups, I will probably change this to represent them with half cups because that is the default base for fruit servings according to myplate.

breakfastservings = {
                        fruitgroup :   2,
                        graingroup :   4,
                        protiengroup : 5,
                        dairygroup :   2,
                    }
dinnerservings = {
                    fruitgroup :          1,
                    graingroup :          6,
                    protiengroupseafood : 2,
                    dairygroup :          1,
                }
#the veggiegroupservings variable represents the servings for a week.
#the veggiedayservings variable represents the ammount of vegetables you want in one day for breakfast lunch and dinner.

veggiegroupservings = {
                         othervegetables :     7,
                         starchyvegetables :   8,
                         beansandpeas :        3,
                         redvegetables :       8,
                         darkgreenvegetables : 3,
                      }
veggiedayservings = {
                        'breakfast' : 2,
                        'dinner' :    2,
                    } 
#Mealmakers are defined here, and then they will use methods within them to generate the meals

breakfastmaker = MealMaker('breakfast',breakfastservings)
dinnermaker = MealMaker('dinner',dinnerservings)
veggiemaker = ExhaustableMealMaker('vegetables',veggiegroupservings,veggiedayservings)

daymaker = DayOfFoodMaker((breakfastmaker,dinnermaker),(veggiemaker,))

weekmaker = WeekOfFoodMaker(daymaker)
weekofmeals = weekmaker.make_week_of_meals()

folder = f'meal_plan/{str(today)}_{str(round(time()))}_{version}'
import sys 
weekofmeals.write_foods(folder)
with open(folder+"/weekofmeals.pkl",'wb') as f : 
    pickle.dump(weekofmeals,f) 
weekofmeals.grocerylist.order() 
