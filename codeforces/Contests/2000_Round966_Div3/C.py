# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)

def solve():

  # lenght + list of numbers
  arr_len = int(input())
  template = [int(n) for n in input().split()]

  def valid_s(s):
    if len(s) != arr_len:
      return False

    n_to_s = {}
    s_to_n = {}

    for ss, nn in zip(s, template):
      if ss in s_to_n:
        if s_to_n[ss] != nn:
          return False
      if nn in n_to_s:
        if n_to_s[nn] != ss:
          return False
      n_to_s[nn] = ss
      s_to_n[ss] = nn

    return True

  # lenght + N lines of 2 numbers
  LEN = int(input())
  for _ in range(LEN):
    if valid_s(input()):
      print("YES")
    else:
      print("NO")

cases = int(input())
for _ in range(cases):
  solve()
