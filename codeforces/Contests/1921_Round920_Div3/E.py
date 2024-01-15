cases = int(input())

for _ in range(cases):

  W, H, ra, ca, rb, cb = [int(n) for n in input().split()]
  print(W, H, ra, ca, rb, cb)
  vert_dist = rb - ra
  hor_dist = abs(ca - cb)

  print(hor_dist, vert_dist)

  if vert_dist <= 0:
    print("Draw")
  elif vert_dist % 2 == 1:
    print("Alice or Draw")
  else:
    print("Bob or Draw")
