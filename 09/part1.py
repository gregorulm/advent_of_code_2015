# AoC: Day 9
from itertools import permutations

with open("input") as f:
    lines = f.readlines()

distances = dict()

for line in lines:
    tmp = line.split()
    s   = tmp[0]
    t   = tmp[2]
    d   = int(tmp[4])

    if s in distances.keys():
        distances[s].append((t, d))
    else:
        distances[s] = [(t, d)]
        
    if t in distances.keys():
        distances[t].append((s, d))
    else:
        distances[t] = [(s, d)]
    

def cost(path):
    
    total = 0
    path  = list(path)
    
    while len(path) > 1:
        head         = path.pop(0)              
        destinations = distances[head]

        for (d, cost) in destinations:
            if d == path[0]:                
                total += cost
                break
        
    return total


# brute force
currentMin = 1000000000  # 'infinity'
minPath    = []

count = 0
for path in permutations(distances.keys()):
    tmp = cost(path)
    if tmp < currentMin:
        currentMin = tmp
        minPath    = path

print currentMin, minPath
