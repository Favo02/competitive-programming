#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, cnt = 1;
    cin >> n;
    vector<int> v(n), l;
    for (auto &x : v)
        cin >> x;
    for (int i = 1; i < n; i++) {
        if (v[i] <= v[i - 1]) {
            l.push_back(cnt);
            cnt = 0;
        }
        cnt++;
    }
    l.push_back(cnt);
    if (l.size() > 2) {
        cout << l[1] << "\n";
    } else if (l.size() == 2) {
        int last = v[l[0] - 1], nxt = v[l[0]];
        cout << last / (nxt - 1) << "\n";
    } else {
        int delta = v[n - 1] - v[n - 2];
        cout << max(delta, v[n - 1] / delta) << "\n";
    }
}

int main() {
    int t;
    cin >> t;
    while (t--)
        solve();
}
