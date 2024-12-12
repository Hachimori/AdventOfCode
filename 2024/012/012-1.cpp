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


void rec(int r, int c, vector<vector<bool>> &visited, int &area, int &perimeter) {
    ++area;
    visited[r][c] = true;

    const static int dr[] = {-1, 0, 1, 0};
    const static int dc[] = {0, 1, 0, -1};
    for (int i = 0; i < 4; ++i) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (nr < 0 || nr >= row || nc < 0 || nc >= col) {
            ++perimeter;
        } else if (ch[nr][nc] != ch[r][c]) {
            ++perimeter;
        } else if (!visited[nr][nc]) {
            rec(nr, nc, visited, area, perimeter);
        }
    }
}


void work() {
    vector visited(row, vector(col, false));

    int ans = 0;
    for (int r = 0; r < row; ++r) {
        for (int c = 0; c < col; ++c) {
            if (visited[r][c]) continue;
            int area = 0, perimeter = 0;
            rec(r, c, visited, area, perimeter);
            ans += area * perimeter;
        }
    }

    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
