# AoC: Day 3


houses = dict()


def update(c, pos):
    global houses

    (x, y) = pos
    
    if c == '^':
        pos = (x, y + 1)

    elif c == 'v':
        pos = (x, y - 1)

    elif c == '<':
        pos = (x - 1, y)

    elif c == '>':
        pos = (x + 1, y)

    if pos in houses.keys():
        val = houses[pos]
        houses[pos] = val + 1
    else:
        houses[pos] = 1
        
    return pos


with open("input") as f:
    content = f.readlines()

posSanta      = (0, 0)
posRobo       = (0, 0)
houses[(0,0)] = 2

turnSanta     = True
turnRobo      = False

for c in content[0]:

    if turnSanta:
        posSanta  = update(c, posSanta)
        turnSanta = False
        turnRobo  = True
    elif turnRobo:
        posRobo   = update(c, posRobo)
        turnRobo  = False
        turnSanta = True
        

total = 0

for key in houses.keys():
    if houses[key] >= 1:
        total += 1

print total
