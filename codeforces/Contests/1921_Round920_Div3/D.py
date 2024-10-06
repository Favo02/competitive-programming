from collections import deque

cases = int(input())

for _ in range(cases):
  _ = input()
  nums = [int(n) for n in input().split()]
  available = [int(n) for n in input().split()]

  nums = deque(sorted(nums))
  available = deque(sorted(available))

  res = 0
  while nums:
    uno = abs(available[0] - nums[0])
    due = abs(available[0] - nums[-1])
    tre = abs(available[-1] - nums[0])
    qua = abs(available[-1] - nums[-1])

    maxx = max(uno, due, tre, qua)
    res += maxx
    if uno == maxx:
      available.popleft()
      nums.popleft()
    elif due == maxx:
      available.popleft()
      nums.pop()
    elif tre == maxx:
      available.pop()
      nums.popleft()
    elif qua == maxx:
      available.pop()
      nums.pop()
    else:
      assert False

  print(res)
