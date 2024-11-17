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

    ll h, pu, end;
    cin >> h >> pu >> end;

    ll power = 1;

    map<ll, ll> power_required;

    ll l, r;
    for (int i = 0; i < h; i++) {
        cin >> l >> r;
        // cout << format("{} {}-{}req: {}", l, l, r, r-l+2) << endl;
        power_required[l] = r-l+2;
    }

    vector<pair<ll, ll>> ups;
    ll pos, val;
    for (int i = 0; i < pu; i++) {
        cin >> pos >> val;
        ups.push_back({pos, val});
    }

    for (auto p : ups) {
        // cout << p.first << ": ";
        // dbg(p.second);
    }

    vector<ll> available;
    int ups_index = 0;
    int res = 0;

    // cout << endl;

    for (auto req : power_required) {
        for (int ui = ups_index; ui < ups.size(); ui++) {
            int pos = ups[ui].first, val = ups[ui].second;
            if (pos > req.first) {
                break;
            }
            available.push_back(val);
            push_heap(all(available));
            ups_index++;
        }

        // dbg(req);
        // dbg(available);

        while (!available.empty() && power < req.second) {
            pop_heap(all(available));
            // cout << "use " << available.back() << endl;
            power += available.back();
            available.pop_back();
            res++;
        }

        // dbg(power);
        // cout << endl;

        if (power < req.second) {
            cout << -1 << endl;
            return;
        }
    }

    cout << res << endl;
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
