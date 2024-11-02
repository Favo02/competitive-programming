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
    string s;
    cin >> s;

    // dbg(s);

    set<int> starts;
    for (int i = 0; i < s.size()-3; i++) {
        if (s[i] == '1' && s[i+1] == '1' && s[i+2] == '0' && s[i+3] == '0') {
            starts.insert(i);
        }
    }

    // dbg(starts);

    int q;
    cin >> q;

    int tc, neww;

    for (int i = 0; i < q; i++) {
        cin >> tc >> neww;

        if (neww == 1) {
            s[tc-1] = '1';
        } else {
            s[tc-1] = '0';
        }

        for (int iii = max(tc-4, 0); iii < min((int)(s.size()-3), tc); iii++) {
            if (s[iii] == '1' && s[iii+1] == '1' && s[iii+2] == '0' && s[iii+3] == '0') {
                starts.insert(iii);
            } else {
                starts.erase(iii);
            }
        }

        if (starts.size() > 0) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case ####################" << t << endl;
        solve();
    }
}
