#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    int sum = 0;

    cin >> n;
    sum += n;

    cin >> n;
    sum += n;

    cin >> n;
    sum += n;

    cout << ceil(sum / 20.0) << endl;
}
