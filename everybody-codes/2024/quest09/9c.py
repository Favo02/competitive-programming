import sys
from heapq import heappop, heappush

queue = [(0, 0)]
seen = {0: 0}

def solve(n):
  if n in seen:
    return seen[n]

  while queue:
    steps, num = heappop(queue)
    num = -num # maxheap instead of minheap

    for s in stamps:
      if num+s == n:
        return steps+1
      if num+s not in seen:
        heappush(queue, (steps+1, -(num+s)))
        seen[num+s] = steps+1

stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]

res = 0

for line in sys.stdin:
  n = int(line.strip())

  cur_res = float("inf")

  mid = n // 2
  for nn in range(mid-53, mid+53): # cba to calculate bounds for even and odd
    a, b = nn, n - nn
    if abs(a - b) <= 100: # cba to calculate bounds for even and odd
      cur_res = min(cur_res, solve(a) + solve(b))

  res += cur_res

print(res)
