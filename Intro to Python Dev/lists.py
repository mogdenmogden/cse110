# blank list variable
clients = []  # preferred method
clients = list()  # less preferred b/c list is also a keyword
# good to make list variables plural nouns so readers recognize the potential for multiple values in the list

clients = []

clients.append("Emily")  # adds emily to the end of the list
clients.append("John")
clients.append("Mary")

# will print each item in the list. "client" is a random name you choose to give each element in the list. can be anything
for client in clients:
    print(client)

new_client = input("what is the neame of a client? ")
clients.append(new_client)

for client in clients:
    print(client)


print()
print()
clients = []
new_client = ''
# add many values
while new_client != 'quit':
    new_client = input("what is the neame of a client? ")
    if new_client == 'quit':
        pass
    else:
        clients.append(new_client)
for client in clients:
    print(client)
