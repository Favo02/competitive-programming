aaa = input().split(" ")
booksN, edgesN = int(aaa[0]), int(aaa[1])
letters = input().split(" ")

graph = [[] for _ in range(booksN)]

for _ in range(edgesN):
  e = input().split(" ")
  graph[int(e[0])].append(int(e[1]))
  graph[int(e[1])].append(int(e[0]))


print(graph, letters)

mem = {}


def bfs(graph, start, to):
  prev = [None for _ in graph]
  prev[start] = -1

  queue = []
  queue.append(start)

  while queue:
    cur = queue.pop(0)

    for adj in graph[cur]:
      if adj == to:
        prev[adj] = cur
        return prev

      if prev[adj] is None:
        prev[adj] = cur
        queue.append(adj)
  return prev

def recPath(fro, to, prev):
  path = []
  cur = prev[to]
  while cur != fro:
    path.append(prev[cur])
    cur = prev[cur]
  return path


rules = int(input())
for _ in range(rules):
  rrr = input().split(" ")
  fro, to = int(rrr[0]), int(rrr[1])

  print(fro, to)
  prev = bfs(graph, fro, to)
  print(recPath(fro, to, prev))
