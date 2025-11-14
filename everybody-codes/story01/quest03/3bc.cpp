#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll extended_euclidean(ll a, ll b, ll &x, ll &y) {
    x = 1, y = 0;
    ll x1 = 0, y1 = 1, a1 = a, b1 = b;
    while (b1) {
        ll q = a1 / b1;
        tie(x, x1) = make_tuple(x1, x - q * x1);
        tie(y, y1) = make_tuple(y1, y - q * y1);
        tie(a1, b1) = make_tuple(b1, a1 - q * b1);
    }
    return a1;
}

ll mod_inv(ll a, ll m) {
    ll x, y;
    ll g = extended_euclidean(a, m, x, y);
    if (g != 1) {
        return -1;
    } else {
        x = (x % m + m) % m;
        return x;
    }
}

struct Congruence {
    ll a, m;
};

ll chinese_remainder_theorem(vector<Congruence> const &congruences) {
    ll M = 1;
    for (auto const &congruence : congruences) {
        M *= congruence.m;
    }

    ll solution = 0;
    for (auto const &congruence : congruences) {
        ll a_i = congruence.a;
        ll M_i = M / congruence.m;
        ll N_i = mod_inv(M_i, congruence.m);
        solution = (solution + a_i * M_i % M * N_i) % M;
    }
    return solution;
}

// NOTE: the input is manually simplified to this format
// 4
// 1 2
// 2 3
// 3 4
// 4 4
int main() {
    ll disc;
    cin >> disc;

    ll x, y, mod;
    vector<Congruence> congrs;

    for (ll i = 0; i < disc; i++) {
        cin >> x >> y;
        x--;
        mod = x + y;

        congrs.push_back(Congruence{mod - 1 - x, mod});
    }

    cout << chinese_remainder_theorem(congrs) << endl;

    // xs[i] + x = mods[i]-1 (mod mods[i])
    // 11 + x = 12 (mod 13)
    // 7 + x = 10 (mod 11)

    // x = mods[i]-1 - xs[i] (mod mods[i])
    // x = 1 (mod 13)
    // x = 3 (mod 11)
}
