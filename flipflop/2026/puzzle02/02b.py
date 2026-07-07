from operator import itemgetter

dirs = input().strip()
r = w = res = 0
for dr, dw in zip(dirs, dirs[::-1]):
    if dr == '>':
        r = (r+1)%100
    else:
        r = (r-1)%100
    if dw == '>':
        w = (w+1)%100
    else:
        w = (w-1)%100
    if r == w:
        res += 1
print(res)
