def solve():
  n = int(input())
  ranges = []

  minn, maxx = None, None
  for i in range(n):
    s, e = map(int, input().split())

    s = max(s, 0.00000000000001)
    e = max(e, 0.00000000000001)

    mi = (i+1)/e
    ma = (i+1)/s

    if i == 0:
      minn = mi
      maxx = ma
    else:
      maxx = min(maxx, ma)
      minn = max(minn, mi)

    if minn > maxx:
      return -1

  return minn

cases = int(input())
for i in range(cases):
  print(f"Case #{i+1}: {solve()}")
