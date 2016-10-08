# AoC: Day 14

with open("input") as f:
    lines = f.readlines()

valsDict = dict()
points   = dict()

for line in lines:
    tmp      = line.split()
    name     = tmp[0]
    speed    = int(tmp[3])
    flyTime  = int(tmp[6])
    restTime = int(tmp[13])

    command    = "fly"
    flown      = 0
    rested     = 0
    pos        = 0

    valsDict[name] = (command, speed, flyTime, restTime, flown, rested, pos)
    points[name]   = 0


def advance(key):

    (command, speed, flyTime, restTime, flown, rested, pos) = valsDict[key]

    if command == "fly":

        if flown == flyTime:
            command       = "rest"
            rested        = 1
            valsDict[key] = \
                (command, speed, flyTime, restTime, flown, rested, pos)

        else:
            flown        += 1
            pos          += speed
            valsDict[key] = \
                (command, speed, flyTime, restTime, flown, rested, pos)

    elif command == "rest":

        if rested == restTime:
            command       = "fly"
            flown         = 1
            pos          += speed
            valsDict[key] = \
                (command, speed, flyTime, restTime, flown, rested, pos)

        else:
            rested       += 1
            valsDict[key] = \
                (command, speed, flyTime, restTime, flown, rested, pos)


def moveAllAndRewardLeader():

    for key in valsDict:
        advance(key)

    best = -1
    name = None
    # determine leading reindeer
    for key in valsDict:
        (_, _, _, _, _, _, pos) = valsDict[key]
        if pos > best:
            best = pos
            name = key

    points[name] += 1


for i in range(1, 2504):
    moveAllAndRewardLeader()


# find largest overall value
print max(points.values())