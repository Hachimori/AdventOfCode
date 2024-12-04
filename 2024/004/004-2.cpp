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
    const static string pattern[4][3] = {
        {
            "M.S",
            ".A.",
            "M.S",
        },
        {
            "M.M",
            ".A.",
            "S.S",
        },
        {
            "S.M",
            ".A.",
            "S.M",
        },
        {
            "S.S",
            ".A.",
            "M.M",
        },
    };
    int cnt = 0;
    for (int r = 0; r + 3 <= row; r++) {
        for (int c = 0; c + 3 <= col; c++) {
            for (int i = 0; i < 4; ++i) {
                for (int rr = 0; rr < 3; rr++) {
                    for (int cc = 0; cc < 3; cc++) {
                        if (pattern[i][rr][cc] == '.') {
                            continue;
                        }
                        if (ch[r + rr][c + cc] != pattern[i][rr][cc]) {
                            goto _fail;
                        }
                    }
                }
                ++cnt;
                _fail:;
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
