n = int(input())
nums = list(map(int, input().split()))
assert len(nums) == n

res = list(map(str, (sorted(list(set(nums))))))
print(len(res))
print(" ".join(res))
