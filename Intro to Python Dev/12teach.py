#lin = 0
max_chpt = -1
max_book = ""
max_div = ""

# #regular version
# with open("books_and_chapters.txt") as scrip:
#     for line in scrip:
#         # print(line)
#         #lin = lin + 1
#         bk_list = line.strip().split(":")
#         # print(bk_list)
#         division = bk_list[2]
#         chpt = int(bk_list[1])
#         book = bk_list[0]
#         print(f'Scripture: {division}, Book: {book}, Chapters: {chpt} ')
#         if chpt > max_chpt:
#             max_chpt = chpt
#             max_book = book
#             max_div = division
#         #print(f'{max_chpt} {max_book}')

# print(f'\nThe book with the largest number of chapters is:')
# print(f'{max_book}, with {max_chpt} chapters in the {max_div}. ')

# stretch version
max_chpt = -1
max_book = ""
max_div = ""

print('[1] Old Testament\n[2] New Testament\n[3] Book of Mormon\n[4] Doctrine and Covenants\n[5] Pearl of Great Price')
choice = int(input(
    'Please select the number of the volume of scripture you want to examine: '))-1
volumes = ["Old Testament", "New Testament", "Book of Mormon",
           "Doctrine and Covenants", "Pearl of Great Price"]
chosen = volumes[choice]
# print(chosen)

with open("books_and_chapters.txt") as scrip:
    for line in scrip:

        bk_list = line.strip().split(":")

        division = bk_list[2]
        chpt = int(bk_list[1])
        book = bk_list[0]

        if division == chosen:

            print(f'Scripture: {division}, Book: {book}, Chapters: {chpt} ')
            if chpt > max_chpt:
                max_chpt = chpt
                max_book = book
                max_div = division

print(f'\nThe book with the largest number of chapters is:')
if choice == 3:
    print(f'The {max_book} itself, with {max_chpt} sections. ')
else:
    print(f'{max_book}, with {max_chpt} chapters in the {max_div}. ')
