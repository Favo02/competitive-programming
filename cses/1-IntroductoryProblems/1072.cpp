#include <bits/stdc++.h>

using namespace std;

#pragma GCC optimize("Ofast,unroll-loops")
#pragma GCC target("avx,avx2,fma")

template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#ifdef LOCAL
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

#define ar array
#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()
#define pa pair<int, int>

#define PI 3.1415926535897932384626433832795l
const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

void solve() {
    int n;
    cin >> n;


    for (int size = 1; size <= n; size++) {

        // https://oeis.org/A172132
        // ll n = size;
        // cout << (n - 1)*(n + 4)*(n*n - 3*n + 4)/2 << endl;

        // sum of cells that are not already seen
        ll s2 = size*size;
        ll res = s2*s2 - (s2*(s2 + 1))/2;

        // number of cells that can take all 4 "forward" jumps
        ll complete = (size-4)*(size-2);
        // number of cells that are in column 1 and 2 (can take 2 and 3 jumps)
        ll c1c2 = (size-2)*2;
        // number of cells that are in second to last row (can take 2 jumps)
        ll rm2 = (size-4);
        // number of places where the first two columns intersect the second to last row (can take 1 jump)
        ll edges = 4;

        ll jumps = complete*4 + c1c2*2 + c1c2*3 + rm2*2 + edges*1;

        cout << res-jumps << endl;
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
