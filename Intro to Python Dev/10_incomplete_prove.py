
your_list = []
new_item = ''
the_prices = []
new_price = ''
the_quantities = []
new_qty = ''
total_price = 0

print('\nEnter the items for your shopping list. Type "quit" when you are done.')
while new_item != 'quit':
    new_item = input('Item: ')
    if new_item == 'quit':
        pass
    else:
        your_list.append(new_item)
        new_qty = int(input('How many do you want? (whole numbers only) '))
        the_quantities.append(new_qty)
        new_price = float(input('What is it\'s unit price? '))
        the_prices.append(new_price)

# print('The shopping list contains: ')
# for item in your_list:
#     print(f'Item: {item} ')
# print()

print('\nThe shopping list contains: ')
for i in range(len(your_list)):
    item = your_list[i]
    qty = the_quantities[i]
    price = the_prices[i]
    print(f'[{i+1}] {qty} {item} @ ${price:.2f} ')
    #print(f'[{i}] {item} ')
print()

# change_index = int(
#     input('What item would you like to CHANGE on your list? (type the item#) '))
change_index = int(
    input('What item would you like to CHANGE on your list? (type the item# or 0 for nothing) '))-1
if change_index < 0:
    pass
else:
    your_list[change_index] = input('What would you put in it\'s place? ')
    the_quantities[change_index] = int(
        input('How many do you want? (whole numbers only) '))
    the_prices[change_index] = float(input('What is it\'s unit price? '))


print()
print('The shopping list contains: ')
for i in range(len(your_list)):
    item = your_list[i]
    qty = the_quantities[i]
    price = the_prices[i]
    print(f'[{i+1}] {qty} {item} @ ${price:.2f} ')
    total_price += the_quantities[i] * the_prices[i]

print()
print(f'The Total in the Shopping Cart is ${total_price:.2f}. ')
print(f'The local tax rate is 8.25%. That will be ${0.0825*total_price:.2f}. ')
print(f'Your Final Expense is ${1.0825*total_price:.2f}. (with taxes)')
print()
