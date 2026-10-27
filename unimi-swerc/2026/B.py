n, r = map(int, input().split())
r = r * 2 + 1

d, m = n // r, n % r
if m != 0:
    d += 1
print(d)
