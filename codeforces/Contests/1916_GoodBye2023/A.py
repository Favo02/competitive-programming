from math import prod

FACTORS = [n for n in range(1, 2024) if 2023%n == 0]

def solve(num, rem):
  if rem == 0:
    if num == 2023:
      return True, []
    else:
      return False, None

  for f in FACTORS:
    s, arr = solve(num*f, rem-1)
    if s:
      return True, [f] + arr

  return False, []

cases = int(input())

for _ in range(cases):

  a, rem = input().split()
  a = int(a)
  rem = int(rem)
  num = prod([int(n) for n in input().split()])

  # print(rem, num)

  res, ress = solve(num, rem)
  if res:
    print("YES")
    for n in ress:
      print(n, end=" ")
    print()
  else:
    print("NO")
