

# # No loop
# guess = -1

# number = int(input(
#     'What is the magic number we are using? \nPick a whole number between 1 and 10. '))

# guess = int(input('Guess a number. '))
# if guess < number:
#     guess = int(input('Guess higher. '))
# elif guess > number:
#     guess = int(input('Guess lower. '))
# elif guess == number:
#     print('Right on!')
# else:
#     print('That was weird. Do you know what happened? \n\n')

# # Loop
# guess = -1

# number = int(input(
#     'What is the magic number we are using? \nPick a whole number between 1 and 10. '))

# guess = int(input('Guess a number. '))
# while guess != number:
#     if guess < number:
#         guess = int(input('Guess higher. '))
#     elif guess > number:
#         guess = int(input('Guess lower. '))
#     else:
#         print('That was weird. Do you know what happened? \n\n')

# print('Right on!\n\n')

# # Loop and random magic number

# import random
# guess = -1
# guess = int(input('Guess a number. '))
# number = random.randint(1, 10)
# print('We have a new randomly generated magic number. ')
# while guess != number:
#     if guess < number:
#         guess = int(input('Guess higher. '))
#     elif guess > number:
#         guess = int(input('Guess lower. '))
#     else:
#         print('That was weird. Do you know what happened? \n\n')

# print('Right on!\n\n')


# # stretch
import random
guess = -1
play_again = 'Y'

while play_again == 'Y':
    times = 1
    number = random.randint(1, 10)
    print('We have a new randomly generated magic number between 1 and 10. ')
    guess = int(input('Guess a number. '))
    while guess != number:
        times = times + 1
        if guess < number:
            guess = int(input('Guess higher. '))
        elif guess > number:
            guess = int(input('Guess lower. '))
        else:
            print('That was weird. Do you know what happened? \n\n')

    print('Right on!')
    print(f'You guessed it in {times} guesses! \n\n')
    play_again = input('Do you want to play again? (Y/N) ').upper()
    if play_again == 'N':
        print('I\'m so sorry. \n\n')
print('Goodbye. \n\n')
