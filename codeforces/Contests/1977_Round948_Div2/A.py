from collections import Counter
from collections import defaultdict
import heapq
import bisect

def solve():
  moves, cubes = [int(n) for n in input().split()]
  # print(moves, cubes)

  if cubes > moves:
    return False
  if ((moves-cubes) % 2) == 0:
    return True
  return False

cases = int(input())
for _ in range(cases):
  print("YES" if solve() else "NO")
