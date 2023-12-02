def toTime(min):
  h = min // 60
  m = min % 60
  return "{:d} {:02d}".format(h, m)

ng = input().split(" ")
n, g = int(ng[0]), int(ng[1])

limit = 14 * 60 - g
print(toTime(limit))

if n == 0:
  print(toTime(limit))
else:

  stud = []
  for _ in range(n):
    tokens = [int(a) for a in input().split(" ")]
    h, m, t = tokens[0], tokens[1], tokens[2]
    m += h*60
    stud.append((m, t))

  stud.sort()

  time = 0
  for m, t in stud:
    print("from", toTime(time), end=" ")
    if time <= m:
      time = m + t
    else:
      time += t
    print("to", toTime(time))

    if limit < time:
      print("troppo tardi, accodarsi!!!")
      print(toTime(m))
      break
  else:
    print(toTime(limit))

