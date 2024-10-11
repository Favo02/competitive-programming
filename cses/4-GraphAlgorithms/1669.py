cities, roads = map(int, input().split())

graph = [[] for _ in range(cities)]
for _ in range(roads):
  f, t = map(int, input().split())
  graph[f-1].append(t-1)
  graph[t-1].append(f-1)

print(graph)
