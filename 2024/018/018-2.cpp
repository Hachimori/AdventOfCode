#include<bits/stdc++.h>
using namespace std;


class Point {
public:
    int r, c;
    Point(int r, int c): r(r), c(c) {}
};


int row, col;
vector<Point> pts;

void read() {
    // For input.txt
    row = 71, col = 71;

    // For tmp
    // row = 7, col = 7;

    int r, c;
    char dummy;
    while (cin >> c >> dummy >> r) {
        pts.push_back(Point(r, c));
    }
}


bool isReachable(int nUse) {
    vector isOk(row, vector(col, true));
    for (int i = 0; i < nUse; ++i) {
        isOk[pts[i].r][pts[i].c] = false;
    }

    vector cost(row, vector(col, -1));
    queue<Point> Q;

    Q.push(Point(0, 0));
    cost[0][0] = 0;

    while (!Q.empty()) {
        Point p = Q.front();
        Q.pop();

        if (p.r == row - 1 && p.c == col - 1) {
            return true;
        }

        const int dr[] = {-1, 0, 1, 0};
        const int dc[] = {0, 1, 0, -1};
        for (int i = 0; i < 4; ++i) {
            int nr = p.r + dr[i];
            int nc = p.c + dc[i];

            if (nr < 0 || nr >= row || nc < 0 || nc >= col) {
                continue;
            }

            if (!isOk[nr][nc]) {
                continue;
            }

            if (cost[nr][nc] != -1) {
                continue;
            }

            cost[nr][nc] = cost[p.r][p.c] + 1;
            Q.push(Point(nr, nc));
        }
    }

    return false;
}


void work() {
    for (int nUse = 0; ; ++nUse) {
        if (!isReachable(nUse)) {
            cout << pts[nUse - 1].c << "," << pts[nUse - 1].r << endl;
            break;
        }
    }
}


int main() {
    read();
    work();
    return 0;
}
