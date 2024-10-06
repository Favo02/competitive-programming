cases = int(input())

while cases > 0:
  cases -= 1
  vert = int(input())
  dirs = input()

  parent = {}
  tree = []
  leafs = []
  i = 1
  while vert > 0:
    vert -= 1
    temp = input().split(" ")
    l,r = int(temp[0]), int(temp[1])
    if l == r == 0: leafs.append(i)
    if l != 0: parent[l] = i
    if r != 0: parent[r] = i
    tree.append((l,r))
    i+=1
  parent[1] = -1

  res = 10**9
  for l in leafs:
    modifications = 0

    cur = l
    while True:
      Parent = parent[cur]
      if Parent == -1: break
      ParDirection = dirs[Parent-1]
      if ParDirection == 'U':
        modifications += 1
      else:
        Target = tree[Parent-1][0] if ParDirection == 'L' else tree[Parent-1][1]
        if Target != cur:
          modifications += 1
      cur = Parent

    res = min(res, modifications)
  print(res)


