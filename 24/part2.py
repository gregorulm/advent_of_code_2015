# AoC: Day 24

with open("input") as f:
    lines = f.readlines()

weights  = map(lambda x: int(x), lines)
goal     = sum(weights) / 4

subSets  = []
shortest = 1000

# based on:
# http://stackoverflow.com/questions/4632322/finding-all-possible-combinations-of-numbers-to-reach-a-given-sum


def product(lst):
    if len(lst) == 0:
        return 1
    else:
        return lst[0] * product(lst[1:])


def subsetSum(numbers, target, partial=[]):
    global shortest
    global subSets

    s = sum(partial)


    if s == target:

        # retain only shortest partial sums
        if len(partial) == shortest:
            subSets.append(partial)

        elif len(partial) < shortest:
            shortest = len(partial)
            subSets = []
            subSets.append(partial)

    if s >= target:
        return

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subsetSum(remaining, target, partial + [n])


subsetSum(weights, goal)

choice = []
lowest = 9999999999999999999999L # 'infinity'

for elem in subSets:
    tmp = product(elem)
    if tmp < lowest:
        choice = elem
        lowest = tmp

print elem, lowest