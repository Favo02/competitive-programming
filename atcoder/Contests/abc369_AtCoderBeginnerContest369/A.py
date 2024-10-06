# from collections import deque
# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math
# import sys

# sys.setrecursionlimit(10**5)

# lenght + list of numbers
a, b = [int(n) for n in input().split()]

if a == b:
  print(1)

elif ((b - a) / 2) == ((b - a) // 2):
  print(3)
else:
  print(2)
