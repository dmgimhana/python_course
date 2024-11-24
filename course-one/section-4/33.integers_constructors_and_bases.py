print(type(10))
# help command will give you the internal documentation
help(int)
# The decimal potion gets truncated
print(int(10.5))
print(int(10.999))


print(int(True))
print(int(False))

import fractions
a = fractions.Fraction(22/7)
print(float(a))
print(int(a))

print(int("12345"))
# base 2
print(int("101",2))
# base 16
print(int("FF",16))
# base 16
print(int("ff",16))

# Built in methods for different base representations
print(bin(10))
print(oct(10))
print(hex(10))

a = int('101',2)
b = 0b101

print(a)
print(b)

# Let's write a function to get the provided base representation of a base 10 number
# First function variation
def from_base10VerstionOne(n, b):
    if n < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        m = n % b
        n = n // b
        digits.insert(0, m)
    return digits

# Second function variation
def from_base10VerstionTwo(n, b):
    if n < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        m, n = n % b, n // b
        digits.insert(0, m)
    return digits

# Third function variation
def from_base10VerstionThree(n, b):
    if n < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        n, m = divmod(n,b)
        digits.insert(0, m)
    return digits

print(from_base10VerstionThree(10,2))
print(from_base10VerstionThree(255,16))

# Let's create an encoding fuction for the above output
# Encoding function one
def encodeVersionOne(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode the digits")
    encoding = ''
    for d in digits:
        encoding += digit_map[d]
    return encoding

print(encodeVersionOne([15,15], '0123456789ABCDEF'))

# Encoding function two
def encodeVersionTwo(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode the digits")
    return ''.join([digit_map[d] for d in digits])

print(encodeVersionTwo([15,15], '0123456789ABCDEF'))

def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError('Invalid base: 2 <= base <= 36')
    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10VerstionThree(number, base)
    encoding = encodeVersionTwo(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding

e = rebase_from10(314,2)
print(e)
print(int(e,base = 2))

e = rebase_from10(3451, 16)
print(e)
print(int(e, base = 16))

e = rebase_from10(-314,2)
print(e)
print(int(e,base = 2))

e = rebase_from10(-3451, 16)
print(e)
print(int(e, base = 16))

