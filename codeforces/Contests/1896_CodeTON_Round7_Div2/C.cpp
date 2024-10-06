#include <bits/stdc++.h>
using namespace std;

int main() {
  int cases;
  cin >> cases;

  while(cases-- > 0) {
    int len, len2, x;
    cin >> len >> x;
    len2 = len;
    vector<int> a, b;

    while (len-- > 0) {
      int num;
      cin >> num;
      a.push_back(num);
    }
    while (len2-- > 0) {
      int num;
      cin >> num;
      b.push_back(num);
    }

    vector<int> oldA = vector<int>(a);

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    rotate(a.begin(),a.end()-x,a.end());

    vector<int> result;

    for (size_t j = 0; j < oldA.size(); j++) {
      if (x < 0) break;

      int elem = oldA[j];

      int i = find(a.begin(), a.end(), elem) - a.begin();
      a[i] = -1;
      if (elem > b[i]) {
        x--;
      }
      result.push_back(b[i]);
    }

    if (x != 0) {
      cout << "NO\n";
    }
    else {
      cout << "YES\n";
      for(int x : result) {
        cout << x << " ";
      }
      cout << "\n";
    }


  }
}
