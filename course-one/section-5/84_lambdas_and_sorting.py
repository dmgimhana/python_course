help(sorted)

l = [1, 5, 4, 10, 9, 6]

print(sorted(l))
print(l)

help(ord)

l = ['c', 'B', 'D', 'a']

print(sorted(l))

print(ord('a'))

print(ord('A'))

print(sorted(l, key=lambda s: s.upper()))

d = {'abc':200,'def':300,'ghi':100}

for e in d:
    print(e)

print(sorted(d))

print(sorted(d, key=lambda e: d[e]))

def dist_sq(x):
    return (x.real)**2 + (x.imag)**2

print(dist_sq(1+1j))

l = [3+3j, 1-1j, 0, 3+0j]

# print(sorted(l)) Not going to work

print(sorted(l, key=dist_sq))

print(sorted(l, key=lambda x: (x.real)** 2 + (x.imag)** 2))

l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']
print(sorted(l))

print("####################### Sorting a string of list using the last characters #######################")
print(sorted(l, key=lambda s: s[-1]))

l = ['Idle','Cleese', 'Palin', 'Chapman', 'Gilliam', 'Jones']
print(sorted(l, key=lambda s: s[-1]))

print('#############################################################################')