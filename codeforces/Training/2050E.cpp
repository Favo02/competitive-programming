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

string a, b, c;

vector<vector<int>> dp;

int recdp(int ai, int bi) {
    int ci = ai + bi;
    if (ci == c.length()) return 0;

    if (dp[ai][bi] != -1) return dp[ai][bi];

    int res;

    if (ai == a.length()) {
        if (b[bi] != c[ci]) res = 1 + recdp(ai, bi+1);
        else res = recdp(ai, bi+1);
    } else if (bi == b.length()) {
        if (a[ai] != c[ci]) res = 1 + recdp(ai+1, bi);
        else res = recdp(ai+1, bi);
    } else {
        int takea = recdp(ai+1, bi);
        if (a[ai] != c[ci]) takea++;

        int takeb = recdp(ai, bi+1);
        if (b[bi] != c[ci]) takeb++;
        res = min(takea, takeb);
    }

    dp[ai][bi] = res;
    return res;
}

void solve() {
    cin >> a >> b >> c;
    dp = vector<vector<int>>(a.length()+1, vector<int>(b.length()+1, -1));
    cout << recdp(0, 0) << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}
