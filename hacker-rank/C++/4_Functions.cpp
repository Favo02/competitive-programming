#include <bits/stdc++.h>
using namespace std;

int max_of_four(int a, int b, int c, int d) {
    return max(max(max(a,b),c),d);
}

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    cout << max_of_four(a,b,c,d) << "\n";
}
