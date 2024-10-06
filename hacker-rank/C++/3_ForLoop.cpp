#include <bits/stdc++.h>
using namespace std;

int main() {
    int s, e;
    cin >> s >> e;
    for (int i = s; i <= e; i++) {
        switch (i) {
            case 1: cout << "one\n"; break;
            case 2: cout << "two\n"; break;
            case 3: cout << "three\n"; break;
            case 4: cout << "four\n"; break;
            case 5: cout << "five\n"; break;
            case 6: cout << "six\n"; break;
            case 7: cout << "seven\n"; break;
            case 8: cout << "eight\n"; break;
            case 9: cout << "nine\n"; break;
            default: cout << (i%2==0 ? "even\n" : "odd\n");
        }
    }
}
