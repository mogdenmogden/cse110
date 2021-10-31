# calculate loan decision
print('Let\'s decide whether you will get your loan.')
print('Enter integers on a scale of 1 to 10 in response to the questions below.')

size = int(input('How large is the loan? 1 is Tiny, 10 is Huge \n'))
print()
credit = int(
    input('How good is your credit history? 1 is Very very Bad, 10 is Perfect \n'))
print()
income = int(input('How high is your income? 1 is None, 10 is Huge \n'))
print()
downpayment = int(
    input('How large is your down payment? 1 is None, 10 is Huge \n'))
print()
# point = 0
if size >= 5:
    # point = 1
    if credit >= 7 and income >= 7:
        # point = 2
        decision = True
    elif credit >= 7 or income >= 7:
        # point = 3
        if downpayment >= 5:
            # point = 4
            decision = True
        else:
            # point = 5
            decision = False
    else:
        # point = 6
        decision = False
else:
    # point = 7
    if credit < 4:
        # point = 8
        decision = False
    else:
        # point = 9
        if income >= 7 or downpayment >= 7:
            # point = 10
            decision = True
        elif income >= 4 and downpayment >= 4:
            # point = 11
            decision = True
        else:
            # point = 12
            decision = False

# Render the decision
print()
# print(point)
# print(decision)
# print()
print(f'After carefully considering your ability to repay the loan, we have decided...')
if decision:
    print('...to give you the loan.  Congratulations!')
else:
    print('...to deny you the loan at this time.  Better luck next time.')
print()
