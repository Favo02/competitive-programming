import sys

adj = [(0,-1), (0,+1), (1,0), (-1,0)]
diag = [(1,1), (-1,-1), (1,-1), (-1,1)]

diagComple = {
  (1,-1): ((0,-1),(1,0)),
  (1,1): ((0,1),(1,0)),
  (-1,1): ((-1,0),(0,1)),
  (-1,-1): ((-1,0),(0,-1)),
}

def checkValid(path):
  for i,c in enumerate(path):

    for j,g in enumerate(path):

      if i != j and c == g:
        return False

  for i in range(len(path) - 1):
    cur = path[i]
    next = path[i+1]

    if cur[0] != next[0] and cur[1] != next[1]:
      diag = (next[0] - cur[0], next[1] - cur[1])
      # print(diag)
      compl = diagComple[diag]
      compl = (cur[0]+compl[0][0], cur[1]+compl[0][1]), (cur[0]+compl[1][0], cur[1]+compl[1][1])

      for j in range(len(path)-1):
        if i == j: continue
        if path[j] == compl[0] and path[j+1] == compl[1]:
          # print("found", path[j])
          return False
        if path[j] == compl[1] and path[j+1] == compl[0]:
          # print("found", path[j])
          return False
      # print(cur, next, diag)

  return True

input = sys.argv[1]
f = open(input, "r")
lines = list(map(lambda l: l[:-1], f.readlines()))
gridSize = int(lines[0])
grid = lines[1:1+gridSize]
coords = list(map(lambda t: t.split(" "), lines[1+gridSize:][1:]))
paths = []
# print(coords)
for c in coords:
  path = []
  for p in c:
    tokens = p.split(",")
    path.append((int(tokens[0]), int(tokens[1])))
  paths.append(path)

# print(paths)

for i,path in enumerate(paths):
  # print("----------", i)
  if checkValid(path):
    print("VALID")
  else:
    print("INVALID")
