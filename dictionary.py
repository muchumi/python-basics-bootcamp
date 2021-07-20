student = {
    "name": "Wycliffe Muchumi",
    "age": 26,
    "occupation": "Software Engineer",
    "height": "6Ft"
}
print("My name is %s" %(student["name"]))

# Adding a new key and its value to a dictionary
# We just assign a value to a dictionary key
student["favorite_color"] = "blue"
print(student)

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

# Looping through a dictionary using the for loop
# Here we apply the key only
for key in fruit:
    print("%s --> %s" %(key, fruit[key]))