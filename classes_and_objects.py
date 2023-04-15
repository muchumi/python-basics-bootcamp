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
