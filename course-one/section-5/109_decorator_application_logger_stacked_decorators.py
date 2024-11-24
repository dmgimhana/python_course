def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0}: called {1}'.format(run_dt, fn.__name__))
        return result
    
    return inner

@logged
def func_1():
    pass

@logged
def func_2():
    pass

func_1()

func_2()

def timed(fn):
    from time import perf_counter
    from functools import wraps

    wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__, args_str, elapsed))

        return result
    
    return inner

print('#################################')

@logged
@timed
def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1))

print(fact(3))

print(fact(5))

# The above is equivalent to the fallowing

fact = logged(timed(fact))

print(fact(3))

print(fact(5))

def dec_1(fn):
    def inner():
        print('Running dec_1')
        return fn()
    return inner

def dec_2(fn):
    def inner():
        print("Running dec_2")
        return fn()
    return inner

@dec_1
@dec_2
def my_func():
    print('Running my_func')

# The above is equivalent to fallowing
    
# my_func = dec_1(dec_2(my_func))

my_func()