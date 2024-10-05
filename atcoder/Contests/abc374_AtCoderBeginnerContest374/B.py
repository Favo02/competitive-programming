# from collections import deque
# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math

a = input()
b = input()

if a == b:
  print(0)
else:
  for i in range(max(len(a), len(b))):
    if len(a) == i or len(b) == i:
      print(i+1)
      break
    else:
      if a[i] != b[i]:
        print(i+1)
        break
