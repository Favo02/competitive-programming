from collections import defaultdict

n = int(input())
sponsors = defaultdict(int)
for _ in range(n):
    sponsors[input().strip()] += 1

res = []
maxx = max(sponsors.values())
for k, v in sponsors.items():
    if v == maxx:
        res.append(k)
print("\n".join(sorted(res)))
