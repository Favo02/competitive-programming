from heapq import heappop, heappush

n, q = map(int, input().split())

heap = []
for ver in range(n):
    heappush(heap, (ver, 1))

for _ in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    applied = 0
    while heap[0][0] <= x:
        applied += heap[0][1]
        heappop(heap)
    heappush(heap, (y, applied))
    print(applied)
