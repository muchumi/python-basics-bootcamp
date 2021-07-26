for i in range(1, 11):
    print(i)


friends = ['Katu', 'Kelvin', 'Edwin', 'Melka']
for friend in friends:
    print('Happy Birthday: ',friend)
print('I am done with the wishes!')

# Finding the largest number
largest_number_so_far = 0
print('Largest number as per now is: ', largest_number_so_far)
for num in [12, 45, 56, 190, 673, 94, 87]:
    if num > largest_number_so_far:
        largest_number_so_far = num
    print('Largest number is: ', largest_number_so_far)
print('We already found ', largest_number_so_far, ' as the largest number')



# for loops are referred to as definite loops since they execute an exact number of times