#include <bits/stdc++.h>
using namespace std;
#define ll long long

int m(int n, int mod) {
    return ((n % mod) + mod) % mod;
}

// NOTE: the input is manually simplified to this format
// 4
// 1 2
// 2 3
// 3 4
// 4 4
int main() {
    int disc;
    cin >> disc;

    ll res = 0;
    int x, y, mod;
    for (int i = 0; i < disc; i++) {
        cin >> x >> y;
        mod = x - 1 + y;
        res += (m(x - 1 + 100, mod) + 1) + (m(y - 1 - 100, mod) + 1) * 100;
    }
    cout << res << endl;
}
