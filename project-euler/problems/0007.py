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

gen = gen_primes()
i = 0
while i < 10001:
    n = next(gen)
    if i+1 == 10001:
        print(n)
    i += 1
