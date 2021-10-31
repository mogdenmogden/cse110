# sentence = 'The dog is named Sammy.'
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.capitalize())
# print(sentence.count('a'))

# first_name = input('What is your first name?')
# last_name = input('What is your last name?')
# print('Hello '+first_name.capitalize() + last_name.capitalize())

# fname = 'Christopher'
# lname = 'Harrison'

fname = input('Please enter your first name: ')
lname = input('Please enter your last name: ')
# print(fname + lname)
print('Hello, '+fname.capitalize()+' '+lname.capitalize()+'.')

# Custom string formatting.
output = 'Hello, ' + fname + ' ' + lname
print(output)
output = 'Hello, {} {}'.format(fname, lname)
print(output)
output = 'Hello, {0} {1}'.format(fname, lname)
print(output)
output = 'Hello, {1}, {0}'.format(fname, lname)
print(output)
# Only available in Python 3
output = f'Hello, {fname} {lname}'
print(output)

# words = 'the cat IN THE hat'
# words.capitalize() #cap like sentence
# words.title() # title case
# words.upper() # all caps
# words.lower() # all lower case
# words.count("t") # counts all of that character case sensitive
# words.lower().count("t") # makes all Tt characters lower and then counts them (t)
