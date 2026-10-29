#include <bits/stdc++.h>
#define ll long long
using namespace std;

const ll INF = 1e18;

void mincammino(int N, int M, vector<int> X, vector<int> Y, vector<int> P, vector<ll> &D) {

    unordered_map<int, vector<pair<int, int>>> graph;
    for (int i = 0; i < M; i++) {
        graph[X[i]].push_back({Y[i], P[i]});
    }

    fill(D.begin(), D.end(), INF);

    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;
    D[0] = 0;
    pq.push({0, 0});

    while (!pq.empty()) {
        auto [dist, from] = pq.top();
        pq.pop();
        if (dist != D[from])
            continue;

        for (auto [to, w] : graph[from]) {
            if (D[from] + w < D[to]) {
                D[to] = D[from] + w;
                pq.push({D[to], to});
            }
        }
    }

    for (int i = 0; i < N; i++) {
        if (D[i] == INF)
            D[i] = -1;
    }
}

// int main() {
//     int N, M;
//     cin >> N >> M;

//     vector<int> X(M), Y(M), P(M);
//     vector<long long> D(N);

//     for (int i = 0; i < M; i++) {
//         cin >> X[i] >> Y[i] >> P[i];
//     }

//     mincammino(N, M, X, Y, P, D);

//     for (int i = 0; i < N; i++) {
//         cout << D[i] << ' ';
//     }
//     cout << '\n';
// }
