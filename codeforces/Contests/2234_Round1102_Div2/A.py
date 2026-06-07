def solve(nums):
    for i in range(N-2):
        if (nums[i] % nums[i+1]) != nums[i+2]:
            return False
    return True

T = int(input())
for _ in range(T):
    N = int(input())
    nums = sorted(list(map(int, input().split())), reverse=True)
    if solve(nums):
        print(nums[0], nums[1])
    else:
        print(-1)
