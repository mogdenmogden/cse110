
friends = []

add_one = ''
# add many values
while add_one != 'end':
    add_one = input(
        'Who are your friends? Type "end" if you are done with your list. ')
    if add_one == 'end':
        pass
    else:
        friends.append(add_one)
for name in friends:
    print(name)
