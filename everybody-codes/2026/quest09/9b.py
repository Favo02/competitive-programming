import sys

lines = list(map(str.strip, sys.stdin.readlines()))

res = 0
for line in lines:
    idd, growth, limit = line.split(", ")
    idd = idd.split("=")[1]
    growth = int(growth.split("=")[1])
    limit = int(limit.split("=")[1])

    branches = [0]
    time = 0
    elements = 1
    while True:
        time += 1
        newbr = []
        for i, b in enumerate(branches):
            branches[i] += 1
            if branches[i] == growth:
                branches[i] = growth // 2
                elements += 1
                newbr.append(growth // 2)
                newbr.append(1)
        branches += newbr
        if elements >= limit:
            res += time
            break
print(res)
