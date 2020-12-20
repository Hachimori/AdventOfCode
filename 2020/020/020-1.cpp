#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
using namespace std;


class Tile {
public:
    int id;
    vector<string> t;

    Tile(){}
    Tile(int id, vector<string> t): id(id), t(t) {}

    void flip() {
        for (int i = 0; i < t.size(); ++i) {
            reverse(t[i].begin(), t[i].end());
        }
    }

    void rotate() {
        vector<string> next(t[0].size(), string(t.size(), ' '));
        for (int i = 0; i < t.size(); ++i) {
            for (int j = 0; j < t[i].size(); ++j) {
                next[j][t.size() - i - 1] = t[i][j];
            }
        }
        t = next;
    }
};


vector<Tile> tileList;

void read() {
    tileList.clear();

    while (1) {
        string line;
        getline(cin, line);
        if (line.empty()) break;

        int id;
        sscanf(line.c_str(), "Tile %d:", &id);

        vector<string> lineList;
        while (1) {
            getline(cin, line);
            if (line.empty()) break;
            lineList.push_back(line);
        }

        tileList.push_back(Tile(id, lineList));
    }
}


bool rec(int r, int c, vector<bool> &used, int sz, vector<vector<Tile> > &board) {
    if (r == sz) return true;
    if (c == sz) return rec(r + 1, 0, used, sz, board);

    for (int i = 0; i < tileList.size(); ++i) {
        if (used[i]) continue;
        for (int j = 0; j < 2; ++j) {
            tileList[i].flip();
            for (int k = 0; k < 4; ++k) {
                tileList[i].rotate();
                
                board[r][c] = tileList[i];
                
                if (c > 0) {
                    int len = board[r][c].t.size();
                    for (int rr = 0; rr < len; ++rr) {
                        if (board[r][c].t[rr][0] != board[r][c - 1].t[rr][len - 1]) {
                            goto _fail;
                        }
                    }
                }
                
                if (r > 0) {
                    int len = board[r][c].t.size();
                    for (int cc = 0; cc < len; ++cc) {
                        if (board[r][c].t[0][cc] != board[r - 1][c].t[len - 1][cc]) {
                            goto _fail;
                        }
                    }
                }
                
                used[i] = true;
                if (rec(r, c + 1, used, sz, board)) return true;
                used[i] = false;

            _fail:;
            }
        }
    }
    
    return false;
}


void work() {
    int sz = 1;
    while (sz * sz < tileList.size()) ++sz;

    vector<bool> used(tileList.size(), false);
    
    vector<vector<Tile> > board(sz, vector<Tile>(sz));
    rec(0, 0, used, sz, board);

    cout << 1LL * board[0][0].id * board[0][sz - 1].id * board[sz - 1][0].id * board[sz - 1][sz - 1].id << endl;

    vector<string> m(sz * (board[0][0].t.size() - 2));
    for (int i = 0; i < sz; ++i) {
        for (int j = 0; j < sz; ++j) {
            for (int k = 0, l = 1; l < board[i][j].t.size() - 1; ++k, ++l) {
                m[i * (board[i][j].t.size() - 2) + k] += board[i][j].t[l].substr(1, board[i][j].t[l].size() - 2);
            }
        }
    }

    for (int i = 0; i < m.size(); ++i) {
        cout << m[i] << endl;
    }
}


int main() {
    read();
    work();
    return 0;
}
