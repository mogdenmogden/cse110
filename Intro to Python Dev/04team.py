# file: teach04_sample.py
# author: Matt Ogden
# purpose: calculate the velocity of a falling object using the formula
# v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
# where c = 1/2 p A C
# see the variable definitions below

import math
import cmath

print()

print('Welcome to the velocity calculator. Please enter the following: ')
print()

m = 15  # float(input('Mass (in kg): '))
g = 9.8  # float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
t = 25  # float(input('Time (in seconds): '))
# float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
p = 1.3
A = 0.8  # float(input('Cross sectional area (in m^2): '))
C = 0.5  # float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

c = (1/2)*p*A*C
v = math.sqrt((m*g)/c) * (1 - math.exp((-math.sqrt(m*g*c)/m)*t))

print()
print(f'The inner value of c is: {c:.3f}.')
print(f'The velocity after {t:.2f} seconds is : {v:.3f} m/s.')
print()

v_terminal = math.sqrt((m*g)/c)

print(f'This object reaches terminal velocity of {v_terminal:.3f} m/s. ')
print()


# Calculate the time required to reach terminal velocity.
term_x = math.sqrt((m*g)/c)
print(str(term_x)+' for term_x')
term_y = 1/(v_terminal*(math.sqrt(m*g*c)/m))
print(str(term_y)+' for term_y')
term_z = math.log(term_y)
print(str(term_z)+' for term_z')
# term_z1 = 1 - term_z
# term_z1
# term_t = term_x * term_z1
# term_t
# print(str(term_t)+' is term t')


# term_a = -m/(math.sqrt(m*g*c))
# print(str(term_a)+' is term a')
# print(str(-v_terminal/math.sqrt((m*g)/c)))
# term_b = 1+(-1*(v_terminal/(math.sqrt((m*g)/c))))
# print(str(term_b)+' is term b')
# term_t = math.log(term_b)  # *term_a
#print(str(term_t)+' is term t')

print()


# print(f'This object reaches it\'s terminal velocity in {term_t:.3f} seconds. ')

# The drag coefficient of a skydiver is between 1 and 1.4.
