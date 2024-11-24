def outer_func():
    x = 'hello'
    def inner_func():
        print(x)
    inner_func()

outer_func()

print("1###############################")

def outer_func():
    x = "hello"
    def inner1():
        def inner2():
            print(x)
        inner2()
    inner1()

outer_func()

print("2###############################")

def outer_func():
    x = 'hello'
    def inner():
        x = 'python'
        print('inner:', x)
    inner()
    print('outer: ',x )

outer_func()

print("3###############################")

def outer_func():
    x = 'hello'
    def inner():
        nonlocal x
        x = 'python'
        print('inner:', x)
    print('outer(before)', x)
    inner()
    print('outer(after): ',x )

outer_func()

print("4###############################")

def outer():
    x = "hello"
    def inner1():
        def inner2():
            nonlocal x
            x = 'python'
        inner2()
    inner1()
    print(x)

outer()

print("5###############################")

def outer():
    x = "hello"
    def inner1():
        nonlocal x
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        inner2()
    inner1()
    print(x)

outer()

print("6###############################")

x = "python"

# def outer():
#     global x
#     x = 'monty'
    
#     def inner():
#         nonlocal x
#         x = 'hello'
#     inner()
#     print(x)
# the above won't work because there is no binding for x

def outer():
    x = 'monty'

    def inner():
        nonlocal x
        x = 'hello'

    inner()
    print(x)

outer()

print(x)

print("7###############################")

def outer():
    global x
    x = 'monty'

    def inner():
        global x
        x = 'hello'

    inner()
    print(x)

outer()

print(x)



