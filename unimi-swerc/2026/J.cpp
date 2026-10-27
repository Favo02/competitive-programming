#include <bits/stdc++.h>
#define ll long long
#define MOD 1000000007
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<ll> nums(N);
    for (int i = 0; i < N; i++)
        cin >> nums[i];

    vector<ll> prefix;
    prefix.push_back(0);
    for (int i = 0; i < N; i++)
        prefix.push_back(prefix.back() + nums[i]);

    vector<ll> dp(N, 1);

    ll res = 1;
    for (int div = 1; div < N; div++) {
        vector<ll> newdp(N, 0);
        vector<ll> sumrem(div + 1, 0);
        for (int i = 0; i < N; i++) {
            int rem = prefix[i + 1] % (div + 1);
            newdp[i] = sumrem[rem];
            sumrem[rem] = (sumrem[rem] + dp[i]) % MOD;
        }
        dp = newdp;
        res = (res + dp.back()) % MOD;
    }

    cout << res << endl;
}
