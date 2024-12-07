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

vector<vector<int>> tree;

pair<bool, int> recsolve(int start, int prec) {
    if (tree[start].size() == 1 && tree[start][0] == prec) {
        return {false, 0};
    }

    int res = 0;
    bool used = false;
    for (auto ad : tree[start]) {
        if (ad == prec) continue;
        auto [aused, ares] = recsolve(ad, start);
        res += ares;
        if (aused || used) continue;
        res++;
        used = true;
    }
    return {used, res};
}

void solve() {
    int n;
    cin >> n;

    tree = vector<vector<int>>(n);

    int f, t;
    for (int i = 0; i < n-1; i++) {
        cin >> f >> t;
        f--;
        t--;
        tree[f].push_back(t);
        tree[t].push_back(f);
    }

    cout << recsolve(0, -1).second << endl;
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
