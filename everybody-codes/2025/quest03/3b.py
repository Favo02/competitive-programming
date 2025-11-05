nums = list(map(int, input().split(",")))

print(sum(sorted(list(set(nums)))[:20]))
