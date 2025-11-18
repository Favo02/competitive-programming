#include <bits/stdc++.h>
using namespace std;
#define ll long long

struct RobustHash {
    template <typename T>
    inline size_t hash_combine(size_t seed, const T &v) const {
        hash<T> hasher;
        return seed ^ (hasher(v) + 0x9e3779b9 + (seed << 6) + (seed >> 2));
    }

    template <typename T1, typename T2, typename T3>
    size_t operator()(const tuple<T1, T2, T3> &t) const {
        size_t seed = 0;
        seed = hash_combine(seed, get<0>(t));
        seed = hash_combine(seed, get<1>(t));
        seed = hash_combine(seed, get<2>(t));
        return seed;
    }
};

struct Dice {
    ll id;
    vector<ll> faces;
    ll seed;
    ll cur_face;
    ll pulse;
    ll rolls;
};

int roll(Dice &d) {
    d.rolls++;
    ll spin = d.rolls * d.pulse;
    ll res_face = (d.cur_face + spin) % d.faces.size();
    d.cur_face = res_face;
    d.pulse = (d.pulse + spin) % d.seed;
    d.pulse = d.pulse + 1 + d.rolls + d.seed;
    return d.faces[res_face];
}

vector<vector<bool>> taken;
vector<string> grid;
int ROWS, COLS;

void sim_dice(Dice d, int sx, int sy, int seqstart) {
    vector<int> seq;
    seq.push_back(seqstart);
    queue<tuple<int, int, int>> q; // x, y, seqi
    q.push({sx, sy, 0});

    unordered_set<tuple<int, int, int>, RobustHash> seen;

    while (!q.empty()) {
        auto [x, y, i] = q.front();
        taken[y][x] = 1;
        q.pop();

        int next;
        if (i + 1 < seq.size()) {
            next = seq[i + 1];
        } else {
            next = roll(d);
            seq.push_back(next);
        }

        for (auto [dx, dy] : vector<pair<int, int>>{{0, 0}, {1, 0}, {0, 1}, {-1, 0}, {0, -1}}) {
            int nx = x + dx, ny = y + dy;
            if (!(nx >= 0 && nx < COLS))
                continue;
            if (!(ny >= 0 && ny < ROWS))
                continue;
            if (next != grid[ny][nx] - '0')
                continue;
            if (seen.count({nx, ny, i + 1}) != 0)
                continue;
            q.push({nx, ny, i + 1});
            seen.insert({nx, ny, i + 1});
        }
    }
}

// NOTE: the input is manually simplified:
// add number of dices at start
// each dice is in this format:
// id numberoffaces face1 face2 ... facen seed
int main() {
    int D;
    cin >> D;

    vector<Dice> dices;
    ll F, x;
    for (int i = 0; i < D; i++) {
        Dice d = {0, vector<ll>(), 0, 0, 0, 0};
        cin >> d.id >> F;
        for (int f = 0; f < F; f++) {
            cin >> x;
            d.faces.push_back(x);
        }
        cin >> d.seed;
        d.pulse = d.seed;
        dices.push_back(d);
    }

    ROWS;
    cin >> ROWS;
    grid = vector<string>(ROWS);
    for (int i = 0; i < ROWS; i++)
        cin >> grid[i];
    COLS = grid[0].length();

    taken = vector<vector<bool>>(ROWS, vector<bool>(COLS));

    for (auto &d : dices) {
        int r = roll(d);
        for (int sy = 0; sy < ROWS; sy++) {
            for (int sx = 0; sx < COLS; sx++) {
                if (r == grid[sy][sx] - '0') {
                    sim_dice(d, sx, sy, r);
                }
            }
        }
    }

    ll res = 0;
    for (int y = 0; y < ROWS; y++) {
        for (int x = 0; x < COLS; x++) {
            res += taken[y][x];
        }
    }
    cout << res << endl;
}
