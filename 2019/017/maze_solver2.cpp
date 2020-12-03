#include<iostream>
#include<vector>
using namespace std;
const int LENG_LIMIT = 20;


enum Turn {
           LEFT = -1,
           RIGHT = -2
};


int row, col;
vector<string> b;

void read() {
    b.clear();
    
    string s;
    while (cin >> s) {
        b.push_back(s);
    }

    row = b.size();
    col = b[0].size();
}


vector<int> getMove() {
    int sr, sc, sdir;
    for (int r = 0; r < b.size(); ++r) {
        for (int c = 0; c < b[r].size(); ++c) {
            // Do not consider '>','v','<' cases
            if (b[r][c] == '^') {
                sr = r;
                sc = c;
                sdir = 0;
            }
        }
    }
    
    int r = sr;
    int c = sc;
    int dir = sdir;

    static int dr[] = {-1, 0, 1, 0};
    static int dc[] = {0, 1, 0, -1};
    
    vector<int> ret;
    while (1) {
        int cnt = 0;
        while (1) {
            int nr = r + dr[dir];
            int nc = c + dc[dir];
            if (!(0 <= nr && nr < row && 0 <= nc && nc < col && b[nr][nc] == '#')) break;
            r = nr;
            c = nc;
            ++cnt;
        }

        if (cnt) ret.push_back(cnt);

        int nextDDir = 0;
        for (int ddir = -1; ddir <= 1; ++ddir) {
            if (ddir == 0) continue;
            int nr = r + dr[(dir + ddir + 4) % 4];
            int nc = c + dc[(dir + ddir + 4) % 4];
            if (0 <= nr && nr < row && 0 <= nc && nc < col && b[nr][nc] == '#') {
                nextDDir = ddir;
                break;
            }
        }

        if (nextDDir == -1) {
            ret.push_back(LEFT);
        } else if (nextDDir == 1) {
            ret.push_back(RIGHT);
        } else {
            break;
        }
        dir = (dir + 4 + nextDDir) % 4;
    }
    
    return ret;
}


int calcLeng(vector<int> &moves) {
    int ret = 0;
    for (int i = 0; i < moves.size(); ++i) {
        if (i) ret++; // ','
        int n = moves.size();
        if (n < 0) ++ret;
        else {
            while (n) {
                ++ret;
                n /= 10;
            }
        }
    }

    return ret;
}


void printMove(vector<int> &moves) {
    for (int i = 0; i < moves.size(); ++i) {
        if (i) cout << ",";
        if (moves[i] == LEFT) {
            cout << "L";
        } else if (moves[i] == RIGHT) {
            cout << "R";
        } else {
            cout << moves[i];
        }
    }
    cout << endl;
}
                            

bool rec(int idx, vector<vector<int> > &moveList, vector<int> &orig, vector<int> &history) {
    if (idx == orig.size()) {
        return true;
    }
    
    for (int i = 0; i < moveList.size(); ++i) {
        vector<int> &move = moveList[i];
        
        if (idx + move.size() > orig.size()) continue;

        for (int j = 0; j < move.size(); ++j) {
            if (move[j] != orig[idx + j]) {
                goto _fail;
            }
        }

        history.push_back(i);
        if (rec(idx + move.size(), moveList, orig, history)) {
            return true;
        }
        history.pop_back();
        
    _fail:;
    }

    return false;
}


void compressMove(vector<int> &moves) {
    /*
    for (int i = 0; i < moves.size(); ++i) {
        cout << moves[i] << ' ';
    }
    cout << endl;
    */

    int aBgn = 0;
    for (int aEnd = 2; aEnd < moves.size(); aEnd += 2) {
        for (int bBgn = aEnd + 2; bBgn < moves.size(); bBgn += 2) {
            for (int bEnd = bBgn + 2; bEnd < moves.size(); bEnd += 2) {
                for (int cBgn = bBgn + 2; cBgn < moves.size(); cBgn += 2) {
                    for (int cEnd = cBgn + 2; cEnd < moves.size(); cEnd += 2) {
                        vector<vector<int> > moveList;
                        moveList.push_back(vector<int>(moves.begin() + aBgn, moves.begin() + aEnd));
                        moveList.push_back(vector<int>(moves.begin() + bBgn, moves.begin() + bEnd));
                        moveList.push_back(vector<int>(moves.begin() + cBgn, moves.begin() + cEnd));

                        if (calcLeng(moveList[0]) > LENG_LIMIT) continue;
                        if (calcLeng(moveList[1]) > LENG_LIMIT) continue;
                        if (calcLeng(moveList[2]) > LENG_LIMIT) continue;

                        vector<int> history;
                        if (rec(0, moveList, moves, history)) {
                            printMove(moveList[0]);
                            printMove(moveList[1]);
                            printMove(moveList[2]);
                            for (int i = 0; i < history.size(); ++i) {
                                if (i) cout << ",";
                                cout << "ABC"[history[i]];
                            }
                            cout << endl;
                            return;
                        }
                    }
                }
            }
        }
    }
}


int main() {
    read();
    vector<int> moves = getMove();
    compressMove(moves);
    return 0;
}
