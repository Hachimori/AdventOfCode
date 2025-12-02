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
        if (ch == 'L') {
            cur = (100 + cur - cnt) % 100;
        } else if (ch == 'R') {
            cur = (cur + cnt) % 100;
        }
        ans += cur == 0;
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
