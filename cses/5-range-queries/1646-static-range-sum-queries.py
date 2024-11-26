n, q = map(int, input().split())
nums = list(map(int, input().split()))

prefix = [0]
summ = 0
for n in nums:
  summ += n
  prefix.append(summ)

for _ in range(q):
  l, r = map(int, input().split())
  print(prefix[r] - prefix[l-1])
