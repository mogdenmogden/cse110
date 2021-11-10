# welcom and first menu
print('\nWelcome! This is your Python Shopping Cart.')
selection = 0
shopping_list = []
new_item = ''
remove_this = ''
tot_cost = 0

# shopping_list = ["jam", "jelly", "gum", "pig"]
# fred = [*range(0, len(shopping_list), 1)]
# print(f'{fred}')


while int(selection) != 6:
    print('Select an item from this menu of functions.')
    print('1 - Add a new item')
    print('2 - Display the contents of the shopping cart')
    print('3 - Remove an item by name')
    print('4 - Remove an item by number')
    print('5 - Compute the total cost')
    print('6 - Quit')
    selection = input('Choose a number:  ')
    if selection not in ["1", "2", "3", "4", "5", "6"]:
        print('\nThat is not a valid selection. Try again. \n')
        selection = 0
    elif int(selection) == 1:
        new_item = input('\nWhat will you add to the list? ')
        shopping_list.append(new_item)
        print(f'{new_item.title()} has been added to your cart.\n')
    elif int(selection) == 2:
        if len(shopping_list) == 0:
            print('\nYour cart is empty. \n')
        else:
            print(f'\nYour cart contains: \n')
            for item in shopping_list:
                print(f'{1+shopping_list.index(item)}) {item}')
            print()
    elif int(selection) == 3:
        remove_this = input('\nWhat would you like to remove? (NAME) ')
        if remove_this in shopping_list:
            shopping_list.remove(remove_this)
            print(f'{remove_this.title()} has been deleted.\n')
            print(f'Your shopping cart now holds: ')
            for item in shopping_list:
                print(f'{1+shopping_list.index(item)}) {item}')
            print()
        else:
            print(f'\n{remove_this.title()} is not in your Cart.\n')
    elif int(selection) == 4:
        remove_this = input('\nEnter the NUMBER of the item to remove. ')
        if int(remove_this) not in [*range(1, 1+len(shopping_list), 1)]:
            print('That item number does not exist. \n')
        else:
            shopping_list.pop(int(remove_this)-1)
            print(f'Your shopping cart now holds: ')
            for item in shopping_list:
                print(f'{1+shopping_list.index(item)}) {item}')
            print()
    elif int(selection) == 5:
        print('\nDid I hear you say, "I\'ll gladly pay you Tuesday for some ')
        print(f'{shopping_list} today?"')
        print()
    elif int(selection) == 6:
        print('\nYou have chosen to exit the Shopping List. \n')
    else:
        print('\nThat is not a valid selection. \n')


print('\nThanks for shopping with Python!\n')
