def sumOfDigits(n):
  nString = str(n)
  sum = 0
  for c in nString:
    sum += int(c)
  return sum


def sumRec(n):
  global s
  if(n == 1): return s
  return 2*sumRec(n-1) + sumOfDigits(n)



t = input().split(" ")
s, n = int(t[0]), int(t[1])
res = s
# for i in range(n-1):

#   print(res, s+i)
#   res =  sumOfDigits(s+1+i) + res*2



print(sumRec(n))

