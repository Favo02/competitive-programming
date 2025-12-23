what = input()
if what == "first":
    n = int(input())
    nums = list(map(int, input().split()))
    assert len(nums) == n
    print("".join(chr(ord('a') + n-1) for n in nums))

if what == "second":
    s = input()
    print(len(s))
    print(" ".join(str(ord(c) - ord('a') + 1) for c in s))
