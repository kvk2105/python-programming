"""
This is a 
demo of Docstrings 
in python.
"""
class AnimalDocStrings:
    """
    This is Animal class.
    """
    def __init__(self, name, age):
        """
        This is class initialisation
        """
        self.name = name
        self.age = age

    def make_noise(self):
        """
        This is how animals make noise.
        """
        print ("Animal is making a noise")


# print (help(AnimalDocStrings)) # this prints the Documentation of the source code

#Annotations: Attach metat data to function parameters, return types, 
# variable etc. These are optional, and benifits developers/IDE to identify 
# potential type related errors even beofre code is run.
items: list[str] = ["apple", "google", "amazon"]

def annotation_fun(text: str) -> str:
    return "Hello", text

print(annotation_fun("Vamshi"))

