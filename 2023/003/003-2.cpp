#include<bits/stdc++.h>
using namespace std;


int row, col;
vector<string> ch;

void read() {
    ch.clear();
    string s;
    while (cin >> s) {
        ch.emplace_back(s);
    }
    row = ch.size();
    col = ch[0].size();
}


void rec(int r, int c, vector<vector<bool>> &visited, vector<vector<int>> &mul2id, int &mulId) {
    if (!isdigit(ch[r][c])) {
        if (ch[r][c] == '*') {
            mulId = mul2id[r][c];
        }
        return;
    }

    visited[r][c] = true;
    for (int i = 0; i < 8; ++i) {
        const static int dr[] = {-1, -1, -1, 0, 1, 1, 1, 0};
        const static int dc[] = {-1, 0, 1, 1, 1, 0, -1, -1};
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (0 <= nr && nr < row && 0 <= nc && nc < col && !visited[nr][nc] && ch[nr][nc] != '.') {
            rec(nr, nc, visited, mul2id, mulId);
        }
    }
}


void work() {
    int nId = 0;
    vector mul2id(row, vector(col, -1));
    vector visited(row, vector(col, false));

    for (int r = 0; r < row; ++r) {
        for (int c = 0; c < col; ++c) {
            if (ch[r][c] == '*') {
                mul2id[r][c] = nId++;
            }
        }
    }

    vector mulId2vList(nId, vector<int>());
    for (int r = 0; r < row; ++r) {
        for (int c = 0; c < col; ++c) {
            if (visited[r][c]) continue;
            if (!isdigit(ch[r][c])) continue;

            int mulId = -1;
            rec(r, c, visited, mul2id, mulId);
            if (mulId >= 0) {
                int cc = c;
                int toAdd = 0;
                while (cc < col && isdigit(ch[r][cc])) {
                    toAdd = toAdd * 10 + ch[r][cc] - '0';
                    ++cc;
                }
                mulId2vList[mulId].emplace_back(toAdd);
            }
        }
    }

    int ans = 0;
    for (int i = 0; i < nId; ++i) {
        if (mulId2vList[i].size() == 2) {
            ans += mulId2vList[i].front() * mulId2vList[i].back();
        }
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
