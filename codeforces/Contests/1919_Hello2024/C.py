cases = int(input())

# def solve(index, lasta, lastb, resa, resb):
#   if index == LEN:
#     return resa + resb
#   a = solve(index+1, nums[index], lastb, resa+1 if nums[index] > lasta else resa, resb)
#   b = solve(index+1, lasta, nums[index], resa, resb+1 if nums[index] > lastb else resb)
#   return min(a, b)

for _ in range(cases):

  LEN = int(input())
  nums = [int(n) for n in input().split()]
  # print(LEN, nums)

  pen = 0
  a = nums[-1]
  b = -1
  for i in range(LEN-2, -1, -1):
    n = nums[i]

    # va bene per entrambi
    if n >= a and n >= b:
      if a > b:
        a = n
      else:
        b = n
    # non va bene per entrambi:
    elif n < a and n < b:
      pen += 1
      if a > b:
        a = n
      else:
        b = n
    # va bene per uno solo
    elif n >= a:
      a = n
    elif n >= b:
      b = n
    else:
      assert False

  print(pen)

  # print(solve(0, 10**9, 10**9, 0, 0))


# quello prima deve essere piu grande
# quando va bene per entrambi allora sostituire il piu grande (forse)
# quando NON va bene per entrambi allora sostuire il piu grande

# 8 2 3 1 1 7 4 3
# 3 0, -1 0
# 4 0, -1 0
# 7 0, -1 0
# 7 0, 1 0
# 7 0, 1 0
# 7 0, 3 0
# 2 1, 3 0
# 2 1, 8 0
