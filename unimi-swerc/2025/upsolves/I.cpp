#include <bits/stdc++.h>

using namespace std;

int main() {
    int P, K;
    cin >> P >> K;

    vector<int> pieces(P);
    for (int i = 0; i < P; i++) {
        cin >> pieces[i];
    }

    vector<vector<int>> kept(P, vector<int>(K + 1, 1e9));
    vector<vector<int>> rem(P, vector<int>(K + 1, 1e9));

    for (int i = 0; i < P; i++) {
        rem[i][0] = 1;
    }

    if (pieces[0] <= K) {
        kept[0][pieces[0]] = 0;
    }

    for (int p = 1; p < P; p++) {
        for (int k = 0; k <= K; k++) {
            if (k - pieces[p] >= 0) {
                kept[p][k] = min(kept[p - 1][k - pieces[p]], rem[p - 1][k - pieces[p]]);
            }

            rem[p][k] = min(rem[p - 1][k], kept[p - 1][k] + 1);
        }
    }

    for (int k = 1; k <= K; k++) {
        int r = min(kept[P - 1][k], rem[P - 1][k]);
        cout << (r == 1e9 ? -1 : r) << endl;
    }
}
