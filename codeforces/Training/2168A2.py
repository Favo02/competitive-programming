base = "qwertyuiopasdfghjklzxcvbn"
space = "m"

def enc(n):
    res = []
    while n > 0:
        res.append(base[n % len(base)])
        n //= len(base)
    return "".join(reversed(res))

def dec(s):
    res = 0
    exp = 0
    for c in reversed(s):
        res += len(base)**exp * base.index(c)
        exp += 1
    return res

def first():
    n = int(input())
    nums = list(map(int, input().split()))
    assert len(nums) == n
    print(space.join(enc(n) for n in nums))
def second():
    s = input()
    print(len(s.split(space)))
    print(" ".join(str(dec(c)) for c in s.split(space)))

what = input()
if what == "first":
    first()
if what == "second":
    second()
