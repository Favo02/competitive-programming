def solve():
    n, x, y = map(int, input().split())
    nums = list(map(int, input().split()))
    assert len(nums) == n

    out = nums[:x] + nums[y:]
    ins = nums[x:y]

    insmin = min(ins)
    for i, n in enumerate(ins):
        if n == insmin:
            break
    ins = ins[i:] + ins[:i]

    res = []
    outi = 0
    while outi < len(out):
        if out[outi] < ins[0]:
            res.append(out[outi])
            outi += 1
        else:
            break
    res += ins
    res += out[outi:]

    return " ".join(map(str, res))



for _ in range(int(input())):
    print(solve())


# | 3 1 4 2 |

# 3 | 2 | 1

# 1 | 3 5 | 2 4

# fuori non cambia ordine
# dentro solo ciclare
