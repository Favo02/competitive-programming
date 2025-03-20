import sys

lines = list(map(str.strip, sys.stdin.readlines()))

nums = []
for line1, line2 in zip(lines[:-1:2], lines[1:-1:2]):
  nums.append(int(line1)*10 + int(line2))

res = nums[0]
signs = lines[-1]

for n, s in zip(nums[1:], signs[::-1]):
  res += (-1 if s == "-" else +1) * n

print(res)
