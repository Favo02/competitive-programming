# from collections import deque
# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math

# import sys
# sys.setrecursionlimit(10**5)

l, r = [int(n) for n in input().split()]

if l + r != 1:
  print("Invalid")
elif l == 1:
  print("Yes")
else:
  print("No")
