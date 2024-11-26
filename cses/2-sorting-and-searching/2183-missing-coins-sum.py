n = int(input())
coins = list(map(int, input().split()))
coins.sort()

maxx = 0

for c in coins:

  if c > maxx + 1:
    print(maxx + 1)
    exit(0)
  else:
    maxx += c

print(maxx + 1)
