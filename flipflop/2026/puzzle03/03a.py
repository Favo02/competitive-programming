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
    score = len(psw) * sum(mults)
    if score > bestscore:
        best = psw
        bestscore = score
print(best)
