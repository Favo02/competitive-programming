from functools import reduce
import math

n, q = map(int, input().split())
nums = list(map(int, input().split()))

INF = float("inf")

def pow2(n):
  return 2**math.ceil(math.log2(n))

def segtree(arr):
  size = pow2(len(arr))
  arr.extend([INF] * (size-len(arr)))
  pieces = [ arr ]

  while size > 1:
    a = pieces[-1]
    pieces.append([min(a[i], a[i+1]) for i in range(0, size, 2)])
    size //= 2

  return reduce(lambda a, b: a+b, reversed(pieces))

def query(i, lbound, rbound, l, r):
  if l == lbound and r == rbound:
    return stree[i]

  mid = (lbound + rbound) // 2

  if l >= lbound and r <= mid:
    return query(2*i + 1, lbound, mid, l, r)
  elif l >= mid and r <= rbound:
    return query(2*i + 2, mid, rbound, l, r)

  return min(
    query(2*i + 1, lbound, mid, l, mid),
    query(2*i + 2, mid, rbound, mid, r)
  )

stree = segtree(nums)

p = pow2(n)
for _ in range(q):
  l, r = map(int, input().split())
  print(query(0, 0, p, l-1, r))

