cases = int(input())

# literal         [1,2,3]
# or composite:   range 0 + [3,4,5]

def recArray(index, q):
  start, end, length, arr = ranges[index]
  if index == 0:
    return arr[q % len(arr)]
  else:
    pass
    qq = q % length
    prevsize = ranges[index-1][1] - ranges[index-1][0]
    if qq < prevsize:
      return recArray(index-1, qq)
    else:
      qqq = qq % prevsize
      return arr[qqq % len(arr)]

for _ in range(cases):

  ops, aaa = [int(n) for n in input().split()]

  curarr = []
  ranges = []
  joints = {}

  cursize = 0

  for _ in range(ops):
    optype, x = [int(n) for n in input().split()]

    # print(optype, x)
    if optype == 1:
      curarr.append(x)
    else:
      if cursize == 0:
        rangelen = cursize + len(curarr)
        ranges.append(( cursize, (cursize+len(curarr)) * (x+1), rangelen, curarr.copy() ))
        cursize = (cursize+len(curarr)) * (x+1)
        curarr = []
      else:
        joints[cursize] = x
        rangelen = cursize + len(curarr)
        ranges.append(( cursize+1, (cursize+len(curarr)) * (x+1), rangelen, curarr.copy() ))
        cursize = (cursize+len(curarr)) * (x+1)
        curarr = []

  # print(ranges)
  # print(joints)


  queries = [int(n) for n in input().split()]
  # print(queries)
  for q in queries:
    q -= 1
    if q in joints:
      # print("===RES", joints[q])
      print(joints[q], end="j ")
    else:
      # print("q", q, f"({q+1})")
      for i, (s, e, l, arr) in enumerate(ranges):
        if s <= q < e:
          # print("===RES", recArray(i, q))
          print(recArray(i, q), end=" ")
  print()

