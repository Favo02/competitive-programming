#include <bits/stdc++.h>
using namespace std;

int solve(){
    int N;
    cin >> N;

    vector<int> nums(N);
    for (int &x: nums) {
        cin >> x;
    }

    int res = nums[0];
    for (auto n : nums) {
        res = lcm(res, n);
    }
    return res;
}

int main(){
    int T;
    cin >> T;
    for (int i = 0; i < T; i++){
        cout << "Case #" << i+1 << ": " << solve() << endl;
    }
    return 0;
}
