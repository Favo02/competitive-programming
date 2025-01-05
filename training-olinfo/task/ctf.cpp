#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll solve(ll players) {
    if (players == 1) return 0;

    if (players % 2 == 0)
        return (solve(players / 2)*2) % players;
    return (solve(players - 1) + 2) % players;
}

int main() {
    int cases;
    cin >> cases;

    ll pl;
    for (int i = 0; i < cases; i++) {
        cin >> pl;
        cout << solve(pl)+1 << endl;
    }
}
