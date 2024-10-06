#include <bits/stdc++.h>
using namespace std;

vector<int> read_vector(int len) {
  vector<int> arr;
  int n;
  while (len-- > 0) {
    cin >> n;
    arr.push_back(n);
  }
  return arr;
}

void print_vector(const vector<int>& arr) {
  for (int n : arr)
    cout << n << " ";
  cout << "\n";
}

void solve() {
  int len;
  cin >> len;
  vector<int> arr = read_vector(len);

  int max = arr[0];
  int min = arr[0];
  for (int n : arr) {
    if (n > max) max = n;
    if (n < min) min = n;
  }

  vector<int> ops;
  int res = 0;
  while (max != min) {
    int x = ((min % 2 == 0) ? 0 : 1);
    max = (max+x) / 2;
    min = (min+x) / 2;
    res++;
    // cout << "m " << max << " " << min << "\n";
    if (ops.size() <= len)
      ops.push_back(x);
  }

  cout << res << "\n";
  if (res <= len) {
    print_vector(ops);
  }

}

int main() {
  int cases;
  cin >> cases;
  while (cases-- > 0) solve();
}