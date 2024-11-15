import sys

stamps = [10, 5, 3, 1]

res = 0

for line in sys.stdin:
  n = int(line.strip())

  i = 0
  while n > 0:

    if stamps[i] <= n:
      n -= stamps[i]
      res += 1
    else:
      i += 1

print(res)
