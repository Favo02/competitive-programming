import sys

lines = sys.stdin.readlines()

ans = 0

for line in lines:
    line = line.strip().split("-")[1]
    a, b = line.split()

    for exp, (aa, bb) in enumerate(zip(a[::-1], b[::-1])):
        ans += int(bb) * (int(aa) ** exp)

print(ans)
