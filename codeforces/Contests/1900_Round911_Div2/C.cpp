#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;

void print_vector(const vector<int>& arr) {
  for (int n : arr)
    cout << n << " ";
  cout << "\n";
}

void solve() {
  int len;
  string dirs;
  cin >> len >> dirs;
  vector<pair<int,int>> tree;
  vi leafs;
  vi parent(len);
  parent[0] = -1;

  for (int i = 0; len-- > 0; i++) {
    int l,r;
    cin >> l >> r;
    l--; r--;
    tree.push_back(make_pair(l,r));
    if (l == -1 && r == -1)
      leafs.push_back(i);
    if (l != -1)
      parent[l] = i;
    if (r != -1)
      parent[r] = i;
  }

  // print_vector(leafs);
  // print_vector(parent);
  // cout << "\n\n";

  int res = INT_MAX;
  for (int l : leafs) {
    int mods = 0;

    int cur = l;
    while (true) {
      int par = parent[cur];
      if (par == -1)
        break;
      char parDir = dirs[par];
      // cout << "cur" << cur << " par" << par << " dir" << parDir << "\n";
      if (parDir == 'U') {
        // cout << "inc\n";
        mods++;
      }
      else {
        int target = (parDir == 'L') ? tree[par].first : tree[par].second;
        if (target != cur) {
          // cout << "inc\n";
          mods++;
        }
      }

      cur = par;
    }

    res = min(res, mods);
  }

  cout << res << "\n";
}

int main() {
  int cases;
  cin >> cases;
  while (cases-- > 0) solve();
}
