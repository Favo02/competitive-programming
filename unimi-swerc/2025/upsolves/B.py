n = int(input())
nums = list(map(int, input().split()))

res = 1

minn = nums[0]
for n in nums[1:]:
    if n <= minn:
        res += 1
    minn = min(minn, n)

print(res)
