# The floats uses a fixed number of bytes -> 8 bytes(64 bits)
# but python objects have some overhead too. Meaning to create an float object it actually uses 24 bytes.
# The 64 bits are used up as fallows:
    # sign -> 1 bit
    # exponent -> 11 bits
    # significant digits -> 52 bits -> 15 - 17 significant (base-10) digits

# Significant digits are all digits except leading and trailing zeros

# The fallowing numbers all have the same significant digits 
# 1.2345 1234.5 1234500000 0.00012345 12345e-50 1.2345e10

# The same problem that occurs when trying to represent 1/3 using a decimal expansion also happens when trying to represent certain numbers using a binary expansion

# 0.1 = 1/10 have an exact representation in decimal but not in binary

# -------------------------

# So, some numbers that do have a finite decimal representation, do not have a finite binary representation, and some do

# Examples for finite representation(Meaning we have an exact float) ->
#  (0.75) base 10 = (0.11) base 2
#  (0.8125) base 10 = (0.1101) base 2

# Examples for infinte representation
# (0.1) base 10 = (0 0011 0011 0011...) base 2 -> approximate float representation