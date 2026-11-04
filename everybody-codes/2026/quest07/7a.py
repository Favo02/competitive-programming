import sys
from collections import defaultdict, deque

graph = defaultdict(list)
lines = sys.stdin.readlines()
start = None
energy = defaultdict(int)

for line in lines:
    idd, en, connections = line.strip().split(", ")
    idd = idd.split("=")[1]
    en = int(en.split("=")[1])
    connections = connections.split("=")[1].split(",")
    graph[idd] += connections
    energy[idd] = en
    if len(connections) > len(graph[start]):
        start = idd

queue = deque()
queue.append((start, 5))
while queue:
    (cur, en) = queue.popleft()
    energy[cur] += en
    if en <= 0:
        continue
    for adj in graph[cur]:
        queue.append((adj, en - 1))

print(sum(energy.values()))
