import datetime
currmonth = datetime.date.today()
currmonth = currmonth.strftime("%B %d, %Y")
print('Welcome to Firm Security.\nThe date is ' + currmonth.title()+'. ')
print('Let\'s make your security badge. \nIt will keep me from throwing you in Detention Block J.')
print('It\'s getting late.  Let\'s get on with it.')
print('I need valid responses for all the following questions.')
fname = input('What is your first name? ')
lname = input('What is your last name? ')
email = input('Please enter your email address. ')
phone = input('Please enter your phone number. ')
title = input('What is your job title? (Don\'t guess.) ')
idnum = input(
    'Enter your 7-digit id number with a dash, like this. (#####-##) \nWe will can Human Resources, if you need a hint. ')
species = input('Species? (Common or Latin names are both acceptable.) ')
hair = input('What color is your hair? The lighting is pretty bad down here. ')
eyes = input('...and your eye color? ')
print('\n\nThe ID Card will look like this.')
output = f'--------------------------\n{lname.upper()}, {fname.capitalize()}\n{title.title()}\n{idnum}\n\n{email.lower()}\n{phone}'
print(output)
output = f'\n\nSpecies: {species.upper()}\t\tHair: {hair.upper()}\tEyes: {eyes.upper()}'
print(output)
output = f'\nTraining: In Progress\t\tProcessed: {currmonth}\n--------------------------\n'
print(output)
#
#
# here is another way to write the output
print('')
print('\n\nThe ID Card will look like this.')
print('--------------------------')
print(lname.upper()+', '+fname.capitalize())
print(title.title())
print(idnum)
print('')
print(email.lower())
print(phone)
print('')
print('Species: '+species.upper()+'\t\tHair: '+hair.upper()+'\tEyes: '+eyes.upper() +
      '\nTraining: In Progress'+'\t\t'+'Processed: '+currmonth)
print('--------------------------')
