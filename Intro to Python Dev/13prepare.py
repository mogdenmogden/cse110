def display_regular(input):
    reg_input = input
    return reg_input


def display_uppercase(input):
    upp_input = input.upper()
    return upp_input


def display_lowercase(input):
    low_input = input.lower()
    return low_input


prompt = input('Enter a message to display 3 ways: ')

reg = display_regular(prompt)

up = display_uppercase(prompt)

low = display_lowercase(prompt)

print(reg)
print(up)
print(low)

print('...and here is a bonus, a FOURTH way to display your message! ')


def display_proper(input):
    proper_input = input.title()
    return proper_input


proper = display_proper(prompt)
print(proper)
