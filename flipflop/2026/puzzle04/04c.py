import sys

lines = list(filter(lambda l: l != '|', map(lambda l: l.strip(), sys.stdin.readlines())))

lines = lines[3:-1]
lines = lines[::-1]

res = 0
while lines:
    newlines = []
    last = lines[0]
    for l in lines[1:]:
        if l == last:
            newlines.append(last)
        last = l
    lines = newlines
    res += 1


print(res)
