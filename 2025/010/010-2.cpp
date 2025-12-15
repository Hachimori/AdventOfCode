#include<bits/stdc++.h>
using namespace std;
const int INF = 1 << 20;


class Machine {
public:
    string light;
    vector<vector<int>> ops;
    vector<int> requirements;
};


vector<Machine> machines;

void read() {
    string line;
    while (getline(cin, line)) {
        Machine machine;
        stringstream ss(line);

        string s;
        ss >> s;

        machine.light = s.substr(1, s.size() - 2);

        while (ss >> s) {
            bool isOp = s[0] == '(';
            for (int i = 0; i < s.size(); ++i) {
                if (!isdigit(s[i])) {
                    s[i] = ' ';
                }
            }
            stringstream innerSS(s);
            int v;
            vector<int> vList;
            while (innerSS >> v) {
                vList.push_back(v);
            }
            if (isOp) {
                machine.ops.push_back(vList);
            } else {
                machine.requirements = vList;
                break;
            }
        }

        machines.push_back(machine);
    }
}


int calc(vector<int> &curr, vector<pair<int, vector<int>>> &combinedOps) {
    if (curr == vector<int>(curr.size(), 0)) {
        return 0;
    }

    int minV = INF;

    for (auto &combinedOp : combinedOps) {
        vector<int> next = curr;
        for (int i = 0; i < next.size(); ++i) {
            next[i] -= combinedOp.second[i];

            if (next[i] < 0 || next[i] % 2 == 1) {
                goto _fail;
            }
        }

        for (int i = 0; i < next.size(); ++i) {
            next[i] /= 2;
        }

        minV = min(minV, calc(next, combinedOps) * 2 + combinedOp.first);

        _fail:;
    }

    return minV;
}


vector<pair<int, vector<int>>> createCombinedOps(int n, vector<vector<int>> ops) {
    vector<pair<int, vector<int>>> ret;
    for (int mask = 0; mask < (1 << ops.size()); ++mask) {
        vector<int> combionedOp(n, 0);
        for (int i = 0; i < ops.size(); ++i) {
            if (mask & (1 << i)) {
                for (int v : ops[i]) {
                    ++combionedOp[v];
                }
            }
        }
        ret.push_back({__builtin_popcount(mask), combionedOp});
    }
    return ret;
}


void work() {
    long long ans = 0;
    for (Machine &machine : machines) {
        vector<pair<int, vector<int>>> combinedOps = createCombinedOps(machine.requirements.size(), machine.ops);

        int v = calc(machine.requirements, combinedOps);
        ans += v;
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
