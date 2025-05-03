import string

s = input()

valid = set(string.ascii_lowercase)

print((valid - set(s)).pop())
