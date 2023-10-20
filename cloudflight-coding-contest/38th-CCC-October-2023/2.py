import sys

adj = [(0,-1), (0,+1), (1,0), (-1,0)]

def sameIsland(x1, y1, x2, y2, visited):
  # print("check", x1, y1, x2, y2)
  for a in adj:
    newx = x1+a[0]
    newy = y1+a[1]

    if newx == x2 and newy == y2:
      return True
    
    type = grid[newy][newx]
    # print(visited)
    if type == "L" and (newx, newy) not in visited:
      visited.add((newx, newy))
      if sameIsland(newx, newy, x2, y2, visited):
        return True

  return False

input = sys.argv[1]
f = open(input, "r")
lines = list(map(lambda l: l[:-1], f.readlines()))
gridSize = int(lines[0])
grid = lines[1:1+gridSize]
coords = list(map(lambda t: t.split(" "), lines[1+gridSize:][1:]))
# print(coords)
for c in coords:
  tokens1 = c[0].split(",")
  tokens2 = c[1].split(",")

  x1 = int(tokens1[0])
  y1 = int(tokens1[1])
  
  x2 = int(tokens2[0])
  y2 = int(tokens2[1])

  res = sameIsland(x1, y1, x2, y2, set())
  if (x1 == x2 and y1 == y2):
    print("SAME")
    continue
  if res:
    print("SAME")
  else:
    print("DIFFERENT")
