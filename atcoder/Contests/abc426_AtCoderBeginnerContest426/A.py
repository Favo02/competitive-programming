vers = ["Ocelot", "Serval", "Lynx"]
a, b = input().split()
ai = vers.index(a)
bi = vers.index(b)

if ai >= bi:
    print("Yes")
else:
    print("No")
