#include <bits/stdc++.h>

using namespace std;

#pragma GCC optimize("Ofast,unroll-loops")
#pragma GCC target("avx,avx2,fma")

template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)

#define ar array
#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

#define PI 3.1415926535897932384626433832795l
const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

void solve() {
    int n, m;
    cin >> n >> m;

    vector<pair<int, int>> pairs(n);
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        pairs[i] = {a, b};
    }

    sort(all(pairs));

    vector<int> suffix_min(n);
    int last = 1e9;
    for (int i = n-1; i >= 0; i--) {
        suffix_min[i] = min(last, pairs[i].second);
        last = suffix_min[i];
    }

    // dbg(pairs);
    // dbg(suffix_min);

    ll res = 0;

    for (int miss = 1; miss < pairs[0].first; miss++) {
        // cout << "miss: " << miss << " " << m - miss << endl;
        res += suffix_min[0] - miss;
    }

    last = -1;
    for (int i = 0; i < n; i++) {
        if (pairs[i].first == last) continue;
        if (i == 0) last = pairs[i].first;

        int upper = suffix_min[i];
        // cout << "UPPER: " << upper << endl;

        for (int miss = last + 1; miss < pairs[i].first; miss++) {
            // cout << "miss: " << miss << " " << upper - miss << endl;
            res += upper-miss;
        }

        res += upper - pairs[i].first;
        // cout << "pair: " << pairs[i] << " " << upper - pairs[i].first << endl;

        last = pairs[i].first;
    }

    for (int miss = pairs[n-1].first + 1; miss <= m; miss++) {
        // cout << "miss: " << miss << " " << m - miss << endl;
        res += m-miss + 1;
    }


    cout << res << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    // cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}
