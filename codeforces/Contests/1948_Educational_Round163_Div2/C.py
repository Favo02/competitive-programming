from collections import deque

def bfs(size, graph):
  seen = set()
  queue = deque([ (0,0) ])

  while queue:
    cx, cy = queue.popleft()
    if (cx, cy) in seen: continue
    seen.add((cx, cy))

    # print(cx, cy)

    for dx, dy in [(-1,0), (+1,0), (0,-1), (0,+1)]:
      if not (0 <= cx + dx < size):
        continue
      if not (0 <= cy + dy < 2):
        continue

      nx, ny = cx + dx, cy + dy
      if graph[ny][nx] == "<":
        nx -= 1
      else:
        assert graph[ny][nx] == ">"
        nx += 1

      if nx == size-1 and ny == 1:
        return True
      queue.append((nx, ny))

  return False

cases = int(input())

for _ in range(cases):

  LEN = int(input())

  uno = input()
  due = input()

  # print(uno)
  # print(due)

  if due[LEN-2] == "<":
    print("NO")
    continue

  if bfs(LEN, [uno, due]):
    print("YES")
  else:
    print("NO")
