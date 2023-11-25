def reconstruct(a,sa,sb):
  b = []
  for aa in a:
    i = sa.index(aa)
    b.append(sb[i])
  return b

def zero(a,b):
  sa = sorted(a)
  sb = list(reversed(sorted(b)))

  for aa, bb in zip(sa,sb):
    if aa > bb:
      return False, []

  return True, reconstruct(a,sa,sb)


def solve(x,a,b):
  assert x != 0
  # print(x)
  # print(a)
  # print(b)

  sa = sorted(a)
  sb = sorted(b)

  # print("s", sa)
  # print("s", sb)

  pivotA, pivotB = sa[-x], sb[x-1]
  if pivotA <= pivotB: return False, []

  ra = sa[:-x]
  rb = sb[x:]

  # print("r", ra)
  # print("r", rb)

  for aa,bb in zip(ra,rb):
    if aa > bb: return False, []

  return True, reconstruct(a,sa[-x:]+ra,sb[:x]+rb)


cases = int(input())


while cases > 0:
  cases -= 1
  line1 = input().split(" ")
  x = int(line1[1])
  a = [int(n) for n in input().split(" ")]
  b = [int(n) for n in input().split(" ")]
  res = False
  arr = []
  if x == 0:
    res, arr = zero(a,b)
  else:
    res, arr = solve(x,a,b)
  if res:
    print("YES")
    for n in arr:
      print(n, end=" ")
    print()
  else:
    print("NO")
