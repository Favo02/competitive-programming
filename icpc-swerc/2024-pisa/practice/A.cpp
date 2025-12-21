#include <bits/stdc++.h>

using namespace std;

int main() {
    int l = 1, r = 1000;
    while (l <= r) {
        cout << (l+r) / 2 << endl;

        string s;
        cin >> s;
        if (s == "found") break;
        if (s == "hollow") l = (l+r)/2 + 1;
        if (s == "solid") r = (l+r)/2 - 1;
    }

}
