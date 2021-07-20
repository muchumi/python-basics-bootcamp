my_list = [1,2,3,4,5]
print(my_list[0]) #1
print(my_list[1]) #2
print(my_list[4]) #5

relatives = [
    "Anne",
    "Michael",
    "Miriam",
    "Joyce",
    "Mary",
    "Abigail"
]
print(relatives[3]) #Joyce

# Adding an element to a list using the append method
# Using our defined relatives above
relatives.append("Maurice")
print(relatives)

# Looping through lists
# Using the for loop
for name in relatives:
    print(name)

# Looping using the iteritems method
fruit = {
    "name": "Mango",
    "color": "yellow",
    "weight": "0.5kg",
    "species": "Kesar",
    "flavor": "sweet"
}
for key, value in fruit.items():
    print("%s --> %s" %(key, value))

