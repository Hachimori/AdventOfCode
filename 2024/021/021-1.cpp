#include<bits/stdc++.h>
using namespace std;
const int INF = 1 << 30;


enum Op {
    A = 10,
    UP = 11,
    RIGHT = 12,
    DOWN = 13,
    LEFT = 14,
};


vector<vector<vector<int>>> control = {
    {{7, 8, 9},
     {4, 5, 6},
     {1, 2, 3},
     {-1, 0, A},},

    {{-1, UP, A},
     {LEFT, DOWN, RIGHT}},

    {{-1, UP, A},
     {LEFT, DOWN, RIGHT}},
};
vector<int> row = {4, 2, 2};
vector<int> col = {3, 3, 3};


class QData {
public:
    int targetIdx;
    vector<int> r;
    vector<int> c;
    QData(int targetIdx, vector<int> r, vector<int> c) : targetIdx(targetIdx), r(r), c(c) {}
};

vector<string> input;

void read() {
    string line;
    while (cin >> line) {
        for (int i = 0; i < line.size(); i++) {
            if (line[i] == 'A') {
                line[i] = A;
            } else {
                line[i] -= '0';
            }
        }
        input.push_back(line);
    }
}


int calc(string &target) {
    queue<QData> Q;
    Q.push(QData(
        0,
        {3, 0, 0},
        {2, 2, 2}
    ));

    // dp[targetIdx][r0][c0][r1][c1][r2][c2]
    int dp[10][4][3][2][3][2][3];

    memset(dp, -1, sizeof(dp));
    dp[0][3][2][0][2][0][2] = 0;

    while (!Q.empty()) {
        QData q = Q.front();
        Q.pop();

        int cost = dp[q.targetIdx][q.r[0]][q.c[0]][q.r[1]][q.c[1]][q.r[2]][q.c[2]];

        // cout << q.targetIdx << " " << q.r[0] << " " << q.c[0] << " " << q.r[1] << " " << q.c[1] << " " << q.r[2] << " " << q.c[2] << endl;

        if (q.targetIdx == target.size()) {
            return cost;
        }

        // move
        const int dr[] = {-1, 0, 1, 0};
        const int dc[] = {0, 1, 0, -1};

        for (int i = 0; i < 4; ++i) {
            int nr2 = q.r[2] + dr[i];
            int nc2 = q.c[2] + dc[i];

            if (nr2 < 0 || nr2 >= row[2] || nc2 < 0 || nc2 >= col[2]) {
                continue;
            }

            if (dp[q.targetIdx][q.r[0]][q.c[0]][q.r[1]][q.c[1]][nr2][nc2] == -1) {
                dp[q.targetIdx][q.r[0]][q.c[0]][q.r[1]][q.c[1]][nr2][nc2] = cost + 1;

                Q.push(QData(
                    q.targetIdx,
                    {q.r[0], q.r[1], nr2},
                    {q.c[0], q.c[1], nc2}
                ));
            }
        }

        // push
        for (int i = 2; i >= 0; --i) {
            if (control[i][q.r[i]][q.c[i]] == -1) {
                // prohibited
                break;
            }

            if (control[i][q.r[i]][q.c[i]] == UP) {
                if (q.r[i - 1] == 0 || control[i - 1][q.r[i - 1] - 1][q.c[i - 1]] == -1) {
                    // out of range
                    break;
                }
                q.r[i - 1] -= 1;
                if (dp[q.targetIdx][q.r[0]][q.c[0]][q.r[1]][q.c[1]][q.r[2]][q.c[2]] == -1) {
                    dp[q.targetIdx][q.r[0]][q.c[0]][q.r[1]][q.c[1]][q.r[2]][q.c[2]] = cost + 1;
                    Q.push(QData(
                        q.targetIdx,
                        q.r,
                        q.c
                    ));
                }
                q.r[i - 1] += 1;
                break;
            } else if (control[i][q.r[i]][q.c[i]] == RIGHT) {
                if (q.c[i - 1] == col[i - 1] - 1 || control[i - 1][q.r[i - 1]][q.c[i - 1] + 1] == -1) {
                    // out of range
                    break;
                }
                q.c[i - 1] += 1;
                if (dp[q.targetIdx][q.r[0]][q.c[0]][q.r[1]][q.c[1]][q.r[2]][q.c[2]] == -1) {
                    dp[q.targetIdx][q.r[0]][q.c[0]][q.r[1]][q.c[1]][q.r[2]][q.c[2]] = cost + 1;
                    Q.push(QData(
                        q.targetIdx,
                        q.r,
                        q.c
                    ));
                }
                q.c[i - 1] -= 1;
                break;
            } else if (control[i][q.r[i]][q.c[i]] == DOWN) {
                if (q.r[i - 1] == row[i - 1] - 1 || control[i - 1][q.r[i - 1] + 1][q.c[i - 1]] == -1) {
                    // out of range
                    break;
                }
                q.r[i - 1] += 1;
                if (dp[q.targetIdx][q.r[0]][q.c[0]][q.r[1]][q.c[1]][q.r[2]][q.c[2]] == -1) {
                    dp[q.targetIdx][q.r[0]][q.c[0]][q.r[1]][q.c[1]][q.r[2]][q.c[2]] = cost + 1;
                    Q.push(QData(
                        q.targetIdx,
                        q.r,
                        q.c
                    ));
                }
                q.r[i - 1] -= 1;
                break;
            } else if (control[i][q.r[i]][q.c[i]] == LEFT) {
                if (q.c[i - 1] == 0 || control[i - 1][q.r[i - 1]][q.c[i - 1] - 1] == -1) {
                    // out of range
                    break;
                }
                q.c[i - 1] -= 1;
                if (dp[q.targetIdx][q.r[0]][q.c[0]][q.r[1]][q.c[1]][q.r[2]][q.c[2]] == -1) {
                    dp[q.targetIdx][q.r[0]][q.c[0]][q.r[1]][q.c[1]][q.r[2]][q.c[2]] = cost + 1;
                    Q.push(QData(
                        q.targetIdx,
                        q.r,
                        q.c
                    ));
                }
                q.c[i - 1] += 1;
                break;
            } else if (control[i][q.r[i]][q.c[i]] == A) {
                if (i == 0) {
                    if (target[q.targetIdx] == A) {
                        if (dp[q.targetIdx + 1][q.r[0]][q.c[0]][q.r[1]][q.c[1]][q.r[2]][q.c[2]] == -1) {
                            dp[q.targetIdx + 1][q.r[0]][q.c[0]][q.r[1]][q.c[1]][q.r[2]][q.c[2]] = cost + 1;
                            Q.push(QData(
                                q.targetIdx + 1,
                                q.r,
                                q.c
                            ));
                        }
                    } else {
                        // wrong target
                        break;
                    }
                } else {
                    // next robot is moved
                    continue;
                }
            } else {
                // number (first robot only)
                if (target[q.targetIdx] == control[i][q.r[i]][q.c[i]]) {
                    if (dp[q.targetIdx + 1][q.r[0]][q.c[0]][q.r[1]][q.c[1]][q.r[2]][q.c[2]] == -1) {
                        dp[q.targetIdx + 1][q.r[0]][q.c[0]][q.r[1]][q.c[1]][q.r[2]][q.c[2]] = cost + 1;

                        Q.push(QData(
                            q.targetIdx + 1,
                            q.r,
                            q.c
                        ));
                    }
                } else {
                    // wrong target
                    break;
                }
            }
        }
    }

    return -1;
}


void work() {
    long long ans = 0;
    for (string line : input) {
        long long v = calc(line);
        long long toMul = 0;
        for (char ch : line) {
            if (ch == A) {
                break;
            }
            toMul *= 10;
            toMul += ch;
        }
        ans += toMul * v;
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
