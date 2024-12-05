n = int(input())

for _ in range(n):
  nn = int(input())
  nums = list(map(int, input().split()))

  avg = sum(nums) / len(nums)
  if avg != int(avg):
    print("NO")
  else:
    avg = int(avg)

    for i in range(nn-2):
      nums[i+2] += nums[i] - avg
      nums[i] = avg

    # print(nums)
    if all(a == b for a, b in zip(nums, nums[1:])):
      print("YES")
    else:
      print("NO")
    # print(nums[i])
