import random

def generate_random_numbers(N, low=2, upp=10**17):
  res = []
  while len(res) < N:
    n = random.randint(low, upp)
    if n % 2 == 1:
      n+=1
    res.append(n)
  return res

cases = int(input())

for _ in range(10**6):
  # L = int(input())
  # nums = [int(n) for n in input().split()]
  nums = generate_random_numbers(3, 2, 1000)
  # print(nums)

  for i in range(1, 10**18 + 1):
    if len(set(n % i for n in nums)) == 2:
      if i > 1000:
        print(nums)
        print(i)
      break


# 122, 586, 714 -> 29
    # [432, 384, 336] -> 32
# [274, 810, 122]
# 16
# [434, 978, 130]
# 17

# [202, 714, 458]
# 512
