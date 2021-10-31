
from typing import TYPE_CHECKING


print()
print('================================================================================================================')
print('')
print('Welcome to the Great Underground Empire! ')
print('You wake up on the side of a strangely shimmering path within a large cavern.  You wonder how you got here.   ')
print('There\'s a certain magical feeling in the atmosphere.  Something like \ncountless electrons buzzing along tiny twisted pathways.')
print('The light seems strangely dim.  You don\'t much feel like hanging out in a place like this...   ')
print('Still, when you are lost they always say you should stay where you are until someone finds you.')
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
choice_start_path = input(
    '\nYour choices are to go "NW", "SE", or "STAY" where you are.  \n').upper()


if choice_start_path == 'NW':
    location = 'rocky_road'
    print('You go NW. ')
    print('You find yourself on a stretch of Rocky Road.')
    print('Despite feeling vaguely hungry, you see a large silver coin on the ground here.')
    print('The path runs N and SE from here. ')
    choice_rocky_road = input(
        '\nWill you "GET" the coin, go "N", or go "SE"? \n').upper()

elif choice_start_path == 'SE':
    location = 'sandy_stretch'
    print('You go SE.')
    print('You come to a Sandy Stretch on the path. ')
    print('You see a shiny gold coin half buried in the sand. ')
    print('The path runs NW and S from here.  You hear something that sounds like giggling from the northwest. ')
    choice_sandy_stretch = input(
        '\nWill you "GET" the coin, go "NW", or go "S" from here? \n').upper()


elif choice_start_path == 'STAY':
    location = 'start_path'
    print('You have chosen to stay where you are, for now at least. ')
    print('You notice a small copper coin nearby, under a bush.')
    choice_start_path = input(
        '\nWill you "GET" the coin, or "STAY" still? \n').upper()
    if choice_start_path == 'STAY':
        start_path_counter = 0
        while start_path_counter < 1 and choice_start_path == 'STAY':
            print('An odd purple mist has begun swirling in, closer and closer to you. It blocks the path. You can\'t go anywhere.')
            choice_start_path = input(
                '\nThe coin is still there.  You can "GET" the coin, or "STAY" still. \n').upper()
            if choice_start_path == 'GET':
                pass
            else:
                start_path_counter = start_path_counter + 1
        if start_path_counter >= 1:
            location = 'dead'
        else:
            pass
    elif choice_start_path == 'GET':
        pass
    else:
        print('I don\'t think you "CHOSE WISELY".')
        location = 'dead'
else:
    print('I don\'t think you "CHOSE WISELY".')
    location = 'dead'

# stayed put and picked up the coin
if location == 'start_path' and choice_start_path == 'GET':
    print('You take and look closely at the small copper coin.  As you do, ')
    print('the copper color begins to rub off, revealing the golden features of a bearded man in a tophat.')
    print('(Funny. That\'s not Abraham Lincoln.)')
    print('A very short man in olive colored formal wear runs into view.   ')
    print('The man demands: "Give me back my coin!" ')
    choice_start_path = input(
        '\nYou can "GIVE" it back or "KEEP" it.  Which will you do? \n').upper()
    if choice_start_path == 'GIVE':
        print('The man gratefully takes the coin.  He is so happy, he offers to send you home.')
        print('The man pulls some shiny green powder from his vest pocket and blows it into your face!')
        print('You cough, and ...')

    elif choice_start_path == 'KEEP':
        print('You decide to keep the coin.  The small man seems furious!')
        print('If you give the coin back, the little man promises to give you a ruby.')
        choice_start_path = input(
            '\nWill you "RETURN" it back or "KEEP" it? \n').upper()
        if choice_start_path == 'KEEP':
            print(
                'The man jumps up and down, promising to send you home if you give the coin to him.')
            choice_start_path = input(
                '\nWill you "GIVE" it back or "KEEP" the little coin? \n').upper()
            if choice_start_path == 'GIVE':
                print('The man jumps for joy, throwing his arms in the air.')
                print('As you watch, you feel yourself float up into the air. You notice your body is dispersing, like steam in the air. ')
            elif choice_start_path == 'KEEP':
                print('You put the coin in your pocket, and turn your back to the man.')
            else:
                print('I don\'t think you "CHOSE WISELY".')
                location = 'dead'
        elif choice_start_path == 'RETURN':
            print(
                'The man pulls a ruby as large as the coin from his vest pocket and hands it to you.  ')
            print('He disappears in a puff of purple smoke.  You are left holding the ruby. You put it in your pocket.')
        else:
            print('I don\'t think you "CHOSE WISELY".')
            location = 'dead'
    else:
        print('I don\'t think you "CHOSE WISELY".')
        location = 'dead'
else:
    pass

