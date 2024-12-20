#include<bits/stdc++.h>
using namespace std;
const int INF = 1 << 30;


int row, col;
int sr, sc;
int gr, gc;
vector<string> ch;

void read() {
    string line;
    while (getline(cin, line)) {
        ch.push_back(line);
    }
    row = ch.size();
    col = ch[0].size();
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            if (ch[i][j] == 'S') {
                sr = i;
                sc = j;
                ch[i][j] = '.';
            }
            if (ch[i][j] == 'E') {
                gr = i;
                gc = j;
                ch[i][j] = '.';
            }
        }
    }
}


const int dr[] = {-1, 0, 1, 0};
const int dc[] = {0, 1, 0, -1};

int calcDist() {
    queue<pair<int, int>> Q;
    vector dist(row, vector(col, INF));

    Q.push({sr, sc});
    dist[sr][sc] = 0;

    while (!Q.empty()) {
        auto [r, c] = Q.front();
        Q.pop();

        for (int dir = 0; dir < 4; ++dir) {
            int nr = r + dr[dir];
            int nc = c + dc[dir];
            if (nr < 0 || nr >= row || nc < 0 || nc >= col) {
                continue;
            }
            if (ch[nr][nc] == '#') {
                continue;
            }
            if (dist[nr][nc] != INF) {
                continue;
            }

            dist[nr][nc] = dist[r][c] + 1;
            Q.push({nr, nc});
        }
    }

    return dist[gr][gc];
}


void work() {
    int origDist = calcDist();
    int cnt = 0;

    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            char back = ch[i][j];
            ch[i][j] = '.';

            cnt += origDist - calcDist() >= 100;

            ch[i][j] = back;
        }
    }

    cout << cnt << endl;
}


int main() {
    read();
    work();
    return 0;
}
