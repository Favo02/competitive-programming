# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
from math import sqrt
# import sys

# sys.setrecursionlimit(10**5)

def solve():

  # string
  l = int(input())
  string = input()
  # print(string)

  if sqrt(l) != int(sqrt(l)):
    return False

  lato = int(sqrt(l))

  # print(string[:lato], string[-lato:], "1" * lato)

  if string[:lato] != string[-lato:] != "1" * lato:
    return False

  for i in range(lato, l-lato-1, lato):
    # print(i, i+lato, "1" + ("0" * (lato-2)) + "1")
    if string[i:i+lato] != ("1" + ("0" * (lato-2)) + "1"):
      return False


  return True

cases = int(input())
for _ in range(cases):
  print("YES" if solve() else "NO")
