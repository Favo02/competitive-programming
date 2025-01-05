#include <bits/stdc++.h>
using namespace std;

void solve() {
    int N1, N2, N3, N4, M;
    cin >> N1 >> N2 >> N3 >> N4 >> M;

    string strs[4];
    cin >> strs[0] >> strs[1] >> strs[2] >> strs[3];

    for (int start = 0; start <= N1 - M; start++) {
        string virus = strs[0].substr(start, M);

        vector<int> res(4, -1);
        res[0] = start;

        for (int i = 1; i < 4; i++) {
            auto f = strs[i].find(virus);
            if (f == string::npos) break;
            res[i] = f;
        }

        if (res[3] != -1) {
            for (auto r : res) cout << r << " ";
            break;
        }
    }
}

int main() {
    int cases;
    cin >> cases;

    for (int i = 0; i < cases; i++) {
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << endl;
    }
}
