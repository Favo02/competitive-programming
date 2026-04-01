#include <bits/stdc++.h>
using namespace std;

int tempo_massimo(int N, int a[], int b[]) {

    vector<vector<int>> mem(N + 1, vector<int>(2, -1));

    function<int(int, bool)> rec = [&](int day, bool skip) {
        if (day >= N)
            return 0;

        if (mem[day][skip] != -1)
            return mem[day][skip];

        int res = rec(day + 1, false);
        res = max(res, a[day] + rec(day + 1, true));
        if (!skip)
            res = max(res, b[day] + rec(day + 1, true));
        return mem[day][skip] = res;
    };

    return rec(0, false);
}

// int main() {
//     int N;
//     cin >> N;

//     int *A = new int[N];
//     int *B = new int[N];

//     for (int i = 0; i < N; ++i) {
//         cin >> A[i] >> B[i];
//     }

//     cout << tempo_massimo(N, A, B) << '\n';
// }
