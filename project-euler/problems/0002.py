res = 0

a, b = 1, 1
# every third fibonacci element is even
while b < 10**6 * 4:
  c = a+b
  res += c

  a = c+b
  b = c+a

print(res)
