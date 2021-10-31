
# Comparing numbers
print()
print('Let\'s fiddle with some numbers. I need two integers. ')
a = int(input('Please enter the first integer. '))
b = int(input('Please enter the second integer. '))
print()

# if #1
if a > b:
    print(f'The first number, {a} is greater. ')
else:
    print(f'The first number is not greater. ')

# if #2
if a == b:
    print(f'The numbers are equal. ')
else:
    print(f'The numbers are not equal. ')

# if #3
if a < b:
    print(f'The second number, {b} is greater. ')
else:
    print(f'the second number is not greater. ')

# Greater by calculation
# import math
# if a < 0 or b < 0:
#     greater = 0.5*(abs(a+b)+abs(a-b))
#     if abs(a)==greater:
#         print(f'{a} is greater! ')
#     elif abs(greater)==b:

# greater = 0.5*((a+b)+(a-b))
# print('The greater number using the calculation is : {greater}! ')

# Comparing strings
print()
print('Hey, let\'s compare favorite animals. ')
your_animal = input('What is your favorite animal? ').lower()
# NOTE THE USE OF .lower() IN THE INPUT, RATHER THAN THE IF STATEMENTS.  I ONLY NEED IT ONCE THIS WAY.

print(f'You said: "{your_animal}". ')
if your_animal == 'goldfish':
    print('That\'s my favorite animal too! ')
else:
    print('That\'s not my favorite.  ')
print()
