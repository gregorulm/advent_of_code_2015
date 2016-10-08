# AoC: Day 8

with open("input") as f:
    lines = f.readlines()

lines        = map(lambda x: x.strip(), lines)
escapedChars = map(lambda x: x.count('\\') + x.count('"') + 2, lines)

print sum(escapedChars)