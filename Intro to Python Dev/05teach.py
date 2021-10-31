import math
print()
pct = int(input(
    'Enter your grade percent and I\'ll tell you your letter grade. \n(Ex: 70. It has to be a number between 1 and 100, \nrepresenting your percent score in the class.)\nYour Percent:  '))
check = False
# check input value for error
while check == False:
    if -1 < pct < 101:
        check = True
    else:
        pct = int(input(
            'There must have been some mistake. \nPlease enter a number between 1 and 100. '))
print()

# assign a letter grade
if pct >= 90:
    letter = 'A'
elif 80 <= pct < 90:
    letter = 'B'
elif 70 <= pct < 80:
    letter = 'C'
elif 60 <= pct < 70:
    letter = 'D'
else:
    letter = 'F'

# calculate whether the grade is '+' or '-'
plus_minus = (pct % 10)

if plus_minus >= 7:
    sign = '+'
elif plus_minus < 3:
    sign = '-'
else:
    sign = ''

# handle the +/- and some grammar
if letter in ('A', 'F'):
    article = 'an'
    if letter == 'A' and sign != '+':
        letter = letter+sign
    else:
        exit
else:
    article = 'a'
    letter = letter+sign

# print the results
print(f'You earned {article} {letter}.')

if pct >= 70:
    print('You pass the course! ')
else:
    print('I\'m sorry. You didn\'t pass the course.  Please enroll again.')
    print('Never quit until you get the result you want. You can do it!')
print()
