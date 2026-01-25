cases = int(input())

for _ in range(cases):
    n = int(input())
    nums = list(map(int, input().split()))
    assert n == len(nums)

    nums2 = nums.copy()
    nums2.sort(reverse=True)

    for i in range(n):
        if nums2[i] == nums[i]:
            print(nums[i], end=" ")
        else:
            break

    if i < n-1:
        rem = nums[i:]
        # print(rem)
        maxi = rem.index(max(rem))
        # print(maxi)

        rem = list(reversed((rem[:maxi+1]))) + rem[maxi+1:]

        print(" ".join(map(str, rem)))
    else:
        print()
