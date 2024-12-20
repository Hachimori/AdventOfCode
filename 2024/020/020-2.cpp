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

vector<vector<int>> calcDist(int initR, int initC) {
    queue<pair<int, int>> Q;
    vector dist(row, vector(col, INF));

    Q.push({initR, initC});
    dist[initR][initC] = 0;

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

    return dist;
}


void work() {
    vector distFromS = calcDist(sr, sc);
    vector distFromE = calcDist(gr, gc);
    int cnt = 0;

    int origDist = distFromS[gr][gc];

    for (int rr1 = 0; rr1 < row; ++rr1) {
        for (int cc1 = 0; cc1 < col; ++cc1) {
            if (distFromS[rr1][cc1] == INF) {
                continue;
            }

            for (int rr2 = 0; rr2 < row; ++rr2) {
                for (int cc2 = 0; cc2 < col; ++cc2) {
                    if (abs(rr1 - rr2) + abs(cc1 - cc2) > 20) {
                        continue;
                    }

                    if (ch[rr2][cc2] == '#') {
                        continue;
                    }

                    int cheatDist = abs(rr1 - rr2) + abs(cc1 - cc2);
                    if (origDist - (distFromS[rr1][cc1] + cheatDist + distFromE[rr2][cc2]) >= 100) {
                        cnt++;
                    }
                }
            }
        }
    }

    cout << cnt << endl;
}


int main() {
    read();
    work();
    return 0;
}
