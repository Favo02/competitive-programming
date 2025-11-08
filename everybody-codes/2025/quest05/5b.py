import sys
from operator import itemgetter


def quality(nums):
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

    return int("".join(map(str, map(itemgetter(1), sword))))


swords = [
    quality(list(map(int, line.split(":")[1].split(","))))
    for line in sys.stdin.readlines()
]

print(max(swords) - min(swords))
