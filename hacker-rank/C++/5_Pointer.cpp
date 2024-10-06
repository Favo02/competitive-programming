#include <bits/stdc++.h>
using namespace std;

void update(int *a,int *b) {
    int oldA = *a;
    *a = *a + *b;
    *b = abs(oldA - *b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    cin >> a >> b;

    update(pa, pb);

    cout << a << "\n" << b;
}
