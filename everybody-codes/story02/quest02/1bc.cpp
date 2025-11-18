#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
    string bal;
    cin >> bal;
    string bow = "RGB";

    string balloons;

    // part2:
    // for (int i = 0; i < 100; i++) {
    // part 3:
    for (int i = 0; i < 100000; i++) {
        balloons += bal;
    }

    int B = balloons.length();
    int arrow = 0, front = 0, back = B / 2;

    while (B) {
        if (balloons[front] == '-') {
            front++;
            continue;
        }

        if (bow[arrow % 3] == balloons[front] && B % 2 == 0) {
            balloons[back] = '-';
            back++;
            B--;
        } else if (bow[arrow % 3] != balloons[front] && B % 2 == 0) {
            back++;
        }

        arrow++;
        balloons[front] = '-';
        front++;
        B--;
    }

    cout << arrow << endl;
}
