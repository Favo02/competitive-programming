#include <bits/stdc++.h>
using namespace std;
#define ll long long

vector<string> grid;
vector<string> tokens;
vector<vector<pair<int, int>>> mem;
int SLOTS;

pair<int, int> solve(int tokeni, int slots_taken) {
    if (tokeni == tokens.size())
        return {0, 0};

    if (mem[tokeni][slots_taken] != make_pair(-1, -1))
        return mem[tokeni][slots_taken];

    int best = 0;
    int worse = 1e9;

    for (int start = 0; start <= SLOTS; start++) {
        if ((slots_taken >> start) & 1)
            continue;

        int dir = 0;
        int y = 0, x = start * 2;
        for (; y < grid.size(); y++) {
            if (grid[y][x] == '*') {
                x += tokens[tokeni][dir] == 'R' ? 1 : -1;
                if (x < 0)
                    x += 2;
                if (x >= grid[0].size())
                    x -= 2;
                dir++;
            }
        }

        int coins = max(0, (x / 2 + 1) * 2 - (start + 1));
        auto [w, b] = solve(tokeni + 1, slots_taken | (1 << start));
        worse = min(worse, w + coins);
        best = max(best, b + coins);
    }

    mem[tokeni][slots_taken] = {worse, best};
    return {worse, best};
}

// NOTE: the input is manually simplified:
// add number of lines of grid
// add number of lines of tokens
int main() {
    int G;
    cin >> G;
    grid = vector<string>(G);
    for (int i = 0; i < G; i++) {
        cin >> grid[i];
    }
    int T;
    cin >> T;
    tokens = vector<string>(T);
    for (int i = 0; i < T; i++) {
        cin >> tokens[i];
    }

    SLOTS = grid[0].size() / 2;

    mem = vector<vector<pair<int, int>>>(T + 1, vector<pair<int, int>>(1 << (SLOTS + 1), {-1, -1}));
    auto [worse, best] = solve(0, 0);
    cout << worse << " " << best << endl;
}
