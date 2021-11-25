
accounts = []
balances = []

new_one = ''
new_money = ''
change_index = 0
t_bal = 0.0
a_bal = 0.0

print('\nEnter the names and balances of bank accounts. (type "quit" when done) ')
while new_one != 'quit':
    new_one = input('What is the account name? ')
    if new_one == 'quit':
        pass
    else:
        new_money = float(input('What is the account balance($)? '))
        accounts.append(new_one)
        balances.append(new_money)
        # t_bal += new_money
        # print(t_bal)

print('\nAccount information: ')
for i in range(len(accounts)):
    print(f'[{i+1}] {accounts[i]} - ${balances[i]:.2f}')

while change_index >= 0:
    change_index = int(
        input('\nWhat Account Balance would you like to UPDATE? (type the item# or 0 for nothing) '))-1
    if change_index < 0:
        pass
    else:
        balances[change_index] = float(input('What is the new balance? '))
        print()
        print('Account Information: ')
        for i in range(len(accounts)):
            print(f'[{i+1}] {accounts[i]} - ${balances[i]:.2f}')


# comput the total and average
t_bal = sum(balances)
a_bal = t_bal/len(balances)

# print('\n\n')
# print(t_bal)
# print(a_bal)
print()
print('Account Information: ')
for i in range(len(accounts)):
    print(f'[{i+1}] {accounts[i]} - ${balances[i]:.2f}')
print()
print(f'Total: ${t_bal:.2f} ')
print(f'Average: ${a_bal:.2f} ')


biggest = max(balances)
index = balances.index(biggest)


print(f'The [{index+1}] {accounts[index]} account has the largest balance. ')

print()
