def add_item(name, quantity, unit, grocery_list):
    grocery_list.append("{0} ({1} {2})".format(name, quantity, unit))
    return grocery_list

store1 = []
store2 = []

add_item('banana', 2, 'units', store1)
add_item('milk', 1, 'liter', store1)
print(store1)

add_item('python', 1, 'medium-rare', store2)
print(store2)

print('################################################')

def add_item(name, quantity, unit, grocery_list = []):
    grocery_list.append("{0} ({1} {2})".format(name, quantity, unit))
    return grocery_list

del store1
del store2

store1 = add_item('banana', 2, 'units')
print(add_item('milk', 1, 'liter', store1))
print(store1)

store2 = add_item('python', 1, 'medium-rare')
print(store2)
print(store1)
print(store1 is store2)


def add_item(name, quantity, unit, grocery_list = None):
    if not grocery_list:
        grocery_list = []
    grocery_list.append("{0} ({1} {2})".format(name, quantity, unit))
    return grocery_list

store1 = add_item('banana', 2, 'units')
add_item('milk', 1, 'liter', store1)
print(store1)

store2 = add_item('python', 2, 'medium-rare')
add_item('milk', 1, 'liter', store2)
print(store2)

print(store1 is store2)

def factorial(n):
    if n < 1:
        return 1
    else:
        print('calculating {0}!'.format(n))
        return n * factorial(n - 1)
    
print(factorial(3))

print("$$$$$$$$$$$$$$$$$$$$$$$ MUTABLITY CAN SOMETIMES HELP US $$$$$$$$$$$$$$$$$$$$$$$")

print("######################################")
def factorial(n, *, cache):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorial(n - 1,cache=cache)
        cache[n] = result
        return result

cache = {}
factorial(3, cache=cache)
print("Print cache > ",cache)
factorial(3, cache=cache)
print("Print cache > ",cache)
factorial(4, cache=cache)
print("Print cache > ",cache)
print("######################################")
print("**************************************")
print('######################################')
def factorial(n,cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorial(n - 1,cache=cache)
        cache[n] = result
        return result

factorial(3)
print("Print cache > ",cache)
factorial(3)
print("Print cache > ",cache)
factorial(4)
print("Print cache > ",cache)
print("######################################")