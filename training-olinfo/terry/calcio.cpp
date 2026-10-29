#include <bits/stdc++.h>
using namespace std;

void solve(int t) {
    int R, C, K, A, B;
    cin >> R >> C >> K >> A >> B;

    vector<pair<int, int>> trees(K);
    for (int i = 0; i < K; i++)
        cin >> trees[i].first >> trees[i].second;

    vector<vector<int>> prefix(R, vector<int>(C, 0));

    for (int i = 0; i < K; i++)
        prefix[trees[i].first][trees[i].second]++;

    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            if (r == 0 && c == 0)
                continue;
            else if (r == 0)
                prefix[r][c] += prefix[r][c - 1];
            else if (c == 0)
                prefix[r][c] += prefix[r - 1][c];
            else
                prefix[r][c] += prefix[r][c - 1] + (prefix[r - 1][c] - prefix[r - 1][c - 1]);
        }
    }

    int res = 1e9;
    for (int r = A - 1; r < R; r++) {
        for (int c = B - 1; c < C; c++) {
            int cur = prefix[r][c];
            if (r != A - 1 && c != B - 1) {
                cur -= prefix[r - A][c];
                cur -= prefix[r][c - B];
                cur += prefix[r - A][c - B];
            } else if (r != A - 1) {
                cur -= prefix[r - A][c];
            } else if (c != B - 1) {
                cur -= prefix[r][c - B];
            }
            res = min(res, cur);
        }
    }
    cout << "Case #" << t << ": " << res << endl;
}

int main() {
    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        solve(t);
    }

    return 0;
}
