# print("Hello, pyhton", 4.5,"Hello, hi",sep="|")

# #accept input from user
# name = input('Name: ')
# age = input('Age: ')
# print ('Hello',  name, 'Your age is',  age)

#operators
# x=12
# y=9
# result = x+y
# print (result)


# hello ='heLLO WorLd'
# print (hello.count('orL'))

import random

def get_choices():
    player_choice = input("Eter a choice(ROck, Paper, Sciccors).!")
    machine_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(machine_choices)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

# choices = get_choices()
# print (choices)

def check_win(player, computer):
    print(f"you chose {player} and computer chose {computer}")
    if player == computer:
        return "Its a tie..!"

# print (check_win("Rock", "Paper"))

# Enums:
from enum import Enum
class State(Enum):
    ACTIVE = 1
    INACTIVE = 0

# print (State.ACTIVE.value)
# print (list(State))
# print (len(State))


#Lists : mutable collection of items
fruits = ["apple", "banana", "mango"]
fruits += ["grapes", "chico"]
# print (f"fruits:  {fruits}")
# fruits.remove("grapes")
# print (f"fruits:  {fruits}")
# print (fruits.pop())
# print (len(fruits))
# fruits.insert(2, "water melon")
# fruits.sort()
# print (f"fruits:  {fruits}")
# print (fruits[2])
# fruits_copy = fruits[:]
# print(f"fruits_copy: {fruits_copy}")

#Tuples : Immutable collection of items
names = ("ram", "sita", "hanuman")
# print(names.index("sita"))
# print (names[2])

# print(sorted(names))

#Dictionary - key-value pairs
dog = {'name':'john', 'age':8, 'color':'brown'}
# print ("dog: ", dog)
# print (dog['name'])
# print (dog.get('color', 'green'))

# print (dog.pop('age')) # returns the corresponding item and remove that from dict
# dog.popitem() #removes always the last item
# print(dog)
# del dog['name']
# dog['food'] = 'meat'
# print (dog)
# dog_copy = dog.copy()
# print (dog_copy)


#Sets : superset > , subset <, & intersection, | union
set1 = {"item1", "item2", "item3"}
set2 = {"item1", 'item4'}
result = set1 - set2
# print (result)

#Functions
# def hello(age, name = " friend"):
#     print ("Hello, ", name, " your age is: ", age)
#     return "Hello ", name, age

# print (hello(8, "Vamshi"))

#Scope of variable
# def test():
#     print (age)

# age = 8
# test()

#Nested functions
# def talk(phrase):
#     def say(word):
#         print (word)
    
#     for word in phrase.split(' '):
#         say(word)
# talk('I love india. Welcome to Python')


#non local variable
def count():
    count = 10
    def increment():        
        nonlocal count
        count = count + 1
        # print (count)
    increment()

count()


# Objects
#Everything in python are objects and majorly immutable

#loops
count = 5
while count > 0:
    count -= 1
    # print (count)

items = [1,2,3,4,5,6]
# for item in items:
for item in range(4):
    print (item)

#To print the index along with item
for index, item in enumerate(items):
    print (index, item)


