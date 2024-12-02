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
    map<int, int> r2cnt;
    for (int r : R) {
        r2cnt[r]++;
    }

    int ans = 0;
    for (int l : L) {
        ans += l * r2cnt[l];
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
