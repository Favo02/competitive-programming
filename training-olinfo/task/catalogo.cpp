#include <bits/stdc++.h>
using namespace std;

unordered_map<long long, int> freqs;

void aggiungi(long long int id) {
    freqs[id]++;
}

void togli(long long int id) {
    freqs[id]--;
}

int conta(long long int id) {
    return freqs[id];
}
