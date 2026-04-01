#include <algorithm>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <iostream>
#include <numeric>
#include <set>
#include <utility>
#include <vector>

using namespace std;

void solve(int t) {
    int N, K;
    cin >> N >> K;

    vector<int> C(N);
    for (int i = 0; i < N; i++)
        cin >> C[i];
    sort(C.begin(), C.end());

    vector<int> dists;
    for (int i = 0; i < N - 1; i++)
        dists.push_back(C[i + 1] - C[i]);
    sort(dists.begin(), dists.end());

    long long risposta = 0;
    for (int i = 0; i < N - K; i++)
        risposta += dists[i];

    cout << "Case #" << t << ": " << risposta << "\n";
}

int main() {
    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        solve(t);
    }

    return 0;
}
