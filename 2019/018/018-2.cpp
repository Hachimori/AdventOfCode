#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<queue>
#include<cctype>
#define r first
#define c second
using namespace std;
const int SIZE = 100;
const int NODE = 30;
typedef pair<int, int> Point;


class State {
public:
    vector<int> idList;
    int mask;

    State(){}
    State(vector<int> idList, int mask):
        idList(idList), mask(mask) {}

    bool operator< (const State &opp) const {
        if (idList != opp.idList) return idList < opp.idList;
        return mask < opp.mask;
    }
};


int row, col;
vector<string> b;
Point id2pt[NODE];  // id2pos[id] = (row, col)

void read() {
    b.clear();
    
    string s;
    while (cin >> s) {
        b.push_back(s);
    }

    row = b.size();
    col = b[0].size();

    int nRobot = 0;
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            if (b[i][j] == '@') {
                id2pt[26 + nRobot++] = Point(i, j);
            } else if (islower(b[i][j])) {
                id2pt[b[i][j] - 'a'] = Point(i, j);
            }
        }
    }
}


void bfs(int initId, int mask, int id2distance[NODE]) {
    int cost[SIZE][SIZE];
    queue<Point> Q;

    memset(cost, -1, sizeof(cost));
    
    Q.push(id2pt[initId]);
    cost[id2pt[initId].r][id2pt[initId].c] = 0;

    while (!Q.empty()) {
        Point curr = Q.front();
        Q.pop();

        static int dr[] = {-1, 0, 1, 0};
        static int dc[] = {0, -1, 0, 1};
        for (int i = 0; i < 4; ++i) {
            int nr = curr.r + dr[i];
            int nc = curr.c + dc[i];
            if (b[nr][nc] == '#') continue;
            if (isupper(b[nr][nc]) && !(mask & (1 << (b[nr][nc] - 'A')))) continue;
            if (cost[nr][nc] != -1) continue;
            
            if (islower(b[nr][nc])) {
                id2distance[b[nr][nc] - 'a'] = cost[curr.r][curr.c] + 1;
            }
            cost[nr][nc] = cost[curr.r][curr.c] + 1;
            Q.push(Point(nr, nc));
        }
    }
}


void work() {
    priority_queue<
        pair<int, State>,
        vector<pair<int, State> >,
        greater<pair<int, State> > > Q;
    map<State, int> cost;

    State initState;
    initState.idList.push_back(26);
    initState.idList.push_back(27);
    initState.idList.push_back(28);
    initState.idList.push_back(29);
    initState.mask = 0;
    
    Q.push(make_pair(0, initState));
    cost[initState] = 0;

    while (!Q.empty()) {
        State curr = Q.top().second;
        int currCost = Q.top().first;

        Q.pop();

        if (cost[curr] < currCost) {
            continue;
        }

        if (curr.mask == (1 << 26) - 1) {
            cout << currCost << endl;
            break;
        }
        
        int id2distance[4][NODE];
        memset(id2distance, -1, sizeof(id2distance));

        for (int robot = 0; robot < 4; ++robot) {
            bfs(curr.idList[robot], curr.mask, id2distance[robot]);
        }

        for (int robot = 0; robot < 4; ++robot) {
            for (int i = 0; i < 26; ++i) {
                if (id2distance[robot][i] == -1) continue;
                if (curr.mask & (1 << i)) continue;

                
                State nexState = curr;
                nexState.idList[robot] = i;
                nexState.mask |= 1 << i;
                
                int nexCost = currCost + id2distance[robot][i];

                if (!cost.count(nexState) || cost[nexState] > nexCost) {
                    cost[nexState] = nexCost;
                    Q.push(make_pair(nexCost, nexState));
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
