# AoC: Day 2

def product(xs):
    if xs == []:
        return 1
    else:
        return xs[0] * product(xs[1:])


total = 0

with open("input") as f:
    content = f.readlines()

for c in content:
    dim    = map (lambda x: int(x), c.split('x'))
    dim.sort()
    total += 2 * (dim[0] + dim[1]) + product(dim)

print total


