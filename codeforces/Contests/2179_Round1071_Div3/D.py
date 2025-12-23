from collections import defaultdict

cases = int(input())

def solve():
    n = int(input())
    # if n == 1:
    #     return [1, 0]
    # if n == 2:
    #     return [3, 1, 0, 2]

    # print(best, bin(best))
    buckets = defaultdict(list)
    res = []
    for i in range(0, 2**n):
        b = bin(i)[2:].rjust(n, '0')

        # print(b, b.rfind('0'))
        buckets[b.rfind('0')].append(i)

    buck = list(buckets.items())
    buck.sort(key=lambda b: b[0], reverse=False)
    for (_, v) in buck:
        res += sorted(v)

    # res.sort(key=lambda i: bin(i)[2:], reverse=True)

    seen = set(res)
    for i in range(0, 2**n):
        if i in seen:
            continue
        res.append(i)

    # for r in res:
    #     print(bin(r)[2:].rjust(n, '0'))
    return res

for c in range(cases):
    print(" ".join(map(str, solve())))
    # print()
