a, *b = [-10, 5, 2, 100]
print(a, b)

a, *b = (-10, 5, 2, 100)
print(a, b)

a, *b = 'XYZ'
print(a, b)

a, b, *c = 1,2,3,4,5
print(a, b, c)

a, b, *c, d = [1,2,3,4,5]
print(a,b,c,d)

a, *b, c, d = 'Python'
print(a,b,c,d)

l1 = [1,2,3]
l2 = [4,5,6]
l3 = [*l1, *l2]
print(l3)

l1 = [1,2,3]
l2 = 'XYZ'
l3 = [*l1, *l2]
print(l3)

# Types like sets and dictionaries have no ordering
# Sets and dicionaries keys are still iterable, but iteration has no guarantee of preserving the order in which the elements were created/ added

# But, the * operator still works, since it works with any iterable
s = {10,-99,3,'d'}

# In practice, we rarely unpack sets and dictionaries directly in this way
a, *b, c = s
print(a, b, c)

d1 = {'p':1, 'y':2}
d2 = {'t':3, 'h':4}
d3 = {'h':5, 'o':6, 'n':7}

# the resulting list or sets does not guarante order
l = [*d1, *d2, *d3]
s = {*d1, *d2, *d3}

print(l)
print(s)

print('############ UNPACKING KEY-VALUE PAIRS IN DICTIONARIES #################')
d1 = {'p':1, 'y':2}
d2 = {'t':3, 'h':4}
d3 = {'h':5, 'o':6, 'n':7}

# Note that the key 'h' is in both d2 and d3
# Also not that the ** operator cannot be used in the LHS of an assignment
d = {**d1, **d2, **d3}
print(d)
# Since d3 got merged last its 'h':5 value is retained

d1 = {'a':1, 'b':2}
print({'a':10, 'c':3, **d1})
print({**d1,'a':10, 'c':3})

# Nested Unpacking
l = [1, 2, [3, 4]]
a, b , c = l
print(a, b, c)
a, b, (c, d) = [1, 2, [3,4]]
print(a, b, c, d)
a, *b, (c, d, e) = [1, 2, 3, 'XYZ']
print(a, b, c, d, e)

a, *b, (c, *d) = [1,2,3,'python']
print(a, b, c, d)