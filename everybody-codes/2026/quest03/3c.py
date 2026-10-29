import sys

lines = sys.stdin.readlines()

ans = 0


def convert(base, n):
    res = 0
    for exp, bb in enumerate(n[::-1]):
        res += int(bb) * (int(base[::-1][exp % len(a)]) ** exp)
        exp += 1
    return res


for line in lines:
    line = line.strip().split("-")[1]
    a, b = line.split()

    target = convert(a, b)
    for i in range(int(b)):
        if convert(a, str(i)) == target:
            break
    else:
        ans += int(target)

print(ans)
