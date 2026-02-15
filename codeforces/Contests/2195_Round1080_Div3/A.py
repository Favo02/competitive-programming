def solve():
    n = int(input())
    nums = set(map(int, input().split()))
    if 67 in nums:
        return "YES"
    return "NO"


for _ in range(int(input())):
    print(solve())
