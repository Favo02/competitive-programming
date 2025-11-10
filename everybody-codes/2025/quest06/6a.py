s = input()

res = 0
mentors = 0
for c in s:
    if c == 'A': mentors += 1
    if c == 'a': res += mentors
print(res)
