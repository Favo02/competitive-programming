K = int(input())

# print(K)

tot = 0
for a in range(1,K):
  div = K // a
  if K % a == 0:
    div -= 1
  tot += div

print(tot)

