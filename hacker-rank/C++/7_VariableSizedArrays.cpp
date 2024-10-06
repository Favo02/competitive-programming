#include <bits/stdc++.h>
using namespace std;

#define PB push_back
typedef vector<int> vi;

int main() {
    int n, q;
    cin >> n >> q;

    vi arrs[n];

    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        vi arr;
        for (int j = 0; j < k; j++) {
            int temp;
            cin >> temp;
            arr.PB(temp);
        }
        arrs[i] = arr;
    }

    for (int i = 0; i < q; i++) {
        int a, b;
        cin >> a >> b;
        cout << arrs[a][b] << "\n";
    }
}
