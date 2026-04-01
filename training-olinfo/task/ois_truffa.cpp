#include <bits/stdc++.h>
using namespace std;

#define MAXN 100000

int sfangate(int N, int V[]) {
    sort(V, V + N);
    long long sum = 0;
    for (int i = 0; i < N; i++)
        sum += V[i];

    int i;
    for (i = 0; i < N && sum <= 0; i++)
        sum -= V[i] * 2;
    return i;
}

int V[MAXN];

int main() {
    FILE *fr, *fw;
    int N, i;

    fr = fopen("input.txt", "r");
    fw = fopen("output.txt", "w");
    assert(1 == fscanf(fr, "%d", &N));
    for (i = 0; i < N; i++)
        assert(1 == fscanf(fr, "%d", &V[i]));

    fprintf(fw, "%d\n", sfangate(N, V));
    fclose(fr);
    fclose(fw);
    return 0;
}
