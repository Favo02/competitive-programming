#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll eni(ll n, ll exp, ll mod) {
    ll score = 1;
    unordered_map<ll, int> seen;
    vector<ll> res;
    bool cfound = false;
    for (ll i = 0; i < exp; i++) {
        score = score * n % mod;
        if (i >= 5 && !cfound && seen.count(score)) {
            ll cycle = i - seen[score];
            cfound = true;
            i = exp - ((exp - i) % cycle);
        }
        if (i < exp) {
            res.push_back(score);
            seen[score] = i;
        }
    }

    string strres;
    for (int i = 0; i < min(5, (int)res.size()); i++) {
        strres += to_string(res[res.size() - 1 - i]);
    }
    return stoll(strres);
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
