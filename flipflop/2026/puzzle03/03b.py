import sys

psws = sys.stdin.readlines()
best = ""
bestscore = 0
for psw in psws:
    mults = [False, False, False]
    for c in psw:
        if 'a' <= c <= 'z':
            mults[0] = True
        if 'A' <= c <= 'Z':
            mults[1] = True
        if '0' <= c <= '9':
            mults[2] = True
    score = sum(mults)
    if set(filter(lambda l: '0' <= l <= '9', psw)) == {'7'}:
        score += 7
    if "red" in psw or "green" in psw or "blue" in psw:
        score *= 3
    longestsub = ""
    subs = " "
    for c in psw:
        if c == subs[-1]:
            subs += c
        else:
            if len(subs) > len(longestsub):
                longestsub = subs
            subs = c
    if len(longestsub) >= 3:
        score += len(longestsub)**2

    score *= len(psw)
    if score > bestscore:
        best = psw
        bestscore = score
print(best)
