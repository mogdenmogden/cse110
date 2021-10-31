age = int(input('How old are you? (Tell the truth.) '))
age = age+1
print('Next year you will be '+str(age)+'. ')


cartons = int(input('How many egg cartons do you have? (The 12 count kind.) '))
eggs = cartons*12
print('You can store up to '+str(eggs)+' eggs. ')
##print('How wonderful! ')

cookies = float(input('How many cookies are in your bag? '))
people = float(input('How many people are here with you? '))
portion = cookies/people
print('Each person can have '+str(portion)+' cookies. ')
