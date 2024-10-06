cases = int(input())

for _ in range(cases):

  _, charge, consuption, turnoff = [int(n) for n in input().split()]
  msgs = [0] + [int(n) for n in input().split()]

  deltas = [m2 - m1 for m1, m2 in zip(msgs, msgs[1:])]

  # print(charge, consuption, turnoff)
  # print(msgs)
  # print(deltas)


  for d in deltas:
    # print(consuption*d)
    # print(turnoff)
    charge -= min((consuption*d), (turnoff))
    # print("newcharge", charge)
    if charge <= 0:
      print("NO")
      break
  else:
    print("YES")
