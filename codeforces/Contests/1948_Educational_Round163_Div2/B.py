cases = int(input())

def solve():

  while True:

    for i, (a, b) in enumerate(zip(nums, nums[1:])):
      if a > b:
        if a < 10:
          return "NO"
        else:
          nums[i] = int(str(a)[0])
          nums.insert(i+1, int(str(a)[1]))
          break
    else:
      return "YES"

for _ in range(cases):
  LEN = int(input())
  nums = [int(n) for n in input().split()]
  print(solve())
