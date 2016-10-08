# AoC: Day 10

num = "1321131112"

def transformOne(s):

    x     = s[0]
    count = 0

    for c in s:
        if c == x:
            count += 1
        else:
            break

    rest = s[count:]

    return (str(count) + x, rest)


def transformAll(s):

    res = ""

    while not s == "":
        (x, s) = transformOne(s)
        res += x

    return res


i = 0
while i < 40:
    num = transformAll(num)
    print i
    i += 1

print len(num)
