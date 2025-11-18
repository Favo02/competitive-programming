#include <bits/stdc++.h>
using namespace std;
#define ll long long

struct Dice {
    int id;
    vector<int> faces;
    int seed;
    int cur_face;
    int pulse;
    int rolls;
};

int roll(Dice &d) {
    d.rolls++;
    int spin = d.rolls * d.pulse;
    int res_face = (d.cur_face + spin) % d.faces.size();
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
    int F, x;
    for (int i = 0; i < D; i++) {
        Dice d = {0, vector<int>(), 0, 0, 0, 0};
        cin >> d.id >> F;
        for (int f = 0; f < F; f++) {
            cin >> x;
            d.faces.push_back(x);
        }
        cin >> d.seed;
        d.pulse = d.seed;
        dices.push_back(d);
    }

    int res = 0;
    int rolls = 0;
    while (res < 10000) {
        rolls++;
        for (auto &d : dices) {
            res += roll(d);
        }
    }
    cout << rolls << endl;
}
