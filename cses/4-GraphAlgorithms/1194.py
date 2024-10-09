cities, roads = map(int, input().split())

sets = [-1] * cities

def union(a, b):
  aa = find(a)
  bb = find(b)
  if aa != bb:
    sets[aa] = bb

def find(a):
  cur = a
  while sets[cur] != -1:
    cur = sets[cur]
  if cur != a:
    sets[a] = cur
  return cur

for _ in range(roads):
  f, t = map(int, input().split())
  union(f-1, t-1)

res = 0
new = []

first = find(0)
for c in range(1, cities):
  if find(c) != first:
    res += 1
    union(c, 0)
    new.append((0, c))

print(res)
for f, t in new:
  print(f+1, t+1)
