# AoC: Day 15

def transpose(inp, acc):


    if len(inp[0]) == 1:
        row = map(lambda x: x[0], inp)
        acc.append(row)
        return acc

    else:
        row = map(lambda x: x[0], inp)
        out = map(lambda x: x[1:], inp)
        acc.append(row)
        return transpose(out, acc)


def dotProduct(u, v):
    assert isinstance(u, list)
    assert isinstance(v, list)

    return sum(map(lambda x, y: x * y, u, v))


def fun(x, y):

    tmp = x * y

    if tmp <= 0:
        return 0
    else:
        return tmp


with open("input") as f:
    lines = f.readlines()


combinations = []

for a in range(0, 101):

    for b in range(0, 101):
        if a + b > 100:
            break

        for c in range(0, 101):
            if a + b + c > 100:
                break

            for d in range(0, 101):
                if a + b + c + d == 100:
                    combinations.append([a, b, c, d])
                elif a + b + c + d > 100:
                    break


ingredients = []


for line in lines:

    tmp = map(lambda x: x.strip().replace(',', ''), line.split())

    capacity   = int(tmp[2])
    durability = int(tmp[4])
    flavor     = int(tmp[6])
    texture    = int(tmp[8])
    calories   = int(tmp[10])

    ingredients.append([capacity, durability, flavor, texture, calories])


def mult(xs):
    if len(xs) == 0:
        return 1
    else:
        return xs[0] * mult(xs[1:])


m    = transpose(ingredients, [])
best = 0

for c in combinations:
    tmp = map(lambda x: dotProduct(x, c), m)

    # last element in list is calorie count
    if tmp[-1] == 500:
        tmp = tmp[:-1]
        tmp = mult(map(lambda x: 0 if x < 0 else x, tmp))

        if tmp > best:
            best = tmp

print best