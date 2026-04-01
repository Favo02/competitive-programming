#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000;
const int MAXM = 1000;

int solve() {
    int N, M;
    cin >> N >> M;

    vector<int> V(N), G(M);

    for (int i = 0; i < N; i++)
        cin >> V[i];
    for (int i = 0; i < M; i++)
        cin >> G[i];

    vector<vector<int>> mem(MAXN, vector<int>(MAXM, -1));

    function<int(int, int)>
        rec = [&](int ni, int mi) {
            if (ni >= N)
                return 0;
            if (mi >= M)
                return N - ni;
            if (mem[ni][mi] != -1)
                return mem[ni][mi];

            int res = 0;
            if (V[ni] < G[mi])
                res = 2 + rec(ni + 1, mi + 1);
            res = max(res, 1 + rec(ni + 1, mi));
            res = max(res, rec(ni, mi + 1));
            return mem[ni][mi] = res;
        };

    return rec(0, 0);
}

int main() {
    int T, t;
    cin >> T;

    for (t = 1; t <= T; t++) {
        cout << "Case #" << t << ": " << solve() << endl;
    }
}
