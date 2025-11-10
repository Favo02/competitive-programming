from collections import defaultdict, Counter

SIZE = 1000
s = input() * 1000

mentors = defaultdict(int, Counter(filter(lambda c: c.isupper(), s[:SIZE])))
start, end = -SIZE, SIZE
res = 0

for i, c in enumerate(s):
    if end < len(s) and s[end].isupper():
        mentors[s[end]] += 1
    end += 1

    if c.upper() != c:
        res += mentors[c.upper()]

    if start >= 0 and s[start].isupper():
        mentors[s[start]] -= 1
    start += 1

print(res)
