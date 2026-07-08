import sys
from itertools import chain

psws = sys.stdin.readlines()

def score(char):
    totscore = 0
    for psw in psws:
        psw = psw.strip() + char

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

        longestsub = ""
        subs = psw[0]
        for c in psw[1:]:
            if c == subs[-1]:
                subs += c
            else:
                if len(subs) > len(longestsub):
                    longestsub = subs
                subs = c
        if len(subs) > len(longestsub):
            longestsub = subs
        if len(longestsub) >= 3:
            score += len(longestsub)**2

        if "red" in psw or "green" in psw or "blue" in psw:
            score *= 3

        score *= len(psw)
        totscore += score
    return totscore

print(max(score(chr(c)) for c in chain(range(ord('a'), ord('z')+1), range(ord('A'), ord('Z')+1), range(ord('0'), ord('9')+1))))
