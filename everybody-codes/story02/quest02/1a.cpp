#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
    string balloons;
    cin >> balloons;
    int B = balloons.length();

    string bow = "RGB";
    int ai = 0, bi = 0;
    while (bi < B) {
        if (bow[ai % 3] != balloons[bi]) {
            ai++;
        }
        bi++;
    }
    if (bow[ai % 3] == balloons.back())
        ai++;

    cout << ai << endl;
}
