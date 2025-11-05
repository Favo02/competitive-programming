#include <bits/stdc++.h>

using namespace std;

#define ll long long

bool check(ll x, ll y) {
    ll rx = 0;
    ll ry = 0;

    for (int i = 0; i < 100; i++) {
        ll nrx = (rx * rx - ry * ry) / 100000 + x;
        ll nry = (rx * ry + ry * rx) / 100000 + y;

        rx = nrx;
        ry = nry;

        if (rx < -1000000 || rx > 1000000)
            return false;
        if (ry < -1000000 || ry > 1000000)
            return false;
    }

    return true;
}

int main() {

    string s;
    cin >> s;

    int comma = s.find(',');
    ll x = stoll(s.substr(3, comma - 3));
    ll y = stoll(s.substr(comma + 1, s.length() - 2 - comma));

    int res = 0;

    for (ll yy = y; yy <= y + 1000; yy += 10) {
        for (ll xx = x; xx <= x + 1000; xx += 10) {
            if (check(xx, yy))
                res++;
        }
    }

    cout << res << endl;
}
