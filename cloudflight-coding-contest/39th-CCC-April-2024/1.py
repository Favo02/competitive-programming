from collections import Counter

paths = int(input())

for _ in range(paths):
  string = input()
  count = Counter(string)
  # print(count)
  print(f"{count["W"]} {count["D"]} {count["S"]} {count["A"]}")
