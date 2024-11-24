a = 10
def my_func(n):
    c = n ** 2
    return c

def my_func(n):
    print('global a:',a)
    c = a ** n
    return c

print(my_func(2))

def my_func(n):
    a = 20
    c = a ** n
    return c

print(a)

print(my_func(2))

print(a)

def my_func(n):
    global a
    a = 20
    c = a ** n
    return c

print(a)

print(my_func(2))

print(a)

def my_func():
    global var
    var =  'hello world'
    return

# print(var) This will error out because the var is not defined

my_func() # running this function will create a variable called var in the global scope. So the below print statement will work.

print(var)

print('##############################################')

a = 10

def my_func():
    global a
    a = 'hello'
    print('global a: ',a)

my_func()

print(a)

a = 10

def my_func():
    print('global a:', a)
    a = 'hello world'
    print(a)

# my_func() This will error out because as soon as you make an assignment you are effective putting the 'a' variable to local scope
    

f = lambda n: print(a ** n)

f(2)

print(True)

def print(x):
    return 'hello {0}'.format(x)

print('world')

del print

print('world')