#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, rip, len;
    cin >> n >> rip >> len;

    unordered_map<string, int> count;
    string s;
    for (int i = 0; i < n; i++) {
        cin >> s;
        if (s.length() < len) continue;
        count[s.substr(0, len)]++;
    }

    string ris = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz";
    for (auto c : count) {
        if (c.second > rip) {
            ris = min(ris, c.first);
        }
    }

    if (ris == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") cout << 0 << endl;
    else cout << ris << endl;
}
