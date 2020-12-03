#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<queue>
#include<cctype>
#define id first
#define mask second
#define r first
#define c second
using namespace std;
const int SIZE = 100;
const int NODE = 30;
typedef pair<int, int> State;
typedef pair<int, int> Point;


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

    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            if (b[i][j] == '@') {
                id2pt[26] = Point(i, j);
            } else if (islower(b[i][j])) {
                id2pt[b[i][j] - 'a'] = Point(i, j);
            }
        }
    }
}


void bfs(State &init, int id2distance[NODE]) {
    int cost[SIZE][SIZE];
    queue<Point> Q;

    memset(cost, -1, sizeof(cost));
    
    Q.push(id2pt[init.id]);
    cost[id2pt[init.id].r][id2pt[init.id].c] = 0;

    while (!Q.empty()) {
        Point curr = Q.front();
        Q.pop();

        static int dr[] = {-1, 0, 1, 0};
        static int dc[] = {0, -1, 0, 1};
        for (int i = 0; i < 4; ++i) {
            int nr = curr.r + dr[i];
            int nc = curr.c + dc[i];
            if (b[nr][nc] == '#') continue;
            if (isupper(b[nr][nc]) && !(init.mask & (1 << (b[nr][nc] - 'A')))) continue;
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

    Q.push(make_pair(0, State(26, 0)));
    cost[State(26, 0)] = 0;

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
        
        int id2distance[NODE];
        memset(id2distance, -1, sizeof(id2distance));

        bfs(curr, id2distance);

        for (int i = 0; i < 26; ++i) {
            if (id2distance[i] == -1) continue;
            if (curr.mask & (1 << i)) continue;
            
            State nexState = State(i, curr.mask | (1 << i));
            int nexCost = currCost + id2distance[i];

            if (!cost.count(nexState) || cost[nexState] > nexCost) {
                cost[nexState] = nexCost;
                Q.push(make_pair(nexCost, nexState));
            }
        }
    }
}


int main() {
    read();
    work();
    return 0;
}
