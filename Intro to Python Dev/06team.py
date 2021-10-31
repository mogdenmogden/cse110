

# amusement park ride
ht, age, alone = '0', '0', 'N'
ht2, age2 = '0', '0'
good_to_go = False
rider2 = ''
print('So you want to ride?  You need to meet some safety requirements. \n')
ht = int(input('How tall are you, in inches? \n'))
age = int(input('How old are you? \n'))

if age >= 18 and ht >= 62:
    good_to_go = True
elif ht < 36:
    print('You are not tall enough to ride this attraction. ')
else:
    print('You need a buddy to ride this attraction. ')
    alone = input('Is there someone riding with you? (Y/N) \n').lower()
    if alone == 'n':
        print('Someone must ride with you. How about the next kid in line? ')
        ht2 = int(input(
            'How tall is the kid, in inches?  (They had better be taller than 36 inches.) \n'))
        age2 = int(input('How old is the kid? \n'))
        if age2 >= 18 and ht2 >= 36:
            good_to_go = True
        elif age2 >= 18 and ht2 < 36:
            print('Your friend doesn\'t meet height requirements. ')
        else:
            exit

    else:
        ht2 = int(input(
            'How tall is your friend, in inches?  (They had better be taller than 36 inches.) \n'))
        age2 = int(input('How old is your friend? \n'))
        if age2 >= 18 and ht2 >= 36:
            good_to_go = True
        elif age2 >= 18 and ht2 < 36:
            print('Your friend doesn\'t meet height requirements. ')
        else:
            exit


if good_to_go:
    print('Have a nice ride! \n')
else:
    print('Sorry. You cannot ride on this attraction. \n')
