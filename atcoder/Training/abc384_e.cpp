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

void solve() {
    int H, W, sx, sy;
    ll X;
    cin >> H >> W >> X >> sy >> sx;

    sx--;
    sy--;

    vector<vector<ll>> field(H, vector<ll>(W));
    for (int r = 0; r < H; r++) {
        for (int c = 0; c < W; c++) {
            cin >> field[r][c];
        }
    }

    deque<pair<int, int>> queue;
    queue.push_back({sx, sy});
    vector<tuple<ll, int, int>> waiting;

    vector<pair<int, int>> DIRS = {{0,1}, {0,-1}, {1,0}, {-1,0}};

    ll strength = field[sy][sx];
    field[sy][sx] = -1;

    while (!queue.empty()) {
        auto [x, y] = queue.front();
        queue.pop_front();

        for (auto [dx, dy] : DIRS) {
            int nx = x+dx;
            int ny = y+dy;
            if (!(0 <= nx && nx < W)) continue;
            if (!(0 <= ny && ny < H)) continue;
            if (field[ny][nx] == -1) continue;

            waiting.push_back({-field[ny][nx], nx, ny});
            push_heap(all(waiting));

            field[ny][nx] = -1;
        }

        ll newstrength = strength;
        while (!waiting.empty()) {
            pop_heap(all(waiting));
            tuple<ll, int, int> cand = waiting.back();

            ll candidate = -1ll * get<0>(cand);
            int x = get<1>(cand);
            int y = get<2>(cand);

            // cout << candidate << " < " << ceil((double)strength / X) << endl;
            ll reqstrenght = 0ll;
            if (strength % X == 0) reqstrenght = strength / X;
            else reqstrenght = (strength / X) + 1ll;

            if (candidate < reqstrenght) {
                // cout << "valid" << endl;
                newstrength += candidate;
                waiting.pop_back();
                queue.push_back({x, y});
            } else {
                // cout << "invalid" << endl;
                push_heap(all(waiting));
                break;
            }
        }
        strength = newstrength;
    }

    cout << strength << endl;
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
