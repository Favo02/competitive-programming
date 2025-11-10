from collections import defaultdict

s = input()

mentors = defaultdict(int)
res = 0

for c in s:
    if c.isupper(): mentors[c] += 1
    else: res += mentors[c.upper()]

print(res)
