cases = int(input())

for _ in range(cases):
    n, s, x = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    assert n == len(nums)

    if sum(nums) > s:
        print("NO")
    elif (sum(nums) - s) % x != 0:
        print("NO")
    else:
        print("YES")
