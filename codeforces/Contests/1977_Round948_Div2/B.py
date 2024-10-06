from collections import Counter
from collections import defaultdict
import heapq
import bisect

powers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648]

def solve():

  x = int(input())
  arr = [0, 0] + [int(l) for l in bin(x)[2:]]
  # print(x)
  # print(arr)

  while not valid(arr):
    arr = remove(arr)
    # print(arr)
    arr = pass2(arr)
    # print(arr)
  # print(' '.join([str(n) for n in reversed(arr)]))

  # print('==========', arr)
  while arr[0] == 0:
    arr.pop(0)
  # print(arr)
  print(len(arr))
  print(' '.join([str(n) for n in reversed(arr)]))
  # return -1

def remove(arr):
  first_one = -1
  for i, bit in enumerate(arr):
    if bit == 1 and first_one == -1:
      first_one = i
    if bit == 0 and first_one != -1:
      # print(first_one, i, arr[first_one:i])
      if i-first_one > 1:
        arr[first_one-1] = 1
        for j in range(first_one, i-1):
          arr[j] = 0
        arr[i-1] = -1
      first_one = -1

  if first_one != -1:
    i += 1
    if i-first_one > 1:
      # print(first_one, i, arr[first_one:i])
      arr[first_one-1] = 1
      for j in range(first_one, i-1):
        arr[j] = 0
      arr[i-1] = -1
    first_one = -1
  return arr

def pass2(arr):
  last = arr[0]
  for i in range(1, len(arr)):
    if last == -1 and arr[i] == 1:
      arr[i-1] = 0
      arr[i] = -1
    if last == 1 and arr[i] == -1:
      arr[i-1] = 0
      arr[i] = 1

    last = arr[i]
  return arr

def valid(arr):
  for a, b in zip(arr, arr[1:]):
    if abs(a) + abs(b) == 2:
      return False
  return True

cases = int(input())
for _ in range(cases):
  # print("=" * 10)
  solve()
  # print(solve())

# - lunghezza 1 - 32 inclusi
# - ogni bit deve essere 0, 1, -1
# - non ci possono essere due uni (-1 o 1) vicini
#   ogni due caratteri ci deve essere uno zero
# - x == al numero letto in notazione binaria
#   sum (a_i * 2^i)

'''
32 16 8 4 2 1

2 + 1 = 4 - 1

4 + 2 = 8 - 2

4 + 8 = 16 - 4

4


14:

8 4 2

8 + 4 = 16 - 4





'''
