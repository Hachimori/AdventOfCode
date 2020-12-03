#include<iostream>
#include<string>
#include<set>
#include<vector>
using namespace std;


int row, col;
vector<vector<bool> > initB;

void read() {
    string s;
    while (cin >> s) {
        initB.push_back(vector<bool>());
        for (int i = 0; i < s.size(); ++i) {
            initB.back().push_back(s[i] == '#');
        }
    }
    row = initB.size();
    col = initB[0].size();
}


void work() {
    set<vector<vector<bool> > > bSet;

    vector<vector<bool> > b = initB;
    
    while (1) {
        if (bSet.count(b)) {
            break;
        }
        bSet.insert(b);
        
        vector<vector<bool> > nextB = b;
        for (int r = 0; r < row; ++r) {
            for (int c = 0; c < col; ++c) {
                static int dr[] = {-1, 0, 1, 0};
                static int dc[] = {0, 1, 0, -1};
                
                int cnt = 0;
                for (int i = 0; i < 4; ++i) {
                    int nr = r + dr[i];
                    int nc = c + dc[i];
                    if (!(0 <= nr && nr < row && 0 <= nc && nc < col)) {
                        continue;
                    }
                    cnt += b[nr][nc];
                }

                if (b[r][c]) {
                    nextB[r][c] = cnt == 1;
                } else {
                    nextB[r][c] = cnt == 1 || cnt == 2;
                }
            }
        }

        b = nextB;
    }

    int ans = 0;
    for (int r = 0; r < row; ++r) {
        for (int c = 0; c < col; ++c) {
            if (b[r][c]) {
                ans += (1 << (r * col + c));
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
