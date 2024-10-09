from collections import deque

ADJS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(r, c):
  queue = deque([(r, c)])

  while queue:
    cr, cc = queue.popleft()

    for ar, ac in ADJS:
      if not (0 <= cr + ar < rows):
        continue
      if not (0 <= cc + ac < cols):
        continue
      if graph[cr+ar][cc + ac] == ".":
        graph[cr+ar][cc + ac] = "#"
        queue.append((cr+ar, cc+ac))

rows, cols = map(int, input().split())

graph = []

for r in range(rows):
  graph.append(list(input()))

rooms = 0

for r in range(rows):
  for c in range(cols):
    if graph[r][c] == ".":
      rooms += 1
      bfs(r, c)

print(rooms)
