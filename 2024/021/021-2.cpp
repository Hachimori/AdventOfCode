#include<bits/stdc++.h>
#define r first
#define c second
using namespace std;
const int ROBOT = 25;
const long long INF = 1LL << 60;


class QData {
public:
    int childR, childC;
    int childChildR, childChildC;
    long long cost;

    QData(int childR, int childC, int childChildR, int childChildC, long long cost) :
        childR(childR), childC(childC), childChildR(childChildR), childChildC(childChildC), cost(cost) {}

    bool operator< (const QData &other) const {
        return cost > other.cost;
    }
};

class QData2 {
public:
    int targetIdx;
    int selfR, selfC;
    int childR, childC;
    long long cost;

    QData2(int targetIdx, int selfR, int selfC, int childR, int childC, long long cost) :
        targetIdx(targetIdx), selfR(selfR), selfC(selfC), childR(childR), childC(childC), cost(cost) {}

    bool operator< (const QData2 &other) const {
        return cost > other.cost;
    }
};


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
};
vector<int> row = {4, 2};
vector<int> col = {3, 3};



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


pair<int, int> posIdToRC(int robotId, int posId) {
    if (robotId == 0) {
        if (posId == 0) return {3, 1};
        if (posId == A) return {3, 2};
        return {2 - (posId - 1) / 3, (posId - 1) % 3};
    } else {
        if (posId == 0) return {0, 1}; // UP
        if (posId == 1) return {1, 2}; // RIGHT
        if (posId == 2) return {1, 1}; // DOWN
        if (posId == 3) return {1, 0}; // LEFT
        return {0, 2}; // A
    }
}


int dir2id(int dir) {
    if (dir == 0) return UP;
    if (dir == 1) return RIGHT;
    if (dir == 2) return DOWN;
    if (dir == 3) return LEFT;
    cout << "dir2id: invalid dir: " << dir << endl;
    return -1;
}

pair<int, int> dir2panelPos(int dir) {
    if (dir == 0) return {0, 1};
    if (dir == 1) return {1, 2};
    if (dir == 2) return {1, 1};
    if (dir == 3) return {1, 0};
    cout << "dir2panelPos: invalid dir: " << dir << endl;
    return {-1, -1};
}

// 自分の robotId が robotId で、
// child が (childR, childC) にいるとき、
// self が action を行うためのコストを返す
//   action: 10 (UP) -> 上に行く
//   action: 11 (RIGHT) -> 右に行く
//   action: 12 (DOWN) -> 下に行く
//   action: 13 (LEFT) -> 左に行く
//   action: 14 (A) -> Action する (自分が今いる場所のパネルを押す)
//
//   action を行なった後、child は action に相当するパネルにいて、それ以降の child は A にいる
//
// robotId: 0~27   (0 は含まない)
// childR: 0~1
// childC: 0~2
// action: 10~14    (A,UP,RIGHT,DOWN,LEFT)
long long calcChildAction(
    int robotId, int childR, int childC, int action,
    long long actionDp[ROBOT][2][3][15]
) {
    if (robotId == ROBOT) {
        return 1;
    }

    long long &ret = actionDp[robotId][childR][childC][action];
    if (ret != INF) {
        return ret;
    }

    QData init = QData(
        childR,
        childC,
        0,
        2,
        0
    );
    priority_queue<QData> Q;
    Q.push(init);

    long long dp[2][3][2][3]; // dp[childR][childC][child's childR][child's childC]
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 3; ++j) {
            for (int k = 0; k < 2; ++k) {
                for (int l = 0; l < 3; ++l) {
                    dp[i][j][k][l] = INF;
                }
            }
        }
    }
    dp[init.childR][init.childC][0][2] = 0;

    while (!Q.empty()) {
        QData q = Q.top();
        Q.pop();

        long long cost = dp[q.childR][q.childC][q.childChildR][q.childChildC];
        if (cost < q.cost) {
            continue;
        }

        // act
        if (control[1][q.childR][q.childC] == action) {
            long long nexCost = cost + calcChildAction(robotId + 1, q.childChildR, q.childChildC, A, actionDp);
            ret = min(ret, nexCost);
        }

        // move
        const int dr[] = {-1, 0, 1, 0};
        const int dc[] = {0, 1, 0, -1};
        for (int i = 0; i < 4; ++i) {
            int nextChildR = q.childR + dr[i];
            int nextChildC = q.childC + dc[i];

            if (nextChildR < 0 || nextChildR >= 2 || nextChildC < 0 || nextChildC >= 3) {
                continue;
            }

            if (control[1][nextChildR][nextChildC] == -1) {
                continue;
            }

            auto [nextChildChildR, nextChildChildC] = dir2panelPos(i);
            long long nexCost = cost + calcChildAction(robotId + 1, q.childChildR, q.childChildC, dir2id(i), actionDp);
            if (dp[nextChildR][nextChildC][nextChildChildR][nextChildChildC] > nexCost) {
                dp[nextChildR][nextChildC][nextChildChildR][nextChildChildC] = nexCost;
                Q.push(QData(
                    nextChildR,
                    nextChildC,
                    nextChildChildR,
                    nextChildChildC,
                    nexCost
                ));
            }
        }
    }

    return ret;
}


