#include<bits/stdc++.h>
using namespace std;


vector<pair<long long, long long>> range;

void read() {
    long long bgn, end;
    char ch;
    while (cin >> bgn >> ch >> end) {
        range.push_back({bgn, end});
        if (!(cin >> ch)) break;
    }
}


bool isRep(long long v) {
    for (long long p = 10; p <= v; p *= 10) {
        long long mod = v % p;
        if (mod < p / 10) continue;
        if (v % p == v / p) {
            return true;
        }
    }
    return false;
}


void work() {
    long long ans = 0;
    for (auto [bgn, end] : range) {
        for (long long cur = bgn; cur <= end; ++cur) {
            if (isRep(cur)) {
                ans += cur;
            }
        }
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
