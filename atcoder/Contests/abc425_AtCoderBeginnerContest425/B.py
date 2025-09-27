N = int(input())
nums = list(map(int, input().split()))


valid = [n for n in nums if n != -1]

if len(valid) != len(set(valid)):
    print("No")
    exit(0)

print("Yes")

valid = set(valid)
nnext = 1

def nexxt():
    global nnext
    while nnext in valid:
        nnext += 1
    valid.add(nnext)
    return nnext

for i, n in enumerate(nums):
    if n != -1: continue
    nums[i] = nexxt()

print(" ".join(map(str, nums)))
