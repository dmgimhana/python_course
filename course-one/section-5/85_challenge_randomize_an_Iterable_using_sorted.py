import random

l = [1, 5, 4, 10, 9, 6]

print(sorted(l, key=lambda e: random.random()))