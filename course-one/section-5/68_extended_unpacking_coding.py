# the below syntax works with only iterables that are indexable. Below way of unpacking is called slicing
l = [1,2,3,4,5,6]
a = l[0]
b = l[1:]
print(a)
print(b)

# the below syntax works with only iterables that are indexable. Below way of unpacking is called slicing
a, b = l[0], l[1:]
print(a)
print(b)

# # Below will not work, because sets are not indexable
# s = {1, 2, 3}
# a = s[0]
# b = s[1:]

# Below way of unpacking is called stared unpacking or extended unpacking
a, *b = l
print(a)
print(b)

s = 'Python'
a, *b = s
print(a)
print(b)

t = ('a', 'b', 'c')
a, *b = t
print(a)
print(b)

# Above we unpacked to a tuple(because it was of syntax a, (the comma is what makes it a tuple)). However we can also unpack to a list as well

[a, b, c] = "XYZ"
print(a)
print(b)
print(c)

print("#######################")

s = 'Python'
a, b, *c, d = s
print(a)
print(b)
print(c)
print(d)

print("#######################")

a, b, c, d = s[0], s[1], s[2:-1], s[-1]
print(a)
print(b)
print(c)
print(d)

print("#######################")

a, b, c, d = s[0], s[1], s[2:-1], s[-1]
*c, = c
print(a)
print(b)
print(c)
print(d)

print("#######################")

a, b, c, d = s[0], s[1], s[2:-1], s[-1]

print(a)
print(b)
print(list(c))
print(d)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]
print(l)

l1 = [1, 2, 3]
s = 'abc'
print([*l1,*s])

l1 = [1, 2, 3]
s = {'x', 'y', 'z'}
print([*l1,*s])

s1 = 'abc'
s2 = 'cde'
print([*s1, *s2])

print({*s1, *s2})

s = "Python"

for c in s:
    print(c)

a, b, c, *d = s
print(a, b, c, d)

s = {'d', 10, 3, -99}
print(list(s))
*q, = s
print(q)

s1 = {1, 2, 3}
s2 = {3, 4, 5}

c = {*s1, *s2}
print(c)

help(set)

print(s1.union(s2))

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s4 = {7, 8, 9}

print(s1.union(s2).union(s3).union(s4))
print(s1.union(s2,s3,s4))
print([*s1, *s2, *s3, *s4])
print({*s1, *s2, *s3, *s4})

d1 = {'key1':1, 'key2':2}
d2 = {'key2':3, 'key4':4}

print({*d1, *d2})
# double star only works with dictionaries
print({**d1, **d2})
print({**d2, **d1})
print({'key1':1, 'key2':2, 'key4':4})
print({'a':1, 'b':2, **d1, 'c':3})
a, b, c = [1,2,'XY']
print(a, b, c)
print("#############################################")
a , b, (c, d) = [1, 2, 'XY']
print(a, b, c, d)
print("#############################################")
a, b, (c, d, *e) = [1, 2, 'Python']
print(a, b, c, d, e)

l = [1, 2, 3, 4, "Python"]
a, *b, (c, d, *e) = l
print(a, b, c, d, e)

# Using slicing
a , b, c, d ,e = l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])
print(a, b, c, d, e)

print("*************************************")

l = (1, 2, 3, 4, ['a', 'b', 'c', 'd'])

a, *b, (c, d, *e) = l
print(a, b, c, d, e)

print("*************************************")

a, b, c, d, e = l[0], list(l[1:-1]), l[-1][0], l[-1][1], list(l[-1][2:])
print(a, b, c, d, e)