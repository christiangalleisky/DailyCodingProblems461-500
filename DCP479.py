from itertools import permutations

u = [1,2,3]

x = permutations(u, len(u))
for y in list(x):
    print(y)