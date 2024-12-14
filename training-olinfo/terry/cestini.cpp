#include <bits/stdc++.h>
using namespace std;

void solve() {
    int N, M, Q;
    string S;
    cin >> N >> M >> Q >> S;

    vector<vector<char>> bins(M);
    for (char s : S) bins[0].push_back(s);

    for (int i = 0; i < Q; i++) {
        char type;
        int a, b;
        cin >> type >> a >> b;

        if (type == 's') {
            bins[b].push_back(bins[a].back());
            bins[a].pop_back();
        } else {
            cout << bins[a][b];
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
