# create the list variable
numbers = []

user_numb = -1

# ask user for a series of numbers
while user_numb != 0:
    user_numb = float(input(
        'Enter a number, positive or negative.  Type "0" when you want to stop. '))
    #print(f'you entered {user_numb} ')
    if user_numb == 0:
        pass
    else:
        user_numb = user_numb
        numbers.append(user_numb)

# find the total
total = 0

for nbr in numbers:
    total += nbr

print(f'\nYour total is {total}. ')

# count the number of things in the list
list_items = len(numbers)
# print(list_items)

# find the average
avg_numb = total/list_items
print(f'The average is : {avg_numb}. ')

# max value
the_max = max(numbers)
print(f'The biggest number is: {the_max}. ')

# the smallest non-negative number
smallest = max(numbers)
for nbr in numbers:
    if nbr > 0 and nbr < smallest:
        smallest = nbr
    else:
        pass

print(f'The smallest positive number is: {smallest:.3f}. ')

print(f'This is your list sorted in ascending order. ')
numbers.sort()
for nbr in numbers:
    print(nbr)

print(f'This is your list sorted in descending order. ')
numbers.sort(reverse=True)
for nbr in numbers:
    print(nbr)


print('\ndone\n')
