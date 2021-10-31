
print()
print('================================================================================================================')
print('')
print('Welcome to the Great Underground Empire! ')
print('You wake up on the side of a strangely shimmering path.  You wonder how you got here.   ')
print('There\'s a certain magical feeling in the atmosphere.  Something like \ncountless electrons buzzing along tiny twisted pathways.')
print('The light seems strangely dim.  You don\'t feel like hanging out in a place like this.   \n')
print('The road runs northwest and southeast from where you stand.')
print('You hear a tiny but ominous voice, something like the sound of little furry animals saying:\n"Choose precisely or be eaten by a grue! "')
print('You had better choose one direction or another.')
print('Enter your choice, but be careful.  I think this is what the voice meant by \'choose precisely\'.  ')

score = 0
location = 'start_path'
choice_start_path = ''
choice_rocky_road = ''
choice_sandy_stretch = ''


# while location != 'dead':
# while choice_start_path == '':
choice_start_path = input('Your choices are NW or SE.  ').upper()
print(1)

if choice_start_path == 'NW':
    location = 'rocky_road'
    print('You go NW. ')
    print('You find yourself on a stretch of Rocky Road.')
    print('Despite feeling vaguely hungry, you see a large silver coin on the ground here.')
    print('The path runs N and SE from here. ')
    while choice_rocky_road == '':
        choice_rocky_road = input(
            'Will you LOOK at the coin, go N, or go SE? ').upper()
        print(2)
elif choice_start_path == 'SE':
    location = 'sandy_stretch'
    print('You go SE.')
    print('You come to a Sandy Stretch on the path. ')
    print('You see a shiny gold coin half buried in the sand. ')
    print('The path runs NW and S from here.  You hear something that sounds like giggling from the south. ')
    while choice_sandy_stretch == '':
        choice_sandy_stretch = input(
            'Will you LOOK at the coin, go NW, or go S from here? ').upper()
        print(3)
else:
    location = 'dead'
    exit

# if choice_sandy_stretch == '':
#     if choice_rocky_road == 'N':
#         print(4)
#     elif choice_rocky_road == 'SE':
#         print(5)
#     elif choice_rocky_road == 'LOOK':
#         print(6)
#     else:
#         error_choice = 'dead'
#         exit
# elif choice_rocky_road == '':
#     if choice_sandy_stretch == 'NW':
#         print(7)
#     elif choice_sandy_stretch == 'S':
#         print(8)
#     elif choice_sandy_stretch == 'LOOK':
#         print(9)
#     else:
#         error_choice = 'dead'
#         exit
# else:
#     exit


if location == 'dead':
    print('oops...The lights go out. In the dark you hear sniffling noises quickly approaching...\n')
    print('You have been eaten by a grue, and to think it happened to such a nice person as yourself.')
    print()
else:
    print('A mist of green fluorescent light begins to swirl about you.')
    print('You feel as if your whole body is dissolving, to be transported back to whereever you came from.')
    print('You wonder if you get to keep the coins you picked up, and whether you will ever discover what a grue is...')
    print('I hope you had fun!  ')
    print()
