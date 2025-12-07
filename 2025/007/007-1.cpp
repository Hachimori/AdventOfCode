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


void rec(int r, int c, vector<vector<bool>> &visited, int &ans) {
    if (!(0 <= r && r < row && 0 <= c && c < col)) {
        return;
    }

    if (visited[r][c]) {
        return;
    }
    visited[r][c] = true;

    if (ch[r][c] == '^') {
        ++ans;
        rec(r, c - 1, visited, ans);
        rec(r, c + 1, visited, ans);
    } else {
        rec(r + 1, c, visited, ans);
    }
}


void work() {
    int initR = 0;
    int initC = ch[0].find('S');

    int ans = 0;
    vector<vector<bool>> visited(row, vector<bool>(col, false));
    rec(initR, initC, visited, ans);
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
