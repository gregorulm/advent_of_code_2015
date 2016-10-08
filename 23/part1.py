# AoC: Day 23

with open("input") as f:
    lines = f.readlines()


instructions = []

for line in lines:
    instructions.append(line.strip())

reg = { "a": 0
      , "b": 0 }


pos = 0
while pos < len(instructions):

    val = instructions[pos]

    if val.startswith("hlf"):
        (_, r)  = val.split()
        reg[r]  = reg[r] / 2
        pos    += 1

    elif val.startswith("tpl"):
        (_, r)  = val.split()
        reg[r]  = reg[r] * 3
        pos    += 1

    elif val.startswith("inc"):
        (_, r)  = val.split()
        reg[r] += 1
        pos    += 1

    elif val.startswith("jmp"):
        (_, n)  = val.split()
        pos    += int(n)

    elif val.startswith("jie"):
        (x, n)  = val.split(",")
        n       = int(n)
        (_, r)  = x.split()

        if reg[r] % 2 == 0:
            pos += int(n)
        else:
            pos += 1

    elif val.startswith("jio"):
        (x, n)  = val.split(",")
        n = int(n)
        (_, r) = x.split()

        if reg[r] == 1:
            pos += int(n)
        else:
            pos += 1

print reg["b"]