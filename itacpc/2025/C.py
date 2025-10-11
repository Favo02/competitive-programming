from collections import defaultdict

n = int(input())
points = []
for _ in range(n):
    a, b = map(int, input().split())
    points.append((a, b))

points.sort()
# print(points)

res = 0

count = defaultdict(int)

for i in range(n):
    x1, y1 = points[i]
    count[x1-y1] += 1


for k, v in count.items():
    if v == 1: continue
    if v == 2:
        res += 1
    else:
        n = v-1
        res += max(0, (n * (n+1)) // 2)
print(res)
