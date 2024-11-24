# args is used to scoop up variable amount of remaning positional arguments. The parameter name args is arbitary - * is the real performer here. This returns a tuple

# **kwargs is used to scoop up a variable amount of remaining keyword arguments. The parameter name kwargs is arbitrary - ** is the real performer here. This returns a dictionary

# **kwargs can be specified even if the positional arguments have not been axhausted(unlike keyword-only arguments)

# No parameter can come after **kwargs

# * indicated there is no positional arguments here after

def func(**others):
    print(others)

func(a = 1, b = 2, c = 3)

def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, x = 100, y = 200)

def func(a, b, *, d, **kwargs):
    print(a)
    print(b)
    print(d)
    print(kwargs)

func(1, 2, x = 100, y = 200, d = 20)

def func(a, b, **kwargs):
    print(a)
    print(b)
    print(kwargs)

func(1, 2, x = 100, y = 200)