n = int(input())
monsters = [int(m) for m in input().split(" ")]

if len(monsters) == 1:
  print(monsters[0])
else:

  Max = max(monsters)

  maxPower = Max
  power = Max

  i = monsters.index(Max)
  monsters[i] = None
  power -= 1

  adjL, adjR = None, None
  if i == 0:
    adjR = 1
  elif i == len(monsters)-1:
    adjL = len(monsters)-2
  else:
    adjL, adjR = i-1, i+1

  while True:
    # print(monsters)
    # print(power, maxPower)

    iMin = None
    if adjL != None and adjR != None:
      if monsters[adjL] < monsters[adjR]:
        iMin = adjL
      else:
        iMin = adjR
    elif adjL != None:
      iMin = adjL
    elif adjR != None:
      iMin = adjR
    else:
      break

    if power < monsters[iMin]:
      maxPower += (monsters[iMin] - power)
      power += (monsters[iMin] - power)

    power -= 1
    monsters[iMin] = None

    if adjR != None and monsters[adjR] == None:
      if adjR == len(monsters)-1: adjR = None
      else: adjR += 1

    if adjL != None and monsters[adjL] == None:
      if adjL == 0: adjL = None
      else: adjL -= 1

  print(maxPower)
