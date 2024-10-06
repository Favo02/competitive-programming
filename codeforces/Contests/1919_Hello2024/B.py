cases = int(input())

for _ in range(cases):

  LEN = int(input())
  nums = [1 if n == "+" else -1 for n in input()]

  print(abs(sum(nums)))
