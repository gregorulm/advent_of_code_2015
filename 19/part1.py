# AoC: Day 19

with open("input") as f:
    lines = f.readlines()


replace = []
target  = lines[-1].strip()
output  = set()

for line in lines:
    if "=>" in line:
        (a, b) = line.split("=>")
        a      = a.split()[0]
        b      = b.split()[0]
        replace.append((a, b))


def substitute(string, pos, s, t):
    return string[:pos] + t + string[pos + len(s):]


def replaceAll(subst, pos, firstRun):

    (s, t)  = subst
    tmp     = target

    if firstRun:
        pos = tmp.find(s, 0)

    if pos == -1:
        return

    res     = substitute(tmp, pos, s, t)
    output.add(res)

    nextPos = tmp.find(s, pos + 1)

    return replaceAll(subst, nextPos, False)


for subst in replace:
    replaceAll(subst, 0, True)


print len(output)
