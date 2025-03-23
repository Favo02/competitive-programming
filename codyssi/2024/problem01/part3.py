import sys

res = 0
prices = list(map(int, sys.stdin.read().strip().split("\n")))

for i, p in enumerate(prices):
  if i % 2 == 0:
    res += p
  else:
    res -= p

print(res)
