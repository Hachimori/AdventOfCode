#include<bits/stdc++.h>
using namespace std;


int row, col;
vector<string> ch;

void read() {
    string line;
    while (cin >> line) {
        ch.push_back(line);
    }
    row = ch.size();
    col = ch[0].size();
}


void rec(int r, int c, vector<vector<bool>> &visited, int &area, int &side) {
    ++area;
    visited[r][c] = true;

    const static int dr[] = {-1, 0, 1, 0};
    const static int dc[] = {0, 1, 0, -1};
    for (int i = 0; i < 4; ++i) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        if ((nr < 0 || nr >= row || nc < 0 || nc >= col) || ch[nr][nc] != ch[r][c]) {
            int nrr1 = r + dr[(i + 1) % 4];
            int ncc1 = c + dc[(i + 1) % 4];
            int nrr2 = nrr1 + dr[i];
            int ncc2 = ncc1 + dc[i];
            if (0 <= nrr1 && nrr1 < row && 0 <= ncc1 && ncc1 < col && ch[r][c] == ch[nrr1][ncc1] &&
                (!(0 <= nrr2 && nrr2 < row && 0 <= ncc2 && ncc2 < col) || ch[r][c] != ch[nrr2][ncc2])) {
                continue;
            }
            ++side;
        } else if (!visited[nr][nc]) {
            rec(nr, nc, visited, area, side);
        }
    }
}


void work() {
    vector visited(row, vector(col, false));

    int ans = 0;
    for (int r = 0; r < row; ++r) {
        for (int c = 0; c < col; ++c) {
            if (visited[r][c]) continue;
            int area = 0, side = 0;
            rec(r, c, visited, area, side);
            ans += area * side;
        }
    }

    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
