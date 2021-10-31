

# amusement park ride
ht, age, alone = '0', '0', 'N'
ht2, age2 = '0', '0'
good_to_go = False
rider2 = ''
print('\nWelcome to the main attraction! Its a thrilling roller coaster ride!  \nYou need to meet some safety requirements before you can board. \n')
ht = int(input('How tall are you, in inches? \n'))
age = int(input('How old are you? \n'))

# check golden passport of primary rider
if 12 <= age <= 17:
    golden1 = input('Do you have a golden passport? \n').lower()
    if golden1 == 'y':
        age = 18
# check age and height
if ht < 36:
    print('You are not tall enough to ride this attraction. ')
# handle scenarios when rider 1 can ride alone
elif age >= 18 and ht >= 62:
    good_to_go = True
    print('You can ride alone. ')
    # check if there is a 2nd rider
    alone = input('Is there someone riding with you? (Y/N) \n').lower()
    if alone == 'y':
        ht2 = int(input(
            'How tall is your friend, in inches?  (They had better be taller than 36 inches.) \n'))
        age2 = int(input('How old is your friend? \n'))
        if ht2 < 36:
            print(
                'Your friend doesn\'t meet the height requirement.  You will have to ride without them.')
        elif age2 >= 18 and ht2 >= 36:
            good_to_go = True
        elif age >= 12 and age2 >= 12 and ht >= 52 and ht2 >= 52:
            good_to_go = True
        else:
            exit
# handle scenarios when a 2nd rider is required
else:
    # require a 2nd rider
    print('You don\'t meet the requirements to ride alone.  You need a buddy. ')
    alone = input('Is there someone riding with you? (Y/N) \n').lower()
    # handle scenarios when there is not a rider friend
    if alone == 'n':
        print('Someone must ride with you. How about the next kid in line? ')
        ht2 = int(input(
            'How tall is the kid, in inches?  (They had better be taller than 36 inches.) \n'))
        age2 = int(input('How old is the kid? \n'))
        if age2 >= 18 and ht2 >= 36:
            good_to_go = True
        elif age2 >= 18 and ht2 < 36:
            print('That kid doesn\'t meet height requirements. They can\'t ride. ')
            print(
                'The next kid in line is 16 years old and 54 inches tall.  You will ride with him. ')
            ht2 = 54
            age2 = 16
            good_to_go = True
        elif (age >= 12 and age2 >= 12 and ht >= 52 and ht2 >= 52) or ((age >= 14 and age2 >= 16) or (age >= 16 and age2 >= 14)):
            good_to_go = True
        else:
            exit
    # handle scenarios when the friend is present
    else:
        ht2 = int(input(
            'How tall is your friend, in inches?  (They had better be taller than 36 inches.) \n'))
        age2 = int(input('How old is your friend? \n'))
        if age2 >= 18 and ht2 >= 36:
            good_to_go = True
        elif age2 >= 18 and ht2 < 36:
            print('Your friend doesn\'t meet height requirements. They cannot ride this attraction, no matter their age. ')
            print(
                'The next kid in line is 16 years old and 54 inches tall.  You will ride with him. ')
            ht2 = 54
            age2 = 16
            good_to_go = True
        elif (age >= 12 and age2 >= 12 and ht >= 52 and ht2 >= 52) or ((age >= 14 and age2 >= 16) or (age >= 16 and age2 >= 14)):
            good_to_go = True
        else:
            exit


if good_to_go == True:
    print('Have a nice ride! \n')
else:
    print('Sorry. You cannot ride on this attraction. \n')
