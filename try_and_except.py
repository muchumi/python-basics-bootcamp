try:
    with open('logs.txt') as file:
        read_data = file.read()
except:
    print('Could not open logs.txt file')


#Example 2
while True:
    try:
        number = int(input("Enter an integer"))
        print(number, "is an integer")
    except ValueError:
        print("is not a valid integer")