#include <bits/stdc++.h>
using namespace std;

void solve(int t) {
    int N, A, B;
    cin >> N >> A >> B;

    unordered_map<int, vector<int>> graph;
    deque<int> queue;
    vector<int> dists(N, 1e9);

    int single;
    for (int i = 0; i < A; i++) {
        cin >> single;
        queue.push_back(single);
        dists[single] = 1;
    }
    int a, b;
    for (int i = 0; i < B; i++) {
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    while (!queue.empty()) {
        auto cur = queue.front();
        queue.pop_front();

        for (auto &adj : graph[cur]) {
            if (dists[cur] + 1 < dists[adj]) {
                dists[adj] = dists[cur] + 1;
                queue.push_back(adj);
            }
        }
    }

    int ir = -1, r = 0;
    for (int i = 0; i < N; i++) {
        if (dists[i] != 1e9 && dists[i] >= r) {
            ir = i;
            r = dists[i];
        }
    }

    cout << "Case #" << t << ": " << ir << " " << r << "\n";
}

int main() {
    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        solve(t);
    }

    return 0;
}
