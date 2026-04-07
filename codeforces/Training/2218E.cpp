#include <bits/stdc++.h>
using namespace std;

void solve() {
    int N;
    cin >> N;
    vector<int> nums(N);
    for (int i = 0; i < N; i++)
        cin >> nums[i];

    int res = 0;
    for (int i = 0; i < N; i++)
        for (int ii = i + 1; ii < N; ii++)
            res = max(res, nums[i] ^ nums[ii]);

    cout << res << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
        solve();
}
