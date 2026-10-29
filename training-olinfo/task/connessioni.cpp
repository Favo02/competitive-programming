#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> parent, sz; // sz: number of elements of the set
    int components;

    DSU(int n) {
        parent.resize(n);
        sz.assign(n, 1);
        components = n;
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) { // path compression
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }

    bool unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX == rootY)
            return false; // already in same set

        if (sz[rootX] < sz[rootY]) // union by size
            swap(rootX, rootY);

        parent[rootY] = rootX;
        sz[rootX] += sz[rootY];
        components--;
        return true;
    }
};

DSU dsu(0);

void inizia(int N) {
    dsu = DSU(N);
}

int collega(int X, int Y) {
    dsu.unite(X, Y);
    return dsu.components;
}

// int main() {
//     int N, Q;
//     cin >> N >> Q;

//     inizia(N);

//     for (int i = 0; i < Q; i++) {
//         int X, Y;
//         cin >> X >> Y;
//         cout << collega(X, Y) << "\n";
//     }
// }
