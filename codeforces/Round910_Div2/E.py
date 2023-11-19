from collections import defaultdict

def solve(s1, s2):
  for i,v in enumerate(s2):
    if v not in s1:
      return "NO"

    s1Index = s1.index(v)

    smaller = list(filter(lambda x: x < v, s2[i+1:]))
    # print(v, smaller)

    S1 = s1[s1Index:]
    for s in smaller:
      for j, ss in enumerate(S1):
        if ss == s:
          S1[j] = -1
          break
      else:
        return "NO"
    else:
      s1[s1Index] = -1

  return "YES"


cases = int(input())

while cases > 0:
  cases -= 1
  input()
  s1 = [ord(c) for c in input()]
  s2 = [ord(c) for c in input()]

  print(solve(s1, s2))



