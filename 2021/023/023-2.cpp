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


const int row = 7, col = 13;
string ch[] =
    {
     "#############",
     "#...........#",
     "###.#.#.#.###",
     "###.#.#.#.###",
     "###.#.#.#.###",
     "###.#.#.#.###",
     "#############"
    };
vector<Point> init;

void read() {
    vector<Point> ch2pt[4];
    
    for (int r = 0; r < row; ++r) {
        string s;
        if (r == 3) {
            s = "###D#C#B#A###";
        } else if (r == 4) {
            s = "###D#B#A#C###";
        } else if (!getline(cin, s)) {
            break;
        }

        for (int c = 0; c < col; ++c) {
            if (isalpha(s[c])) {
                ch2pt[s[c] - 'A'].push_back(Point(r, c));
            }
        }
    }

    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            init.push_back(ch2pt[i][j]);
        }
    }
}


int calcEstCost(const vector<Point> &curState, const vector<Point> &goal) {
    static int ch2cost[] = {1, 10, 100, 1000};

    int ret = 0;
    for (int chType = 0; chType < 4; ++chType) {
        int cost[row][col];
        queue<Point> Q;

        memset(cost, -1, sizeof(cost));
        for (int i = 0; i < 4; ++i) {
            Q.push(goal[chType * 4 + i]);
            cost[goal[chType * 4 + i].r][goal[chType * 4 + i].c] = 0;
        }

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
        for (int i = 0; i < 4; ++i) {
            ret += ch2cost[chType] * cost[curState[chType * 4 + i].r][curState[chType * 4 + i].c];
        }
    }

    return ret;
}


vector<pair<Point, int> > genMoveCandi(const vector<Point> &state, int movePtIdx) {
    static int ch2cost[] = {1, 10, 100, 1000};
    int visited[row][col];
    queue<Point> Q;

    memset(visited, -1, sizeof(visited));
    visited[state[movePtIdx].r][state[movePtIdx].c] = 0;
    Q.push(state[movePtIdx]);
    
    while (!Q.empty()) {
        Point cur = Q.front();
        Q.pop();
        
        static int dr[] = {-1, 0, 1, 0};
        static int dc[] = {0, 1, 0, -1};
        for (int i = 0; i < 4; ++i) {
            int nr = cur.r + dr[i];
            int nc = cur.c + dc[i];
            if (ch[nr][nc] != '.') continue;
            if (count(state.begin(), state.end(), Point(nr, nc))) continue;
            if (visited[nr][nc] == -1) {
                visited[nr][nc] = visited[cur.r][cur.c] + 1;
                Q.push(Point(nr, nc));
            }
        }
    }

    vector<pair<Point, int> > candi;
    
    if (state[movePtIdx].r != 1) {
        for (int c = 0; c < col; ++c) {
            if (visited[1][c] == -1) continue;
            if (c == 3 || c == 5 || c == 7 || c == 9) continue;
            candi.push_back(make_pair(Point(1, c), visited[1][c] * ch2cost[movePtIdx / 4]));
        }
    } else {
        for (int r = 5; r >= 2; --r) {
            // 'A' -> checkCol = 3
            // 'B' -> checkCol = 5
            // 'C' -> checkCol = 7
            // 'D' -> checkCol = 9
            int checkCol = 3 + movePtIdx / 4 * 2;

            int ptIdx = find(state.begin(), state.end(), Point(r, checkCol)) - state.begin();
            if (ptIdx != 16 && ptIdx / 4 != movePtIdx / 4) break;

            if (visited[r][checkCol] == -1) continue;
        
            candi.push_back(make_pair(Point(r, checkCol), visited[r][checkCol] * ch2cost[movePtIdx / 4]));

            break;
        }
    }
    
    return candi;
}


void work() {
    vector<Point> goal;
    goal.push_back(Point(2, 3));
    goal.push_back(Point(3, 3));
    goal.push_back(Point(4, 3));
    goal.push_back(Point(5, 3));
    goal.push_back(Point(2, 5));
    goal.push_back(Point(3, 5));
    goal.push_back(Point(4, 5));
    goal.push_back(Point(5, 5));
    goal.push_back(Point(2, 7));
    goal.push_back(Point(3, 7));
    goal.push_back(Point(4, 7));
    goal.push_back(Point(5, 7));
    goal.push_back(Point(2, 9));
    goal.push_back(Point(3, 9));
    goal.push_back(Point(4, 9));
    goal.push_back(Point(5, 9));
    
    priority_queue<QData> Q;
    map<vector<Point>, int> state2cost;

    map<vector<Point>, vector<Point> > pre;

    Q.push(QData(0, calcEstCost(init, goal), init));
    state2cost[init] = 0;
    pre[init] = vector<Point>();
    

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

        for (int ptIdx = 0; ptIdx < 16; ++ptIdx) {
            vector<pair<Point, int> > candi = genMoveCandi(cur.state, ptIdx);

            for (int i = 0; i < candi.size(); ++i) {
                vector<Point> nexState = cur.state;
                nexState[ptIdx] = candi[i].first;

                for (int j = 0; j < 4; ++j) {
                    sort(nexState.begin() + j * 4, nexState.begin() + j * 4 + 4);
                }
                if (!state2cost.count(nexState) || state2cost[nexState] > cur.cost + candi[i].second) {
                    pre[nexState] = cur.state;
                    state2cost[nexState] = cur.cost + candi[i].second;
                    Q.push(QData(cur.cost + candi[i].second, calcEstCost(nexState, goal), nexState));
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
