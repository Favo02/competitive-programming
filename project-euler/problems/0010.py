# sieve of eratosthenes
def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

res = 0
gen = gen_primes()
while True:
    n = next(gen)
    if n >= 2_000_000:
        break
    res += n
print(res)
