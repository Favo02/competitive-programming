n = int(input())
string = input()
q = int(input())

parent = {}

to = list('qwertyuiopasdfghjklzxcvbnm')
to.sort()

for _ in range(q):
    a, b = input().split()

    for j in range(26):
        if to[j] == a:
            to[j] = b

for c in string:
    print(to[ord(c) - ord('a')], end="")
print()
