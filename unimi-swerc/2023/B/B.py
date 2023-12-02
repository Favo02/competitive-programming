t = [int(n) for n in input().split(" ")]

print(max([t[0]*t[2], t[0]*t[3], t[1]*t[2], t[1]*t[3]]))
