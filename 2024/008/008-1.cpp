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
    vector<vector<pair<int, int>>> ch2posList(256);
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            if (ch[i][j] == '.') {
                continue;
            }
            ch2posList[ch[i][j]].push_back({i, j});
        }
    }

    set<pair<int, int>> used;
    for (int ch = 0; ch < 256; ++ch) {
        for (int i = 0; i < ch2posList[ch].size(); i++) {
            int r1 = ch2posList[ch][i].first;
            int c1 = ch2posList[ch][i].second;
            for (int j = i + 1; j < ch2posList[ch].size(); ++j) {
                int r2 = ch2posList[ch][j].first;
                int c2 = ch2posList[ch][j].second;

                int dr = r2 - r1;
                int dc = c2 - c1;

                auto add = [&](int r, int c) {
                    if (r < 0 || r >= row || c < 0 || c >= col) {
                        return;
                    }
                    used.insert({r, c});
                };

                add(r2 + dr, c2 + dc);
                add(r1 - dr, c1 - dc);
            }
        }
    }

    cout << used.size() << endl;
}


int main() {
    read();
    work();
    return 0;
}
