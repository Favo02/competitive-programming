#include <bits/stdc++.h>

using namespace std;

#define ll long long
const ll MOD = 1e9 + 7;

int bfs(vector<pair<int, int>> & child, vector<int> & undernodes, int cur) {
    if (child[cur].first == 0 && child[cur].second == 0) {
        undernodes[cur] = 0;
        return 1;
    }
    bfs(child, undernodes, child[cur].first);
    bfs(child, undernodes, child[cur].second);
    undernodes[cur] = 2 + undernodes[child[cur].first] + undernodes[child[cur].second];
    return undernodes[cur];
}

void result(vector<pair<int, int>> & child, vector<int> & parent, vector<int> & undernodes, int cur, vector<int> & res) {

    if (parent[cur] == 0) {
        res[cur] = (2 * undernodes[cur] + 1) % MOD;
    } else {
        res[cur] = (2 * undernodes[cur] + 1 + res[parent[cur]]) % MOD;
    }

    if (child[cur].first != 0 && child[cur].second != 0) {
        result(child, parent, undernodes, child[cur].first, res);
        result(child, parent, undernodes, child[cur].second, res);
    }

}

void solve() {
    int n;
    cin >> n;

    vector<int> parent(n+1);
    vector<pair<int, int>> child(n+1);

    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        if (a == 0 && b == 0) continue;
        child[i + 1] = {a, b};
        parent[a] = i + 1;
        parent[b] = i + 1;
    }

    vector<int> undernodes(n+1);
    bfs(child, undernodes, 1);

    vector<int> res(n+1);
    result(child, parent, undernodes, 1, res);

    for (int i = 1; i <= n; i++) {
        cout << res[i] << " ";
    }
    cout << "\n";
}

int main() {
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        solve();
    }
}
