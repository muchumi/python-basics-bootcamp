x = 5
if x == 5:
    print('Equals 5')
if x > 4:
    print('Greater than 4')
if x >= 5:
    print('Greater than or equals 5')
if x < 6:
    print('Less than 6')
if x <= 5:
    print('Less than or equals 5')
if x != 6:
    print('Not equal 6')


# Multiway conditional statements
# Grading program
averageMarks = eval(input('Enter your average marks: '))
if averageMarks >=80 and averageMarks <= 100:
    print('Your Grade is A')
elif averageMarks >= 70 and averageMarks <= 79:
    print('Your Grade is B+')
elif averageMarks >= 60 and averageMarks <= 69:
    print('Your Grade is B')
elif averageMarks >= 55 and averageMarks <= 59:
    print('Your Grade is B-')
elif averageMarks >= 45 and averageMarks <= 54:
    print('Your Grade is C')
elif averageMarks >= 40 and averageMarks <= 44:
    print('Your Grade is C-')
elif averageMarks >= 35 and averageMarks <= 39:
    print('Your Grade is D+')
elif averageMarks >= 30 and averageMarks <= 34:
    print('Your Grade is D')
elif averageMarks >= 25 and averageMarks <= 29:
    print('Your Grade is D-')
elif averageMarks >= 20 and averageMarks <= 24:
    print('Your Grade is E')
else:
    print('Fail')