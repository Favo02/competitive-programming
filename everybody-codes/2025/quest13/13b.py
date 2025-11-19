import sys

nums = list(map(str.strip, sys.stdin.readlines()))

front = [1]
back = []

for i, n in enumerate(nums):
    a, b = map(int, n.split("-"))
    if i % 2 == 0:
        front += list(range(a, b+1))
    else:
        back += list(range(a, b+1))

lock = front + list(reversed(back))
print(lock[20252025 % len(lock)])
