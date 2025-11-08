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

    return int("".join(map(str, map(itemgetter(1), sword)))), [
        int("".join(map(str, filter(lambda x: x is not None, s)))) for s in sword
    ]


swords = sorted(
    [
        (*quality(list(map(int, nums.split(",")))), int(id))
        for id, nums in map(lambda line: line.split(":"), sys.stdin.readlines())
    ],
    reverse=True,
)

print(sum((i + 1) * id for i, (_, _, id) in enumerate(swords)))
