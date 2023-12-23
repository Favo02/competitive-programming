cases = int(input())

for _ in range(cases):
  N = int(input())
  l = [int(n) for n in input().split()]
  r = [int(n) for n in input().split()]
  w = [int(n) for n in input().split()]
  # print(sum(rr - ll for (rr,ll) in zip(r,l)))
  # l.sort()
  # r.sort()
  # print(sum(rr - ll for (rr,ll) in zip(r,l)))
  w.sort(reverse=True)

  coeff = [rr - ll for (rr,ll) in zip(r,l)]
  coeff.sort()
  # print(l)
  # print(r)
  # print(w)
  # print(coeff)
  print(sum(c*w for c,w in zip(coeff, w)))
  # print()

