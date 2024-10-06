cases = int(input())

for _ in range(cases):
  n = int(input())

  if n == 1:
    input()
    print("NO")
    continue
  assert n >= 2

  nums = [int(nn) for nn in input().split()]

  # print("=" * 10)
  # print(nums)

  s = 0
  e = n
  iulia = sum(nums[i] for i in range(s, e,) if i % 2 == 0)
  date = sum(nums[i] for i in range(s, e) if i % 2 == 1)

  if iulia == date:
    print("YES")
    continue

  while s < e:
    iulia = sum(nums[i] for i in range(s, e) if i % 2 == 0)
    date = sum(nums[i] for i in range(s, e) if i % 2 == 1)

    if iulia == date:
      # print(s,e)
      print("YES")
      break

    if iulia > date:
      if s % 2 == 0:
        s += 1
      else:
        e -= 1
    else:
      if s % 2 == 0:
        e -= 1
      else:
        s += 1


  else:
    print("NO")

