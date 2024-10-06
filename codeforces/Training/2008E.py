from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)

def solve():

  l = int(input())
  string = input()

  if l == 1:
    return 1

  if l % 2 == 1:

    right_even = [0] * 26
    right_odd = [0] * 26
    for i, s in enumerate(string):
      if i % 2 == 0:
        right_even[ord(s) - ord('a')] += 1
      else:
        right_odd[ord(s) - ord('a')] += 1

    left_even = [0] * 26
    left_odd = [0] * 26


    res = float('inf')

    for rem in range(l):

      if rem % 2 == 0:
        right_even[ord(string[rem]) - ord('a')] -= 1
      else:
        right_odd[ord(string[rem]) - ord('a')] -= 1

      even = [e1 + e2 for e1, e2 in zip(left_even, right_odd)]
      odd = [o1 + o2 for o1, o2 in zip(left_odd, right_even)]

      res = min(res, sum(even) - max(even) + sum(odd) - max(odd))

      if rem % 2 == 0:
        left_even[ord(string[rem]) - ord('a')] += 1
      else:
        left_odd[ord(string[rem]) - ord('a')] += 1

    return res+1

  else:
    even = Counter(string[::2]).values()
    odd = Counter(string[1::2]).values()

    return sum(even) - max(even) + sum(odd) - max(odd)

cases = int(input())
for _ in range(cases):
  print(solve())
