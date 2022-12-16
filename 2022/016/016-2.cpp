#include<bits/stdc++.h>
using namespace std;
const int INF = 1 << 29;


class State {
public:
    int remain;
    int turn;
    int cur;
    long long openedNodes;

    State(){}
    State(int remain, int turn, int cur, long long openedNodes):
        remain(remain), turn(turn), cur(cur), openedNodes(openedNodes) {}

    bool operator< (const State &opp) const {
        if (remain != opp.remain) return remain < opp.remain;
        if (turn != opp.turn) return turn < opp.turn;
        if (cur != opp.cur) return cur < opp.cur;
        return openedNodes < opp.openedNodes;
    }
};

class StrInfo {
public:
    int flowRate;
    vector<string> adjStr;

    StrInfo(){}
    StrInfo(int flowRate, vector<string> &adjStr):
        flowRate(flowRate), adjStr(adjStr) {}
};


map<string, StrInfo> str2strInfo;

void read() {
    string line;
    while (getline(cin, line)) {
        for (int i = 0; i < line.size(); ++i) {
            if (i == 0 || !(isupper(line[i])|| isdigit(line[i]))) {
                line[i] = ' ';
            }
        }

        stringstream in(line);
        string node;
        int flowRate;
        in >> node >> flowRate;

        string adj;
        vector<string> nodes;
        while (in >> adj) {
            nodes.emplace_back(adj);
        }

        str2strInfo[node] = StrInfo(flowRate, nodes);
    }
}


map<string, int> getStr2id() {
    map<string, int> str2id;
    for (auto & [str, _] : str2strInfo) {
        int nId = str2id.size();
        str2id[str] = nId;
    }
    return str2id;
}


vector<vector<int>> getNode2nodeDist(map<string, int> &str2id) {
    int nNode = str2id.size();
    vector<vector<int>> node2nodeDist(nNode, vector<int>(nNode, INF));

    for (auto & [str, strInfo] : str2strInfo) {
        node2nodeDist[str2id[str]][str2id[str]] = 0;
        for (string &adjS : strInfo.adjStr) {
            node2nodeDist[str2id[str]][str2id[adjS]] = 1;
        }
    }

    for (int k = 0; k < nNode; ++k) {
        for (int i = 0; i < nNode; ++i) {
            for (int j = 0; j < nNode; ++j) {
                node2nodeDist[i][j] = min(node2nodeDist[i][j], node2nodeDist[i][k] + node2nodeDist[k][j]);
            }
        }
    }

    return node2nodeDist;
}


vector<int> getFlowRate(map<string, int> &str2id) {
    vector<int> flowRate(str2id.size());
    for (auto & [str, id] : str2id) {
        flowRate[id] = str2strInfo[str].flowRate;
    }
    return flowRate;
}


int rec(int remain, int turn, int cur, long long opened, map<State, int> &dp, vector<vector<int>> &node2nodeDist, vector<int> &flowRate, int initID) {
    State state = State(remain, turn, cur, opened);
    if (dp.count(state)) {
        return dp[state];
    }
    // cout << remain << ' ' << turn << ' ' << cur << ' ' << opened << endl;
    int ret = 0;

    // Move to adjacent node, and open valve
    const int nNode = flowRate.size();
    for (int i = 0; i < nNode; ++i) {;
        if (flowRate[i] == 0) continue;
        if (remain - node2nodeDist[cur][i] - 1 < 0) continue;
        if (opened & (1LL << i)) continue;
        ret = max(ret, rec(remain - node2nodeDist[cur][i] - 1, turn, i, opened | (1LL << i), dp, node2nodeDist, flowRate, initID) + (remain - node2nodeDist[cur][i] - 1) * flowRate[i]);
    }

    if (turn == 0) {
        // Human finishes moving, let elephant move
        ret = max(ret, rec(26, 1, initID, opened, dp, node2nodeDist, flowRate, initID));
    }

    return dp[state] = ret;
}

void work() {
    map<string, int> str2id = getStr2id();
    vector<vector<int>> node2nodeDist = getNode2nodeDist(str2id);
    vector<int> flowRate = getFlowRate(str2id);

    map<State, int> dp;
    cout << rec(26, 0, str2id["AA"], 0, dp, node2nodeDist, flowRate, str2id["AA"]) << endl;
}


int main() {
    read();
    work();
    return 0;
}
