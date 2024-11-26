n = int(input())

res = 0
while n > 0:
  maxx = 0
  for d in str(n):
    maxx = max(maxx, int(d))
  n -= maxx
  res += 1

print(res)
