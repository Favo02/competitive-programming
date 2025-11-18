#include <bits/stdc++.h>
using namespace std;
#define ll long long

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

    string sequence;
    cin >> sequence;

    vector<int> pos(D, 0);
    vector<int> res;

    while (res.size() < D) {
        for (int i = 0; i < D; i++) {

            if (pos[i] >= sequence.length())
                continue;

            if (roll(dices[i]) == sequence[pos[i]] - '0') {
                pos[i]++;
            }

            if (pos[i] == sequence.length()) {
                res.push_back(i + 1);
            }
        }
    }

    for (auto p : res)
        cout << p << ",";
    cout << endl;
}
