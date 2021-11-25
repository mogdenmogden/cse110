# welcom and first menu
print('\nWelcome! This is your Python Shopping Cart.')
selection = 0
shopping_list = []
price_list = []
new_item = ''
new_price = 0.0
remove_this = ''
the_quantities = []
new_qty = ''
result_list = []
total_price = 0


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

        new_qty = int(input('How many do you want? (whole numbers only) '))
        the_quantities.append(new_qty)

        new_price = float(input(f'What is the unit price of {new_item}? '))
        price_list.append(new_price)
        print()
        print(
            f'{new_qty} {new_item.title()} @ ${new_price:.2f} each has been added to your cart.\n')

    elif int(selection) == 2:
        if len(shopping_list) == 0:
            print('\nYour cart is empty. \n')

        else:
            print(f'\nYour Shopping Cart contains: \n')
            for i in range(len(shopping_list)):
                print(
                    f'[{1+i}] {the_quantities[i]} {shopping_list[i]} @ ${price_list[i]:.2f} each')
            print()

    elif int(selection) == 3:
        if len(shopping_list) == 0:
            print('\nYour cart is empty. \n')

        else:
            remove_this = input('\nWhat would you like to remove? (NAME) ')
            if remove_this in shopping_list:
                index = shopping_list.index(remove_this)
                shopping_list.remove(remove_this)
                del price_list[index]
                del the_quantities[index]

                print(f'{remove_this.title()} has been deleted.\n')
                print(f'Your shopping cart now holds: ')

                if len(shopping_list) == 0:
                    print('\n<nothing> \n')

                else:
                    for i in range(len(shopping_list)):
                        print(
                            f'[{1+i}] {the_quantities[i]} {shopping_list[i]} @ ${price_list[i]:.2f} each')
                    print()

            else:
                print(f'\n{remove_this.title()} is not in your Cart.\n')

    elif int(selection) == 4:
        if len(shopping_list) == 0:
            print('\nYour cart is empty. \n')

        else:
            remove_this = input('\nEnter the NUMBER of the item to remove. ')
            if int(remove_this) not in [*range(1, 1+len(shopping_list), 1)]:
                print('That item number does not exist. \n')

            else:
                index = int(remove_this)-1
                hold_name = shopping_list[index]
                # shopping_list.pop(int(remove_this)-1)
                del shopping_list[index]
                del price_list[index]
                del the_quantities[index]

                print(f'{hold_name.title()} has been deleted.\n')
                print(f'Your shopping cart now holds: ')

                if len(shopping_list) == 0:
                    print('\n<nothing> \n')

                else:
                    for i in range(len(shopping_list)):
                        print(
                            f'[{1+i}] {the_quantities[i]} {shopping_list[i]} @ ${price_list[i]:.2f} each')
                    print()

    elif int(selection) == 5:
        # print('\nDid I hear you say, "I\'ll gladly pay you Tuesday for some ')
        # print(f'{shopping_list} today?"')
        result_list = [the_quantities[i] * price_list[i]
                       for i in range(len(shopping_list))]
        total_price = sum(result_list)
        print()
        print(f'Your Shopping Cart Total is : ${total_price:.2f} ')
        print(
            f'Sales Tax is 8.25%. That will be ${0.0825*total_price:.2f}. ')
        print(f'Grand Total: ${1.0825*total_price:.2f}. ')
        print()

    elif int(selection) == 6:
        print('\nYou have chosen to exit the Shopping List. \n')

    else:
        print('\nThat is not a valid selection. \n')


print('\nThanks for shopping with Python!\n')
