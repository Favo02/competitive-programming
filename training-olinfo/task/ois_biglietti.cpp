#include <bits/stdc++.h>
using namespace std;

int compra(int corse, int corse_carnet, int costo_corsa, int costo_carnet) {
    if (corse_carnet * costo_corsa <= costo_carnet)
        return corse * costo_corsa;

    int carnet_acquistati = corse / corse_carnet;
    return min(
        (carnet_acquistati * costo_carnet) + (corse - (carnet_acquistati * corse_carnet)) * costo_corsa,
        (carnet_acquistati+1) * costo_carnet
    );
}


int main() {
    FILE *fr, *fw;
    int N, M, A, B;

    fr = fopen("input.txt", "r");
    fw = fopen("output.txt", "w");

    assert(4 == fscanf(fr, "%d%d%d%d", &N, &M, &A, &B));

    fprintf(fw, "%d\n", compra(N, M, A, B));
    fclose(fr);
    fclose(fw);
    return 0;
}
