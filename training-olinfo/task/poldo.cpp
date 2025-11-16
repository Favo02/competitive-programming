#include <bits/stdc++.h>

using namespace std;

int lis(vector<int> const &a) {
    int n = a.size();
    const int INF = 1e9;
    vector<int> d(n + 1, -INF);
    d[0] = INF;

    for (int i = 0; i < n; i++) {
        int l = upper_bound(d.begin(), d.end(), a[i], greater<int>()) - d.begin();
        if (d[l - 1] > a[i] && a[i] > d[l])
            d[l] = a[i];
    }

    int ans = 0;
    for (int l = 0; l <= n; l++) {
        if (d[l] > -INF)
            ans = l;
    }
    return ans;
}

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");

    int n;
    in >> n;

    vector<int> panini(n);
    for (int i = 0; i < n; i++) {
        in >> panini[i];
    }

    out << lis(panini) << endl;
}
