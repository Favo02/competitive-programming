from math import lcm, gcd

cases = int(input())

def divisors(number):
  divisors = []
  for i in range(int(number**0.5), 0, -1):
    if number % i == 0:
      divisors.append(i)
      if i != number // i:
        divisors.append(number // i)
  return sorted(divisors)[-3:-1]

for _ in range(cases):

  a, b = input().split()
  a = int(a)
  b = int(b)

  fb = set()

  i = 1
  while True:
    aa = a * i
    if aa in fb and aa > b:
      if divisors(aa) == [a,b]:
        print(aa)
        break

    bb = b * i
    fb.add(bb)
    i+=1
