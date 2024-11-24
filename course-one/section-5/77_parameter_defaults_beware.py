from datetime import datetime
print(datetime.utcnow())
print(datetime.utcnow())


def log(msg, *, dt=datetime.utcnow()):
    print('{0}: {1}'.format(dt, msg))


log('message 1', dt='2010-01-01 00:00:00.000')
log('message 2')
log('message 3')
log('message 4')
log('message 5')

# And as you can see, no time has elapsed.Write the date and time is still the same.And it doesn't matter how many times I call this, it will still remain the same.Right.And the reason for that is, as we discussed in the lecture, is that this date time dot UTC now is evaluated when Def is run. At this point here, the function wasn't executed, the function was created and the default value was also created at that time. So it will never change throughout the lifetime of this.

def log1(msg, *, dt=None):
    if not dt:
        dt = datetime.utcnow()
    print('{0}: {1}'.format(dt, msg))

log1('message 6', dt='2010-01-01')
log1('message 7')
log1('message 8')

def log2(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    print('{0}: {1}'.format(dt, msg))

log2('message 9', dt='2010-01-01')
log2('message 10')
log2('message 11')
log2('message 12', dt=None)


# Be careful when using mutable types like below
print("##################################")
my_list = [1, 2, 3]
def func(a = my_list):
    print(a)
func()
func(['a', 'b'])
my_list.append(4)
print(my_list)
func()
print("##################################")

# To avoid the above better if we can use a tuple

print("##################################")
my_list = (1,2,3)
def func(a = my_list):
    print(a)
func()
func(['a', 'b'])
# my_list.append(4) this is not allowed
print(my_list)
func()
print("##################################")