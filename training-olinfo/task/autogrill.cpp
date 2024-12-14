#include <bits/stdc++.h>
using namespace std;

set<long long> autogrills;

void inizia() {
    autogrills.clear();
}

void apri(long long p) {
    autogrills.insert(p);
}

void chiudi(long long p) {
    autogrills.erase(p);
}

long long chiedi(long long p) {
    if (autogrills.size() == 0) return -1;
    if (autogrills.size() == 1) return *autogrills.begin();

    auto lb = autogrills.lower_bound(p);

    if (lb == autogrills.end()) return *autogrills.rbegin();
    if (lb == autogrills.begin()) return *autogrills.begin();

    auto after = *lb;
    auto before = *succ(lb);

    if (abs(before-p) < abs(after-p)) return before;
    return after;
}
