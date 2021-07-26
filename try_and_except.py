try:
    with open('logs.txt') as file:
        read_data = file.read()
except:
    print('Could not open logs.txt file')