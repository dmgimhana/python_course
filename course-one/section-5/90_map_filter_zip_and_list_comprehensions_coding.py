def fact(n):
    return 1 if n < 2 else n * fact(n - 1)

print(fact(3))
print(fact(4))

results = map(fact, range(6))

print(results)

# Here the results object is a generator. The call calculations. The calculation is not done ahead of time

for x in results:
    print(x)

# Once you

for x in results:
    print(x)


results1 = list(map(fact, range(6)))
print(results1)

l1 = [1,2,3,4,5]
l2 = [10,20,30]
l3 = [100,200,300,400]

results = list(map(lambda x, y, z: x + y + z, l1, l2, l3))

print(results)

results = map(lambda x, y: x + y, l1, l2, l3)

print(results)

# The below code will not work because of the below given reason
# for x in results:
#     print(x)

# But you'll notice we didn't get the error until we actually started the iteration.Why? Because again, it doesn't actually make the calculation right away.It defers that until you actually request items from that new iterable.And this is why the error doesn't show up until this point here.

x = range(25)

print(x)

for i in x:
    print(i)

for i in x:
    print(i)


print(list(filter(lambda x: x % 3 == 0, range(25))))

print(list(filter(None, [1, 0, 4, 'a', '', None, True, False])))

l1 = [1 , 2, 3, 4]
l2 = [10,20,30,40]
l3 = 'python'

results = zip(l1, l2, l3)

for x in results:
    print(x)

for x in results:
    print(x)

# Well in above loop, again, zip differs the calculation until you request it.But it's a generator.It's not a list, which means that once you've exhausted this generator, you're done.You can't go back.If you want to be able to go back, then you should put it into a list.

print("######################################")
    
results = list(zip(l1, l2, l3))

for x in results:
    print(x)

for x in results:
    print(x)

print("######################################")

print(list(zip(range(10000), 'python')))

l = range(10)

print(list(l))

print(list(map(fact, l)))

results = [fact(n) for n in range(10)]

print(results)

print("#########################")

results = (fact(n) for n in range(10))

print(results)

for x in results:
    print(x)

for x in results:
    print(x)


print("#########################")

results = list((fact(n) for n in range(10)))

print(results)

results = [fact(n) for n in range(10)]

print(results)

print("**********************************")

l1 = [1,2,3,4,5,6]
l2 = [10, 20, 30, 40]

print(list(map(lambda x, y: x + y, l1, l2)))

print([x + y for x, y in zip(l1, l2)])

print(list(filter(lambda x: x % 2 == 0, map(lambda x, y: x + y, l1, l2))))

print([x + y for x, y in zip(l1,l2) if (x+y) % 2 == 0])

# change the above code to a generator, which means it does not calculate everything until you request it. To request you can call in the list function, that is what i have done in the last print statement. list function will iterate through all the elements in the generator

print((x + y for x, y in zip(l1,l2) if (x+y) % 2 == 0))

list1 = (x + y for x, y in zip(l1,l2) if (x+y) % 2 == 0)

print(list(list1))
