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


void rec(int r, int c, vector<vector<bool>> &visited, bool &isPartNumber) {
    if (!isdigit(ch[r][c])) {
        isPartNumber = true;
        return;
    }
    visited[r][c] = true;
    for (int i = 0; i < 8; ++i) {
        const static int dr[] = {-1, -1, -1, 0, 1, 1, 1, 0};
        const static int dc[] = {-1, 0, 1, 1, 1, 0, -1, -1};
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (0 <= nr && nr < row && 0 <= nc && nc < col && !visited[nr][nc] && ch[nr][nc] != '.') {
            rec(nr, nc, visited, isPartNumber);
        }
    }
}


void work() {
    int ans = 0;
    vector visited(row, vector(col, false));

    for (int r = 0; r < row; ++r) {
        for (int c = 0; c < col; ++c) {
            if (visited[r][c]) continue;
            if (!isdigit(ch[r][c])) continue;

            bool isPartNumber = false;
            rec(r, c, visited, isPartNumber);
            if (isPartNumber) {
                int cc = c;
                int toAdd = 0;
                while (cc < col && isdigit(ch[r][cc])) {
                    toAdd = toAdd * 10 + ch[r][cc] - '0';
                    ++cc;
                }
                ans += toAdd;
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
