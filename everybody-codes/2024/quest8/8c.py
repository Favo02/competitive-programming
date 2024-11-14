priests = int(input())
div = 10
summ = 10
blocks = 202400000

# example
# priests = 2
# div = 5
# summ = 5
# blocks = 160

def thickness(last):
  return ((last * priests) % div) + summ

def empty(width, height):
  return ((priests * width) * height) % div

def used(cols):
  width = len(cols) * 2 - 1
  tot_used = 0
  for i, c in enumerate(cols):
    if i == len(cols) - 1:
      tot_used += 2*c
      continue

    to_keep = c - cols[i+1] + 1
    max_remove = c - to_keep

    torem = min(max_remove, empty(width, c))

    u = c - torem

    if i != 0:
      tot_used += 2*u
    else:
      tot_used += u

  return tot_used

thick = 1
cols = []
layers = 0
use = 0

while use <= blocks:
  for i in range(len(cols)):
    cols[i] += thick
  cols.append(thick)
  thick = thickness(thick)
  layers += 1
  use = used(cols)

print(use - blocks)
