def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elasped = end - start
        print('Run time: {0:.6f}s'.format(elasped))
        return result
    return inner

def calc_recursive_fib(n):
    return 1 if n < 3 else calc_recursive_fib(n - 2) + calc_recursive_fib(n - 1)

@timed
def fib(n):
    return calc_recursive_fib(n)

print(fib(20))

print('#################################')

def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += end - start

        avg_run_time = total_elapsed / 10
        print('Avg Run time: {0:.6f}s'.format(avg_run_time))
        return result
    return inner

def fib(n):
    return calc_recursive_fib(n)

fib = timed(fib)
print(fib(28))

print('#################################')

def timed(fn,reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += end - start

        avg_run_time = total_elapsed / reps
        print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
        return result
    return inner

def fib(n):
    return calc_recursive_fib(n)

fib = timed(fib, 5)
print(fib(28))

print("###################################################")

def dec(fn):
    print("running dec")

    def inner(*args, **kwargs):
        print("running inner")
        return fn(*args, **kwargs)
    
    return inner

@dec
def my_func():
    print("running my_func")

my_func()
print('**************')
my_func = dec(my_func)
print('**************')
my_func()

print('############### CREATING A DECORATOR FACTORY SO THAT WE CAN USE THE @ syntax with parameters ##################')

def dec_factory():
    print('running dec_factory')

    def dec(fn):
        print("running dec")

        def inner(*args, **kwargs):
            print("running inner")
            return fn(*args, **kwargs)
    
        return inner
    return dec

@dec
def my_func():
    print('running my_func')

my_func()

print('***********************')

@dec_factory()
def my_func():
    print('running my_func')


def my_func():
    print('running my_func')

my_func = dec_factory()(my_func)
my_func()

print('*****************************')

def dec_factory(a , b):
    print('running dec_factory')

    def dec(fn):
        print("running dec")

        def inner(*args, **kwargs):
            print("running inner")
            print('a={0}, b={1}'.format(a, b))
            return fn(*args, **kwargs)
    
        return inner
    return dec

dec = dec_factory(10, 20)

@dec
def my_func():
    print('running my_func')

my_func()

print('**********************')

@dec_factory(100, 200)
def my_func():
    print('running my_func')

print('^^^^^^^^^^^')
my_func()

def my_func():
    print("running my_func")

print("****")

my_func = dec_factory(150, 250)(my_func)

print('$$$$')

my_func()

print('#####################################')
def dec_factory(reps):
    def timed(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += end - start

            avg_run_time = total_elapsed / reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
            return result
        return inner
    return timed

@dec_factory(5)
def fib(n):
    return calc_recursive_fib(n)

fib(28)

@dec_factory(15)
def fib(n):
    return calc_recursive_fib(n)

fib(28)

print("*************CLEANING UP THE DECORATOR FACTORY***************")

def time(reps):
    def dec(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += end - start

            avg_run_time = total_elapsed / reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
            return result
        return inner
    return dec

@timed(15)
def fib(n):
    return calc_recursive_fib(n)

fib(28)