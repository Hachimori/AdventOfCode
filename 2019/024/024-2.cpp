#include<iostream>
#include<string>
#include<vector>
using namespace std;
const int LOOP = 200;
const int DEPTH = 500;

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
    vector<vector<vector<bool> > > b(DEPTH, vector<vector<bool> >(row, vector<bool>(col)));
    b[DEPTH / 2] = initB;
    
    
    for (int loop = 0; loop < LOOP; ++loop) {
        vector<vector<vector<bool> > > nextB = b;
        for (int d = 0; d < DEPTH; ++d) {
            for (int r = 0; r < row; ++r) {
                for (int c = 0; c < col; ++c) {
                    if (r == 2 && c == 2) continue;
                    
                    static int dr[] = {-1, 0, 1, 0};
                    static int dc[] = {0, 1, 0, -1};
                
                    int cnt = 0;
                    for (int i = 0; i < 4; ++i) {
                        int nr = r + dr[i];
                        int nc = c + dc[i];
                        
                        if (!(0 <= nr && nr < row && 0 <= nc && nc < col)) {
                            if (d - 1 < 0) continue;
                            static int nnr[] = {1, 2, 3, 2};
                            static int nnc[] = {2, 3, 2, 1};
                            cnt += b[d - 1][nnr[i]][nnc[i]];
                            continue;
                        } else if (nr == 2 && nc == 2) {
                            if (d + 1 >= DEPTH) continue;
                            
                            static int nnr[4][5] =
                                {
                                 {4, 4, 4, 4, 4},
                                 {0, 1, 2, 3, 4},
                                 {0, 0, 0, 0, 0},
                                 {0, 1, 2, 3, 4}
                                };
                            static int nnc[4][5] =
                                {
                                 {0, 1, 2, 3, 4},
                                 {0, 0, 0, 0, 0},
                                 {0, 1, 2, 3, 4},
                                 {4, 4, 4, 4, 4}
                                };

                            for (int j = 0; j < 5; ++j) {
                                cnt += b[d + 1][nnr[i][j]][nnc[i][j]];
                            }
                            continue;
                        }
                        
                        cnt += b[d][nr][nc];
                    }

                    if (b[d][r][c]) {
                        nextB[d][r][c] = cnt == 1;
                    } else {
                        nextB[d][r][c] = cnt == 1 || cnt == 2;
                    }
                }
            }
        }

        b = nextB;
    }

    int ans = 0;
    for (int d = 0; d < DEPTH; ++d) {
        for (int r = 0; r < row; ++r) {
            for (int c = 0; c < col; ++c) {
                ans += b[d][r][c];
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
