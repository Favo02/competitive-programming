#include <bits/stdc++.h>
using namespace std;

class SegTree {
public:
    vector<int> tree;
    int n;

    int op(int a, int b) { return max(a, b); }
    int neutral = 0;

    void build(vector<int> &v, int node, int l, int r) {
        if (l == r) {
            tree[node] = v[l];
            return;
        }
        int mid = (l + r) / 2;
        build(v, 2 * node, l, mid);
        build(v, 2 * node + 1, mid + 1, r);
        tree[node] = op(tree[2 * node], tree[2 * node + 1]);
    }

    void update(int node, int l, int r, int i, int val) {
        if (l == r) {
            tree[node] = val;
            return;
        }
        int mid = (l + r) / 2;
        if (i <= mid)
            update(2 * node, l, mid, i, val);
        else
            update(2 * node + 1, mid + 1, r, i, val);
        tree[node] = op(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l)
            return neutral;
        if (ql <= l && r <= qr)
            return tree[node];
        int mid = (l + r) / 2;
        return op(query(2 * node, l, mid, ql, qr), query(2 * node + 1, mid + 1, r, ql, qr));
    }

    SegTree() {
    }

    SegTree(vector<int> &v) {
        n = v.size();
        tree = vector<int>(4 * n);
        build(v, 1, 0, n - 1);
    }

    void update(int i, int val) { update(1, 0, n - 1, i, val); }

    int query(int l, int r) { // [l, r] inclusive, 0-indexed
        return query(1, 0, n - 1, l, r);
    }
};

SegTree sg;

void inizia(int N, vector<int> A) {
    sg = SegTree(A);
}

void aggiorna(int P, int X) {
    sg.update(P, X);
}

int massimo(int L, int R) {
    return sg.query(L, R);
}

// int main() {
//     int N, Q;
//     cin >> N >> Q;

//     vector<int> A(N);
//     for (int &x : A)
//         cin >> x;

//     inizia(N, A);

//     for (int i = 0; i < Q; i++) {
//         char t;
//         cin >> t;

//         if (t == 'U') {
//             int P, V;
//             cin >> P >> V;
//             aggiorna(P, V);
//         }
//         if (t == 'Q') {
//             int L, R;
//             cin >> L >> R;
//             cout << massimo(L, R) << "\n";
//         }
//     }
// }
