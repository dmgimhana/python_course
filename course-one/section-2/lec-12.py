# In python, an iterable is an object capabale of returning values on at a time.

i = 0
while i < 5:
    print(i)
    i += 1

i = None

print("----------------------")

for i in range(5):
    print(i)

print("----------------------")

for i in range(1, 8):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
else:
    print('no multiple of 7 in the range ')

s = "hello"

print("--------------------")
for i in range(len(s)):
    print(i, s[i]);

    
print("--------------------")

v = "orange"

for i, c in enumerate(v):
    print(i, c)