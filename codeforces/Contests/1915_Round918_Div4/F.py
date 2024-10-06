cases = int(input())

START, END, DIR = 0, 1, 2

for _ in range(cases):
  people = int(input())
  pep = []

  for _ in range(people):
    fromm, too = input().split()
    fromm = int(fromm)
    too = int(too)
    pep.append((fromm, too, True if fromm < too else False))

  res = 0

  for i, p1 in enumerate(pep):
    for j in range(i+1, people):
      p2 = pep[j]

      if p1[DIR] == p2[DIR]:
        if p2[START] > p1[START] and p2[END] < p1[END]:
          res += 1
        elif p1[START] > p2[START] and p1[END] < p2[END]:
          res += 1
      # opposite directions
      else:
        if not (p1[END] < p2[START] or p1[START] > p2[END]):
          res += 1

  print(res)
