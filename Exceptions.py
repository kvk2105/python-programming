#Exceptions

try:
    raise Exception('An Error.!') # Explicitly user can raise and throw exception
    #result = 2 / 0    # code can throw exception
except ZeroDivisionError as error:
    print("Can not divide by zero")
    print(error)
except Exception as error:
    print (error)
else:
    print("can do division w/o issue")
finally:    
    result = 1

print(result)

class DogNotFoundException(Exception):
    pass

try:
    raise DogNotFoundException("Dog not found..!")
except DogNotFoundException as error:
    print(error)
finally:
    print ("Dog not found finally")
