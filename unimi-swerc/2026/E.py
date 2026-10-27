N, Z = map(int, input().split())

H = list(map(int, input().split()))
I = list(map(int, input().split()))
# assert len(H) == N
# assert len(I) == N

reach = [[False] * N for _ in range(2)]
reach[0][0] = True
reach[1][0] = True

i = 0
for i in range(N - 1):
    if reach[0][i]:
        if abs(H[i] - H[i + 1]) <= Z:
            reach[0][i + 1] = True
        if abs(H[i] - I[i + 1]) <= Z:
            reach[1][i + 1] = True
    if reach[1][i]:
        if abs(I[i] - H[i + 1]) <= Z:
            reach[0][i + 1] = True
        if abs(I[i] - I[i + 1]) <= Z:
            reach[1][i + 1] = True

if reach[0][-1] or reach[1][-1]:
    print("Yes")
else:
    print("No")
