friends = ["Luke", "Mari", "Rex"]
tips = [12.25, 13.95, 8.50]

# typically not good to mix numbers and strings in a list.
# recommend keeping it to one type of data

# total tips
# loop through the list and add each iteration to a new variable

running_total = 0
for tip_amount in tips:
    #running_total = running_total + tip_amount
    running_total += tip_amount  # shorthand for the above
    print(running_total)

print(f'\nThe total is: ${running_total:.2f}. ')
