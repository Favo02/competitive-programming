

# cur = 66
# for i in range(10**100):
#   if all(x == "3" or x == "6" for x in str(cur)):
#     print(cur)
#   cur += 66


def solve(n):
  if n < 2:
    return -1
  if n == 3:
    return -1
  if n % 2 == 0:
    return ("3" * (n-2)) + "66"
  return ("3" * (n-4)) + "6366"


cases = int(input())
for _ in range(cases):
  n = int(input())
  print(solve(n))
