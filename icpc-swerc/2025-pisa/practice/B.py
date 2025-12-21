import sys

def front(seq, n):
    for i in range(n):
        if seq[i] == -1: continue
        whats = [ii for ii in range(1, i+2) if seq[ii-1] == -1]
        if len(whats) < 2: continue
        print("?", len(whats), *whats)
        sys.stdout.flush()
        reply = int(input())
        if reply != 0:
            seq[i] = reply
    return seq

def back(seq, n):
    already = set()
    for i, s in enumerate(seq):
        if s == -1: continue
        already.add(i+1)

    for i in range(n):
        if seq[i] == -1:
            print("?", len(already)+1, *already, i+1)
            seq[i] = int(input())
    return seq

cases = int(input())
for case in range(cases):
    n = int(input())
    seq = front([-1] * (2*n), 2*n)
    seq = back(seq, 2*n)
    print("!", *seq)
    sys.stdout.flush()
