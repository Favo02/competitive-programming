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

#define int ll

void solve() {
    // cout << "----------------------------" << endl;

    int partecipants, problems;
    cin >> partecipants >> problems;

    int KEVIN;
    cin >> KEVIN;

    vector<int> a;
    for (int i = 0; i < partecipants-1; i++) {
        int x;
        cin >> x;

        if (x > KEVIN) a.push_back(x);
    }

    sort(all(a));

    vector<int> P(problems);
    for (int i = 0; i < problems; i++) {
        cin >> P[i];
    }

    sort(all(P));

    vector<int> rank(problems);
    int aa = 0;
    for (int i = 0; i < problems; i++) {
        if (P[i] <= KEVIN) rank[i] = 1;
        else {
            while (aa < a.size() && a[aa] < P[i]) aa++;
            rank[i] = a.size() - aa + 1;
        }
    }

    // dbg(KEVIN);
    // dbg(a);
    // dbg(P);
    // dbg(rank);

    sort(all(rank));

    // dbg(rank);

    // cout << "prec" << endl;


    for (int m = 1; m <= problems; m++) {
        int res = 0;
        for (int r = 0; r < rank.size(); r += m) {
            if (r+m > rank.size()) break;
            res += rank[r + m - 1];
        }
        cout << res << " ";
    }
    cout << endl;

}

int32_t main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}
