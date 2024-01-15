cases = int(input())

for _ in range(cases):

  LEN = int(input())
  now = input()
  des = input()


  prev = post = 0
  for n,d in zip(now, des):
    if n == d:
      continue
    elif n == "1":
      prev += 1
    elif d == "1":
      post += 1
    else:
      assert False

  if prev > post:
    res = post + (prev-post)
  elif post > prev:
    res = prev + (post-prev)
  else:
    res = prev

  print(res)
