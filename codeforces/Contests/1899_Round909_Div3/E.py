import sys

cases = int(input())

lines = []
for l in sys.stdin:
  lines.append(l.rstrip('\n'))

for i in range(0, len(lines), 2):
  nums = [int(w) for w in lines[i+1].split(" ")]
  # print(nums)

  count = 0

  MIN = min(nums)
  for i, n in enumerate(nums):
    if n == MIN:
      count = i
      break

  # for n in nums[count:]:
  # print(nums[count:])
  Max = nums[count]
  for n in nums[count+1:]:
    if n < Max:
      print(-1)
      break
    Max = max(Max, n)
  else:
    print(count)
