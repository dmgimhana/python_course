i = 2;

while i < 5:
    print(i)
    i += 1

j = 0;

while True:
    print(j)
    if j >= 5:
        break
    else:
        j += 1

min_length = 2

while True:
    name = input("Please enter your name: ")
    if(len(name) >= min_length and name.isprintable() and name.isalpha()):
        break

print("Hello, {0}".format(name))


# continue statement
a = 0

while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print("value of a is ", a);


# using a flag
l = [1,2,3]
val = 10

found = False

idx = 0

while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1

if not found:
    l.append(val)

print(l)


# not using a flag, using an else statement in while

p = [1,2,3,10]

value = 10
index = 0

while index < len(p):
    if p[index] == val:
        break
    index += 1

else:
    p.append(value)

print(p)