from operator import itemgetter

nums = list(map(int, input().split(":")[1].split(",")))
sword = [[None, nums[0], None]]

for n in nums[1:]:
    for i, (a, b, c) in enumerate(sword):
        if a is None and n < b:
            sword[i][0] = n
            break
        if c is None and n > b:
            sword[i][2] = n
            break
    else:
        sword.append([None, n, None])

print("".join(map(str, map(itemgetter(1), sword))))
