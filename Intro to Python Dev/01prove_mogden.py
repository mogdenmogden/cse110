from time import sleep
print(
    'Hello, class.  My name is Matt. \nI am going to ask you what your favorite color is.  \nAnswer carefully.')
sleep(1)
print('.')
sleep(1)
print('..')
sleep(1)
print('...')
print('I hope you thought long and hard about your favorite color. \nIt\'s nearly as important as the meaning of life.')
fave = input('What is your favorite color? ')
fave = fave.lower()
if fave == '':
    print('What was that? I missed it...')
    fave = input('Please answer again. ').lower
elif fave == 'magenta':
    print("Are you sure?  That doesn't sound like a carefully chosen favorite...")
elif fave == 'green':
    print('Good choice!')
else:
    print('I can see you are sure of yourself.')
print('After deliberation, your favorite color is ' +
      fave.title() + '. \n\n\n')
