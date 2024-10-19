import sys
sys.setrecursionlimit(10**8)

def generate(cur, left, right, rem):
  # print(f"{cur = } {rem = }")

  if rem <= 0:
    return { cur }

  res = set()
  if rem == 1:
    for i in range(1, left):
      for j in range(1, right):
        res.add(int(f"{i}{cur}{j}"))
    return res

  for i in range(1, left):
    for j in range(1, right):
      res.update(generate(int(f"{i}{cur}{j}"), i+1, j+1, rem-1))
  return res

def solve(a, b, m):
  res = 0

  startsize = len(str(a))
  if startsize % 2 == 0: startsize -= 1
  endsize = len(str(b))
  if endsize % 2 == 0: endsize -= 1
  # print(f"{startsize = } {endsize = }")

  mounts = set()

  for size in range(startsize, endsize+1, 2):
    for center in range(size // 2 + 1, 10):
      # print(size, generate(center, center, center, size // 2))
      mounts.update(generate(center, center, center, size // 2))
      # for pp in generate(center, center, center, size // 2):
      #   if a <= pp <= b:
      #     if pp % m == 0:
      #       res += 1

  # print(mounts)
  for mm in mounts:
    if a <= mm <= b:
      if mm % m == 0:
        res += 1
  return res

cases = int(input())
for i in range(cases):
  a, b, mult = map(int, input().split())
  print(f"Case #{i+1}: {solve(a, b, mult)}")
