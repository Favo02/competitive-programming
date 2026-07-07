from operator import itemgetter

dirs = input().strip()

walls = [0] * 100
i = 0
for dr, dw in zip(dirs, dirs[::-1]):
    if dr == '>':
        i = (i+1)%100
    else:
        i = (i-1)%100
    if dw == '>':
        i = (i-1)%100
    else:
        i = (i+1)%100
    walls[i] += 1

res = max(enumerate(walls), key=itemgetter(1))
print((res[0]+1) * res[1])
