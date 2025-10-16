from string import ascii_lowercase

n = int(input())
string = input()
q = int(input())

to = {c: c for c in ascii_lowercase}

for _ in range(q):
    f, t = input().split()
    to = {k: (t if v == f else v) for k, v in to.items()}

for c in string:
    print(to[c], end="")
print()
