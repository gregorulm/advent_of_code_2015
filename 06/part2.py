# AoC: Day 6

d = 1000
m = [[0 for j in range(d)] for i in range(d)]


def toggle(pos):
    (x, y)   = pos
    m[x][y] += 2


def turnOff(pos):
    (x, y)  = pos
    if m[x][y] != 0:
        m[x][y] -= 1


def turnOn(pos):
    (x, y)   = pos
    m[x][y] += 1


def getRange(s):

    tmp = s.split()
    tmp = filter(lambda x: "," in x, tmp)
    tmp = map(lambda x: x.split(","), tmp)
    tmp = tmp[0] + tmp[1]
    tmp = map(lambda x: int(x), tmp)

    (a, b) = (tmp[0], tmp[1])
    (x, y) = (tmp[2], tmp[3])

    result = []

    for i in range(a, x + 1):
        for j in range(b, y + 1):
            result.append((i, j))

    return result


with open("input") as f:
    content = f.readlines()


for command in content:

    allPos = getRange(command)

    if command.startswith("toggle"):
        map(lambda x: toggle(x), allPos)

    elif command.startswith("turn off"):
        map(lambda x: turnOff(x), allPos)

    elif command.startswith("turn on"):
        map(lambda x: turnOn(x), allPos)


total = 0

for row in m:
    total += sum(row)

print total