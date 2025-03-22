string = input().strip()
print(len([s for s in string if ord('a') <= ord(s) <= ord('z') or ord('A') <= ord(s) <= ord('Z')]))
