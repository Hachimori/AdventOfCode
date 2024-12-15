#include<bits/stdc++.h>
using namespace std;


int row, col;
int sr, sc;
vector<string> ch;
string op;

void read() {
    string line;
    while (getline(cin, line)) {
        if (line.empty()) {
            break;
        }
        string toPush;
        for (char c : line) {
            if (c == '#') toPush += "##";
            if (c == 'O') toPush += "[]";
            if (c == '.') toPush += "..";
            if (c == '@') toPush += "@.";
        }
        ch.push_back(toPush);
    }

    while (getline(cin, line)) {
        op += line;
    }

    row = ch.size();
    col = ch[0].size();
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            if (ch[i][j] == '@') {
                sr = i;
                sc = j;
                ch[i][j] = '.';
            }
        }
    }
}


const static int dr[] = {-1, 0, 1, 0};
const static int dc[] = {0, 1, 0, -1};


bool recVerticalOpCheck(int r, int c, int dir) {
    int rr = r + dr[dir];

    if (ch[rr][c] == '#') {
        return false;
    }
    if (ch[rr][c] == '.') {
        return true;
    }
    if (ch[rr][c] == '[') {
        return
            recVerticalOpCheck(rr, c, dir) &&
            recVerticalOpCheck(rr, c + 1, dir);
    }
    if (ch[rr][c] == ']') {
        return
            recVerticalOpCheck(rr, c, dir) &&
            recVerticalOpCheck(rr, c - 1, dir);
    }
    cout << "unknown character: " << ch[rr][c] << endl;
    return false;
}


void recVerticalMove(int r, int c, int dir, vector<vector<bool>> &visited) {
    if (visited[r][c]) {
        return;
    }
    visited[r][c] = true;

    int rr = r + dr[dir];

    if (ch[rr][c] == '.') {
    } else if (ch[rr][c] == '[') {
        recVerticalMove(rr, c, dir, visited);
        recVerticalMove(rr, c + 1, dir, visited);
    } else if (ch[rr][c] == ']') {
        recVerticalMove(rr, c, dir, visited);
        recVerticalMove(rr, c - 1, dir, visited);
    }
    swap(ch[r][c], ch[rr][c]);
}


void verticalOp(int dir, int &curR, int &curC) {
    if (recVerticalOpCheck(curR, curC, dir)) {
        vector visited(row, vector(col, false));
        recVerticalMove(curR, curC, dir, visited);
        curR += dr[dir];
    }
}


void horizontalOp(int dir, int &curR, int &curC) {
    int rr = curR + dr[dir];
    int cc = curC + dc[dir];

    while (1) {
        if (ch[rr][cc] == '.') {
            int rrr = rr;
            int ccc = cc;
            while (rrr - dr[dir] != curR || ccc - dc[dir] != curC) {
                swap(ch[rrr][ccc], ch[rrr - dr[dir]][ccc - dc[dir]]);
                rrr -= dr[dir];
                ccc -= dc[dir];
            }
            curR += dr[dir];
            curC += dc[dir];
            break;
        } else if (ch[rr][cc] == '#') {
            break;
        }
        rr += dr[dir];
        cc += dc[dir];
    }
}


void work() {
    const static string move = "^>v<";

    int curR = sr;
    int curC = sc;

    for (char moveCh : op) {
        int dir = move.find(moveCh);
        if (dir % 2 == 0) {
            verticalOp(dir, curR, curC);
        } else {
            horizontalOp(dir, curR, curC);
        }
    }

    int ans = 0;
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            if (ch[i][j] == '[') {
                ans += 100 * i + j;
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
