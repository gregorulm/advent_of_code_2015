# AoC: Day 8

with open("input") as f:
    lines = f.readlines()

lines         = map(lambda x: x.strip(), lines)

allChars      = map(lambda x: len(x), lines)
inMemoryChars = map(lambda x: len(eval(x)), lines)

print sum(allChars) - sum(inMemoryChars)