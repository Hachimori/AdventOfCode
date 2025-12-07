#include<bits/stdc++.h>
using namespace std;


int row;
int col;
vector<string> ch;

void read() {
    string line;
    while (getline(cin, line)) {
        ch.push_back(line);
    }
    row = ch.size();
    col = ch[0].size();
}


long long rec(int r, int c, vector<vector<long long>> &dp) {
    if (!(0 <= r && r < row && 0 <= c && c < col)) {
        return 1;
    }

    if (!(0 <= c && c < col)) {
        return 0;
    }

    long long &ret = dp[r][c];
    if (ret != -1) {
        return ret;
    }

    ret = 0;

    if (ch[r][c] == '^') {
        ret += rec(r, c - 1, dp);
        ret += rec(r, c + 1, dp);
    } else {
        ret += rec(r + 1, c, dp);
    }

    return ret;
}


void work() {
    int initR = 0;
    int initC = ch[0].find('S');

    vector<vector<long long>> dp(row, vector<long long>(col, -1));
    cout << rec(initR, initC, dp) << endl;
}


int main() {
    read();
    work();
    return 0;
}
