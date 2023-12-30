cases = int(input())

for _ in range(cases):

  LEN = int(input())
  nums = [int(n) for n in input().split()]
  print(LEN, nums)

  LEN = int(input())
  nums = []
  for _ in range(LEN):
    a, b = input().split()
    nums.append((int(a), int(b)))
  print(LEN, nums)

  string = input()
  print(string)
