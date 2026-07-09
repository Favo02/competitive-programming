import sys

lines = list(filter(lambda l: l != '|', map(lambda l: l.strip(), sys.stdin.readlines())))

res = 0
last = lines[3]
for l in lines[4:-1]:
    if last != l:
        res += 1
    last = l

print(res)
