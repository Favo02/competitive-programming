cases = int(input())

change = {"w": "w", "p": "q", "q": "p"}

for _ in range(cases):
  s = input()
  for ss in s[::-1]:
    print(change[ss], end="")
  print()
