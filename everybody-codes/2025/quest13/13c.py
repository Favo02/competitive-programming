import sys

nums = list(map(str.strip, sys.stdin.readlines()))

front = [(1,1,1)]
back = []

totsize = 1

for i, n in enumerate(nums):
    a, b = map(int, n.split("-"))
    if i % 2 == 0:
        front.append((a, b-a+1, +1))
    else:
        back.append((b, b-a+1, -1))
    totsize += b+1-a

lock = front + list(reversed(back))
# el = 20252025 % totsize # for part2
el = 202520252025 % totsize

for i, (a, qty, mult) in enumerate(lock):
    if el < qty:
        print(a + mult*el)
        break
    el -= qty
