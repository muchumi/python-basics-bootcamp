handle = open('message.txt', 'r')
for sentence in handle:
    print(sentence)

# Counting lines in a file
file_handle = open('message.txt')
count = 0
for cheese in file_handle:
    count = count + 1
print('Line count: ', count)

# Reading a file
file_handle2 = open('details.txt')
read_action = file_handle2.read()
print(len(read_action))
print(read_action[:22])