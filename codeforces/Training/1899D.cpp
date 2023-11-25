#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

vector<int> read_vector(int len) {
  vector<int> arr;
  int n;
  while (len-- > 0) {
    cin >> n;
    arr.push_back(n);
  }
  return arr;
}

void print_map(const map<int,int>& map) {
  for (pair<int,int> pair : map)
    cout << pair.first << ": " << pair.second << "\n";
}

void solve() {
  int len;
  cin >> len;

  vector<int> arr = read_vector(len);
  map<int,int> occs;

  ll res = 0;

  for (int n : arr) {
    if (n == 1) n = 2;
    if (occs[n] > 0) {
      res += occs[n];
    }
    occs[n] += 1;
  }

  cout << res << "\n";
}

int main() {
  int cases;
  cin >> cases;
  while (cases-- > 0) solve();
}
