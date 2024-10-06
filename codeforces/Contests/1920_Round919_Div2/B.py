cases = int(input())

for _ in range(cases):

  n, k, x = [int(n) for n in input().split()]
  nums = [int(n) for n in input().split()]

  # print("=" * 10)
  # print(k,x)

  nums.sort()
  res = sum(nums[:-x]) - sum(nums[-x:])

  # print(res, nums)

  next_to_rem = n-1
  next_to_sub = n-x-1
  temp_res = res

  for _ in range(k):

    s = 0 if next_to_sub < 0 else nums[next_to_sub]

    temp_res = temp_res + nums[next_to_rem] - 2*s

    res = max(res, temp_res)

    next_to_rem -= 1
    next_to_sub -= 1

  print(res)
