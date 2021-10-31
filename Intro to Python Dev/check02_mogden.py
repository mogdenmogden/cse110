first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print('')
output = ('Your name is {1}, {0} {1}.').format(first_name, last_name).title()
print(output)
print('')
print('This is the second way to do this, as illustrated in the videos.')
output = f'Your name is {last_name.title()}, {first_name.title()} {last_name.title()}.'
print(output)

print('')
# I'm experimenting...
output = f'Your name is {last_name}, {first_name} {last_name}.'.title()
print(output)
