# AoC: Day 25

import copy

with open("input") as f:
    lines = f.readlines()

line = lines[0].split()
y = int(line[-1][:-1])
x = int(line[-3][:-1])

N   = 10000
row = [0] * N
m   = [copy.deepcopy(row) for i in range(N)]


def fillDiagonal(pos_x):
    pos_y = 0

    val = (m[0][pos_x - 1] * 252533) % 33554393

    while pos_x >= 0:
         m[pos_x][pos_y]  = val
         pos_x            = pos_x - 1
         pos_y            = pos_y + 1
         val = (val * 252533) % 33554393


m[0][0] = 20151125

for i in range(1, N):
    if i % 1000 == 0:
        print i
    fillDiagonal(i)


print m[x - 1][y - 1]