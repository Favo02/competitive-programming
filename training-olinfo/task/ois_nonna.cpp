#include <bits/stdc++.h>
using namespace std;

#define MAXN 5000
#define MAXK 5000
#define MAXP 1000000

int mangia(int N, int K, int P[]) {

    vector<int> used(K + 1, 1e9);
    used[0] = -1;

    int res = 1e9;

    for (int i = 0; i < N; i++) {
        for (int ii = 0; ii < K + 1; ii++) {
            if (used[ii] < i) {
                if (ii + P[i] >= K) {
                    res = min(res, ii + P[i]);
                    continue;
                }
                if (used[ii + P[i]] > i) {
                    used[ii + P[i]] = i;
                }
            }
        }
    }

    return res;
}

int P[MAXN];

int main() {
    FILE *fr, *fw;
    int N, K, i;

    fr = fopen("input.txt", "r");
    fw = fopen("output.txt", "w");
    assert(2 == fscanf(fr, "%d %d", &N, &K));
    for (i = 0; i < N; i++)
        assert(1 == fscanf(fr, "%d", &P[i]));

    fprintf(fw, "%d\n", mangia(N, K, P));
    fclose(fr);
    fclose(fw);
    return 0;
}
