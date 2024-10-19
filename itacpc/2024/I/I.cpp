#include <bits/stdc++.h>

using namespace std;

#pragma GCC optimize("Ofast,unroll-loops")
#pragma GCC target("avx,avx2,fma")

template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)

#define ar array
#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

#define PI 3.1415926535897932384626433832795l
const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

pair<int, int> bfs_start(vector<string> grid, int sr, int sc, int ROWS, int COLS) {
    queue<tuple<int, int, int>> q;
    q.push({sr, sc, 0});

    vector<pair<int, int>> DIR = {{0,1}, {0,-1}, {1,0}, {-1,0}};

    int to_s = -1;

    while (q.size() > 0) {
        auto [r, c, dist] = q.front();
        q.pop();

        for (auto dir : DIR) {
            int nr = r + dir.first;
            int nc = c + dir.second;

            if (nr < 0 || nr >= ROWS || nc < 0 || nc >= COLS || grid[nr][nc] == '#' || grid[nr][nc] == 'U') {
                continue;
            }

            if (grid[nr][nc] == 'S' && to_s == -1) {
                to_s = dist + 1;
            }
            if (grid[nr][nc] == 'B') {
                return {dist+1, to_s};
            }

            q.push({nr, nc, dist + 1});
            grid[nr][nc] = 'U';
        }
    }
    return {-1, to_s};
}

int bfs_end(vector<string> grid, int sr, int sc, int ROWS, int COLS) {
    queue<tuple<int, int, int>> q;
    q.push({sr, sc, 0});

    vector<pair<int, int>> DIR = {{0,1}, {0,-1}, {1,0}, {-1,0}};

    while (q.size() > 0) {
        auto [r, c, dist] = q.front();
        q.pop();

        for (auto dir : DIR) {
            int nr = r + dir.first;
            int nc = c + dir.second;

            if (nr < 0 || nr >= ROWS || nc < 0 || nc >= COLS || grid[nr][nc] == '#' || grid[nr][nc] == 'U') {
                continue;
            }

            if (grid[nr][nc] == 'S') {
                return dist + 1;
            }

            q.push({nr, nc, dist + 1});
            grid[nr][nc] = 'U';
        }
    }
    return -1;
}


void solve() {

    int r, c;
    cin >> r >> c;

    vector<string> matrix(r);

    pair<int, int> start;
    pair<int, int> end;

    for (int i = 0; i < r; i++) {
        cin >> matrix[i];
        for (int j = 0; j < c; j++) {
            if (matrix[i][j] == 'P') {
                start = {i, j};
            }
            if (matrix[i][j] == 'B') {
                end = {i, j};
            }
        }
    }

    auto [path, start_to_s] = bfs_start(matrix, start.first, start.second, r, c);
    if (start_to_s == -1) {
        cout << path << endl;
        return;
    }

    auto end_to_s = bfs_end(matrix, end.first, end.second, r, c);

    auto using_s = -1;
    if (end_to_s != -1 && start_to_s != -1) {
        using_s = end_to_s + start_to_s + 1;
    }

    if (path == -1 && using_s == -1) {
        cout << -1 << endl;
    } else if (path == -1) {
        cout << using_s << endl;
    } else if (using_s == -1) {
        cout << path << endl;
    } else {
        cout << min(path, using_s) << endl;
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    // cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}
