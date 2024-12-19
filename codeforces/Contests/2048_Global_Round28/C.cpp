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

vector<int> count(string &S, int start1, int start2, int lenght2) {
    vector<int> changed;
    for (int i = 0; i < lenght2; i++) {
        if (S[start1 + i] != S[start2 + i]) {
            changed.push_back(i);
        }
    }
    return changed;
}

void print(int a, int b, int c, int d) {
    cout << a << " " << b << " " << c << " " << d << endl;
}

void solve() {

    string S;
    cin >> S;
    int LEN = S.length();

    // cout << S << endl;

    int first_zero = S.find('0');
    if (first_zero == string::npos) {
        print(1, LEN, 1, 1);
        return;
    }

    int LEN2 = LEN - first_zero;
    // cout << first_zero << " " << LEN2 << endl;

    vector<int> best = {};
    int l = -1;
    int r = -1;
    for (int i = 0; i <= LEN-LEN2; i++) {
        vector<int> changed = count(S, first_zero, i, LEN2);
        // cout << i+1 << " " << i+LEN2 << endl;
        // dbg(changed);
        if (changed.empty()) continue;

        bool stillgoing = true;
        for (int j = 0; j < min(changed.size(), best.size()); j++) {
            if (changed[j] < best[j]) {
                stillgoing = false;
                best = changed;
                l = i;
                r = i + LEN2;
                break;
            } else if (changed[j] > best[j]) {
                stillgoing = false;
                break;
            }
        }

        if (stillgoing && changed.size() > best.size()) {
            best = changed;
            l = i;
            r = i + LEN2;
        }
    }

    print(1, LEN, l+1, r);
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "---------" << endl;
        // cout << "Case #" << t << ": ";
        solve();
    }
}