long long calc(string &target, long long actionTable[ROBOT][2][3][15]) {
    // dp[targetIdx][selfR][selfC][childR][childC]
    long long dp[5][4][3][2][3];
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 4; ++j) {
            for (int k = 0; k < 3; ++k) {
                for (int l = 0; l < 2; ++l) {
                    for (int m = 0; m < 3; ++m) {
                        dp[i][j][k][l][m] = INF;
                    }
                }
            }
        }
    }
    dp[0][3][2][0][2] = 0;

    priority_queue<QData2> Q;
    Q.push(QData2(0, 3, 2, 0, 2, 0));

    while (!Q.empty()) {
        QData2 q = Q.top();
        Q.pop();

        if (q.targetIdx == target.size()) {
            return q.cost;
        }

        long long cost = dp[q.targetIdx][q.selfR][q.selfC][q.childR][q.childC];
        if (cost < q.cost) {
            continue;
        }

        // act
        if (control[0][q.selfR][q.selfC] == target[q.targetIdx]) {
            long long nexCost = cost + calcChildAction(0, q.childR, q.childC, A, actionTable);
            if (dp[q.targetIdx + 1][q.selfR][q.selfC][0][2] > nexCost) {
                dp[q.targetIdx + 1][q.selfR][q.selfC][0][2] = nexCost;
                Q.push(QData2(
                    q.targetIdx + 1,
                    q.selfR,
                    q.selfC,
                    0,
                    2,
                    nexCost
                ));
            }
            continue;
        }

        // move
        const int dr[] = {-1, 0, 1, 0};
        const int dc[] = {0, 1, 0, -1};

        for (int i = 0; i < 4; ++i) {
            int nextSelfR = q.selfR + dr[i];
            int nextSelfC = q.selfC + dc[i];

            if (nextSelfR < 0 || nextSelfR >= 4 || nextSelfC < 0 || nextSelfC >= 3) {
                continue;
            }

            if (control[0][nextSelfR][nextSelfC] == -1) {
                continue;
            }

            auto [nextChildR, nextChildC] = dir2panelPos(i);

            long long nexCost = q.cost + calcChildAction(0, q.childR, q.childC, dir2id(i), actionTable);
            if (dp[q.targetIdx][nextSelfR][nextSelfC][nextChildR][nextChildC] > nexCost) {
                dp[q.targetIdx][nextSelfR][nextSelfC][nextChildR][nextChildC] = nexCost;
                Q.push(QData2(
                    q.targetIdx,
                    nextSelfR,
                    nextSelfC,
                    nextChildR,
                    nextChildC,
                    nexCost
                ));
            }
        }
    }

    return -1;
}


void work() {
    long long actionTable[ROBOT][2][3][15];
    for (int i = 0; i < ROBOT; ++i) {
        for (int j = 0; j < 2; ++j) {
            for (int k = 0; k < 3; ++k) {
                for (int l = 0; l < 15; ++l) {
                    actionTable[i][j][k][l] = INF;
                }
            }
        }
    }


    for (int i = ROBOT - 1; i >= 0; --i) {
        for (int j = 0; j < 2; ++j) {
            for (int k = 0; k < 3; ++k) {
                if (control[1][j][k] == -1) {
                    continue;
                }
                for (int l = 10; l < 15; ++l) {
                    actionTable[i][j][k][l] = calcChildAction(i, j, k, l, actionTable);
                }
            }
        }
    }

    long long ans = 0;
    for (string line : input) {
        long long v = calc(line, actionTable);
        long long toMul = 0;
        for (char ch : line) {
            if (ch == A) {
                break;
            }
            toMul *= 10;
            toMul += ch;
        }
        cout << toMul << ' ' << v << endl;
        ans += toMul * v;
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
