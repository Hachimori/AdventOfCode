#include<bits/stdc++.h>
using namespace std;
const int BUF = 2005;
const int INF = 1 << 30;


class Edge {
public:
    int dst, cap;
    Edge *revEdge;

    Edge(int dst, int cap): dst(dst), cap(cap), revEdge(NULL) {}
};


int nNode, SRC, DST;
vector<Edge*> adj[BUF];

void addEdge(int s, int t, int capST, int capTS) {
    adj[s].push_back(new Edge(t, capST));
    adj[t].push_back(new Edge(s, capTS));
    adj[s].back()->revEdge = adj[t].back();
    adj[t].back()->revEdge = adj[s].back();
}


void bfs(int level[BUF]) {
    queue<int> Q;

    level[SRC] = 0;
    Q.push(SRC);

    while (!Q.empty()) {
        int curr = Q.front();
        Q.pop();

        for (int i = 0; i < adj[curr].size(); ++i) {
            Edge &e = *adj[curr][i];
            if (e.cap == 0 || level[e.dst] != -1) continue;
            level[e.dst] = level[curr] + 1;
            Q.push(e.dst);
        }
    }
}


int dfs(int curr, int flow, int iter[BUF], int level[BUF]) {
    if (curr == DST) return flow;
    for (int &i = iter[curr]; i < adj[curr].size(); ++i) {
        Edge &e = *adj[curr][i];
        if (e.cap == 0) continue;
        if (level[e.dst] <= level[curr]) continue;
        if (int f = dfs(e.dst, min(flow, e.cap), iter, level)) {
            e.cap -= f;
            e.revEdge->cap += f;
            return f;
        }
    }
    return 0;
}


int dinic() {
    int sum = 0;

    int level[BUF];
    int iter[BUF];
    while (1) {
        memset(level, -1, sizeof(level));
        bfs(level);

        if (level[DST] == -1) break;

        memset(iter, 0, sizeof(iter));
        while (int f = dfs(SRC, INF, iter, level)) {
            sum += f;
        }
    }

    return sum;
}


map<string, int> node2idx;
map<int, vector<int>> edgeList;

void add(string &a, string &b) {
    if (!node2idx.count(a)) {
        int id = node2idx.size();
        node2idx[a] = id;
    }
    if (!node2idx.count(b)) {
        int id = node2idx.size();
        node2idx[b] = id;
    }
    edgeList[node2idx[a]].emplace_back(node2idx[b]);
}


void read() {
    string line;
    while (getline(cin, line)) {
        stringstream in(line);
        string name, opp;

        in >> name;
        name.pop_back(); // remove ':'

        while (in >> opp) {
            add(name, opp);
        }
    }
}


int bfs() {
    queue<int> Q;
    bool visited[BUF] = {};

    int cnt = 0;
    Q.push(SRC);
    visited[SRC] = true;

    while (!Q.empty()) {
        int cur = Q.front();
        Q.pop();

        ++cnt;
        for (Edge *e : adj[cur]) {
            if (e->cap == 0) continue;
            if (visited[e->dst]) continue;
            visited[e->dst] = true;
            Q.push(e->dst);
        }
    }

    return cnt;
}


void work() {
    for (int goal = 1; goal < edgeList.size(); ++goal) {
        nNode = node2idx.size() + 2;
        SRC = node2idx.size();
        DST = node2idx.size() + 1;

        for (int i = 0; i < nNode; ++i) {
            adj[i].clear();
        }

        addEdge(SRC, 0, 100, 0);
        for (auto stList : edgeList) {
            for (int t : stList.second) {
                addEdge(stList.first, t, 1, 1);
            }
        }
        addEdge(goal, DST, 100, 0);

        if (dinic() == 3) {
            break;
        }
    }


    int t = bfs() - 1;
    cout << 1LL * t * (node2idx.size() - t) << endl;
}


int main() {
    read();
    work();
    return 0;
}
