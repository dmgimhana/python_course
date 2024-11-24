# print(help(bool))
print(issubclass(bool, int))

# bool is a subclass of int

print('############# PRINTING TYPE, MEMORY ADDRESS, INT VALUE OF TRUE')
print(type(True),id(True), int(True) )

print('############# PRINTING TYPE, MEMORY ADDRESS, INT VALUE OF FALSE')
print(type(False),id(False), int(False) )

print(3 < 4)
print(type(3 < 4))
print(id(3 < 4))

print((3 < 4) == True)
print((3 < 4) is True)
print(None is False)

print((1 == 2) == False)
print(1 == 2 == False)
print(1 == 2 and 2 == False)
print(int(True), int(False))
print(1 + True)
print(100 * False)
print(True > False)
print((True + True + True) % 2 )
print(-True)

print(True and False)
print(True or False)

print(bool(0))
print(bool(1))
print(int(True))
print(bool(True))
print(bool(False))
print(bool(100))
print(bool(-1))
print(bool(0))