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

vector<ll> stree;

ll pow2(ll a) {
    ll n = 1;
    while (n < a) {
        n *= 2;
    }
    return n;
}

vector<ll> build(vector<ll> arr) {
    ll size = pow2(arr.size());
    arr.resize(size, -1);

    vector<vector<ll>> pieces;
    pieces.push_back(arr);

    while (size > 1) {
        auto a = pieces[pieces.size() - 1];
        vector<ll> newp;
        for (ll i = 0; i < size; i += 2) {
            newp.push_back(a[i] ^ a[i+1]);
        }
        pieces.push_back(newp);
        size /= 2;
    }

    vector<ll> stree;
    for (ll i = pieces.size()-1; i >= 0; i--) {
        stree.insert(stree.end(), pieces[i].begin(), pieces[i].end());
    }

    return stree;
}

ll query(ll i, ll lbound, ll rbound, ll l, ll r) {
    if (l == lbound && r == rbound) {
        return stree[i];
    }

    ll mid = (lbound + rbound) / 2;
    if (l >= lbound && r <= mid) {
        return query(2*i + 1, lbound, mid, l, r);
    } else if (l >= mid && r <= rbound) {
        return query(2*i + 2, mid, rbound, l, r);
    }

    return query(2*i + 1, lbound, mid, l, mid) ^ query(2*i + 2, mid, rbound, mid, r);
}

void solve() {
    ll n, q;
    cin >> n >> q;

    vector<ll> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];

    stree = build(nums);

    n = pow2(n);

    ll a, b;
    for (int i = 0; i < q; i++) {
        cin >> a >> b;

        cout << query(0, 0, n, a-1, b) << endl;
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
