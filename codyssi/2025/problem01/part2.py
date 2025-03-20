import sys

lines = list(map(str.strip, sys.stdin.readlines()))

nums = []
for line in lines[:-1]:
  nums.append(int(line))

res = nums[0]
signs = lines[-1]

for n, s in zip(nums[1:], signs[::-1]):
  res += (-1 if s == "-" else +1) * n

print(res)
