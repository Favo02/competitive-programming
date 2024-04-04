def solve():
  A, B, C = [int(n) for n in input().split()]

  rem = { 2: A, 1: B, 0: C }
  toplace = 2
  height = 0

  freepaces = 1
  nextfree = 0

  while toplace >= 0:

    if rem[toplace] <= 0:
      toplace -= 1
      continue

    if freepaces > 0:
      nextfree += toplace
      rem[toplace] -= 1
      freepaces -= 1
    else:
      if nextfree == 0:
        return -1
      freepaces = nextfree
      nextfree = 0
      height += 1

  if freepaces != 0 or nextfree != 0:
    return -1
  return height


cases = int(input())

for _ in range(cases):
  print(solve())
