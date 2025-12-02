#include<bits/stdc++.h>
using namespace std;


vector<pair<char, int>> ops;

void read() {
    char ch;
    int cnt;
    while (cin >> ch >> cnt) {
        ops.push_back({ch, cnt});
    }
}


void work() {
    int ans = 0;
    int cur = 50;
    for (auto [ch, cnt] : ops) {
        ans += cnt / 100;
        cnt %= 100;

        if (cnt == 0) continue;

        if (ch == 'L') {
            ans += cur != 0 && cur - cnt <= 0;
            cur = (100 + cur - cnt) % 100;
        } else if (ch == 'R') {
            ans += cur != 0 && cur + cnt >= 100;
            cur = (cur + cnt) % 100;
        }
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
