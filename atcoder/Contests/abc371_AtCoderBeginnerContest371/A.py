# from collections import deque
# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math

# import sys
# sys.setrecursionlimit(10**5)

ab, ac, bc = input().split()

if ab == "<":
  if ac == "<":
    if bc == "<":
      print("B")
    else:
      print("C")
  else:
    print("A")
else:
  if bc == "<":
    if ac == "<":
      print("A")
    else:
      print("C")
  else:
    print("B")



