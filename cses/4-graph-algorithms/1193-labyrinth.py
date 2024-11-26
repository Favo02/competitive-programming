from collections import deque

ADJS = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]

def bfs(sr, sc):
  queue = deque([(sr, sc, 0)])
  while queue:
    r, c, dist = queue.popleft()
    for i, (ar, ac, _) in enumerate(ADJS):
      if not (0 <= r+ar < rows): continue
      if not (0 <= c+ac < cols): continue
      if graph[r+ar][c+ac] == "B":
        graph[r+ar][c+ac] = i
        return dist+1
      if graph[r+ar][c+ac] == ".":
        graph[r+ar][c+ac] = i
        queue.append((r+ar, c+ac, dist+1))
  return -1

def path(sr, sc, er, ec):
  path = []
  while not (sr == er and sc == ec):
    dr, dc, dir = ADJS[graph[sr][sc]]
    path.append(dir)
    sr -= dr
    sc -= dc
  return "".join(reversed(path))


rows, cols = map(int, input().split())

graph = []
start = end = None
for r in range(rows):
  graph.append(list(input()))

  if "A" in graph[-1]:
    start = (r, graph[-1].index("A"))
  if "B" in graph[-1]:
    end = (r, graph[-1].index("B"))

dist = bfs(*start)
if dist == -1:
  print("NO")
else:
  print("YES")
  print(dist)
  print(path(*end, *start))
