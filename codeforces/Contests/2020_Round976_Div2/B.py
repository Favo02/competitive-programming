# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
from math import isqrt
# import sys

# sys.setrecursionlimit(10**5)


def solve():

  n = int(input())

  # https://oeis.org/A000037
  return n+(k:=isqrt(n))+int(n>=k*(k+1)+1)


cases = int(input())
for _ in range(cases):
  print(solve())
