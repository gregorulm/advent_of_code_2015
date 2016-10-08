# AoC: Day 1

total = 0

with open("input") as f:
    content = f.readlines()

for c in content[0]:
    if c == '(':
        total += 1

    elif c == ')':
        total -= 1

print total