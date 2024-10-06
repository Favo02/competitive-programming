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
  int cells, t, queries, q, x;
  cin >> cells >> t >> queries;

  vector<int> teachers;
  for (int i = 0; i < t; i++) {
    cin >> x;
    teachers.push_back(x);
  }
  sort(all(teachers));

  // dbg(teachers);

  int res = 0;

  for (int i = 0; i < queries; i++) {
    cin >> q;
    // cout << q << ": ";

    auto ge = lower_bound(all(teachers), q);
    auto gr = upper_bound(all(teachers), q);

    if (ge != teachers.end() && teachers[distance(teachers.begin(), ge)] == q) {
      cout << 0 << endl;
      continue;
    }

    // it is guaranteed that q != a teacher

    // no before
    if (ge == teachers.begin()) {
      cout << teachers[0]-1 << endl;
      continue;
    }
    // no after
    if (gr == teachers.end()) {
      cout << cells - teachers[t-1] << endl;
      continue;
    }

    int bef = teachers[distance(teachers.begin(), ge)-1];
    int aft = teachers[distance(teachers.begin(), gr)];
    int distance = (aft - bef);
    if (distance % 2 == 1) {
      distance--;
    }
    cout << distance / 2 << endl;

  }

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
