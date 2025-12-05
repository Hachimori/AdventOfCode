#include<bits/stdc++.h>
using namespace std;

vector<string> ch;

void read() {
    string s;
    while (cin >> s) {
        ch.push_back(s);
    }
}


void work() {
    int row = ch.size();
    int col = ch[0].size();

    const int dr[] = {-1, -1, -1, 0, 1, 1, 1, 0};
    const int dc[] = {-1, 0, 1, 1, 1, 0, -1, -1};

    int ans = 0;
    for (int r = 0; r < row; ++r) {
        for (int c = 0; c < col; ++c) {
            if (ch[r][c] != '@') {
                continue;
            }
            int cnt = 0;
            for (int i = 0; i < 8; ++i) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                if (!(0 <= nr && nr < row && 0 <= nc && nc < col)) {
                    continue;
                }
                cnt += ch[nr][nc] == '@';
            }
            ans += cnt < 4;
        }
    }

    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
