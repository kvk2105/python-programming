from lib import Animal  #Able to import Animal, because, __init__.py file was placed in 
                        #the directory where Animal.py was located. Placing __init__.py 
                        # makes the whole folder as package of modules to be imported

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print (f"{self.name} says Woof..!!")        

dog1 = Dog('Buddy', 8)
dog2 = Dog('Tommy', 5)
print(dog1.name)
print(dog2.age)
dog1.bark()
dog2.bark()

dog1.walk()

from math import sqrt
print (sqrt(9))