# AoC: Day 11

pwd      = "cqjxjnds"
letters  = "abcdefghjkmnpqrstuvwxyz"
allPairs = map(lambda x: x + x, letters)


def p1(s):
    return countUp(s + " ", 1)


def countUp(s, count):

    if count == 3:
        return True

    if len(s) == 1:
        return False

    if ord(s[1]) == (ord(s[0]) + 1):
        return countUp(s[1:], count + 1)

    else:
        return countUp(s[1:], 1)


def p2(s):

    illegal = ["i", "o", "u"]

    for c in illegal:
        if c in s:
            return False

    return True


def p3(s):

    count = 0

    for pair in allPairs:
        if pair in s:
            count += 1

    return count >= 2


def increaseMultiple(s):

    tmp = s[::-1]
    res = ""

    # overflow not implemented
    pos = 0
    for c in tmp:

        if c == 'z':
            res += 'a'
            pos += 1

        else:
            break

    res += nextLetter(tmp[pos])
    res += tmp[pos + 1:]

    return res[::-1]


def increase(s):

    res = ""

    if s[-1] != 'z':
        res = s[:-1] + nextLetter(s[-1])

    else:
        res = increaseMultiple(s)

    return res


def nextLetter(c):

    if c == 'z':
        return 'a'

    else:
        return chr(ord(c) + 1)



while True:

    if all([ p1(pwd), p2(pwd), p3(pwd) ]):
        break

    pwd = increase(pwd)


print pwd
