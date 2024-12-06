/**
 * Environment:
 *   MacBook Pro
 *   Apple M3 Max
 *   64 GB RAM
 *
 * $ time ./a.out < input.txt
 * 1711
 * ./a.out < input.txt  5.24s user 0.03s system 99% cpu 5.294 total
 */

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


bool canStuck() {
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

    vector visited(4, vector(row, vector(col, false)));
    visited[dir][sr][sc] = true;

    while (1) {
        int nr = sr + dr[dir];
        int nc = sc + dc[dir];
        if (!(0 <= nr && nr < row && 0 <= nc && nc < col)) {
            return false;
        }
        if (visited[dir][nr][nc]) {
            return true;
        }
        if (ch[nr][nc] == '#') {
            dir = (dir + 1) % 4;
            continue;
        }
        visited[dir][nr][nc] = true;
        sr = nr;
        sc = nc;
    }
}


void work() {
    int ans = 0;
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            if (ch[i][j] != '.') {
                continue;
            }
            ch[i][j] = '#';
            ans += canStuck();
            ch[i][j] = '.';
        }
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
