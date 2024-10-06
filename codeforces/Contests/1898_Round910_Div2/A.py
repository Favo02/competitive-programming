cases = int(input())

while cases > 0:
  cases -= 1

  line1 = input().split(" ")
  target = int(line1[1])

  s = input()
  # print(target, s)

  a, b = 0, 0
  for c in s:
    if c == 'A': a += 1
    if c == 'B': b += 1

  if b == target:
    print(0)

  elif b < target:
    count = target - b
    for i,c in enumerate(s):
      if c == 'A': count -= 1
      if count == 0:
        print(1)
        print(i+1, 'B')
        break

  elif b > target:
    count = b - target
    for i,c in enumerate(s):
      if c == 'B': count -= 1
      if count == 0:
        print(1)
        print(i+1, 'A')
        break

  # elif target > b:

    # print(1)
