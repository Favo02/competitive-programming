from collections import Counter, defaultdict

def indexes():
  res = defaultdict(list)
  for i,n in enumerate(nums):
    res[n].append(i)
  return res

def solve():
  count = Counter(nums)
  indx = indexes()

  splits = 0
  splite = LEN-1

  # print(count)
  for n in range(LEN+1):
    if count[n] == 0:
      break

    if count[n] == 1:
      return -1

    splits = max(splits, indx[n][0])
    splite = min(splite, indx[n][-1])
    if splits >= splite:
      return -1
    # print(splits, splite)

  return [splits, splite]



cases = int(input())

for _ in range(cases):
  # print("=" * 10)

  LEN = int(input())
  nums = [int(n) for n in input().split()]
  # print(nums)

  res = solve()
  if type(res) is list:
    print(2)
    print(1, res[0]+1)
    print(res[0]+2, LEN)
  else:
    print(-1)

