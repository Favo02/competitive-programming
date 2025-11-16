#include <bits/stdc++.h>
using namespace std;

int main() {
    int cases;
    cin >> cases;

    int N, K;
    int b;
    vector<int> br;
    for (int i = 0; i < cases; i++) {
        br.clear();
        cin >> N >> K;

        for (int ii = 0; ii < N; ii++) {
            cin >> b;
            br.push_back(b);

            while (br.size() >= 2 && br[br.size() - 1] == br[br.size() - 2]) {
                br.pop_back();
                br.pop_back();
            }
        }

        if (br.empty())
            cout << 1 << "\n";
        else
            cout << 0 << "\n";
    }
}
