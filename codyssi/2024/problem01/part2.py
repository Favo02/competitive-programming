import sys

prices = sorted(list(map(int, sys.stdin.read().strip().split("\n"))))
print(sum(prices[:-20]))
