# AoC: Day 17

import itertools

SIZE  = 150


with open("input") as f:
    lines = f.readlines()
    
elems = map(lambda x: int(x), lines)
count = 0

for i in range(0, len(elems) + 1):
    for subset in itertools.combinations(elems, i):
        if sum(list(subset)) == SIZE:
            count += 1

print count
    
    
