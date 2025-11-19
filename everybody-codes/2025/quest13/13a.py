import sys

nums = list(map(int, map(str.strip, sys.stdin.readlines())))

lock = [-1 for _ in range(len(nums)+1)]
lock[0] = 1

f = e = 1
for i, n in enumerate(nums):
    if i % 2 == 0:
        lock[f] = n
        f+=1
    else:
        lock[-e] = n
        e+=1

print(lock[2025 % len(lock)])
