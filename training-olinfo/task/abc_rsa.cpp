#include <bits/stdc++.h>
#define ll long long
using namespace std;

int modpow(ll x, unsigned int y, int p) {
    int res = 1;
    x %= p;

    if (x == 0) return 0;

    while (y > 0) {
        if (y % 2 == 1) {
            res = (res*x) % p;
        }
        y /= 2;
        x = (x*x) % p;
    }
    return res;
}

void decifra(int N, int d, int L, int* messaggio, char* plaintext) {
    for (int i = 0; i < L; i++) {
        plaintext[i] = modpow(messaggio[i], d, N);
    }
}
