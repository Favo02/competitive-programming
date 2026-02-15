def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    assert len(nums) == n

    for i, nn in enumerate(nums):
        if i + 1 == nn:
            continue
        if nn < i + 1:
            while nn < i + 1:
                nn *= 2
                if i + 1 == nn:
                    break
            else:
                return "NO"

        if nn > i + 1:
            while nn > i + 1 and nn % 2 == 0:
                nn //= 2
                if i + 1 == nn:
                    break
            else:
                return "NO"

    return "YES"


for _ in range(int(input())):
    print(solve())
