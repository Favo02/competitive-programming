n = int(input())

tot = 0

for _ in range(n):
  coff = input()

  if coff == "espresso":
    tot += 1
  if coff == "espresso-doppio":
    tot += 2
  if coff == "cappuccino":
    tot += 1
  if coff == "affogato":
    tot += 2
  if coff == "dead-eye":
    tot += 3
  if coff == "irish-coffee":
    tot += 2

print((tot + 1) // 2)
