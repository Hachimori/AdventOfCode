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


long long rec(bool hasFft, bool hasDac, int cur, long long dp[2][2][1000]) {
    if (cur == name2id["out"]) return hasFft && hasDac;

    long long &ret = dp[hasFft][hasDac][cur];
    if (ret != -1) return ret;

    ret = 0;
    for (int nex : adj[cur]) {
        ret += rec(
            hasFft | (nex == name2id["fft"]),
            hasDac | (nex == name2id["dac"]),
            nex,
            dp
        );
    }
    return ret;
}


void work() {
    long long dp[2][2][1000];
    memset(dp, -1, sizeof(dp));
    cout << rec(0, 0, name2id["svr"], dp) << endl;
}


int main() {
    read();
    work();
    return 0;
}
