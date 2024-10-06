cases = int(input())

vow = "ae"
con = "bcd"

for _ in range(cases):
  n = int(input())
  word = input()
  # print(word)

  res = []

  i = n-1
  while i >= 0:
    if word[i] in vow:
      # print(f"{word[i-i]}{word[i]}", end="")
      res.append(f"{word[i-1]}{word[i]}")
      i -= 2

    else:
      # print(f"{word[i-2]}{word[i-1]}{word[i]}", end="")
      res.append(f"{word[i-2]}{word[i-1]}{word[i]}")
      i -= 3

  print(".".join(reversed(res)))
  # print()
