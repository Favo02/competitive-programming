from collections import Counter

n = int(input())
s = input()
assert n == len(s)

c = Counter(s)
for k, v in c.items():
    if v % 2 == 1:
        print(k)
        break

