#include<bits/stdc++.h>
using namespace std;

map<string, int> name2id;
vector<vector<int>> adj;

void read() {
    string line;
    while (getline(cin, line)) {
        for (int i = 0; i < line.size(); i++) {
            if (line[i] == ':') {
                line[i] = ' ';
            }
        }

        auto getId = [](string name) {
            if (!name2id.count(name)) {
                adj.push_back({});
                int id = name2id.size();
                name2id[name] = id;
            }
            return name2id[name];
        };

        stringstream ss(line);
        string src, dst;
        ss >> src;
        while (ss >> dst) {
            int id1 = getId(src);
            int id2 = getId(dst);
            adj[id1].push_back(id2);
        }
    }
}


long long rec(int cur, vector<long long> &dp) {
    if (cur == name2id["out"]) return 1;

    long long &ret = dp[cur];
    if (ret != -1) return ret;

    ret = 0;
    for (int nex : adj[cur]) {
        ret += rec(nex, dp);
    }
    return ret;
}


void work() {
    int n = adj.size();
    vector<long long> dp(n, -1);
    cout << rec(name2id["you"], dp) << endl;
}


int main() {
    read();
    work();
    return 0;
}
