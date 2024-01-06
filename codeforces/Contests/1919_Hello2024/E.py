from collections import Counter
from functools import lru_cache
import sys

# 0 1 0 3 1
# @lru_cache(maxsize=None)
def solve(index, cur, count, lenn, mem):
  # print(f"sol i{index},\tcur{cur},\t{count}\tl{lenn}")

  if (cur, count) in mem:
    return mem[(cur, count)]

  if lenn == LEN:
    # print("eheh")
    mem[(cur, count)] = 1
    return 1

  adjs = []
  adjsi = []
  if 0 <= index+1 < len(unique):
    ad = unique[index+1]
    if abs(ad-cur) == 1:
      if count[conversion[ad]] > 0:
        adjs.append(ad)
        adjsi.append(index+1)

  if 0 <= index-1 < len(unique):
    ad = unique[index-1]
    if abs(ad-cur) == 1:
      if count[conversion[ad]] > 0:
        adjs.append(ad)
        adjsi.append(index-1)

  if not adjs:
    mem[(cur, count)] = 0
    return 0

  res = 1
  count = list(count)
  for a, ai in zip(adjs, adjsi):
    count[conversion[a]] -= 1
    res *= solve(ai, a, tuple(count), lenn+1, mem)
    count[conversion[a]] += 1

  mem[(cur, tuple(count))] = res
  return res


sys.setrecursionlimit(10**8)
cases = int(input())
MOD = 998244353

for _ in range(cases):

  LEN = int(input())
  nums = [int(n) for n in input().split()]

  unique = list(set(nums))
  conversion = {}
  for ii, uu in enumerate(unique):
    conversion[uu] = ii

  count = Counter(nums)
  count = list(count.values())

  starts = [i for i,n in enumerate(unique) if n == 1 or n == -1]

  if not starts:
    # print("="*5)
    print(0)
    # print("="*5)
  else:
    res = 0

    for s in starts:
      count[conversion[unique[s]]] -= 1
      sol = solve(s, unique[s], tuple(count), 1, {})
      res += (sol * (count[conversion[unique[s]]]+1))
      # print(f"start: {unique[s]}: {sol} * {(count[conversion[unique[s]]]+1)}")
      count[conversion[unique[s]]] += 1


    # print("="*5)
    print(res)
    # print(solve.cache_info())
    # print("="*5)


  # print("-" * 30)

