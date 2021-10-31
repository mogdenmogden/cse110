first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print('')
output = ('Your name is {1}, {0} {1}.').format(first_name, last_name)
print(output)


output = f'Your name is {last_name}, {first_name} {last_name}.'
print(output)
