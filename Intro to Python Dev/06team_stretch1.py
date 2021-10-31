
# amusement park ride
ht, age, alone, single_rider = '', '', 'N', False
golden1, golden2 = 'n', 'n'
print('So you want to ride?  You need to meet some safety requirements. \n')
ht = int(input('How tall are you, in inches? \n'))
if ht < 36:
    print('You cannot ride on this attraction. ')
    # exit
else:
    age = int(input('How old are you? \n'))
    alone = input('Do you want to ride alone? (Y/N) \n').lower()

    if 12 <= age <= 17:
        golden1 = input('Do you have a golden passport? (Y/N) \n').lower()

    if alone == 'y' and ((age >= 18 and ht >= 62)):
        # single_rider = True
        print('Climb in. ')
    elif alone == 'y' and golden1 == 'y':
        # single_rider = True
        print('OK. You have a golden ticket. You can go alone even though you are not 18. ')

    elif alone != 'y' and ((age >= 18 and ht >= 62) or (age < 18 and golden1 == 'y')):
        # single_rider = False
        print('So, you are riding with someone. ')
        ht2 = int(input('How tall is your friend, in inches? \n'))
        age2 = int(input('How old is your friend? \n'))

        else:
            exit
    else:
        # single_rider = False
        print('You can\'t ride alone. You need a buddy. ')
        ht2 = int(input('How tall is your buddy, in inches? \n'))
        age2 = int(input('How old is your buddy? \n'))

        if ht2 < 36:
            print('Your friend can\'t ride. Sorry. ')
        elif 12 <= age2 <= 17:
            golden2 = input(
                'Does your friend have a golden passport? (Y/N) \n').lower()
        else:
            exit

        if (golden2 == 'y' or golden1 == 'y') and age >= 12 and age2 >= 12 and ht >= 52 and ht2 >= 52:
            print('You can ride together. ')
        else:
            exit


print('Goodbye. \n')
