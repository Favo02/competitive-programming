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
#define pii pair<int, int>

#define PI 3.1415926535897932384626433832795l
const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

void solve() {
  int n, x;
  cin >> n;

  vector<int> coord;
  for (int i = 0; i < n; i++) {
    cin >> x;
    coord.push_back(x);
  }

  vector<int> villagers;
  vector<ll> prefix;
  ll sum;
  for (int i = 0; i < n; i++) {
    cin >> x;
    sum += x;
    villagers.push_back(x);
    prefix.push_back(sum);
  }

  // dbg(coord);
  // dbg(villagers);
  // dbg(prefix);

  int q, l, r;
  cin >> q;

  for (int i = 0; i < q; i++) {
    cin >> l >> r;

    auto lb = lower_bound(all(coord), l);
    auto ub = upper_bound(all(coord), r);

    // if (lb == coord.end() || ub == coord.end()) {
    //   cout << 0 << endl;
    //   continue;
    // }

    ll start, end;

    if (lb == coord.begin()) {
      start = 0;
    } else {
      start = prefix[distance(coord.begin(), lb) - 1];
    }

    if (ub == coord.begin()) {
      end = 0;
    } else {
      end = prefix[distance(coord.begin(), ub) - 1];
    }

    cout << end - start << endl;



    // cout << lower_bound(all(coord), l) << "-" << upper_bound(all(coord), r) << endl;
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
