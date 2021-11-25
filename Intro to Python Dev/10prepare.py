
your_list = []
new_item = ''

print('Enter the items on your list. Type "quit" when you are done.')
while new_item != 'quit':
    new_item = input('Item: ')
    if new_item == 'quit':
        pass
    else:
        your_list.append(new_item)

print('the shopping list contains: ')
for item in your_list:
    print(f'Item: {item} ')


print('the shopping list contains: ')
for i in range(len(your_list)):
    item = your_list[i]
    # print(f'[{i+1}] {item} ')
    print(f'[{i}] {item} ')

# change_index = int(
#     input('What item would you like to CHANGE on your list? (type the item#) '))-1
change_index = int(
    input('What item would you like to CHANGE on your list? (type the item#) '))
your_list[change_index] = input('What would you put in it\'s place? ')
print()
print('the shopping list contains: ')
for i in range(len(your_list)):
    item = your_list[i]
    print(f'[{i+1}] {item} ')


print()
