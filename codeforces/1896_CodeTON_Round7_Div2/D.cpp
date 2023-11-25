#include <bits/stdc++.h>
using namespace std;

bool check(vector<int> arr, int target) {
  int sum = arr[0];
  size_t start = 0;

  for (size_t i = 1; i <= arr.size(); i++) {
    while (sum > target && start < i - 1) {
      sum -= arr[start];
      start++;
    }

    if (sum == target)
      return true;

    if (i < arr.size())
      sum += arr[i];
  }
  return false;
}

int main() {
  int cases;
  cin >> cases;

  while(cases-- > 0) {
    int n, q;
    cin >> n >> q;
    vector<int> arr;

    while (n-- > 0) {
      int num;
      cin >> num;
      arr.push_back(num);
    }

    while (q-- > 0) {
      int op;
      cin >> op;
      if (op == 1) {
        int targetSum;
        cin >> targetSum;

        if (targetSum > arr.size() * 2)
          cout << "NO\n";
        else if (check(arr, targetSum))
          cout << "YES\n";
        else
          cout << "NO\n";
      }
      else {
        int a, b;
        cin >> a >> b;
        arr[a-1] = b;
      }
    }
  }
}