# rocky road and picked up the coin
if location == 'rocky_road' and choice_rocky_road == 'GET':
    print('You pick up the large silver coin. It\'s heavy.  It looks very valuable. ')
    print('One side depicts an evil looking bird of prey, wings spread.  The other has a picture of flames.')
    choice_rocky_road = input(
        '\nWill you "KEEP" the coin, or "DROP" it? \n').upper()
    if choice_rocky_road == 'KEEP':
        print('As you put the coin into your pocket, you feel it becoming warm. ')
        print('Within a few moments the coin and your pocket begin to smolder. ')
        print('You realize your peril and try to push the coin from your pocket onto the ground.')
        print('Unfortunately, it is too late.  You feel your body turn to a black charcoal dust...')
        location = 'dead'

    elif choice_rocky_road == 'DROP':
        print('In the act of dropping the coin, you see a small man in olive colored formal wear sprinting toward you.')
        print('He yells, "Get back!" and sweeps up the large silver coin with an impressive bejeweled glove.')
        print('Once he has the coin safely stowed in a wet handkerchief, the man bows.')
        print('He says, "Thank you for helping me find that coin.  As a reward, here is a gold doubloon."')
        print('He drops the gold coin into your outstretched palm.  With it\'s touch you start to feel a little light headed...')
    else:
        print('I don\'t think you "CHOSE WISELY".')
        location = 'dead'
# rocky road and returned SE (block the way)
elif location == 'rocky_road' and choice_rocky_road == 'SE':
    print('You try returning to the southeast, the direction you came.')
    print('A small man wearing olive colored evening wear blocks your way.')
    print('The man says: "What are you doing here? Do you want to go home?" ')
    choice_rocky_road = input(
        '\nDo you say "YES" I want to go home, or "NO" leave me alone? \n').upper()
    if choice_rocky_road == 'YES':
        print('The little man grants my wish.  He whacks me with a little wand...')
    elif choice_rocky_road == 'NO':
        print('You step around the man, and move on.  ')
        print('As you do, you trip over some unseen thing.  Falling, you perceive reality ')
        print('shattering around you, like a rainbow mirage...')
    else:
        print('I don\'t think you "CHOSE WISELY".')
        location = 'dead'

# rocky road and went N
elif location == 'rocky_road' and choice_rocky_road == 'N':
    print('Moving on, you find a beautiful still pool among a forest-like jumble of stalacmites.')
    print('The pool reflects light, like a mirror.')
    print('Naturally, you look into the pool.  You expect to see your handsome self, ')
    print('but instead you see a bedraggled person who bears no resemblance to the face you know and love.')
    print('A little man, dressed in olive drab formal attire appears beside you.')
    print('He says, have you seen any coins around here? I will help you if you help me...')
    choice_rocky_road = input(
        '\nDo you "TELL" the man about the coin you saw or say "SORRY"? \n').upper()
    if choice_rocky_road == 'TELL':
        print('The man thanks you, and offers you your heart\'s desire.  Perhaps he guesses what that might be, because he doesn\'t ask anything else. ')
        print('The little man removes his hat, bows, and taps your shoe using a wand with a little star on the end.  You find yourself transporting home.')
    elif choice_rocky_road == 'SORRY':
        print('The man replies, "Quite all right."')
        print('The next thing you know, you have been pushed into the pool. ')
        print('You find yourself swirling, as if circling a drain...')
        location = 'dead'
    else:
        print('I don\'t think you "CHOSE WISELY".')
        location = 'dead'

else:
    pass


# sandy stretch and picked up the coin
if location == 'sandy_stretch' and choice_sandy_stretch == 'GET':
    print('You pick up the coin. ')
    print('You notice the gold coin has a square hole in the center.')
    print('As you put the coin in your pocket, a small man wearing olive drab evening attire walks into view.')
    print('The man says: "I\'ve been looking for that coin for a long time.  If you give it to me, I\'ll ')
    print('make it worth your while.  I will trade either this sapphire or these magical wings. "')
    print('The sapphire is a large, cobalt blue speciment.  Waaay too big for a ring.  \nThe magic wings flutter gently as the man holds them up for inspection.  They can be worn, like a vest or harness.')
    choice_sandy_stretch = input(
        '\nWhat will you do?  Do you "KEEP" the coin, trade for the "GEM", or the "WINGS"? \n').upper()
    if choice_sandy_stretch == 'KEEP':
        print('The man grimaces and says I will regret my decision.  Yeah, right!')
        print('The man turns his back and walks away.  ')
        print('As he doe so, he whistles a strange tune.  Something like that candy guy played on a flute in that movie...')
        print('A giant ant lion erupts from the sand and devours you!')
        location = 'dead'
    elif choice_sandy_stretch == 'GEM':
        print('The man snatches the strange coin from your hand and gives you the sapphire.  It is really, really, really beautiful...')
        print('As you gaze at the sapphire, you feel pulled in.  It\'s like you are being transported to another place.')

    elif choice_sandy_stretch == 'WINGS':
        print('The man snatches the strange coin and hands you the wings.  When I ask what the wings can do, his reply is: ')
        print('"What do you think?  They fly!."  ')
        print('He runs away.  You strap the wings on.')
        print('The wings flutter, and you are lifted off the cavern floor.  You see the wings have grown proportionally to fit your body.')
        print('As you zoom about, testing your new found freedom, someone hiding behind a nearby boulder shines what appears to be')
        print('a green laser pointer at you.  The moment it touches you, you feel dizzy.')
    else:
        print('I don\'t think you "CHOSE WISELY".')
        location = 'dead'
