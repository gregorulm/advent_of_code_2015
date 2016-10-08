# AoC: Day 16

with open("input") as f:
    lines = f.readlines()

realSue = { "children"    : 3
          , "cats"        : 7
          , "samoyeds"    : 2
          , "pomeranians" : 3
          , "akitas"      : 0
          , "vizslas"     : 0
          , "goldfish"    : 5
          , "trees"       : 3
          , "cars"        : 2
          , "perfumes"    : 1
          }

keys = realSue.keys()

for line in lines:
    tmp             = line.split(",")
    (sue, p1, val1) = tmp[0].split(":")
    tmp[0]          = p1 + ":" + val1
    match           = True

    for i in range(3):
        (key, val) = tmp[i].split(":")
        val        = int(val)
        key        = key.strip()

        if key in keys:

            if key == "cats" or key == "trees":
                if not val > realSue[key]:
                    match = False

            elif key == "pomeranians" or key == "goldfish":
                if not val < realSue[key]:
                    match = False

            elif not realSue[key] == val:
                match = False

    # all three attributes match
    if match:
        print sue
