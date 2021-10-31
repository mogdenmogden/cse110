"""
File: 04prepare_check_mro.py
Author: Matt Ogden
Purpose: Convert Fahrenheit temperature to Celsius.
"""
print()

f_temp = float(input('What is the temperature in degrees Fahrenheit? '))
c_temp = (5/9)*(f_temp-32)

print(f'The temperature in Celsius is {c_temp:.1f} ', chr(176), 'C. ', sep='')
print()
