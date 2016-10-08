# AoC: Day 13
from itertools import permutations

with open("input") as f:
    lines = f.readlines()

valDict = dict()


for line in lines:
    tmp = line.split()

    key    = tmp[0]
    op     = tmp[2]
    val    = int(tmp[3])
    nextTo = tmp[-1][:-1]

    if op == "lose":
        val = -val

    if key in valDict.keys():
        valDict[key].append((nextTo, val))
    else:
        valDict[key] = [(nextTo, val)]


def getNeighbours(lst, x):
    assert isinstance(lst, list)
    assert isinstance(x,   str )

    pos = lst.index(x)

    if pos == 0:
        return (lst[pos + 1], lst[-1])

    elif pos == len(lst) - 1:
        return (lst[pos - 1], lst[0])

    else:
        return (lst[pos - 1], lst[pos + 1])


def getVal(x, neighbour):

    vals = valDict[x]

    for (y, val) in vals:
        if (y == neighbour):
            return val


def getSum(arrangement):

    total = 0

    for x in arrangement:
        (a, b) = getNeighbours(list(arrangement), x)
        total += getVal(x, a)
        total += getVal(x, b)

    return total


allGuests = valDict.keys()
maxVal    = -1000000000 # 'infinity'

for arrangement in permutations(allGuests):
    val = getSum(arrangement)
    if val > maxVal:
        maxVal = val

print maxVal