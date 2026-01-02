#Lambda
double_it = lambda a : a * 2
print(double_it(4))


#map()
items = [1,2,3,4,5]
def double_func(a):
    return a * 2

double = lambda a : a * 2

result = map(double, items)
print (list(result))

result = map(lambda b: b * 2, items) 
print (list(result))

#filter()
def filter_fun(a):
    return a % 2 == 0

result = filter(filter_fun, items) 
print (list(result))

result = filter(lambda a : a % 2 != 0, items) 
print (list(result))

# reduce()
from functools import reduce
expenses = [('travel',100), ('food',80)]
result = reduce (lambda a, b : a[1] + b[1], expenses)
print (result)

#Recursion
def factorial(n):
    if n==1: return 1    
    return n * factorial(n-1)

print ("factorial: ", factorial(4))

#decorators : used for caching, test performance, logging, verify permissions
import datetime
def logtime(func):
    def wrapper():
        print(datetime.datetime.now())
        value = func()
        print(datetime.datetime.now())
        return value
    return wrapper

@logtime
def decorator_demo():
    print ("Hello")

print("Decorator demo..! ")
decorator_demo()

#List compressions
items = [1,2,3,4,5]
items_power_2 = []
for n in items:
    items_power_2.append(n**2)
print("powers using for iteration")
print(items_power_2)    

items_power_2 = [n**2 for n in items]
print("powers using list compression")
print(items_power_2)    

items_power_2 = map(lambda n:n**2, items)
print("powers using map - lambda")
print(list(items_power_2))    