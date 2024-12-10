#include<bits/stdc++.h>
using namespace std;


int row, col;
vector<string> ch;

void read() {
    string line;
    while (cin >> line) {
        for (int i = 0; i < line.size(); ++i) {
            line[i] -= '0';
        }
        ch.push_back(line);
    }
    row = ch.size();
    col = ch[0].size();
}


void rec(int r, int c, vector<vector<bool>> &visited, int &ans) {
    if (ch[r][c] == 9) {
        ++ans;
        return;
    }
    static int dr[] = {-1, 0, 1, 0};
    static int dc[] = {0, 1, 0, -1};
    for (int i = 0; i < 4; ++i) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (!(0 <= nr && nr < row && 0 <= nc && nc < col)) {
            continue;
        }
        if (visited[nr][nc]) {
            continue;
        }
        if (ch[nr][nc] != ch[r][c] + 1) {
            continue;
        }
        visited[nr][nc] = true;
        rec(nr, nc, visited, ans);
        visited[nr][nc] = false;
    }
}


void work() {
    vector visited(row, vector(col, false));

    int ans = 0;
    for (int r = 0; r < row; ++r) {
        for (int c = 0; c < col; ++c) {
            if (ch[r][c] != 0) {
                continue;
            }
            visited[r][c] = true;
            rec(r, c, visited, ans);
            visited[r][c] = false;
        }
    }

    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
