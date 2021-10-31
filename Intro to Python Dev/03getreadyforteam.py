import math

print(math.pi)

print('Let\'s calculate the area of a square.')
squareside = float(input('What is the length of the side of the square? '))
squarearea = squareside*squareside
print('The area of your square is '+str(squarearea))
print()

print('Now, let\'s calculate the area of a rectangle. ')
rectlong = float(input('How long is the long side of the rectangle? '))
rectshort = float(input('How long is the short side? '))
rectanglearea = rectlong*rectshort
print('The area of your rectangle is ' + str(rectanglearea))
print()

print('Now, the area of a circle... ')
circle = float(input('What is the radius of your circle? '))
circlearea = 3.14159*(circle**2)
print('The area of your circle is '+str(circlearea)+'\n')
print()
circlearea = math.pi*(circle**2)
print('The area of your circle is '+str(circlearea)+'\n')
print(str(circle))
print(str(circle*circle))
print(str(circle*circle*3.14159))

# calculate areas and volumes of a square, cube, circle, and sphere based on a single input

print('I want to calculate the area of a square and circle, \nand the volumes of a cube and sphere using a number you give me. ')
master_variable = float(
    input('Enter any value in centimeters (cm). '))
meters = master_variable/100
square = pow(master_variable, 2)
cube = pow(master_variable, 3)
circle = math.pi*square
sphere = (4/3)*math.pi*(master_variable**3)

m_square = pow(meters, 2)
m_cube = pow(meters, 3)
m_circle = math.pi*m_square
m_sphere = (4/3)*math.pi*(meters**3)

print('Based on your input,')
print('The area of a square is '+str(square) +
      ' square cm, or '+str(m_square)+' square meters.')
print('The volume of a cube is '+str(cube) +
      ' cubic centimeters, or '+str(m_cube)+' cubic meters.')
print('The area of a circle is '+str(circle) +
      ' square cm, or '+str(m_circle)+' square meters.')
print('The volume of a sphere is '+str(sphere) +
      ' cubic centimeters, or '+str(m_sphere)+' cubic meters.')
