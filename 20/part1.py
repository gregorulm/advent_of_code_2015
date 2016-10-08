# AoC: Day 20

target = 29000000
limit  = 1000000
arr    = [ 0 for i in range(limit + 1)]

i = 1
while True:

    if i > limit:
        break

    j = i
    while j < limit + 1:
        arr[j] += i * 10
        j      += i

    i += 1


for idx in range(len(arr)):
    if arr[idx] >= target:
        print idx
        exit()

