#include <bits/stdc++.h>
using namespace std;

int quadri(int N, long long M, int V[]) {
    long long cur = 0;
    int start = 0;
    int end = 0;

    while (end < N && cur + V[end] <= M) {
        cur += V[end];
        end++;
    }

    int res = end - start;
    // cout << start << "-" << end << endl;

    while (start < N && end < N) {
        cur -= V[start];
        start++;
        while (end < N && cur + V[end] <= M) {
            cur += V[end];
            end++;
        }
        // cout << start << "-" << end << endl;

        res = min(res, end - start);
    }

    return res;
}

// int main() {
//     int N, M;
//     cin >> N >> M;

//     int *V = new int[N];
//     for (int i = 0; i < N; ++i) {
//         cin >> V[i];
//     }

//     cout << quadri(N, M, V) << '\n';
// }
