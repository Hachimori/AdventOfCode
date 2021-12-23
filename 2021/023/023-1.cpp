// Compile:
//   $ g++ -O2 023-1.cpp
// Runtime is 5m43.107s
// Environment:
//   - 2.6 GHz 6 core intel Core i7
//   - 16 GB 2400 MHz DDR4 RAM

#include<iostream>
#include<queue>
#include<vector>
#include<map>
#include<cctype>
#include<cstring>
#define r first
#define c second
using namespace std;
typedef pair<int, int> Point;


class QData {
public:
    int cost, estCost;
    vector<Point> state;

    QData(int cost, int estCost, vector<Point> &state):
        cost(cost), estCost(estCost), state(state) {}
    
    bool operator< (const QData &opp) const {
        return cost + estCost > opp.cost + opp.estCost;
    }
};


const int row = 5, col = 13;
string ch[] =
    {
     "#############",
     "#...........#",
     "###.#.#.#.###",
     "###.#.#.#.###",
     "#############"
    };
vector<Point> init;

void read() {
    vector<Point> ch2pt[4];
    
    for (int r = 0; r < row; ++r) {
        string s;
        if (!getline(cin, s)) break;
        for (int c = 0; c < col; ++c) {
            if (isalpha(s[c])) {
                ch2pt[s[c] - 'A'].push_back(Point(r, c));
            }
        }
    }

    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 2; ++j) {
            init.push_back(ch2pt[i][j]);
        }
    }
}


int calcEstCost(vector<Point> &curState, vector<Point> &goal) {
    static int ch2cost[] = {1, 10, 100, 1000};

    int ret = 0;
    for (int chType = 0; chType < 4; ++chType) {
        int cost[row][col];
        queue<Point> Q;

        memset(cost, -1, sizeof(cost));
        Q.push(goal[chType * 2]);
        Q.push(goal[chType * 2 + 1]);
        cost[goal[chType * 2].r][goal[chType * 2].c] = 0;
        cost[goal[chType * 2 + 1].r][goal[chType * 2 + 1].c] = 0;


        while (!Q.empty()) {
            Point cur = Q.front();
            Q.pop();

            static int dr[] = {-1, 0, 1, 0};
            static int dc[] = {0, 1, 0, -1};
            for (int i = 0; i < 4; ++i) {
                int nr = cur.r + dr[i];
                int nc = cur.c + dc[i];

                if (ch[nr][nc] != '.') continue;
                if (cost[nr][nc] == -1) {
                    cost[nr][nc] = cost[cur.r][cur.c] + 1;
                    Q.push(Point(nr, nc));
                }
            }
        }

        ret += ch2cost[chType] * cost[curState[chType * 2].r][curState[chType * 2].c];
        ret += ch2cost[chType] * cost[curState[chType * 2 + 1].r][curState[chType * 2 + 1].c];
    }

    return ret;
}


void work() {
    vector<Point> goal;
    goal.push_back(Point(2, 3));
    goal.push_back(Point(3, 3));
    goal.push_back(Point(2, 5));
    goal.push_back(Point(3, 5));
    goal.push_back(Point(2, 7));
    goal.push_back(Point(3, 7));
    goal.push_back(Point(2, 9));
    goal.push_back(Point(3, 9));
    
    priority_queue<QData> Q;
    map<vector<Point>, int> state2cost;

    Q.push(QData(0, calcEstCost(init, goal), init));
    state2cost[init] = 0;


    while (!Q.empty()) {
        QData cur = Q.top();
        Q.pop();
        
        if (cur.state == goal) {
            cout << cur.cost << endl;
            break;
        }

        if (state2cost[cur.state] < cur.cost) {
            continue;
        }

        for (int ptIdx = 0; ptIdx < 8; ++ptIdx) {
            static int dr[] = {-1, 0, 1, 0};
            static int dc[] = {0, 1, 0, -1};
            for (int i = 0; i < 4; ++i) {
                int nr = cur.state[ptIdx].r + dr[i];
                int nc = cur.state[ptIdx].c + dc[i];
                if (ch[nr][nc] != '.') continue;
                if (count(cur.state.begin(), cur.state.end(), Point(nr, nc))) continue;

                vector<Point> nexState = cur.state;
                nexState[ptIdx] = Point(nr, nc);

                for (int j = 0; j < 8; j += 2) {
                    if (nexState[j] > nexState[j + 1]) {
                        swap(nexState[j], nexState[j + 1]);
                    }
                }
                
                static int ch2cost[] = {1, 10, 100, 1000};
                int nexCost = cur.cost + ch2cost[ptIdx / 2];
                    
                if (!state2cost.count(nexState) || state2cost[nexState] > nexCost) {
                    state2cost[nexState] = nexCost;
                    Q.push(QData(nexCost, calcEstCost(nexState, goal), nexState));
                }
            }
        }
    }
}


int main() {
    read();
    work();
    return 0;
}
