# dmmmy code
i = 100

#TODO: fix this function
# currently does nothing, but should do ....
def my_func(a: "mandatory positional", 
            b: "optional positional" = 1,
            c = 2,
            *args: "add extra positional here",
            kw1,
            kw2 = 100,
            kw3 = 200,
            **kwargs: "provide extra kw-only here") -> "does nothing":
    """This function does nothing but does have various parameters and annotations"""
    i = 10
    j = 20

print("####################")
print(my_func.__doc__)
print("####################")
print(my_func.__annotations__)
print("####################")

my_func.short_description = "this is a function that does nothing much"
print(my_func.short_description)

print("####################")
print(dir(my_func))
print("####################")

print(my_func.__name__)
print(id(my_func))

def func_call(f):
    print(id(f))
    print(f.__name__)

func_call(my_func)

print(my_func.__defaults__)
print(my_func.__kwdefaults__)
print(my_func.__code__)
print(dir(my_func.__code__))

print(my_func.__code__.co_name)
print(my_func.__code__.co_varnames)
print(my_func.__code__.co_argcount)

import inspect
from inspect import isfunction, ismethod, isroutine

a = 10

print(isfunction(a))
print(isfunction(my_func))
print(ismethod(my_func))

class MyClass:
    def f(self):
        pass


print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

print(isfunction(MyClass.f))
my_obj = MyClass()
print(isfunction(my_obj.f))
print(ismethod(my_obj.f))
print(isroutine(MyClass.f))
print(isroutine(my_obj.f))

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

print("#############################")

print(inspect.getsource(my_func))

print(inspect.getmodule(my_func))

print(inspect.getmodule(print))

import math

print(inspect.getmodule(math.sin))

print("###############################")
print(inspect.getcomments(my_func))
print("###############################")

print(my_func.__doc__)

print("###############################")

print(inspect.signature(my_func))

print(dir(inspect.signature(my_func)))

print("###############################")

print(my_func.__annotations__)

print(inspect.signature(my_func).return_annotation)

sig = inspect.signature(my_func)

print(sig)

print("#####################")

print(sig.parameters)

print("######################")

for k, v in sig.parameters.items():
    print(k, v)

print("######################")

for k, v in sig.parameters.items():
    print(k, type(v))

print("######################")

for k, v in sig.parameters.items():
    print(dir(v))

print("######################")

for k, param in sig.parameters.items():
    print('Key: ', k)
    print('Name: ', param.name)
    print('Default: ', param.default)
    print('Annotation: ', param.annotation)
    print('Kind: ', param.kind)
    print("--------------------")

print("######################### CLEANING THE ABOVE FUNCTION BIT MORE #########################")

for param in sig.parameters.values():
    print('Name: ', param.name)
    print('Default: ', param.default)
    print('Annotation: ', param.annotation)
    print('Kind: ', param.kind)
    print("--------------------")

print("************* POSTIONAL ONLY ARGUMENTS ********************")
print("POSITIONAL ONLY PARAMETERES CANNOT BE CREATED BY US. ONLY PYTHON CAN DO IT")

help(divmod)
print("--------------------------------------------")
print(divmod(4,3))

print("################################################")
for param in inspect.signature(divmod).parameters.values():
    print(param.kind)

