#include <bits/stdc++.h>
using namespace std;

void solve() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        cout << (2 * i + 1) * (2 * i + 3) << " ";
    }
    cout << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
        solve();
}
