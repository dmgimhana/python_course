def func(a, b, c):
    print(a, b, c)

func(1, 2, 3)

func(1, c = 3, b = 2)

func(c = 3, b = 2, a = 1)

def func1(a, b, *args):
    print(a, b, args)

func1(1, 2, 3, 4)

def func1(a, b, *args, d):
    print(a, b, args, d)

func1(1, 2, 3, 4, d = 5)

def func1(*args, d):
    print(args, d)

func1(1, 2, 3, d='a')
func1(d='a')

def func(*, d):
    print(d)

func(d = 100)

def func(a, b, *, d):
    print(a, b, d)

func(1, 2, d=4)

def func(a, b = 2, *args, d):
    print(a, b, args, d)

func(1, 5, 3, 4, d='a')

def func(a, b = 20 , *args, d = 0, e):
    print(a, b, args, d, e)

func(5, 4, 3, 2, 1, e = "all engines running")

func(0, 600, d = "good morning", e = "Python")

func(11, "m/s", 24, 'mph', d='unladen', e='swallow')

# So, so far we've seen how to create positional arguments, how to have optional positional arguments by specifying basically a default value. We've looked at how to scoop up extra positional arguments. So in any number of variable number of them using the star args approach, we've seen how to stop taking in extra positional arguments using the star just by itself. And that also allowed us to specify functions where we didn't have any positional arguments. And then we saw how to specify keyword arguments and keyword arguments that became either mandatory or optional depending on whether they had a default value or not.