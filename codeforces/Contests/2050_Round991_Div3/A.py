n = int(input())

for _ in range(n):
  keep = True
  words, maxfirst = map(int, input().split())
  cur = 0
  for i in range(words):
    w = input()
    cur += len(w)
    # print(cur)

    if keep and cur > maxfirst:
      print(i)
      keep = False

  if keep:
    print(words)

