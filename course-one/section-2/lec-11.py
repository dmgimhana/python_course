a = 10;
b = 2 ;

try:
    a/b
except ZeroDivisionError:
    print('Division by zero')
finally:
    print('This always executes')


print("test - 2")

# finally always executes even if there in a continue statement or break statement

x = 0;
y = 2;

while x < 4:
    print("-------------------")
    x += 1;
    y -= 1;

    try:
        x / y
    
    except ZeroDivisionError:
        print("{0},{1} -  division by 0".format(x, y))
        continue
    finally:
        print("{0},{1} -  always executes".format(x, y)) 

    print("{0},{1} -  main loop".format(x, y))


print("test - 3")

# finally always executes even if there in a continue statement or break statement

p = 0;
q = 2;

while p < 4:
    print("-------------------")
    p += 1;
    q -= 1;

    try:
        p / q
    
    except ZeroDivisionError:
        print("{0},{1} -  division by 0".format(p, q))
        break
    finally:
        print("{0},{1} -  always executes".format(p, q)) 

    print("{0},{1} -  main loop".format(p, q))

print("test - 4")

j = 0;
i = 10;

while j < 4:
    print("-------------------")
    j += 1;
    i -= 1;

    try:
        j / i
    
    except ZeroDivisionError:
        print("{0},{1} -  division by 0".format(j, i))
        break
    finally:
        print("{0},{1} -  always executes".format(j, i)) 

    print("{0},{1} -  main loop".format(j, i))

else:
    print("Code executed without a zero division error")