# sandy stretch and returned NW (block the way)
elif location == 'sandy_stretch' and choice_sandy_stretch == 'NW':
    print('You turn around, and see a large lime-green gelatinous cube sliding toward you.')
    print('You can see remnants of things it has engulfed in the past: \nbits of travel gear, shoes, tools, carrots, and a few stray coins.')
    print('A small man appears. He is wearing an olive drab tuxedo.  He waves a long orange carrot at the gelatinous cube, and it halts! ')
    print('The man asks, "Have you seen any coins around here?  I lost mine. ')
    print('You you did, just a moment ago in the sand!  That big green cube makes you nervous.  You want to get out of there. ')
    choice_sandy_stretch = input(
        '\nDo you "TELL" him about the coin, or say "SORRY" and back away slowly. \n').upper()
    if choice_sandy_stretch == 'TELL':
        print('The man walks over to the sand and picks up the coin.  He is overjoyed.')
        print('Waving his magic carrot in your general direction, he sends you home. ')
    elif choice_sandy_stretch == 'SORRY':
        print('The man is not pleased.  He swishes the magic carrot in the air.')
        print('As you are engulfed by the gelationous cube, you get the feeling you won\'t like how this turns out. ')
        location = 'dead'
    else:
        print('I don\'t think you "CHOSE WISELY".')
        location = 'dead'


# sandy stretch and went S
elif location == 'sandy_stretch' and choice_sandy_stretch == 'S':
    print('Moving along you realize you are walking in a dry stream bed.')
    print('You notice an object protruding from the sand.  It appears to be a handle.')
    choice_sandy_stretch = input(
        '\nWill you "GET" the object or "LEAVE" it? \n').upper()
    # print(choice_sandy_stretch)
    if choice_sandy_stretch == 'GET':
        print('You pull the object from the sand by its handle.  It is a sword.')
        print('The sword gleams in the strange light of the realm.  As you hold it, you feel a strange sensation.')
        print('You are somehow stronger, more aware.  Huh. Weird. ')
    elif choice_sandy_stretch == 'LEAVE':
        print('Turning to go, you begin to hear something moving toward you.  You look to see what looks like an ')
        print('enormous ant lion emerging from the sand. That thing in the sand appears to be a sword.')
        print('Perhaps the sword belonged to the ant lion\'s last victim.  You grab it, despite the danger.')
        choice_sandy_stretch = input('\nWill you "FIGHT" or "RUN"? \n').upper()
        if choice_sandy_stretch == 'FIGHT':
            print('Have you ever used a sword before? You swing the sword in a valiant effort to save your life. Alas, the ant lion wins...')
            location = 'dead'
        elif choice_sandy_stretch == 'RUN':
            print('You see a nearby series of ledges in the cavern wall and recognize your chance to escape.  \nBounding toward it with the sword you ')
            print('jump onto the lowest ledge and climb out of the ant lion\'s reach. ')
            print(
                'While you look around from your high perch, you notice a void in the rock face.')
            print(
                'The the hole contains a gold coin, as big and thick as a hockey puck.  ')
            print('Reaching for the coin you think to yourself, it\'s my lucky day!.  ')
            print(
                'As your hand closes about the gold coin the world seems to dim around you...')
        else:
            print('I don\'t think you "CHOSE WISELY".')
            location = 'dead'
    else:
        print('I don\'t think you "CHOSE WISELY".')
        location = 'dead'
else:
    pass


if location == 'dead':
    print('\n\noops...The lights go out. \n')
    print('You died.  And to think it happened to such a nice person as yourself.')
    print('Somehow, still very self aware, you feel for a moment as if you are swirling around some dark vortex.')
    print('The next moment, you find you are not really dead.  You are back home, safe and sound.')
    print()
else:
    print('\n\nA voice from nowhere announces: "Good job, wanderer!" ')
    print('A mist of green fluorescent light begins to swirl about you.')
    print('You feel as if your whole body is dissolving, to be transported back to whereever you came from.')
    print('You wonder if you get to keep your treasure, and whether you will ever discover what a grue is...')
    print('I hope you had fun!  ')
    print()
