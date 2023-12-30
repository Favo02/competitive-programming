cases = int(input())

def solve(val, even, odd):
  turn = True

  while even + odd > 1:

    # maximise
    if turn:
      if odd >= 2:
        odd -= 2
        even += 1
      elif even >= 2:
        even -= 1
      else:
        val -= 1
        odd -= 1

    # minimize
    else:
      if odd >= 1 and even >= 1:
        val -= 1
        odd -= 1
      elif even >= 2:
        even -= 1
      elif odd >= 2:
        odd -= 2
        even += 1
      else:
        assert False

    turn = not turn

  return val


for _ in range(cases):

  LEN = int(input())
  nums = [int(n) for n in input().split()]
  # print(nums)


  e = o = 0
  summ = 0
  for k in nums:
    summ += k
    if k % 2 == 0:
      e += 1
    else:
      o += 1

    print(solve(summ, e, o), end=" ")
  print()
