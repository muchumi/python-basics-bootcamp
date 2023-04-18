# Example One
class Dog:
    kind = 'canine'     # class variable shared by all instances

    def __init__(self, name):
        self.name = name   # instance variable unique to each instance

breedOne = Dog('Rex') 
breedTwo = Dog('Alpha')       
"""
>>> breedOne.kind       # shared by all dogs
'canine'
>>> breedTwo.kind       # shared by all dogs
'canine'
>>> breedOne.name       # unique to breedOne
'Rex'
>>> breedTwo.name       # unique to breedTwo
'Alpha'
"""

# Example Two
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = [] # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

breedOne = Dog('Rex')
breedTwo = Dog('Alpha')

"""

>>> breedOne.add_trick('roll over')
>>> breedTwo.add_trick('play dead')
>>> breedOne.tricks
['roll over']
>>> breedTwo.tricks
['play dead']

"""

"""
    If the same attribute name occurs in both an instance and in a class, then attribute look up
    prioritizes the instance.
"""

class Entertainer:
    profession = 'Actor'
    movies = 'Comedy'

personalityOne = Entertainer()
print(personalityOne.profession, personalityOne.movies)
personalityTwo = Entertainer()
personalityTwo.movies = 'Horror'
print(personalityTwo.profession, personalityTwo.movies)

"""
    Methods may call other methods by using method attributes of the self argument.
"""
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addTwice(self, x):
        self.add(x)
        self.add(x)

