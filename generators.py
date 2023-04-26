"""
    Generators are a simple and powerful tool for creating iterators.They are written like regular
    functions but use the yield statement to return data.With generators, the __iter__() and __next__() methods are 
    created automatically.
"""

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for item in reverse('Software'):
    print(item)



