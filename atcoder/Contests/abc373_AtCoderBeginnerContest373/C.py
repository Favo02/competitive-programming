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
n = int(input())
nums1 = [int(n) for n in input().split()]
nums2 = [int(n) for n in input().split()]

print(max(nums1) + max(nums2))
