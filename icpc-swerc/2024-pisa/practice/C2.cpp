#include <bits/stdc++.h>

using namespace std;

vector<int> weights;
vector<double> probs;
int n;

vector<vector<double>> mem;

double solve(int peso, int index) {
    if (peso <= 0) return 1.0;
    if (index == n) return 0.0;

    if (mem[peso][index] != -1) {
        return mem[peso][index];
    }

    double yes = probs[index] * solve(peso - weights[index], index+1);
    double no = (1-probs[index]) * solve(peso, index+1);

    mem[peso][index] = yes + no;
    return yes + no;
}

int main() {
    cin >> n;

    weights = vector<int>(n);
    int summ = 0;
    for (int i = 0; i < n; i++) {
        cin >> weights[i];
        summ += weights[i];
    }

    probs = vector<double>(n);
    for (int i = 0; i < n; i++) {
        cin >> probs[i];
    }

    mem = vector<vector<double>>(100001, vector<double>(1001, -1));

    cout << solve(ceil(summ / 2.0), 0) << endl;
}
