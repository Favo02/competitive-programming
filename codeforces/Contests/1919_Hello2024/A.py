cases = int(input())

for _ in range(cases):

  a, b = input().split()
  a = int(a)
  b = int(b)
  if (a+b)%2==0:
    print("Bob")
  else:
    print("Alice")
