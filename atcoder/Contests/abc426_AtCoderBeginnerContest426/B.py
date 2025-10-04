from collections import Counter

strr = input()
c = Counter(strr)

for k, v in c.items():
    if v == 1:
        print(k)
