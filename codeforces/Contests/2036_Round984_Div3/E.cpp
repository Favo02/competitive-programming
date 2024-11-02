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
    int n, k, q;
    cin >> n >> k >> q;

    vector<vector<int>> reg(k, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int ii = 0; ii < k; ii++) {
            cin >> reg[ii][i];

            if (i != 0) {
                reg[ii][i] |= reg[ii][i-1];
            }
        }
    }

    // dbg(reg);

    int m;
    for (int i = 0; i < q; i++) {
        cin >> m;

        int minn, maxx;
        minn = 0;
        maxx = reg[0].size();

        for (int ii = 0; ii < m; ii++) {
            int region, value;
            char sign;
            cin >> region >> sign >> value;
            region--;
            // dbg(reg[region]);
            // cout << region << sign << value << endl;


            if (sign == '>') {
                // cout << distance(reg[region].begin(), upper_bound(all(reg[region]), value)) << endl;
                minn = max(minn, (int)distance(reg[region].begin(), upper_bound(all(reg[region]), value)));

            } else {
                // cout << distance(reg[region].begin(), lower_bound(all(reg[region]), value)) << endl;
                maxx = min(maxx, (int)distance(reg[region].begin(), lower_bound(all(reg[region]), value)));
            }

            // cout << minn << '-' << maxx << endl;
        }

        if (minn >= maxx) {
            cout << -1 << endl;
        } else if (minn >= reg[0].size()) {
            cout << -1 << endl;
        } else {
            cout << minn+1 << endl;
        }
    }
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
