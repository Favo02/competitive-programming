#include <bits/stdc++.h>
using namespace std;
#define ll long long

// NOTE: the input is manually simplified:
// add number of lines of grid
// add number of lines of tokens
int main() {
    int G;
    cin >> G;
    vector<string> grid(G);
    for (int i = 0; i < G; i++) {
        cin >> grid[i];
    }

    int T;
    cin >> T;
    vector<string> tokens(T);
    for (int i = 0; i < T; i++) {
        cin >> tokens[i];
    }

    int SLOTS = grid[0].size() / 2;

    int res = 0;
    for (int i = 0; i < T; i++) {
        int best = 0;
        for (int start = 0; start <= SLOTS; start++) {
            int dir = 0;
            int y = 0, x = start * 2;
            for (; y < G; y++) {
                if (grid[y][x] == '*') {
                    x += tokens[i][dir] == 'R' ? 1 : -1;
                    if (x < 0)
                        x += 2;
                    if (x >= grid[0].size())
                        x -= 2;
                    dir++;
                }
            }
            best = max(best, (x / 2 + 1) * 2 - (start + 1));
        }
        res += best;
    }
    cout << res << endl;
}
