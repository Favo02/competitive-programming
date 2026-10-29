import sys

lines = sys.stdin.readlines()

ans = 0

for line in lines:
    line = line.strip().split("-")[1]
    a, b = line.split()

    for exp, bb in enumerate(b[::-1]):
        ans += int(bb) * (int(a[::-1][exp % len(a)]) ** exp)

print(ans)
