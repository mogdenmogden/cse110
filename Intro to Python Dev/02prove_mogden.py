# Matt Ogden CSE 110, Thacker
# Submission Category: Made it my own.
# Justification: I created a scenario/context in which this game is played,
# and added an 'if' statement to handle an initial response by the user.
from time import sleep
print()
print('Hi! My name is Alice. Have you seen a white rabbit wearing gloves and a top hat?')
print('I hoped to play MadLib with him...')
response1 = input('Do you want to do a MadLib? (Y/N) ')
if response1.upper() == 'Y':
    print('/nGreat!  I\'ve got a good one for you.')
    print('In case you\'ve never done this before, or it\'s been a long time, here are some instructions.')
    print('I will ask you for words to use in a story, to replace the "original" words that were used there.')
    print('If you give me boring words, the story will end up being boring.  Let\'s not have that!')
    print('I\'ll help you know what kind of word is needed, to fit the sentence it will be used in. ')
    print('Ready or not, here we go.  I need six words. Make \'em wacky!\n')
    noun1 = input('Give me a type of animal, any kind. ')
    adj1 = input('Give me an adjective (a word to describe your noun). ')
    verb1 = input(
        'I need a verb. (an action word, gerund form. Like "sneezing".) ')
    yell1 = input('Give me a word you might yell loudly. ')
    verb2 = input(
        'Give me another verb. Just the infinitive form, like "sneeze". ')
    verb3 = input('Last one. Give me another verb. ')
    print('I\'m so excited! Just a sec, let me put this together. \n')
    sleep(2)
    print('OK! Here it is!\n')
    print('The other day, I was really in trouble. It all started when I saw a very')
    print(adj1+' '+noun1+' '+verb1+' ' +
          'down the hallway. "'+yell1.upper()+'!" I yelled. But all')
    print('I could think to do was to ' +
          verb2+' over and over. Miraculously,')
    print('that caused it to stop, but not before it tried to '+verb3)
    print('right in front of my family.')
    print('\nWasn\'t that fun?  Thanks for playing with me. ')
else:
    print('\nHuh? Sorry to bother you.\nI\'ll go back to my side of the mirror.\nMaybe the white rabbit went home.')
print('Bye for now.\n')


# The other day, I was really in trouble. It all started when I saw a very
# [adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all
# I could think to do was to [verb] over and over. Miraculously,
# that caused it to stop, but not before it tried to [verb]
# right in front of my family.
