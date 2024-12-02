#include<bits/stdc++.h>
using namespace std;

vector<int> L, R;

void read() {
    int x, y;
    while (cin >> x >> y) {
        L.push_back(x);
        R.push_back(y);
    }
}


void work() {
    sort(L.begin(), L.end());
    sort(R.begin(), R.end());

    int ans = 0;
    for (int i = 0; i < L.size(); i++) {
        ans += abs(L[i] - R[i]);
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
