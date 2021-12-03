people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

for i in people:
    p_list = i.split(" ")
    # #print(i.split(" "))
    # print(p_list)
    for j in p_list:
        print(j)


y_age = 999
y_person = ''

for i in people:
    peep = i.split(" ")
    for j in peep:
        # print(peep[1])
        age = int(peep[1])
        name = peep[0]
        if age < y_age:
            y_age = age
            y_person = name

print(f'The youngest person is {y_person}, who is {y_age} years old.')
