import functions

functions.startup()

print('Menu')
print('1. New account')
print('2. Login')

ch = int(input('Enter your choice: '))

if ch == 1:
    functions.newacc()

if ch == 2:
    functions.login()