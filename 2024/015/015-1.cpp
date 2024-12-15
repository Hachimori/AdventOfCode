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
        ch.push_back(line);
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


void work() {
    const static int dr[] = {-1, 0, 1, 0};
    const static int dc[] = {0, 1, 0, -1};
    const static string move = "^>v<";

    int curR = sr;
    int curC = sc;

    for (char moveCh : op) {
        int dir = move.find(moveCh);

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

    int ans = 0;
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            if (ch[i][j] == 'O') {
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
