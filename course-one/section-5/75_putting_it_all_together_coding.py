def func(a, b, *args):
    print(a, b, args)

func(1, 2, 'x', 'y', 'z')

def func(a, b=2, *args, c=3, d):
    print(a, b, args, c, d)

func(10, 20, 'x', 'y', 'z', c=4, d=1)
func(10, 20, 'x', 'y', 'z', d=10)
func(1, 'x', 'y', 'z', d=10)

def func(a, b, *args, c=10, d=20, **kwargs):
    print(a, b, args, c, d, kwargs)

func(1, 2, 'x', 'y', 'z', c=100, d=200, x=0.1, y=0.2)

help(print)

print(1, 2, 3, sep='-', end=" *** ")
print(1, 2, 3, sep='-')

def calc_hi_to_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = min(args) if len(args) > 0 else 0
    avg = (hi + lo) / 2
    if log_to_console:
        print("high={0}, low={1}, avg={2}".format(hi, lo, avg))
    return avg

avg = calc_hi_to_avg(1, 2, 3, 4, 5)
is_debug = True
avg = calc_hi_to_avg(1, 2, 3, 4, 5,log_to_console=is_debug)