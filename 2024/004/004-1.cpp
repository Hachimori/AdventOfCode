#include<bits/stdc++.h>
using namespace std;


int row, col;
vector<string> ch;

void read() {
    string line;
    while (getline(cin, line)) {
        ch.push_back(line);
    }
    row = ch.size();
    col = ch[0].size();
}


void work() {
    int cnt = 0;
    for (int r = 0; r < row; r++) {
        for (int c = 0; c < col; c++) {
            const static int dr[] = {-1, -1, -1, 0, 1, 1, 1, 0};
            const static int dc[] = {-1, 0, 1, 1, 1, 0, -1, -1};
            for (int i = 0; i < 8; ++i) {
                int rr = r;
                int cc = c;
                string cmp;
                while (0 <= rr && rr < row && 0 <= cc && cc < col) {
                    cmp += ch[rr][cc];
                    if (cmp.size() == 4) {
                        break;
                    }
                    rr += dr[i];
                    cc += dc[i];
                }
                cnt += cmp == "XMAS";
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
