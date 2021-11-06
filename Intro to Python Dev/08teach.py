import math

magic_number = int(
    input('How many rows and columns do you want in your multiplication table? '))

for i in range(0, magic_number):
    i = i+1
    print(i)
print()

for i in range(0, magic_number):
    i = i+1
    print(i, end="")
print()
print()

# for i in range(0, magic_number):
#     i = i+1
#     # print(i)
#     for j in range(0, magic_number):
#         j = j+1
#         print(f'{i*j}', end="   ")
#     print()
# print('\n\n\n')

# magic_number = int(
#     input('How many rows and columns do you want in your multiplication table? '))

# for i in range(0, magic_number):
#     i = i+1
#     # print(i)
#     for j in range(0, magic_number):
#         j = j+1
#         print(f'{i*j:5}', end="")
#     print()

width = int(math.log10(magic_number*magic_number))+2
print(width)


for i in range(0, magic_number):
    i = i+1
    # print(i)
    for j in range(0, magic_number):
        j = j+1
        print(f'{i*j:{width}}', end="")
    print()
