print(True or True and False)
print(True or (True and False))
print((True or True) and False)

a = 10
b = 2

if a / b > 2:
    print('a is at least twice b')


a = 10
b = 0
    
if b > 0 and a / b > 2:
    print('a is at least twice b')

if b and a / b > 2:
    print('a is at least twice b')


import string

# help(string)

a = 'c'
print(a in string.ascii_uppercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.ascii_letters)

name = None
if name and name[0] in string.digits:
    print("Name cannt start with a digits")

name2 = '1abc'
if name2 and name2[0] in string.digits:
    print("Name cannt start with a digits")
