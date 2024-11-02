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

vector<string> field;

bool valid(char a, char b, char c, char d) {
    // cout << a << b << c << d << endl;
    return (a == '1' && b == '5' && c == '4' && d == '3');
}

// dirs = 0 >, 1 v, 2 <, 3 ^
tuple<int, int, int> next(int r, int c, int startr, int startc, int w, int h, int dir) {
    // cout << field[r][c] << " " << dir;

    if (dir == 0) { // right
        if (c == startc+w-1) {
            return {r+1, startc+w-1, 1};
        } else {
            return {startr, c+1, 0};
        }

    } else if (dir == 1) { // down
        if (r == startr+h-1) {
            return {startr+h-1, c-1, 2};
        } else {
            return {r+1, startc+w-1, 1};
        }

    } else if (dir == 2) { // left
        if (c == startc) {
            return {r-1, startc, 3};
        } else {
            return {startr+h-1, c-1, 2};
        }

    } else if (dir == 3) { // up
        if (r == startr) {
            return {startr, c+1, 0};
        } else {
            return {r-1, startc, 3};
        }
    }

    assert(false);
}

void solve() {
    int R, C;
    cin >> R >> C;

    field = vector<string>(R);
    for (int i = 0; i < R; i++) {
        cin >> field[i];
        assert(field[i].size() == C);
    }

    ll res = 0;

    // dbg(field);


    int h = R;
    int w = C;

    int startr = 0;
    int startc = 0;

    while (h > 0 && w > 0) {

        ll size = w + (h-1) + (w-1) + (h-1) + 2;
        char last1 = '-';
        char last2 = '-';
        char last3 = '-';
        char last4 = '-';

        int dir = 0;
        int r = startr;
        int c = startc;

        // cout << startr << " " << startc << " " << h << " " << w << " " << dir << endl;

        while (size > 0) {
            last4 = field[r][c];

            if (valid(last1, last2, last3, last4)) {
                res++;
            }

            auto nnn = next(r, c, startr, startc, w, h, dir);
            // cout << get<2>(nnn) << endl;
            r = get<0>(nnn);
            c = get<1>(nnn);
            dir = get<2>(nnn);

            last1 = last2;
            last2 = last3;
            last3 = last4;

            size--;
        }

        h -= 2;
        w -= 2;
        startr++;
        startc++;
        // cout << "--" << endl;
    }

    cout << res << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #############" << t << endl;
        solve();
    }
}
