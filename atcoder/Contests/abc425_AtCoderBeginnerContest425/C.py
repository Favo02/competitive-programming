N, Q = map(int, input().split())
nums = list(map(int, input().split()))

# print(nums)

prefix = [nums[0]]
for n in nums[1:]:
    prefix.append(prefix[-1] + n)

# print(prefix)

offset = 0

for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 1:
        offset += q[0]
    else:
        l, r = q
        l += offset - 1
        r += offset - 1
        l %= N
        r %= N

        if r < l:
            # print(l, r, nums)
            toend = prefix[-1] - prefix[l] + nums[l]
            fromstart = prefix[r]
            print(toend + fromstart)
        elif r == l:
            print(nums[r])
        else:
            print(prefix[r] - prefix[l] + nums[l])
            pass

        # print(l, r, nums[l:r+1])
        # print(sum(nums[l:r]))
