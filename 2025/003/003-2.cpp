#include<bits/stdc++.h>
using namespace std;
const long long INF = 1LL << 50;


vector<string> str;

void read() {
    string s;
    while (cin >> s) {
        str.push_back(s);
    }
}


long long rec(int nAdded, int idx, string &s, vector<vector<long long>> &dp) {
    if (nAdded == 12) {
        return 0;
    }

    if (idx == s.size()) {
        return -INF;
    }

    long long &ret = dp[nAdded][idx];
    if (ret != -1) return ret;

    ret = 0;

    // add
    ret = max(ret, (s[idx] - '0') + 10 * rec(nAdded + 1, idx + 1, s, dp));

    // not add
    ret = max(ret, rec(nAdded, idx + 1, s, dp));

    return ret;
}


void work() {
    long long sum = 0;
    for (string s : str) {
        reverse(s.begin(), s.end());
        vector dp(13, vector(s.size(), -1LL));
        sum += rec(0, 0, s, dp);
    }
    cout << sum << endl;
}


int main() {
    read();
    work();
    return 0;
}
