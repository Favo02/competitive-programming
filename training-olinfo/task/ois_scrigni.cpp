#include <stdio.h>
#include <assert.h>

double scosse(int N) {
    long long sum = N * (N+1ll) / 2;
    return (sum - N) / 2.0;
}


int main() {
    FILE *fr, *fw;
    int N;

    fr = fopen("input.txt", "r");
    fw = fopen("output.txt", "w");
    assert(1 == fscanf(fr, "%d", &N));
    fprintf(fw, "%.6f\n", scosse(N));
    fclose(fr);
    fclose(fw);
    return 0;
}
