nLin = int(input())

def bfs(start):
  queue = [start]
  dist = {start: 0}

  while queue:
    cur = queue.pop(0)

    for adj in graph[cur]:

      if adj in atm:
        return dist[cur]+1

      if adj not in dist:
        dist[adj] = dist[cur] + 1
        queue.append(adj)

  return -1

# stazToId = {}
c = 0
graph = {}
linee = []
for _ in range(nLin):
  staz = input()[2:].split(" ")
  id = None

  stazId = []
  for s in staz:
    # if s in stazToId:
    #   id = stazToId[s]
    # else:
    #   stazToId[s] = c
    #   id = c
    #   c += 1
    stazId.append(s)

  for i, si in enumerate(stazId):
    if si in graph:
      if i > 0:
        graph[si].append(stazId[i-1])
      if i < len(stazId)-1:
        graph[si].append(stazId[i+1])
    else:
      if i > 0:
        graph[si] = [stazId[i-1]]
      if i < len(stazId)-1:
        if si in graph:
          graph[si].append(stazId[i+1])
        else:
          graph[si] = [stazId[i+1]]

nATM = int(input())
atm = {}
for _ in range(nATM):
  s = input()
  atm[s] = True

nQ = int(input())
for _ in range(nQ):
  s = input()
  id = s
  if id in atm:
    print(0)
  else:
    print(bfs(id))
