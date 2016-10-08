# AoC: Day 14

with open("input") as f:
    lines = f.readlines()

vals = []

for line in lines:
    tmp      = line.split()
    #name     = tmp[0]
    speed    = int(tmp[3])
    flyTime  = int(tmp[6])
    restTime = int(tmp[13])

    vals.append((speed, flyTime, restTime))


def getDistance(specs, command, remaining, acc):

    (speed, flyTime, restTime) = specs

    if command == "fly":
        if remaining <= flyTime:
            return acc + (remaining * speed)
        else:
            return getDistance(specs, "rest", remaining - flyTime, acc + (speed * flyTime))

    elif command == "rest":
        if remaining <= restTime:
            return acc
        else:
            return getDistance(specs, "fly", remaining - restTime, acc)


best = 0

for specs in vals:
    tmp = getDistance(specs, "fly", 2503, 0)
    if tmp > best:
        best = tmp

print best