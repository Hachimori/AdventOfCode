#include<bits/stdc++.h>
using namespace std;


int row, col;
vector<string> ch;

void read() {
    string s;
    while (cin >> s) {
        ch.push_back(s);
    }
    row = ch.size();
    col = ch[0].size();
}


void work() {
    int sr = 0, sc = 0;
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; ++j) {
            if (ch[i][j] == '^') {
                sr = i;
                sc = j;
            }
        }
    }

    const static int dr[] = {-1, 0, 1, 0};
    const static int dc[] = {0, 1, 0, -1};
    int dir = 0;

    vector visited(row, vector(col, false));
    visited[sr][sc] = true;

    while (1) {
        int nr = sr + dr[dir];
        int nc = sc + dc[dir];
        if (!(0 <= nr && nr < row && 0 <= nc && nc < col)) {
            break;
        }
        if (ch[nr][nc] == '#') {
            dir = (dir + 1) % 4;
            continue;
        }
        visited[nr][nc] = true;
        sr = nr;
        sc = nc;
    }

    int ans = 0;
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; ++j) {
            ans += visited[i][j];
        }
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
