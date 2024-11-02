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

vector<pair<int, int>> DIRS = {{-1, 0}, {+1, 0}, {0, +1}, {0, -1}};

ll ssolve(vector<vector<bool>> field, int sr, int sc, int rem) {
    field[sr][sc] = false;

    ll res = 0;
    for (auto dir : DIRS) {
        int dr = dir.first, dc = dir.second;

        if (!(0 <= sr+dr && sr+dr < field.size())) continue;
        if (!(0 <= sc+dc && sc+dc < field[0].size())) continue;

        if (field[sr+dr][sc+dc]) {
            field[sr+dr][sc+dc] = false;
            if (rem == 1) {
                res++;
            } else {
                res += ssolve(field, sr+dr, sc+dc, rem-1);
            }
            field[sr+dr][sc+dc] = true;
        }
    }

    return res;
}

void solve() {
    int h, w, k;
    cin >> h >> w >> k;

    vector<vector<bool>> field = vector<vector<bool>>(h, vector<bool>(w, false));
    for (int i = 0; i < h; i++) {
        string line;
        cin >> line;
        for (int j = 0; j < w; j++) {
            if (line[j] == '.') {
                field[i][j] = true;
            }
        }
    }

    // dbg(field);

    ll res = 0;
    for (int r = 0; r < h; r++) {
        for (int c = 0; c < w; c++) {
            if (!field[r][c]) continue;

            res += ssolve(field, r, c, k);

        }
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
