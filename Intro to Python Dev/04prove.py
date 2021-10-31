#
# File: 04prove.py
# Author: Matt Ogden
# Purpose: Meal Price Calculator.
#

# welcome scenario
print()
print(f'Welcome to Mel\'s Diner!')
print()
print(f'This diner is a little weird.')
print(f'You just tell us what you want and how much you are willing pay for it. ')
print(f'Make sure you have enough money when we are done. (wink, wink) \n\n')

# input and calculations
# drinks
print('Would you like something to drink?  We only serve large 7-Ups. ')
qty_drinks = int(input('How many drinks would you like? '))
drink_price = float(input('How much will you pay for each drink? '))
exp_drinks = qty_drinks*drink_price
print()

# appetizers
print('How about an appetizer or two, to get started?  We only have cheese fries tonight. ')
qty_appetizer = int(input('How many appetizers do you want? '))
appetizer_price = float(input('How much will you pay for each appetizer? '))
exp_appetizer = qty_appetizer*appetizer_price
print()

# summarize drinks & appetizers
print(
    f'All right. We have {qty_drinks} drinks and {qty_appetizer} appetizers. I\'ll bring those right out!')
print('\n.\n..\n...')
print('Here are your drinks and appetizers. \n')

# entrées
# child menu
print('Are you ready to order?  \n\nWould any of you like something from the children\'s menu?')
print('We have chicken nuggets on the children\'s menu.  Six nuggets in each meal.')
qty_child = int(input('How many nugget meals will you order? '))
child_meal = float(input('How much will you pay for each nugget meal? '))
exp_child = qty_child*child_meal


# adult menu
print('\nWould you like something from the regular menu? We are out of everything, except Salisbury Steaks.')
print(f'Luckily, Salisbury Steak is our house specialty!  ')
print(f'People come from all over the Underground Empire to try it. Is that what brought you here? ')
print(f'...')
qty_adult = int(input('Anyway, how many entrées will you buy? '))
adult_meal = float(
    input('How much would you pay for our FAMOUS Salisbury Steak? '))
exp_adult = qty_adult*adult_meal

# meal summary
print()
print(
    f'Right! \nI have {qty_child} nugget meals, \nand {qty_adult} FAMOUS Salisbury Steaks.  ')
print(f'I\'ll be right back with your order!')
print(f'...')
print('\n.\n..\n...\nHere\'s your food. Enjoy!')
print(f'...an hour later...\n')


# desert
print(f'Have you saved room for desert!? Our desert portions are HUGE.')
print(f'We have flahn.  It\'s French flahn.')
print(f'Can you tell, just by the way I say it? FlAAHn. ')
qty_desert = int(input('How many HUGE \'flahnz\' will you have? '))
if qty_desert > 0:
    desert_price = float(input('What will you pay for French flahn? '))
    exp_desert = qty_desert*desert_price
else:
    print('OK, then.')
    exp_desert = 0

# finish and settle the bill
print(f'Are you ready for your bill?\n\n')
# sales tax
print(f'You know, like everything else here you get to choose your sales tax. ')
taxrate = float(input(
    f'What is YOUR sales tax rate? \nPlease input the percent in decimal form. \nEx: 8.5 %= 0.085 '))
print(f'Thank you. ')

# calculate subtotal and taxes
subtotal = exp_drinks+exp_appetizer+exp_child+exp_adult+exp_desert
taxes = round(taxrate*subtotal, 2)
total = subtotal+taxes

# print a receipt
print(f'\n\nThis is your receipt. ')
print(
    f'Drinks: {qty_drinks} @ $ {drink_price: .2f}= $ {exp_drinks: .2f}')
print(
    f'Appetizer: {qty_appetizer} @ $ {appetizer_price: .2f}= $ {exp_appetizer: .2f}')
print(
    f'Child meals: {qty_child} @ $ {child_meal: .2f}= $ {exp_child: .2f}')
print(
    f'Adult meals: {qty_adult} @ $ {adult_meal:.2f} = $ {exp_adult: .2f} ')
if qty_desert > 0:
    print(
        f'Desert: {qty_desert} @ $ {desert_price:.2f} = $ {exp_desert: .2f} ')
else:
    next
print()
print(f'Subtotal   $ {subtotal:.2f} ')
print(f'Tax  @ {taxrate} $ {taxes:.2f} ')
print(f'Total      $ {total:.2f} ')
print()
print()

# gratuity
tip = round(float(
    input('Was your service excellent?\nHow much will you tip the server? ')), 2)
total = round(total + tip, 2)

# print revised receipt
print('\n\nThis is your new receipt. \n')

print(
    f'Drinks: {qty_drinks} @ $ {drink_price: .2f}= $ {exp_drinks: .2f}')
print(
    f'Appetizer: {qty_appetizer} @ $ {appetizer_price: .2f}= $ {exp_appetizer: .2f}')
print(
    f'Child meals: {qty_child} @ $ {child_meal: .2f}= $ {exp_child: .2f}')
print(
    f'Adult meals: {qty_adult} @ $ {adult_meal:.2f} = $ {exp_adult: .2f} ')
if qty_desert > 0:
    print(
        f'Desert: {qty_desert} @ $ {desert_price:.2f} = $ {exp_desert: .2f} ')
else:
    next
print()
print(f'Subtotal   $ {subtotal:.2f} ')
print()
print(f'Tax  @ {taxrate} $ {taxes:.2f} ')
print()
print(f'Gratuity   $ {tip} ')
print()
print(f'Total      $ {total:.2f} ')
print()
print()


# cash exchanged
pmt_type = input('Will you be paying by cash, check, or card? ')

while(True):
    tendered = float(input('How much will you pay? '))
    if tendered < total:
        print('You must pay your whole bill. ')
        print('Do we need you to put in some time washing dishes? Your party can wait for you in the alley.')
        print('Or, maybe you could get a little cash from the other customers to cover your bill? ')
    else:
        print('Thank you. ')
        print()
        break

change_given = round(tendered, 2) - round(total, 2)
print()
print(f'Your change is $ {change_given: .2f} ')
print()

# goodbye
print('Please come again! ')
print()
