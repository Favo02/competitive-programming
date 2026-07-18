import sys

numbers, rawcards = sys.stdin.read().split("\n\n")
numbers = list(map(int, (" ".join(map(str.strip, numbers.splitlines()))).split()))
time = {n: i for i, n in enumerate(numbers)}
cubes = []

for card in rawcards.splitlines():
    face = list(map(int, card.split()))
    if cubes and len(cubes[-1]) < 5:
        cubes[-1].append([face[i * 5 : (i + 1) * 5] for i in range(5)])
    else:
        cubes.append([[face[i * 5 : (i + 1) * 5] for i in range(5)]])

alll = []
for cube in cubes:
    movez = []
    for x in range(5):
        for y in range(5):
            cur = 0
            for z in range(5):
                cur = max(cur, time[cube[x][y][z]])
            movez.append(cur)
    # print(movez)

    movex = []
    for y in range(5):
        for z in range(5):
            cur = 0
            for x in range(5):
                cur = max(cur, time[cube[x][y][z]])
            movex.append(cur)
    # print(movex)

    movey = []
    for x in range(5):
        for z in range(5):
            cur = 0
            for y in range(5):
                cur = max(cur, time[cube[x][y][z]])
            movey.append(cur)
    # print(movey)

    diagx = []
    for x in range(5):
        for diag in [
            [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)],
            [(0, 4), (4, 0), (1, 3), (3, 1), (2, 2)],
        ]:
            cur = 0
            for z, y in diag:
                cur = max(cur, time[cube[x][y][z]])
            diagx.append(cur)
    # print(diagx)

    diagy = []
    for y in range(5):
        for diag in [
            [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)],
            [(0, 4), (4, 0), (1, 3), (3, 1), (2, 2)],
        ]:
            cur = 0
            for z, x in diag:
                cur = max(cur, time[cube[x][y][z]])
            diagy.append(cur)
    # print(diagy)

    diagz = []
    for z in range(5):
        for diag in [
            [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)],
            [(0, 4), (4, 0), (1, 3), (3, 1), (2, 2)],
        ]:
            cur = 0
            for y, x in diag:
                cur = max(cur, time[cube[x][y][z]])
            diagz.append(cur)
    # print(diagz)

    diag3d = []
    for diag in [
        [(i, i, i) for i in range(5)],
        [(4, 0, 0), (3, 1, 1), (2, 2, 2), (1, 3, 3), (0, 4, 4)],
        [(4, 0, 4), (3, 1, 3), (2, 2, 2), (1, 3, 1), (0, 4, 0)],
        [(0, 0, 4), (1, 1, 3), (2, 2, 2), (3, 3, 1), (4, 4, 0)],
    ]:
        cur = 0
        for x, y, z in diag:
            cur = max(cur, time[cube[x][y][z]])
        diag3d.append(cur)
    # print(diag3d)

    alll += movez + movex + movey + diagx + diagy + diagz + diag3d
alll.sort()
print(numbers[alll[4]])

exit(0)
