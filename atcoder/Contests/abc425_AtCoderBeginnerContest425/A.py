n = int(input())

res = 0
for i in range(1, n+1):
    res += ((-1) ** i) * (i**3)
print(res)
