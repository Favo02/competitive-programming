cases = int(input())

for _ in range(cases):
  m, a, b, c = map(int, input().split())

  res = 0

  m1 = m2 = m

  res += min(m, a)
  m1 -= min(m, a)

  res += min(m, b)
  m2 -= min(m, b)

  res += min(c, m1+m2)
  print(res)
