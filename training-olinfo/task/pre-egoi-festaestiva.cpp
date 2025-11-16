#include <bits/stdc++.h>

using namespace std;

int organizza(int N, int X, int Y, vector<int> A, vector<int> B) {
    vector<pair<int, int>> events;

    for (int i = 0; i < N; i++) {
        if (A[i] > X) {
            events.push_back({X, +1});
            events.push_back({A[i], -1});
        }
        if (B[i] < Y) {
            events.push_back({B[i] + 1, +1});
            events.push_back({Y + 1, -1});
        }
    }

    sort(events.begin(), events.end());

    int res = 0;
    int open = 0;
    for (int i = 0; i < events.size(); i++) {
        open += events[i].second;
        res = max(res, open);
    }

    return res;
}

int main() {
    cout << organizza(3, 2, 10, vector<int>{0, 5, 3}, vector<int>{8, 9, 4}) << endl;
    cout << organizza(6, 2, 8, vector<int>{0, 6, 0, 6, 0, 9}, vector<int>{10, 10, 3, 9, 5, 10}) << endl;
}
