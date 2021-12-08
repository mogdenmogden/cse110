import math

# functions to calcualte area
# square


def compute_area_square(value):
    value = float(value)
    square = value**2
    return square
# rectangle


def compute_area_rectangle(long_side, short_side):
    long_side = float(long_side)
    short_side = float(short_side)
    rectangle = long_side*short_side
    return rectangle
# circle


def compute_area_circle(radius):
    radius = float(radius)
    circle = (radius**2)*math.pi
    return circle


# loop to ask the shape
shape_chosen = ''
print('Let\'s calculate the area of some shapes! ')
print(
    'You may choose one of the following: \n[1] square \n[2] rectangle\n[3] circle \nType "quit" to stop. ')

while shape_chosen != "quit":
    shape_chosen = input('Which shape will you choose? ')
    if shape_chosen == 'quit':
        pass
    elif shape_chosen == '1':
        print('Great! Let\'s calculate the area of a square. ')
        side_sq = input('Enter the length (cm) of a side of a square: ')
        print(
            f'The area of your square is: {compute_area_square(side_sq):.2f} square centimeters! ')
        print()
    elif shape_chosen == '2':
        print('You want to calculate the area of a rectangle. ')
        r1 = input('How long is the long side of your rectangle (cm)? ')
        r2 = input('How long is the short side of your rectangle (cm)? ')
        print(
            f'The area of your rectangle is: {compute_area_rectangle(r1,r2):.2f} square centimeters. How exciting! ')
        print()
    elif shape_chosen == '3':
        print('Yes! A circle\'s area. \nLet\'s go! ')
        rad = input('What is the radius of your FAVORITE circle (cm)? ')
        print(
            f'The area of your circle is: {compute_area_circle(rad):.2f} square centimeters.  ')
        print('Can you feel the excitement in here?  Maybe it\'s just me. ')
        print()
    else:
        print('That isn\'t one of our shapes')
        print(
            'You may choose one of the following: \n[1] square \n[2] rectangle\n[3] circle \nType "quit" to stop. ')


print('\nOK. Bye.\n\n')
# print('I\'ll bet you could see this coming...\nLet\'s calculate the area of a circle. ')
