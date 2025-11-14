#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll eni(ll n, ll exp, ll mod) {
    ll score = 1;
    unordered_map<ll, int> seen;
    vector<ll> res;
    ll sum = 0;
    bool cfound = false;
    for (ll i = 0; i < exp; i++) {
        score = score * n % mod;
        if (i >= 5 && !cfound && seen.count(score)) {
            ll cycle = i - seen[score];
            cfound = true;
            ll skipping = ((exp - i) / cycle);
            i = exp - ((exp - i) % cycle);
            sum += skipping * ((sum + score) - res[seen[score]]);
        }
        if (i < exp) {
            sum += score;
            res.push_back(sum);
            seen[score] = i;
        }
    }

    cout << sum << endl;
    return sum;
}

// NOTE: the input is manually simplified:
// remove all letters=
// add number of lines at start
int main() {
    int lines;
    cin >> lines;
    ll a, b, c, x, y, z, m;
    ll res = 0;
    for (int i = 0; i < lines; i++) {
        cin >> a >> b >> c >> x >> y >> z >> m;
        res = max(res, eni(a, x, m) + eni(b, y, m) + eni(c, z, m));
    }

    cout << res << endl;
}
