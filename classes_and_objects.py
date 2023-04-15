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