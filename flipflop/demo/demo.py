import sys
from collections import Counter
from operator import itemgetter

nums = [int(n) for n in sys.stdin.readlines()]

print("Part1:", sum(nums))
print("Part2:", round(sum(nums) / len(nums)))
print("Part3:", str(max(Counter(nums).items(), key=itemgetter(1))[0]) + min(Counter("".join(map(str, nums))).items(), key=itemgetter(1))[0])

