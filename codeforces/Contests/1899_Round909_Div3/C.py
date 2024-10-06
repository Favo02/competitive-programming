import sys

cases = int(input())

lines = []
for l in sys.stdin:
  lines.append(l.rstrip('\n'))

for i in range(0, len(lines), 2):
  nums = [int(w) for w in lines[i+1].split(" ")]

  maxx = [0 for _ in nums]
  for i,n in enumerate(nums):
    if i == 0:
      maxx[0] = n
      continue
    if nums[i-1] % 2 != n % 2:
      maxx[i] = max(maxx[i-1]+n, n)
    else:
      maxx[i] = n

  # print(nums)
  # print(maxx)
  maxxx = -10**9
  for n in maxx:
    maxxx = max(maxxx, n)


  print(maxxx)
