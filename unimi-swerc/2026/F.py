N = int(input())
delay = list(map(int, input().split()))
sugg = list(map(int, input().split()))

res = sugg.copy()

cur = float("inf")
for i in range(2 * N):
    i = i % N
    cur = min(cur, sugg[i])
    res[i] = min(res[i], cur)
    cur += delay[i]

print(*res)
