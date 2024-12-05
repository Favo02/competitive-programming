from collections import Counter

cases = int(input())

miss = {
  1: [(5, 0), (2, 1), (8, 2)],
  2: [(1, 0), (4, 2), (7, 1)],
  3: [(6, 0), (0, 2), (3, 1)],
  4: [(2, 0), (5, 2), (8, 1)],
  5: [(7, 0), (1, 2), (4, 1)],
  6: [(3, 0), (0, 1), (6, 2)],
  7: [(8, 0), (2, 2), (5, 1)],
  8: [(4, 0), (1, 1), (7, 2)],
}

def check(num):
  summ = 0
  while True:
    for digit in num:
      summ += int(digit)
    if summ < 1_000_000_000:
      return summ % 9
    num = str(summ)

add = {"2": 2, "3": 6}

for _ in range(cases):
  # print()

  num = input()
  missing = 9 - check(num)
  # print(num, missing)

  if missing == 9 or missing == 0:
    print("YES")
  else:
    assert missing in miss
    available = Counter([nnn for nnn in num if nnn in "23"])
    # print(available, miss[missing])

    valid = False
    for comb in miss[missing]:
      twos, threes = comb
      if available["2"] >= twos and available["3"] >= threes:
        valid = True
        break

    if valid:
      print("YES")
    else:
      print("NO")
