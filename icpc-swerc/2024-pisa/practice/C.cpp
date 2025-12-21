#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> weights(n);
    int summ = 0;
    for (int i = 0; i < n; i++) {
        cin >> weights[i];
        summ += weights[i];
    }

    vector<double> probs(n);
    for (int i = 0; i < n; i++) {
        cin >> probs[i];
    }

    vector<vector<double>> dp(summ+1, vector<double>(n+1, 0));
    dp[0][0] = 1;

    for (int person = 0; person < n; person++) {
        for (int weight = 0; weight < summ+1; weight++) {
            dp[weight][person+1] += dp[weight][person] * (1-probs[person]);

            if (weight + weights[person] < summ+1) {
                dp[weight+weights[person]][person+1] += dp[weight][person] * (probs[person]);
            }
        }
    }

    double res = 0.0;
    for (int row = ceil(summ/2.0); row < summ+1; row++) {
        res += dp[row][n];
    }

    cout << res << endl;
}
