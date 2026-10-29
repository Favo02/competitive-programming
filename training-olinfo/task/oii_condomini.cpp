#include <bits/stdc++.h>
using namespace std;

int sbugiarda(int N, vector<int> H) {
    if (N <= 2)
        return N;

    vector<int> left;
    int best = 0;
    vector<pair<int, int>> monstack;
    for (int i = 0; i < N; i++) {
        int bestvista = 0;
        while (!monstack.empty() && monstack.back().first < H[i]) {
            bestvista = max(bestvista, monstack.back().second);
            monstack.pop_back();
        }
        monstack.push_back({H[i], bestvista + 1});
        best = max(best, bestvista + 1);
        left.push_back(best);
    }

    reverse(H.begin(), H.end());

    vector<int> right;
    best = 0;
    monstack.clear();
    for (int i = 0; i < N; i++) {
        int bestvista = 0;
        while (!monstack.empty() && monstack.back().first < H[i]) {
            bestvista = max(bestvista, monstack.back().second);
            monstack.pop_back();
        }
        monstack.push_back({H[i], bestvista + 1});
        best = max(best, bestvista + 1);
        right.push_back(best);
    }

    reverse(right.begin(), right.end());

    // pprint(left);
    // pprint(right);

    int res = 2;
    for (int i = 0; i < N; i++) {
        res = max(res, left[i] + right[i] - 1);
        if (i != N - 1)
            res = max(res, left[i] + right[i + 1]);
        if (i != 0)
            res = max(res, left[i - 1] + right[i]);
    }
    return res;
}

int main() {
    cout << sbugiarda(3, {1, 4, 3}) << endl;
    cout << sbugiarda(5, {4, 1, 2, 5, 3}) << endl;
    cout << sbugiarda(2, {1, 1}) << endl;
    cout << sbugiarda(3, {1, 1, 1}) << endl;
    cout << sbugiarda(4, {10, 2, 5, 8}) << endl;
    cout << sbugiarda(5, {10, 2, 4, 3, 5}) << endl;
    cout << sbugiarda(8, {3, 4, 5, 1, 2, 7, 8, 9}) << endl;
    cout << sbugiarda(8, {3, 4, 5, 1, 1, 5, 4, 3}) << endl;
}
