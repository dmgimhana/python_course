from html import escape

def html_escape(arg):
    return escape(str(arg))

def html_int(a):
    return '{0}(<li>{1}</li>)'.format(a, str(hex(a)))

def html_real(a):
    return '{0:.2f}'.format(round(a, 2))

def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')

def html_list(l):
    items = ('<li>{0}</li>'.format(html_escape(item)) for item in l)

    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(k, v) for k, v in d.item())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print(html_str("""
    this is a multi line string with special characters: 10 < 100
"""))

print(html_int(255))

print(html_escape(3+10j))

from decimal import Decimal

def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        return html_escape(arg)
    
print(htmlize(100))

print(htmlize("""Python 
              rocks!"""))

print(htmlize([1 , 2, 3]))

print(htmlize(["""Python rocks! 0 < 1""", (10, 20, 30), 100]))

print("######################################################")

def html_escape(arg):
    return escape(str(arg))

def html_int(a):
    return '{0}(<li>{1}</li>)'.format(a, str(hex(a)))

def html_real(a):
    return '{0:.2f}'.format(round(a, 2))

def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')

def html_list(l):
    items = ('<li>{0}</li>'.format(htmlize(item)) for item in l)

    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(html_escape(k), htmlize(v)) for k, v in d.item())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def html_set(arg):
    return html_list(arg)


def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    elif isinstance(arg, set):
        return html_set(arg)
    else:
        return html_escape(arg)
    

print(htmlize(["""Python rocks! 0 < 1""", (10, 20, 30), 100]))
print(htmlize({1,2,3}))

print("######################################################")

def htmlize(arg):
    registry = {
        object:html_escape,
        int:html_int,
        float: html_int,
        Decimal:html_int,
        str:html_str,
        list:html_list,
        tuple:html_list,
        set: html_set,
        dict:html_dict
    }

    fn = registry.get(type(arg), registry[object])

    return fn(arg)


print(htmlize(100))

print(htmlize([1,2,3]))

print("#####################################################")

def htmlize(arg):
    registry = {
        object:html_escape,
        int:html_int,
        float: html_real,
        Decimal:html_real,
        str:html_str,
        list:html_list,
        tuple:html_list,
        set: html_set,
        dict:html_dict
    }

    fn = registry.get(type(arg), registry[object])

    return fn(arg)


def singledispatch(fn):
    registry = {}

    registry[object] = fn

    def inner(arg):
        return registry[object](arg)
    
    return inner

@singledispatch
def htmlize(a):
    return escape(str(a))

print(htmlize('1 < 100'))

print("#####################################################")

def singledispatch(fn):
    registry = {}

    registry[object] = fn
    registry[int] = lambda a: '{0}(<li>{1}</li>)'.format(a, str(hex(a)))
    registry[str] = lambda s: escape(s).replace('\n', '<br/>\n')

    def inner(arg):
        f = registry.get(type(arg), registry[object])
        return f(arg)
    
    return inner

@singledispatch
def htmlize(a):
    return escape(str(a))

print(htmlize('1 < 100'))
print(htmlize(100))

print("#####################################################")

def singledispatch(fn):
    registry = {}

    registry[object] = fn

    def decorated(arg):
        f = registry.get(type(arg), registry[object])
        return f(arg)
    
    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner
    
    def dispatch(type_):
        return registry.get(type_, registry[object])

    decorated.register = register
    decorated.registry = registry
    decorated.dispatch = dispatch
    return decorated

@singledispatch
def htmlize(a):
    return escape(str(a))

print(htmlize('1 < 100'))
print(htmlize(100))

print("PRINT REGISTRY 1:",htmlize.registry)
print("PRINT DISPATCH 1:",htmlize.dispatch(int))

@htmlize.register(int)
def html_int(a):
    return '{0}(<li>{1}</li>)'.format(a, str(hex(a)))

print(html_int)
print(htmlize(100))

print("PRINT REGISTRY 2:",htmlize.registry)
print("PRINT DISPATCH 2:",htmlize.dispatch(int))

@htmlize.register(list)
def html_list(l):
    items = ('<li>{0}</li>'.format(htmlize(item)) for item in l)

    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# long form of the above decoration
# html_list = htmlize.register(list)(html_list)

# stacking decorators
@htmlize.register(tuple)
@htmlize.register(list)
def html_sequence(l):
    items = ('<li>{0}</li>'.format(htmlize(item)) for item in l)

    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


print("PRINT REGISTRY 3:",htmlize.registry)
print("PRINT DISPATCH 3:",htmlize.dispatch(tuple))

print(htmlize([1, 2, 3]))
print(htmlize((1, 2, 3)))
print(htmlize(100))
print(htmlize(True))

print("#####################################")

from numbers import Integral

class Person:
    pass

class Student(Person):
    pass

p = Student()

print(type(p))

print(isinstance(p, Student))

print(isinstance(p, Person))

print("################ PLACES WHERE THIS FAILS #####################")

@singledispatch
def htmlize(a):
    return escape(str(a))

@htmlize.register(Integral)
def html_integral_number(a):
    return '{0}(<li>{1}</li>)'.format(a, str(hex(a)))

print(isinstance(True, Integral))

print(htmlize(10))

@htmlize.register(int)
@htmlize.register(bool)
def html_integral_number(a):
    return '{0}(<li>{1}</li>)'.format(a, str(hex(a)))


print(htmlize(10))

print(htmlize(True))

from collections.abc import Sequence

print(isinstance([1,2,3], Sequence))

print(isinstance((1, 2,3 ), Sequence))

@htmlize.register(Sequence)
def html_sequence(l):
    items = ('<li>{0}</li>'.format(htmlize(item)) for item in l)

    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print(type([1,2,3]) is Sequence)