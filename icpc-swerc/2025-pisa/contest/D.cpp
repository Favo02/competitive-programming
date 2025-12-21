#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    map<int, int> mp;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        mp[x]++;
    }
    int res = 0;
    for (auto [a, b] : mp) {
        if (b < a)
            res += b;
        else
            res += (b - a);
    }
    cout << res << endl;
}
