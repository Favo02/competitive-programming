cases = int(input())

for _ in range(cases):
  s = list(map(int, list(input())))

  for i in range(len(s)):
    ii = i-1
    while ii >= 0 and s[ii]+1 < s[ii+1]:
      s[ii], s[ii+1] = s[ii+1]-1, s[ii]
      ii -= 1

    # print(s)
  print("".join(map(str, s)))
