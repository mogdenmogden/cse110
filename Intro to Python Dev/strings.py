colors = "red green blue yellow orange"

color_parts = colors.split()
#color_parts = ['red', 'green', 'blue', 'yellow', 'orange']

print(colors)
print(color_parts)

for color in color_parts:
    print(color)

second = color_parts[1]
print(second)

colors = "red,green,blue,yellow,orange"
color_sepa = colors.split(sep=",")
print(color_sepa)
#color_sepa = ['red', 'green', 'blue', 'yellow', 'orange']


###################
name = " \t   Matt Ogden   \n"
name = name.strip()
print(f'---{name}---')

cleaned = name.strip()
print(f'---{cleaned}---')


###################
