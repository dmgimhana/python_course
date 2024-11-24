print('a' or [1,2])
print('' or [1,2])
print(1 or 2/3)

s1 = None
s2 = ''
s3 = 'abc'

s1 = s1 or 'n/a'
s2 = s2 or 'n/a'
s3 = s3 or 'n/a'

print(s1, s2, s3)

print([] or [0])

print(None and 100)

a = 2
b = 4

if(b == 0):
    print(0)
else:
    print(a/b)



a = 2
b = 4

print(b and a/b)


s1 = None
s2 = ''
s3 = 'abc'

print(s1 and s1[0])
print(s2 and s2[0])
print(s3 and s3[0])
print("##########################")
print((s1 and s1[0]) or 'n/a')
print((s2 and s2[0]) or 'n/a')
print((s3 and s3[0]) or 'n/a')

# Not operator is not a part of bool class

print(not True)
print(not False)
print(bool('abc'))
print(bool(''))
print(not bool('abc'))
print(not bool(''))

print('################################')
# Below code. Python will go in and actually apply the bool and look at the truth value of abc and it will then do a NOT of that truth value and return the boolean.
print(not 'abc')
print('################################')

print(type(not 'abc'))
print(bool(None))
print(not None)