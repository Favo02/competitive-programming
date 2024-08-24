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
LEN = int(input())
nums = [int(n) for n in input().split()]
print(LEN, nums)

# lenght + N lines of 2 numbers
LEN = int(input())
nums = []
for _ in range(LEN):
  a, b = input().split()
  nums.append((int(a), int(b)))
print(LEN, nums)

# string
string = input()
print(string)
