#include <bits/stdc++.h>
#define ll long long
using namespace std;

vector<vector<ll>> mem(19);

vector<ll> generate(int digits) {
    if (mem[digits].size() > 0) {
        return mem[digits];
    }

    if (digits == 1) {
        mem[digits] = vector<ll>{3, 6, 9};
        return vector<ll>{3, 6, 9};
    }

    vector<ll> res;
    for (ll r : vector<ll>{3, 6, 9}) {
        ll p = pow(10, digits-2);
        for (ll rec : generate(digits-1)) {
            if (r % 10 == rec / p) continue;
            res.push_back(r * (ll)(pow(10, digits-1)) + rec);
        }
    }

    mem[digits] = res;
    return res;
}

long long occulta(int N, int M) {
    generate(N);

    ll res = 0;
    for (int i = 0; i <= N; i++) {
        for (ll num : mem[i]) {
            res = max(res, num % M);
        }
    }

    return res;
}

int main() {
    FILE *fr, *fw;
    int T, N, M, i;

    fr = fopen("input.txt", "r");
    fw = fopen("output.txt", "w");
    assert(1 == fscanf(fr, "%d", &T));
    for (i=0; i<T; i++) {
        assert(2 == fscanf(fr, "%d %d", &N, &M));
        fprintf(fw, "%d ", occulta(N, M));
    }

    fprintf(fw, "\n");
    fclose(fr);
    fclose(fw);
    return 0;
}
